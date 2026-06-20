# Cross-model adversarial review

> **Status: RATIFIED — ADR 0023.** This began as a trial and graduated on
> the evidence in [`log.md`](./log.md) (4 rounds, 2 repos, 2 real BLOCKs,
> 0 false positives — including a flaw caught in the methodology's own ADR
> 0022 that a same-model review would have merged). It is now a practice
> with a decision-guide row. It remains **advisory — never a merge gate**;
> deterministic CI stays the required check and the human adjudicates every
> finding. The [`adversary-prompt.md`](./adversary-prompt.md) is the shared,
> model-neutral review **policy**; the *Current roster* below is the
> swappable model binding. CI automation of the adversary role is a scoped
> follow-up (ADR 0023, Rollout).

## What it is

Two **roles**, never two specific vendors:

- The **author model** produces the work and reviews its own output (the
  existing same-model PR reviewer,
  [ADR 0021](../../adr/0021-shared-claude-pr-review-workflow.md)).
- The **adversary model** — a *different* model — is prompted to refute
  it.

The premise, borne out by the log: a same-model reviewer shares the
author's blind spots, so it systematically misses a class of defect that a
different model — with different training, priors, and failure modes —
catches.

The relationship is **adversarial by design**. The adversary is prompted
to refute, not to bless: find the missing test, break the unstated case,
steelman the rejected ADR alternative. The two models disagreeing in
front of the human is the product. **The human stays the author of
record and adjudicates every finding** — the adversary advises, it never
decides or merges.

Scope is both halves of the lifecycle this methodology already names:
**code review** (a diff against its spec) and **design decisions** (an
ADR, spec, or planning option before sign-off).

## Current roster — the one place to swap models

Everything else in this directory is written in terms of the *roles*
above, so switching or upgrading a model means editing **only this
table** — the guide and the [adversary prompt](./adversary-prompt.md)
stay untouched. That is the whole point: the methodology is model-
agnostic; this roster is its single, disposable binding to today's
models.

| Role | Filled today by | How it's invoked |
|---|---|---|
| **Author model** | Claude (Claude Code) | Normal development; produces the PR or ADR/spec draft. |
| **Adversary model** | Google Antigravity / Gemini 3 | Antigravity IDE, or the `agy` CLI headless with `GEMINI_API_KEY` / `ANTIGRAVITY_API_KEY` in the environment. |

To swap (e.g. a newer Gemini, or a different vendor entirely as the
adversary): change the cells above and, if invocation differs, the *How
to run it* mechanics below. No prompt edits, no role rewrites.

## How to run it (manual)

1. The **author model** produces the work (a PR, or an ADR/spec draft) as
   usual.
2. Open the work in the **adversary model** (per the roster above).
3. Paste [`adversary-prompt.md`](./adversary-prompt.md) — the shared
   framing plus the **Code review** or **Design decision** block — and
   give it the inputs that block lists (the diff/draft, the spec, the
   relevant ADRs, the glossary, the Definition of Done).
4. Take the adversary's verdict (**BLOCK** / **PUSH BACK** / **NO STRONG
   OBJECTION**) back to the author model. Resolve each finding into one
   of: a test, an ADR, a spec edit, or a *defended* "no change."
5. Log the round (below).

## Review log

Keep a running [`log.md`](./log.md), one row per review. It was the
graduate-or-kill evidence during the trial; it now stays as the running
record of adversary passes:

| Date | Repo / PR or ADR | Mode | Adversary verdict | Did it catch something the author model + CI missed? | False positives | Friction notes |
|---|---|---|---|---|---|---|

The questions the trial must answer:

- **Signal:** does it find real defects the same-model reviewer and
  deterministic CI did not? (The whole justification.)
- **Noise:** what's the false-positive rate — confident findings that
  were wrong or irrelevant?
- **Cost:** minutes per review, context-shuffling friction, API spend.

## Graduated → ADR 0023; the rollout that remains

This practice **graduated** on the log above (4 rounds, 2 repos, 2 real
BLOCKs, 0 false positives — including a flaw it caught in the
methodology's own ADR 0022) and is ratified in
[ADR 0023](../../adr/0023-cross-model-adversarial-review-ratified.md). That
ADR also made **both** review roles model-agnostic: a shared,
model-neutral review *policy* (this prompt plus ADR 0021's) with thin,
swappable per-provider *bindings* — author = Claude (`claude-code-action`);
adversary = Gemini (`run-gemini-cli` / the Antigravity **`agy`** CLI).
Swapping or upgrading either model is a one-binding edit; the policy is
untouched.

**What remains is the CI rollout** (ADR 0023, Rollout — a follow-up, *not*
done): generalize ADR 0021's `claude-review.yml` into the role-based shared
workflow, add an adversary-review workflow and caller template, and update
consuming projects' callers. Until then, the manual pass above is the
ratified practice and the existing same-model workflow keeps running.
