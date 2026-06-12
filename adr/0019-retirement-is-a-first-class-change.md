# ADR 0019: Retirement is a first-class change

- **Status:** Accepted
- **Date:** 2026-06-12
- **Deciders:** vpc

## Context

A lifecycle audit (ideas → planning → execution → release) found the
decision guide covers creating, changing, refactoring, and incident
response — but nothing for **removal**. Sunsetting a feature, service,
or data store is the methodology's own worst case: irreversible by
definition (data deletion, user migration, external side effects), and
§11 already makes irreversible actions ADR-mandatory. Yet §11's
deprecation guidance speaks only of *API surfaces*, and no
decision-guide row routes a retirement anywhere.

The silence produces the same failure mode ADR 0014 fixed for
refactoring: with no row, a removal happens as a bare PR — the
architecture doc drifts, the feature's tests are deleted silently
(indistinguishable from coverage rot), and the decision trail never
answers the future contributor asking "why was X removed?"

## Decision

Route retirement through existing machinery; add navigation, not new
obligations:

- **A decision-guide row** for retiring a feature, service, or data
  store.
- **A §11 bullet** extending "deprecate with a transition window" from
  API surfaces to features, services, and data stores: decide the
  sunset in an ADR, then walk it down — **deprecation window → dark
  (disabled behind its flag) → removal**.
- **The removal PR carries its artifacts**, as any structural change
  already must: `docs/architecture.md` updated, and the feature's tests
  retired *deliberately*, citing the ADR — never deleted silently.
- **The frozen spec stays as history.** Its status flips to `Retired` —
  a metadata change exactly like the `Implemented` flip (ADR 0007); the
  content is never rewritten. The spec and plan template status enums
  gain `Retired`.

A retirement large enough to be its own project (a long migration, a
user-facing transition) may still warrant a thin spec with a Rollout
plan — framed as *the transition*, not a new feature. Most retirements
are an ADR and a removal PR.

## Alternatives considered

- **A dedicated retirement/sunset template** — rejected: ceremony for
  what is usually one ADR and one PR. The point of the row is to route
  the work, not to manufacture a new artifact (mirrors ADR 0014's
  rejection of a refactor template).
- **Status quo — rely on §11's "irreversible → ADR" alone** — rejected:
  the rule exists but nothing navigates to it; the audit found that
  silence at the navigation layer is exactly what produces skipped
  artifacts (the ADR 0014 lesson, again).
- **Leave the spec status enum untouched** — considered, since the spec
  is frozen anyway. Rejected: `Retired` is one enum value, the flip is
  metadata (the freeze already permits the `Implemented` flip), and a
  self-describing record beats cross-referencing an ADR to learn a spec
  describes removed behavior.

## Consequences

- Removals get the same decision trail as additions; "why was X
  removed?" has an answer at the conventional path.
- Tests leave the suite only deliberately, citing the ADR — silent
  coverage loss during a removal becomes visible in review.
- The decision guide is one row longer; the status enums gain one
  value. No new artifact types, no new enforcement.
- Risk: contributors spec-up small retirements. Mitigated by the
  explicit guard above — most retirements are an ADR and a removal PR.

## Adoption impact

**Reference-only.** Arrives by reading the decision guide and §11.
Optionally per-project: re-sync `templates/spec/{spec,plan}.md` for the
`Retired` status value when next touching a spec. Forward-only
(`adopting.md`): nothing to backfill for past removals.

## References

- `methodology.md` — decision guide, §1 (ADRs), §11 (reversible by
  default), artifact map.
- ADR 0007 (spec freeze; the `Implemented` flip this mirrors),
  ADR 0014 (the refactoring row; the navigation-gap precedent),
  ADR 0012 (forward-only adoption).
- `templates/spec/spec.md`, `templates/spec/plan.md` (status enums).

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
