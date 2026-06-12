# ADR 0020: User-facing documentation rides along

- **Status:** Accepted
- **Date:** 2026-06-12
- **Deciders:** vpc

## Context

Every artifact in the artifact map is contributor-facing: ADRs, specs,
glossary, architecture doc, tests. The "docs change in the same PR as
the behavior" rule binds exactly those — a change that makes "the
glossary, an ADR, a spec, or the README wrong" must fix it in the same
change. Nothing binds the documentation a project's *users and
operators* rely on: usage guides, API reference, runbooks.

For a project with actual users, that is a real lifecycle stage with no
home and no honesty rule. The drift is identical in kind to
architecture-doc drift — the document describes a system that no longer
exists — but unlike architecture drift it is *externally* visible, and
§8's observability mandate presumes an operator who can act on what
they see, which in practice means a runbook that is not lying to them.

## Decision

Extend the existing honesty rule rather than adding a practice:

- **The same-PR rule explicitly binds user-facing documentation.** A
  user-visible behavior change updates the usage docs, API reference,
  or runbook it invalidates in the same PR. No "docs later."
- **The artifact map gains a row** naming the conventional home:
  `README.md` usage plus `docs/`; a project that adopts an external
  docs site records that as its own tooling ADR, as with any tooling
  choice.
- **`CONTRIBUTING.md` makes it checkable**: the definition of done and
  the review checklist's "artifacts ride along" item name user-facing
  docs explicitly.

Scale-to-work applies unchanged: a library with no users beyond its
README, or an internal tool with no operators, has nothing to update —
the rule binds only docs that exist and are invalidated.

## Alternatives considered

- **A new numbered practice ("§12 Documentation")** — rejected: the
  entire discipline is one sentence of the existing keep-artifacts-
  honest rule. A numbered practice with origins and a "why this lasts"
  would be ceremony around a clause.
- **Mandate a docs-as-code toolchain** (docs site generator, doc tests,
  link checkers) — rejected: a premature tooling commitment, which the
  methodology explicitly avoids; each project decides its toolchain
  with its own ADR.
- **Status quo — "the README covers it"** — rejected: the README is the
  front door, a short pointer (artifact map's own words). API reference
  and runbooks accrue in any real project regardless; without a rule
  they rot, and the rot is user-visible.

## Consequences

- User-facing docs stop rotting by default; the review checklist makes
  the rule enforceable in the same pass that already checks the other
  artifacts.
- Behavior-changing PRs get slightly larger — that is the point, and it
  matches how every other artifact already works.
- Projects without user-facing docs are untouched (scale-to-work).
- The conventional home is deliberately loose (`README.md` + `docs/`);
  precision about structure stays a per-project decision.

## Adoption impact

**Reference-only** for the rule — it arrives by reading. **Per-project
action (optional):** re-sync `CONTRIBUTING.md` (definition of done,
review checklist) from the template. Forward-only: no backfill of
existing docs; the rule binds from the next behavior change.

## References

- `methodology.md` — "Keep the artifacts honest," artifact map, §8
  (observability presumes an actionable operator surface).
- ADR 0005 (artifact integrity / navigability), ADR 0015 (review
  checks artifacts ride along), ADR 0012 (forward-only adoption).
- `templates/project-CONTRIBUTING.md`.

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
