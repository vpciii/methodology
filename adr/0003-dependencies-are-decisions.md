# ADR 0003: Dependencies are decisions

- **Status:** Accepted
- **Date:** 2026-06-05
- **Deciders:** vpc

## Context

The methodology said *tech-stack* choices get ADRs, but said nothing
about ongoing dependency hygiene. Every added dependency is a
future-constraining choice: it expands the supply-chain attack
surface, imposes a maintenance and licensing obligation, and is often
harder to remove than to add. Humans tend to add dependencies
casually; AI agents even more so. Left unstated, the cost is invisible
until it isn't.

## Decision

Add **"Dependencies are decisions"** as a named practice
(methodology §10):

- **Adding a dependency is a decision.** Weigh maintenance health,
  license compatibility, supply-chain surface, and whether the need
  could be met with the standard library or existing deps. Record a
  non-trivial addition as an ADR (especially anything load-bearing,
  copyleft-licensed, or sparsely maintained).
- **Lockfiles are committed.** Builds are reproducible; versions are
  pinned and updated deliberately, not drifting silently.
- **Updates are deliberate.** Dependency bumps are normal `chore:`
  work, reviewed like any change; a major-version bump that changes
  behavior may warrant its own ADR.

## Alternatives considered

- **Fold into the existing "tech-stack ADR" line** — rejected: that
  line covers the initial stack choice, not the steady-state habit of
  adding/upgrading deps, which is where the risk actually accrues.
- **A tooling mandate (specific SCA scanner, Dependabot config)** —
  rejected for the core doc: tool choices are per-project ADRs. The
  durable rule is "weigh and record," not a particular tool.

## Consequences

- The true cost of a dependency is considered at add-time and left in
  the decision trail.
- Reproducible builds via committed lockfiles.
- Slightly more friction to add a dependency — intended.

## References

- `methodology.md` §10, §1; ADR 0001.
