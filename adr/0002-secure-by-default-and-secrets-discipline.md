# ADR 0002: Security and secrets as a first-class practice

- **Status:** Accepted
- **Date:** 2026-06-05
- **Deciders:** vpc

## Context

The initial methodology (ADR 0001) had no security practice. Secrets
were addressed only tangentially via the Twelve-Factor "config in the
environment" factor. In practice, the absence bit us: live API
key/secret pairs were found stored in plaintext in a tool's
configuration, and security-relevant behavior had no home in the
spec/test/ADR loop. A methodology that both humans and AI agents
follow needs security to be an explicit, artifact-producing practice —
agents in particular will not infer an unstated security posture.

## Decision

Add **"Security and secrets by default"** as a named practice
(methodology §9), expressed in the same artifact-centric terms as the
rest of the methodology:

- **Secrets never live in the repository.** Not in code, config,
  fixtures, or committed env files. They come from the environment or
  a secret manager. A leaked secret is rotated, not just deleted.
- **Trust boundaries and the authorization model are decisions** —
  they get ADRs (they are expensive to reverse, cross-component, and
  future-constraining by definition).
- **Security-relevant bugs ship with a regression test**, exactly like
  any other bug (extends §5 and the §8 operational-feedback rule).
- **Validate input at trust boundaries; default to least privilege.**
  These are design defaults, not afterthoughts.

It stays tool-agnostic: no scanner or vendor is named. The durable
artifacts are the ADR (the boundary/decision) and the test (the proof).

## Alternatives considered

- **Keep security implicit / per-project** — rejected: agents and new
  contributors won't apply an unwritten standard, and "secrets in repo"
  recurs without a stated rule.
- **A separate SECURITY.md standard** — rejected for the core doc:
  security belongs in the methodology's practice list so it's read with
  everything else. A per-project `SECURITY.md` may still exist for
  disclosure policy.

## Consequences

- Security decisions become discoverable (ADRs) and verifiable (tests)
  rather than tribal knowledge.
- One more practice in the list — justified: it is durable and
  language/tool-independent.
- Does not adopt heavyweight machinery (formal threat-model templates,
  specific scanners); those, if chosen, get their own project ADR.

## References

- `methodology.md` §9, §5, §8; ADR 0001.
