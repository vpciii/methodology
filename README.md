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
| `methodology.md` | The canonical methodology (8 practices + the reasoning). |
| `templates/adr/_template.md` | Architecture Decision Record template. |
| `templates/spec/{spec,plan,tasks}.md` | Spec-first feature templates. |
| `templates/glossary.md` | Ubiquitous-language glossary seed. |
| `templates/twelve-factor.md` | Twelve-Factor status checklist (deployable services). |
| `templates/project-CLAUDE.md` | Drop-in `CLAUDE.md` for a new project (AI orientation pointer). |
| `templates/project-CONTRIBUTING.md` | Drop-in `CONTRIBUTING.md` (PR flow, commit labels, DoD, review scope). |
| `adr/NNNN-*.md` | Decisions about *this methodology itself*. |

## How it's wired in globally

`~/.claude/CLAUDE.md` (global Claude memory, loaded in every project)
contains the hard rules inline and points here for the full document.
So every Claude session — in any repo — already knows the methodology
and where to read the detail.

## Adopting it in a project

1. Copy `templates/project-CLAUDE.md` → `<project>/CLAUDE.md` and fill
   in the project-specific blanks.
2. Copy `templates/project-CONTRIBUTING.md` → `<project>/CONTRIBUTING.md`.
3. Create `<project>/docs/adr/`, `<project>/docs/glossary.md`, and
   (for deployable services) `<project>/docs/twelve-factor.md` from
   the templates here.
4. Use `templates/spec/` for the first feature: `specs/<slug>/`.

Projects reference this repo by path; they do not vendor a copy of
`methodology.md`. One source of truth, updated in one place.

## Changing the methodology

Edit `methodology.md` and record the change as an ADR in `adr/`. See
the "Changing this document" section of the methodology.
