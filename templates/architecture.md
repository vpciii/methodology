# Architecture — <Project name>

- **Updated:** YYYY-MM-DD — changes in the **same PR** as the structure
  it describes (methodology §2; ADR 0005, 0007).

A short, current-state overview of how the system is shaped **now**.
This is a *navigational* document, not a decision log: it says *what*
the system is and points at `docs/adr/` for *why*. Keep it brief — a
stale one-pager is cheap to fix; resist letting it grow into detail the
code, tests, and ADRs already hold.

## What this is

One or two sentences: what the system does and for whom.

## System context

The system and the things outside it that it talks to — users, client
apps, upstream/downstream services, third-party APIs. A list or a small
diagram at the C4 "context" altitude is enough.

```
[ user ] → [ this system ] → [ external API ]
                  │
                  ▼
            [ data store ]
```

## Major components

The internal pieces and what each is responsible for. One line each;
link to the module or package.

| Component | Responsibility | Lives in |
|---|---|---|
| `<name>` | … | `path/` |

## Data stores

Databases, caches, queues, buckets — what each holds, and which data it
is the source of truth for.

| Store | Holds | Source of truth for |
|---|---|---|
| … | … | … |

## External dependencies

Third-party services and the load-bearing libraries the shape depends
on. Each significant one should trace to a dependency ADR
(methodology §10).

- `<service / lib>` — why it's here; ADR-NNNN.

## Trust boundaries

Where untrusted input enters and where authorization is enforced
(methodology §9). Each boundary should trace to an ADR.

- … — ADR-NNNN.

## Shape-defining decisions

The non-superseded ADRs that determine the current structure. A pointer
list, not a summary — read the ADRs for the reasoning.

- ADR-NNNN — what it fixed about the shape.
