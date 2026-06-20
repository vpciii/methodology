# Adversarial review — trial log

One row per cross-model adversarial review run, per the trial guide
([README.md](./README.md)). Detailed per-review write-ups live in the
reviewed project (e.g. a `docs/reviews/` file in that repo); this log is
the aggregate evidence for the graduate-or-kill decision.

| Date | Target | Mode | Verdict | Caught something the author model + CI missed? | False positives | Notes |
|---|---|---|---|---|---|---|
| 2026-06-20 | opn-mcp PR #13 (retrospective) | Code review | BLOCK | **Yes** — stale `docs/scheduled-tasks/` setup templates recreate the bug #13 fixed for any new operator; missed by CI and the same-model reviewer on #13 | 0 (one finding self-labeled a hunch) | First run. Adversary: Antigravity / Gemini. Detail: opn-mcp `docs/reviews/pr13_adversarial_review.md`. Corrective fix: opn-mcp PR #14. |

## Running tally

- **Runs:** 1
- **BLOCKs that held up as real defects:** 1 / 1
- **Clear false positives:** 0 (Finding 4 was honestly self-labeled a hunch)
- **Signal so far:** the first pass found a real, user-facing defect the
  same-model reviewer and deterministic CI both missed — the trial's core
  hypothesis, supported at n=1. Needs more runs (and more than one repo)
  before the graduation trigger is met.
