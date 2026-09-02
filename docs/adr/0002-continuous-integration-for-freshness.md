# 2. Continuous integration here checks freshness, not correctness

## Status

Accepted

## Context

ADR 0001 declared Release & Versioning N/A here: there is no build, no package,
and nothing to ship. The same reasoning was quietly extended to CI, and this
repository had none. `CONTRIBUTING.md` said to run `make verify` before pushing,
and nothing enforced it — the checks ran when someone remembered.

That reasoning was wrong, because it assumed the thing CI protects is a build.
What actually breaks here is a claim, and it breaks without anyone touching this
repository:

- A project gets renamed. GitHub forwards the old name forever and answers
  `200`, so the profile keeps printing a name that no longer exists and no
  status check notices. Three renames happened in the six weeks before this ADR.
- A project is made private or archived. Every link to it becomes a 404 for a
  visitor, and a bare name in a sentence becomes a reference to nothing.
- A file linked deep inside another repository moves, or that repository's
  default branch is renamed, and a `/blob/<branch>/<path>` URL dies.

None of those produce a commit here. All of them are, for a stranger reading
this page, the profile being wrong.

## Decision

`.github/workflows/verify.yml` runs the `make verify` checks on pull requests,
on pushes to `main`, and on a weekly schedule. The weekly run is the point: it
is the only one that fires when the cause of the failure is in someone else's
repository.

The checks are split by what they need, not by what they look at:

- `make lint` and `make links` need no credentials. `make links` is
  *deliberately* unauthenticated, so that it sees what a logged-out visitor
  sees, and it treats a path-changing redirect on `github.com` as a failure
  rather than a pass, because that is exactly what a rename looks like.
- `make names` needs an authenticated `gh` that can see private repositories.
  CI's default `GITHUB_TOKEN` cannot: it lists only public repositories and
  reports no error, which would leave the watchlist empty and the check passing
  on nothing. So `check_repo_names.py` now refuses an empty watchlist, and the
  workflow emits a warning saying the check did not run unless an
  `INVENTORY_TOKEN` secret is configured.

Neither link checking nor name checking subsumes the other, and both stay.

## Amendment, 2026-08-28

The paragraph above treated `make names` as one check that either runs or does
not. It is two, and only one of them needs the privileged token. Because they
were bound together, a missing `INVENTORY_TOKEN` skipped both — and no
`INVENTORY_TOKEN` has ever been configured on this repository, so from the day
this workflow was added the step exited `0` on every run having checked
nothing at all. Green, and watching for nothing. That is the shape of check
this profile spends its README refusing to ship, sitting in its own CI.

The two halves are now separate steps:

- **Every linked repository is public and not archived.** This needs no
  privileged inventory. `check_repo_names.py --links-only` asks the public API
  about each linked slug, using `GITHUB_TOKEN` for the rate limit only and
  never to see more than a stranger would. It runs on every build. It is not
  redundant with `make links`, which cannot see an archived repository: an
  archived repository answers `200`.
- **Bare project names in prose, with no URL attached.** This genuinely needs a
  token that can see private repositories, and still warns rather than running
  until `INVENTORY_TOKEN` exists.

The `--links-only` mode is fail-closed in the same two ways as everything else
here: it exits non-zero if the API cannot be reached or answers with a rate
limit rather than an answer, and it exits non-zero if it finds no links at all,
because a profile made of links that contains none means the file selection
broke rather than that everything passed.

## Consequences

- A stale link or a reference to a repository that stopped being public now
  surfaces within a week instead of whenever someone next reads the page
  closely.
- CI is green-but-incomplete until `INVENTORY_TOKEN` exists, and as of the
  2026-08-28 amendment that gap is narrowed to one half of one check: bare
  project names in prose. It is stated in the run summary as a warning rather
  than hidden, because a check that did not run is not a check that passed —
  the rule this profile applies to everything else it builds.
- Public repositories run Actions free, so this costs nothing to keep.
- If a third-party link starts flapping, the fix is to record why in
  `UNCHECKABLE` in `tools/check_links.py`, with the reason, where it is visible
  in the output — not to loosen the check.
