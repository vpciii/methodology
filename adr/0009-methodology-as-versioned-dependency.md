# ADR 0009: The methodology is a versioned dependency

- **Status:** Accepted
- **Date:** 2026-06-06
- **Deciders:** vpc

## Context

Projects consume this methodology by **reference** (ADR 0001): they
point at `$METHODOLOGY_HOME/methodology.md` rather than vendoring it.
That already keeps the bulk of the methodology cross-project consistent
— change `methodology.md` once and every project reading it sees the
new version. (The cloud/web surface is the exception: it has only the
cloned project repo, so it relies on the durable core inlined in the
project's own `CLAUDE.md`.)

What does **not** auto-propagate is the set of **instantiated
artifacts** each project copied from a template and then customized —
its `CONTRIBUTING.md`, the inlined core of its `CLAUDE.md`, its `docs/`
layout, any CI checks. When a methodology change touches those (e.g.
ADR 0006 added a spec-criterion-coverage CI check; ADR 0007 added
`docs/architecture.md`), existing projects drift until someone updates
them — and they cannot simply be overwritten, because they carry
project-specific content.

There was no stated way to handle this: no version, no changelog, and
no convention for telling a project whether a given methodology change
needs action or rides in for free by reference.

## Decision

Treat the methodology as a **versioned dependency** that each project
consumes, and handle changes the way the methodology already handles
dependencies (§10) and reversibility (§11) — versioned, changelogged,
adopted deliberately, never force-pushed.

- **SemVer + `CHANGELOG.md`.** This repo carries a semantic version and
  a human-facing `CHANGELOG.md`. A change that obligates per-project
  work is at least a minor bump; one that breaks an existing project
  convention is major. A project may note which version it is synced to.
- **Every methodology ADR declares an "Adoption impact."** A required
  section classifying the change for consumers as either:
  - **Reference-only** — projects get it automatically by reading
    `methodology.md`; no per-project action.
  - **Per-project action** — names the concrete change a project makes
    to adopt, and points at the diff or template.
- **Adoption is a deliberate, reviewed PR in the consuming project**, on
  its own cadence, like any dependency bump — recorded in that project's
  history, accepted by the human, and reversible.
- **Propagation stays pull, not push.** A migration helper (a script, a
  documented diff) may be *offered* for the mechanical parts, but the
  consuming project chooses when to apply it; nothing rewrites a
  project's customized artifacts automatically.

Cross-project *visibility* tooling — a per-project `methodology-version`
stamp plus a sweep that reports which projects are behind — is
deliberately **not** adopted now. With only a handful of projects, the
changelog and per-ADR adoption impact are enough; revisit it (its own
ADR) if the project count grows.

## Alternatives considered

- **Active propagation / codemods that rewrite every project** —
  rejected as the mechanism: it clobbers legitimately customized
  per-project artifacts and removes the human-accepts gate. Migration
  helpers remain available as opt-in convenience.
- **Do nothing; rely on the reference model alone** — rejected: the
  reference model covers `methodology.md` but not the instantiated
  artifacts, and gives no signal about whether a change needs project
  action. Silent drift is exactly what the methodology warns against.
- **Version-stamp every project + a sweep-audit now** — rejected for
  now: detection tooling earns its keep past ~5 projects; below that it
  is ceremony. Left as a future ADR.

## Consequences

- A methodology change has a clear, honest path to each project:
  reference-only ones arrive for free; action-required ones are
  labelled and adopted as small, reviewed PRs.
- The `CHANGELOG.md` becomes the single human-facing record of what
  changed across releases — closing a documentation gap and giving each
  project a checklist when it chooses to upgrade.
- Projects keep their autonomy and upgrade cadence; consistency is a
  deliberate act with a decision trail, not a forced sweep.
- Cost: one more required ADR section and a changelog to maintain — both
  cheap, and they ride in the same PR as the change they describe.
- With no version-stamp tooling yet, "which projects are behind" is
  answered by hand — acceptable at a handful of projects, revisited if
  that grows.

## Adoption impact

**Reference-only** for existing projects — nothing to change today.
This ADR introduces the upgrade *mechanism* (SemVer, `CHANGELOG.md`, and
the required "Adoption impact" ADR section) that future methodology
changes use to reach projects.

## References

- `methodology.md` §10 (dependencies are decisions), §11 (reversible),
  "Changing this document"; `CHANGELOG.md`; `templates/adr/_template.md`
  (Adoption impact section).
- ADR 0001 (reference, don't vendor); ADR 0006, 0007, 0008 (the changes
  whose adoption this governs).
