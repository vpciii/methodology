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

Add a **single source of truth** item to "Keep the artifacts honest",
**scoped to the actual hazard.**

The hazard is hand-maintained **verbatim** duplication: two or more copies
of a fact that are meant to stay identical, kept in sync only by memory.
They drift — the motivating incident was a prompt copied verbatim into a
second file that silently went stale. For copies meant to be identical:

- Prefer to **remove** the duplicate (single-source it).
- If an identical second copy must exist (a generated artifact, a copy some
  tool requires), it is **generated from** the source or **machine-checked
  for equality** against it — never synced by memory.
- Hand-maintained verbatim duplication kept in sync by memory is a **review
  smell**, treated like any other honesty violation.

**Deliberate derivatives are *not* this hazard.** A copy that is
intentionally *not* identical to its source cannot be "checked for
equality"; it is kept honest by the same-PR rule instead:

- **Curated summaries / abridgments** — e.g. this methodology's own
  `global-CLAUDE.md` and `.mdc` summaries of `methodology.md`: lossy by
  design, kept honest by editing them in the same PR as the change they
  summarize (ADR 0018). Forcing a generator onto a single curated markdown
  file is the ceremony ADR 0018 explicitly rejected.
- **Instantiated templates in consuming projects** — a project's
  `CLAUDE.md` / `CONTRIBUTING.md` copied from a template and customized,
  re-synced deliberately on a methodology upgrade: governed by the
  versioned-dependency adoption model (ADR 0009), not equality-checked
  against a template they were meant to diverge from.
- **Small convenience repetition for readability** — restating a value or
  step so a doc reads self-contained (ADR 0005): fine in moderation; it
  does not trigger tooling.

The line: *if two copies are supposed to be character-for-character the
same and a human keeps them so from memory, that is the smell.* A
deliberate derivative is kept honest by the same-PR rule, not equality.

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
- **An absolute "no hand-maintained duplication" rule** (the first draft) —
  rejected: it indicts the methodology's own curated summaries (ADR 0018)
  and every consuming project's instantiated templates (ADR 0009), and
  forces tooling ceremony onto single markdown files — the opposite of the
  anti-premature-tooling stance. The hazard is *verbatim drift kept in sync
  by memory*, not all repetition; the rule is scoped to that. (An
  adversarial review of the first draft caught the over-reach — see
  Consequences.)

## Consequences

- Reviewers and agents get an explicit trigger: duplication is a
  defect-in-waiting, caught at review rather than after it drifts.
- Existing deliberate duplication in projects surfaces and wants
  single-sourcing or a check — forward-only (`adopting.md`); no
  retroactive sweep.
- The repo's own practices stay compliant under the scoping: the curated
  summaries (ADR 0018) and consuming-project templates (ADR 0009) are
  deliberate derivatives kept honest by the same-PR rule, not duplication to
  machine-check. The motivating opn-mcp case — a *verbatim* copy of a prompt
  — is squarely the hazard and is fixed by removal.
- **This ADR was itself scoped by an adversarial review.** The first draft
  stated the rule absolutely ("generated or machine-checked, never synced by
  memory"); a cross-model review (round 3,
  `docs/reviews/pr18_adversarial_review.md`) BLOCKed it for outlawing the
  methodology's own summaries and every adopter's templates. The
  verbatim-vs-derivative scoping above is the resolution — the trial working
  as intended.

## Adoption impact

**Reference-only** — arrives by reading the honesty rules. Optionally
*per-project*: where a project has known, deliberate duplication, add an
equality or code-generation check (its own tooling decision). Forward-only;
nothing to backfill.

## References

- `methodology.md` — "Keep the artifacts honest"; ADR 0018 (the global
  summary — a *curated derivative* hand-edited in the same PR, the carve-out
  this ADR scopes around), ADR 0009 (versioned-dependency model —
  instantiated templates), ADR 0006 (rule vs. mechanism split), ADR 0005
  (dual-audience navigability — readability), ADR 0020 (user-facing docs
  ride along — the adjacent honesty rule), ADR 0021 (the same-model
  reviewer's blind spot).
- The cross-model adversarial review trial (`experiments/adversarial-review/`)
  that caught both the motivating incident and this ADR's own first-draft
  over-reach (`docs/reviews/pr18_adversarial_review.md`); the consuming
  project's own dedup ADR.

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
