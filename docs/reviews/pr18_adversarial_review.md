# Adversarial Review: PR #18 (ADR 0022)

- **Date:** 2026-06-20
- **PR:** #18 (Single Source of Truth)
- **Adversary Model:** Gemini 3.5 Flash (Medium) / Antigravity
- **Target Files:**
  - `adr/0022-single-source-of-truth.md`
  - `methodology.md`
- **Verdict:** BLOCK

---

## Findings

### 1. Self-Consistency Violation (High Severity)
The proposed rule states:
> "If it must exist in more than one — a generated artifact, a mirrored summary, a copy some tool requires — the copy is **generated from** the source or **machine-checked against** it, **never kept in sync by human memory**..." (adr/0022-single-source-of-truth.md)

However, the methodology repository's own mirrors—`templates/global-CLAUDE.md` and `templates/methodology.mdc`—are hand-maintained duplicates of `methodology.md`. They are **not** generated and **not** machine-checked in CI. 

According to ADR 0018:
> "It is edited **in the same PR** as any change it summarizes — the same-PR honesty rule now reaches it." (adr/0018-global-summary-is-a-repo-artifact.md)

This manual same-PR editing is exactly "keeping in sync by memory and review diligence." Therefore, the new rule in ADR 0022 immediately outlaws the repo's own flagship practice. The repository is in immediate violation of its own honesty rules upon merging this PR.

### 2. Steelmaning the Rejected Alternative: Deletion vs. Usability
ADR 0022 prioritizes removing duplicates as the "cheapest correct response" (adr/0022-single-source-of-truth.md). 

However, in documentation, "convenience copies" (repeating a command, structure, or definition) are crucial for reader usability and self-contained flow. Stripping helpful context to avoid setting up a generator or check violates the core principle of "dual-audience navigability" (ADR 0005). The ADR dismisses file inclusion/generation too quickly in favor of deletion.

### 3. Over-reach and Catch-22 Ceremony
The rule classifies all hand-maintained duplication as an "honesty violation" (adr/0022-single-source-of-truth.md). 

This clashes with the methodology's rejection of premature tooling commitments (ADR 0020) and anti-ceremony stance:
- ADR 0018 rejected generating summaries because "build tooling for one markdown file is ceremony."
- Under ADR 0022, authors must either accept the tooling ceremony of custom CI checkers for simple convenience copies, or strip readability from the docs, or commit an honesty violation.

### 4. Reverse-Engineering from a Single Incident
The rule was written to retro-justify the `opn-mcp` prompt duplication fix (PR #13 / PR #14). While prompt drift is a bug, generalizing a project-specific incident into a global constraint for all projects adopting the methodology is premature and over-reaching.

### 5. Hidden Coupling with Instantiation
Consuming projects copy and customize rules templates (`CLAUDE.md`, `CONTRIBUTING.md`). These copies are updated manually when the dependency is upgraded. Under ADR 0022, this manual synchronization makes all adopting projects immediately non-compliant unless they build custom dependency-upgrade validators.

---

## Required Changes to Resolve BLOCK

1. **Resolve the `global-CLAUDE.md` / `methodology.mdc` Contradiction:**
   - Provide a generator or CI check to verify these summaries automatically, OR
   - Update ADR 0022 to explicitly allow same-PR manual synchronization for curated abridgments.
2. **Soften the Deletion Bias:** acknowledge that convenience copies are valid for readability, and same-PR sync is an acceptable tier of compliance when the cost of automation is disproportionate.
3. **Clarify the Instantiation Boundary:** explicitly exempt or define compliance rules for instantiated templates (like `CLAUDE.md` and `CONTRIBUTING.md`) in consuming projects.
