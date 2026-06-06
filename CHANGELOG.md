# Changelog

All notable changes to this methodology are recorded here. The format
is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this methodology adheres to [Semantic Versioning](https://semver.org/).

Each entry notes its **adoption impact** for consuming projects:
*reference-only* (arrives by reading `methodology.md`; no action) or
*per-project action* (the concrete change a project makes to adopt).
See [ADR 0009](./adr/0009-methodology-as-versioned-dependency.md).

## [Unreleased]

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
