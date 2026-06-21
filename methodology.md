# Methodology

A small set of development practices that have stood the test of time.
None of them depend on a particular language, framework, editor, or AI
tool. All of them are markdown, git, and tests — the substrate that
every modern toolchain (and every replacement that comes next) reads
and writes.

This document is **global**: it is the shared methodology for all
projects, followed by **both humans and AI agents**. It lives in its
own repository (`$METHODOLOGY_HOME`, default `~/Developer/methodology`)
so it outlives any single project, and each project points at it from
its own `CLAUDE.md`.

> **`$METHODOLOGY_HOME`** is this repository's location. It defaults to
> `~/Developer/methodology` and is set in `~/.claude/settings.json`
> (`env`) so every Claude session resolves it; add it to your shell
> profile for terminal use. All paths below are written relative to it.

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
person — or a future you, or a future agent — will maintain). Apply
judgment.

The judgment is revisited when the facts change: a throwaway that
outlives its purpose — the script that quietly became production — is
adopted *brownfield*, forward-only (`adopting.md`). Graduation triggers
the artifacts from that point on, not a retroactive backfill.

---

## Using this methodology (humans and agents)

This methodology is meant to be followed by a human contributor and by
an AI coding agent equally. This section is the navigable surface for
both.

### Reading order (onboarding)

To get oriented in any project, in order:

1. **This document** — the practices (§1–§11) and why they exist.
2. The project's **`docs/architecture.md`** — the current shape of the
   system at a glance (components, boundaries, data stores, external
   dependencies). It tells you *how the system is now*; the ADRs tell
   you *why*. Skim it before the ADRs.
3. The project's **`docs/adr/`**, highest number down, until the
   reasoning behind that shape is clear. Each ADR is binding unless
   `superseded`.
4. The project's **`docs/glossary.md`** — the ubiquitous language; use
   these terms exactly.
5. The **`planning/<feature>/`** folder, if the work began as a bet that
   went through planning (`planning.md`) — the problem, options, and
   appetite behind the spec.
6. The **`specs/<feature>/`** folder for the work at hand, if one was
   named.

### Decision guide — which artifact, when

| If you are about to… | Produce… | Where |
|---|---|---|
| Take on an uncertain or expensive bet (decide *what* / *whether* to build) | plan it before the spec — problem, options, appetite (planning.md) | `planning/<slug>/` |
| Do substantial or long-lived work (more than a function/bugfix) | a spec, then plan, then tasks | `specs/<slug>/{spec,plan,tasks}.md` |
| Make a decision that is expensive to reverse, cross-component, or future-constraining | an ADR | `docs/adr/NNNN-*.md` |
| Add or change behavior | a test that fails before and passes after; in a spec, trace it to a success-criterion id (§5) | `tests/` |
| Restructure code without changing behavior (refactor, tech-debt paydown) | no spec — keep the test suite green; an ADR only if it closes off future options (§1, §11) | the commit / `docs/adr/` |
| Use a domain term that isn't defined | a glossary entry | `docs/glossary.md` |
| Change the system's structure (a component, boundary, store, or external dependency) | an update to the current-state overview, in the same PR | `docs/architecture.md` |
| Add or upgrade a dependency | weigh it; record non-trivial ones as an ADR (§10) | `docs/adr/` |
| Ship something risky or hard to undo | a flag / transition plan (§11) | `plan.md` Rollout |
| Retire a feature, service, or data store | an ADR deciding the sunset (irreversible by definition, §11): deprecation window → dark → removal; update `docs/architecture.md` and retire its tests in the removal PR; mark the frozen spec `Retired` | `docs/adr/` |
| Resolve an incident | at least one of: regression test, ADR, spec update; a short blameless postmortem if user-visible (§8) | `tests/`, `docs/adr/`, `specs/`, `docs/postmortems/` |
| Make a trivial, throwaway, or five-minute change | nothing — a good commit message is enough | the commit |

### Operating rules for AI agents

An AI agent (Claude today, something else tomorrow) is a first-class
contributor here, bound by the same artifacts. Specifically:

- **Read before you write.** Follow the reading order above before
  proposing changes.
- **Produce artifacts, not just code.** A change to substantial or
  long-lived work includes its spec, its tests, and an ADR for any
  significant decision — not code alone.
- **A failing test is the most precise instruction you can be given,
  and a passing suite is the most trustworthy signal that work is
  done.** Prefer encoding intent as executable constraints.
- **Stop and ask** when a needed domain term is undefined, when a
  decision looks expensive to reverse, or when the spec is ambiguous —
  do not invent a term or guess a boundary.
- **The human is the author of record.** You may draft anything; the
  human reviews the diff, runs the tests, and accepts. Never assume an
  unstated standard (security posture, naming, API shape) — surface it.

#### Guardrails against agent-specific drift

Agents desync confidently and asymmetrically; these four failures are
the ones least likely to be caught by a human skimming an internally
consistent diff (see ADR 0008):

- **Do not silently change an agreed contract.** An `Approved` or
  `Implemented` spec's requirements and success criteria are what you
  build against — never edit them to match code you just wrote. A
  genuine contract change is its own diff, with rationale, for human
  sign-off; it is never folded into an implementation change.
- **Show "done," do not assert it.** When you claim a success criterion
  is met, cite the passing test that proves it (§5). Completion you
  cannot point at is reported as unproven. For a bug fix this includes
  the red half: show the regression test failing before the fix — its
  output, or a test-first commit — not only passing after (ADR 0015).
- **Re-read before you write.** Before editing a spec, ADR, or
  glossary, re-read the current file — not a remembered or summarized
  version. Treat recalled context as a possibly-stale pointer to
  verify, not as ground truth.
- **Surface drift; don't paper over it.** If you notice code, spec, and
  glossary disagreeing while doing unrelated work, flag it (an issue, a
  note, or the §8 loop) rather than quietly editing the doc to match
  the code.

### Keep the artifacts honest

- **Docs change in the same PR as the behavior they describe.** No
  "docs later." A change that makes the glossary, an ADR, a spec, or
  the README wrong must fix it in the same change. User-facing
  documentation is bound the same way: a user-visible behavior change
  updates the usage docs, API reference, or runbook it invalidates in
  the same PR (ADR 0020).
- **Single source of truth.** A fact lives in one place. The hazard is
  two hand-maintained *verbatim* copies kept in sync only by memory —
  they drift. Single-source it, generate the copy, or machine-check the
  copies for equality. Deliberate *derivatives* are not this hazard: a
  curated **summary** (this document's global summary, kept honest in the
  same PR — ADR 0018) and an **instantiated template** customized in a
  consuming project (versioned-dependency model — ADR 0009) are kept
  honest by the same-PR rule, not equality (ADR 0022).
- **ADRs are append-only** — supersede, never rewrite history.
- **Automate what is checkable.** Anything a machine can verify —
  tests, type-checks, lint, commit-message format, spec-criterion
  coverage (§5) — is enforced in CI, not left to memory or review
  diligence.

---

## Artifact map

The methodology's durable surface — the things that survive any tool
change — lives at conventional paths. Newcomers (human or AI) use this
table to find what's where without hunting.

| Primitive | Conventional path | Purpose |
|---|---|---|
| This methodology | `$METHODOLOGY_HOME/methodology.md` | The document you are reading; shared across all projects. |
| Project README | `README.md` | Front door for the repo; short pointer to the artifacts below. |
| Current-state architecture | `docs/architecture.md` | How the system is shaped *now* — components, boundaries, data stores, external dependencies. Points at ADRs for the *why*. Template: `$METHODOLOGY_HOME/templates/architecture.md`. |
| Architecture Decision Records | `docs/adr/NNNN-*.md` | One short file per significant decision. Template: `$METHODOLOGY_HOME/templates/adr/_template.md`. |
| Ubiquitous language / glossary | `docs/glossary.md` | The project's domain terms. Template: `$METHODOLOGY_HOME/templates/glossary.md`. |
| Twelve-Factor checklist | `docs/twelve-factor.md` | Status table for deployable services. Template in `templates/`. |
| Postmortems | `docs/postmortems/YYYY-MM-DD-<slug>.md` | Blameless record of a user-visible incident; links its §8 follow-through (regression test, ADR, or spec update). Template: `$METHODOLOGY_HOME/templates/postmortem.md`. |
| User-facing documentation | `README.md` usage + `docs/` (an external docs site is a project tooling ADR) | What users and operators rely on — usage, API reference, runbooks. Updated in the same PR as the user-visible behavior change that invalidates it (ADR 0020). |
| Feature specifications | `specs/<slug>/{spec,plan,tasks}.md` | Spec-first workflow. Templates in `$METHODOLOGY_HOME/templates/spec/`. |
| AI agent orientation | `CLAUDE.md` | Points the active AI tool at the artifacts above. Template: `templates/project-CLAUDE.md`. |
| Contributor guide | `CONTRIBUTING.md` | Operational rules: PR flow, commit labels, definition of ready/done, review scope. Template: `templates/project-CONTRIBUTING.md`. |
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
- Lives in: `docs/adr/`. Template: `$METHODOLOGY_HOME/templates/adr/_template.md`.

**When is an ADR required?** When a decision is any of:

- **Expensive to reverse** — changing it later would require
  coordinated work across files, data, or deployments.
- **Cross-component** — affects more than one bounded module or layer.
- **Future-constraining** — closes off options that would otherwise
  have remained open.

The simpler test: would a future contributor (or AI agent) reasonably
ask "why?" about this? If yes, write an ADR. If no, the commit message
is enough. The goal is a decision trail rich enough to onboard a
stranger, not an exhaustive log of every micro-choice.

Why this lasts: a written decision trail is the single highest-
leverage habit in software engineering. It is the answer to every
future "why is it like this?"

### 2. Spec-first development

Write the spec before the code. One folder per feature, three files:
`spec.md` (what + why), `plan.md` (how), `tasks.md` (PR-sized work
items). The spec is reviewed and agreed before implementation.
Sign-off sits **between the stages**: the spec is agreed before the
plan is written against it, and the plan before the tasks are cut and
built — each stage is the reviewed input to the next, so disagreement
is caught at the cheapest altitude.

Everything *upstream* of the spec — whether to build, what, and which
approach — is the **planning methodology**'s concern (`planning.md`, ADR
0010). It converges to the `spec.md` this practice begins with; that
handoff is the seam between the two documents.

**The spec is the contract. The tests and the code review are how you
prove you met it.** §5 elaborates the test side; review-scope rules
live in each project's `CONTRIBUTING.md`.

**A spec freezes when it ships.** While it is `Draft`, `Under review`,
or `Approved` it is edited freely. When its status reaches
`Implemented` it becomes a historical record of what was agreed and
built, and is no longer rewritten to track ongoing change — a
contradiction discovered later flows to a *living* artifact instead (a
regression test, a new spec, or an ADR), exactly as the
operational-feedback loop prescribes (§8). Current truth lives
elsewhere: *behavioral* current state in the test suite (§5),
*structural* current state in `docs/architecture.md`. Each success
criterion carries a stable id and is traced to the test that verifies
it (§5).

- Origin: Tom Preston-Werner, [Readme Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html) (2010).
- Lives in: `specs/<feature-slug>/`. Templates: `$METHODOLOGY_HOME/templates/spec/`.

Why this lasts: every modern "spec-driven AI" framework (Spec Kit,
BMAD, Kiro, etc.) is repackaging this. Owning the primitive means you
are never locked into a wrapper.

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

Short-lived branches merged frequently to `main`. PRs kept small. The
discipline: keep changes reviewable, keep `main` always shippable,
surface integration problems early.

- Reference: [trunkbaseddevelopment.com](https://trunkbaseddevelopment.com/).
- Empirical backing: the [DORA](https://dora.dev/) research program
  (Accelerate, Forsgren et al., 2018) shows these practices correlate
  with high software delivery performance across thousands of orgs.

Why this lasts: it is the only execution discipline with hard
empirical evidence behind it. (It is only safe paired with §11 —
reversible changes.)

### 5. Tests as executable specification

Tests are not merely merge gates. They are the executable encoding of:

- **Business invariants.** Especially rules that must hold for *every*
  input rather than a finite test set — money math, access control,
  idempotency, state-machine transitions. Property-based tests
  (Hypothesis, fast-check, QuickCheck, etc.) are preferred when an
  invariant holds over an infinite input space.
- **Acceptance criteria from specs.** Every success criterion in a
  `spec.md` carries a stable id (`SC-1`, …) and maps to at least one
  test that fails before the feature is built and passes after. The
  test cites the id it verifies, a Traceability table in the spec
  records the mapping, and a CI check fails on any criterion left
  uncovered — so "done" is provable, not asserted, and a later change
  that breaks a criterion is caught loudly. Requirements feed this
  surface rather than bypassing it: every `MUST` / `MUST NOT` requirement
  (`R-…`) is reflected in at least one success criterion, so a normative
  obligation is never shipped without a test (ADR 0011) — success criteria
  stay the single verification surface, and requirements are what they
  must cover. The id-and-table convention is global; the CI mechanism
  (including checking that every `MUST` is covered) is a project tooling
  decision (ADR 0006). A reference checker to adapt or replace ships at
  `$METHODOLOGY_HOME/templates/ci/check-spec-coverage.py` (ADR 0017).
- **Regression records.** Every bug fix ships with the test that would
  have caught the bug. The test is the permanent record of what went
  wrong. The fix cites its **red→green evidence** — the test's failing
  output from before the fix, or a test-first commit a reviewer can
  run — so "fails before" is shown, not asserted; whether CI also
  enforces this is a project tooling decision (ADR 0015).
- **Characterized legacy behavior.** On an existing codebase, before
  changing untested code, a *characterization test* pins its current
  behavior so a fix or refactor has a safety net even where no spec ever
  existed. It is the brownfield entry point to the suite; see
  `adopting.md`.

The philosophical posture: **behavior over implementation.** A test
should describe what the system does for a user or a caller, not how
the code happens to be structured today. Implementation refactors
should not require test changes; behavior changes must.

This framing also strengthens the AI-agent story. Agents operate best
against **executable constraints**: a failing test is the most precise
specification you can give one, and a passing suite is the most
trustworthy signal that work is done.

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

See each project's `CONTRIBUTING.md` for the project-specific gloss of
each commit type label and the disambiguation rules between them.

Why this lasts: boring, simple, machine-readable. Every tool from
changelog generators to release bots speaks both.

### 8. Operational feedback loops

Production behavior is part of the specification process. Specs, ADRs,
and tests describe what the system *should* do; production tells us
what it *actually* does. The loop only closes when those two are
reconciled.

No formal SRE machinery is required. One rule is:

> Incidents, outages, and unexpected operational behavior result in
> **at least one** of:
>
> - **A failing test (now passing)** — capturing the regression so it
>   cannot recur silently.
> - **A new or updated ADR** — when the incident revealed a decision
>   we should have made, or made differently.
> - **A spec update** — when the incident revealed that the specified
>   behavior was wrong, ambiguous, or incomplete.

Lightweight supporting practices:

- **Observability is non-negotiable for deployed services** —
  structured logs (event-stream format per 12-Factor), key metrics,
  and traces when warranted.
- **Postmortems are written for any user-visible incident.** Short,
  blameless, focused on what the system *permitted* rather than who
  pushed which button. The deliverable is one of the three artifacts
  above — not the postmortem itself; the postmortem records the
  incident and links that follow-through. It lives at
  `docs/postmortems/YYYY-MM-DD-<slug>.md` (template:
  `$METHODOLOGY_HOME/templates/postmortem.md`, ADR 0016).

Why this lasts: production is a continuous, free source of information
about how the system actually behaves. Projects that discard it
relearn the same lessons repeatedly.

### 9. Security and secrets by default

Security is a design default, expressed (like everything else) as
durable artifacts — a decision record and a test — not as tooling.

- **Secrets never live in the repository** — not in code, config,
  fixtures, or committed env files. They come from the environment or
  a secret manager (ties to §6, config in the environment). A leaked
  secret is **rotated**, not merely deleted.
- **Trust boundaries and the authorization model are decisions** —
  they get ADRs (they are expensive to reverse, cross-component, and
  future-constraining by definition).
- **Validate input at trust boundaries; default to least privilege.**
- **Security-relevant bugs ship with a regression test**, exactly like
  any other bug (§5, §8).

Why this lasts: the durable artifacts — the boundary written in an ADR,
the regression test that proves the hole is closed — outlive any
scanner or vendor. (Specific security tooling, when adopted, gets its
own project ADR.)

### 10. Dependencies are decisions

Every dependency is a future-constraining choice: maintenance burden,
licensing obligation, and supply-chain surface.

- **Adding a dependency is a decision.** Weigh maintenance health,
  license compatibility, supply-chain surface, and whether the standard
  library or an existing dependency would do. Record non-trivial
  additions as an ADR (§1) — especially load-bearing, copyleft, or
  sparsely maintained ones.
- **Lockfiles are committed.** Builds are reproducible; versions are
  pinned and updated deliberately, never drifting silently.
- **One-command onboarding.** A substantial project bootstraps from a
  clone to a working environment with a single documented, reproducible
  command (`make setup`, a devcontainer, a Nix flake — the tool is the
  project's choice). Reproducible builds aren't reproducible if the setup
  isn't: "works on my machine" is a defect in the onboarding path, fixed
  like any other.
- **Updates are deliberate** — normal `chore:` work, reviewed like any
  change; a behavior-changing major bump may warrant its own ADR.

Why this lasts: the cheapest dependency to remove is the one you never
added. Considering the cost at add-time, and leaving it in the decision
trail, is independent of any package manager or scanner.

### 11. Reversible by default

Frequent merging to `main` (§4) is only safe when changes are easy to
undo.

- **Prefer changes you can turn off or roll back** — feature flags for
  risky behavior; ship dark, enable gradually.
- **Evolve schemas with expand-contract (parallel-change):** add the
  new shape, migrate, then remove the old — never a destructive
  in-place change in one irreversible step.
- **Evolve APIs backward-compatibly:** additive first; deprecate with a
  transition window before removing.
- **Retire with a transition, not a deletion.** Sunsetting a feature,
  service, or data store is this section's irreversible case par
  excellence: decide it in an ADR (§1), then walk it down — deprecate
  with a transition window, ship dark (disabled behind its flag), then
  remove. The removal PR updates `docs/architecture.md` and retires the
  feature's tests deliberately, citing the ADR; the spec stays frozen
  as history, its status flipped to `Retired` (ADR 0019).
- **Every non-trivial change has a known undo** — a flag flip, a
  revert, or a documented rollback in `plan.md`. A genuinely
  irreversible action (data deletion, an external side effect) is
  called out explicitly and decided with an ADR.

Why this lasts: cheap, fast recovery is what makes continuous delivery
viable. The principle is independent of any flag system or platform.

---

## The artifacts as a durable semantic interface

The practices above produce a small set of artifacts: ADRs, specs,
glossary entries, tests. Together, those artifacts form a project's
**durable semantic interface** — the stable contract that both human
contributors and automated agents read, write, and reason against.

This framing matters because it is independent of any particular AI
tool, IDE, or workflow:

- A human contributor onboards by reading the ADRs, the glossary, and
  the most recent specs (the reading order above).
- An AI agent — Claude Code today; something else tomorrow — does the
  same. The agent reads the spec, the ADRs, the glossary, and the
  tests; it writes code, tests, and new ADRs.
- Any tool that can read those artifacts and produce well-typed code,
  tests, and decision records is a competent collaborator, regardless
  of vendor or model.

If every AI tool in use today disappeared overnight, the project would
still be intelligible to a human (or a future tool) because the
interface is plain markdown, plain git, and plain test files.

A project's `CLAUDE.md` is the orientation pointer for the current AI
tool. When the tool changes, only that file changes.

**Optional workflow tools are welcome but disposable.** If a workflow
framework (BMAD, Spec Kit, Kiro, a custom set of skills, or whatever
emerges next) helps you draft specs, run reviews, or coordinate
multi-step work, you may use it — provided it only reads and writes the
canonical artifacts in the artifact map above. The artifacts are the
source of truth; the workflow tool is disposable orchestration over
them. The day the tool is retired, the project loses an editor, not a
project.

The same holds for **issue trackers and backlogs**. The tracker is
disposable orchestration for sequencing work; anything durable that
surfaces in an issue — a decision, a requirement, a regression —
graduates to the corresponding artifact. The artifacts, not the
backlog, are the record.

---

## What is intentionally not here

- **No agent personas or role-playing workflows.** They are
  framework-flavored; the underlying practices give the same benefit
  without the lock-in.
- **No methodology branding** (Scrum, SAFe, BMAD, Spec Kit, Kiro,
  etc.). Useful inspirations; none of their vocabulary is load-bearing.
- **No formal SRE / ITIL machinery.** Operational feedback loops exist
  (§8) but are deliberately lightweight.
- **No premature tech-stack or tooling commitments.** Each tooling
  choice — stack, security scanner, flag system, CI provider — gets an
  ADR in the project that makes it, when it is made, not before.

---

## Changing this document

This repository holds two methodology documents — `methodology.md`
(development) and `planning.md` (planning, ADR 0010) — plus `adopting.md`,
the guide for bringing an existing project onto them (ADR 0012); all three
share one version and `CHANGELOG.md`. If a practice changes, update the
relevant document and record the change in an ADR under this repository's
`adr/` (see the numbered ADRs in `adr/` for the decisions that shaped the
current version). Each such ADR declares an **adoption
impact** for consuming projects, and the change is noted in
`CHANGELOG.md` under semantic versioning, so projects adopt it
deliberately like any dependency (ADR 0009). The always-loaded global
summary (`templates/global-CLAUDE.md`, deployed as `~/.claude/CLAUDE.md`)
changes in the **same PR** as any change it summarizes; copying it into
place is the per-machine release step (ADR 0018). If you find yourself
arguing for or against a practice that isn't listed here, that is a sign
you need an ADR, not a longer methodology doc.
