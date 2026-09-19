# Chelsea Kelly-Reif 🏳️‍⚧️

**Engineering leader for government digital services.**
Director of Engineering for [CiviForm](https://github.com/civiform/civiform) at
[Exygy](https://github.com/Exygy).

I've built and led engineering for benefit applications, a statewide career platform, Medicaid and
CHIP reporting to CMS, and California's energy-data filings. I learned the work inside California
government, and I still write code.

[chelseakr.com](https://chelseakr.com) ·
[Resume (PDF)](https://chelseakr.com/files/Chelsea_Kelly-Reif_Resume.pdf) ·
[LinkedIn](https://www.linkedin.com/in/chelseakr) · Davis, California

## Government programs I've led and shaped

What each program is, who it serves, my role, and what the public record shows. Results belong to
the teams that built them; my part is stated as scope.

- **[CiviForm](https://github.com/civiform/civiform)** (Exygy, 2026 to present). Open-source
  software that lets a government offer one application for many benefit programs, reusing what an
  applicant has already entered. Four city and state governments run it in production, including
  Seattle and Arkansas. I have been Director of Engineering since August 2026, leading engineering
  for the platform. The four-person team ships on a biweekly release train.
- **[MyCareer.NJ.gov](https://mycareer.nj.gov)** (Coforma, 2022 to 2026). New Jersey's statewide
  career and training platform, in English and Spanish: career exploration, training programs with
  their outcomes, and job search. I was engineering lead and principal engineer from an early
  prototype to a statewide service, and primary engineer across its three production codebases. It
  has recorded 1.8 million active users since December 2023. I did the 2023 data modeling that
  began the state's move to Credential Engine's CTDL standard, and its training programs are live
  in the Registry today.
- **[Medicaid and CHIP Data Collection Tools (MDCT)](https://github.com/Enterprise-CMCS?q=macpro-mdct)**
  (Coforma, 2025 to 2026). CMS's open-source suite of seven applications that states and
  territories use to report Medicaid and CHIP program data. I owned engineering for the suite
  within Coforma's healthcare portfolio: direction, standards, and the conditions for delivery.
  Feature leads did the hands-on build. The team took a new CMS Rural Health Transformation
  application from zero to first production in about eight weeks, and all seven applications
  shipped production releases in 2026 while I led the portfolio.
- **[Medicaid Drug Programs (MDP)](https://chelseakr.com/health)**
  (Coforma, 2025 to 2026). The CMS system behind the Medicaid Drug Rebate Program. Drug
  manufacturers report product and pricing data through it, and CMS uses that data to calculate the
  rebates owed to state Medicaid agencies. About 780 manufacturers participate. My role was
  oversight within the same healthcare portfolio; a partner's technical leads ran implementation.
- **[Data Submission Portal (DSP)](https://chelseakr.com/energy)** (California Energy
  Commission, 2019 to 2022). The Energy Commission's secure, cloud-based portal for filing
  regulatory energy data, starting with petroleum and quarterly fuel-and-energy reports. As Lead
  Software Engineer I architected and shipped it on AWS and helped lead the commission's cloud
  modernization. The commission later expanded the platform across the agency and into residential
  solar-permit reporting.

## How I lead

I lead managers and senior engineers, and I stay close enough to the architecture to answer for it.

At Coforma I was a Senior Director of Engineering, one of three in a 50-person engineering
organization, and I owned the company-wide healthcare engineering portfolio. My reporting structure
was 22 people, with five direct reports, three of them Directors. Nine engineers were promoted
within it, four to Director or Principal, and three people left voluntarily in three years.

The practices I put in place cover planning, hiring, delivery, and growth. On MyCareer.NJ.gov,
accessibility, security, and bilingual parity became part of the release path, and automated test
coverage went from zero to 93 to 96 percent while security vulnerabilities fell 94 percent. At
CiviForm I supervise two Google.org fellowship workstreams alongside the engineering team.

## Public projects I build and run

Independent work on my own time, built in the open on public data. The status beside each one says
how far along it is. Most of my public repositories are measurement tools: validators,
scorecards, and evaluation harnesses pointed at real transit feeds, hospital price files,
health-plan APIs, credential records, college disclosures, and California energy filings. These
are personal projects with no proprietary or client material in them.
They are not CiviForm or Exygy work, and nothing in them speaks for either. Most are pre-1.0, and I
would rather you take a repository's own word for its maturity than mine.
[State of the portfolio](docs/state-of-the-portfolio.md) is the honest map, re-measured on
2026-09-18: what is installable, what is live, what is a synthetic demonstration, and what is
waiting on a person rather than on code.

### Live products

- [Afterward](https://afterward.chelseakr.com) ([source](https://github.com/ChelseaKR/afterward)),
  beta. 3,266 California training programs joined to the state's own job projections, in English
  and Spanish, with no account.
- [Homeroom](https://homeroom.chelseakr.com) ([source](https://github.com/ChelseaKR/homeroom)),
  live. California public school data for every active school, 10,534 of them, readable by the
  families it describes, in English and Spanish.
- [Trout Truck](https://chelseakr.github.io/ca-fish-planting-alerts/)
  ([source](https://github.com/ChelseaKR/ca-fish-planting-alerts)), beta. California's trout
  planting schedule, with a stocking history for each water, rebuilt daily from the Department of
  Fish and Wildlife's weekly schedule.
- [Next Home Game](https://nexthomegame.com)
  ([source](https://github.com/ChelseaKR/womens-sports-calendar)), live. Calendar feeds for
  women's pro and college sports, by league and team, updated nightly.
- [Family Greenhouse](https://familygreenhouse.net)
  ([source](https://github.com/ChelseaKR/family-greenhouse)), live. A shared plant-care journal
  for households: watering schedules, care tasks, and reminders. Free accounts and paid plans.
- [Transit Delivery Atlas](https://transit.chelseakr.com)
  ([source](https://github.com/ChelseaKR/transit-delivery-atlas)), early release. A source-linked
  crosswalk of California's transit executive order, N-7-26, directive by directive.

### Open-source scorecards and validators

- [GTFS Scorecard](https://gtfsscorecard.org)
  ([source](https://github.com/ChelseaKR/gtfs-scorecard)), live beta. Daily plain-language quality
  grades for more than 2,100 public transit feed records, with a GitHub Action and a read API.
- [fhir-scorecard](https://fhir.chelseakr.com/)
  ([source](https://github.com/ChelseaKR/fhir-scorecard)), beta. Daily grades for public FHIR
  health-data endpoints, with every finding cited to the spec.
- [TODS Validate](https://chelseakr.github.io/tods-validate/)
  ([source](https://github.com/ChelseaKR/tods-validate)), beta. A validator for the Transit
  Operational Data Standard, as a command-line tool, a GitHub Action, and a browser playground.
- [ctdl-validate](https://chelseakr.github.io/ctdl-validate/)
  ([source](https://github.com/ChelseaKR/ctdl-validate)), beta. Checks CTDL credential records
  against the published rules before they go to the Credential Registry.

Every project, with its evidence, is on [chelseakr.com/work](https://chelseakr.com/work).

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
  `outcome-receipts`, `obligation-receipts`, `exitdrill`.
- **Community and personal tools.** Start with
  [`habitable`](https://github.com/ChelseaKR/habitable). Then `ledger`, `swelter`, `nearmiss`,
  `id-churn-sentinel`, `davis-bike-hazard-map`, `queer-the-stacks`, `encore`, `family-greenhouse`,
  `olive-bark-logger`, `lavender-rotation`.

## Six that show the range

Most are pre-1.0, and I would rather you take a repository's own word for its maturity than mine.
[State of the portfolio](docs/state-of-the-portfolio.md) is the honest map, re-measured on
2026-09-18: what is installable, what is live, what is a synthetic demonstration, and what is
waiting on a person rather than on code.

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

I have written the whole class up, with nine instances and the fix commits attached, in
[The confident zero](docs/the-confident-zero.md). It includes the part that is least flattering
and most useful: I built a static detector for this shape, it missed more of them than it caught,
and its highest-recall rule is the one I cannot ship.

## Earlier work

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
