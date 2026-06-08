# Adopting the methodology

This guide covers bringing an **existing project** onto the methodology.
`methodology.md` and `planning.md` describe steady state — they assume the
artifacts exist and the practices were followed from the start. Most real
projects adopt mid-life, on a codebase with sparse docs and uneven tests,
where "read before you write" has little to read. This is the bootstrap
path from there to steady state.

A greenfield project does not need this guide — start straight from the
templates (see the README's "Adopting it in a project"). This document is
for the brownfield case.

## The principle: forward-only by default

**The methodology applies from the adoption date forward.** You do not
retroactively spec, test, or ADR work that already shipped. Adoption is
not a documentation project, and it never blocks delivery.

- **Don't spec the past.** Code that already exists and isn't changing
  gets no spec. Its *structure* is captured in `docs/architecture.md` and
  its *behavior* by its tests — not by a back-dated `spec.md`.
- **Don't block a fix to backfill.** A change to untested legacy code
  ships with a regression or characterization test and a clear commit
  message — not a freshly invented feature spec.
- **Artifacts accrue on touch.** The first time you change an area, you
  seed only what that change needs — a glossary term, a decision-capture
  ADR, a characterization test — and no more.

Scale-to-work (`methodology.md`) still governs: most legacy changes are
small and need nothing beyond a good commit message.

## Three modes

| Mode | When | What you do |
|---|---|---|
| **Greenfield** | New project | Start from templates; planning (if the bet is uncertain) → spec → seed docs → build. See the README. |
| **Brownfield** | Existing code, adopting now | Seed current-state artifacts (below), then work forward-only from here. |
| **Retroactive** | Only an area you are *actively* changing | Capture the decisions and behavior you are about to depend on — never a blanket backfill. |

## Seed order — what pays rent fastest

Week one, in this order. Each artifact is honestly *partial* and grows as
you touch the system; partial-but-honest beats exhaustive-but-stale.

1. **`docs/architecture.md`** — reverse-engineer the current shape from
   the code: components, boundaries, data stores, external dependencies.
   Mark unknowns as unknown. This is the highest-leverage artifact for
   orienting both humans and agents on a strange codebase. (Template +
   the §"current-state" rule in `methodology.md`.)
2. **`docs/glossary.md`** — record the domain terms already in the code,
   exactly as the code uses them. Capture reality; don't invent synonyms
   or aspirational names.
3. **Decision-capture ADRs** in `docs/adr/` — one short ADR for each
   load-bearing decision already baked in (the datastore, the auth model,
   the framework, a boundary you can't easily cross). Status `Accepted`,
   dated to *now*, with a line noting it **records a pre-existing
   decision** rather than making a new one. You are not re-deciding; you
   are writing down the "why" before it is lost.
4. **CI: spec-criterion coverage on new specs only** — wire the §5
   coverage check so it governs specs created from adoption forward, not
   the entire history.

Stop there. Resist the pull to document everything at once.

## Characterization tests: the brownfield safety net

On legacy code with no tests, the **characterization test** is the entry
point: before changing untested code, write a test that pins its *current*
behavior — whatever it is, even if it looks wrong — then make your change.
It gives a fix or refactor a safety net where no spec ever existed, and it
turns "I think this still works" into a checked fact.

- It is the brownfield form of the regression record (`methodology.md`
  §5): a regression test captures a bug you fixed; a characterization
  test captures behavior you are about to depend on.
- If the pinned behavior turns out to be **wrong**, that is an
  incident-style finding (`methodology.md` §8): the fix ships a regression
  test, and a wrong decision it exposed gets an ADR.

## What adoption is not

- **Not a docs sprint.** No freezing feature work to write specs for
  everything that already shipped.
- **Not retroactive spec-writing.** Shipped code is described by
  `architecture.md` (structure) and its tests (behavior). A spec freezes
  as a historical record of what was *agreed* (`methodology.md` §2); a
  back-dated spec for code that shipped without one is fiction.
- **Not all-or-nothing.** Adopt the decision guide and ADRs this week and
  the spec workflow next quarter if that fits. Incremental is expected.

## When you've adopted

Once the current-state artifacts exist and new work flows through specs,
ADRs, and tests, you are on the steady-state methodology — follow the
reading order and decision guide in `methodology.md` from here, and reach
for `planning.md` on the next uncertain bet. This guide has done its job.

---

## Changing this document

`adopting.md` shares this repository's version and `CHANGELOG.md` (ADR
0009); it was added by ADR 0012. Changes to the adoption path follow the
same process as the rest of the methodology: update this file and record
the change in an ADR under `adr/`, with its **adoption impact**, noted in
`CHANGELOG.md` under semantic versioning.
