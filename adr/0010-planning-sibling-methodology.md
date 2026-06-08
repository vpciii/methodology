# ADR 0010: Planning as a sibling methodology

- **Status:** Accepted
- **Date:** 2026-06-08
- **Deciders:** vpc

## Context

`methodology.md` deliberately starts at the spec: it covers how to
**build the thing right**. Everything *upstream* of the spec — deciding
**whether** to build, **what** to build, and **which** of several
approaches to take — had no home in the methodology. The spec template
(`templates/spec/spec.md`) assumes the "what" is already chosen; how a
team arrives at it was unaddressed.

The question surfaced as "should we add brainstorming to the
methodology?" Examined against the methodology's own bar — durable,
artifact-producing primitives with named origins and a "why this lasts" —
"brainstorming" as such fails it: it is an *activity, not an artifact*
(the doc's thesis is "document the artifact, not the tool/activity"); its
empirical pedigree is weak (classic group brainstorming is undercut by
the nominal-group research); and its useful outputs are already captured
by ADR "alternatives considered" (§1) and the spec's "why" (§2).

But the question points at a real, recurring seam: the pre-spec phase of
problem-framing, option-generation, and betting. Leaving it undocumented
means each project reinvents that phase ad hoc, and the divergent
thinking that should feed an ADR's alternatives is lost.

## Decision

We will add a **sibling methodology document, `planning.md`**, covering
the pre-spec phase, parallel in form and rigor to `methodology.md`.

- It holds **five artifact-producing practices** — frame the problem
  before the solution (problem brief); work backwards from the outcome
  (PR-FAQ); diverge before converging (set-based options doc); price the
  work before committing (a bet with appetite); test the riskiest
  assumptions (pre-mortem + spikes) — each with a named origin, a "why
  this lasts," and a durable markdown artifact.
- It **converges to a `spec.md`**: the seam between the two documents.
  Planning artifacts live in **`planning/<slug>/`** (sibling to
  `specs/<slug>/`) and **freeze** when the spec is created, mirroring
  spec-freeze (`methodology.md` §2).
- It **shares this repository's SemVer track and `CHANGELOG.md`** (ADR
  0009): one repo, one version. Adding it is a minor bump (0.2.0).

This is the rigorous, artifact-producing home for the "brainstorming"
impulse — practice 3 (set-based divergence) — without adopting
brainstorming as a loose activity.

## Alternatives considered

- **Add "brainstorming" as a 12th practice to `methodology.md`** —
  rejected: an activity, not a durable artifact; weak empirical backing
  relative to the other practices; its outputs are already captured by
  ADR alternatives and the spec's "why."
- **Do nothing; treat the pre-spec phase as out of scope** — rejected:
  the seam is real and recurring, and silence means every project
  reinvents discovery ad hoc and discards the option-reasoning that
  should feed ADRs.
- **Fold the pre-spec practices into `methodology.md`** — rejected: a
  different audience (product/strategy vs. engineering), a different
  cadence, and a different output (bets and decisions vs. code) would
  dilute the tight, code-artifact focus that makes `methodology.md` good.
- **A separate repository for planning** — rejected for now: a second
  versioning stream and a second orientation pointer is overhead a
  handful of projects don't need. Reversible: split it out later if
  planning grows a genuinely distinct audience (§11).
- **A separate SemVer track for `planning.md`** — rejected: one
  repo/one version is simpler for consumers to pin and track; revisit if
  the two documents come to evolve at very different rates.
- **Fold pre-spec docs into `specs/<slug>/` instead of a new folder** —
  rejected: mixes "whether/what to build" with "how to build" in one
  folder; a sibling `planning/<slug>/` keeps the seam legible.

## Consequences

- The pre-spec phase has a durable home; discovery and option-generation
  become artifact-producing, and the handoff to `spec.md` is explicit.
- The repository now hosts **two** methodologies under one version; the
  "keep artifacts honest" discipline (same-PR doc updates) spans both.
  `methodology.md`'s "only methodology document" line is retired.
- Cost: a second methodology document to maintain, and a standing risk of
  planning-ceremony creep — mitigated by the scale-to-work rule and the
  "What is intentionally not here" section in `planning.md`.
- New constraint: a methodology change that touches the pre-spec phase
  now belongs in `planning.md` (with its own ADR), not `methodology.md`.

## Adoption impact

**Reference-only** for existing projects — nothing to change today.
`planning.md` arrives by reading, like `methodology.md`. The
`planning/<slug>/` artifact home is an **opt-in convention** a project
uses when it takes on a genuinely uncertain or expensive bet; trivial or
obvious work still goes straight to a spec. Matching templates under
`templates/planning/` are a deliberate follow-up, not part of this
change.

## References

- `planning.md` (the document this ADR adopts).
- `methodology.md` §2 (spec-first — the seam), §1 (ADRs / alternatives
  considered), "A note on practice vs. ceremony," "What is intentionally
  not here."
- ADR 0009 (methodology as a versioned dependency — shared SemVer and
  `CHANGELOG.md`); ADR 0001 (reference, don't vendor).
- Origins cited in `planning.md`: Christensen (JTBD); Bryar & Carr,
  *Working Backwards*; Ward/Sobek/Liker (set-based concurrent
  engineering); Reinertsen, *Product Development Flow* / Basecamp,
  *Shape Up* (appetite); Klein (pre-mortem); Hunt & Thomas (spikes).

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
