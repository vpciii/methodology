# ADR 0005: Dual-audience navigability and artifact integrity

- **Status:** Accepted
- **Date:** 2026-06-05
- **Deciders:** vpc

## Context

The methodology is meant to be followed by **both humans and AI
agents** (e.g. Claude). Humans tolerate scattered criteria and infer
reading order; agents do better with an explicit, machine-navigable
surface. Three concrete problems surfaced:

1. **Discovery / portability.** Project files and the global pointer
   hard-code `~/Developer/methodology`. On another machine, a clone at
   a different path, or a shared project, those references dangle — an
   agent then can't find the methodology at all.
2. **"Which artifact when?" was scattered** across §1, §2, and the
   hard rules. An agent (or a hurried human) has no single place to
   decide spec-vs-ADR-vs-test-vs-glossary.
3. **No stated reading order** and no concrete agent operating rules,
   only the philosophical "durable semantic interface" framing.

Separately, the doc warned that stale artifacts are worse than none
but only mechanized freshness for ADRs (append-only). The "docs ride
with the code" rule and "automate what's checkable" rule were missing.

## Decision

Make the methodology explicitly usable by humans and agents alike, and
keep its artifacts honest:

- **Stable discovery via `$METHODOLOGY_HOME`.** All references use
  `$METHODOLOGY_HOME` (default `~/Developer/methodology`). It is set in
  `~/.claude/settings.json` `env` so every Claude session resolves it,
  and documented for shell profiles. Projects/templates reference the
  variable, not a hard path.
- **A "Using this methodology" section** in `methodology.md` with: a
  **reading order** (onboarding path), a **decision guide** table
  (which artifact to produce when — including "throwaway work →
  nothing but a good commit message"), and concrete **operating rules
  for AI agents** (read before write; produce artifacts not just code;
  stop and ask on undefined domain terms or hard-to-reverse decisions;
  a failing test is the most precise spec; the human is author of
  record).
- **Artifact integrity rules:** docs change in the **same PR** as the
  behavior they describe (no "docs later"); ADRs remain append-only
  (supersede, never edit); **anything machine-checkable is enforced in
  CI**, not left to memory (tests, types, lint, commit format).
- **Definition of Ready** added to `CONTRIBUTING` to balance the
  existing Definition of Done.

## Alternatives considered

- **Leave hard-coded paths** — rejected: breaks agent discovery off
  this machine; the env-var indirection is cheap.
- **A separate AGENTS.md** — rejected: a second audience-specific doc
  drifts from the human one. One methodology, dual-audience, is the
  point. (`CLAUDE.md` remains only a thin pointer.)
- **Heavier process gates** — rejected: the decision guide and DoR are
  lightweight and explicitly include the "do nothing" path for trivial
  work, preserving the anti-ceremony stance.

## Consequences

- An agent dropped into any project can find the methodology, decide
  what to produce, and know the reading order — without bespoke
  prompting.
- Artifacts stay current because doc updates ship with the code.
- One indirection to maintain (`$METHODOLOGY_HOME`); if unset, the
  documented default path still resolves for a human.

## References

- `methodology.md` ("Using this methodology"); `~/.claude/settings.json`
  (`env`), `~/.claude/CLAUDE.md`; `templates/project-CLAUDE.md`,
  `templates/project-CONTRIBUTING.md`; ADR 0001.
