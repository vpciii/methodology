# ADR 0023: Cross-model adversarial review, ratified; both review roles made model-agnostic

- **Status:** Proposed
- **Date:** 2026-06-20
- **Deciders:** vpc

## Context

Two threads converge here.

**The trial.** `experiments/adversarial-review/` ran a manual cross-model
adversarial review as an explicit trial (added under [Unreleased], no ADR,
no merge gate). Its README set a graduation trigger: promote only when the
log shows it catching defects the same-model path misses, at an acceptable
false-positive rate, across more than one repo. The log
(`experiments/adversarial-review/log.md`) records four rounds across two
repos:

| Round | Target | Mode | Verdict | Real? |
|---|---|---|---|---|
| 1 | opn-mcp PR #13 | code | BLOCK | real defect (stale setup templates recreating a fixed bug) |
| 2 | opn-mcp PR #14 | code | NO STRONG OBJECTION | fix verified, no invented objections |
| 3 | methodology PR #18 | design | BLOCK | a self-consistency flaw in this methodology's *own* ADR 0022 — which a same-model reviewer shares and would have merged |
| 4 | opn-mcp PR #15 | design | PUSH BACK | two real bugs + a fair design challenge |

Four runs, two repos, **zero false positives**, the verdict scale
(BLOCK / PUSH BACK / NO STRONG OBJECTION) discriminating honestly. Round 3
is the decisive evidence: a different model caught a flaw in the
methodology's own design that the author model and a same-model review
would have passed. The trigger is met.

**The deferred generalization.** The existing PR reviewer (ADR 0021) is the
*same model that wrote the code* reviewing its own work, and it is
vendor-bound in CI (`anthropics/claude-code-action`). When the adversary
trial was set up, generalizing *both* reviewers to model-agnostic roles was
deliberately deferred to graduation, to avoid churning a live, cross-repo CI
path twice. Graduation is now. The user's standing requirement is that the
methodology stay model-agnostic — express roles, not vendors, and bind to
today's models in one swappable place.

## Decision

**1. Ratify cross-model adversarial review as a methodology practice.** A
second model — *different from the one that produced the work* —
adversarially reviews substantial changes and hard design decisions. It is
prompted to refute, not to bless. It is **advisory, never a merge gate**
(an LLM's subjective findings do not block merges — consistent with
ADR 0021); deterministic CI stays the required check, and **the human
adjudicates every finding**. A decision-guide row and the shared review
policy carry it; the trial graduates out of `experiments/`.

**2. Both review roles are model-agnostic.** Review is two roles, not two
vendors:

- **Author-model review** — the model that produced the work reviews it
  (today's reviewer, ADR 0021). Cheap, broad; shares the author's blind
  spots.
- **Adversary-model review** — a *different* model refutes it. Catches the
  self-consistency class the author-model structurally cannot (demonstrated:
  round 3).

The durable artifact is a **model-neutral review policy** (the prompt /
checklist — the trial's `adversary-prompt.md` and ADR 0021's review prompt
are its first instances). Each model is a **thin, swappable binding**.
Today's roster: author = Claude (`claude-code-action`); adversary =
Antigravity / Gemini (`run-gemini-cli`, or the `agy` CLI). Swapping or
upgrading either model is a one-binding edit; the policy is untouched. This
**supersedes the vendor-specific *framing* of ADR 0021** (its "Claude PR
reviewer" becomes the "author-model reviewer"); ADR 0021's *mechanism* —
reusable workflow, advisory, pinned action — stands.

**3. Rollout — manual now, automation as a scoped follow-up.** The manual
practice is ratified today (the trial proved it). CI automation is a
defined, ADR-gated follow-up, **not** done in this PR: a reusable
adversary-review workflow mirroring ADR 0021's (advisory, tuned in one
place), and the same refactor that turns both reviewers into a shared policy
+ swappable per-provider bindings. Forward-only; the existing same-model
workflow keeps running until then.

## Alternatives considered

- **Keep it a perpetual trial** — rejected: the evidence met the bar the
  trial itself set; staying "trial" just avoids the decision.
- **Ratify the adversary but leave ADR 0021 vendor-bound** — rejected: the
  model-agnostic requirement covers *both* roles, and generalizing them
  together avoids churning the CI path twice (the reason it was deferred).
- **Make it a merge gate** — rejected: subjective LLM findings should not
  block merges (ADR 0021); advisory, human-adjudicated.
- **Mandate a specific adversary model/vendor** — rejected: the binding is
  swappable by design (the trial's roster). Naming a vendor in the practice
  is the coupling the methodology exists to avoid.

## Consequences

- Reviews gain a second, independent lens that catches the same-model
  blind-spot class — including, on the evidence, flaws in the methodology's
  own design.
- One more review pass costs tokens and time. Bounded: the adversary runs on
  *substantial* changes and *design decisions*, not trivia.
- The CI generalization is real work (generalize `claude-review.yml` to a
  role-based shared policy + per-provider bindings, add an adversary
  workflow and caller template, update consuming projects' callers). Scoped
  as the rollout; forward-only.
- ADR 0021's vendor framing is superseded; its workflow keeps working until
  the generalization lands.
- Because the practice is role-based, future model swaps are one-binding
  edits — the methodology stays model-agnostic.

## Adoption impact

**Per-project (optional).** The manual practice arrives by reading; a
project applies it by running an adversary-model pass on substantial
changes and design decisions and recording the result (e.g. `docs/reviews/`).
Adopting the *automated* adversary workflow is a per-project opt-in once the
reusable workflow ships (as with ADR 0021). Forward-only; nothing to
backfill.

## References

- The trial: `experiments/adversarial-review/` (README, `adversary-prompt.md`,
  `log.md` rounds 1–4); the per-review records in each repo's `docs/reviews/`.
- ADR 0021 (same-model reviewer — framing superseded, mechanism retained),
  ADR 0015 (review checklist / red→green evidence), ADR 0022 (single source
  of truth — the flaw the adversary caught in round 3), ADR 0009
  (versioned-dependency adoption — how per-project workflow callers upgrade).

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
