# ADR 0014: Behavior-preserving refactoring in the decision guide

- **Status:** Accepted
- **Date:** 2026-06-08
- **Deciders:** vpc

## Context

The decision guide routes *behavior* changes to a test and *structural*
changes to `docs/architecture.md`, but it had no entry for the common
middle case: **restructuring code without changing behavior** — a
refactor, or bounded tech-debt paydown. The methodology's existing pieces
imply how to handle it (§5: a true refactor changes no behavior, so it
changes no tests; §11: a future-constraining change gets an ADR;
scale-to-work: non-feature work needs no spec), but this was never stated
in one place.

A code review flagged the gap: with no explicit row, a contributor —
especially an AI agent told "spec-first for non-trivial work" — either
skips the artifacts or invents a fake user-facing feature spec to satisfy
the rule. Neither is right for "change the structure of much, the
behavior of nothing."

## Decision

Add a decision-guide row for behavior-preserving restructuring:

- **No spec.** A refactor introduces no new behavior to specify.
- **Keep the test suite green.** Because behavior is unchanged, the
  existing tests are the safety net and must not need editing (§5,
  behavior over implementation). On an untested brownfield area, pin
  current behavior with a characterization test first (`adopting.md`).
- **An ADR only if it closes off future options** (§1, §11) — most
  refactors don't; some (changing a boundary, a shared abstraction) do.
- **Update `docs/architecture.md` in the same PR** if the refactor
  changes the system's structure — already required, unchanged here.

A refactor large enough to be its own project may still warrant a thin
spec, but framed as *properties preserved*, not a new feature.

## Alternatives considered

- **A dedicated refactor spec template** — rejected: ceremony for what is
  usually a commit. The point of the row is to *avoid* manufacturing a
  spec.
- **Status quo (no row)** — rejected: the silence is what produces fake
  feature specs or skipped artifacts — exactly the agent failure mode the
  review identified.
- **A multi-row sub-table** (pure refactor vs. refactor-to-enable vs.
  debt-paydown) — rejected: one row plus the existing §5 / §11 / §1 rules
  covers all three without bloating the guide.

## Consequences

- Contributors and agents get a clear "no fake spec" signal for
  structural-only work, and a clear trigger (closes off options → ADR)
  for the refactors that do warrant a decision record.
- The decision guide is one row longer; no other artifact changes.
- The rule adds *navigation*, not new obligations — it leans entirely on
  existing practices (§5, §11, §1), so there is nothing new to enforce.

## Adoption impact

**Reference-only.** Arrives by reading the decision guide; no per-project
action.

## References

- `methodology.md` — the decision guide; §5 (tests; behavior over
  implementation), §11 (reversible / future-constraining), §1 (ADRs).
- `adopting.md` (characterization tests for untested brownfield code).
- `templates/methodology.mdc` (the mirrored decision guide).

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
