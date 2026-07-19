---
name: plan-brief
description: Frame a problem before any solution — draft a solution-free problem brief in planning/<slug>/brief.md (planning.md §1). Use at the very start of an uncertain or expensive bet, when someone says "we should build/fix X" and the problem behind X hasn't been written down, or when it's unclear whether a problem is worth solving at all.
---

# plan-brief — frame the problem before the solution

Drafts `planning/<slug>/brief.md`: the problem, who feels it, evidence,
why now — **with no solution named**. This is planning.md §1; the brief
is what gets validated before anyone spends an hour on "how."

## Setup

1. `METHODOLOGY_HOME` defaults to `~/Developer/methodology`. Read
   `$METHODOLOGY_HOME/templates/planning/brief.md` (the template) and,
   if unfamiliar, planning.md §1.
2. Slug: from the arguments, or derive a short kebab-case slug from the
   topic and confirm it with the user. Artifact path:
   `planning/<slug>/brief.md` in the current repo.
3. **Ceremony check first.** If what the user describes is an obvious or
   trivial change (not genuinely uncertain, not expensive to commit),
   say so: it should go straight to a `spec.md` or the commit. Stop.

## Drafting discipline

- **Solution-free is the whole point.** The user will almost certainly
  describe a solution ("we need a caching layer"). Extract the problem
  behind it ("page loads are slow and users notice") and park every
  remedy explicitly: tell the user it's noted for `options.md`, and keep
  it out of the brief.
- **Interrogate, don't transcribe.** For each section, push past the
  first answer:
  - *Who feels it* — a named user, role, or system. "Users" in the
    abstract is a red flag; ask who specifically noticed, and how it
    showed up.
  - *Evidence* — separate **measured** (data, tickets, observed
    behavior) from **suspected**. If everything is suspected, say so in
    the brief plainly; that's a finding, not a failure.
  - *Why now* — a deadline, growing cost, or closing window. If there
    is nothing, write "nothing forces this now" — that too is a
    finding, and a legitimate reason to drop the bet.
  - *Not the problem* — name at least one adjacent problem explicitly
    out of frame, so the brief stays sharp.
- Status starts at `Exploring`. Only the human moves it to `Validated`
  or `Dropped`.

## Output

Write only `planning/<slug>/brief.md`, following the template's
structure exactly. Then present it and iterate until the user accepts.
Suggest the natural next steps: `plan-prfaq` (is the outcome worth
wanting?) or `plan-options` (how might we solve it?) — or dropping the
bet if the brief undermined it, which is the cheapest possible win.
