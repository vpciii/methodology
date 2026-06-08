# Planning

A small set of practices for deciding **what** to build, **whether** to
build it, and **which** of several approaches to take — *before* a spec
exists. None of them depend on a particular language, framework, editor,
or AI tool. All of them are markdown and git — the same durable substrate
as the development methodology.

`methodology.md` deliberately starts at the spec: it is how you **build
the thing right**. This document covers the half that comes first —
**building the right thing** — and ends exactly where `methodology.md`
begins. The handoff artifact between them is a `spec.md`.

The rule of thumb mirrors the development methodology: **document the
artifact, not the activity.** A problem brief, an options doc, and a
written bet outlive any workshop, whiteboard, or ideation tool. "We
brainstormed" leaves nothing behind; the artifact does.

## A note on practice vs. ceremony

Planning is where ceremony metastasizes fastest — roadmaps nobody keeps,
discovery for its own sake, estimation theater. The discipline these
artifacts encode matters more than the artifacts themselves. A planning
phase that does not converge to either a spec or a deliberate "no" is
waste, however many documents it produced.

**Scale the ceremony to the work.** Most work does not need all five
practices below. An obvious change goes straight to a `spec.md` (or, if
trivial, straight to the commit). The practices earn their keep on bets
that are *genuinely uncertain* (we don't yet know what to build) or
*expensive to commit* (significant capacity, hard to unwind). Apply
judgment.

---

## Scope — where planning ends

Planning **converges to a spec.** Its exit criterion is a `spec.md` ready
to enter `Draft` under the development methodology. Concretely, the
planning artifacts feed the spec like this:

| Planning artifact | Feeds | In `spec.md` |
|---|---|---|
| Problem brief | the problem, solution-free | `## Problem` |
| PR-FAQ / pitch | what success looks like | `## Goals`, `## Non-goals` |
| Options doc (the winner) | chosen approach + the rejected ones | `plan.md` + ADR "alternatives considered" |
| Bet (appetite + why-now) | how much scope is worth it | `## Non-goals`, `## Out of scope` |
| Pre-mortem + spike findings | retired or surfaced unknowns | `## Open questions` |

Once the spec exists, the development methodology takes over and the
planning artifacts **freeze** into a historical record of the bet that
was made — mirroring spec-freeze (`methodology.md` §2). A contradiction
discovered later does not get edited back into the pitch; it flows to a
new spec, an ADR, or the operational-feedback loop.

### Decision guide — which artifact, when

| If you are about to… | Produce… | Where |
|---|---|---|
| Decide whether a problem is worth solving at all | a problem brief (solution-free) | `planning/<slug>/brief.md` |
| Pin down what the world looks like if you succeed | a PR-FAQ / pitch | `planning/<slug>/pr-faq.md` |
| Choose among genuinely different approaches | an options doc (≥2 approaches) | `planning/<slug>/options.md` |
| Commit scarce capacity to a bet | a bet: appetite + why-now | `planning/<slug>/bet.md` |
| De-risk before committing to build | a pre-mortem + spike findings | `planning/<slug>/premortem.md` |
| Hand off to implementation | a spec (development methodology takes over) | `specs/<slug>/spec.md` |
| Make an obvious or throwaway change | nothing — go straight to the spec or the commit | — |

Templates for each artifact live in `$METHODOLOGY_HOME/templates/planning/`.

---

## The practices

### 1. Frame the problem before the solution

Write down the problem — who feels it, how you know, why now — *without*
naming a remedy. The brief is solution-free on purpose: it is the thing
you validate before spending a single hour on "how."

- Origin: Jobs-To-Be-Done — Clayton Christensen, *Competing Against
  Luck* (2016); the "fall in love with the problem, not the solution"
  posture.
- Durable artifact: a **problem brief** — problem, who notices it,
  evidence, why now. (This is the upstream, broader sibling of a
  `spec.md` `## Problem`: it also asks *whether to act at all*.)

Why this lasts: solving the wrong problem precisely is the most expensive
mistake in software. Reframing a problem on one page is cheap; reframing
it after it is built in code is ruinous.

### 2. Work backwards from the outcome

Before committing to the work, write the announcement of its success: a
short internal press release plus the FAQ a skeptic would ask. If the
outcome is not worth wanting once written plainly, stop here — for free.

- Origin: Amazon's *Working Backwards* (Bryar & Carr, 2021), the PR-FAQ.
  Kin to the Readme-Driven Development already cited for spec-first
  (`methodology.md` §2) — same move, one step upstream.
- Durable artifact: a **PR-FAQ / pitch** — one page describing the world
  after success and the hard questions about getting there.

Why this lasts: writing the outcome first surfaces whether it is worth
wanting *before* any cost is sunk. The narrative is plain prose — it
survives every tool change and reads the same to a human or an agent.

### 3. Diverge before you converge

Generate at least two genuinely different approaches and keep them alive
until the last responsible moment. This is "brainstorming," made rigorous
and artifact-producing: the value is not the act of generating ideas, it
is the **written set of options with their trade-offs** that you converge
*from*.

- Origin: set-based concurrent engineering — Ward, Sobek & Liker, "The
  Second Toyota Paradox" (1995); converge late rather than committing to
  the first plausible design.
- Durable artifact: an **options doc** — ≥2 approaches, each with its
  trade-offs and the conditions under which it wins. The chosen option's
  rejected siblings become the ADR's "alternatives considered"
  (`methodology.md` §1), so the divergence is preserved, not discarded.

Why this lasts: committing to the first plausible option is the most
common planning failure. Carrying a small set of options briefly, and
converging late with the reasoning written down, beats early lock-in —
independent of any ideation tool or workshop format.

### 4. Price the work before committing

Decide how much a bet is *worth* before deciding how to do it. Fix an
**appetite** (the capacity you are willing to spend) rather than asking
for an open-ended estimate, and make the cost of delay explicit so
sequencing is a decision, not a default.

- Origin: Cost of Delay / WSJF — Don Reinertsen, *Principles of Product
  Development Flow* (2009); appetite — Basecamp, *Shape Up* (2019).
- Durable artifact: a **bet** — an explicit appetite (e.g. "two weeks,
  one engineer") and a why-now, recorded alongside the pitch.

Why this lasts: capacity is always scarce, so sequencing is the real
decision. Making appetite and cost-of-delay explicit beats gut-feel
roadmaps and outlives any planning tool or ticketing system.

### 5. Test the riskiest assumptions before committing

Before freezing a spec, name the assumptions the bet depends on and probe
the most dangerous ones cheaply. A pre-mortem surfaces them; a time-boxed
spike retires them. The point is to kill a bad bet on paper or in a
throwaway prototype — never in production.

- Origin: the pre-mortem — Gary Klein, *Harvard Business Review* (2007);
  spikes and tracer bullets — Extreme Programming and Hunt & Thomas, *The
  Pragmatic Programmer* (1999).
- Durable artifact: a **pre-mortem note** ("assume it failed — why?") and
  **spike findings** that either retire an unknown or escalate it into the
  spec's `## Open questions`.

Why this lasts: the cheapest place to kill a bad bet is before code.
Surfacing assumptions and probing them with disposable experiments is a
discipline, not a brand — it survives every framework that packages it.

---

## The artifacts as a durable interface

Like the development methodology, planning produces a small set of plain
markdown artifacts — a brief, a pitch, an options doc, a bet, a
pre-mortem. They are the durable, tool-independent record of *why this
work was chosen over the alternatives*, readable by a human or an agent
long after the workshop is forgotten.

**Optional planning tools are welcome but disposable.** If a discovery
framework, an AI agent generating and scoring options, or a whiteboarding
tool helps you draft these artifacts, use it — provided it only reads and
writes the canonical artifacts above. The day the tool is retired, you
lose an editor, not the decision trail.

---

## What is intentionally not here

- **No estimation theater.** Appetite (how much it is worth) over
  open-ended estimates and story-point accounting.
- **No roadmap-as-contract.** Sequencing is a living decision, not a Gantt
  chart promised to a date.
- **No personas or role-play workflows** — framework-flavored; the
  artifacts give the benefit without the lock-in (mirrors `methodology.md`).
- **No product-management brand vocabulary** (Scrum, SAFe, etc.). Useful
  inspirations; none of it is load-bearing.
- **No discovery for its own sake.** Planning that does not converge to a
  spec or a deliberate "no" is waste.

---

## Changing this document

`planning.md` is a sibling to `methodology.md`; the two share this
repository's version and `CHANGELOG.md` (ADR 0009). If a planning
practice changes, update it here and record the change in an ADR under
`adr/`, with its **adoption impact**, and note it in `CHANGELOG.md` under
semantic versioning — so projects adopt it deliberately like any
dependency. As with the development methodology, arguing for or against a
practice that isn't listed here is a sign you need an ADR, not a longer
document.
