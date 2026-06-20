# Adversarial Review: Methodology PR #21 (ADR 0023)

### 1. EXPAND-CONTRACT VIOLATION
* **Claim Refuted:** The ADR asserts under the `Migration` and `Consequences` sections that renaming `claude-review.yml` to `review-author.yml` is "a breaking change for callers until updated", casually labeling this as "Forward-only."
* **Grounding:** `adr/0004-reversible-by-default.md` (Lines 25-27) and `methodology.md` (§11) explicitly mandate: "Evolve schemas with expand-contract (parallel-change): add the new shape, migrate, then remove the old — never a destructive in-place change in a single irreversible step."
* **Defect:** A rename of a reusable workflow that cross-repo callers rely upon is a destructive, in-place change. Because the methodology repo and the caller repos are updated via separate PRs, this guarantees a window where the caller's CI is broken. Calling it "forward-only" does not excuse a direct violation of the methodology's own core rule for safe evolution. The workflow should be duplicated, migrated, and then the original deprecated.

### 2. BUILD-BEFORE-VALIDATE
* **Claim Refuted:** Under `Decision` (4), the ADR states the swappable binding is "what makes the methodology's model-agnosticism *real* rather than terminological." However, under `Consequences`, it concedes "The agnosticism is still only *enabled*, not yet *demonstrated*," noting every trial run was Claude-author / Gemini-adversary.
* **Defect:** The ADR commits to building out permanent, cross-repo CI infrastructure for model-agnosticism before validating the core premise. Taking the time to run a single manual, reversed-role or third-model test would validate the premise trivially. Engineering the infrastructure to *enable* a property before producing the evidence to *demonstrate* it is completely backward and risks overfitting to the two specific models tested.

### 3. REDUNDANT DOUBLE REVIEW
* **Claim Refuted:** Under `Decision` (2 & 3), the ADR establishes both an "Author-model binding" and an "Adversary-model binding," running two LLM reviews per PR. `Consequences` acknowledges this brings "more token cost and PR-comment noise."
* **Defect:** If the adversary model checks against the identical single-sourced policy and *also* possesses the capability to catch the same-model's structural blind spots, what unique value justifies keeping the author-model reviewer? The ADR justifies the author model simply as being "broad and cheap" and "shares the author's blind spots"—which is a weakness, not a feature. Keeping both models is unexamined ceremonial redundancy.

### 4. SUPERSESSION STILL INCOHERENT
* **Claim Refuted:** Under `Decision` (5), the ADR claims it will "Supersede ADR 0021 wholesale." In the very next sentence, it says, "Its mechanism (reusable workflow, advisory, pinned action, trigger/skip rules) is carried forward in role-based form — not a partial edit."
* **Defect:** In the round-5 review (`pr19_adversarial_review.md`), partial supersession was rejected as incoherent under the append-only rule. Claiming you are superseding a decision "wholesale" while explicitly carrying forward its exact mechanism is just "partial supersession" with a fresh coat of rhetorical paint. It attempts to dodge the structural incoherence by redefining the word "wholesale."

### 5. HAND-WAVED SINGLE-SOURCING
* **Claim Refuted:** Under `Decision` (1), the ADR claims the review policy is single-sourced (citing ADR 0022), asserting each binding receives it "by generation or a CI equality check." 
* **Hunch / Defect:** The ADR asserts a technical property without specifying the implementation, committing the same aspirational-claim sin punished in round 5. Furthermore, creating two separate reusable workflows (`review-author.yml` and `review-adversary.yml`) inevitably duplicates GitHub Actions boilerplate (e.g., `on: opened`, `ready_for_review`, `[skip-review]` triggers and skip rules). This introduces the exact flavor of hand-maintained verbatim duplication that `adr/0022-single-source-of-truth.md` (Lines 36-47) was written to forbid. 

***

### VERDICT: BLOCK
The deliberate Expand-Contract violation (breaking callers via a destructive in-place rename instead of parallel addition) directly contradicts the methodology's own explicit `Reversible by default` rule (ADR 0004 / §11). This alone mandates a BLOCK. Furthermore, the single-sourcing implementation is entirely hand-waved, redundant CI boilerplate is introduced, and the build-before-validate approach engineers a heavy CI solution to an untested premise.
