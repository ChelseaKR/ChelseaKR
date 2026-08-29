# Changelog

This repository has no versioned releases — it is a GitHub profile README that
changes in place. Notable content changes are recorded here; the full history
is the git log.

## [Unreleased]

- Split `make names` in CI so that the half of it needing no privileged token
  actually runs. A missing `INVENTORY_TOKEN` had been skipping both halves, and
  no such secret has ever been configured here, so from the day the workflow
  was added that step exited 0 on every run having checked nothing. The linked-
  repository half — every `github.com/ChelseaKR/<name>` link is public and not
  archived — now runs on every build through a new `--links-only` mode that
  uses only the public API. It catches what `make links` structurally cannot:
  an archived repository answers 200. The bare-name-in-prose half still needs
  the token and still warns. Recorded as an amendment to ADR 0002 (2026-08-28).

- Checked every claim on the page against its source rather than assuming the
  last pass held. The current role, the not-consulting-and-not-looking line,
  and the separation of personal projects from Exygy and CiviForm work are all
  correct as written. The figures were re-verified against the repositories
  that produce them: `ctdl-validate`'s 120 documents and forty ERROR findings,
  `fhir-scorecard`'s 27 plans and eight verified base URLs, `disclosed`'s 600
  institutions and 387 with no admission rate, GTFS Scorecard's "more than
  2,100 feed records", and the wildfire overlap's 37.9 percent over 132,522
  records. None had drifted (2026-08-28).

- Followed the `inspected` rename to `wildfire-service-territory-overlap`. The
  weekly `verify` run went red on 2026-08-24 having been green on the same
  commit five days earlier, which is the failure mode ADR 0002 predicted: the
  rename happened in the other repository, so nothing was committed here and
  the page went stale on its own. Both checks caught it, from different angles
  — `make links` saw a `github.com` redirect that changed the path, and
  `make names` saw a link to a repository that is not in the public inventory
  under that name (2026-08-26).

- Gave this repository a license, which it had never had, and split it by what
  it covers: `LICENSE` is CC BY 4.0 for the profile prose, and `tools/LICENSE`
  is Apache-2.0 for the two checkers, matching the rest of the portfolio. With
  no `LICENSE` at all, everything here was reserved by default and nobody could
  quote the profile or reuse the checkers. Recorded as ADR 0003 (2026-08-26).

- Stopped saying that Unitrans and Yolobus "are running a 90-day pilot of the
  remediation handoff." They are not, and neither has agreed to anything. GTFS
  Scorecard uses those two feeds as worked examples — its own docs call them
  home-pilot examples — and separately has a 90-day remediation pilot that is
  still recruiting: the recruit step is open, the pilot issue has no replies,
  and the one piece of repair work done on those feeds is headed "independent
  demonstration, not an agency-published change." Two unrelated senses of the
  word "pilot" had been fused into a claim about two named public agencies
  (2026-08-18).
- Linked `mrf-honest` and `fare-policy-assistant` where "What I find in my own
  work" first names them. Every other project offered as evidence in that
  section was already a link. `mrf-honest` is public, and was the one project
  named on this page with no way to reach it from anywhere on it (2026-08-18).
- Gave this repository CI, which it had never had. `CONTRIBUTING.md` said to run
  `make verify` before pushing and nothing enforced it, so the checks ran only
  when someone remembered. `.github/workflows/verify.yml` now runs them on every
  pull request, on pushes to `main`, and once a week — weekly because link rot
  here is caused by renames and visibility changes made in *other* repositories,
  and arrives with no commit to trigger on (2026-08-18).
- Added `make links` (`tools/check_links.py`), which fails if a URL in this
  repository does not resolve for a logged-out visitor, or resolves somewhere
  other than where it says. It is unauthenticated on purpose, so it sees what a
  stranger sees. The failure it exists for is not a 404: GitHub forwards a
  renamed repository forever and answers `200`, so the stale links left by three
  renames in six weeks all passed a status check while the profile printed names
  that no longer existed. A redirect that changes the path on `github.com` is
  therefore a failure here, and the message names the target (2026-08-18).
- Closed a way `make names` could pass without looking at anything: a
  repository-scoped token — GitHub Actions' default `GITHUB_TOKEN` is one —
  lists only public repositories and reports no error, leaving the watchlist of
  non-public names empty. An inventory with no non-public repositories in it is
  now treated as an inventory that could not be read (2026-08-18).
- Added `make names` (`tools/check_repo_names.py`), which fails if any Markdown
  here names or links a repository of mine that is not public. It reads the
  live list from `gh repo list` and checks bare names in prose as well as
  links, because the failure it exists to prevent was three project names in
  sentences with no URL attached, which no link checker would have seen
  (2026-08-15).
- Second freshness pass (2026-08-15): linked the ctdl-validate browser
  playground, and called Permit Bearings a prototype, which is the word its own
  README and repository description use (2026-08-15).
- Freshness pass (2026-08-15): corrected the fare-policy-assistant figures to
  the 385-case, eighteen-agency harness and stated that the promoted 192-of-201
  baseline predates that expansion; added gauntlet, ctdl-validate-jvm, and
  oscal-validate to the project list; stopped naming projects that are no
  longer public in this changelog and in `docs/I18N.md`.
- Surfaced twelve previously unlisted repositories, fixed dead links, and
  stated the federal-contracting line explicitly (2026-08-12).
- Named the portfolio timeline, moved the AI-workflow disclosure above the
  project list, and added the "What outside review has changed" section
  (2026-08-08).
- Corrected the M.S. and test-coverage claims, added 2026 recognition, linked
  the live artifacts, stated the CTDL migration precisely, surfaced Afterward,
  removed the contract-value figures, and stated availability for consulting
  (2026-08-06).
- Removed the Ko-fi support link added earlier the same day (2026-08-05).

- Consolidated the repository's git history to a single commit (2026-07-19);
  earlier notable changes remain recorded below.

- Added Women-Artist Discovery, ID Churn Sentinel, and two projects that have
  since been made private to the project list; widened the climate section
  title to cover environmental and water-reuse work (2026-07-19).
- Removed the Standards Conformance section from the README; added a
  Recognition section, an education line, and a note on personal job-search
  tooling under "How I build" (2026-07-19).
- Added technology badges and live-state badges (PyPI version, Action release,
  site status) and reworded "This site" to "My personal site" to avoid reading
  as if the README were chelseakr.com (2026-07-19).
- Added standards-conformance documentation: `## Standards Conformance` table
  in the README, `SECURITY.md`, ADR log (`docs/adr/`), `docs/I18N.md`,
  `CODEOWNERS`, markdownlint via `make verify` and pre-commit, and this
  changelog (2026-07-16 portfolio standards sweep).
