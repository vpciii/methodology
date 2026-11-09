#!/usr/bin/env python3
"""Tests for `claude_review.py` and the workflows around it
(specs/claude-review-agent-sdk/, SC-1 to SC-9). Ported from
nurturepa/cif's scripts/ci/test-claude-review.py.

The SDK is never imported: `main` takes a `runner` stand-in for the agent,
and SDK messages are stubbed with SimpleNamespace. So these run with plain
python3 — no packages, no network, no API key.

Usage:
    test_claude_review.py

Exits 0 if every test passes, 1 otherwise.
"""

import contextlib
import io
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
WORKFLOWS = REPO_ROOT / ".github" / "workflows"
REUSABLE = WORKFLOWS / "claude-review.yml"
SELF_CALLER = WORKFLOWS / "pr-review.yml"
TEMPLATE = REPO_ROOT / "templates" / "github" / "claude-review.yml"
CI = WORKFLOWS / "ci.yml"

sys.path.insert(0, str(HERE))
import claude_review as cr  # noqa: E402

MODEL_1M = "claude-opus-5[1m]"


def good_result(text="Looks fine.", window=1_000_000):
    return SimpleNamespace(
        subtype="success", is_error=False, result=text, errors=None,
        total_cost_usd=1.23,
        model_usage={"claude-opus-5-5": {"contextWindow": window}})


class SystemMessage:
    """Stand-in for the SDK's SystemMessage."""

    def __init__(self, subtype, data):
        self.subtype = subtype
        self.data = data


class ResultMessage(SimpleNamespace):
    """Stand-in for the SDK's ResultMessage."""


def as_result(namespace):
    return ResultMessage(**vars(namespace))


def feed_all(messages, model=MODEL_1M):
    """Drive cr.StreamCheck over stub messages, as run_review does."""
    check = cr.StreamCheck(SystemMessage, ResultMessage, model)
    for message in messages:
        check.feed(message)
    return check.finish()


def write_event(tmp):
    path = Path(tmp) / "event.json"
    path.write_text(json.dumps({"pull_request": {
        "number": 1, "title": "t", "body": "b",
        "base": {"ref": "main"}, "head": {"ref": "x"}}}),
        encoding="utf-8")
    return path


@contextlib.contextmanager
def api_key(value):
    old = os.environ.get("ANTHROPIC_API_KEY")
    if value is None:
        os.environ.pop("ANTHROPIC_API_KEY", None)
    else:
        os.environ["ANTHROPIC_API_KEY"] = value
    try:
        yield
    finally:
        if old is None:
            os.environ.pop("ANTHROPIC_API_KEY", None)
        else:
            os.environ["ANTHROPIC_API_KEY"] = old


def run_main(runner, key="test-key", diff="diff --git a/x b/x\n",
             model=MODEL_1M, extra=()):
    """Run main() against this repo's checkout with a stub runner and a
    stubbed diff; return (exit code, review text or None, stdout)."""
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "review.md"
        argv = ["--model", model, "--repo", str(REPO_ROOT),
                "--docs", "README.md methodology.md",
                "--event", str(write_event(tmp)), "--out", str(out),
                *extra]
        real_read_diff = cr.read_diff
        cr.read_diff = lambda root: diff
        stdout = io.StringIO()
        try:
            with api_key(key), contextlib.redirect_stderr(io.StringIO()), \
                    contextlib.redirect_stdout(stdout):
                code = cr.main(argv, runner=runner)
        finally:
            cr.read_diff = real_read_diff
        text = out.read_text(encoding="utf-8") if out.exists() else None
        return code, text, stdout.getvalue()


def test_options_are_locked_down():
    """SC-1: the agent's options fix its tools, isolation and caps, and
    the caps are the ones the caller passed."""
    opts = cr.build_options(MODEL_1M, REPO_ROOT)
    assert opts["tools"] == ["Read", "Grep", "Glob"], opts["tools"]
    assert opts["setting_sources"] == [], opts["setting_sources"]
    assert opts["strict_mcp_config"] is True
    assert opts["mcp_servers"] == {}
    assert opts["permission_mode"] == "dontAsk"
    assert opts["max_turns"] == cr.DEFAULT_MAX_TURNS == 40
    assert opts["max_budget_usd"] == cr.DEFAULT_MAX_BUDGET_USD == 3.00
    assert set(opts["allowed_tools"]) <= set(opts["tools"])

    seen = {}

    def capture(prompt, options):
        seen.update(options)
        return cr.check_result(good_result(), MODEL_1M)

    code, _, _ = run_main(capture, extra=["--max-turns", "7",
                                          "--max-budget-usd", "0.5"])
    assert code == 0, code
    assert seen["max_turns"] == 7 and seen["max_budget_usd"] == 0.5, seen


def test_success_writes_review():
    """SC-2: a successful, non-empty result is written, exits 0, and
    prints its cost."""
    code, text, stdout = run_main(
        lambda p, o: cr.check_result(good_result("Ship it."), MODEL_1M))
    assert code == 0, code
    assert text == "Ship it.\n", repr(text)
    assert "total_cost_usd=1.23" in stdout, stdout


def test_failures_exit_nonzero():
    """SC-3: error subtypes, cap hits, SDK exceptions and empty text all
    exit non-zero with no review written."""
    failures = {
        "error subtype": SimpleNamespace(subtype="error_during_execution",
                                         is_error=True, result=None),
        "turn cap": SimpleNamespace(subtype="error_max_turns", is_error=True),
        "budget cap": SimpleNamespace(subtype="error_max_budget_usd",
                                      is_error=True),
        "empty text": good_result(text="   "),
    }
    for label, message in failures.items():
        code, text, _ = run_main(
            lambda p, o, m=message: cr.check_result(m, MODEL_1M))
        assert code != 0, label
        assert text is None, label

    def sdk_raises(prompt, options):
        raise RuntimeError("CLI process exited with code 1")

    code, text, _ = run_main(sdk_raises)
    assert code != 0 and text is None, "SDK exception"


def test_requires_api_key():
    """SC-4: no ANTHROPIC_API_KEY means no run, before any SDK call."""
    called = []
    code, text, _ = run_main(lambda p, o: called.append(1), key=None)
    assert code != 0 and text is None
    assert called == [], "runner was called without a key"


def step_blocks(text):
    """Split a workflow's steps on their `- name:` lines."""
    return re.split(r"\n      - name: ", text)[1:]


def test_workflow_shape():
    """SC-5: the reusable workflow's inputs, skip rule, model and SDK
    pins, the API key only in the review step and the GitHub token only
    in the posting step; the callers' triggers."""
    text = REUSABLE.read_text(encoding="utf-8")
    assert "workflow_call:" in text
    for name in ("model", "max_turns", "max_budget_usd", "project_docs",
                 "reviewer_ref"):
        assert re.search(r"\n      %s:\n" % name, text), "input %s" % name
    assert 'default: "claude-opus-5[1m]"' in text
    assert "claude_args" not in text
    assert "github.event.pull_request.draft == false" in text
    assert "!contains(github.event.pull_request.title, '[skip-review]')" in text
    assert re.search(r"claude-agent-sdk==\d+\.\d+\.\d+\b", text), "SDK not pinned exactly"
    assert "anthropics/claude-code-action" not in text
    assert "id-token" not in text
    assert text.count("persist-credentials: false") == 2

    steps = step_blocks(text)
    token_steps = [s.splitlines()[0] for s in steps
                   if "github.token" in s or "GITHUB_TOKEN" in s]
    assert token_steps == ["Post review"], token_steps
    key_steps = [s.splitlines()[0] for s in steps
                 if "anthropic_api_key" in s or "ANTHROPIC_API_KEY" in s]
    assert key_steps == ["Run Claude review"], key_steps

    for caller in (SELF_CALLER, TEMPLATE):
        body = caller.read_text(encoding="utf-8")
        assert "types: [opened, ready_for_review]" in body, caller.name
        assert "id-token" not in body, caller.name
        assert "claude-review.yml" in body, caller.name
    # R-15: the template's prerequisites and its billing caveat.
    template = TEMPLATE.read_text(encoding="utf-8")
    assert "apps/claude" not in template, "GitHub App prerequisite is back"
    assert "promotional API credit" in template, "billing caveat missing"
    assert "reviewer_ref" in template, "template does not mention reviewer_ref"
    # The script's ref: present, defaulting to main (spec, Open questions).
    assert re.search(r'\n      reviewer_ref:\n(.*\n)*?        default: "main"\n',
                     text), "reviewer_ref default"


def test_prompt_includes_project_docs():
    """SC-6: every listed doc that exists is in the prompt in full,
    missing ones are skipped, and none existing fails the run."""
    docs = cr.read_project_docs(REPO_ROOT,
                                ["README.md", "no-such.md", "methodology.md"])
    assert [rel for rel, _ in docs] == ["README.md", "methodology.md"]
    pr = {"number": 1, "title": "t", "body": "", "base": "b", "head": "h"}
    prompt = cr.build_prompt(docs, pr, "diff")
    for rel in ("README.md", "methodology.md"):
        full = (REPO_ROOT / rel).read_text(encoding="utf-8")
        assert full in prompt, rel

    with tempfile.TemporaryDirectory() as tmp:
        try:
            cr.read_project_docs(tmp)
        except cr.ReviewFailed:
            pass
        else:
            raise AssertionError("no docs at all did not fail")


def test_unexpected_tools_abort():
    """SC-7: a session that starts with any other tool list, or never
    reports one, aborts before a review is written."""
    cr.check_init({"tools": ["Glob", "Grep", "Read"]})  # order-insensitive
    for tools in (["Read", "Grep", "Glob", "Bash"], ["Read", "Grep"], None):
        try:
            cr.check_init({"tools": tools})
        except cr.ReviewFailed:
            pass
        else:
            raise AssertionError("tools %r were accepted" % (tools,))

    def starts_with_bash(prompt, options):
        cr.check_init({"tools": ["Read", "Grep", "Glob", "Bash"]})
        return cr.check_result(good_result(), MODEL_1M)

    code, text, _ = run_main(starts_with_bash)
    assert code != 0 and text is None

    good_init = SystemMessage("init", {"tools": ["Read", "Grep", "Glob"]})
    streams = {
        "no init message": [SystemMessage("other", {}), as_result(good_result())],
        "result before init": [as_result(good_result()), good_init],
        "init with Bash": [SystemMessage("init", {"tools": ["Read", "Grep",
                                                             "Glob", "Bash"]}),
                           as_result(good_result())],
        "no result": [good_init],
    }
    for label, stream in streams.items():
        try:
            feed_all(stream)
        except cr.ReviewFailed:
            pass
        else:
            raise AssertionError("stream %r was accepted" % label)
    assert feed_all([good_init, as_result(good_result("ok"))])[0] == "ok"


def test_long_diff_is_cut_on_a_line_with_file_list():
    """A diff over MAX_DIFF_CHARS is cut on a line boundary, and the note
    names every file the PR changes (a cost guard carried over from cif)."""
    short = "diff --git a/x b/x\n+one\n"
    assert cr.truncate_diff(short) == short

    block = "diff --git a/f%d b/f%d\n" + ("+" + "y" * 99 + "\n") * 50
    diff = "".join(block % (i, i) for i in range(200))
    assert len(diff) > cr.MAX_DIFF_CHARS
    out = cr.truncate_diff(diff)
    head, note = out.split("\n\n[diff truncated", 1)
    assert diff.startswith(head + "\n"), "not cut on a line boundary"
    assert len(head) <= cr.MAX_DIFF_CHARS
    assert "f0" in note and "f199" in note, "file list missing from note"
    assert "200 file(s)" in note


def test_small_context_window_fails():
    """SC-8: with a [1m] model, a window under 1M fails the run; without
    the suffix the window is not checked."""
    code, text, _ = run_main(
        lambda p, o: cr.check_result(good_result(window=200_000), MODEL_1M))
    assert code != 0 and text is None

    model = "claude-sonnet-5-5"
    code, text, _ = run_main(
        lambda p, o: cr.check_result(good_result("ok", window=200_000), model),
        model=model)
    assert code == 0 and text == "ok\n", (code, text)


def test_ci_runs_reviewer_tests_and_coverage():
    """SC-9: this repo's CI runs these tests and the spec coverage check
    on every pull request."""
    text = CI.read_text(encoding="utf-8")
    assert re.search(r"^on:\n(  \w+:.*\n)*  pull_request:", text, re.M), \
        "CI does not run on pull requests"
    assert "python .github/claude-review/test_claude_review.py" in text
    assert "python templates/ci/check-spec-coverage.py" in text


TESTS = [
    test_options_are_locked_down,
    test_success_writes_review,
    test_failures_exit_nonzero,
    test_requires_api_key,
    test_workflow_shape,
    test_prompt_includes_project_docs,
    test_unexpected_tools_abort,
    test_long_diff_is_cut_on_a_line_with_file_list,
    test_small_context_window_fails,
    test_ci_runs_reviewer_tests_and_coverage,
]


def main():
    failures = 0
    for test in TESTS:
        try:
            test()
        except Exception as exc:  # report every failure, not just the first
            failures += 1
            print("FAIL  %s: %s: %s" % (test.__name__, type(exc).__name__, exc))
        else:
            print("PASS  %s" % test.__name__)
    print()
    if failures:
        print("%d of %d test(s) FAILED." % (failures, len(TESTS)))
        return 1
    print("All %d test(s) pass." % len(TESTS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
