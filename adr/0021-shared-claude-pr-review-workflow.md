# ADR 0021: A shared, methodology-aware Claude PR review workflow

- **Status:** Accepted
- **Date:** 2026-06-11
- **Deciders:** vpc

## Context

Projects following this methodology now carry heavy AI-assisted change.
Deterministic CI (lint, format, strict type-check, tests, spec-criterion
coverage) gates *mechanical* correctness, but nothing independently
reviews a PR for *contract* fidelity — does the change match the spec's
success criteria, ship the test a fix requires, respect the ADRs and the
glossary, keep docs in the same PR? That is the human review checklist
(ADR 0015), and it is worth automating as an independent first pass.

The reviewer should be **shared** — one definition, every project, tuned
in one place — for the same reason the methodology itself is shared.
Copy-pasting a workflow into each repo would drift.

A fully centralized setup (one API key, auto-applied to all repos) is a
GitHub *organization* feature; these projects live under a personal
account, so a per-repo secret and a thin per-repo caller are unavoidable.

## Decision

Host a **reusable GitHub Actions workflow** in this repository
(`.github/workflows/claude-review.yml`, `on: workflow_call`) that runs
`anthropics/claude-code-action` with a methodology-aware prompt — reviewing
each PR against the project's own CLAUDE.md, ADRs, glossary, specs, and
Definition of Done. Projects adopt it with a ~12-line caller workflow
(template: `templates/github/claude-review.yml`).

- **This repo dogfoods it.** The methodology repo adopts its own reusable
  workflow via a local caller (`.github/workflows/pr-review.yml`,
  `uses: ./...`), so ADR and methodology PRs get the same review. The
  prompt reads whichever governing artifacts a repo has, so it fits both
  this repo's layout (`adr/`, `methodology.md`) and a project's
  (`docs/adr/`, `specs/`).
- **Advisory, not a gate.** It posts review comments; deterministic CI
  stays the required merge check. Subjective findings never block a merge.
- **The policy is the durable artifact; the Action is disposable
  orchestration.** The review criteria mirror the human checklist, so the
  GitHub-specific runner can be swapped without losing them.
- **Pinned** to a released major (`@v1`), not a moving tag (ADR 0003).
- **Cost/noise controls:** runs on `opened` + `ready_for_review`, skips
  drafts and `[skip-review]` titles.

## Alternatives considered

- **Per-repo copies of the workflow** — rejected: drift; defeats "tune
  once."
- **A required/blocking check** — rejected: an LLM's subjective findings
  should not gate merges; that is the deterministic CI's role.
- **A GitHub organization** (org secret, org reusable workflow, rulesets)
  — the only path to a truly central key and auto-application, but moving
  personal repos into an org is disproportionate now. Revisit if the
  per-repo secret becomes a burden.
- **A composite action instead of a reusable workflow** — rejected:
  reusable workflows are the supported way to share across private repos.

## Consequences

- One place to tune the reviewer; consistent review across projects.
- Each adopting repo needs (a) the ~12-line caller and (b) its own
  `ANTHROPIC_API_KEY` secret (no central key on a personal account), and
  this repo must allow reusable-workflow access from user-owned repos
  (one-time Actions setting).
- Per-token API cost per reviewed PR — bounded by the trigger/skip rules.
- A third-party action dependency, pinned and reviewed like any other
  (ADR 0003).

## References

- ADR 0015 (review checklist / red-green evidence); ADR 0003 (dependencies
  are decisions).
- `.github/workflows/claude-review.yml`; `templates/github/claude-review.yml`.
- `anthropics/claude-code-action` (pinned `@v1`).
