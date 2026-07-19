---
name: plan-options
description: Diverge before converging — fan out independent divergers to draft an options doc (≥2 genuinely different approaches) in planning/<slug>/options.md (planning.md §3). Use when choosing among approaches, when only one solution is on the table and it hasn't been challenged, or for any brainstorming request about how to solve a stated problem.
---

# plan-options — diverge before you converge

Drafts `planning/<slug>/options.md`: at least two genuinely different
approaches with trade-offs and win-conditions, converged from at the
last responsible moment. This is brainstorming made rigorous: the value
is the written set of options, not the ideation session.

## Setup

1. `METHODOLOGY_HOME` defaults to `~/Developer/methodology`. Read
   `$METHODOLOGY_HOME/templates/planning/options.md` and, if unfamiliar,
   planning.md §3.
2. Slug from arguments or ask. Read `planning/<slug>/brief.md` and
   `pr-faq.md` if present — the divergers get the *problem*, never a
   preferred solution. If the user has already named a favorite
   solution, strip it from what the divergers see; it re-enters as one
   option among peers.
3. **Ceremony check.** If there is genuinely only one sane approach and
   the user knows it, say so — go to the spec. Stop.

## Diverge — independent stances, in parallel

Spawn one subagent (Agent tool) per stance, **in parallel, each blind to
the others**, with only the problem context (brief, PR-FAQ, relevant
repo facts). Default stances — adjust to the domain, keep them genuinely
opposed:

1. **Boring** — the smallest change with proven, already-present
   technology; optimize for reversibility and time-to-shipped.
2. **Reuse** — don't build it: an existing tool, library, service, or
   process change that makes the problem go away.
3. **Structural** — solve the *class* of problem properly, accepting
   more up-front cost; optimize for where the system should be in two
   years.
4. **Contrarian** (always include) — argue the bet shouldn't be placed:
   the problem is misframed, the status quo is acceptable, or a cheaper
   reframing dissolves it.

Each diverger returns one option in the template's shape: what,
attractive-because, trade-offs/risks, wins-when.

## Converge — with the user, at the last responsible moment

- **Check for genuine difference.** If two options are restatements of
  one idea, merge them and say so — and note it: whether single-model
  divergers actually diverge is the question this spike exists to
  answer.
- Assemble the comparison table (cost/appetite, risk, reversibility).
- Draft the recommendation **with the user** — theirs, not the
  divergers' vote. Carry the runner-up's best ideas into it. The
  contrarian's case, if not taken, gets answered in writing, not
  dropped.
- Remind: the rejected options become the ADR's "alternatives
  considered" when the choice is made (methodology.md §1).

Status starts at `Open`; the human sets `Converged`.

## Output

Write only `planning/<slug>/options.md`. Present, iterate, and suggest
next steps: `plan-bet` (is it worth the capacity?) and `plan-premortem`
(what kills the chosen approach?).
