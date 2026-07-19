---
name: plan-handoff
description: Converge planning to a spec — draft specs/<slug>/spec.md from the planning/<slug>/ artifacts and freeze them (planning.md, Scope). Use when a bet is placed and it's time to hand off to the development methodology, or when someone asks to "turn this planning into a spec".
---

# plan-handoff — converge to a spec

Planning's exit criterion: a `specs/<slug>/spec.md` ready to enter
`Draft` under the development methodology. This skill drafts it from the
planning artifacts and closes out the planning record. From here,
`methodology.md` (and any orchestration over it, e.g. agent-framework)
takes over.

## Setup

1. `METHODOLOGY_HOME` defaults to `~/Developer/methodology`. Read
   `$METHODOLOGY_HOME/templates/spec/spec.md` and planning.md's "Scope —
   where planning ends" table.
2. Slug from arguments or ask. Read **all** artifacts in
   `planning/<slug>/`.

## Readiness check — before drafting anything

Planning must have *converged*, not merely accumulated documents:

- An approach is chosen (options doc recommendation accepted, or the
  path was obvious enough to skip it).
- The bet is `Placed` — the human has committed an appetite. If not,
  stop and point to `plan-bet`.
- The pre-mortem's high-danger assumptions are dispositioned (retired /
  accepted / escalated) — dangling ones block the handoff or become
  `## Open questions` explicitly, with the user's agreement.

Not every bet has all five artifacts — that's fine (ceremony scales).
Flag only what's *missing and needed*, don't demand the full set.

## Draft the spec

Map planning → spec per planning.md's table:

| From | Into `spec.md` |
|---|---|
| Brief | `## Problem` (solution-free, condensed) |
| PR-FAQ | `## Goals` (the press release's outcome, as ordered goals), `## Non-goals` (what it deliberately doesn't do) |
| Bet — in/out | `## Non-goals`, `## Out of scope (for now)` |
| Bet — done looks like | seeds for `## Success criteria` |
| Pre-mortem — escalated items; PR-FAQ unanswered questions | `## Open questions` |
| Options — the winner | informs `plan.md` later; **not** pasted into the spec |

Then draft `## Requirements` (`R-…`, RFC 2119) and `## Success criteria`
(`SC-…`) with the user — this is new authorship, not transcription:
every `MUST`/`MUST NOT` must be reflected in at least one criterion
(ADR 0011), and criteria must be concrete enough to be verified by a
test that cites the id. Leave `## Traceability` as the empty scaffold.

Spec status: `Draft`. The human signs off before anything downstream
happens.

## Close out the planning record

With the user's confirmation, update the planning artifacts' statuses to
their terminal values (brief `Validated`, PR-FAQ `Approved`, options
`Converged`, bet `Placed`, pre-mortem per its disposition) — they now
freeze as the historical record of the bet (planning.md, Scope). A
contradiction found later goes to a new spec or ADR, never back into
them.

Two reminders to surface, not perform:

- If the chosen approach is expensive to reverse or future-constraining,
  it needs an **ADR** — the options doc's rejected siblings are its
  "alternatives considered" ready-made.
- If the project uses an adversarial spec review (different lineage,
  design-mode) for substantial/risky specs, this spec is the input to it
  **before** decomposition into tasks.

## Output

Write `specs/<slug>/spec.md` (draft) and the status-line updates to the
`planning/<slug>/` artifacts — nothing else. Present the spec for the
human's review; the handoff is complete when *they* move it forward.
