# ADR 0008: AI-agent drift guardrails

- **Status:** Accepted
- **Date:** 2026-06-06
- **Deciders:** vpc

## Context

The methodology treats an AI agent as a first-class contributor and
already states the basics — read before you write, produce artifacts
not just code, the human is author of record (ADR 0005). It does not,
however, name the drift dynamics that are **specific to agents** and
differ in kind from human drift:

- **Asymmetric, confident desync.** An agent will rewrite an
  `Approved` spec post-hoc so it matches code the agent just wrote —
  making the artifacts agree by *corrupting the contract* rather than
  by meeting it. The diff looks internally consistent and sails
  through review while the drift is hidden, not recorded.
- **Asserted completion.** An agent declares a criterion "done" when
  no test covers it. (ADR 0006 hardens the mechanism; a stated norm is
  still needed.)
- **Stale-context action.** An agent acts on a summarized or
  remembered view of a spec/ADR it did not actually re-read this
  turn — a real failure mode given context-window summarization.

These are precisely the failures that erode "the spec is the
contract," and they are the ones least likely to be caught by a
human skimming an internally-consistent diff.

## Decision

Add a short **"AI-agent guardrails"** subsection under the existing
agent operating rules in `methodology.md` ("Using this methodology"):

- **Do not silently alter an agreed contract.** An agent may not
  change an `Approved` or `Implemented` spec's requirements or success
  criteria as a side effect of implementing against them. Changing the
  contract is itself a spec change: proposed as its own diff with a
  rationale and left for human sign-off, never folded into an
  implementation PR as though it had always read that way.
- **Show "done," do not assert it.** An agent claiming a criterion is
  met cites the passing test that proves it (ADR 0006). Completion that
  cannot be pointed at is reported as unproven, not as done.
- **Re-read before you write.** Before editing a spec, ADR, or
  glossary, re-read the current file rather than a remembered or
  summarized version. Recalled or summarized context is treated as a
  possibly-stale pointer to verify, not as ground truth.
- **Surface drift, do not paper over it.** An agent that notices
  code/spec/glossary divergence while doing unrelated work flags it (an
  issue, a note, or the §8 loop) rather than quietly editing the doc to
  match the code.

Mirror the contract-protection and "show, don't assert" points into
`templates/project-CONTRIBUTING.md`'s "Using AI assistants" section.

## Alternatives considered

- **Rely on the existing "read before you write" + "human is author of
  record"** — rejected: necessary but insufficient. Neither names the
  agent-specific failure of *rewriting the contract to match the
  work*, which is the subtle one and the one most likely to pass
  review.
- **Lock specs to be technically uneditable by agents (tooling)** —
  rejected: mechanism over principle. The rule is "don't change the
  contract silently," enforced by review and commit conventions, not
  file permissions. A project may add such tooling via its own ADR.

## Consequences

- The spec keeps its force as a contract even when one agent both
  implements against it and edits the repository around it.
- Slightly more friction when a spec genuinely must change
  mid-implementation — by design: that becomes a surfaced human
  decision rather than a buried one.
- Pairs with ADR 0006 (provable "done") and ADR 0007 (frozen specs):
  together they make agent contributions auditable and make drift
  loud rather than silent.

## References

- `methodology.md` "Using this methodology" (agent operating rules),
  §2, §8; `templates/project-CONTRIBUTING.md` ("Using AI assistants").
- ADR 0005 (author of record; read before write), ADR 0006, ADR 0007.
