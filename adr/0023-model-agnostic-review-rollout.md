# ADR 0023: Model-agnostic review rollout — shared policy + per-provider bindings; adds the adversary reviewer (supersedes ADR 0021)

- **Status:** Proposed
- **Date:** 2026-06-20
- **Deciders:** vpc

## Context

ADR 0021 established a shared, methodology-aware **same-model** PR reviewer
(`.github/workflows/claude-review.yml`, `anthropics/claude-code-action`).
It is **vendor-bound**: the action, the secret, and the GitHub App are all
Claude-specific.

The cross-model adversarial review trial (`experiments/adversarial-review/`,
`log.md`) showed that a *different* model catches a class of defect the
same-model reviewer structurally shares — 5 runs, 2 repos, 3 BLOCKs, 0 false
positives, including a self-consistency flaw in this methodology's *own*
ADR 0022, and a BLOCK on the trial's own premature graduation ADR (PR #19,
withdrawn).

That withdrawn graduation attempt established two hard constraints this ADR
must honor (round-5 review, `docs/reviews/pr19_adversarial_review.md`):

- **Model-agnosticism cannot be *claimed* while the implementation is
  vendor-bound.** Changing documentation vocabulary to "author-model
  review" does not make the CI reviewer model-agnostic. The property must be
  *built*.
- **"Partial supersession" of ADR 0021 is incoherent** under the
  append-only rule. ADRs supersede wholesale.

This ADR is the **rollout that builds the capability**. It deliberately does
**not** ratify adversary review as a mandated practice (no decision-guide
row) — that is a later graduation ADR, made only once this is live *and* the
agnosticism claim has been tested in a direction the trial never ran (see
Consequences).

## Decision

**Two review roles, each a thin per-provider binding over one shared,
model-neutral review policy.**

1. **The review policy is the durable artifact.** One model-neutral
   prompt/checklist: review the change against the project's own spec, ADRs,
   glossary, and Definition of Done; for the adversary, the
   refute-don't-bless stance and the BLOCK / PUSH BACK / NO STRONG OBJECTION
   verdict. It is **single-sourced** (ADR 0022): it lives in one file and
   each binding workflow receives it by **generation or a CI equality
   check**, never hand-copied into two workflows.

2. **Author-model binding** — the existing reviewer, generalized: Claude via
   `claude-code-action` today. The same model that produced the work; broad
   and cheap, shares the author's blind spots.

3. **Adversary-model binding** — a *different* model refutes the work:
   Gemini via [`run-gemini-cli`](https://github.com/google-github-actions/run-gemini-cli)
   (or the Antigravity `agy` CLI) today.

   Both are **advisory — never a merge gate** (ADR 0021); deterministic CI
   stays the required check and **the human adjudicates** every finding.

4. **The binding is the one swappable place.** Swapping or upgrading a model
   — a newer Gemini, a different vendor as the adversary, or *reversing the
   roles* (Gemini author / Claude adversary) — is editing a binding
   workflow's action + secret. The shared policy is untouched. This is what
   makes the methodology's model-agnosticism *real* rather than
   terminological.

5. **Supersede ADR 0021 wholesale.** This ADR replaces 0021's single
   vendor-bound reviewer with the role-based structure; ADR 0021 is marked
   `Superseded by ADR 0023` when this is accepted. Its mechanism (reusable
   workflow, advisory, pinned action, trigger/skip rules) is carried forward
   in role-based form — not a partial edit.

## Migration (the rollout)

Implemented in a follow-up PR once this ADR is accepted — itemized here so
the breaking changes are decided, not discovered:

- **Reusable workflows** in this repo: `review-author.yml` (Claude) and
  `review-adversary.yml` (Gemini), both `on: workflow_call`, both fed by the
  single-sourced policy. This **renames** `claude-review.yml` — a breaking
  change for callers.
- **Caller templates** under `templates/github/` for each; a project adopts
  one or both with a thin caller.
- **Secrets / apps**, per repo (personal account, no org central key):
  author needs `ANTHROPIC_API_KEY` + the Claude GitHub App (as today);
  adversary needs `GEMINI_API_KEY` + the Gemini GitHub App.
- **This repo dogfoods both.** `opn-mcp`'s existing caller
  (`…/claude-review.yml@main`) is updated to the renamed author workflow in
  the same rollout (ADR 0009 — callers upgrade deliberately).
- **Cost / noise:** two advisory LLM reviews per PR; the ADR 0021
  draft / `[skip-review]` skip rules apply to both.

## Alternatives considered

- **One parameterized reusable workflow** (a `provider` input switching
  actions) — rejected: `claude-code-action` and `run-gemini-cli` have
  different inputs, secrets, and posting mechanisms; one workflow
  conditionally switching actions is brittle. Two thin bindings each stay
  simple.
- **Hand-copy the policy into both workflows** — rejected: that is exactly
  the verbatim duplication ADR 0022 forbids. Single-source + CI equality
  check instead (this rollout eats its own dog food).
- **Keep ADR 0021 and add the adversary alongside, no supersession** —
  rejected: making the *author* reviewer model-agnostic requires
  restructuring 0021's workflow (the rename + role binding), which is a
  wholesale replacement. Superseding is the honest record; "partial" is the
  incoherence round 5 flagged.
- **Make either reviewer a merge gate** — rejected (ADR 0021): advisory
  only; the human adjudicates.
- **Ratify the practice in this same ADR** — rejected: round 5's lesson is
  not to claim or mandate ahead of implementation *and* evidence. This ADR
  builds the capability; a separate graduation ADR ratifies it once it is
  live and the agnosticism is actually tested.

## Consequences

- **Model-agnosticism becomes real** after this lands: both roles are
  swappable bindings over a shared policy. The claim round 5 rejected can
  then be made honestly.
- **The agnosticism is still only *enabled*, not yet *demonstrated*.** Every
  trial run was Claude-author / Gemini-adversary. This rollout makes role
  reversal and third-model substitution a one-binding edit; the graduation
  ADR should carry at least one **reversed-role or third-model** run as
  evidence before ratifying. Naming this is the honest counter to the
  round-5 "untested agnosticism" finding.
- Reviews gain the adversary lens *in CI* (advisory) — automating what the
  trial did by hand.
- **Breaking change:** the workflow rename breaks existing callers until
  updated (opn-mcp + the template, same rollout). Forward-only.
- A second per-repo credential + GitHub App (Gemini), like the Claude one;
  no org central key (personal account).
- Two advisory LLM reviews per PR — more token cost and PR-comment noise;
  bounded by triggers/skips, both advisory.
- ADR 0021 superseded; its history retained, its mechanism carried forward.
- The shared-policy single-sourcing is itself CI-checked (ADR 0022) — if it
  is not, this ADR reintroduces the very drift it cites.

## Adoption impact

**Per-project.** Existing adopters of the ADR 0021 reviewer update their
caller to the renamed author workflow (a one-line change) when the rollout
lands; adopting the adversary workflow is opt-in (add the `GEMINI_API_KEY`
secret, the Gemini App, and a caller). Forward-only. This repo dogfoods
both.

## References

- ADR 0021 (the same-model reviewer — superseded here), ADR 0022 (single
  source of truth — the shared policy), ADR 0009 (versioned-dependency —
  callers upgrade deliberately), ADR 0003 (pinned action dependencies).
- The trial: `experiments/adversarial-review/` (`README.md`, `log.md`),
  `docs/reviews/pr19_adversarial_review.md` (the round-5 constraints this
  ADR honors).
- `anthropics/claude-code-action`; `google-github-actions/run-gemini-cli`.

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
