# Adversarial review — trial log

One row per cross-model adversarial review run, per the trial guide
([README.md](./README.md)). Detailed per-review write-ups live in the
reviewed project (e.g. a `docs/reviews/` file in that repo); this log is
the aggregate evidence for the graduate-or-kill decision.

| Date | Target | Mode | Verdict | Caught something the author model + CI missed? | False positives | Notes |
|---|---|---|---|---|---|---|
| 2026-06-20 | opn-mcp PR #13 (retrospective) | Code review | BLOCK | **Yes** — stale `docs/scheduled-tasks/` setup templates recreate the bug #13 fixed for any new operator; missed by CI and the same-model reviewer on #13 | 0 (one finding self-labeled a hunch) | First run. Adversary: Antigravity / Gemini. Detail: opn-mcp `docs/reviews/pr13_adversarial_review.md`. Corrective fix: opn-mcp PR #14. |
| 2026-06-20 | opn-mcp PR #14 (re-review of the #13 fix) | Code review | NO STRONG OBJECTION | n/a — re-review: confirmed the BLOCK and test-gap resolved; reiterated 2 known non-blocking follow-ups (timezone-coupled poll, remove/reinstall hunch) | 0 | Dogfood — adversary on the author model's own fix. Detail: opn-mcp `docs/reviews/pr14_adversarial_review.md`. |

## Running tally

- **Runs:** 2
- **BLOCKs that held up as real defects:** 1 / 1
- **Clear false positives:** 0 across both runs (one round-1 finding self-labeled a hunch)
- **Signal so far:** round 1 found a real, user-facing defect the same-model
  reviewer and deterministic CI both missed; round 2 cleanly verified the
  fix and self-cleared (NO STRONG OBJECTION) without inventing objections —
  the trial's core hypothesis supported, and the verdict scale behaving
  honestly. Still one repo; needs more runs (ideally a *pre*-merge review
  and a second repo) before the graduation trigger is met.
