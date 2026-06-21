# ADR 0023: One-command onboarding added to §10

- **Status:** Proposed
- **Date:** 2026-06-21
- **Deciders:** vpc

## Context

§10 (Dependencies are decisions) was established by ADR 0003 as exactly
three bullets: adding-is-a-decision, lockfiles-committed, updates-deliberate.
Version 0.12.0 (PR #25) added a **fourth, normative** bullet —
"one-command onboarding; 'works on my machine' is a defect" — but shipped it
**without an ADR**, asserting scale-to-work.

A PR review flagged the governance gap, and it is real. The methodology's own
rules require it:

- *"If a practice changes, update the relevant document and record the change
  in an ADR."* ("Changing this document")
- *"If you find yourself arguing for or against a practice that isn't listed
  here, that is a sign you need an ADR, not a longer methodology doc."*

PR #25's body was precisely an argument for a practice (it cited the withdrawn
#22/#24 exchange). And the precedent is consistent: comparably-scoped additions
in this repo got ADRs — ADR 0014 (a decision-guide row), ADR 0016 (a
postmortem home). Without this record, §10 carried a normative bullet no ADR
traced to — the doc/decision drift §1 exists to prevent. ADR 0003 is
append-only, so the new bullet is recorded **here**, not by editing it.

## Decision

Record the §10 **one-command onboarding** bullet as an accepted extension of
ADR 0003's Dependencies practice:

> A substantial project bootstraps from a clone to a working environment with
> a single documented, reproducible command; "works on my machine" is a defect
> in the onboarding path. The tool (`make setup` / devcontainer / Nix flake) is
> the project's choice — **no tooling mandate**, consistent with ADR 0003's
> "weigh and record, not a particular tool."

§10's decision trail is now **ADR 0003 + this ADR** together. The bullet is the
one survivor of the withdrawn #22/#24 expansion exchange, kept at sub-bullet
scale rather than as a new numbered practice.

## Alternatives considered

- **Leave the bullet unrecorded** (rely on scale-to-work alone) — rejected: a
  normative §10 bullet with no ADR is the exact drift §1 prevents, and the
  precedent (0014/0016) records comparable additions.
- **Revert the bullet** — rejected: the developer entry point is the one thing
  §6/§10's reproducible-build guidance genuinely left unsaid, and the owner
  chose to keep it.
- **Edit ADR 0003's Decision list to add the bullet** (the reviewer's
  alternative) — rejected: ADRs are append-only; you supersede or record
  anew, never edit.

## Consequences

- §10 is traceable to its decisions again.
- A small, deliberate precedent: a normative sub-bullet that extends a practice
  gets a short ADR — honoring the "arguing for a practice → ADR" rule without a
  whole new practice.
- Cheap to reverse: revert the bullet and supersede this ADR.

## Adoption impact

**Reference-only.** The bullet already shipped in 0.12.0; this ADR records the
decision behind it. Nothing for consuming projects to do.

## References

- ADR 0003 (`adr/0003-dependencies-are-decisions.md`) — the §10 practice this
  extends; `methodology.md` §10, §1, "Changing this document."
- ADR 0014, ADR 0016 — precedent: comparably-scoped additions recorded by ADR.
- PR #25 (the bullet) and its review (the flagged governance gap).

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
