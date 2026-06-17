# Experiment: cross-model adversarial review

> **Status: TRIAL — not a ratified practice.** This is a manual process
> being evaluated. It is deliberately *not* in `methodology.md`'s numbered
> practices or the decision guide, and it carries **no adoption
> obligation** for any project. If it proves out, it graduates to an ADR
> (the trigger below); if it doesn't, this directory is deleted. Nothing
> here gates a merge.

## What we're testing

A *second, different* model reviews work the first model produced —
Claude implements and reviews its own work (the existing Claude PR
reviewer, [ADR 0021](../../adr/0021-shared-claude-pr-review-workflow.md));
Google Antigravity (Gemini 3) plays the adversary. The bet: a same-model
reviewer shares the author's blind spots, so it systematically misses a
class of defect that a different model — with different training,
priors, and failure modes — would catch.

The relationship is **adversarial by design**. The adversary is prompted
to refute, not to bless: find the missing test, break the unstated case,
steelman the rejected ADR alternative. The two models disagreeing in
front of the human is the product. **The human stays the author of
record and adjudicates every finding** — the adversary advises, it never
decides or merges.

Scope is both halves of the lifecycle this methodology already names:
**code review** (a diff against its spec) and **design decisions** (an
ADR, spec, or planning option before sign-off).

## How to run it (manual)

1. Claude produces the work (a PR, or an ADR/spec draft) as usual.
2. Open the work in **Antigravity** (IDE) or via the **`agy` CLI**, with
   a `GEMINI_API_KEY` / `ANTIGRAVITY_API_KEY` in the environment.
3. Paste [`adversary-prompt.md`](./adversary-prompt.md) — the shared
   framing plus the **Code review** or **Design decision** block — and
   give it the inputs that block lists (the diff/draft, the spec, the
   relevant ADRs, the glossary, the Definition of Done).
4. Take the adversary's verdict (**BLOCK** / **PUSH BACK** / **NO STRONG
   OBJECTION**) back to Claude. Resolve each finding into one of: a test,
   an ADR, a spec edit, or a *defended* "no change."
5. Log the round (below).

## Trial log — the evidence the eventual ADR needs

Keep a running [`log.md`](./log.md) (create on first use), one row per
review, so the graduate-or-kill decision rests on data, not vibe:

| Date | Repo / PR or ADR | Mode | Adversary verdict | Did it catch something Claude's reviewer + CI missed? | False positives | Friction notes |
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
than one repo. That ADR also decides the **automation rollout**, for
which the path already exists:

- Google's [`run-gemini-cli`](https://github.com/google-github-actions/run-gemini-cli)
  action does Gemini PR review in CI.
- The Antigravity **`agy`** CLI runs headless with an API key.

Either could become a *reusable adversary workflow* in this repo, the
exact mirror of [ADR 0021](../../adr/0021-shared-claude-pr-review-workflow.md)'s
shared Claude reviewer — advisory, not a gate, tuned in one place. That
is a deliberate, ADR-gated step, **not** part of this trial.

If the log shows weak signal or heavy noise after a fair run, delete this
directory and record the negative result in an ADR — a defended "no" is
also a result worth keeping.
