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
| 2026-06-20 | opn-mcp PR #15 (ADR 0008, the dedup) | Design decision | PUSH BACK | **Partly** — 2 real bugs the removal introduced (dropped daily-task settings in MONITORING.md; stale "templates" wording in README), + a fair design pushback (generate+CI-check was equally ADR-0022-compliant; removal was a preference, not a mandate) | 0 — the UX pushback is a legitimate preference, not a false finding | Adversary on the author model's own fix-PR. Outcome: 2 bugs fixed; design **answered, not reversed** — removal held on scale-to-work grounds, ADR 0008 revised to be honest about the trade. Shows PUSH BACK working as "justify or change," not "must change." Detail: opn-mcp `docs/reviews/pr15_adversarial_review.md`. |

## Running tally

- **Runs:** 4 — across 2 repos (opn-mcp ×3, methodology ×1); modes: 2 code review, 2 design decision; 1 retrospective + 3 pre-merge.
- **Verdicts:** 2 BLOCK (both held up as real defects), 1 PUSH BACK (2 real bugs + a fair design challenge), 1 NO STRONG OBJECTION (clean re-review).
- **Clear false positives:** 0 across all four runs.
- **Signal so far:** strong and consistent. The two BLOCKs caught real defects — including a self-consistency flaw in the author model's *own methodology design* (round 3) that a same-model reviewer shares and would have merged. The PUSH BACK (round 4) surfaced two genuine bugs and forced an explicit justification of a design choice (answered, not reversed) — the verdict scale discriminating honestly across BLOCK / PUSH BACK / NO STRONG OBJECTION. Two repos, zero false positives. **This meets the graduation bar** the README set (real defects the same-model path misses, acceptable false-positive rate, >1 repo); next step is the graduating ADR that ratifies the practice and generalizes both review roles model-agnostically.
