# Postmortem: <incident short name>

- **Status:** Draft | Complete
- **Incident date:** YYYY-MM-DD
- **Written:** YYYY-MM-DD
- **Author:** name

> Short and blameless: focus on what the system *permitted*, not who
> pushed which button (methodology §8). This file records the incident;
> the durable deliverable is the follow-through below — at least one
> regression test, ADR, or spec update. File as
> `docs/postmortems/YYYY-MM-DD-<slug>.md`.

## What happened

Two or three sentences, plus a brief timeline if it helps. Plain
language — a reader six months from now should understand it without
tribal knowledge.

## Impact

Who or what was affected, how badly, for how long. User-visible
effects first; data effects called out explicitly.

## Contributing causes

What the system permitted that let this happen — a missing validation,
an unguarded boundary, an untested path, an ambiguous spec. Systems
and gaps, not names. More than one cause is the normal case.

- …
- …

## Follow-through (methodology §8 — at least one)

The artifact(s) this incident produced. An empty table means the loop
is still open, not that there was nothing to learn.

| Deliverable | Artifact | Status |
|---|---|---|
| Regression test (failed on the incident's behavior, now passing) | `tests/…::…` | |
| New or updated ADR | ADR-NNNN | |
| Spec update / new spec | `specs/…` | |

## Where we got lucky

Optional. Near-misses that limited the blast radius by chance rather
than design — often the best source of the *next* follow-through item.
