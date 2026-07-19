---
name: plan-prfaq
description: Work backwards from the outcome — draft a PR-FAQ (press release + skeptic's FAQ) in planning/<slug>/pr-faq.md (planning.md §2). Use after a problem brief exists, when deciding whether an outcome is worth wanting before committing to build it, or when someone asks "write the pitch/announcement first".
---

# plan-prfaq — work backwards from the outcome

Drafts `planning/<slug>/pr-faq.md`: the announcement of the work's
success, plus the hard questions a skeptic would ask. If the outcome
isn't worth wanting once written plainly, the bet stops here — for free.

## Setup

1. `METHODOLOGY_HOME` defaults to `~/Developer/methodology`. Read
   `$METHODOLOGY_HOME/templates/planning/pr-faq.md` and, if unfamiliar,
   planning.md §2.
2. Slug from arguments or ask. Read `planning/<slug>/brief.md` first if
   it exists — the press release's "problem" paragraph should restate
   the brief, not invent a new problem. If no brief exists and the bet
   seems uncertain, suggest `plan-brief` first (but don't insist).
3. **Ceremony check.** Obvious or trivial work → go straight to the
   spec or the commit. Say so and stop.

## Drafting discipline

**Press release** — write it as already shipped, one page, in language
the affected user would understand (no internal jargon). The discipline:
concrete world-after, not aspiration. "Deploys take four minutes" beats
"deployment is dramatically improved."

**FAQ — run a real skeptic, not a friendly one.** After drafting the
press release, spawn a subagent (Agent tool) with only the press release
and brief as context, prompted as a skeptic whose job is to find the
questions the author hopes nobody asks — cost, who loses, what breaks,
why the status quo is actually fine, what has to be true, why this fails.
Take its hardest 5–8 questions into the FAQ. Then answer them **with the
user, honestly**:

- A question with a good answer → write it in.
- A question with no good answer yet → keep it in the FAQ with the
  honest non-answer; it will feed the spec's `## Open questions` or the
  pre-mortem.
- A question that guts the pitch → say so plainly. Stopping here is the
  PR-FAQ working as designed, not a failure.

Always include the template's three standing questions (what it
deliberately does *not* do; what has to be true; why it might fail).

Status starts at `Draft`. Only the human moves it onward.

## Output

Write only `planning/<slug>/pr-faq.md`. Present, iterate, and suggest
next steps: `plan-options` (how), `plan-premortem` (what kills it), or a
deliberate stop.
