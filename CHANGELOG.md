# Changelog

All notable changes to this methodology are recorded here. The format
is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this methodology adheres to [Semantic Versioning](https://semver.org/).

Each entry notes its **adoption impact** for consuming projects:
*reference-only* (arrives by reading `methodology.md`; no action) or
*per-project action* (the concrete change a project makes to adopt).
See [ADR 0009](./adr/0009-methodology-as-versioned-dependency.md).

## [Unreleased]

## [0.12.0] - 2026-06-21

### Added

- **One-command onboarding** — §10 gains a bullet: a substantial project
  bootstraps from a clone to a working environment with one documented,
  reproducible command; "works on my machine" is a defect in the
  onboarding path. The tool stays the project's choice (no mandate). The
  developer entry point is the one thing §6/§10's reproducible-build
  guidance left unsaid; recorded as a sub-bullet, not a new practice
  (ADR 0023). *Adoption: reference-only; optionally add a one-command
  setup where a substantial project lacks one.*

## [0.11.0] - 2026-06-20

### Added

- **Single source of truth named in the honesty rules** — the hazard is
  two hand-maintained *verbatim* copies of a fact kept in sync only by
  memory (they drift); single-source it, generate the copy, or
  machine-check for equality. Deliberate derivatives — a curated summary
  (this repo's own global summary, ADR 0018) or an instantiated
  per-project template (ADR 0009) — are kept honest by the same-PR rule,
  not equality. Closes the blind spot behind a real drift incident the
  same-PR rule, same-model reviewer, and CI all missed; the scope was
  itself sharpened by an adversarial review of the first draft. (ADR 0022)
  *Adoption: reference-only; optionally add an equality/codegen check
  where a project has known verbatim duplication.*

- **Cross-model adversarial review (trial)** — `experiments/adversarial-review/`:
  a manual process under evaluation where an *adversary model* — a
  different model from the *author model* that produced the work —
  adversarially refutes it, complementing the same-model PR reviewer
  (ADR 0021). Written in terms of **roles**, not vendors: a single
  *Current roster* names today's models (Claude as author, Antigravity /
  Gemini as adversary), so swapping or upgrading a model is a one-table
  edit and the rest stays model-agnostic. Includes the adversary prompt
  and a trial log; covers code review and design decisions. Explicitly
  **not** a ratified practice — absent from the numbered practices and
  the decision guide, no merge gate. *Adoption: none — a trial with no
  obligation; graduates to an ADR only if the log shows it earns its
  keep, otherwise it is deleted.*

## [0.10.0] - 2026-06-12

### Added

- **Retirement in the decision guide** — sunsetting a feature, service,
  or data store is routed like any other change: an ADR decides it
  (irreversible by definition, §11), the sunset walks deprecate → dark →
  remove, the removal PR updates `docs/architecture.md` and retires the
  feature's tests deliberately, and the frozen spec is marked `Retired`
  (the spec/plan status enums gain the value). Fills the lifecycle gap a
  completeness audit found: the guide covered create, change, refactor,
  and incident — but not removal. (ADR 0019) *Adoption: reference-only;
  optionally re-sync the spec templates for the status enum.*
- **User-facing docs ride along** — the same-PR honesty rule now
  explicitly binds user-facing documentation (usage, API reference,
  runbooks): a user-visible behavior change updates the docs it
  invalidates in the same PR. The artifact map gains a row naming the
  conventional home (`README.md` usage + `docs/`; an external docs site
  is a project tooling ADR), and `CONTRIBUTING.md`'s definition of done
  and review checklist gain the check. (ADR 0020) *Adoption:
  per-project action (optional) — re-sync `CONTRIBUTING.md`.*

### Fixed

- **Stale changelog compare links** — `[0.8.0]` and `[0.9.0]` link
  definitions were missing and `[Unreleased]` still compared from
  `v0.7.0`.

## [0.9.0] - 2026-06-09

### Added

- **The global summary is a repo artifact** — the always-loaded
  `~/.claude/CLAUDE.md` now has a canonical source at
  `templates/global-CLAUDE.md`, edited in the same PR as any change it
  summarizes; copying it into place is the per-machine release step.
  Repairs the drift a review found (missing planning and refactor
  rows, no `planning.md` mention) and folds in the 0.8.0 updates.
  (ADR 0018) *Adoption: no project action; per-machine — copy the
  template to `~/.claude/CLAUDE.md`.*

- **Release guidance for projects** — the `CONTRIBUTING.md` template
  gains a Releases section: tag `vX.Y.Z`, keep a curated human-facing
  `CHANGELOG.md` (Keep a Changelog; Conventional Commits make it cheap
  to draft). *Adoption: per-project action (optional) — re-sync
  `CONTRIBUTING.md`.*

### Changed

- **Sign-off gates stated canonically** — `methodology.md` §2 now says
  what the summary already claimed: each spec → plan → tasks stage is
  agreed before the next is written against it. (ADR 0018)
  *Adoption: reference-only.*
- **Throwaway graduation** — the scope note now routes the script that
  quietly became production to brownfield adoption (`adopting.md`),
  forward-only. *Adoption: reference-only.*
- **Issue trackers declared disposable orchestration** — the tracker
  sequences work; anything durable in an issue (a decision, a
  requirement, a regression) graduates to an artifact. *Adoption:
  reference-only.*
- **Non-functional and data prompts in the spec templates** —
  `spec.md` Requirements now prompts for load-bearing NFRs (latency,
  availability, retention); `plan.md` Data model changes prompts for
  data sensitivity, retention, and deletion path. *Adoption:
  per-project action (optional) — re-sync the spec templates.*
- **`plan.md` status vocabulary** — gains `Superseded | Withdrawn`,
  matching `spec.md`; a withdrawn spec's plan now has a legal status.
  *Adoption: reference-only.*

## [0.8.0] - 2026-06-09

### Added

- **Review checklist + red→green evidence** — every review checks a
  short named list (spec conformance, test honesty, language,
  boundaries/reversibility, artifacts ride along), and a bug-fix PR
  cites its regression test failing *before* the fix (output or a
  test-first commit), so "fails before" is shown, not asserted. The
  "show done" agent guardrail is extended to the red half. (ADR 0015)
  *Adoption: per-project action — re-sync `CONTRIBUTING.md` (Reviews,
  definition of done, Tests) and `CLAUDE.md` from the templates.*
- **Postmortems get a conventional home** — the §8-mandated postmortem
  now lives at `docs/postmortems/YYYY-MM-DD-<slug>.md`, with a template
  (`templates/postmortem.md`) whose follow-through table links the
  incident's §8 deliverable. The deliverable rule is unchanged.
  (ADR 0016) *Adoption: reference-only — the first user-visible
  incident uses the template; nothing to backfill.*
- **Reference spec-coverage checker** —
  `templates/ci/check-spec-coverage.py`, a single-file stdlib-only
  Python 3 script verifying the §5 traceability rules (SC → test
  mapping, `MUST`/`MUST NOT` → criterion coverage per ADR 0011, test
  files exist and cite their ids). Explicitly adapt-or-replace; ADR
  0006's rule-vs-mechanism split is unchanged. (ADR 0017) *Adoption:
  reference-only — an optional helper; wiring it is the project's own
  tooling decision.*

## [0.7.0] - 2026-06-08

### Added

- **Refactoring in the decision guide** — a row for restructuring code
  without changing behavior: no spec, keep the test suite green, an ADR
  only if it closes off future options. Fills the gap between "add or
  change behavior" (→ a test) and "change the system's structure"
  (→ `architecture.md`). (ADR 0014) *Adoption: reference-only.*

### Changed

- **`plan.md` freeze made explicit** — the plan template now states it
  freezes with its spec at `Implemented` (methodology §2, ADR 0007),
  matching `spec.md`.
- **`templates/methodology.mdc`** documents why it hardcodes the default
  methodology path instead of `$METHODOLOGY_HOME` (Cursor User Rules don't
  expand shell variables; ADR 0005), and gains the refactoring
  decision-guide row.

## [0.6.0] - 2026-06-08

### Added

- **Planning seam wired in + planning templates** — the planning
  methodology (ADR 0010) is now reachable from the rest of the docs:
  `methodology.md` gains a decision-guide row and a reading-order entry
  for `planning/<slug>/`, and the `project-CLAUDE.md` / `CONTRIBUTING`
  templates route uncertain or expensive bets through planning before the
  spec. New `templates/planning/{brief,pr-faq,options,bet,premortem}.md`
  match `templates/spec/`. (completes ADR 0010)
  *Adoption: reference-only for the navigation; the new
  `templates/planning/` are available to copy when a project takes on an
  uncertain bet.*

### Changed

- `methodology.md` (reading order, decision guide), `planning.md`
  (templates pointer), `README.md` (layout row),
  `templates/project-CLAUDE.md`, `templates/project-CONTRIBUTING.md`, and
  `templates/methodology.mdc` (decision-guide row) updated for the above.

## [0.5.0] - 2026-06-08

### Added

- **License** — the repository is dedicated to the public domain under
  [CC0 1.0 Universal](./LICENSE); everything here (methodology, templates,
  ADRs) may be copied into any project with no attribution required. The
  repo is a curated synthesis of existing, separately-credited practices,
  so copyright covers only that authored expression — which is waived.
  (ADR 0013) *Adoption: reference-only.*

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

[Unreleased]: https://github.com/vpciii/methodology/compare/v0.12.0...HEAD
[0.12.0]: https://github.com/vpciii/methodology/compare/v0.11.0...v0.12.0
[0.11.0]: https://github.com/vpciii/methodology/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/vpciii/methodology/compare/v0.9.0...v0.10.0
[0.9.0]: https://github.com/vpciii/methodology/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/vpciii/methodology/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/vpciii/methodology/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/vpciii/methodology/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/vpciii/methodology/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/vpciii/methodology/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/vpciii/methodology/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/vpciii/methodology/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/vpciii/methodology/releases/tag/v0.1.0
