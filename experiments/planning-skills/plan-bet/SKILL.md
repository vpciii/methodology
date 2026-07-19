---
name: plan-bet
description: Price the work before committing — scaffold a bet (appetite + why-now) in planning/<slug>/bet.md (planning.md §4). Use when deciding whether to commit capacity to work, when sequencing competing work, or when someone asks "how long will this take" and the real question is "how much is it worth".
---

# plan-bet — price the work before committing

Scaffolds `planning/<slug>/bet.md`: an explicit appetite (what the work
is *worth* spending, not an estimate of what it costs) and a why-now.
**This is the most human of the practices — the agent scaffolds and
pressure-tests; the appetite and the decision to place the bet are
never the agent's call.**

## Setup

1. `METHODOLOGY_HOME` defaults to `~/Developer/methodology`. Read
   `$METHODOLOGY_HOME/templates/planning/bet.md` and, if unfamiliar,
   planning.md §4.
2. Slug from arguments or ask. Read the sibling planning artifacts —
   the options doc's recommendation (and its cost column) is the main
   input; the PR-FAQ says what success is worth.
3. **Ceremony check.** Trivial work needs no bet. Say so and stop.

## Drafting discipline

Ask, don't assume — these are the user's answers to elicit:

- **Appetite** — "How much is solving this worth to you — a day, a
  week, a month?" Push back on estimate-speak: the appetite is a
  budget; *scope flexes to fit it*, never the reverse. If the chosen
  option can't plausibly fit the stated appetite, surface the conflict
  now — shrink the slice or re-open the options doc.
- **Why now** — the cost of delay, and what this displaces. If nothing
  makes now better than later, write that honestly; "not now" is a
  legitimate disposition.
- **In / out** — the slice that fits the appetite, and what is
  explicitly cut to make it fit. Be concrete; this feeds the spec's
  `## Non-goals` and `## Out of scope`.
- **Done looks like** — the signal the bet paid off, sharp enough to
  later become success criteria. "We'll know because…" not "it's
  better."
- **No-go conditions** — what would stop the bet mid-flight. Every bet
  should have at least one.

Pressure-test the draft: if the pre-mortem exists, check the bet
acknowledges its high-danger assumptions; if the appetite covers spikes
(planning.md §5), say what part of the budget they get.

Status: write `Proposed`. Only the human sets `Placed`.

## Output

Write only `planning/<slug>/bet.md`. Present, iterate. Next steps:
`plan-premortem` if dangerous assumptions are untested, or
`plan-handoff` when the bet is placed and the path is clear.
