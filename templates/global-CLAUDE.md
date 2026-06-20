<!-- Canonical source: $METHODOLOGY_HOME/templates/global-CLAUDE.md (ADR 0018).
     Edit it there, in the same PR as the methodology change it summarizes;
     copy it to ~/.claude/CLAUDE.md when the release lands on main.
     Do not edit the deployed copy in place. -->

# Global development methodology

My standing development practices for **all** projects, followed by
humans and AI agents alike. The full canonical documents live in
`$METHODOLOGY_HOME` (default `~/Developer/methodology`, its own git
repo): `methodology.md` (development), `planning.md` (the pre-spec
phase), and `adopting.md` (bringing an existing codebase on). **For any
substantial or long-lived work, read `methodology.md` first.** This
file is the always-loaded summary.

## Scope — apply judgment

These practices earn their keep on work that is **substantial** (more
than a single function or bugfix) or **long-lived** (something to be
maintained). For throwaway scripts, quick experiments, and five-minute
fixes, don't impose the ceremony — a good commit message is enough. A
throwaway that turns long-lived is adopted forward-only (`adopting.md`).

A project's own `CLAUDE.md` adds project-specific rules and takes
precedence over this file. An accepted ADR beats both.

## Decision guide — which artifact, when

| About to… | Produce… |
|---|---|
| Take on an uncertain/expensive bet (what / whether to build) | planning first — problem, options, appetite in `planning/<slug>/` (planning.md) |
| Do substantial/long-lived work | a spec → plan → tasks in `specs/<slug>/` |
| Make a decision expensive to reverse / cross-component / future-constraining | an ADR in `docs/adr/` |
| Add or change behavior | a test that fails before, passes after; in a spec, trace it to a criterion id |
| Restructure code without changing behavior (refactor) | no spec — keep tests green; an ADR only if it closes off future options |
| Use an undefined domain term | a `docs/glossary.md` entry (don't invent synonyms) |
| Change the system's structure (component / boundary / store / dependency) | update `docs/architecture.md`, same PR |
| Add/upgrade a dependency | weigh it; ADR for non-trivial ones |
| Retire a feature / service / data store | an ADR with the sunset plan (deprecate → dark → remove); update `architecture.md`, retire its tests, mark the spec `Retired` |
| Resolve an incident | ≥1 of: regression test, ADR, spec update; postmortem in `docs/postmortems/` if user-visible |
| Trivial / throwaway change | nothing but a clear commit message |

## Hard rules (the durable core)

- **Spec-first for non-trivial work.** `spec.md` (what+why) → `plan.md`
  (how) → `tasks.md` (PR-sized). Sign-off between stages. Templates:
  `$METHODOLOGY_HOME/templates/spec/`.
- **Decisions get ADRs.** For anything expensive to reverse, multi-
  component, or future-constraining. Template:
  `$METHODOLOGY_HOME/templates/adr/_template.md`.
- **Small PRs, trunk-based.** Short branches to `main`; split past ~300
  lines of diff.
- **Reversible by default.** Prefer flags / expand-contract migrations
  / backward-compatible APIs. Every non-trivial change has a known undo;
  genuinely irreversible actions are called out and decided with an ADR.
- **Tests as specification.** New behavior ships with tests; fixes ship
  a regression test (fails before, passes after — failing run cited in
  the PR). Test behavior, not implementation. Spec success criteria
  carry stable ids traced to tests, CI-checked for coverage.
- **Current-state & spec freeze.** Keep `docs/architecture.md` honest
  (the system's shape *now*) in the same PR as any structural change. A
  spec freezes at `Implemented` (a historical record); a contradiction
  found later goes to a test, a new spec, or an ADR — not back into it.
- **Security & secrets.** Secrets never in the repo (env / secret
  manager only); a leaked secret is rotated. Trust boundaries and authz
  are ADR-worthy decisions; security bugs ship a regression test.
- **Dependencies are decisions.** Weigh maintenance/license/supply-chain
  before adding; commit lockfiles; record non-trivial deps as ADRs.
- **Ubiquitous language.** Use the project's domain terms exactly in
  code, tests, and docs.
- **Conventional Commits + SemVer.** `feat: fix: docs: refactor: test:
  chore: perf: build: ci:`; `!` for breaking changes.
- **Keep artifacts honest.** Docs — user-facing docs included — change
  in the **same PR** as the behavior; a fact lives in one place (don't
  hand-sync two *verbatim* copies by memory — generate or equality-check
  them; curated summaries and per-project template copies are derivatives
  kept honest by the same-PR rule); ADRs are append-only (supersede,
  never edit); whatever is machine-checkable is enforced in CI, not left
  to memory.
- **Operational feedback.** An incident produces ≥1 of: a now-passing
  regression test, a new/updated ADR, or a spec update.

## Author of record

AI assistants may draft; **the human accepts.** Read before you write
(methodology + architecture + ADRs + glossary + active spec). Produce
artifacts, not just code. Stop and ask on undefined terms or
hard-to-reverse decisions. Review every diff, run every test. The
artifacts (specs, ADRs, tests) are the source of truth; any workflow
framework (BMAD, Spec Kit, etc.) is disposable orchestration over them.

**Agent guardrails.** Don't silently rewrite an agreed spec's
requirements or criteria — a contract change is its own diff for
sign-off, never folded into an implementation PR; show "done" by citing
the passing test (for a fix, also the failing run before it), don't
assert it; re-read a file before you edit it; surface drift you notice
rather than papering over it.
