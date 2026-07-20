# Hi, I'm Chelsea Kelly-Reif 🏳️‍⚧️

![Python][b-py] ![TypeScript][b-ts] ![React][b-react] ![AWS][b-aws] ![PostgreSQL][b-pg]
![Trans rights are human rights][b-trans]

**Senior Director of Engineering. I lead teams, write code, and build public-interest software.**

At [Coforma](https://coforma.io), I lead a 23-person engineering structure with six direct reports,
including engineering managers and directors, and own the company-wide healthcare engineering
portfolio. I also stay hands-on as engineering lead and principal engineer for
[MyCareer.NJ.gov](https://mycareer.nj.gov), a statewide workforce platform available in English and
Spanish and used by about 1.7 million New Jersey residents. I am not bilingual; the language options
describe the service and reviewed translation work. I stay close to architecture, accessibility,
reliability, and the people doing the work.

I've spent the last decade building civic technology. Much of that work is unglamorous but
important: turning policy into software, fixing messy data, making public services accessible, and
keeping them secure and reliable. I also work on open data standards, including CTDL for workforce
credentials and FHIR for health data.

Before Coforma, I built public systems inside California government at the Department of Social
Services, Energy Commission, and Public Utilities Commission, and led application development at
UC Berkeley. I hold an M.S. in Software Engineering from CSU Fullerton, completed while working
full-time in state government, and a B.S. in Computer Science from the University of Oregon.

Based in Davis, California · [Portfolio](https://chelseakr.com) ·
[LinkedIn](https://linkedin.com/in/chelseakr)

> Most projects here are betas or reference implementations. They are not proof of production use
> or adoption. Each README says what works, what does not, and what still needs human review.

Shipped and self-updating — these badges report live state, not claims:
[![tods-validate on PyPI][b-pypi]][l-pypi]
[![GTFS Scorecard Action release][b-action]][l-action]
[![gtfsscorecard.org status][b-site]][l-site]

## Projects worth opening

### Transit data, policy, and public delivery

- **[Transit Delivery Atlas](https://github.com/ChelseaKR/transit-delivery-atlas).** A close,
  source-linked reading of California Executive Order N-7-26. The signed order, my analysis, and
  unanswered questions are kept separate across 21 directive records. It is independent public
  research, not an official implementation or compliance dashboard, and missing evidence does not
  show that work did not occur. [Explore the atlas](https://transit.chelseakr.com).
- **[GTFS Scorecard](https://github.com/ChelseaKR/gtfs-scorecard).** Live beta quality scorecards
  for 1,100+ public GTFS feeds, drawn from a curated registry of 1,600+ feed records concentrated in
  the United States and Canada with reviewed cohorts across Europe, Asia-Pacific, and South America.
  Feed records are not necessarily distinct agencies. It prioritizes rider-facing fixes, scores
  realtime only when a usable feed is configured, and publishes a read API, GitHub Action, and
  read-only MCP server.
  [Visit gtfsscorecard.org](https://gtfsscorecard.org).
- **[tods-validate](https://github.com/ChelseaKR/tods-validate).** A beta TODS 1.0 and 2.1 validator
  for CLI, GitHub Actions, pre-commit, browser, Docker, and language-server workflows. It applies
  conservative auto-fixes and detects TODS references broken by GTFS changes. Some semantic checks
  use 2.1-only mechanisms and are skipped with disclosure for 1.0; the VS Code client is not
  published to a marketplace. It also includes a
  [merged upstream standards correction](https://github.com/MobilityData/transit-operational-data-standard/pull/147).
- **[Fare Policy Assistant](https://github.com/ChelseaKR/fare-policy-assistant).** A reduced-fare
  beta reference assistant for five California transit agencies. It answers from dated sources and
  refuses eligibility decisions and personal information. The repo includes a public 201-case
  white-box benchmark and a separate black-box audit, including missed representational, refusal,
  multilingual, and groundedness thresholds. Manual accessibility review and judge calibration
  remain open. [Review the evaluation surface](https://evals.chelseakr.com/).
- **[NearMiss](https://github.com/ChelseaKR/nearmiss).** A beta road-safety toolkit and public FARS
  evidence atlas. The live atlas presents reviewed 2020–2024 NHTSA fatal-crash counts for all 50
  states and D.C., labeled as burden rather than exposure-normalized risk. Separate local workflows
  use synthetic reports to demonstrate privacy-preserving intake, exposure normalization,
  uncertainty intervals, and hotspot analysis. Manual screen-reader review remains pending.
  [Explore the atlas](https://nearmiss.chelseakr.com).

### Responsible AI and inspectable decisions

- **[Sprout](https://github.com/ChelseaKR/sprout).** An in-build, offline-first plant-care reference
  assistant whose evaluation harness is the headline artifact. It measures groundedness, toxicity
  safety, calibrated uncertainty, and English/Spanish parity; the deterministic public reference
  answers only from a versioned, cited corpus and runs locally in the browser.
- **[constituent-reconciler](https://github.com/ChelseaKR/constituent-reconciler).** An offline-first
  nonprofit record-resolution pipeline with OCR, probabilistic matching, consent-aware exports,
  and a human review gate so uncertain records never merge silently.
- **[outcome-receipts](https://github.com/ChelseaKR/outcome-receipts).** Draft funder reports where
  every figure carries its SQL, row count, data-slice hash, definition, and timestamp. Its offline
  default refuses ungrounded numbers, requires named human approval, and emits verifiable bundles.
  The included small-cell suppression settings are an example policy, not a compliance determination.
- **[Women-Artist Discovery](https://github.com/ChelseaKR/women-artist-discovery).** A beta,
  local-first music recommender that surfaces women (cis and trans — explicitly), nonbinary, and
  female-fronted artists. Identity comes only from cited self-identification sources, never
  inference — a merge-blocking test enforces this — and "unknown" is a first-class answer that
  never down-ranks an artist. Every pick shows its signals, identity basis, and provenance beside
  a live fairness and exposure panel. The public demo runs on a labeled synthetic world; live
  Last.fm orchestration is still deferred.

### Evidence, rights, and community control

- **[ID Churn Sentinel](https://github.com/ChelseaKR/id-churn-sentinel).** Cited, machine-checkable
  change detection for US transgender identity-document law and process. A technical alpha that
  watches 152 registry-claimed government source candidates across all 50 states, D.C., and
  federal agencies; a named human reviews every detected change before publication. None of the
  152 sources is human-verified yet, and the published site says so next to every entry. It
  reports that a page changed — never what the law is.
- **[habitable](https://github.com/ChelseaKR/habitable).** A working alpha reference implementation
  for tenant unions to keep encrypted habitability records with RFC 3161 timestamps, chain of
  custody, peer-to-peer sync, an English and Spanish local web app, and independently verifiable
  packets. There is no central store of tenants' personal data. It has not had an independent
  security or legal review or a real tenant-union pilot, so do not rely on it in a real legal
  matter yet.
- **[ledger](https://github.com/ChelseaKR/ledger).** A private community archive for queer history
  and mutual-aid knowledge. It uses established preservation formats, revocable consent, and
  synthetic identity-leak tests. It has not had an independent security or cryptography audit and
  should not yet hold high-stakes records.

### Climate, environment, community data, and product systems

- **[Swelter](https://github.com/ChelseaKR/swelter).** A maintained reference implementation for
  neighborhood heat and air-quality sensing. Its English and Spanish dashboard shows daily
  Copernicus model data for 337 California cities and provisional readings from physical,
  uncalibrated low-cost sensors in Stuttgart. The pipeline keeps raw and calibrated values separate
  and exports OGC SensorThings data. It is not an established community sensing network, and manual
  accessibility review remains a separate gate.
- **[Davis Bike Hazard Map](https://github.com/ChelseaKR/davis-bike-hazard-map).** A private-beta,
  offline-first cycling-hazard PWA with privacy-preserving photo intake, safer routing, saved-route
  alerts, moderation, and handoff to the city's 311 system.
- **[CEQA Preflight](https://github.com/ChelseaKR/ceqa-preflight).** An early-stage (pre-alpha),
  local-first CLI that checks the technical readiness of CEQA Submit filing packages with
  deterministic, source-cited advisory findings. It never uploads or alters documents and does not
  determine legal sufficiency. NOD- and NOE-specific rules are experimental and opt-in while
  official-source review, practitioner review, and a permissioned pilot complete. It is an
  independent project, not affiliated with the State of California.
- **[ReuseProof CA Core](https://github.com/ChelseaKR/reuseproof-ca-core).** An open-source,
  deterministic evidence-domain core for California onsite treated nonpotable water (OTNWS)
  programs under the 2026 Title 22 regulations. It assembles traceable permit, monitoring, and
  reporting evidence, fails closed on ambiguous or incomplete data, and never makes compliance
  determinations. The public repository ships a synthetic, headless domain foundation only — no
  hosted deployment and no real jurisdiction data.
- **[Family Greenhouse](https://github.com/ChelseaKR/family-greenhouse).** A React and TypeScript
  household plant-care PWA with Capacitor mobile shells and a serverless AWS backend. Commercial
  activity is on hold: it remains a technical demonstration and is not accepting new registrations
  or payments, offering paid plans, conducting launch activity, or doing customer outreach.
- **Personal tools that keep their data local:**
  [Olive Bark Logger](https://github.com/ChelseaKR/olive-bark-logger) and
  [Queer the Stacks](https://github.com/ChelseaKR/queer-the-stacks).
- **My personal site:** [chelseakr.com](https://chelseakr.com) offers an English interface and a
  Spanish translation. I am not bilingual. Accessibility checks run in CI, while manual
  assistive-technology review and external conformance review remain separate human gates.

There is also a [TODS fork](https://github.com/ChelseaKR/transit-operational-data-standard) I use
for upstream standards work. [Browse every public repository](https://github.com/ChelseaKR?tab=repositories).

## What I will and won't work on

- I won't work on weapons or warfare, policing or mass surveillance, or technology that profits
  from incarceration. I also won't work with organizations based in, or strongly tied to, Israel.
- I look for organizations whose work helps people routinely failed by public systems, and whose
  leadership reflects the communities they serve.
- I won't use AI to decide whether someone gets a job, benefit, service, or opportunity. It can
  help a person make a decision, but that person should be able to see the evidence, correct bad
  information, and make the final call.
- I collect as little personal data as I can. I prefer local and offline tools when they are
  practical, and I want people to choose what they share.
- I show sources, calculations, and my own interpretation separately. When a system does not know
  something, it should say so.

## How I build

I spend most days in Python, TypeScript, React, AWS, and data systems. I like clear boundaries,
useful logs, known-answer tests, and checks that stop when they cannot prove the result. Privacy,
accessibility, and operations are part of the first design, not a cleanup pass.

AI agents are part of my development workflow. I choose the architecture, write the acceptance
criteria, review the output, and decide whether it is ready to release. Legal, policy,
subject-matter, and manual accessibility reviews are done by people.

Even my job search is engineered. A private serverless AWS tool polls 500+ organizations' direct
ATS job boards, scores postings against my background with a two-pass Bedrock pipeline gated by a
prompt-injection regression suite, and screens out organizations that conflict with the values
above. It is a personal, single-user tool, and I describe it that way.

## Recognition

MyCareer.NJ.gov, the platform I lead engineering for, has been featured by Fast Company (2024) and
the Royal Statistical Society's Real World Data Science (2024). The Harvard Kennedy School's
Project on Workforce cited its Training Explorer as a "promising potential model" (2023),
Credential Engine features its CTDL credential publishing, and it was a NASWA Workforce Innovation
Award nominee. I spoke on how AI/ML will impact fedtech and civic tech at a Digital Services
Coalition round table (2023).

## What I'm looking for

I'm interested in W-2 engineering people-management roles—VP, Head of Engineering, Director, or
Senior/Principal Engineering Manager—where I can lead people and managers, stay close to the
architecture, and build reliable, accessible public-interest technology. My strongest domains are
energy and utilities, public health, workforce systems, social services, and responsible AI.

Reach me through [chelseakr.com](https://chelseakr.com) or
[LinkedIn](https://linkedin.com/in/chelseakr).

[b-py]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white
[b-ts]: https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white
[b-react]: https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB
[b-aws]: https://img.shields.io/badge/AWS-232F3E?logo=amazonwebservices&logoColor=white
[b-pg]: https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white
[b-trans]: https://img.shields.io/badge/trans_rights-are_human_rights-F5A9B8?labelColor=5BCEFA
[b-pypi]: https://img.shields.io/pypi/v/tods-validate?label=tods-validate
[l-pypi]: https://pypi.org/project/tods-validate/
[b-action]: https://img.shields.io/github/v/release/ChelseaKR/gtfs-scorecard?label=gtfs-scorecard
[l-action]: https://github.com/ChelseaKR/gtfs-scorecard/releases
[b-site]: https://img.shields.io/website?url=https%3A%2F%2Fgtfsscorecard.org&label=gtfsscorecard.org
[l-site]: https://gtfsscorecard.org
