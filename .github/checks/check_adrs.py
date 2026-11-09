#!/usr/bin/env python3
"""Check this repo's ADR files: one number each, named and titled alike.

Fails when two files in the ADR directory share a number (two drafts
that each took "the next one"), when a file is not named
`NNNN-slug.md`, or when its first line is not `# ADR NNNN: ...` with
the same number. A pull request is checked as merged with `main`, so a
number already taken on `main` is caught before merge.

Usage:
    check_adrs.py [ADR_DIR]        (default: adr)

Exits 0 if the directory is consistent, 1 otherwise.
"""

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^(\d{4})-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")


def problems(adr_dir):
    """Return a list of human-readable problems found in adr_dir."""
    found = []
    by_number = {}
    for path in sorted(Path(adr_dir).glob("*.md")):
        match = NAME_RE.match(path.name)
        if not match:
            found.append("%s: not named NNNN-slug.md" % path.name)
            continue
        number = match.group(1)
        by_number.setdefault(number, []).append(path.name)
        lines = path.read_text(encoding="utf-8").splitlines()
        first = lines[0] if lines else ""
        if not first.startswith("# ADR %s: " % number):
            found.append("%s: first line is %r, expected '# ADR %s: ...'"
                         % (path.name, first, number))
    for number, names in sorted(by_number.items()):
        if len(names) > 1:
            found.append("ADR %s is used by %d files: %s"
                         % (number, len(names), ", ".join(names)))
    return found


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    adr_dir = args[0] if args else "adr"
    found = problems(adr_dir)
    for line in found:
        print("FAIL  %s" % line)
    if found:
        return 1
    print("PASS  %s: %d ADR(s), numbers unique"
          % (adr_dir, len(list(Path(adr_dir).glob("*.md")))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
