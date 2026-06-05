# Working notes for AI agents in this repo

This file orients an AI coding agent for **<project name>**. It is
intentionally short. The global practices live in
`~/Developer/methodology/methodology.md`; the durable project-specific
rules live in `docs/adr/` and `docs/glossary.md`.

## Read first, every session

1. `~/Developer/methodology/methodology.md` — the practices and why
   (global; read once if unfamiliar).
2. `docs/glossary.md` — this project's ubiquitous language. Use these
   terms exactly.
3. `docs/adr/` — every numbered ADR is a binding decision unless its
   status says `superseded`. Read the most recent ones first.
4. The `specs/<feature>/` folder for the feature you are working on,
   if one was named.

## Hard rules

- **Never invent a domain term.** If a concept needs a name and one
  doesn't exist in `docs/glossary.md`, stop and propose it.
- **No code without a spec for non-trivial work.** If the request is
  larger than a single function or bugfix, draft `specs/<slug>/spec.md`
  first and confirm before implementing. Templates:
  `~/Developer/methodology/templates/spec/`.
- **One PR-sized change per task.** If a task's diff grows past ~300
  lines, split it.
- **Decisions get ADRs.** Write an ADR for any decision that is
  **expensive to reverse**, **affects multiple components**, or
  **constrains future choices**. Skip ADRs for things you can change
  in five minutes without telling anyone. Template:
  `~/Developer/methodology/templates/adr/_template.md`.
- **Tests before merge.** New behavior ships with tests; bug fixes
  ship with a regression test. Test behavior, not implementation.
- **Conventional Commits.** `feat:`, `fix:`, `docs:`, `refactor:`,
  `test:`, `chore:`, `perf:`, `build:`, `ci:`. `!` for breaking changes.

<!-- Add project-specific hard rules below, each backed by an ADR.
     e.g. "Never represent money as a float — see ADR 0004." -->

## What this file is not

This file is a pointer, not the methodology. If something here
contradicts `~/Developer/methodology/methodology.md` or a project ADR,
the ADR wins and this file should be updated.
