# ADR 0025: One-off operations on production get a record

- **Status:** Accepted
- **Date:** 2026-09-29
- **Deciders:** vpc

## Context

The methodology covers changes that ship through code: a feature gets a
spec, a decision an ADR, behavior a test, a release a deploy. It says
nothing about a change made **directly to production outside the
normal deploy path** — a data repair, a bulk send, a backfill, a
one-time account cleanup. These are real, recurring, and often
irreversible, and the one live adopter does them regularly.

Evidence from nurturepa/cif (a HIPAA-constrained SMS platform, adopted
2026-07-13):

- **Two county SMS campaigns** (Aug 13, Aug 15) were run by hand through
  an existing endpoint, because the proper feature
  (`specs/admin-bulk-message-send`) is still Draft. Each has a careful
  record — decisions, pre-flight checks, opt-out scan, dry run,
  post-send verification — filed under `planning/aug13-county-campaign/`
  because there was nowhere else. Its README opens *"Not a spec"*.
  `planning/` is for bets that converge to a spec (planning.md, Scope);
  these don't.
- **A dormant-accounts script** that locks users and *irreversibly*
  overwrites their passwords (`6a193c46`, typed `security:`). Its
  review found the guard would have passed on a demo or training
  database with a fourth account and overwritten real users' passwords
  there. The fix — refuse on any surprise, verify by name not id —
  was the right shape, but nothing in the methodology asked for it.
- **A data repair** (`8aa3d698`, `scripts/data-repairs/`): a hand edit
  on 2026-04-28 copied one user's row over another's, "outside the app
  and unaudited", in a system whose rules require an audit entry for
  every PHI access. The repair script is exemplary (guarded, ends in
  `ROLLBACK`, dry-run first). But the *cause* — an out-of-band manual
  edit to production — produced no regression test, ADR, spec update,
  or postmortem. §8 would have required one; nothing flagged that it
  applied, because the incident surfaced as a chore.

So the practice is being done well by instinct, filed inconsistently,
and the one place it matters most (the manual edit that caused harm)
fell through a gap between §8 and §11.

## Decision

We will treat a one-off change to **production** — any environment
holding real user or customer data (spelled out in rule 3) — as an
**operation**, with a lightweight record and three rules drawn from
existing practices. No new machinery.

1. **An operation gets a record** at
   `operations/YYYY-MM-DD-<slug>/README.md` — dated when planned, since
   the record exists before the run (template
   `templates/operation.md`), with its scripts beside it. The record
   states purpose, environment, pre-flight checks, the exact procedure,
   verification, and the undo — then, after running, what actually
   happened. Once run it **freezes** like an `Implemented` spec (ADR
   0007); a reusable procedure graduates to a runbook in `docs/`
   (user-facing docs, ADR 0020) or to a feature.
2. **Operations follow the existing rules, applied to data:**
   reviewed before running (a PR, like code — §4) — except a repair
   made *during* an active incident, where waiting would prolong it:
   then the record and its review follow immediately after, and the
   operation is still recorded; **guarded** —
   the script checks its premise and refuses on anything unexpected,
   dry-runs on a non-production copy first, and defaults to a
   transaction that rolls back; **reversible by default** — an undo
   (a snapshot, an inverse script) or an explicit
   *irreversible* callout, which §11 already routes to an ADR.
3. **An out-of-band change to production that bypassed its normal
   path is an incident** (§8) when discovered, whether or not anyone
   noticed harm yet. "Production" means any environment holding real
   user or customer data — which can include a demo or training system
   people actually use — not staging or scratch copies, where a hand
   edit is ordinary work. Such an incident gets at least one of a
   regression test, an ADR, or a spec update, and a postmortem if
   user-visible. The repair operation links it.

**Scale to the work:** read-only queries and reports are not
operations; a routine, already-documented procedure (a runbook step)
needs no new record each time. The record earns its keep when the
change is one-off, touches real data or users, or is hard to undo.

## Alternatives considered

- **Leave it to projects** (each picks a folder and conventions) —
  rejected: the one adopter already did, and the result was ops records
  in `planning/`, repairs in `scripts/`, and an incident that skipped
  §8. The *home* is a project detail; the *rules* (guarded, reversible,
  out-of-band edits are incidents) are what went missing.
- **Require a spec for each operation** — rejected: an operation isn't
  a feature with success criteria and tests; forcing it into `spec.md`
  is the ceremony the methodology warns against, and cif's campaign
  records are explicitly "not a spec."
- **Put records under `planning/`** (status quo in cif) — rejected:
  planning converges to a spec and freezes as a bet; an operation
  converges to an executed change. Mixing them muddies both.
- **Put records under `docs/runbooks/`** — rejected as the default: a
  runbook is a *reusable* procedure kept current; an operation record
  is a *one-time* event frozen once run. The template says when one
  graduates to the other.
- **Home under `docs/operations/`**, beside the other records —
  rejected: an operation's scripts are part of it (the exact SQL that
  ran is the record), and scripts under `docs/` sit badly with tooling
  that treats `docs/` as prose. A top-level folder keeps record and
  scripts together.
- **Name the folder `ops/`** — rejected: the path should name the
  artifact, as ADR 0016 chose `postmortems/` over `incidents/`, and
  `ops/` already commonly holds infrastructure and deploy tooling in
  adopting repos, where it would collide. `operations/` is unambiguous.
- **Treat every out-of-band edit as an incident, in any environment** —
  rejected: hand-editing staging or a scratch database is ordinary work;
  making it owe a regression test or ADR contradicts "scale the ceremony
  to the work." The evidence is all production.
- **Require an ADR for every operation** — rejected: most repairs are
  not decisions. §11 already requires one for the genuinely
  irreversible case.

## Consequences

- One conventional home and shape for work that currently has none;
  `planning/` goes back to meaning bets.
- The guard / dry-run / rollback-by-default pattern cif discovered
  becomes the expected shape, not a lucky instinct.
- Manual edits to production stop being invisible to §8: they become
  incidents with a follow-through, which in a regulated system is the
  point.
- A small cost per operation (one short README). Mitigated by the
  scale-to-work clause and the template.
- Projects with existing homes (`scripts/data-repairs/`) need not move
  history — adoption is forward-only (`adopting.md`).
- Cheap to reverse: supersede this ADR.

## Adoption impact

**Per-project action, forward-only.** The next one-off operation on a
production system is recorded at `operations/YYYY-MM-DD-<slug>/` from
`templates/operation.md`; existing records stay where they are. When an
out-of-band manual change is discovered, run it through §8.

For nurturepa/cif specifically (a suggestion, not part of this ADR's
decision): the 2026-04-28 manual edit behind `8aa3d698` is the first
candidate for the §8 follow-through.

## References

- `methodology.md` §4, §8, §11, decision guide, artifact map;
  `planning.md` Scope; `templates/operation.md`;
  `templates/global-CLAUDE.md` (ADR 0018).
- ADR 0004 (reversible by default), ADR 0007 (freeze), ADR 0016
  (postmortems), ADR 0020 (runbooks as user-facing docs).
- Evidence: nurturepa/cif `planning/aug13-county-campaign/`,
  `planning/aug15-county-campaign/`, `scripts/data-repairs/`, commits
  `6a193c46`, `8aa3d698`.

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
