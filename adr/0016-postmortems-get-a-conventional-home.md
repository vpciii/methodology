# ADR 0016: Postmortems get a conventional home

- **Status:** Accepted
- **Date:** 2026-06-09
- **Deciders:** vpc

## Context

§8 mandates that "postmortems are written for any user-visible
incident" — short, blameless, focused on what the system permitted.
But it was the only artifact the methodology mandates without saying
where it lives: no path in the artifact map, no template in
`templates/`. The asymmetry was conspicuous — the *pre*-mortem
(`templates/planning/premortem.md`, ADR 0010) has both.

An unanchored artifact decays into "we talked about it." The
methodology's own posture is that a written, mandated artifact has a
conventional home (the whole point of the artifact map), and that
incident records have reread value: a string of postmortems is where
patterns become visible — the same boundary failing twice is the
signal that the next deliverable is an ADR, not another test.

## Decision

- Postmortems live at **`docs/postmortems/YYYY-MM-DD-<slug>.md`**, one
  file per user-visible incident.
- A template ships at **`templates/postmortem.md`**: what happened,
  impact, contributing causes (systems, not names), and a
  **follow-through** section that records which §8 artifact(s) the
  incident produced.
- The artifact map and the decision guide's incident row point at the
  path.

The §8 rule itself is unchanged: the durable deliverable is still at
least one of a regression test, an ADR, or a spec update. The
postmortem records the incident and *links* the follow-through; it is
the wrapper, not the deliverable.

## Alternatives considered

- **Declare the postmortem ephemeral** — one sentence in §8 saying the
  write-up may be a scratch note; only the test/ADR/spec survives.
  Cheapest, zero ceremony added. Rejected: §8 already says postmortems
  *are written*; a mandated written artifact with no home contradicts
  the artifact map's purpose, and the incident record itself has
  pattern-spotting value the three deliverables don't carry.
- **`docs/incidents/` as the path** — rejected on ubiquitous-language
  grounds: the artifact the methodology names is the postmortem, so
  the path names the artifact, not the event.
- **Fold it into the ADR stream** (an incident is just a
  decision-shaped record) — rejected: most incidents don't change a
  decision, and stretching ADRs to cover narratives dilutes both
  forms.

## Consequences

- The mandate in §8 becomes followable: there is a place to put the
  thing it requires, and a template that ends by asking for the
  follow-through — making the §8 rule harder to skip than to satisfy.
- Pre-mortem and postmortem are now symmetric: assumptions probed
  before the bet, causes recorded after the incident.
- One more template to maintain; accepted, it is a page.
- Risk of postmortem theater (filling the form, skipping the
  follow-through). Mitigated by the template's structure: the
  follow-through table *is* the document's point, and review checks
  artifacts ride along (ADR 0015).

## Adoption impact

**Reference-only.** Nothing to change today and nothing to backfill
(forward-only, `adopting.md`): the first user-visible incident after
this version creates `docs/postmortems/` from the template.

## References

- `methodology.md` §8 (operational feedback loops), artifact map.
- ADR 0010 (planning sibling — introduced the pre-mortem this
  mirrors), ADR 0012 (forward-only adoption), ADR 0015 (review checks
  artifacts ride along).
- `templates/postmortem.md`, `templates/planning/premortem.md`.
