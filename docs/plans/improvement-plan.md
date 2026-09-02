# Improvement plan — freshness audit, 2026-08-28

**Scope.** Every claim this profile makes about its owner and her work, every
URL it publishes, and whether the checks that guard those claims can fail.

**Method.** Claims were checked against the owner's confirmed current facts and
against the repositories that produce the figures. Links were resolved as a
logged-out visitor. The guard changed below was broken on purpose, watched to
fail, restored, and watched to pass.

---

## What is correct, and was verified rather than assumed

PR #22 merged on 2026-08-28 and landed the current-role rewrite. Re-read against
the owner's confirmed facts, it misses nothing:

- The page opens with **Director of Engineering for CiviForm at Exygy**, and
  `## Background` says it again in full.
- **"I am not consulting and I am not looking for a role."** appears under
  `## Where my attention is`. No availability, openness, or fractional-work
  language survives anywhere on the page.
- The projects paragraph states that the repositories **"are not CiviForm or
  Exygy work, and nothing in them speaks for either."**
- `wildfire-service-territory-overlap` is named correctly, after the rename from
  `inspected`.

The figures were re-checked against the repositories that produce them, not
against the last pass:

| Claim | Source | State |
| --- | --- | --- |
| `ctdl-validate`: 120 documents, forty ERROR findings | the repo's own findings write-up | holds |
| `fhir-scorecard`: 27 California plans, eight with a verified base URL | the repo's own cohort write-up | holds |
| `disclosed`: 600-institution sample, 387 with no admission rate, one at exactly zero | the repo's README | holds |
| GTFS Scorecard: "more than 2,100 feed records" | the repo's README | holds |
| wildfire overlap: 37.9 percent, 132,522 records | the repo's README | holds |

`make verify` passes, read by exit code: `GATE_EXIT=0`, with `check_links`
reporting 41 URLs across 9 files — 40 resolved, 0 redirected, 1 not checkable,
0 broken, and `check_repo_names` checking 9 files against 50 public
repositories with 31 non-public names watched for.

The single not-checkable URL is LinkedIn, which answers 404 or 999 to any client
that is not a logged-in browser. It is reported as carrying no information
rather than as a pass, and it was **not** removed on that basis. It is the one
claim on the page no automated check can stand behind; open it logged out.

---

## What was wrong: a CI step that had never checked anything

`.github/workflows/verify.yml` ran `make names` behind this guard:

```yaml
if [ -z "${GH_TOKEN}" ]; then
  echo "::warning ..."
  exit 0
fi
```

`gh secret list` on this repository returns **nothing**. `INVENTORY_TOKEN` has
never existed, so from the day the workflow was added that step has exited `0`
on every single run, having looked at nothing. Green, and watching for nothing —
the exact shape of check the README spends four paragraphs refusing to ship,
sitting in this repository's own CI.

The skip was honestly labelled, and ADR 0002 wrote the gap down. But the label
was wrong about one thing: it treated `make names` as one check. It is two, and
only one of them needs the privileged token.

| Half | Needs a PAT? | Ran in CI before |
| --- | --- | --- |
| Every linked `github.com/ChelseaKR/<name>` is public and **not archived** | no | never |
| Bare project **names** in prose, with no URL attached | yes | never |

The first half is not redundant with `make links`. An archived repository
answers `200`, so the link checker structurally cannot see one — its own
docstring says so.

### The fix

`tools/check_repo_names.py` gains `--links-only`, which asks the **public** API
about each linked slug and needs no privileged inventory. It uses `GITHUB_TOKEN`
for the rate limit only, never to see more than a stranger would: a repository
the token cannot see answers 404 either way, which is the answer we want.

It is fail-closed in the same two ways as everything else here:

- a rate-limit response (403/429) or an unreachable API **exits non-zero**,
  because a check that could not run is not a check that passed;
- finding **no links at all** exits non-zero, because a profile made of links
  that contains none means the file selection broke.

It prints, every run, that the bare-name half did **not** run — rather than
reporting a clean pass over both.

### Break results

Each break was confirmed on disk before the run, and each file confirmed
byte-identical to its backup after restore.

| Break | Result |
| --- | --- |
| Added a link to `ChelseaKR/personal-site` (private) in `CHANGELOG.md` | **FAIL** — "CHANGELOG.md:98: links to ChelseaKR/personal-site, which is not public (private, renamed, or deleted)" |
| Changed the file selection to `*.nosuchext` | **FAIL** — "no ChelseaKR repository links found in 0 Markdown file(s). That is not a pass" |
| Restored (both) | **PASS**, exit 0 — 16 linked repositories across 9 files, public and not archived |

---

## Still open

### `INVENTORY_TOKEN` is still not set

The bare-name half still cannot run in CI, and no change in this repository can
make it. It needs a fine-grained PAT with read access to repository metadata
across all repositories, saved as `INVENTORY_TOKEN`. Creating a secret is a
repository-settings change and was deliberately not made here.

Until then the warning is accurate and narrow: one half of one check does not
run, and CI says so on every build. `make names` in full still runs locally,
where `gh` is authenticated as an account that can see the private repositories
— that is how the 31 watched names were confirmed today.

### Three open issues that the last few passes have overtaken

Not closed here, because closing them is the owner's call:

- **#15** — "This repository has no CI workflow at all". It has had one since
  2026-08-26 (`.github/workflows/verify.yml`, added by PR #20). The issue's real
  substance — that `make verify` was not a gate on anything — was true of
  `make names` until this change, and is now true only of its bare-name half.
- **#17** — "The public CHANGELOG and docs/I18N.md name three private projects,
  and the changelog stopped three passes ago". `make names` passes locally today
  against all 31 non-public names, and the changelog carries entries through
  2026-08-26.
- **#14** — "Two portfolio figures have drifted, and nothing here checks claims
  or links". Link checking landed in PR #20. The figures were re-verified today
  and none had drifted.

### Curation is deliberate, not drift

**#16** notes that `gauntlet` is public and unnamed, and that more repositories
have shipped. There are 50 public repositories and the README names roughly a
third of them, under a heading that says "A few of the projects" and a sentence
pointing at the repositories tab for the rest. That is a curated selection
honestly framed, not a stale list. Adding a project is an editorial decision
about what shows the range, not a correctness fix.
