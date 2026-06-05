# Methodology

A small set of development practices that have stood the test of time.
None of them depend on a particular language, framework, editor, or AI
tool. All of them are markdown, git, and tests — the substrate that
every modern toolchain (and every replacement that comes next) reads
and writes.

This document is **global**: it is the shared methodology for all
projects. It lives in its own repository (`~/Developer/methodology`)
so it outlives any single project, and each project points at it from
its own `CLAUDE.md`.

The rule of thumb: **document the artifact, not the tool.** A spec, a
decision record, and a passing test outlive any IDE or agent.

## A note on practice vs. ceremony

The discipline these artifacts encode matters more than the artifacts
themselves. A vague spec, a ceremonial ADR, a stale glossary, or a
giant unbroken task is worse than not writing one at all — it
preserves the appearance of rigor while losing the substance.

If you find yourself producing artifacts to satisfy a folder
structure rather than to clarify your thinking, stop. The folder
structure is not the methodology; the thinking is. **The quality of
the artifacts matters more than their existence.**

**Scale the ceremony to the work.** A one-off script, a throwaway
experiment, or a five-minute fix does not need a spec and an ADR.
These practices earn their keep on work that is *substantial* (more
than a single function or bugfix) or *long-lived* (something another
person — or a future you — will maintain). Apply judgment.

---

## Artifact map

The methodology's durable surface — the things that survive any tool
change — lives at conventional paths in each project. Newcomers
(human or AI) use this table to find what's where without hunting.

| Primitive | Conventional path | Purpose |
|---|---|---|
| This methodology | `~/Developer/methodology/methodology.md` | The document you are reading; shared across all projects. |
| Project README | `README.md` | Front door for the repo; short pointer to the artifacts below. |
| Architecture Decision Records | `docs/adr/NNNN-*.md` | One short file per significant decision. Template: `~/Developer/methodology/templates/adr/_template.md`. |
| Ubiquitous language / glossary | `docs/glossary.md` | The project's domain terms. Template: `templates/glossary.md`. |
| Twelve-Factor checklist | `docs/twelve-factor.md` | Status table for deployable services. Template: `templates/twelve-factor.md`. |
| Feature specifications | `specs/<slug>/{spec,plan,tasks}.md` | Spec-first workflow. Templates in `templates/spec/`. |
| AI agent orientation | `CLAUDE.md` | Points the active AI tool at the artifacts above. Template: `templates/project-CLAUDE.md`. |
| Contributor guide | `CONTRIBUTING.md` | Operational rules: PR flow, commit labels, definition of done, review scope. Template: `templates/project-CONTRIBUTING.md`. |
| Tests | `tests/` | Executable specification (see practice §5). |

The human is the author of record for every artifact. AI assistants
may draft; the human accepts.

---

## The practices

### 1. Architecture Decision Records (ADRs)

One short markdown file per significant decision: context, the
decision, alternatives considered, consequences. Numbered, immutable
once accepted, superseded rather than edited.

- Origin: Michael Nygard, [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (2011).
- Lives in: `docs/adr/`.
- Template: `templates/adr/_template.md`.

**When is an ADR required?** When a decision is any of:

- **Expensive to reverse** — changing it later would require
  coordinated work across files, data, or deployments.
- **Cross-component** — affects more than one bounded module or
  layer of the system.
- **Future-constraining** — closes off options that would otherwise
  have remained open.

The simpler test: would a future contributor (or AI agent) reasonably
ask "why?" about this? If yes, write an ADR. If no, the commit
message is enough. The goal is a decision trail rich enough to
onboard a stranger, not an exhaustive log of every micro-choice.

Why this lasts: a written decision trail is the single highest-
leverage habit in software engineering. It is the answer to every
future "why is it like this?"

### 2. Spec-first development

Write the spec before the code. One folder per feature, three files:
`spec.md` (what + why), `plan.md` (how), `tasks.md` (PR-sized work
items). The spec is reviewed and agreed before implementation.

**The spec is the contract. The tests and the code review are how
you prove you met it.** §5 elaborates on the test side; review-scope
rules live in each project's `CONTRIBUTING.md`.

- Origin: Tom Preston-Werner, [Readme Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html) (2010).
- Lives in: `specs/<feature-slug>/`.
- Templates: `templates/spec/`.

Why this lasts: every modern "spec-driven AI" framework
(Spec Kit, BMAD, Kiro, etc.) is repackaging this. Owning the
primitive means you are never locked into a wrapper.

### 3. Domain-Driven Design, applied lightly

Use a **ubiquitous language** — the same words in code, docs, and
conversation. Identify **bounded contexts** when the domain has
genuinely distinct subdomains. Skip the heavy patterns (aggregates,
repositories) until the domain demands them.

- Origin: Eric Evans, *Domain-Driven Design* (Addison-Wesley, 2003).
- Short read: Martin Fowler's [BoundedContext](https://martinfowler.com/bliki/BoundedContext.html)
  and [UbiquitousLanguage](https://martinfowler.com/bliki/UbiquitousLanguage.html).
- Lives in: `docs/glossary.md`.

Why this lasts: vague terminology compounds into years of rework.
Getting the core nouns of the domain right early — and using them
identically in code, tests, and docs — prevents whole categories of
confusion.

### 4. Trunk-based development with small PRs

Short-lived branches merged frequently to `main`. PRs kept small.
The discipline: keep changes reviewable, keep `main` always shippable,
surface integration problems early.

- Reference: [trunkbaseddevelopment.com](https://trunkbaseddevelopment.com/).
- Empirical backing: the [DORA](https://dora.dev/) research program
  (Accelerate, Forsgren et al., 2018) shows these practices correlate
  with high software delivery performance across thousands of orgs.

Why this lasts: it is the only execution discipline with hard
empirical evidence behind it.

### 5. Tests as executable specification

Tests are not merely merge gates. They are the executable encoding
of:

- **Business invariants.** Especially for rules that must hold for
  *every* input rather than a finite test set — money math, access
  control, idempotency, state-machine transitions. Property-based
  tests (Hypothesis, fast-check, QuickCheck, etc.) are preferred when
  an invariant holds over an infinite input space.
- **Acceptance criteria from specs.** Every success criterion in a
  `spec.md` should map to at least one test that fails before the
  feature is built and passes after it is.
- **Regression records.** Every bug fix ships with the test that
  would have caught the bug. The test is the permanent record of
  what went wrong.

The philosophical posture: **behavior over implementation.** A test
should describe what the system does for a user or a caller, not how
the code happens to be structured today. Implementation refactors
should not require test changes; behavior changes must.

This framing also strengthens the AI-agent story. Agents operate
best against **executable constraints**: a failing test is the most
precise specification you can give one, and a passing suite is the
most trustworthy signal that work is done.

### 6. The Twelve-Factor App

A checklist for building services that are portable, scalable, and
operable. Config in the environment, logs as event streams, stateless
processes, etc. Applies to deployable services; skip for libraries,
CLIs, and one-off scripts.

- Origin: Adam Wiggins / Heroku, [12factor.net](https://12factor.net/) (2011).
- Lives in: `docs/twelve-factor.md` (status checklist).

Why this lasts: still the baseline for any deployable service,
regardless of language or platform.

### 7. Conventional Commits and Semantic Versioning

Machine-readable commit messages and predictable version numbers.

- [Conventional Commits](https://www.conventionalcommits.org/).
- [Semantic Versioning](https://semver.org/).

See each project's `CONTRIBUTING.md` for the project-specific gloss
of each commit type label and the disambiguation rules between them.

Why this lasts: boring, simple, machine-readable. Every tool from
changelog generators to release bots speaks both.

### 8. Operational feedback loops

Production behavior is part of the specification process. Specs,
ADRs, and tests describe what the system *should* do; production
tells us what it *actually* does. The loop only closes when those
two are reconciled.

No formal SRE machinery is required. One rule is:

> Incidents, outages, and unexpected operational behavior result in
> **at least one** of:
>
> - **A failing test (now passing)** — capturing the regression so
>   it cannot recur silently.
> - **A new or updated ADR** — when the incident revealed a
>   decision we should have made, or made differently.
> - **A spec update** — when the incident revealed that the
>   specified behavior was wrong, ambiguous, or incomplete.

Lightweight supporting practices:

- **Observability is non-negotiable for deployed services.** Every
  one exposes structured logs (event-stream format per 12-Factor),
  key metrics (request rates, latencies, error rates, business-
  relevant counters), and traces when warranted.
- **Postmortems are written for any user-visible incident.** Short,
  blameless, focused on what the system *permitted* rather than who
  pushed which button. The postmortem's deliverable is one or more
  of the three artifacts above — not the postmortem itself.

Why this lasts: production is a continuous, free source of
information about how the system actually behaves. Projects that
discard it relearn the same lessons repeatedly.

---

## The artifacts as a durable semantic interface

The practices above produce a small set of artifacts: ADRs, specs,
glossary entries, tests. Together, those artifacts form a project's
**durable semantic interface** — the stable contract that both human
contributors and automated agents read, write, and reason against.

This framing matters because it is independent of any particular AI
tool, IDE, or workflow:

- A human contributor onboards by reading the ADRs, the glossary,
  and the most recent specs.
- An AI agent — Claude Code today; something else tomorrow — does
  the same. The agent reads the spec, the ADRs, the glossary, and
  the tests; it writes code, tests, and new ADRs.
- Any tool that can read those artifacts and produce well-typed
  code, tests, and decision records is a competent collaborator,
  regardless of vendor or model.

If every AI tool in use today disappeared overnight, the project
would still be intelligible to a human (or a future tool) because
the interface is plain markdown, plain git, and plain test files.

A project's `CLAUDE.md` is the orientation pointer for the current
AI tool. When the tool changes, only that file changes.

**Optional workflow tools are welcome but disposable.** If a
workflow framework (BMAD, Spec Kit, Kiro, a custom set of skills,
or whatever emerges next) helps you draft specs, run reviews, or
coordinate multi-step work, you may use it — provided it only reads
and writes the canonical artifacts in the artifact map above. The
artifacts are the source of truth; the workflow tool is disposable
orchestration over them. The day the tool is retired, the project
loses an editor, not a project.

---

## What is intentionally not here

- **No agent personas or role-playing workflows.** They are
  framework-flavored; the underlying practices (spec-first, ADRs,
  small PRs, tests as specification) give the same benefit without
  the lock-in.
- **No methodology branding** (Scrum, SAFe, BMAD, Spec Kit, Kiro,
  etc.). These are useful inspirations; none of their vocabulary is
  load-bearing.
- **No formal SRE / ITIL machinery.** Operational feedback loops
  exist (practice §8) but are deliberately lightweight. Incident
  response should produce durable artifacts (tests, ADRs, spec
  updates), not paperwork.
- **No premature tech-stack commitments.** Each tooling choice gets
  an ADR in the project that makes it, when it is made, not before.

---

## Changing this document

`methodology.md` is the only methodology document. If a practice
changes, update it here and record the change in an ADR under this
repository's `adr/`. If you find yourself arguing for or against a
practice that isn't listed here, that is a sign you need an ADR, not
a longer methodology doc.
