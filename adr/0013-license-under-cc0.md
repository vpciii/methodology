# ADR 0013: License the methodology under CC0 1.0 (public-domain dedication)

- **Status:** Accepted
- **Date:** 2026-06-08
- **Deciders:** vpc

## Context

The repository had no `LICENSE`. For an unlicensed work the legal default
is **all rights reserved**: others may view it but may not legally copy,
modify, or reuse it. That directly conflicts with the repository's
purpose — the templates exist *to be copied into other projects*, and the
methodology is written to be followed by other people, projects, and
agents. §10 already frames licensing as a decision.

The repository is private today, but the content is written for reuse;
deciding the license now removes the all-rights-reserved ambiguity before
any public or shared use rather than after.

The content is a **curated synthesis of existing, separately-credited
practices** (Nygard's ADRs, Evans's DDD, Preston-Werner's RDD,
Twelve-Factor, the DORA findings, and others, each cited at its origin).
Copyright protects *expression*, not methods or ideas, so the underlying
practices were never anyone's to fence off. The only copyrightable layer
here is the authored expression — the prose, the curation and
arrangement, the tables, the templates, and the ADRs. Attribution to the
author is not a goal.

## Decision

Dedicate the repository to the public domain under **CC0 1.0 Universal**.
The canonical CC0 text lives in `LICENSE`. Reuse requires no permission,
no attribution, and no preservation of notices — anyone, including the
author across any project (personal, client, or employer), may copy the
methodology, templates, and ADRs freely.

## Alternatives considered

- **MIT** — permissive, but requires preserving the copyright and license
  notice in every copy. That is notice-friction for boilerplate templates
  copied into many repositories, in exchange for an attribution benefit we
  do not want. Rejected.
- **CC BY 4.0** — permits reuse but *mandates attribution on every reuse*
  — maximal friction for the copy-everywhere template use case, and credit
  is not a goal. Rejected.
- **Copyleft (CC BY-SA, GPL-family)** — would force derivatives to stay
  open. An unnecessary constraint on a methodology meant to be adopted
  freely, including inside closed or proprietary projects. Rejected.
- **No license (status quo)** — rejected: all-rights-reserved legally
  forbids exactly the copying the repository is designed for, and the
  ambiguity only worsens once the repo is shared or made public.
- **Dual-license (prose under CC BY, templates under MIT/CC0)** — rejected
  as over-engineering for a personal repository; one frictionless license
  is simpler, and the split adds no value once attribution is not wanted.

## Consequences

- Anyone — including the author, across any project — may copy the
  methodology, templates, and ADRs with zero legal overhead.
- The author waives copyright and any attribution or enforcement over the
  authored expression. This is intended, not a cost to mitigate.
- CC0 waives only the author's rights to the author's own expression; it
  makes no claim over the third-party ideas the methodology cites (not
  copyrightable in any case) and grants no patent rights or warranty.
- The all-rights-reserved ambiguity is removed ahead of any decision to
  make the repository public.

## Adoption impact

**Reference-only.** Consuming projects gain explicit permission to copy
anything from this repository; there is nothing they must do to adopt
this change.

## References

- `methodology.md` §10 (dependencies and licensing are decisions).
- `LICENSE` (CC0 1.0 Universal); README "License" section.
- CC0 1.0 deed and legal code:
  <https://creativecommons.org/publicdomain/zero/1.0/>.

---

> Following the format proposed by Michael Nygard in
> [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
