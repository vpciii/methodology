# ADR 0006: Checkable spec↔test traceability

- **Status:** Accepted
- **Date:** 2026-06-06
- **Deciders:** vpc

## Context

Methodology §5 and the `CONTRIBUTING` Definition of Done already
require that "every success criterion in `spec.md` maps to a passing
test." But today that mapping is **asserted once, by hand, at
feature-done** — a checkbox ticked when the spec flips to
`Implemented`. Two weaknesses follow:

1. **No recorded linkage.** Nothing says *which* test verifies *which*
   criterion. A reviewer can't confirm the claim without re-deriving
   it, and after the feature ships nothing notices when a later,
   unrelated change quietly invalidates a criterion. This is the
   primary longitudinal spec-drift vector: the spec ships green, then
   forty PRs later the behavior has moved and the criterion is a lie.
2. **It is exactly where an AI agent fakes "done."** An agent will
   confidently assert a criterion is covered when no test exercises it.
   With no machine-checkable link, the assertion passes review.

The methodology already commits us to the fix in principle —
"anything machine-checkable is enforced in CI, not left to memory"
(ADR 0005) — but never applied that commitment to the spec↔test link
itself.

## Decision

Make the spec↔test mapping **explicit and machine-checkable**, scoped
to spec'd (substantial/long-lived) work:

- **Stable IDs.** Each success criterion in `spec.md` gets a stable id
  (`SC-1`, `SC-2`, …); a `MUST`/`SHOULD` requirement worth tracing
  gets one too (`R-1`, …). IDs are append-only within a spec — reusing
  or renumbering them breaks the trail.
- **Tests cite the id they verify** — in the test name or a structured
  marker (a pytest marker, a `describe`/`it` string, a Go test name,
  etc.). The *convention* (the id appears in the verifying test) is
  global; the *mechanism* for a given stack is a project tooling ADR.
- **A Traceability table** at the foot of `spec.md` lists each
  criterion id and the test(s) that cover it. Maintained (or
  generated) so that, by the time the spec is `Implemented`, every id
  has a test.
- **CI fails on an uncovered criterion.** A missing-coverage lint
  fails if any success-criterion id has no referencing test. The
  methodology *requires that such a check exist* for spec'd features;
  its implementation (a grep over test names, a coverage plugin) is a
  project tooling ADR.
- **Template + DoD updates.** `templates/spec/spec.md` gains ids on
  success criteria and a Traceability table section.
  `templates/project-CONTRIBUTING.md` changes the "feature is done"
  line from *mapped by hand* to *recorded in the Traceability table
  and enforced in CI*.

## Alternatives considered

- **Keep the honor-system checkbox** — rejected: it is the exact
  discipline that erodes over time and that agents fake. "Automate
  what's checkable" already commits us the other way.
- **Full requirements-management tooling (DOORS-style)** — rejected:
  heavyweight and tool-coupled. An id convention plus a grep-able CI
  check is the markdown/git/test-substrate version that survives any
  tool change.
- **Mandate one test framework's tagging scheme** — rejected: the
  mechanism is a project tooling ADR; only the convention ("an id
  appears in the verifying test") is global.

## Consequences

- "Done" becomes **provable, not asserted** — the largest single gain
  for AI contributors, and an auditable artifact for humans.
- Drift becomes **loud**: changing or deleting behavior that breaks a
  criterion either fails its linked test or trips the coverage lint,
  instead of silently rotting the spec.
- Cost: ids and a small Traceability table to maintain, and a
  per-project CI check to build. Scoped to spec'd work — trivial and
  throwaway changes are untouched, preserving the anti-ceremony stance.
- A criterion that resists a good test becomes visible rather than
  silently uncovered — which often reveals the criterion was vague.
  That surfacing is a feature, not a cost.

## Adoption impact

**Per-project action.** To adopt: add `SC-`/`R-` ids and the
Traceability table when next touching a `spec.md` (templates updated),
and wire the spec-criterion-coverage check into the project's CI (the
mechanism is a project tooling ADR). Existing frozen specs are not
retrofitted.

## References

- `methodology.md` §5, §2; `templates/spec/spec.md`,
  `templates/spec/tasks.md`; `templates/project-CONTRIBUTING.md`
  (Definition of Done).
- ADR 0005 (automate what's checkable; docs ride with code).
- Pairs with ADR 0007 (frozen specs) and ADR 0008 (agent guardrails).
