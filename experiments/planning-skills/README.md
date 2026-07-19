# Experiment: planning skills

> **Status: TRIAL — not a ratified practice.** Like
> `../adversarial-review/`, this directory is a trial with no adoption
> obligation. If it earns its keep across 2–3 real bets it graduates to
> an ADR (and likely `templates/`); if not, it is deleted. The trigger
> and evaluation questions are in the bet:
> `agent-framework/planning/planning-orchestration/bet.md`.

Claude Code skills that drive the planning practices in `planning.md` —
one command per practice, each reading and writing **only** the
canonical `planning/<slug>/` artifacts (plus the drafted
`specs/<slug>/spec.md` at handoff). They are optional planning tools in
exactly the sense `planning.md` allows: disposable editors over the
durable artifacts. Retire them and you lose an editor, not the decision
trail.

| Skill | Practice (planning.md) | Writes |
|---|---|---|
| `plan-brief` | §1 Frame the problem | `planning/<slug>/brief.md` |
| `plan-prfaq` | §2 Work backwards | `planning/<slug>/pr-faq.md` |
| `plan-options` | §3 Diverge before converging | `planning/<slug>/options.md` |
| `plan-bet` | §4 Price the work | `planning/<slug>/bet.md` |
| `plan-premortem` | §5 Test riskiest assumptions | `planning/<slug>/premortem.md` |
| `plan-handoff` | Scope — converge to a spec | `specs/<slug>/spec.md` (draft) |

## Install (personal, all projects)

Symlink so the repo stays the single source of truth (methodology ADR
0022 — no hand-synced copies):

```sh
mkdir -p ~/.claude/skills
for s in "$METHODOLOGY_HOME"/experiments/planning-skills/plan-*; do
  ln -sfn "$s" ~/.claude/skills/"$(basename "$s")"
done
```

Uninstall: delete the symlinks.

## Ground rules (all six skills)

- **The human is author of record.** Skills draft and pressure-test;
  the human accepts. The bet's appetite is never the agent's call.
- **Artifacts only.** A skill writes its one canonical artifact and
  nothing else. If a skill needs state, config, or code, that is a
  harness — stop and decide that deliberately (it's Option B of the bet
  this spike is testing).
- **Ceremony scaled to the work.** Every skill first asks whether the
  work is genuinely uncertain or expensive to commit; if not, it says
  "go straight to the spec (or the commit)" and stops.

## Trial log

Append one line per real use, so the graduation verdict has evidence
(mirrors `../adversarial-review/log.md`): date, project/slug, skills
used, and the two signals — were the artifacts produced (vs. skipped),
and did `plan-options`' divergers yield *genuinely different* options
rather than restatements?

| Date | Project / slug | Skills used | Artifacts produced? | Options genuinely diverse? | Notes |
|---|---|---|---|---|---|
| 2026-07-19 | kinshipbonds / kinshipbonds | plan-brief, plan-prfaq, plan-options (+ landscape spike) | Yes — brief, pr-faq, options, landscape scan in one day | Yes — 4 distinct identities (operator/broker/infrastructure/don't-incorporate); blind convergence on 4 tactical points read as signal; contrarian surfaced a novel risk (measurement-as-surveillance) | Skeptic pass corrected a false PR claim; no diverger proposed the founders' original AI-platform concept |
