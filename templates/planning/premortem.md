# Pre-mortem: <bet name>

- **Status:** Open | Assumptions tested | Cleared | Dropped
- **Date:** YYYY-MM-DD
- **Author:** name

> Imagine it shipped and failed — work backward to why, then probe the
> most dangerous assumptions cheaply before committing (planning.md §5).

## "It failed. Why?"

The ways this bet could fail, as if it already had. Be specific and
blunt; quantity first, judgment after.

- …
- …

## Assumptions it depends on

The load-bearing assumptions behind the bet, each rated for confidence
and for impact if wrong.

| Assumption | Confidence (H/M/L) | Impact if wrong (H/M/L) |
|---|---|---|
| | | |

## Spikes

For the high-impact / low-confidence assumptions, a time-boxed
experiment to retire the unknown. Throwaway code is fine — the *finding*
is the deliverable.

| Assumption | Spike (time-boxed) | Finding |
|---|---|---|
| | | |

## Disposition

For each dangerous assumption: **retired** (with the finding),
**accepted** (with rationale), or **escalated** into the spec's
`## Open questions`.
