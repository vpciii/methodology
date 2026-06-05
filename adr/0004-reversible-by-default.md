# ADR 0004: Reversible by default

- **Status:** Accepted
- **Date:** 2026-06-05
- **Deciders:** vpc

## Context

Trunk-based development with frequent merges to `main` (methodology
§4) is only safe if changes are easy to undo. The methodology implied
this — `plan.md` has a "Rollout" section — but never stated
reversibility as a principle. Without it stated, the natural failure
mode is irreversible changes shipped in one big step: a destructive
migration, a breaking API change with no transition window, a feature
with no off switch. This is exactly the kind of standing principle an
AI agent needs spelled out, because it will otherwise optimize for
"make the change" over "make the change safely undoable."

## Decision

Add **"Reversible by default"** as a named practice (methodology §11):

- **Prefer changes you can turn off or roll back.** Feature flags for
  risky behavior; ship dark, enable gradually.
- **Evolve schemas with expand-contract (parallel-change):** add the
  new shape, migrate, then remove the old — never a destructive
  in-place change in a single irreversible step.
- **Evolve APIs backward-compatibly:** additive first; deprecate with
  a transition window before removing.
- **Every non-trivial change has a known undo** — a flag flip, a
  revert, or a documented rollback in `plan.md`'s Rollout section. If
  a change is genuinely irreversible (data deletion, an external side
  effect), that fact is called out explicitly and decided with an ADR.

## Alternatives considered

- **Leave it implicit in trunk-based + plan.md** — rejected: the
  safety rail that makes frequent merging viable deserves to be a
  stated principle, not an inference.
- **Mandate feature-flag tooling** — rejected: the principle is
  "reversible," not a specific flag system; tool choice is a project
  ADR.

## Consequences

- Frequent merging to `main` stays low-risk.
- Slightly more up-front design (transition windows, flags) in
  exchange for cheap, fast recovery when something is wrong.
- Genuinely irreversible actions become conscious, recorded decisions
  rather than accidents.

## References

- `methodology.md` §11, §4; `templates/spec/plan.md` (Rollout).
