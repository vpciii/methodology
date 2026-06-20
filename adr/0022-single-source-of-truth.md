# ADR 0022: Single source of truth — duplication is a hazard

- **Status:** Accepted
- **Date:** 2026-06-20
- **Deciders:** vpc

## Context

The "keep the artifacts honest" rules bind **code↔doc** coupling (docs
change in the same PR as the behavior they describe) and say to "automate
what is checkable." Neither names the failure mode where a single *fact*
is hand-copied into two places that then drift independently — **doc↔doc**
(or code↔code) duplication.

A consuming project surfaced the gap concretely. A scheduled-task prompt
lived in two tracked copies: the canonical skill file the system runs, and
a "template" the setup guide pointed new operators to. An update touched
only the canonical copy; the template silently went stale, so anyone
following the setup guide copied a broken prompt — recreating the very bug
the update had just fixed. The same-PR rule never fired (it governs
code↔doc; this was doc↔doc), the same-model PR reviewer (ADR 0021) missed
it, and CI had nothing to check. A cross-model adversarial review caught it
only retrospectively.

The methodology already *practices* single-sourcing for its own mirrors —
`global-CLAUDE.md` is a summary edited in the same PR as the change it
summarizes (ADR 0018), and the Cursor `.mdc` mirror likewise — but the
underlying principle was never stated as a rule, so consuming projects had
no guard to apply.

## Decision

Add a **single source of truth** item to "Keep the artifacts honest":

- A fact lives in **one** place.
- If it must exist in more than one — a generated artifact, a mirrored
  summary, a copy some tool requires — the copy is **generated from** the
  source or **machine-checked against** it, never kept in sync by human
  memory (this is what "automate what is checkable" buys here).
- **Duplication of a hand-maintained fact is a review smell** — the same
  fact maintained in two editable places is itself a finding, treated like
  any other honesty violation. The cheapest correct response to discovered
  duplication is to remove the duplicate; if a second copy is genuinely
  unavoidable, add the check.

## Alternatives considered

- **Rely on the existing same-PR rule** — rejected: it binds code↔doc.
  Doc↔doc and code↔code duplication is its blind spot, demonstrated by the
  incident that prompted this ADR.
- **Mandate a specific dedup mechanism** (code generation, file includes,
  a CI equality check) — rejected: mechanism is a per-project tooling
  choice (the rule-vs-mechanism split, ADR 0006). The methodology states
  the principle; the project picks the tool.
- **Leave it implicit** since the methodology already single-sources its
  own summaries — rejected: practicing it for our files gave consuming
  projects nothing to apply. Naming the principle is the point.

## Consequences

- Reviewers and agents get an explicit trigger: duplication is a
  defect-in-waiting, caught at review rather than after it drifts.
- Existing deliberate duplication in projects surfaces and wants
  single-sourcing or a check — forward-only (`adopting.md`); no
  retroactive sweep.
- A mild tension remains with convenience copies (a self-contained doc
  that repeats a value for readability). The escape hatch — *generate it
  or check it* — keeps that legal when the repetition genuinely earns its
  keep, while forbidding the memory-synced version that rots.

## Adoption impact

**Reference-only** — arrives by reading the honesty rules. Optionally
*per-project*: where a project has known, deliberate duplication, add an
equality or code-generation check (its own tooling decision). Forward-only;
nothing to backfill.

## References

- `methodology.md` — "Keep the artifacts honest"; ADR 0018 (the global
  summary as a generated/mirrored copy — the principle already in
  practice), ADR 0006 (rule vs. mechanism split), ADR 0020 (user-facing
  docs ride along — the adjacent honesty rule), ADR 0021 (the same-model
  reviewer's blind spot).
- The cross-model adversarial review trial (`experiments/adversarial-review/`)
  that caught the motivating incident; the consuming project's own dedup ADR.

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
