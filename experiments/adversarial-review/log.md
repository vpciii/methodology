# Adversarial review — trial log

One row per cross-model adversarial review run, per the trial guide
([README.md](./README.md)). Detailed per-review write-ups live in the
reviewed project (e.g. a `docs/reviews/` file in that repo); this log is
the aggregate evidence for the graduate-or-kill decision.

| Date | Target | Mode | Verdict | Caught something the author model + CI missed? | False positives | Notes |
|---|---|---|---|---|---|---|
| 2026-06-20 | opn-mcp PR #13 (retrospective) | Code review | BLOCK | **Yes** — stale `docs/scheduled-tasks/` setup templates recreate the bug #13 fixed for any new operator; missed by CI and the same-model reviewer on #13 | 0 (one finding self-labeled a hunch) | First run. Adversary: Antigravity / Gemini. Detail: opn-mcp `docs/reviews/pr13_adversarial_review.md`. Corrective fix: opn-mcp PR #14. |
| 2026-06-20 | opn-mcp PR #14 (re-review of the #13 fix) | Code review | NO STRONG OBJECTION | n/a — re-review: confirmed the BLOCK and test-gap resolved; reiterated 2 known non-blocking follow-ups (timezone-coupled poll, remove/reinstall hunch) | 0 | Dogfood — adversary on the author model's own fix. Detail: opn-mcp `docs/reviews/pr14_adversarial_review.md`. |
| 2026-06-20 | methodology PR #18 (ADR 0022, single-source rule) | Design decision | BLOCK | **Yes** — the drafted rule contradicted the methodology's *own* practices: hand-synced curated summaries (ADR 0018) and per-project instantiated templates (ADR 0009) would all be non-compliant. A self-consistency hole the author and a same-model review would likely have merged | low — 4/5 findings strong; one ("reverse-engineered from one incident") weak/partial, not a false positive | Design-mode review via `agy` CLI; adversary on the author model's own methodology ADR. Resolved by scoping the rule to *verbatim* duplication + carving out derivatives (revised on PR #18). Detail: methodology `docs/reviews/pr18_adversarial_review.md`. |

## Running tally

- **Runs:** 3 — across 2 repos (opn-mcp, methodology); modes: 2 code review, 1 design decision; 1 retrospective + 2 pre-merge.
- **BLOCKs that held up as real defects:** 2 / 2 (opn-mcp #13 stale templates; methodology #18 self-contradicting rule).
- **Clear false positives:** 0 across all three runs (one round-1 hunch self-labeled; one round-3 finding weak but partially valid).
- **Signal so far:** strong. Round 1 caught a real user-facing defect; round 2 verified the fix and self-cleared without inventing objections; round 3 caught a genuine self-consistency flaw in the *author model's own methodology design* — exactly the blind spot a same-model reviewer shares and would have merged. Two repos, two real BLOCKs, zero false positives, honest verdict scale. Approaching the graduation threshold; a clean pre-merge review on an unrelated fresh decision would seal it.
