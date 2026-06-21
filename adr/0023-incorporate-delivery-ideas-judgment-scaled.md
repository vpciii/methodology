# ADR 0023: Incorporate modern-delivery ideas, judgment-scaled (counter to PR #22)

- **Status:** Proposed
- **Date:** 2026-06-21
- **Deciders:** vpc

> This is the methodology-consistent **alternative** to PR #22, which
> proposed six new numbered practices and was BLOCKed by an adversarial
> review (`docs/reviews/pr22_adversarial_review.md`). Accept one or the
> other, not both.

## Context

PR #22 proposed adding six numbered practices — deterministic environments,
automated quality gates, continuous deployment, continuous refactoring, code
review culture, and documentation-as-code — and an ADR mandating them as
"non-negotiable standards."

A cross-model adversarial review (round 8 of the trial,
`docs/reviews/pr22_adversarial_review.md`) returned **BLOCK**, and the
findings hold:

- **Three duplicate existing practices/ADRs.** Continuous refactoring is
  already the decision-guide row + ADR 0014; documentation-as-code is already
  the "Keep the artifacts honest" same-PR rule + ADR 0020; code-review
  substance is already ADR 0015. Re-stating them as new practices creates
  second homes for the same rules — the hazard ADR 0022 names, one ADR after
  adopting it.
- **Two contradict standing exclusions.** Naming formatters and mandating a
  CI/CD provider globally violates "No premature tech-stack or tooling
  commitments"; mandatory continuous deployment imports the heavyweight
  delivery machinery the "no formal SRE/ITIL" exclusion keeps out, and it has
  no deployable-service scoping (§6 has one), so it breaks on libraries,
  CLIs, and this docs repo.
- **The framing inverts the methodology's stance** — "non-negotiable" against
  "scale the ceremony / apply judgment."

But the *underlying ideas* have merit. The question this ADR answers is: what
is genuinely new and durable enough to add, and where does it belong?

## Decision

**1. Add exactly one new practice — §12 Deterministic onboarding** —
tool-agnostic and judgment-scaled: a substantial project bootstraps with one
documented, reproducible command; "works on my machine" is a defect; the tool
(Make / devcontainer / Nix / script) is a per-project choice, not a mandate.
This is the one idea from PR #22 with no existing home — the running system's
determinism is covered (§6 config-in-env, §10 lockfiles) but the *developer's
entry path* is not.

**2. Refine the existing "Automate what is checkable" rule** to fold in the
useful nugget of PR #22's §13/§16: formatting/style is machine-enforced, and
*if a machine can catch it, human review shouldn't spend attention on it* —
review goes to behavior, intent, and the artifacts (ADR 0015). This is a
sharpening of an existing rule, not a new practice.

**3. Add nothing else.** Continuous refactoring (ADR 0014), documentation-as-
code (ADR 0020 + same-PR rule), and code-review substance (ADR 0015) are
already covered — re-adding them would violate ADR 0022. Continuous
deployment stays a per-project deployment/tooling decision (the standing
exclusion) and is already implied by §4 (main always shippable) + §11
(reversible); it does not become a global practice.

**4. Keep the document self-consistent in the same PR** (what PR #22 missed):
update the `§1–§11` → `§1–§12` references and the README practice count, and
sync the `global-CLAUDE.md` / `methodology.mdc` summaries (ADR 0018).

## Alternatives considered

- **PR #22 as written** (six mandated practices) — rejected per the
  adversarial review: duplication (ADR 0022), tooling-commitment and
  lightweight-ops contradictions, missing CD scoping, scale-to-work
  inversion, and self-inconsistency.
- **Status quo / PR #22's own "Option B"** — partially adopted: most of the
  six *is* already covered, so the bar for a *new* practice is "a genuine,
  durable, tool-agnostic gap." Only deterministic onboarding clears it.
- **Fold deterministic onboarding into §6 or §10** instead of a new practice
  — considered; rejected because the developer entry path is distinct from
  running-system parity (§6) and build reproducibility (§10), and neither
  currently states it. A short dedicated practice is clearer than stretching
  an existing one.

## Consequences

- The methodology gains one tool-agnostic, judgment-scaled practice (12
  total) and a sharper automate-what's-checkable rule — no duplication, no
  tooling mandate.
- The genuinely-good ideas from PR #22 are captured where they belong, and
  the already-covered ones are explicitly confirmed as present (reducing the
  temptation to re-add them).
- The document stays self-consistent (references + summaries updated in this
  PR), unlike PR #22.

## Adoption impact

*Reference-only* for the principle. *Per-project (optional):* a substantial
project that lacks a one-command setup adds one; the tool choice, if
non-trivial, is its own project ADR. Forward-only — no backfill.

## References

- `docs/reviews/pr22_adversarial_review.md` (the BLOCK this answers).
- ADR 0014 (refactoring already in the decision guide), ADR 0020
  (user-facing docs ride along), ADR 0015 (review checklist), ADR 0022
  (single source of truth), ADR 0018 (summaries change in the same PR).
- `methodology.md` §4, §6, §10, §11; DORA / Accelerate (Forsgren et al.,
  2018).

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
