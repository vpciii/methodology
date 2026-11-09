# Contributing to the methodology repo

How changes to *this* repository are made. For the practices themselves,
read [`methodology.md`](./methodology.md); for a project's own
contributor guide, start from
[`templates/project-CONTRIBUTING.md`](./templates/project-CONTRIBUTING.md).

The human (vpc) is the author of record. AI assistants may draft; the
human accepts.

This file covers only what is specific to this repo. Commit type labels
and how to choose between them, the definitions of ready and done, and
what a review covers and checks are those of
`templates/project-CONTRIBUTING.md`, applied here unchanged.

## Every change goes through a pull request

`main` requires the `checks` status and applies that to admins, so a
direct push is rejected (the current settings are in the README's
*Settings outside the repository* table). Branch from `main`, push, and
open a PR, even for a one-line fix or a release.

Branch names follow the commit type: `docs/<slug>`, `fix/<slug>`,
`ci/<slug>`, `chore/<slug>`. Commits follow
[Conventional Commits](https://www.conventionalcommits.org/).

Two workflows run on a PR:

- **`CI`** (required): the shared reviewer's tests, the ADR checks
  (`.github/checks/`), and spec coverage. Run them locally, from the
  repo root, with:

  ```
  python3 .github/claude-review/test_claude_review.py
  python3 .github/checks/test_check_adrs.py
  python3 .github/checks/check_adrs.py
  python3 templates/ci/check-spec-coverage.py
  ```

- **`Claude review`** (advisory): one review comment when the PR is
  opened or marked ready (ADR 0021, ADR 0026). It costs about a dollar a
  run. Put `[skip-review]` in the PR title for a change with nothing to
  review, such as a release. It does not re-run on later pushes; to run
  it again, convert the PR to draft and mark it ready. Triage its
  findings in a PR comment (must fix / record / decline); a review is
  finished when the must-fix ones are closed, and one re-review is the
  default (ADR 0028).

## Changing a practice

A change to `methodology.md`, `planning.md`, or `adopting.md` is
recorded as an ADR in `adr/` (see "Changing this document" in the
methodology). In one PR:

1. Add `adr/NNNN-<slug>.md` from `templates/adr/_template.md`, status
   **Proposed**, with its **Adoption impact**. Take the next free
   number; CI fails if it is already used on `main`.
2. Make the text change, and update every summary of it in the same PR:
   `templates/global-CLAUDE.md`, `templates/methodology.mdc`,
   `templates/project-CLAUDE.md`, and any template that states the rule.
3. Add a `CHANGELOG.md` entry under **Unreleased**, with its adoption
   impact.
4. When vpc accepts it, a commit `docs: accept ADR NNNN (human sign-off)`
   sets the status to **Accepted** and, if it supersedes part of an
   earlier ADR, annotates that ADR's status line, and drops "proposed"
   from the changelog entry. This happens in the same PR, before merge:
   an ADR never merges or is released as Proposed. ADRs are otherwise
   append-only.

Work on the repo's own tooling (the reviewer, CI) that is substantial
gets a spec in `specs/<slug>/`, like any project.

## Releasing

The three methodology documents share one version, under
[Semantic Versioning](https://semver.org/) (ADR 0009).

1. Branch `chore/release-X.Y.Z`. In `CHANGELOG.md`, add
   `## [X.Y.Z] - YYYY-MM-DD` under `## [Unreleased]`, and update the
   compare links at the bottom of the file.
2. Commit as `chore: release X.Y.Z`, open a PR titled
   `chore: release X.Y.Z [skip-review]`, and merge it when `CI` passes.
3. Tag the merge commit and push the tag:

   ```
   git tag -a vX.Y.Z -m "vX.Y.Z — <one-line summary>"
   git push origin vX.Y.Z
   ```

4. If `templates/global-CLAUDE.md` changed since the last release, copy
   it to `~/.claude/CLAUDE.md` on each machine (ADR 0018).

There is no GitHub Release page; the tag and the changelog are the
record.
