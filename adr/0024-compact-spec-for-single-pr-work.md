# ADR 0024: A compact spec for work that fits in one PR

- **Status:** Proposed
- **Date:** 2026-09-29
- **Deciders:** vpc

## Context

§2 (Spec-first development) has said since the first version: *"One
folder per feature, three files: `spec.md` (what + why), `plan.md`
(how), `tasks.md` (PR-sized work items)"*, with sign-off between the
stages.

Real use after v0.12.0 has diverged from that, consistently and in both
adopting projects:

- **nurturepa/cif** (brownfield adoption 2026-07-13, ADR 0004 there;
  ~64 PRs since June): **8 of its 9 specs are `spec.md` alone.** The one
  with all three files (`messages-report-conversation-filter`) spanned
  several PRs. The single-file specs are not thin — 170–200 lines, with
  full requirements, success criteria, and traceability — and several
  record their *how* inline in a dated `## Decisions` section.
- **agent-framework**: 2 of 6 specs skip `plan.md`. `verdict-rendering`
  writes it down explicitly: *"Plan: — (single-function slice; the
  spec's Requirements are the plan)"*, with a one-task `tasks.md`.
  Where all three files were written, each stage was its own PR plus an
  "approve (human sign-off)" commit — 32 of ~70 non-merge commits are
  `docs:` against 19 `feat:`.

So the three-file rule is not being followed for small features, and
the rule gives no guidance for when that's legitimate. That is drift
between the document and practice, which the methodology says to
surface, not paper over (ADR 0008). And the ad-hoc version has a real
gap: §11 puts a risky change's undo in "`plan.md` Rollout" — with no
`plan.md`, nothing says where the undo goes.

The value of `plan.md` and `tasks.md` is real where there is something
to sequence: several PRs, a dependency order, parallelisable tasks. For
work that is one PR, `tasks.md` is a single line and `plan.md` repeats
what the spec and the PR already say, each adding a sign-off round-trip.

## Decision

We will allow a **compact spec**: when the whole feature fits in **one
PR** (the §4 ~300-line guide), `spec.md` alone is enough. It carries two
optional sections the template gains:

- **`## Approach`** — the *how*, at plan altitude (what `plan.md` would
  have said), including any design decisions made along the way.
- **`## Rollout and undo`** — required whenever §11 would have required
  a `plan.md` Rollout: the flag, migration shape, or documented undo.

Sign-off still precedes code: the spec, *including* its Approach, is
agreed before implementation — one stage instead of three. If the work
turns out to need more than one PR, add `plan.md` and `tasks.md` then;
the compact spec is the start of the full one, not a different kind.

A **sign-off** is a recorded human approval — a PR review, or an
approval commit on the spec's branch. The methodology does not require a
separate PR per stage, for compact or full specs.

Everything else is unchanged: success-criterion ids, traceability, the
coverage check, the freeze at `Implemented`.

## Alternatives considered

- **Keep the rule and enforce it** — rejected: both adopting projects
  already work around it for small features, and the extra files would
  mostly restate the spec. Enforcing it trades real throughput for
  artifacts that exist to satisfy a folder structure — which the
  methodology's own "practice vs. ceremony" note warns against.
- **Leave it to "scale the ceremony to the work"** — rejected: that note
  is about *whether* to write a spec at all, and practice shows people
  reading it inconsistently (one project writes a one-line `tasks.md`,
  the other none). It also leaves the §11 undo with no home.
- **Make `plan.md` / `tasks.md` optional in general, at the author's
  judgment** — rejected: for multi-PR work the plan and task DAG are
  where disagreement is cheapest to catch, and agent-framework's worker
  dispatch depends on `tasks.md`. A one-PR threshold is objective and
  already a methodology number.

## Consequences

- The document matches how specs are actually written; small features
  have one sign-off, not three.
- The §11 undo has a home in every spec shape.
- A compact spec that grows must be split into plan and tasks
  mid-flight — a small, deliberate cost, and the signal that the work
  was bigger than thought.
- Slightly more judgment at the start ("will this be one PR?"). A wrong
  guess is cheap to fix by adding the two files.
- Cheap to reverse: supersede this ADR and restore the three-file text.

## Adoption impact

**Reference-only.** Nothing is newly required: projects already writing
three files keep doing so, and existing single-file specs become
conforming. Projects that copied `templates/spec/spec.md` or
`templates/project-CONTRIBUTING.md` may pick up the new optional sections
and the reworded "How work flows" step when they next touch them.

## References

- `methodology.md` §2, §11, decision guide, artifact map;
  `templates/spec/spec.md`; `templates/project-CONTRIBUTING.md`;
  `templates/global-CLAUDE.md` (same-PR summary rule, ADR 0018).
- ADR 0007 (specs freeze — unchanged here), ADR 0008 (surface drift),
  ADR 0004 (reversible by default — the §11 undo).
- Evidence: nurturepa/cif `specs/` (8 of 9 single-file);
  agent-framework `specs/verdict-rendering/tasks.md`,
  `specs/regression-claims/`.

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
