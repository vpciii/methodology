# ADR 0015: Review checklist and red→green evidence for fixes

- **Status:** Accepted
- **Date:** 2026-06-09
- **Deciders:** vpc

## Context

"The human accepts" is the methodology's load-bearing quality gate:
every diff is reviewed, every test is run, and the agent guardrails
(ADR 0008) all terminate in a human review catching what drifted. Yet
review itself was the least specified practice. The review-scope rule
in `templates/project-CONTRIBUTING.md` answers what *range* a review
covers (full diff vs. delta since last review) but nothing says what a
review *checks* — the one activity everything else relies on was left
to diligence, which is exactly what "automate what is checkable"
warns against leaving things to.

Separately, §5 requires regression tests that "fail before the fix and
pass after," but nothing required *evidence* of the failing half. A
test written after the fix — especially an agent-drafted one — can
pass without ever having demonstrated it catches the bug: tautological
assertions, testing the mock, or pinning the fixed behavior without
exercising the broken path. The "show done, don't assert it" guardrail
(ADR 0008) covered only the green half of red→green. With AI agents
drafting most code, review is the throughput bottleneck and the last
gate; both gaps sit precisely where the methodology holds itself to
the standard of being checkable, not aspirational.

## Decision

Two additions, both conventions enforced in review:

1. **Every review checks a named list.** The project
   `CONTRIBUTING.md` template carries a short checklist applied to
   whatever diff range the review covers: spec conformance (including
   no quiet contract rewrites), test honesty, glossary language,
   boundaries and reversibility, and artifacts riding in the same PR.
   Deliberately short — a long checklist invites rubber-stamping.

2. **A bug fix cites its red→green evidence.** The fix's PR cites the
   regression test's failing output from before the fix, or a
   test-first commit a reviewer can check out and run. "Fails before"
   is shown, not asserted — the same posture ADR 0008 takes for
   "passes after." The agent guardrail is extended accordingly.

Whether CI also enforces the evidence (e.g. verifying test-first
commit ordering) remains a project tooling decision — the same
rule-vs-mechanism split as ADR 0006.

## Alternatives considered

- **CI-enforced test-first commit ordering** — strongest guarantee,
  but intrusive on rebase/squash workflows and brittle to implement
  generically. Rejected as a global mandate; remains open to any
  project as its own tooling ADR.
- **Agent-only requirement** — make only AI agents show the failing
  run, leaving humans on the honor system. Rejected: the asymmetry is
  unjustified (humans write tautological tests too) and the cost of
  pasting a failing run is near zero.
- **No checklist; trust reviewer diligence** — rejected: the
  methodology's own standard is that what it relies on is specified
  or automated, not remembered. An unnamed expectation is the first
  thing to decay.

## Consequences

- Review quality becomes specifiable and teachable: a new contributor
  (or agent) knows what a review is *for*, not just which commits it
  spans.
- "Fails before, passes after" graduates from claim to evidence; the
  weakest form of test gaming — a regression test that never failed —
  becomes visible at review time.
- Each bug-fix PR carries one extra line of ceremony (the cited
  failing run). Accepted: it is the cheapest possible proof of the
  most important property a regression test has.
- The checklist could ossify or bloat. Mitigation: it lives in the
  project template, edited like any artifact, and is kept to five
  items by design.

## Adoption impact

**Per-project action.** Re-sync from the templates: the **Reviews**
section (checklist), **Definition of done** (red→green evidence
bullet), and **Tests** section of `CONTRIBUTING.md`, and the tests
hard rule in `CLAUDE.md`. Reference-only for projects that point at
the templates without local copies.

## References

- `methodology.md` §5 (tests as executable specification), agent
  guardrails ("show done, don't assert it").
- ADR 0006 (rule global, CI mechanism per-project), ADR 0008
  (agent drift guardrails — this extends "show done" to the red half).
- `templates/project-CONTRIBUTING.md`, `templates/project-CLAUDE.md`,
  `templates/methodology.mdc`.
