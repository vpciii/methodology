# ADR 0011: Every MUST requirement maps to a success criterion

- **Status:** Accepted
- **Date:** 2026-06-08
- **Deciders:** vpc

## Context

Practice §5 makes **success criteria the verification surface**: each
`SC-…` carries a stable id, maps to at least one test that cites it, is
recorded in the spec's Traceability table, and a CI check fails on any
criterion left uncovered (ADR 0006). "Done" is therefore provable for
success criteria.

But `spec.md` also states obligations as RFC 2119 **requirements**
(`R-…`), and the template only asked for an id "when it is worth tracing
to a test." Nothing linked a requirement to a success criterion. The
result is a silent gap: a spec can carry `R-1 (MUST)` with no
corresponding `SC`, every `SC` can be covered by a passing test, and the
feature reports done — while the `MUST` was never tested. The
provable-completion property proves the criteria are met, not that the
requirements are. This is exactly the kind of internally-consistent gap
an agent walks straight through (ADR 0008).

## Decision

Every `MUST` / `MUST NOT` requirement carries a stable id and is
**reflected in at least one success criterion**; success criteria remain
the single, CI-checked verification surface.

- Requirements are the obligation; success criteria are what must cover
  them; tests verify the criteria. The chain is `R-… → SC-… → test`.
- The spec's **Traceability table gains a Requirement(s) column**, so the
  chain is explicit and every `MUST` / `MUST NOT` appears in the table.
- `SHOULD` / `MAY` requirements *may* map to a success criterion but need
  not. Only `MUST` / `MUST NOT` obligations are required to.
- Checking that every `MUST` is covered is, like the criterion-coverage
  check itself (ADR 0006), a project tooling decision — the rule and the
  table convention are global; the CI mechanism is per project.

## Alternatives considered

- **Two-level CI traceability (`R → SC → test` enforced directly)** —
  more complete, but more machinery and a second verification surface to
  maintain. Rejected in favor of the simpler invariant "every `MUST` is
  covered by some `SC`," which keeps one surface (success criteria) and
  reuses the existing coverage check.
- **Status quo — trust authors to write criteria that cover the
  requirements** — rejected: this is precisely the silent gap. "Done" is
  provable for criteria but says nothing about the requirements, and the
  failure is invisible in an otherwise consistent spec.
- **Drop `R-…` requirements; express everything as success criteria** —
  rejected: RFC 2119 normative language states obligations precisely and
  in a different register from a measurable signal. Collapsing the two
  loses the "MUST vs SHOULD vs MAY" distinction that makes requirements
  useful.

## Consequences

- A normative obligation can no longer be shipped untested; the
  `R-… → SC-… → test` chain is explicit and (optionally) CI-checkable.
- Cost: spec authors give every `MUST` / `MUST NOT` an id and ensure a
  criterion covers it, and the Traceability table carries one more
  column.
- The single-surface design is preserved: tests still verify success
  criteria, not requirements directly — requirements just may not float
  free of a criterion.

## Adoption impact

**Per-project action.** When next authoring or touching a spec: give
every `MUST` / `MUST NOT` requirement a stable id, ensure each is
reflected in at least one success criterion, and add the **Requirement(s)**
column to the Traceability table. Optionally extend the existing
spec-coverage CI check to assert every `MUST` requirement is covered
(ADR 0006). The rule itself arrives by reading §5.

## References

- `methodology.md` §5 (tests as executable specification).
- ADR 0006 (checkable spec↔test traceability — the coverage check this
  builds on); ADR 0008 (agent drift — the silent-gap failure mode).
- `templates/spec/spec.md` (Requirements, Success criteria, Traceability);
  `templates/project-CONTRIBUTING.md` (Definition of Done).

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
