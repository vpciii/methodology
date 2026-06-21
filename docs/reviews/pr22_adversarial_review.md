# Adversarial Review: Methodology PR #22 (ADR 0023)

> Reversed-role run: Gemini / Antigravity authored; Claude (Opus 4.8) adversary. Reviewed cold against the existing methodology (§1–§11, the "What is intentionally not here" section, and ADRs 0014/0018/0020/0022).

### 1. "Non-negotiable standards" contradicts the methodology's foundational scale-to-work philosophy

* **Claim Refuted:** ADR 0023 Context — making these "explicit numbered practices ensures they are treated as **non-negotiable standards** rather than optional enhancements," and §12–§14 state them as universal "must."
* **Grounding:** `methodology.md` → "A note on practice vs. ceremony": "**Scale the ceremony to the work.** A one-off script, a throwaway experiment, or a five-minute fix does not need a spec and an ADR… Apply judgment." The entire document is framed around judgment, not non-negotiable mandates.
* **Defect:** The change inverts the methodology's core stance. Mandating DevContainers, CD pipelines, and CI style-gates as non-negotiable for *every* project directly contradicts "apply judgment / scale the ceremony." A throwaway script or a single-file library now nominally "must" have a deployment pipeline and a DevContainer to "fully comply" (ADR Adoption impact). This is the ceremony-for-its-own-sake the methodology explicitly warns against.

### 2. Naming specific tools and mandating CI/CD violates "No premature tech-stack or tooling commitments"

* **Claim Refuted:** §13 "Use tools like Prettier, Black, or GoFmt"; §14 "Merging to `main` triggers a pipeline that deploys to production"; ADR Adoption impact requiring "automated deployment pipelines."
* **Grounding:** `methodology.md` → "What is intentionally not here": "**No premature tech-stack or tooling commitments.** Each tooling choice — stack, security scanner, flag system, **CI provider** — gets an ADR in the project that makes it, when it is made, not before." And the preamble: "**document the artifact, not the tool.**"
* **Defect:** The existing 11 practices never mandate a tool — they name tools only as illustrative "today" instances with the durable principle separated out. These new practices bake tool categories and a CI/CD provider commitment into the *global* methodology, the exact coupling the document exists to prevent. The PR never reconciles §12–§14 with the standing "intentionally not here" section, leaving a direct internal contradiction.

### 3. §14 Continuous Deployment has no deployable-service scoping and breaks for most project types

* **Claim Refuted:** §14 — "`main` must not only be shippable, it should be deployed automatically… Merging to `main` triggers a pipeline that deploys to production," stated universally.
* **Grounding:** `methodology.md` §6 (Twelve-Factor) is explicitly scoped: "Applies to deployable services; **skip for libraries, CLIs, and one-off scripts.**" §8 keeps operational machinery "deliberately lightweight," and "What is intentionally not here" excludes "formal SRE / ITIL machinery."
* **Defect:** A large class of projects the methodology covers — libraries, CLIs, one-off tools, and *this very methodology repo* (a markdown/docs repo) — have nothing to "deploy to production." §14 provides no scoping clause analogous to §6's, so as written it is inapplicable-to-incoherent for those projects, and it imports precisely the heavyweight delivery machinery §8 / the exclusions deliberately keep out.

### 4. §15 Continuous Refactoring duplicates ADR 0014 and the decision guide — a single-source-of-truth violation

* **Claim Refuted:** §15 introduces "Continuous Refactoring / the Boy Scout Rule" as a new numbered practice.
* **Grounding:** Refactoring is *already* a first-class concept: the decision-guide row "Restructure code without changing behavior (refactor, tech-debt paydown) → no spec; keep the suite green; an ADR only if it closes off future options" (ADR 0014), resting on §5 and §11. And ADR 0022 (just adopted): "a fact lives in one place."
* **Defect:** §15 creates a *second* home for the refactoring rule without referencing ADR 0014 or the decision-guide row, and partially restates §5's "protected by tests." This is the hand-maintained duplication ADR 0022 was written to forbid — introduced one ADR later, against the methodology's freshest rule.

### 5. §17 Documentation as Code duplicates "Keep the artifacts honest" and ADR 0020

* **Claim Refuted:** §17 — docs "live in the repository," go through "the same review process," and "a feature is not complete until its documentation is updated."
* **Grounding:** `methodology.md` → "Keep the artifacts honest": "**Docs change in the same PR as the behavior they describe**… User-facing documentation is bound the same way… (ADR 0020)." The artifact map already places docs in-repo.
* **Defect:** §17 is near-verbatim the existing same-PR docs rule plus ADR 0020, again with no cross-reference — a third instance of the ADR-0022 duplication hazard. It adds a numbered practice where a one-line pointer to the existing rule would do, inflating the document it claims to be improving.

### 6. §16 Code Review Culture imports framework-flavored team-process vocabulary the methodology excludes

* **Claim Refuted:** §16 — "async-first," "PR bottlenecks," "high team velocity and **psychological safety**," "Approve with suggestions — Do not block."
* **Grounding:** `methodology.md` → "What is intentionally not here": "**No agent personas or role-playing workflows.** They are framework-flavored." The document centers the **author-of-record** model ("AI assistants may draft; the human accepts") and is written for solo human + AI as much as teams. Review substance is already specified by ADR 0015 (spec conformance, test honesty, artifacts ride along).
* **Defect:** §16 grafts team-culture framing (velocity, psychological safety, async-first) onto a methodology that deliberately avoids framework-flavored process and often describes a single author of record — for whom "PR bottlenecks / team velocity" is inapplicable. "Approve with suggestions, don't block on trivia" also sits in unacknowledged tension with the substantive merge gate of ADR 0015; the practice neither cites nor reconciles it.

### 7. The PR leaves the document internally inconsistent — stale self-references and un-synced summaries

* **Claim Refuted:** Implicit claim that the expansion is complete and consistent (the PR changes only `methodology.md`, the ADR, and `CHANGELOG.md`).
* **Grounding:** After adding §12–§17, `methodology.md:59` still reads "the practices (**§1–§11**)" and `README.md:26` still reads "**11 practices**" — neither updated (README is not even in the changed-file set). Per ADR 0018, `templates/global-CLAUDE.md` and `templates/methodology.mdc` "change in the **same PR** as any change [they summarize]" — neither was touched. And "Keep the artifacts honest" forbids leaving a doc its own change makes wrong.
* **Defect:** The PR violates the methodology's own honesty rule *in the act of expanding the methodology*: it ships stale "11 practices / §1–§11" references and skips the same-PR summary sync ADR 0018 mandates. The expansion is not self-consistent.

### 8. ADR marked "Accepted" on an unmerged PR, with a model listed as a decider

* **Claim Refuted:** ADR header — "**Status:** Accepted" and "**Deciders:** vpciii, Antigravity," while PR #22 is open and unmerged.
* **Grounding:** `methodology.md` → "Author of record": "AI assistants may draft; **the human accepts.**" An accepted ADR is the output of human sign-off, recorded on merge — not a default the draft asserts about itself.
* **Defect:** A draft ADR pre-declaring its own status "Accepted" (and crediting a model as co-decider) inverts the author-of-record rule. The status should be `Proposed` until the human accepts; otherwise the append-only ADR log records an acceptance that never independently happened.

***

### VERDICT: BLOCK

The six practices encode genuinely good ideas (deterministic environments, automated gates, continuous refactoring, docs-as-code) — but as written they **misfit this methodology** at a structural level, and that is what a BLOCK is for. Three of them (§15, §17, and parts of §16) **duplicate existing practices and ADRs** (0014, 0020, the decision guide), violating the single-source-of-truth rule (ADR 0022) the project adopted one ADR earlier. Two of them (§13, §14) **directly contradict the standing "No premature tech-stack or tooling commitments" and lightweight-operations exclusions**, and §14 lacks the deployable-service scoping that would keep it from breaking on libraries, CLIs, and this very docs repo. The whole set is framed as "non-negotiable," inverting the methodology's foundational *scale-the-ceremony / apply-judgment* stance. Finally, the PR leaves the document **internally inconsistent** (stale "11 practices / §1–§11" references, un-synced ADR-0018 summaries) and the ADR pre-declares its own "Accepted" status against the author-of-record rule.

**To resolve:** fold the non-duplicative, genuinely-new ideas (deterministic environments; automated style gates) into existing practices as *judgment-scaled, tool-agnostic* guidance rather than tool-named universal mandates; drop or down-convert §15/§17 to pointers to ADR 0014 / 0020; reconcile §16 with ADR 0015 and shed the team-velocity framing; add deployable-service scoping to any CD guidance; update the §1–§n self-references and the ADR-0018 summaries in the same PR; and set the ADR to `Proposed`. Equally valid is **Option B from the ADR (status quo)** — the methodology already covers most of this implicitly, and "apply judgment" was a feature, not a gap.
