# Operation: <short name>

- **Status:** Planned | Run | Aborted
- **Environment:** e.g. prod / staging / demo
- **Planned:** YYYY-MM-DD
- **Run:** YYYY-MM-DD (by whom)
- **Reversible:** Yes — see Undo | **No** — see ADR-NNNN

> A one-off change to a live environment outside the normal deploy path
> (methodology §11, ADR 0025). File as `ops/YYYY-MM-DD-<slug>/README.md`
> with its scripts beside it. Reviewed before it runs; **frozen once
> run** — append to "What happened", never rewrite. If you run this more
> than once, graduate it to a runbook in `docs/` or build the feature.

## Why

What needs changing and why it can't wait for (or doesn't warrant) a
feature. If this repairs damage from an out-of-band change, link its
incident / postmortem (§8).

## Scope

Exactly what is touched: which rows, records, users, or messages, and
how they are selected. Counts, not just criteria.

## Pre-flight checks

What the script verifies before it changes anything, and what makes it
**refuse**. Check the premise (the data looks like you think it does),
identify things by stable names rather than ids that differ between
environments, and cap the blast radius.

- [ ] …

## Procedure

The exact steps and scripts, in order. Default to a transaction that
rolls back unless explicitly committed. Dry-run on a non-production copy
first and note what that run can and cannot prove.

1. …

## Verification

How you'll know it worked — the queries or checks run afterwards, and
their expected results.

## Undo

The snapshot, inverse script, or manual steps that reverse this. If it
cannot be undone, say so plainly and link the ADR (§11).

## What happened

Filled in after running: date, who, actual counts, verification
results, anything surprising. Append-only.
