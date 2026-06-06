# ADR 0007: Specs freeze at implementation; current state lives in tests and an architecture overview

- **Status:** Accepted
- **Date:** 2026-06-06
- **Deciders:** vpc

## Context

Two latent problems both concern *where current-state truth lives*,
and both are spec-drift surfaces:

1. **An `Implemented` spec's afterlife is undefined, and the templates
   contradict each other.** `spec.md`'s `status: Implemented` reads as
   *frozen*; `CONTRIBUTING`'s "anything learned that contradicts the
   spec has been written back into it" reads as *living*. A
   contributor — human or agent — confronted with an old spec doesn't
   know whether to trust it or rewrite it. Ambiguity invites silent
   post-hoc rewrites that *hide* drift rather than record it.

2. **There is no artifact for "how the system is shaped *now*."** ADRs
   and specs are both point-in-time records. Reconstructing the
   current architecture means reading N non-superseded ADRs in order —
   O(N), error-prone, and a place both newcomers and agents go stale.
   "Current" then gets inferred, often wrongly.

## Decision

Separate *what we agreed then* from *how it is now*, and give the
latter explicit homes:

- **A spec freezes when its status reaches `Implemented`.** From that
  point it is a historical record of what was agreed and built — read
  like an ADR, not edited to track ongoing change. The "write
  contradictions back into the spec" rule applies only while a spec is
  still `Draft`/`Under review`/`Approved`. A contradiction discovered
  *after* implementation flows to a **living** artifact instead — a
  test, a new spec, or an ADR — exactly as the operational-feedback
  loop already prescribes (§8).
- **Living truth has two named homes.** *Behavioral* current-state
  lives in the **test suite** (already §5). *Structural* current-state
  lives in a new **`docs/architecture.md`**: a short, C4-context-
  altitude overview of the system as it is now — major components and
  boundaries, data stores, external dependencies, and the
  non-superseded decisions that define the shape. It is a
  **navigational** doc that points at ADRs for *why*; it is not a
  second decision log and must not duplicate ADR detail.
- **It is kept honest like everything else** — `docs/architecture.md`
  changes in the same PR as the structure it describes (ADR 0005).
- **Wiring.** Add `docs/architecture.md` to the artifact map and the
  reading order (after the ADR skim: read `architecture.md` for the
  current shape, ADRs for the why). Add `templates/architecture.md`.
  Add a `Superseded by spec <slug>` status to `spec.md` for the rare
  spec wholly replaced by a later one (parallels ADRs).

## Alternatives considered

- **Keep specs living indefinitely** — rejected: a perpetually-edited
  spec competes with code+tests as "truth," drifts anyway, and loses
  its value as the record of what was agreed. Freezing it and naming a
  dedicated current-state home is cleaner.
- **No architecture doc; rely on ADRs + reading order (status quo)** —
  rejected: O(N-ADR) reconstruction is the documented pain. One short,
  kept-honest file gives an at-a-glance current shape for a small cost.
- **Auto-generate `architecture.md` from code** — rejected *as a
  mandate*: generation is a fine project choice, but the methodology
  specifies the artifact and the freshness rule, not the tool.

## Consequences

- No more ambiguity about whether an old spec is trustworthy:
  `Implemented` = frozen record; *current* = tests (behavior) +
  `architecture.md` (structure); ADRs = *why*.
- Newcomers and agents get a single at-a-glance current-state surface
  instead of inferring it from a stack of decision records.
- Cost: one more kept-honest doc per project, plus the discipline to
  route post-implementation contradictions to living artifacts rather
  than editing a frozen spec.
- Risk: `architecture.md` is itself a drift candidate if neglected —
  mitigated by the same same-PR rule and by keeping it **short**. A
  stale one-pager is cheap to fix; resist letting it grow into
  duplicated detail (that is what the code, tests, and ADRs are for).

## Adoption impact

**Per-project action** for the architecture overview: seed
`docs/architecture.md` from `templates/architecture.md` and keep it
honest thereafter. **Reference-only** for the spec-freeze rule — it
arrives by reading `methodology.md` and the updated `CONTRIBUTING`
template; existing specs are not changed retroactively.

## References

- `methodology.md` §2, §5, §8; artifact map; reading order.
- `templates/project-CONTRIBUTING.md` ("a feature is done when");
  `templates/spec/spec.md`; new `templates/architecture.md`.
- ADR 0005 (docs ride with code). Pairs with ADR 0006 (provable done)
  and ADR 0008 (agent guardrails).
