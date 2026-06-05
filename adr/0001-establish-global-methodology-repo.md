# ADR 0001: Establish a standalone global methodology repository

- **Status:** Accepted
- **Date:** 2026-06-05
- **Deciders:** vpc

## Context

A coherent development methodology — ADRs, spec-first development,
light DDD, trunk-based development with small PRs, tests as executable
specification, twelve-factor, conventional commits, operational
feedback loops — had been developed and was living inside a single
project (`finstack`), entangled with that project's specifics
(financial glossary, FastAPI/Postgres stack ADRs, a "money as integer
minor units" rule).

The same practices were wanted across *all* projects, not just one.
Copying `methodology.md` into each repo would create drift: N copies,
each aging independently. The methodology's own ethos — "document the
artifact, not the tool" — argues for one durable, tool-agnostic home.

## Decision

We will maintain the methodology as a standalone git repository at
`~/Developer/methodology`, generic to any language/framework/tool, as
the single source of truth. Projects reference it by path from their
own `CLAUDE.md`; they do not vendor a copy. A lean global
`~/.claude/CLAUDE.md` inlines the hard rules and points at the
canonical document so every Claude session (in any repo) is oriented.

## Alternatives considered

- **Keep it in `finstack`** — rejected: ties a global methodology to
  one project; other repos can't cleanly reference it.
- **Put the full doc in `~/.claude/CLAUDE.md`** — rejected: injects
  ~280 lines into every session (token cost on every turn) and binds
  a deliberately tool-agnostic methodology to one tool.
- **Vendor a copy into each project** — rejected: guarantees drift
  across N copies; defeats "one source of truth."

## Consequences

- One place to read and to change the methodology; updates propagate
  by reference, not copy.
- Projects stay lean: a short `CLAUDE.md` pointer plus project-local
  artifacts (ADRs, glossary, specs).
- Trade-off: the canonical doc lives outside any individual project,
  so a project checked out alone (e.g. on another machine without
  this repo) loses the full text — the inlined hard rules in the
  global and project `CLAUDE.md` mitigate this. If cross-machine
  portability becomes important, push this repo to a remote.
- `finstack` keeps its project-specific artifacts (its glossary, its
  stack ADRs, its money-as-minor-units rule); only the generic
  methodology was promoted here.

## References

- `methodology.md` (this repo) — the promoted, genericized document.
- Original: `~/Developer/personal/finstack/docs/methodology.md`.
