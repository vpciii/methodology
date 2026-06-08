# Changelog

All notable changes to this methodology are recorded here. The format
is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this methodology adheres to [Semantic Versioning](https://semver.org/).

Each entry notes its **adoption impact** for consuming projects:
*reference-only* (arrives by reading `methodology.md`; no action) or
*per-project action* (the concrete change a project makes to adopt).
See [ADR 0009](./adr/0009-methodology-as-versioned-dependency.md).

## [Unreleased]

## [0.4.0] - 2026-06-08

### Added

- **Brownfield adoption guide** — new `adopting.md` for bringing an
  existing codebase onto the methodology: a *forward-only* rule (the
  methodology applies from the adoption date forward; no retroactive
  specs, never block a fix to backfill), a seed order for current-state
  artifacts (`architecture.md` → glossary → decision-capture ADRs → CI
  coverage on new specs only), and three modes (greenfield / brownfield /
  retroactive). (ADR 0012)
  *Adoption: reference-only — arrives by reading; the seed order is a
  recommended path, not a gate.*
- **Characterization tests** named in `methodology.md` §5 as the
  brownfield safety net — pin current behavior before changing untested
  legacy code.

### Changed

- `methodology.md` §5 cross-references characterization tests; "Changing
  this document" now lists `adopting.md` and the ADR range extends to
  0012. `README.md` gains an `adopting.md` layout row and a brownfield
  pointer in the adoption steps.

## [0.3.0] - 2026-06-08

### Added

- **`MUST` requirements map to success criteria** — every `MUST` /
  `MUST NOT` requirement (`R-…`) now carries a stable id and is reflected
  in at least one success criterion, closing the gap where a normative
  requirement could ship untested while all criteria passed. Success
  criteria stay the single verification surface; the spec Traceability
  table gains a **Requirement(s)** column so the `R-… → SC-… → test` chain
  is explicit. (ADR 0011)
  *Adoption: per-project — when next touching a spec, id every `MUST` /
  `MUST NOT`, ensure each maps to a criterion, and add the Requirement(s)
  column; optionally extend the spec-coverage CI check to assert every
  `MUST` is covered.*

### Changed

- `templates/spec/spec.md` (Requirements, Success criteria, Traceability)
  and `templates/project-CONTRIBUTING.md` (Definition of Done) updated for
  the above.

## [0.2.0] - 2026-06-08

### Added

- **Planning methodology** — new sibling document `planning.md` covering
  the pre-spec phase (deciding *what / whether / which approach* to
  build): five artifact-producing practices — problem framing,
  working-backwards PR-FAQ, set-based divergence, prioritization
  economics, and assumption testing — that converge to a `spec.md`.
  Planning artifacts live in `planning/<slug>/` and freeze when the spec
  is created. (ADR 0010)
  *Adoption: reference-only — arrives by reading; the `planning/<slug>/`
  artifact home is an opt-in convention for genuinely uncertain or
  expensive bets. Matching `templates/planning/` are a follow-up.*

### Changed

- `methodology.md` cross-references `planning.md` from §2 (the spec seam)
  and retires the "only methodology document" line; `README.md` layout
  table gains a `planning.md` row.

## [0.1.0] - 2026-06-06

### Added

- **Checkable spec↔test traceability** — success criteria carry stable
  `SC-` ids, tests cite them, specs carry a Traceability table, and a CI
  check fails on any uncovered criterion. (ADR 0006)
  *Adoption: per-project — wire the coverage check into CI and add ids +
  the Traceability table when next touching a spec.*
- **Current-state architecture overview** — new `docs/architecture.md`
  (template added) as the home for structural current state; added to
  the reading order and artifact map. (ADR 0007)
  *Adoption: per-project — seed `docs/architecture.md` from the template.*
- **Spec freeze at `Implemented`** — a shipped spec becomes a historical
  record; a contradiction found later flows to a test, a new spec, or an
  ADR. (ADR 0007) *Adoption: reference-only.*
- **AI-agent drift guardrails** — don't silently rewrite an agreed
  contract; show "done" by citing the test; re-read before editing;
  surface drift. (ADR 0008) *Adoption: reference-only.*
- **Versioned-dependency model** — SemVer, this `CHANGELOG.md`, and an
  "Adoption impact" section required on every methodology ADR. (ADR 0009)
  *Adoption: reference-only.*

### Changed

- `templates/spec/spec.md`, `templates/spec/tasks.md`,
  `templates/project-CONTRIBUTING.md`, `templates/project-CLAUDE.md`,
  `templates/methodology.mdc`, and `README.md` updated for the above.
- `templates/adr/_template.md` gains an **Adoption impact** section.

---

Decisions made before this changelog are recorded in git history and in
`adr/0001`–`adr/0005`.

[Unreleased]: https://github.com/vpciii/methodology/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/vpciii/methodology/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/vpciii/methodology/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/vpciii/methodology/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/vpciii/methodology/releases/tag/v0.1.0
