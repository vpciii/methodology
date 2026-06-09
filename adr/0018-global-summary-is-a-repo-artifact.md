# ADR 0018: The always-loaded global summary is a repo artifact

- **Status:** Accepted
- **Date:** 2026-06-09
- **Deciders:** vpc

## Context

`~/.claude/CLAUDE.md` is the always-loaded summary of this methodology
— the surface every Claude session in every project reads, making it
the methodology's highest-frequency consumer. But it lived *only*
outside this repository, so the "docs change in the same PR as the
behavior" rule structurally could not reach it: a methodology change
could not update the summary in the same diff, and nothing else
remembered to.

The predictable result was found by a completeness review
(2026-06-09): the summary was missing the planning decision-guide row
(added in 0.6.0), the refactor row (0.7.0), and never mentioned
`planning.md` at all. ADR 0009 anticipated drift in *instantiated*
artifacts — copies of templates customized per project — but the
global summary was worse off: it was not a copy of anything. It had no
canonical source to drift *from*, only a memory of what it should say.

A second, smaller drift ran the other way: the summary stated
"sign-off between stages" as a hard rule, while `methodology.md` §2
said only that the *spec* is agreed before implementation — the
summary was stricter than the document it summarizes.

## Decision

- The summary's canonical source is
  **`templates/global-CLAUDE.md`**, in this repository. It is edited
  **in the same PR** as any change it summarizes — the same-PR honesty
  rule now reaches it.
- **Copying it to `~/.claude/CLAUDE.md` is the per-machine release
  step**, recorded in "Changing this document" and the README's wiring
  section. The deployed copy carries a header comment naming its
  source, so no one (human or agent) edits the copy in place.
- The live file tracks **released** versions: the copy happens when
  the change lands on `main`, not while it sits on a branch.
- Repair the current drift in both directions: the summary gains the
  planning and refactor rows, the postmortem and red→green updates
  from 0.8.0, and pointers to `planning.md` / `adopting.md`;
  `methodology.md` §2 gains the sign-off-between-stages rule the
  summary already claimed.

## Alternatives considered

- **Generate the summary from `methodology.md`** — rejected: the
  summary is a curated abridgment (different table shape, different
  emphasis), not a mechanical extraction, and build tooling for one
  markdown file is ceremony. If drift recurs despite the same-PR rule,
  revisit as a CI *check* (diff the deployed copy against the
  template), not a generator.
- **Symlink `~/.claude/CLAUDE.md` into the repo** — attractive (drift
  becomes impossible) but rejected: the always-loaded file would track
  the *working tree*, including unmerged branches and mid-edit states.
  Live agent behavior should change when a release lands, not when a
  draft is saved.
- **Status quo: maintain the file by memory** — rejected by
  demonstrated failure; two releases drifted in two days.

## Consequences

- The summary becomes reviewable: a PR that changes the decision guide
  shows the matching summary change in the same diff, and its absence
  is visible.
- One manual step survives — the copy to `~/.claude/`. Accepted: it is
  the release act ADR 0009 already prescribes for instantiated
  artifacts, and the `CHANGELOG.md` entry flags when it is due.
- A second machine (or a future tool with a different always-on file)
  bootstraps from the template instead of from whatever the last
  machine happened to contain.
- `methodology.md` §2 is now normatively complete on stage gates;
  the summary is no longer stricter than the canon.

## Adoption impact

**Reference-only for consuming projects** — their `CLAUDE.md` files
are unaffected. **Per-machine action for the methodology owner:** copy
`templates/global-CLAUDE.md` → `~/.claude/CLAUDE.md` now, and again
whenever a release notes that the summary changed.

## References

- `methodology.md` "Keep the artifacts honest", §2, "Changing this
  document"; README "How it's wired in globally".
- ADR 0005 (dual-audience navigability), ADR 0008 (stale-memory
  guardrails — the same failure mode, here at the infrastructure
  level), ADR 0009 (instantiated-artifact drift and the release
  mechanism this reuses).
