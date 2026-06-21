# Adversarial Review: Methodology PR #24 (ADR 0023)

1. Self-Hypocrisy on §12 (Deterministic Onboarding)
* **Claim Refuted:** ADR 0023 asserts that "deterministic onboarding" (§12) is "the one idea from PR #22 with no existing home" and justifies keeping it while rejecting PR #22's other practices for duplicating existing rules.
* **Grounding:** `methodology.md` §6 (The Twelve-Factor App, specifically factors II on Explicit Dependencies and X on Dev/Prod Parity) and §10 (Dependencies are decisions / reproducible builds).
* **Defect:** If builds are reproducible (§10) and the environment is deterministically matched to production via explicit dependencies (§6), deterministic developer onboarding is inherently required and covered. By asserting that determinism only applies to the "running system", the author splits hairs to justify injecting its own pet practice while hypocritically citing "duplication" to block the original author's practices.

2. Mandate in Disguise
* **Claim Refuted:** ADR 0023 claims the new §12 is "tool-agnostic and judgment-scaled", differentiating it from PR #22 which it attacked for "mandating" practices.
* **Grounding:** `methodology.md` §12 commands: "A substantial project bootstraps locally with one documented, reproducible command", and further states: "\"Works on my machine\" is a defect. If the setup path fails... the onboarding is broken and is fixed like any other defect".
* **Defect:** The rhetorical dressing of "the mechanism is a project tooling choice" does not hide the explicit, non-negotiable directive that you *must* have a one-command setup. The author criticized PR #22 for non-negotiable framing, then wrote a textbook mandate thinly disguised as a principle.

3. The Refinement Duplicates ADR 0015
* **Claim Refuted:** ADR 0023 claims its addition to "Automate what is checkable" is merely a "sharpening of an existing rule, not a new practice", thereby avoiding the duplication trap.
* **Grounding:** `methodology.md` (Keep the artifacts honest) is modified to explicitly state: "review goes to behavior, intent, and the artifacts (ADR 0015)." However, ADR 0015 already formally establishes the review checklist and its scope.
* **Defect:** The author explicitly BLOCKed PR #22 by citing ADR 0022 (Single Source of Truth), stating that adding code-review substance to the core document "creates second homes for the same rules". The author immediately proceeded to create a second home for ADR 0015 inside the core doc by spelling out its contents.

4. Rejected CD Too Fast (Author Bias)
* **Claim Refuted:** ADR 0023 rejected Continuous Deployment (CD) because it "breaks on libraries, CLIs, and this docs repo" and lacks scoping.
* **Grounding:** `methodology.md` §6 (Twelve-Factor App) includes the exact scoping mechanism needed: "Applies to deployable services; skip for libraries, CLIs, and one-off scripts." The author's own review of PR #22 noted the missing scoping.
* **Defect:** If the author was engaging in good-faith refinement, it would have applied the §6 scoping clause to CD rather than discarding it wholesale. Instead, the author weaponized the lack of scoping to reject the competitor's idea entirely, demonstrating adversary-authored-replacement bias aimed at clearing the field for its own counter-proposal.

5. Incomplete Self-Consistency (Stale References)
* **Claim Refuted:** ADR 0023 boasts: "Keep the document self-consistent in the same PR (what PR #22 missed): update the `§1–§11` → `§1–§12` references... The document stays self-consistent... unlike PR #22."
* **Grounding:** A repository-wide search reveals over a dozen stale references to `§11` that were not updated to `§12` or audited. Examples include `CHANGELOG.md` line 74 ("irreversible by definition, §11"), `adr/0004-reversible-by-default.md` line 21, and multiple mentions in ADR 0014 and 0019.
* **Defect:** The author claimed the moral high ground on meticulous self-consistency while leaving behind a broken, desynced web of cross-references. This is the exact same "self-inconsistency" sin it punished PR #22 for.

6. Numbering Collision
* **Claim Refuted:** Implied process integrity and non-collision.
* **Grounding:** The PR introduces `adr/0023-incorporate-delivery-ideas-judgment-scaled.md` while PR #22 already holds `adr/0023-expand-practices-for-modern-delivery.md` and remains open.
* **Defect:** Reusing an ADR number while a competing PR is still actively holding that namespace causes version control collisions and confusion. The author should have used the next available integer (0024) for a counter-proposal.

***

### VERDICT: BLOCK

This PR must be blocked due to overwhelming adversary-authored-replacement bias and hypocrisy. The author rejected PR #22 for duplicating existing rules, creating mandates, and failing to maintain repo consistency—yet committed all three of those exact same sins in this counter-proposal. Specifically, §12 duplicates 12-factor/dependencies determinism, the text refinement creates a second home for ADR 0015, the CD rejection was needlessly dismissive given the existing §6 scoping mechanism, and the author blatantly failed the cross-repository consistency check they boasted about passing.
