# Plan: <Feature name>

- **Status:** Draft | Under review | Approved | Implemented | Superseded | Withdrawn
- **Date:** YYYY-MM-DD
- **Author:** name
- **Spec:** ./spec.md
- **Related ADRs:** ADR-NNNN

> This plan freezes with its spec: editable while `Draft` / `Under
> review` / `Approved`, and a historical record once `Implemented`
> (methodology §2, ADR 0007). A contradiction found later goes to a test,
> a new spec, or an ADR — not back into this file.

## Approach

One or two paragraphs describing the implementation approach at the
right altitude — enough that a reviewer can disagree before code is
written. Save fine-grained details for `tasks.md`.

## Components touched

List the modules, services, packages, or files this change will
modify or create.

- `path/to/component` — what changes and why
- `path/to/component` — …

## Data model changes

Any new tables, columns, indexes, or migrations. Include the shape
inline; do not link out to a moving target. Call out data sensitivity:
any new personal or regulated data, where it lives, how long it is
kept, and how it is deleted.

```
-- example
```

## API changes

New or modified endpoints, message shapes, or CLI commands. Specify
request/response examples. Note backwards-compatibility implications.

## Alternatives considered

For each serious alternative: one short paragraph on what it was,
why it was attractive, why it was rejected. If an alternative
becomes load-bearing later, lift it into a full ADR.

- **Option A** — …
- **Option B** — …

## Risks

Honest list of what could go wrong, ordered by likelihood × impact.
For each risk, a mitigation or a reason we are accepting it.

| Risk | Likelihood | Impact | Mitigation |
| ---- | ---------- | ------ | ---------- |
|      |            |        |            |

## Rollout

How does this ship? Behind a flag? In one PR or several? Any
backfill, migration, or coordination required? How will we know it
worked in production?

## Observability

What new logs, metrics, or traces are needed to know this feature is
healthy after deploy?

## Test strategy

What level(s) of test (unit, integration, end-to-end) and what the
critical cases are. Use property-based tests for invariants that must
hold over an infinite input space (money math, access control,
idempotency, state transitions).
