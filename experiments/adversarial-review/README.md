# Experiment: cross-model adversarial review

> **Status: TRIAL — not a ratified practice.** This is a manual process
> being evaluated. It is deliberately *not* in `methodology.md`'s numbered
> practices or the decision guide, and it carries **no adoption
> obligation** for any project. If it proves out, it graduates to an ADR
> (the trigger below); if it doesn't, this directory is deleted. Nothing
> here gates a merge.

## What we're testing

Two **roles**, never two specific vendors:

- The **author model** produces the work and reviews its own output (the
  existing same-model PR reviewer,
  [ADR 0021](../../adr/0021-shared-claude-pr-review-workflow.md)).
- The **adversary model** — a *different* model — is prompted to refute
  it.

The bet: a same-model reviewer shares the author's blind spots, so it
systematically misses a class of defect that a different model — with
different training, priors, and failure modes — would catch.

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

## Trial log — the evidence the eventual ADR needs

Keep a running [`log.md`](./log.md) (create on first use), one row per
review, so the graduate-or-kill decision rests on data, not vibe:

| Date | Repo / PR or ADR | Mode | Adversary verdict | Did it catch something the author model + CI missed? | False positives | Friction notes |
|---|---|---|---|---|---|---|

The questions the trial must answer:

- **Signal:** does it find real defects the same-model reviewer and
  deterministic CI did not? (The whole justification.)
- **Noise:** what's the false-positive rate — confident findings that
  were wrong or irrelevant?
- **Cost:** minutes per review, context-shuffling friction, API spend.

## Graduation trigger → ADR

Promote to a ratified practice (a numbered methodology practice + a
decision-guide row, recorded in an ADR, mirroring how every other
practice was added) **only when** the log shows it catching defects the
same-model path misses at an acceptable false-positive rate, across more
than one repo.

**That graduating ADR generalizes *both* review roles to be
model-agnostic — by deliberate, deferred decision.** The author-model
reviewer ([ADR 0021](../../adr/0021-shared-claude-pr-review-workflow.md))
is today vendor-bound in CI (`anthropics/claude-code-action`, the
`ANTHROPIC_API_KEY` secret, the Claude GitHub App); its review *prompt*
is already model-neutral, but its *binding* is not. Rather than refactor
that live, cross-repo CI path now — and churn it twice — the graduating
ADR reworks both reviewers together on the same pattern:

- **The model-neutral review policy is the shared, durable artifact** —
  one prompt, no vendor assumptions (both the author-model prompt above
  and the adversary prompt already meet this).
- **Each provider is a thin, swappable binding** that feeds that policy
  to a concrete action — today an *author-model binding* (Claude,
  `claude-code-action`) and an *adversary-model binding* (Gemini,
  [`run-gemini-cli`](https://github.com/google-github-actions/run-gemini-cli)
  or the Antigravity **`agy`** CLI headless with an API key). Swapping or
  upgrading either model is a one-binding edit; the policy is untouched.

The result is the exact mirror of ADR 0021's shared reviewer — advisory,
not a gate, tuned in one place — for both roles, with the model behind
each one swappable. That is a deliberate, ADR-gated step, **not** part of
this trial.

If the log shows weak signal or heavy noise after a fair run, delete this
directory and record the negative result in an ADR — a defended "no" is
also a result worth keeping.
