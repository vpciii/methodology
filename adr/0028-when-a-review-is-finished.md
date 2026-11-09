# ADR 0028: A review is finished when its must-fix findings are closed

- **Status:** Proposed
- **Date:** 2026-11-09
- **Deciders:** vpc

## Context

ADR 0015 says what a review checks, and ADR 0021 added an advisory AI
reviewer to every PR. Neither says when reviewing stops. With a human
reviewer that rarely matters: attention runs out. An AI reviewer does
not tire, costs about a dollar a run, and reads the whole PR afresh each
time. Asked again, it finds something again.

Evidence:

- **PR #33 (2026-11-09), three runs** of the shared reviewer on the same
  PR ($0.91, $1.09, $1.01). Each run raised three to five findings; none
  repeated; several concerned text the previous run had read without
  comment. There was no run that came back clean, and no rule for
  whether to run a fourth.
- **The findings stayed worth having.** The third run found the most
  serious one of the day (the agent could be asked to print the API key
  into a public comment). A rule that simply caps reviews at one would
  have missed it.
- **Not everything found was this PR's to fix.** Runs flagged
  pre-existing gaps (a README table that had never listed the reviewer
  template; whether CI is a required check). Treating every finding as
  blocking would have grown the PR without end.
- **ADRs 0024 and 0025** each took two rounds ("address review",
  "address second review") before acceptance, and stopped there by the
  human's call.
- **PRs #19, #21, #22 and #24 (June 2026)** went nine adversarial rounds
  across four proposals; each was withdrawn after a BLOCK, the last of
  them a counter-proposal blocked "for milder versions of the same
  sins". Review there converged only by the human stopping it.

The methodology already says who decides (the human is the author of
record, and the AI reviewer is advisory). What is missing is the
criterion, so that stopping is a judgment against something and not
fatigue or budget.

## Decision

We will add a short rule to the review guidance in
`templates/project-CONTRIBUTING.md`: **a review is finished when its
must-fix findings are closed, not when a reviewer returns nothing.**

1. **Triage every finding** into one of three, in the PR:
   - **Must fix** — the change is incorrect, breaks its contract (a
     spec criterion, an accepted ADR, the glossary), opens a security
     hole, or makes an artifact false. Fixed in this PR.
   - **Record** — true, but not caused by this PR or not in its scope.
     It goes to the artifact that owns it (an issue, a follow-up PR, a
     dated entry in the spec's Decisions); it does not block the merge.
   - **Decline** — with a one-line reason, posted in the PR beside the
     finding it declines.
2. **Re-review when a fix changed behavior or the contract**, not for
   wording. One re-review is the default; more is the human's call, made
   knowing that a fresh pass will find fresh things.
3. **Say what was not reviewed.** Commits made after the last review are
   named as unreviewed in the PR (the Reviews section of
   `templates/project-CONTRIBUTING.md` already requires each review to
   cite the range it covered).
4. **The human ends it.** An advisory reviewer never gates a merge
   (ADR 0021), and neither does the absence of a clean pass.

## Alternatives considered

- **Review until a pass comes back clean.** The intuitive rule, and the
  one PR #33 was drifting toward. The evidence is that a clean pass does
  not arrive; cost and PR size grow without bound. Rejected.
- **A fixed cap** (one review, or N). Simple and cheap, but the third
  run on PR #33 found the day's most serious defect, and the right
  number depends on what the fixes touched. A default of one re-review
  with the human free to go further keeps the judgment where the
  methodology puts it. Rejected as a rule; kept as the default.
- **Have the reviewer label severity itself.** The shared reviewer's
  prompt could ask for must-fix / record / nit. Worth trying, but it is
  a change to the reviewer's behavior with its own spec and tests, and
  the triage is the human's to own either way. Left as a follow-up.
- **Leave it to judgment, unwritten.** That is the status quo, and it
  worked, at the cost of deciding from scratch each time and of an agent
  that will keep fixing and re-running unless told the criterion.
  Rejected.

## Consequences

- An agent driving a PR has a stopping criterion it can apply and show:
  the triage, in the PR, with the must-fix items closed.
- "Record" can become a place to bury real problems. The check is that
  each recorded finding names where it went.
- Some defects a further pass would have found will ship. That was
  already true; the rule makes the trade explicit instead of implicit.
- A little more writing per review (the triage). For a small PR it is
  three lines.
- Cheap to reverse: supersede this ADR; nothing depends on it.

## Adoption impact

*Per-project action, optional:* copy the **When a review is finished**
subsection from `templates/project-CONTRIBUTING.md` into the project's
`CONTRIBUTING.md`. Projects that call the shared reviewer need no
workflow change.

## References

- ADR 0015 (review checklist), ADR 0021 and ADR 0026 (the shared
  reviewer), ADR 0008 (agent guardrails).
- PR #33 and its three review comments; PRs #19, #21, #22, #24 and
  `docs/reviews/`.
