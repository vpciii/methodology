# Spec: <Feature name>

- **Status:** Draft | Under review | Approved | Implemented | Superseded | Withdrawn
- **Date:** YYYY-MM-DD
- **Author:** name
- **Related ADRs:** ADR-NNNN, ADR-NNNN

> This spec is editable while `Draft` / `Under review` / `Approved`.
> When it reaches `Implemented` it **freezes** into a historical record;
> a contradiction found later goes to a test, a new spec, or an ADR —
> not back into this file (methodology §2, §8).

## Problem

One or two paragraphs. What is wrong, missing, or worth doing? Who
notices the problem today, and how? Why now?

Avoid solutions in this section. Describe the situation, not the
remedy.

## Goals

A short, ordered list of what success looks like. Each goal is a
statement about user-visible outcomes or system properties, not
implementation details.

1. …
2. …

## Non-goals

Explicit list of things this feature will *not* do. Equally important
as the goals — non-goals prevent scope creep and clarify intent for
reviewers.

- …
- …

## Requirements

Use [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) keywords. Give
every requirement a stable id (`R-1`, …). Each `MUST` / `MUST NOT`
requirement is reflected in at least one success criterion below, so it
inherits a test (methodology §5, ADR 0011); `SHOULD` / `MAY` requirements
may be, but need not be.

Non-functional requirements — latency, availability, data retention,
and the like — are requirements too: state them here when they are
load-bearing rather than leaving them implied.

- **R-1 (MUST)** …
- **R-2 (MUST NOT)** …
- **R-3 (SHOULD)** …
- **R-4 (MAY)** …

## Success criteria

Concrete, measurable signals that this feature is working. Each gets a
stable id (`SC-1`, `SC-2`, …) and is verified by at least one test that
cites that id (methodology §5); together they cover every `MUST` /
`MUST NOT` requirement above. Ids are append-only — never reuse or
renumber them.

- **SC-1** — …
- **SC-2** — …

## Open questions

Things the spec does not yet answer. Each question is resolved before
the spec is approved, either inline or by adding an ADR.

- [ ] …
- [ ] …

## Out of scope (for now)

Adjacent things that came up during scoping but are deferred. Linked
to follow-up issues or specs when known.

- …

## Traceability

Built up as the feature is implemented; complete before the spec is
marked `Implemented`. Every success-criterion id maps to the test(s)
that verify it and records which requirement(s) it covers, so the
`R-… → SC-… → test` chain is explicit; a CI check fails on any criterion
left uncovered, and every `MUST` / `MUST NOT` requirement appears in this
table (methodology §5, ADR 0011).

| Criterion | Requirement(s) | Verified by (test) |
|---|---|---|
| SC-1 | R-1 | `tests/…::test_…` |
| SC-2 | R-2, R-3 | `tests/…::test_…` |
