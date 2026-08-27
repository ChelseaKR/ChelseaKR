# 3. Licensing splits the profile prose from the checkers

## Status

Accepted

## Context

This repository carried no `LICENSE` file at all. Under GitHub's terms that
leaves everything here reserved by default: a stranger who wants to quote the
profile, or to lift the link checker into their own profile repository, has no
permission to do either and no statement telling them so.

Two different kinds of thing live here, and one license is a poor fit for both:

- **Prose.** `README.md` is a personal professional profile — a biography and a
  set of claims about my own work. `CHANGELOG.md`, `CONTRIBUTING.md`,
  `SECURITY.md`, and `docs/` are prose about that prose.
- **Code.** `tools/check_links.py` and `tools/check_repo_names.py` are around
  450 lines of Python that solve a problem other people demonstrably have: a
  profile README that keeps printing repository names after a rename, and one
  that names a repository after it stops being public. ADR 0002 is the argument
  for why they exist. They are worth reusing.

A software license on a biography is the wrong instrument — it talks about
source form, object form, and patent grants, none of which a paragraph has.
Creative Commons, for its part, recommends against applying its licenses to
software, because they say nothing about source availability. So the choice is
not which single license, but whether to admit that this repository holds two
kinds of work.

The rest of the portfolio licenses its code Apache-2.0, with one AGPL-3.0
exception, so the code half has an established answer already.

## Decision

Two licenses, scoped by directory:

- **`LICENSE`** (repository root) is **CC BY 4.0**, and covers the profile
  prose: `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, and
  everything under `docs/`. Attribution is the condition that matters for a
  biography: reuse is fine, passing it off as someone else's is not.
- **`tools/LICENSE`** is **Apache-2.0**, and covers the checkers. It is the
  canonical Apache-2.0 text with the appendix placeholder filled in the way the
  rest of the portfolio fills it, so the copyright line reads
  `Copyright 2026 Chelsea Kelly-Reif`.

The root `LICENSE` carries a two-line header pointing at `tools/LICENSE`, so
that a reader who opens only the root file learns the split exists. The header
is short on purpose: GitHub detects a license by comparing the file against a
reference text, and a long preamble would push it below the similarity
threshold and leave the repository reading as unlicensed again.

The split is recorded in `CONTRIBUTING.md` and not in `README.md`. GitHub
renders `README.md` as my profile page, so a "License" heading there would show
up as a section of the biography itself. GitHub already surfaces the root
license in the repository sidebar, which is where someone looking for it looks.

## Consequences

- The repository reports a license through the GitHub API instead of `null`,
  which is what the audit that prompted this ADR was reading.
- Someone may quote or adapt the profile prose with attribution, and may reuse
  the checkers under the same terms as every other tool in this portfolio.
- A third license would be a smell. If a new kind of artifact lands here that
  fits neither file, that is a sign it belongs in its own repository, not that
  this one needs another `LICENSE`.
- If the root header ever grows, GitHub's license detection has to be
  re-checked; the header exists to be read, not to be extended.
