# ADR 0026: The shared Claude PR reviewer runs on the Agent SDK

- **Status:** Proposed
- **Date:** 2026-11-09
- **Deciders:** vpc
- **Supersedes (in part):** ADR 0021 — its choice of
  `anthropics/claude-code-action` as the runner. Its sharing model,
  advisory status, and review criteria stand.

## Context

ADR 0021 hosts a reusable, methodology-aware PR reviewer here and runs
it on `anthropics/claude-code-action@v1`. It also says *the policy is
the durable artifact; the Action is disposable orchestration*. This ADR
uses that clause.

The Console bills the action as **Claude Code**. The Max plan's monthly
$100 promotional API credit covers the Agent SDK and the API, not Claude
Code, so reviews spend purchased credit while the promotional credit
expires unused, and reviews stop when purchased credit runs out.

Evidence from nurturepa/cif (its ADR 0016, spec
`claude-review-agent-sdk`, PR #140, 2026-11-09): the same review driven
by the Claude Agent SDK drew down the promotional credit and left
purchased credit untouched, at about $1 a review. cif's port also made
the reviewer stricter than the action: read-only tools checked at
runtime, no GitHub token in the agent's reach, and every failure a red
check.

## Decision

Run the shared reviewer through the Claude Agent SDK, from a script and
tests in this repo, as specified in `specs/claude-review-agent-sdk/`.
The reusable workflow keeps its path and its `workflow_call` contract
(caller-supplied key, pinned default model), except that `claude_args`
— CLI passthrough specific to the action — is replaced by explicit
`max_turns` / `max_budget_usd` inputs. `claude-agent-sdk` is pinned
exactly (ADR 0003); it bundles the Claude Code CLI, so the pin covers
both.

## Alternatives considered

- **Keep the action.** No code to own, but every review keeps spending
  purchased credit. Rejected.
- **Call the Messages API directly.** Certainly covered by the credit,
  no agent runtime — but the reviewer loses agentic reading of the
  repo (ADRs, specs a PR touches), which is the point of a
  methodology-aware review. Kept as the fallback if Agent SDK billing
  changes.
- **Each project carries its own copy of cif's script.** Rejected for
  the reason ADR 0021 gives: drift.

## Consequences

- Reviews are paid from the promotional credit when the caller's key
  belongs to the org that receives it; otherwise billing is as before.
  It depends on how Anthropic classifies Agent SDK traffic; a change
  there moves reviews back to purchased credit silently. Check the
  Billing page, not the usage analytics.
- This repo now owns a review script, its tests, and its first CI
  workflow. A broken `main` breaks every caller pinned to `@main`;
  the tests running here on every PR are the guard.
- Adoption gets simpler: no Claude GitHub App, no `id-token: write`.
  Comments post as `github-actions[bot]`.
- The action's skip-as-green failure mode, and the workaround step for
  it, go away.

## Adoption impact

Callers on `@main` change behavior on merge, with no edit needed;
callers that pass `claude_args` must switch to the new inputs (none do
today). The template drops two prerequisites. cif is unaffected: it is
cross-account and keeps its own copy.

## References

- ADR 0021 (shared reviewer), ADR 0003 (dependencies), ADR 0024
  (compact spec).
- `specs/claude-review-agent-sdk/spec.md`.
- nurturepa/cif: ADR 0016, `specs/claude-review-agent-sdk/`,
  `scripts/ci/claude-review.py`.
