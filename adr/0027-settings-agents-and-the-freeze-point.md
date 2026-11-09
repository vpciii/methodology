# ADR 0027: Out-of-repo settings, AI agents as actors, and when a spec freezes

- **Status:** Proposed
- **Date:** 2026-11-09
- **Deciders:** vpc
- **Supersedes (in part):** ADR 0007 — its freeze point (the status
  edit; now the merge of the PR that makes it) and, for settings
  outside the repository only, its rule that `docs/architecture.md`
  changes in the same PR as the structure it describes. The rest of
  ADR 0007 stands.

## Context

Porting the shared PR reviewer to the Agent SDK (ADR 0026, PRs #32–#34,
2026-11-09), after nurturepa/cif's own port the same day, exposed three
places where the methodology was silent. Each cost something that day.
They share one ADR because they share one body of evidence; each rule
stands or falls on its own.

**1. Facts that live in a host's settings have no home.** The
methodology keeps `docs/architecture.md` honest by tying it to the PR
that changes the structure. A change made in a settings page has no PR.

- This repository was made public. ADR 0021 and
  `templates/github/claude-review.yml` went on describing it as private,
  and told adopters in another account to keep a standalone copy of the
  reviewer — the drift ADR 0021 exists to prevent. The ADR 0026 spec
  repeated the stale claim as a constraint; two automated reviews caught
  it.
- The ADR 0026 reviewer *depends* on that visibility (callers check the
  script out with their own token). Nothing but that ADR records it.
- `main` gained a required status check on 2026-11-09. It changed how
  releases are made (0.13.0 was a direct commit; 0.14.0 had to be a PR).
  It is recorded nowhere in the repository.
- cif's review bill depends on which Anthropic org a repository secret
  belongs to (cif ADR 0016) — a fact visible only in two settings pages.

**2. §9 does not treat an AI agent as an actor.** The methodology makes
agents first-class *contributors*, but its security practice is written
for code and people.

- cif needed its own ADR 0006 to say no PHI goes into external AI calls.
- Both reviewer ports had to work out from scratch: read-only tools, a
  runtime check of the tool list, no GitHub token in the agent's reach,
  and pull-request content treated as material, not instructions.
- With all that in place, a review still found that the agent could be
  asked to read the process environment and print the API key into a
  public comment. The fix was a guard in the script and a regression
  test.

**3. The freeze point is ambiguous.** §2 says a spec freezes when its
status reaches `Implemented`. That status is set *inside* the
implementing PR, before the PR is reviewed.

- In PR #33 the spec read `Implemented` while its own review found a
  requirement that was literally untrue (R-4) and a non-goal resting on
  a false reason. Two reviews asked whether those could still be
  corrected; the text gave no answer. They were corrected in a separate
  commit with sign-off, which is the answer this ADR writes down.

## Decision

1. **Settings outside the repository are structure.** A project's
   `docs/architecture.md` lists the host and platform settings the
   system's shape or safety depends on — repository visibility, branch
   protection and required checks, which secrets exist and whose account
   they belong to, plan or billing arrangements the system relies on —
   and is updated when one changes. Because no PR carries the change,
   the update follows it promptly as its own small PR. Names and
   ownership only, never secret values (§9). A setting that is expensive
   to reverse or that other artifacts rely on is decided in an ADR like
   any other.

2. **An AI agent is an actor at a trust boundary (§9).** Where an agent
   runs with access to a system:
   - it gets **least privilege**: the tools, credentials and scope the
     task needs, no more;
   - **what it reads is data, not instructions**: content from outside
     the trust boundary (a pull request, a web page, a user's message)
     never widens what it may do;
   - **what it writes is an output channel**: text it publishes can
     carry out anything it could read, so secrets stay out of its reach
     or its output is checked;
   - **what is sent to a model provider crosses a trust boundary**:
     which data may go there is an ADR-worthy decision.

   These are §9's existing rules (least privilege, validate at the
   boundary, boundaries get ADRs) applied to a new kind of actor. How a
   project enforces them is its own tooling decision.

3. **A spec freezes when the PR that marks it `Implemented` merges.**
   Until then it is still editable under the rule that already governs
   an `Approved` spec: a correction to a requirement, criterion, or
   agreed Approach found during the implementing PR's review is its own
   commit, with rationale, signed off by the human — never folded into
   an implementation commit. After merge, nothing changes: a
   contradiction goes to a test, a new spec, or an ADR.

## Alternatives considered

- **Leave settings to memory and ADRs.** ADRs record the decision, not
  the current state; ADR 0021 was correct when written and wrong a few
  months later with no edit possible (ADRs are append-only). Current
  state is `architecture.md`'s job. Rejected.
- **Machine-check settings in CI** (query the host's API, compare with a
  committed file). The strongest form of "automate what is checkable",
  but it needs a token with admin read scope in CI and is host-specific.
  Left as a project tooling option; the rule is the list.
- **A separate `docs/settings.md`.** One more artifact for a short list
  that is structural by nature. Rejected in favor of a section in the
  existing overview.
- **A full AI-security practice** (threat-model template, mandatory
  sandboxing, red-team checklist). No adopter evidence for more than the
  four points, and it would name tooling the methodology deliberately
  leaves to projects. Rejected.
- **Leave agent safety to each project's ADRs.** That is what happened:
  two repositories derived the same rules independently on the same
  day, and one hole survived both. Rejected.
- **Freeze at the status edit, as written.** Forces a known-wrong
  sentence into the permanent record, or a new spec to fix a typo-grade
  error found an hour later in the same PR. Rejected.
- **Set `Implemented` in a follow-up PR after merge.** Removes the
  ambiguity, but leaves `main` with a shipped feature whose spec says
  `Approved` and whose coverage is not yet enforced. Rejected.

## Consequences

- A stale claim about visibility, protection, or whose key pays has one
  place to be wrong, and a reviewer (human or agent) has something to
  compare a PR's assumptions against.
- The settings list can itself go stale: nothing forces the follow-up
  PR. It is a habit plus a review prompt, not a guarantee.
- Listing which secrets exist and whose account they belong to tells a
  reader of a public repository a little about its operations. Projects
  for which that matters keep the list coarse.
- Projects that run agents get four questions to answer instead of
  discovering them one incident at a time. The rules are stated at the
  level of the durable artifact (a boundary in an ADR, a regression
  test), so they should outlive today's agent tooling.
- §9 grows by one bullet; the "small set of practices" stays eleven.
- The freeze rule now depends on merge state, which is not visible in
  the file. A reader of a branch cannot tell from the spec alone whether
  it is frozen; the status plus `git` can.
- Cheap to reverse: supersede this ADR; no data or tooling depends on
  it.

## Adoption impact

*Per-project action, small and forward-only:*

- Add a **Settings outside the repository** section to
  `docs/architecture.md` (template updated) the next time the file is
  touched, or when such a setting next changes.
- A project that runs an AI agent against its systems records where the
  agent sits relative to its trust boundaries (in the Trust boundaries
  section, tracing to an ADR) when it next changes that agent.

The freeze-point clarification is *reference-only*. The global summary
(`templates/global-CLAUDE.md`) changes in this PR; copying it to
`~/.claude/CLAUDE.md` is the per-machine release step (ADR 0018).

## References

- ADR 0026 and `specs/claude-review-agent-sdk/spec.md` (Decisions
  entries of 2026-11-09); PRs #32, #33, #34 and their review comments.
- ADR 0021 (written while this repository was private); ADR 0007 (specs
  freeze; `architecture.md`); ADR 0008 (agent guardrails).
- nurturepa/cif: ADR 0006 (no PHI in external AI/API calls), ADR 0016
  (review paid from a personal plan's credit).
