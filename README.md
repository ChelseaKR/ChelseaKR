# Chelsea Kelly-Reif 🏳️‍⚧️

I lead engineering for public-interest systems, and I still build them. Most of my public
repositories are measurement tools: validators, scorecards, and evaluation harnesses pointed at
real transit feeds, hospital price files, health-plan APIs, credential records, college
disclosures, and California energy filings.

The interesting part is not how many there are. It is that each one is built so it can fail, and
that when it does fail the failure is written down where you reach it before you reach the claim.

Open to engineering leadership roles and to fractional consulting.
[chelseakr.com](https://chelseakr.com) ·
[LinkedIn](https://www.linkedin.com/in/chelseakr) · Davis, California

## What outside review changed

These projects have very few stars. What they have instead is a record of being corrected in
public.

**A project's scope.** [Jannis (derhuerst)](https://github.com/derhuerst), a longtime open
transit-data maintainer, [argued](https://github.com/ChelseaKR/gtfs-scorecard/issues/194) that GTFS
Scorecard's scoring belonged inside MobilityData's canonical validator rather than in one more
dashboard. He was substantially right. I compared the closest existing tools, named in the thread
the ones I had duplicated, declined to push subjective letter grades into an official project where
they would read as guidance, and narrowed this one to the handoff nobody else covers: a named fix
request, a comparable recheck of the same published feed, and reproducible closure evidence.

**A scoring rule.** The person who produces the MRC de Joliette feed
[pushed back](https://github.com/ChelseaKR/gtfs-scorecard/issues/180) on a recommendation to
populate `trip_headsign` on loop routes. They were right. GTFS Best Practices discourage repeating
the route name there, and that feed's blank headsigns were single-pattern frequency templates. I
changed the rule so that case is credited instead of flagged, and the same thread shows the feed's
score moving once the change landed.

Upstream, MobilityData merged a
[specification example fix](https://github.com/MobilityData/transit-operational-data-standard/pull/147)
to the Transit Operational Data Standard and an
[awesome-transit listing](https://github.com/MobilityData/awesome-transit/pull/387). A
[conformance-language clarification](https://github.com/MobilityData/transit-operational-data-standard/pull/156),
a [second awesome-transit listing](https://github.com/MobilityData/awesome-transit/pull/389), and a
[Transitland feed-archival PR](https://github.com/transitland/transitland-atlas/pull/2098) are
open.

## What I find in my own work

A tool that grades other people's work has no business shipping a check that cannot fail. Hunting
those down in my own repositories is a standing part of how I build, and the commit messages
say so.

**A perfect score out of silence.**
[`plumbline`](https://github.com/ChelseaKR/plumbline) is a fail-closed audit harness. A target that
returned 174 blank responses scored 1.0000 on groundedness, privacy, representational harms,
fairness, and cross-language, and the gate exited PASS on that alone, because each of those checks
is phrased as the absence of a bad thing and silence satisfies all of them.
[The fix](https://github.com/ChelseaKR/plumbline/commit/5caf8e5b36094e9693e440dbd9a83d2dab0c34a7)
splits the two kinds of check apart: behavior suites score silence as zero, absence suites report
UNVERIFIABLE instead of passing, and a test now fails the build if a silent target ever passes
again.

**The same shape, everywhere else.** Going looking for it across the rest of the repositories
found it again and again, every instance green at the time.
[`ceqa-preflight`](https://github.com/ChelseaKR/ceqa-preflight/commit/95db489acfb5)
printed four PASS lines over a package whose PDFs had all timed out, byte-identical to the lines
a clean package produces, and one of the four was the active-content check, so the report
affirmatively cleared a document it had never opened. A weekly monitor in
[`id-churn-sentinel`](https://github.com/ChelseaKR/id-churn-sentinel/commit/ad9a9cdf2472) went
green four weeks running while its registry left zero of 152 sources eligible to check, because
observing nothing emitted the same signals as observing no change. The two-person review gate in
[`constituent-reconciler`](https://github.com/ChelseaKR/constituent-reconciler/commit/0a19009ce00a)
was read by the review session and by neither apply path, so a merge under the strict policy pack
went through on a single approver. And the CI lockfile check in these repositories ran only
`uv sync --frozen`, which installs what the lockfile records and exits 0 no matter how far the
lockfile has drifted from `pyproject.toml`; I measured that, fixed it everywhere it appeared, and
corrected the
[decision record](https://github.com/ChelseaKR/tods-validate/commit/ed96461bb0445050032a0b05cc740880066b10b8)
that had asserted the opposite.

**A statistic that could only come back perfect.**
[`fare-policy-assistant`](https://github.com/ChelseaKR/fare-policy-assistant) published a
judge-calibration agreement of 1.000 until I checked how it was computed. Every label that recorded
a disagreement between the human and the judge had gone stale, so the surviving sample was the
agreeing half. It now reports the coefficient as undefined, on 4 scored labels against a floor of
37, on the evaluation report itself.

The same rule applies to results. [`mrf-honest`](https://github.com/ChelseaKR/mrf-honest) broke
twice on its first real cohort of hospital price files, on a CSV dialect the reader guessed instead
of declaring and on a memory ceiling two large exports exceeded. Both breaks are on the front page
of the repository, in the paragraph directly under the grades.

## Measuring named organizations

Several of these projects publish measurements about real, named institutions. That is only
defensible with rules, so the rules are written down and enforced in code.

- `ctdl-validate` validated
  [120 documents sampled from the public Credential Registry](https://github.com/ChelseaKR/ctdl-validate/blob/main/docs/findings/2026-08-15-published-registry-survey.md).
  Forty ERROR findings came back, and each one traced to an inconsistency inside CTDL's own
  published schema encoding rather than to a mistake a publisher made. The write-up leads with
  that, because it is a finding about the tool as much as about the corpus.
- `fhir-scorecard` reviewed
  [what 27 California health plans publish about their FHIR endpoints](https://github.com/ChelseaKR/fhir-scorecard/blob/main/docs/findings/2026-08-15-california-payer-cohort.md).
  The roster was fixed from public directories before any endpoint was looked for, so the plans
  that publish nothing are part of the result rather than an absence in it. Eight of the 27
  publish a base URL the project could verify. None of it is a compliance determination, and the
  document says so before it shows a number, because the federal rule does not require a plan to
  print its base URL where an unregistered visitor can read it.
- Every figure in those write-ups is recomputed from the committed evidence by a test that fails
  the build when a number in the prose stops matching its data.
- GTFS Scorecard grades public agencies by name, so it publishes a
  [listing policy](https://github.com/ChelseaKR/gtfs-scorecard/blob/main/docs/listing-policy.md):
  what gets listed and why, how to correct an entry, and that a removal request is honored without
  argument.

## A few of the projects

The rest are on the [repositories tab](https://github.com/ChelseaKR?tab=repositories). These are
the six that show the range. Most are pre-1.0, every one states its own maturity, and I would
rather you take the repository's word for that than mine.

- **[GTFS Scorecard](https://github.com/ChelseaKR/gtfs-scorecard)** (live at
  [gtfsscorecard.org](https://gtfsscorecard.org)) publishes daily, plain-language transit data
  quality grades over a registry of more than 2,100 feed records. Correctness comes from
  MobilityData's canonical validator, not from a competing one. Unitrans and Yolobus are running a
  90-day pilot of the remediation handoff.
- **[fare-policy-assistant](https://github.com/ChelseaKR/fare-policy-assistant)** (evidence at
  [evals.chelseakr.com](https://evals.chelseakr.com)) answers rider questions about reduced-fare
  policy for eighteen California transit agencies. The assistant exists so that the public
  evaluation harness has something to evaluate: versioned prompts, a committed regression baseline,
  merge-blocking refusal and grounding gates, and mirrored English and Spanish cases a separate gate
  holds to the same agency and the same required facts. It is beta, and it publishes what it has not
  measured. The Spanish parity gate reads a perfect zero-point gap, and the repository says plainly
  that the gate cannot see answer quality and that none of the 28 Spanish answers has been rated.
- **[ctdl-validate](https://github.com/ChelseaKR/ctdl-validate)** is a deterministic structural
  validator for CTDL JSON-LD, the national credential-data standard, with every finding cited to
  the published schema. It runs as a CLI, as a GitHub Action, and in the browser through
  WebAssembly at a [playground](https://chelseakr.github.io/ctdl-validate/) that uploads nothing.
- **[fhir-scorecard](https://github.com/ChelseaKR/fhir-scorecard)** grades publicly observable FHIR
  R4 endpoints daily on reachability and capability-statement transparency, from public metadata
  and SMART discovery documents alone. It never authenticates and never touches patient data. It is
  early, and it describes its own grades as observational snapshots of public surfaces rather than
  audits, rankings, or statements about anyone's compliance.
- **[disclosed](https://github.com/ChelseaKR/disclosed)** grades US colleges on what they disclose
  rather than on how they perform, because a suppressed measure and a zero are different facts that
  most tools render identically. In a 600-institution College Scorecard sample, 387 publish no
  admission rate at all, and one publishes an admission rate of exactly zero. It has no tagged
  release on purpose, and the
  [decision record](https://github.com/ChelseaKR/disclosed/blob/master/docs/adr/0001-no-versioned-release.md)
  says why: a release pipeline with nothing to release would be exactly the kind of gate that never
  fails.
- **[habitable](https://github.com/ChelseaKR/habitable)** is an alpha tool for tenant unions that
  makes habitability evidence tamper-evident with content hashes and RFC 3161 timestamps, then
  syncs peer to peer under end-to-end encryption so there is no central holder to subpoena. Its own
  README says not to rely on it for real legal matters yet, and I agree with it.

Four more are newer than the rest and all California energy and public-data work.
[`qfer-preflight`](https://github.com/ChelseaKR/qfer-preflight) checks a QFER consumption filing
against the Energy Commission's published rules before anyone uploads it.
[`power-content-check`](https://github.com/ChelseaKR/power-content-check) checks a Power Content
Label against the format Title 20 prescribes, and judges nothing about the power mix on it.
[`ca-tariff-parse`](https://github.com/ChelseaKR/ca-tariff-parse) turns a published electricity
rate schedule into structured data carrying the document, page and line behind every value. And
[`inspected`](https://github.com/ChelseaKR/inspected) asks how much of California's public
wildfire damage-inspection record can be attributed to a published electric service territory,
and answers that 37.9 percent of it cannot, with a confidence interval and no utility ranked.
Each cites the published rule behind every finding and reports what it could not check as
unvalidated rather than as a pass, which is why a spotless QFER filing comes back `UNVALIDATED`
and not `PASS`.

These are independent personal projects, built since June 2026, with no proprietary or client
material in them. AI agents are part of how I work: I choose the architecture, write the acceptance
criteria, review the output, and decide what is ready to release. That is why this much exists in
this little time, and it is the same discipline I would set for a team adopting these tools.

## Background

Most recently I was a Senior Director of Engineering at [Coforma](https://coforma.io), one of three
in a 50-person engineering organization, leading a 22-person reporting structure with five direct
reports including three engineering directors, and owning the company-wide healthcare engineering
portfolio. Nine engineers moved into senior or leadership roles under me, four of them to Director
or Principal.

I was engineering lead and principal engineer for [MyCareer.NJ.gov](https://mycareer.nj.gov), New
Jersey's statewide workforce platform, which has served 1.8 million users since December 2023. I
set architecture across its three production codebases, ran a zero-downtime GCP to AWS migration,
took test coverage from zero to the low nineties, cut known vulnerabilities by 94 percent, shipped
full English and Spanish parity, and did the 2023 CTDL data modeling that began New Jersey's
migration of its training-program registry into the national Credential Engine ecosystem, where
those programs are live today. I also designed the platform's shared applied-AI foundation, which
is in production, and six proof-of-concept features, which stayed gated from end users pending
pilot approval. MyCareer.NJ.gov won the 2026 Labor Market Information Institute award for Best
State LMI Focus on Impact and Sustainability, awarded to the New Jersey Department of Labor.

Before that I built public systems for the California Energy Commission, the California Public
Utilities Commission, the California Department of Social Services, and UC Berkeley's Graduate
School of Education. I hold an M.S. in Software Engineering from CSU Fullerton, earned while
working full time, and a B.S. in Computer Science from the University of Oregon, and I am a
registered member of Credential Engine's CTDL Advisory Group.

## What I will and will not work on

- No weapons, warfare, policing, mass surveillance, or technology that profits from incarceration.
- No AI that decides whether a person gets a job, a benefit, a service, or an opportunity. It can
  support a human decision, as long as that human can inspect the evidence, correct what is wrong,
  and make the final call.
- Accessibility, privacy, security, operability, and multilingual delivery are engineering
  requirements, not a later phase.
- I am not considering federal contracting roles.

## What I am looking for

Engineering leadership roles, VP of Engineering through Director or Principal Engineering Manager,
and independent consulting in the same domains while I search: public health, workforce and social
services, energy and utilities, state and local digital services, and responsible AI. I look for
organizations whose work helps people the public systems routinely fail, and whose leadership
reflects the communities they serve. Current technical center of gravity is TypeScript, Python,
React and Next.js, AWS, PostgreSQL, data interoperability, and applied AI evaluation.

Reach me through [chelseakr.com](https://chelseakr.com) or
[LinkedIn](https://www.linkedin.com/in/chelseakr).
