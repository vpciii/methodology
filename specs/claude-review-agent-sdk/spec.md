# Spec: The shared Claude PR reviewer runs on the Agent SDK

- **Status:** Implemented
- **Date:** 2026-11-09
- **Author:** vpc (author of record); drafted with Claude
- **Related ADRs:** ADR 0026 (this decision, proposed), ADR 0021 (the
  shared reviewer), ADR 0024 (compact spec), ADR 0003 (dependencies)

> Compact spec (ADR 0024): the Approach and Rollout sections below
> replace `plan.md` / `tasks.md`. It ports nurturepa/cif's
> `specs/claude-review-agent-sdk/` (Implemented 2026-11-09, PR #140) to
> the shared, reusable reviewer; that spec, its script and its tests are
> the reference implementation.

## Problem

The shared reviewer (`.github/workflows/claude-review.yml`, ADR 0021)
runs `anthropics/claude-code-action@v1`, which drives the Claude Code
CLI. The Anthropic Console bills that traffic as **Claude Code**. The
Max plan's $100 monthly promotional API credit covers *Agent SDK, API,
Batch API, Playground, Managed Agents* — not Claude Code — so every
review spends purchased credit while the promotional credit expires
unused. When purchased credit ran out (2026-10-25, in cif), reviews
failed until it was topped up.

cif moved its own reviewer off the action on 2026-11-09 and confirmed
the Agent SDK draws on the promotional credit (cif spec, Decisions).
The shared reviewer — this repo's own PRs today, and any project that
adopts the template — is still on the action. Running two reviewer
implementations also means two prompts and two failure-handling paths
to keep in step, which is the drift ADR 0021 exists to prevent.

## Goals

1. A review run through the shared reviewer is billed as Agent SDK
   traffic, so a caller whose key belongs to an org with the
   promotional credit spends that credit, not purchased credit.
2. Review scope is unchanged: same trigger and skip rules, same pinned
   default model, the same methodology-aware review criteria, still
   advisory (never a merge gate).
3. A review that did not run is a red check, never a green one.
4. The agent's reach on the runner is no wider than the review needs.
5. Adopting stays a thin caller workflow plus one secret — and gets
   simpler: no Claude GitHub App install, no `id-token: write`.

## Non-goals

- Porting any `@claude` mention responder. This repo has none; projects
  that have one keep it on the action.
- Making the review a required check, or re-reviewing on `synchronize`.
- Inline (line-anchored) comments: one summary comment per run.
- Migrating cif onto the shared reviewer. cif is owned by a different
  account (`nurturepa-vpc`) and cannot call this reusable workflow
  across accounts (template, prerequisite 3); it keeps its standalone
  copy.

## Requirements

- **R-1 (MUST)** The review runs through the Claude Agent SDK,
  authenticated only with the caller-supplied `anthropic_api_key`
  secret.
- **R-2 (MUST)** The agent runs isolated from filesystem settings
  (`setting_sources=[]`), with no MCP servers (`strict_mcp_config`, no
  `mcp_servers`).
- **R-3 (MUST)** The agent's tools are exactly `Read`, `Grep`, `Glob`,
  with `permission_mode="dontAsk"`: no shell, no write, no network, no
  GitHub access.
- **R-4 (MUST)** The agent never posts to GitHub. A separate step posts
  its final text as one PR comment with the job's `GITHUB_TOKEN`, and no
  other step receives that token.
- **R-5 (MUST)** The job fails when the agent did not produce a
  successful result: an SDK error, an error result subtype (including
  `error_max_turns`, `error_max_budget_usd`), or empty review text.
- **R-6 (MUST)** Each run is capped by `max_turns` and `max_budget_usd`,
  with defaults in the reusable workflow and per-caller overrides.
- **R-7 (MUST)** The default model stays pinned in the reusable workflow
  (`claude-opus-5[1m]`), overridable per caller by the `model` input.
- **R-8 (MUST)** Trigger and skip rules are unchanged: callers trigger
  on `opened` and `ready_for_review`; drafts and `[skip-review]` titles
  skip.
- **R-9 (MUST)** The SDK version is pinned exactly (which pins the CLI
  it bundles).
- **R-10 (MUST)** The run logs `total_cost_usd`.
- **R-11 (MUST)** The script inlines the caller's governing docs in the
  prompt, because `setting_sources=[]` stops the SDK auto-loading
  `CLAUDE.md`. The list is a caller input with a default; each listed
  file that exists is inlined; the run fails if none exists.
- **R-12 (MUST)** The script checks the tool list the CLI reports at
  session start and fails closed if it is not exactly `Read`, `Grep`,
  `Glob`, or if no session-start report arrives before the result.
- **R-13 (MUST)** When the model ends in `[1m]`, the run fails if the
  result reports a context window under 1,000,000 tokens, so a silently
  dropped suffix is a red check.
- **R-14 (MUST)** The script and its tests live in this repo and run in
  this repo's CI on every PR, so a change that breaks the reviewer fails
  a deterministic check before the broken reviewer reviews anything.
- **R-15 (MUST)** The caller template and ADR trail are updated in the
  same PR: the template drops the GitHub App prerequisite and
  `id-token: write`, and says the credit benefit depends on whose org
  the key belongs to.

## Success criteria

- **SC-1** — The options the script builds have `tools ==
  ["Read","Grep","Glob"]`, `setting_sources == []`, `strict_mcp_config`
  true, no `mcp_servers`, `permission_mode == "dontAsk"`, and the
  `max_turns` / `max_budget_usd` it was given. (R-2, R-3, R-6)
- **SC-2** — A successful result with non-empty text is written to the
  output file and the script exits 0, printing `total_cost_usd`.
  (R-4, R-10)
- **SC-3** — An error subtype, a cap hit, an SDK exception, or empty
  text exits non-zero and writes no output. (R-5)
- **SC-4** — With `ANTHROPIC_API_KEY` unset the script exits non-zero
  before any SDK call. (R-1)
- **SC-5** — In the reusable workflow: `workflow_call` with `model`
  (default `claude-opus-5[1m]`), `max_turns`, `max_budget_usd` and
  `project_docs` inputs; the draft/`[skip-review]` condition; the exact
  `claude-agent-sdk==` pin; no `claude-code-action`; no `id-token`;
  `GITHUB_TOKEN` passed only to the posting step; the API key only to
  the review step. This repo's caller and the template trigger on
  `opened`/`ready_for_review` only. (R-4, R-6, R-7, R-8, R-9, R-15)
- **SC-6** — The prompt contains the full text of every listed doc that
  exists, skips listed docs that don't, and the script fails when none
  exists. (R-11)
- **SC-7** — A session-start tool list with an extra or missing tool, or
  a stream whose result arrives with no session-start report, exits
  non-zero with no output. (R-12)
- **SC-8** — With a `[1m]` model, a result reporting a window under
  1,000,000 tokens fails; without the suffix the window is not checked.
  (R-13)
- **SC-9** — This repo's CI runs the reviewer's tests and the spec
  coverage check on every PR. (R-14)

## Approach

Port cif's `scripts/ci/claude-review.py` and `test-claude-review.py`,
generalized for a reusable workflow:

1. **Where the code lives.** `.github/claude-review/claude_review.py`
   and `test_claude_review.py` in this repo (public, so any caller can
   check it out without a token).
2. **Reusable workflow** (`.github/workflows/claude-review.yml`, same
   path, so callers' `uses:` lines don't change):
   checkout the *caller's* repo (`fetch-depth: 2`,
   `persist-credentials: false`); checkout `vpciii/methodology` at input
   `reviewer_ref` (default `main`) into `$RUNNER_TEMP`; `setup-python`;
   `pip install claude-agent-sdk==<exact>` (cif: `0.2.179`); run the
   script with `ANTHROPIC_API_KEY` only; post with `gh pr comment
   --body-file` and `GITHUB_TOKEN` only. Inputs: `model`, `max_turns`
   (40), `max_budget_usd` (3.00), `project_docs`, `reviewer_ref`.
   `claude_args` is removed (it was CLI passthrough to the action; no
   caller uses it).
3. **Prompt.** The current reusable prompt's criteria (correctness,
   off-contract, process drift), moved into the script, plus cif's
   system prompt that treats all PR content as material, not
   instructions. Diff from `git diff HEAD^1 HEAD` on the merge commit,
   PR metadata from the event payload, 400,000-character diff cut with a
   changed-file list (as in cif).
4. **Project docs default:** `CLAUDE.md AGENTS.md CONTRIBUTING.md
   docs/glossary.md docs/conventions.md docs/architecture.md`. This
   repo's own caller passes `README.md methodology.md` (≈37 KB).
5. **This repo's CI.** A new `.github/workflows/ci.yml` running
   `python .github/claude-review/test_claude_review.py` and
   `templates/ci/check-spec-coverage.py` over `specs/` — this repo's
   first deterministic check.
6. **Dogfooding.** `pr-review.yml` passes `reviewer_ref:
   ${{ github.event.pull_request.head.sha }}`, so a PR here that edits
   the script is reviewed by its own copy (the same exposure as today:
   only the owner pushes branches; fork PRs get no secrets, and the
   script refuses to run, red).
7. **Docs in the same PR:** template header and prerequisites; ADR 0026
   → Accepted; ADR 0021 status line notes the partial supersession
   (body unchanged, append-only); CHANGELOG; this spec → Implemented
   with Traceability filled.

**Trust boundary.** Unchanged from today and from cif: the caller's key
reaches the PR branch's workflow for same-repo branches. New surface is
prompt injection through PR content, bounded by R-3/R-4: the agent can
only read and emit text; the key is in the process environment, not its
context; the job token is never on disk where `Read` could find it.
Comments are posted as `github-actions[bot]`, which also means an
injected `@claude` in review text cannot trigger another workflow.

**What goes away:** the OIDC skip-as-green path and its `Fail if the
review never ran` step (R-5 replaces it), `track_progress`'s live
comment, and the long header explaining the action's skip behavior.

### Decisions

- *2026-11-09* — Port from cif rather than redesign: cif's version has
  run live, with its billing verified on the Billing page (the Console's
  "Claude Code usage" analytics counts SDK runs as Claude Code anyway).
- *2026-11-09* — Approved by vpc with the three open questions resolved
  as proposed.
- *2026-11-09* — As built: the tests are ten plain-python functions (the
  nine criteria plus cif's long-diff cost guard), run by the new
  `.github/workflows/ci.yml`. The SC-5 test also forbids the strings
  `claude-code-action` and `id-token` anywhere in the reusable workflow,
  this repo's caller and the template, comments included, so the old
  runner cannot come back unnoticed.
- *2026-11-09* — Billing check (Rollout) is still to be recorded: it
  needs the implementation PR's own review run. It is a manual check,
  not a criterion, so it is recorded in the PR and CHANGELOG rather than
  here once this spec is frozen.

## Rollout and undo

Two PRs: this spec + ADR 0026 (Proposed) for sign-off, then the
implementation. The implementation PR's own review runs through the new
reviewer at its head sha (Approach 6), so read its log and cost by hand;
then check the promotional balance dropped by that `total_cost_usd`.

Callers pinned to `@main` pick up the change on merge. Today no other
repo calls the reusable workflow (checked 2026-11-09 across `vpciii`'s
repos), so the blast radius is this repo.

**Undo:** revert the implementation PR; the action-based workflow
returns as it was, with the same secret. A caller that already dropped
`id-token: write` per the new template must add it back. Nothing is
irreversible.

## Open questions

- [x] **`reviewer_ref` default.** A reusable workflow can't reliably
  name the ref it was called at, so a caller on `@v0.14.0` would still
  get `main`'s script. Accept `main` (callers today use `@main`), or
  have the template pass `reviewer_ref` explicitly alongside its `@ref`?
  Proposed: default `main`; template documents keeping the two in step.
  *Resolved 2026-11-09:* approved as proposed.
- [x] **Caps.** Same as cif: `max_turns=40`, `max_budget_usd=3.00`?
  *Resolved 2026-11-09:* approved.
- [x] **Whose key.** This repo's `ANTHROPIC_API_KEY` must be a key from
  the org that receives the Max plan's credit for Goal 1 to hold here.
  Confirm it is (or rotate it to one that is) before the implementation
  PR's billing check.
  *Resolved 2026-11-09:* approved as proposed; the implementation PR's
  billing check (Rollout) verifies it.

## Out of scope (for now)

- A tagged release of the reviewer for callers to pin (beyond `@main`).
- Folding cif back onto the shared reviewer (cross-account; see
  Non-goals).

## Traceability

| Criterion | Requirement(s) | Verified by (test) |
|---|---|---|
| SC-1 | R-2, R-3, R-6 | `.github/claude-review/test_claude_review.py::test_options_are_locked_down` |
| SC-2 | R-4, R-10 | `.github/claude-review/test_claude_review.py::test_success_writes_review` |
| SC-3 | R-5 | `.github/claude-review/test_claude_review.py::test_failures_exit_nonzero` |
| SC-4 | R-1 | `.github/claude-review/test_claude_review.py::test_requires_api_key` |
| SC-5 | R-4, R-6, R-7, R-8, R-9, R-15 | `.github/claude-review/test_claude_review.py::test_workflow_shape` |
| SC-6 | R-11 | `.github/claude-review/test_claude_review.py::test_prompt_includes_project_docs` |
| SC-7 | R-12 | `.github/claude-review/test_claude_review.py::test_unexpected_tools_abort` |
| SC-8 | R-13 | `.github/claude-review/test_claude_review.py::test_small_context_window_fails` |
| SC-9 | R-14 | `.github/claude-review/test_claude_review.py::test_ci_runs_reviewer_tests_and_coverage` |
