#!/usr/bin/env python3
"""Tests for check_adrs.py. Plain python3, no packages.

Usage:
    test_check_adrs.py

Exits 0 if every test passes, 1 otherwise.
"""

import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_adrs  # noqa: E402


def make(files):
    tmp = tempfile.mkdtemp()
    for name, first_line in files.items():
        (Path(tmp) / name).write_text(first_line + "\n", encoding="utf-8")
    return tmp


def test_consistent_directory_passes():
    tmp = make({"0001-first.md": "# ADR 0001: First",
                "0002-second-one.md": "# ADR 0002: Second"})
    assert check_adrs.problems(tmp) == []
    assert check_adrs.main([tmp]) == 0


def test_duplicate_number_fails():
    tmp = make({"0023-one-draft.md": "# ADR 0023: One",
                "0023-another-draft.md": "# ADR 0023: Another"})
    found = check_adrs.problems(tmp)
    assert len(found) == 1 and "ADR 0023 is used by 2 files" in found[0], found
    assert check_adrs.main([tmp]) == 1


def test_title_must_match_filename_number():
    tmp = make({"0004-renumbered.md": "# ADR 0003: Renumbered"})
    found = check_adrs.problems(tmp)
    assert len(found) == 1 and "expected '# ADR 0004: ...'" in found[0], found


def test_bad_filename_fails():
    tmp = make({"draft-adr.md": "# ADR 0009: Draft"})
    found = check_adrs.problems(tmp)
    assert found == ["draft-adr.md: not named NNNN-slug.md"], found


def test_this_repo_is_consistent():
    assert check_adrs.problems(HERE.parents[1] / "adr") == []


def test_ci_runs_the_check():
    ci = (HERE.parent / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert "python .github/checks/check_adrs.py" in ci
    assert "python .github/checks/test_check_adrs.py" in ci


TESTS = [test_consistent_directory_passes, test_duplicate_number_fails,
         test_title_must_match_filename_number, test_bad_filename_fails,
         test_this_repo_is_consistent, test_ci_runs_the_check]


def main():
    failures = 0
    for test in TESTS:
        try:
            test()
        except Exception as exc:
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
