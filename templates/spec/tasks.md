# Tasks: <Feature name>

- **Status:** Draft | Approved | In progress | Done
- **Spec:** ./spec.md
- **Plan:** ./plan.md

Each task below is one pull request. Keep each PR under ~300 lines of
diff where reasonable. If a task grows beyond that, split it.

Mark tasks as you go: `[ ]` → `[~]` (in progress) → `[x]` (done, PR
merged). Link the PR number when merged.

---

## Task 1 — <Imperative verb phrase>

- **Depends on:** —
- **PR:** —

**What:** One sentence describing the change.

**Acceptance criteria:**
- [ ] …
- [ ] …
- [ ] Tests added (unit / integration / e2e as appropriate)
- [ ] Glossary terms used consistently
- [ ] Spec/plan updated if scope changed

---

## Task 2 — <Imperative verb phrase>

- **Depends on:** Task 1
- **PR:** —

**What:** …

**Acceptance criteria:**
- [ ] …

---

<!--
Add more tasks as needed. Suggested ordering:

1. Data model / schema first.
2. Core domain logic with tests.
3. API or interface layer.
4. UI / client.
5. Observability (logs, metrics).
6. Docs (README, ADRs, glossary updates).
-->
