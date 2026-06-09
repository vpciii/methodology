# ADR 0017: A reference implementation of the spec-coverage check

- **Status:** Accepted
- **Date:** 2026-06-09
- **Deciders:** vpc

## Context

ADR 0006 split the traceability rule in two: the id-and-table
convention is global, while the CI mechanism that enforces it is each
project's tooling decision. ADR 0011 extended what that mechanism must
verify (every `MUST` / `MUST NOT` covered by a criterion). The split
is right — the methodology mandates no tech stack — but it left every
project to write the checker from scratch.

That friction lands on the methodology's flagship machine-checkable
rule. A project that defers writing the checker is a project where
"CI fails on any uncovered criterion" is aspiration, and silent
aspiration is exactly the decay mode "automate what is checkable"
exists to prevent. ADR 0009 already anticipates the remedy: migration
helpers "may be offered" for the mechanical parts, pull not push.

## Decision

Ship a reference checker at
**`templates/ci/check-spec-coverage.py`** — a single-file, stdlib-only
Python 3 script, explicitly **adapt-or-replace**. It verifies, for
every spec whose status makes coverage mandatory (`Implemented` by
default; `Approved` opt-in via flag):

1. every success criterion (`SC-…`) maps to at least one test in the
   Traceability table;
2. every `MUST` / `MUST NOT` requirement (`R-…`) is covered by at
   least one criterion in that table (ADR 0011);
3. every referenced test file exists and cites the criterion id it
   verifies;
4. every Traceability row points at a criterion that actually exists
   in the spec.

ADR 0006's split stands unchanged: the rule is global, the mechanism
is the project's. This script is a **default, not a mandate** — a
project may wire it into CI as-is, adapt it, or replace it with
something native to its toolchain; the project's own tooling ADR
records which.

## Alternatives considered

- **A specification document only** (`templates/ci/README.md` listing
  what the check must verify, no code) — zero maintenance, but keeps
  the from-scratch friction that motivated this ADR. Rejected.
- **POSIX shell / awk** — no interpreter dependency beyond a shell,
  but markdown-table parsing in awk is brittle and unreadable, and
  the script must be easy to *adapt*. Rejected.
- **Mandating it as shared tooling** (all projects run this exact
  script) — rejected: it would violate "no premature tooling
  commitments" and promote a disposable helper into a load-bearing
  dependency. The artifacts stay the interface; the script is an
  editor.

## Consequences

- Wiring the coverage check goes from "write a parser" to "copy a
  file and add a CI line" — the flagship rule gets cheaper to follow
  than to skip.
- This repo now contains executable code for the first time. Accepted:
  it is a template like any other, dependency-free, and changes ride
  the same ADR + changelog discipline; the risk of the reference
  drifting from the rule is mitigated by both living in the same repo
  and changing in the same PR.
- The script encodes the templates' conventions (status line, id
  formats, Traceability table shape). A project that diverges from
  the templates must adapt the script — which is the intended
  relationship, not a bug.

## Adoption impact

**Reference-only.** The obligation to run *a* coverage check came
from ADR 0006/0011 and is unchanged. Projects may copy or wire the
reference script at their own cadence; doing so is the project's
tooling decision, recorded in its own ADR per ADR 0006.

## References

- `methodology.md` §5, "Automate what is checkable".
- ADR 0006 (rule vs. mechanism split), ADR 0011 (MUST → criterion
  coverage), ADR 0009 (helpers offered, pull not push).
- `templates/ci/check-spec-coverage.py`, `templates/spec/spec.md`.
