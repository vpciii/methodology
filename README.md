# Methodology

The shared, tool-agnostic development methodology for all projects.
The canonical document is **[`methodology.md`](./methodology.md)** —
read that first.

This repo is the single source of truth for *how* work is done. It is
plain markdown + git on purpose: it must outlive any editor, AI tool,
or workflow framework. It is written to be followed by **humans and AI
agents alike** — see the "Using this methodology" section of
`methodology.md` for the reading order, the decision guide (which
artifact to produce when), and agent operating rules.

## `$METHODOLOGY_HOME`

Everything references this repo via `$METHODOLOGY_HOME` (default
`~/Developer/methodology`), so a clone at a different path still
resolves. It's set in `~/.claude/settings.json` (`env`) for Claude
sessions; add `export METHODOLOGY_HOME="$HOME/Developer/methodology"`
to your shell profile for terminal use.

## Layout

| Path | What |
|---|---|
| `methodology.md` | The canonical methodology (11 practices + the reasoning + a decision guide). |
| `CHANGELOG.md` | Human-facing record of changes to the methodology, under SemVer (ADR 0009). |
| `templates/adr/_template.md` | Architecture Decision Record template. |
| `templates/spec/{spec,plan,tasks}.md` | Spec-first feature templates. |
| `templates/glossary.md` | Ubiquitous-language glossary seed. |
| `templates/architecture.md` | Current-state architecture overview (kept-honest system shape). |
| `templates/twelve-factor.md` | Twelve-Factor status checklist (deployable services). |
| `templates/project-CLAUDE.md` | Drop-in `CLAUDE.md` for a new project (AI orientation pointer). |
| `templates/project-CONTRIBUTING.md` | Drop-in `CONTRIBUTING.md` (PR flow, commit labels, DoR/DoD, review scope). |
| `templates/methodology.mdc` | Cursor rule — paste into Cursor User Rules (global) or drop into a project's `.cursor/rules/`. |
| `adr/NNNN-*.md` | Decisions about *this methodology itself*. |

## How it's wired in globally

- **Claude:** `~/.claude/CLAUDE.md` (global memory, loaded in every
  project) contains the hard rules inline and points here for the full
  document, plus `$METHODOLOGY_HOME` is set in `~/.claude/settings.json`
  `env`. Every Claude session, in any repo, already knows the methodology.
- **Cursor:** paste `templates/methodology.mdc` into **Cursor →
  Settings → Rules → User Rules** for the global equivalent. (Cursor has
  no global rules *file*; User Rules is its only always-on mechanism.)
  For per-project, drop the same file into `<project>/.cursor/rules/`.

## Adopting it in a project

1. Copy `templates/project-CLAUDE.md` → `<project>/CLAUDE.md` and fill
   in the project-specific blanks.
2. Copy `templates/project-CONTRIBUTING.md` → `<project>/CONTRIBUTING.md`.
3. Create `<project>/docs/adr/`, `<project>/docs/glossary.md`,
   `<project>/docs/architecture.md`, and (for deployable services)
   `<project>/docs/twelve-factor.md` from the templates here.
4. Use `templates/spec/` for the first feature: `specs/<slug>/`.

Projects reference this repo by path; they do not vendor a copy of
`methodology.md`. One source of truth, updated in one place.

## Changing the methodology

Edit `methodology.md` and record the change as an ADR in `adr/` — each
ADR declares its **adoption impact** for consuming projects. Note the
change in [`CHANGELOG.md`](./CHANGELOG.md) under semantic versioning, so
projects adopt it deliberately like any dependency (ADR 0009). See the
"Changing this document" section of the methodology.
