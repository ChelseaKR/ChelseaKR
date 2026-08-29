# Chelsea Kelly-Reif 🏳️‍⚧️

**Director of Engineering for [CiviForm](https://github.com/civiform/civiform) at
[Exygy](https://github.com/Exygy).** CiviForm is open source. It is built by Exygy and Google.org
with the City of Seattle and community contributors, and it exists so that applying for one
government benefit does not mean answering the same questions again for the next one.

I lead engineering for public-interest systems, and I still build them. Most of my public
repositories are measurement tools: validators, scorecards, and evaluation harnesses pointed at
real transit feeds, hospital price files, health-plan APIs, credential records, college
disclosures, and California energy filings.

[chelseakr.com](https://chelseakr.com) ·
[LinkedIn](https://www.linkedin.com/in/chelseakr) · Davis, California

## How these got built

Every public repository here was built since June 2026, and AI agents are part of how I work. I
choose the architecture, write the acceptance criteria, review the output, and decide what is
ready to release. That is why this much exists in this little time.

It is also why so much of it is gates. The failure mode of working this way is a check that cannot
fail and a green build that means nothing, so each project is built so that it can fail, and when
it does the failure is written down where you reach it before you reach the claim.

These are independent personal projects with no proprietary or client material in them. They are
not CiviForm or Exygy work, and nothing in them speaks for either.

## What outside review changed

These projects have very few stars. What they have instead is a record of being corrected in
public.

**A project's scope.** [Jannis (derhuerst)](https://github.com/derhuerst), a longtime open
transit-data maintainer, [argued](https://github.com/ChelseaKR/gtfs-scorecard/issues/194) that
GTFS Scorecard's scoring belonged inside MobilityData's canonical validator rather than in one
more dashboard. He was substantially right. I named in the thread the tools I had duplicated,
declined to push subjective letter grades into an official project where they would read as
guidance, and narrowed this one to the handoff nobody else covers.

**A scoring rule.** The person who produces the MRC de Joliette feed
[pushed back](https://github.com/ChelseaKR/gtfs-scorecard/issues/180) on a recommendation to
populate `trip_headsign` on loop routes. They were right, and the rule now credits that case
instead of flagging it.

Upstream, MobilityData merged a
[specification example fix](https://github.com/MobilityData/transit-operational-data-standard/pull/147)
to the Transit Operational Data Standard and an
[awesome-transit listing](https://github.com/MobilityData/awesome-transit/pull/387). A
[conformance-language clarification](https://github.com/MobilityData/transit-operational-data-standard/pull/156),
a [second awesome-transit listing](https://github.com/MobilityData/awesome-transit/pull/389), and
a [Transitland feed-archival PR](https://github.com/transitland/transitland-atlas/pull/2098) are
open. Five small contributions, two of them merged. That is the whole claim.

## Where to start

There are more repositories here than anyone wants to browse. They fall into six groups, and each
group has one worth reading first.

- **Transit data.** Start with [`gtfs-scorecard`](https://github.com/ChelseaKR/gtfs-scorecard).
  Then `tods-validate`, `fare-policy-assistant`, `transit-delivery-atlas`.
- **California filings and public records.** Start with
  [`qfer-preflight`](https://github.com/ChelseaKR/qfer-preflight). Then `power-content-check`,
  `ca-tariff-parse`, `ceqa-preflight`, `permit-bearings`, `perimeter`,
  `wildfire-service-territory-overlap`.
- **Standards conformance.** Start with
  [`ctdl-validate`](https://github.com/ChelseaKR/ctdl-validate). Then `oscal-validate`,
  `fhir-scorecard`, `mrf-honest`, `ctdl-validate-jvm`.
- **Education and workforce.** Start with [`afterward`](https://github.com/ChelseaKR/afterward).
  Then `disclosed`, `homeroom`, `chalkline`.
- **Evaluation gates and receipts.** Start with
  [`plumbline`](https://github.com/ChelseaKR/plumbline). Then `gauntlet`, `cairn`, `sprout`,
  `contextsafe`, `outcome-receipts`, `obligation-receipts`, `exitdrill`.
- **Community and personal tools.** Start with
  [`habitable`](https://github.com/ChelseaKR/habitable). Then `ledger`, `swelter`, `nearmiss`,
  `id-churn-sentinel`, `davis-bike-hazard-map`, `queer-the-stacks`, `encore`, `family-greenhouse`,
  `olive-bark-logger`, `lavender-rotation`.

## Six that show the range

Most are pre-1.0, and I would rather you take a repository's own word for its maturity than mine.

- **[GTFS Scorecard](https://github.com/ChelseaKR/gtfs-scorecard)** (live at
  [gtfsscorecard.org](https://gtfsscorecard.org)) grades more than 2,100 curated transit feed
  records daily in plain language. Correctness findings come from MobilityData's canonical
  validator, not a competing one. Because it names public agencies it publishes a
  [listing policy](https://github.com/ChelseaKR/gtfs-scorecard/blob/main/docs/listing-policy.md),
  and its remediation handoff is badged *Pilot* because that pilot has not recruited a participant
  yet.
- **[tods-validate](https://github.com/ChelseaKR/tods-validate)** checks Transit Operational Data
  Standard feeds, the crew runs and vehicle assignments GTFS does not cover, against TODS v2.1.0,
  with rule IDs that are never renumbered and a GitHub Action so an agency gates a bad feed before
  publishing. Reading that spec closely enough to write the rules is what produced the two upstream
  TODS pull requests above.
- **[ctdl-validate](https://github.com/ChelseaKR/ctdl-validate)** structurally validates CTDL
  JSON-LD, the national credential-data standard, citing the published schema behind every finding,
  as a CLI, a GitHub Action, and a browser
  [playground](https://chelseakr.github.io/ctdl-validate/) that uploads nothing. Run against
  [120 documents sampled from the public Credential Registry](https://github.com/ChelseaKR/ctdl-validate/blob/main/docs/findings/2026-08-15-published-registry-survey.md)
  it returned forty ERROR findings, every one tracing to an inconsistency inside CTDL's own schema
  encoding rather than to a publisher's mistake. That is a finding about the tool as much as about
  the corpus, and the write-up leads with it.
- **[afterward](https://github.com/ChelseaKR/afterward)** joins 3,266 California training programs
  reported under WIOA to the state's own ten-year projection for the occupation each leads to, in
  English and Spanish, with no account and no tracking. A suppressed or unreported outcome never
  renders as zero, and how much the join actually covers is a published output rather than a
  footnote.
- **[fare-policy-assistant](https://github.com/ChelseaKR/fare-policy-assistant)** answers rider
  questions about reduced-fare policy over a corpus covering eighteen California transit agencies.
  The assistant exists so that the public evaluation harness has something to evaluate: 385 cases,
  versioned prompts, a committed regression baseline, merge-blocking refusal and grounding gates,
  and a standing record of what it has not measured, including that none of its 28 Spanish answers
  has been rated.
- **[habitable](https://github.com/ChelseaKR/habitable)** makes habitability evidence for tenant
  unions tamper-evident with content hashes and RFC 3161 timestamps, then syncs peer to peer under
  end-to-end encryption so there is no central holder to subpoena. Its own README says not to rely
  on it for real legal matters yet, and I agree with it.

## What I find in my own work

A tool that grades other people's work has no business shipping a check that cannot fail. Hunting
those down in my own repositories is a standing part of how I build.

[`plumbline`](https://github.com/ChelseaKR/plumbline) is a fail-closed audit harness. A target that
returned 174 empty responses scored 1.0000 on groundedness, privacy, representational harms,
fairness and cross-language, and the gate exited PASS on that alone, because each of those checks
is phrased as the absence of a bad thing and silence satisfies all of them.
[The fix](https://github.com/ChelseaKR/plumbline/commit/5caf8e5b36094e9693e440dbd9a83d2dab0c34a7)
splits the two kinds of check apart, and a test now fails the build if a silent target ever passes
again.

That same shape turned up again and again elsewhere, every instance green at the time.
[`ceqa-preflight`](https://github.com/ChelseaKR/ceqa-preflight/commit/95db489acfb5) printed four
PASS lines over a package whose PDFs had all timed out, one of them affirmatively clearing a
document it had never opened. A weekly monitor in
[`id-churn-sentinel`](https://github.com/ChelseaKR/id-churn-sentinel/commit/ad9a9cdf2472) went
green four weeks running while zero of its 152 sources were eligible to check, because observing
nothing emitted the same signals as observing no change.

## Background

Before Exygy I was a Senior Director of Engineering at [Coforma](https://coforma.io), one of three
in a 50-person engineering organization, leading a 22-person reporting structure and owning the
company-wide healthcare engineering portfolio. Nine engineers moved into senior or leadership roles
under me, four of them to Director or Principal.

Before that I was engineering lead and principal engineer for
[MyCareer.NJ.gov](https://mycareer.nj.gov), New Jersey's statewide workforce platform, where I set
architecture across three production codebases, ran a zero-downtime GCP to AWS migration, shipped
full English and Spanish parity, and did the 2023 CTDL data modeling that began New Jersey's
migration of its training-program registry into the national Credential Engine ecosystem. Earlier I
built public systems for the California Energy Commission, the California Public Utilities
Commission, the California Department of Social Services, and UC Berkeley's Graduate School of
Education. I am a registered member of Credential Engine's CTDL Advisory Group.

The domains I keep returning to are public health, workforce and social services, energy and
utilities, state and local digital services, and responsible AI: work that helps the people public
systems routinely fail.

## What I will and will not work on

- No weapons, warfare, policing, mass surveillance, or technology that profits from incarceration.
- No AI that decides whether a person gets a job, a benefit, a service, or an opportunity. It can
  support a human decision, as long as that human can inspect the evidence, correct what is wrong,
  and make the final call.
- Accessibility, privacy, security, operability, and multilingual delivery are engineering
  requirements, not a later phase.

## Where my attention is

CiviForm, and the repositories above. **I am not consulting and I am not looking for a role.**
Reach me through [chelseakr.com](https://chelseakr.com) or
[LinkedIn](https://www.linkedin.com/in/chelseakr).
