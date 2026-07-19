---
name: plan-premortem
description: Test the riskiest assumptions before committing — run a red-team pre-mortem ("assume it failed, why?") into planning/<slug>/premortem.md, with time-boxed spikes proposed for the most dangerous assumptions (planning.md §5). Use before freezing a spec, after choosing an approach, or whenever someone asks "what could go wrong with this plan".
---

# plan-premortem — assume it failed, work backward

Drafts `planning/<slug>/premortem.md`: failure modes stated as fact, the
load-bearing assumptions behind them rated for confidence and impact,
and time-boxed spikes proposed to retire the dangerous ones. The point
is to kill a bad bet on paper or in throwaway code — never in
production.

## Setup

1. `METHODOLOGY_HOME` defaults to `~/Developer/methodology`. Read
   `$METHODOLOGY_HOME/templates/planning/premortem.md` and, if
   unfamiliar, planning.md §5.
2. Slug from arguments or ask. Read the sibling planning artifacts —
   the pre-mortem targets the *chosen approach* (options doc) and the
   *promised outcome* (PR-FAQ).
3. **Ceremony check.** Trivial or easily-reversed work → skip the
   pre-mortem; say so and stop.

## Red-team fan-out

Spawn subagents (Agent tool) **in parallel, each blind to the others**,
each writing the same fiction — "it is a year later; the bet shipped
and failed; write the honest postmortem" — through a different lens:

1. **Technical** — it broke: scaling, integration, data, the load-bearing
   dependency that didn't hold.
2. **Human / adoption** — it worked and nobody used it, or the team
   couldn't sustain it: friction, habits, maintenance, the person it
   quietly relied on.
3. **External** — the world moved: the dependency changed license or
   died, the platform shifted, the deadline that justified it evaporated,
   a cheaper substitute appeared.

Quantity first, judgment after — take everything plausible into the
`"It failed. Why?"` list, blunt and specific.

## Distill — with the user

- Extract the **assumptions** behind the failures ("this fails if we
  assumed X and X is false"), into the template's table, rated
  confidence H/M/L × impact H/M/L.
- For **high-impact / low-confidence** assumptions, propose a
  **time-boxed spike** each: the cheapest disposable experiment that
  retires the unknown. Throwaway code is fine; the finding is the
  deliverable. If asked to run one, keep it in scratch space — spike
  code never lands in the repo, only the finding lands in this artifact.
- Fill **Disposition** with the user: each dangerous assumption is
  **retired** (finding cited), **accepted** (rationale written), or
  **escalated** to the spec's `## Open questions`. No dangling ones.

Status: write `Open`; the human moves it onward.

## Output

Write only `planning/<slug>/premortem.md`. Present, iterate. Next step:
`plan-handoff` once the dangerous assumptions are dispositioned — or
back to `plan-options`/dropping the bet if the pre-mortem gutted the
approach; that is the practice succeeding, cheaply.
