# ADR 0012: Brownfield adoption is a forward-only bootstrap, in a sibling guide

- **Status:** Accepted
- **Date:** 2026-06-08
- **Deciders:** vpc

## Context

`methodology.md` and `planning.md` describe **steady state**. The reading
order, the decision guide, and "read before you write" all presuppose
that `docs/architecture.md`, ADRs, a glossary, and a meaningful test suite
already exist. But most adoption happens **mid-life**, on an existing
codebase with sparse docs and weak tests, where there is little to read
and the bootstrap cost is undefined.

Nothing in the methodology covered: adopting on an existing codebase;
whether to retroactively spec or test past work; how to reconstruct
current-state artifacts from code; or what to seed first for the most
leverage. A code review of the methodology flagged this as its largest
gap. Without guidance, adopters fail in one of two directions —
**over-ceremony** (a retroactive spec-everything docs sprint that stalls
delivery) or **under-documentation** (skipping artifacts because the
starting cost feels unbounded).

## Decision

Add **`adopting.md`, a sibling guide**, establishing *forward-only*
adoption and a concrete bootstrap order.

- **Forward-only by default.** The methodology applies from the adoption
  date forward. No retroactive specs/tests/ADRs for code that already
  shipped and isn't changing; never block a fix to backfill; artifacts
  accrue when you next touch an area.
- **Seed order:** `docs/architecture.md` (reverse-engineered) → glossary
  → decision-capture ADRs (status `Accepted`, dated now, marked as
  recording a pre-existing decision) → CI criterion-coverage on **new
  specs only**.
- **Three modes** — greenfield / brownfield / retroactive — with
  retroactive capture limited to areas being actively changed.
- **Characterization tests** are named as the brownfield safety net and
  cross-referenced from `methodology.md` §5: pin current behavior before
  changing untested code.
- It is a **separate document, not a section of `methodology.md`**, and
  shares the repository's SemVer track (ADR 0009) — mirroring the
  planning sibling (ADR 0010).

## Alternatives considered

- **Fold a brownfield section into `methodology.md`** — rejected: it
  bloats the steady-state document with one-time bootstrap content.
  Adoption is read once; the practices are read forever. A separate doc
  keeps the core tight and follows the `planning.md` precedent (ADR 0010).
- **No guidance; rely on "scale to the work"** — rejected: scale-to-work
  tells you not to over-spec a fix but says nothing about *seeding*
  current-state artifacts. The silence is what produces both over- and
  under-documentation.
- **Retroactive / back-dated specs for existing code** — rejected: a spec
  freezes as a historical record of what was *agreed* (§2); a back-dated
  spec for code that shipped without one is fiction. Current state belongs
  in `architecture.md` (structure) and the test suite (behavior).
- **A separate repository or tool for adoption** — rejected as
  disproportionate: it is a short guide that shares the version and the
  changelog.

## Consequences

- An adopter — human or agent — has a defined bootstrap order and a clear
  forward-only rule, so "read before you write" degrades gracefully on a
  legacy repo instead of stalling.
- `methodology.md` §5 gains characterization tests as a named primitive,
  giving brownfield work a first-class test pattern.
- Cost: a third document to keep honest, and a risk that "forward-only" is
  used to dodge documentation that is genuinely needed — mitigated by the
  seed-on-touch rule and the §8 operational loop.

## Adoption impact

**Reference-only.** Existing adopters get the guidance by reading; nothing
to change today. New adoption follows `adopting.md`. The seed order is a
recommended path, not a gate — no per-project artifact is mandated by this
ADR.

## References

- `adopting.md` (the guide this ADR adds).
- `methodology.md` — reading order and "read before you write"; §5 (tests,
  now including characterization tests); §2 (spec freeze); "A note on
  practice vs. ceremony" (scale to the work).
- `planning.md` / ADR 0010 (sibling-document precedent); ADR 0006
  (criterion-coverage check, applied here to new specs only); ADR 0009
  (versioned dependency — shared SemVer and `CHANGELOG.md`).

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
