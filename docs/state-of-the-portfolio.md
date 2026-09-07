# State of the portfolio

*Measured 2026-09-07. Every figure on this page was taken from a live query or a repository
on that date, and the command that produces it is named so you can re-take it.*

There are a lot of repositories on this profile and most of them are pre-1.0. This page is the
honest map: what you can actually install, what is actually running, what is a demonstration,
and what is stuck waiting on a person rather than on code.

## Reach

```text
45 public repositories of my own, plus 5 forks
49 stars across all of them
```

`gh repo list ChelseaKR --limit 100 --json name,visibility,isFork,stargazerCount`.

Nobody depends on this work. There is no user base, no download count worth quoting, and no
adoption story. If a number on this profile ever suggests otherwise, it is wrong and I would
like to know.

## Installable

Seven of these are published on PyPI under my name:

| Package | Version on PyPI | `pip install` |
|---|---|---|
| [`ctdl-validate`](https://github.com/ChelseaKR/ctdl-validate) | 0.2.1 | `ctdl-validate` |
| [`tods-validate`](https://github.com/ChelseaKR/tods-validate) | 0.11.0 | `tods-validate` |
| [`nearmiss`](https://github.com/ChelseaKR/nearmiss) | 0.4.0 | `nearmiss-safety` |
| [`habitable`](https://github.com/ChelseaKR/habitable) | 0.4.0 | `habitable` |
| [`cairn`](https://github.com/ChelseaKR/cairn) | 0.3.0 | `cairn-assistant` |
| [`gauntlet`](https://github.com/ChelseaKR/gauntlet) | 0.1.0 | `gauntlet-evals` |
| [`outcome-receipts`](https://github.com/ChelseaKR/outcome-receipts) | 0.1.0 | `outcome-receipts` |

Six of the seven match the version their repository declares. **`outcome-receipts` does not:**
the repository declares `0.2.0` and carries a `v0.2.0` tag with signed artifacts, and PyPI
still serves `0.1.0`. Anyone who installs it gets the older one. That is not a missing
feature; it is a publish step that has not been run.

Everything else on this profile you have to clone. Several repositories hold a distribution
name that is free or already mine and have simply never published.

## Live

These answered `200` to a logged-out request on 2026-09-07:

- [gtfsscorecard.org](https://gtfsscorecard.org) — daily GTFS scorecards
- [afterward.chelseakr.com](https://afterward.chelseakr.com) — California training programs
- [homeroom.chelseakr.com](https://homeroom.chelseakr.com) — California school pages
- [fhir.chelseakr.com](https://fhir.chelseakr.com) — FHIR endpoint scorecard
- [nearmiss.chelseakr.com/fars/national/](https://nearmiss.chelseakr.com/fars/national/) — the
  FARS conflict atlas
- [familygreenhouse.net](https://familygreenhouse.net) — household plant care
- [chelseakr.github.io/ctdl-validate/](https://chelseakr.github.io/ctdl-validate/) — a browser
  playground that uploads nothing
- [chelseakr.github.io/disclosed/](https://chelseakr.github.io/disclosed/) — higher-education
  disclosure grades
- [chelseakr.github.io/mrf-honest/](https://chelseakr.github.io/mrf-honest/) — hospital price
  file grades
- [chelseakr.github.io/plumbline/](https://chelseakr.github.io/plumbline/) and
  [chelseakr.github.io/gauntlet/](https://chelseakr.github.io/gauntlet/) — evidence pages for
  the two evaluation harnesses
- [chelseakr.github.io/perimeter/](https://chelseakr.github.io/perimeter/) — wildfire dataset
  coverage

That is twelve sites out of forty-five repositories. Most of this is a command-line tool or a
library, on purpose.

## Real data, and not

Some of these run against data a public body actually published. Others run against fixtures I
wrote, and the ones that do say so in their own README rather than leaving you to find out:

- [`exitdrill`](https://github.com/ChelseaKR/exitdrill) — *"technical alpha · synthetic data
  only"*, in the status line of its README
- [`contextsafe`](https://github.com/ChelseaKR/contextsafe) — runs on the synthetic fixtures
  that ship inside the package
- [`obligation-receipts`](https://github.com/ChelseaKR/obligation-receipts) — *"offline CLI and
  synthetic demonstration"*
- [`habitable`](https://github.com/ChelseaKR/habitable) — real tool, and its
  [live demo](https://habitable.chelseakr.com/) runs on synthetic data; its README's own status
  line lists *"no independent security/legal review, real tenant-union pilot"* among what is
  still missing
- [`nearmiss`](https://github.com/ChelseaKR/nearmiss) — the committed city datasets are
  synthetic; the 2020–2024 NHTSA FARS reference surface is real
- [`swelter`](https://github.com/ChelseaKR/swelter) — the live map is atmospheric model output,
  not physical sensors

Do not read a synthetic demonstration as a deployment. Where a project is running on real
published files, its README says which files and when they were acquired, and several publish
their own coverage as an output rather than a footnote.

## Blocked on a person, not on code

This is the part of the map I would most want to read about somebody else's portfolio, and it
is the part that never gets written down.

**The document navigator's entire corpus goes stale on 4 December 2026.**
[`trans-docs-navigator`](https://github.com/ChelseaKR/trans-docs-navigator) holds 688 records
across [53 jurisdiction files](https://github.com/ChelseaKR/trans-docs-navigator/tree/main/corpus/jurisdictions),
each with a `last_verified` date and a recheck SLA of 30 days (240 records) or 90 (448).
Adding those together against the real clock:

```text
records                      688
verified                     530
needs_reverification         158
already past SLA 2026-09-07  170
lapse in October 2026        508
last record expires          2026-12-04
sole verifier on record      "Pilot Seed Reviewer"
```

The freshness model works. It degrades records honestly rather than pretending they are
current. But it presumes a verifier roster, and the roster has never contained a named human,
so on 4 December every page it serves will say the same thing: needs reverification. This is
not a bug to fix. It is one person's afternoon per state, and there is no code that can supply
it.

**The GTFS remediation handoff has no pilot participant.** It is badged *Pilot* on
[`gtfs-scorecard`](https://github.com/ChelseaKR/gtfs-scorecard) for that reason, and it stays
badged that way until an agency actually walks through it.

**No Spanish answer in the fare assistant has been rated by a qualified speaker.**
[`fare-policy-assistant`](https://github.com/ChelseaKR/fare-policy-assistant) ships a
bilingual corpus and a 385-case evaluation harness, and its own EVALS record says the
bilingual-parity gate is currently failing. Spanish review is the open gate across several
projects here, including my own site.

**The community-run systems have no community running them.**
[`ledger`](https://github.com/ChelseaKR/ledger) is a preservation system designed for a
community to run itself, and no community runs it yet;
[`swelter`](https://github.com/ChelseaKR/swelter) is the same shape for heat and air quality.
Both are honest about it in the first line of their descriptions. Neither can be finished by
writing more code.

**A batch of engineering-standards changes is waiting on a governance attestation only I can
give.** The gate is deliberate and it is working as designed — the attestation is a human
statement and its list of non-human tokens is there precisely so that automation cannot supply
it. The consequence is a queue, and the queue is mine.

## What I would not rely on

Every repository here states its own maturity in its first line, and I would rather you took
its word than mine. Read that line before you read anything else. Where a project says
*pre-alpha*, *technical alpha*, *in build*, *shelved*, or *not currently live*, it means it.

The three things I would be most careful about: nothing here has had an independent security
review; the Spanish content across the portfolio has not been reviewed by a qualified native
speaker; and every "grade" this portfolio publishes about a named organisation is computed
from that organisation's own published files, which is a narrow claim and is written to stay
narrow.

## How to check this page

```sh
# reach
gh repo list ChelseaKR --limit 100 --json name,visibility,isFork,stargazerCount

# published version of any package above
curl -s https://pypi.org/pypi/outcome-receipts/json | python3 -c 'import json,sys; print(json.load(sys.stdin)["info"]["version"])'

# the corpus expiry, from the committed files
git clone --depth 1 https://github.com/ChelseaKR/trans-docs-navigator
# then sum last_verified + recheck_sla_days over corpus/jurisdictions/*.json
```

If any of it has drifted, that is a defect in this page and I would like an issue about it.

---

*This page is CC BY 4.0, like the rest of this repository's prose.*
