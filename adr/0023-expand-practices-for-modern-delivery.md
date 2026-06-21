# ADR 0023: Expand methodology with modern delivery practices

- **Status:** Accepted
- **Date:** 2026-06-21
- **Deciders:** vpciii, Antigravity

## Context

The current methodology provides a highly robust, tool-agnostic foundation for software engineering that works well for human-agent teams. It distills time-tested practices such as ADRs, Spec-first development, TDD, and Trunk-based development. 

However, during a review of the methodology against empirical DevOps research (such as DORA metrics) and friction points in day-to-day development, a few gaps emerged. Specifically, the methodology did not explicitly mandate deterministic local environments, completely automated linting/formatting, continuous deployment (CD), or explicit code review culture guidelines. While some of these were implicitly supported by Trunk-based development and Twelve-Factor guidelines, making them explicit numbered practices ensures they are treated as non-negotiable standards rather than optional enhancements.

## Decision

We will expand the methodology to include six additional core practices:
1. **Deterministic Dev Environments** (One-Command Onboarding)
2. **Automated Quality Gates** (Strict linting/formatting in CI)
3. **Continuous Deployment** (Zero-touch automated releases)
4. **Continuous Refactoring** (The Boy Scout Rule)
5. **Code Review Culture** (Blameless, behavior-focused, async-first)
6. **Documentation as Code** (Treating docs like code)

## Alternatives considered

- **Option A: Embed these into existing practices** — We considered expanding "Trunk-based development" to include Continuous Deployment and Code Review Culture, and expanding "Twelve-Factor" to cover Deterministic Environments. This was rejected because these concepts are distinct enough to warrant their own dedicated focus. Hiding them under other headings diminishes their importance.
- **Option B: Maintain the status quo** — Keep the list at 11 practices to prioritize brevity. Rejected because the lack of explicit guidance on local environments and CI/CD quality gates frequently leads to "works on my machine" issues and bikeshedding during code review.

## Consequences

- **Easier:** Onboarding new developers (and AI agents) becomes instantly deterministic. Code reviews become faster and less contentious because formatting and style are strictly automated. Tech debt is managed continuously.
- **Harder:** Initial project setup requires slightly more investment to configure DevContainers/Nix/Makefiles, CI pipelines for CD, and strict linters.
- **New constraints:** PRs cannot be merged if they fail style checks, and code must be left cleaner than it was found.

## Adoption impact

*Reference-only* for the methodology itself (arrives by reading `methodology.md`).
*Per-project action* required: Projects must verify they have a deterministic setup command, automated style checks in CI, and automated deployment pipelines to fully comply with the new practices.

## References

- [DORA Metrics / Accelerate (Forsgren et al.)](https://dora.dev/)
- [The Boy Scout Rule](https://deviq.com/principles/boy-scout-rule)
