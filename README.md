# Hi, I'm Chelsea Kelly-Reif 🏳️‍⚧️

![Python][b-py] ![TypeScript][b-ts] ![React][b-react] ![AWS][b-aws] ![PostgreSQL][b-pg]
![Public systems engineering leadership][b-public-systems]
![Accessibility built in][b-accessibility] ![AI evidence and human review][b-ai-review]
![Open to engineering leadership and consulting][b-open-to] ![Trans rights are human rights][b-trans]

**Engineering leader for public systems. I build teams, portfolios, and the technical foundations
those teams need to deliver.**

Most recently, I was a Senior Director of Engineering at [Coforma](https://coforma.io) and one of
three Senior Directors in its 50-person engineering organization. I led a 22-person reporting
structure with five direct reports, including three engineering directors. I owned the company-wide
healthcare engineering portfolio and served as engineering lead for business development.

That work stayed close to outcomes:

- Nine engineers moved into senior or leadership roles, including four promotions to Director or
  Principal. My teams had three voluntary departures across three years.
- I owned engineering for the seven-application CMS Medicaid & CHIP Data Collection Tools suite,
  oversaw Coforma's work on the federal Medicaid Drug Programs system, and led the firm's FHIR and
  health data interoperability specialization.
- I was engineering lead and principal engineer for
  [MyCareer.NJ.gov](https://mycareer.nj.gov), New Jersey's statewide workforce platform. It has
  served 1.8 million users since December 2023 and provides bilingual career, training, labor-market,
  tuition-assistance, and support-service tools.

On MyCareer.NJ.gov, I led the platform and set architecture across its three production codebases.
The work included a zero-downtime GCP-to-AWS migration, test coverage raised from zero to 93–96%, a
94% reduction in known vulnerabilities, complete English and Spanish access, and the 2023 CTDL
data modeling that began New Jersey's migration of its training program registry into the national
Credential Engine ecosystem, where those programs are live today.

I also designed its shared applied-AI foundation and six primary proof-of-concept features. The
foundation is now live in production; the features remained gated from end users pending pilot
approval. The most mature was a bilingual, grounded career coach with cost-aware model routing, a
merge-blocking adversarial test gate, and evaluation designed to expose weak categories rather than
hide them. The 1.8 million-user count above applies to the production platform; the AI features were
proofs of concept, not deployed services.

Before Coforma, I built public systems in California state government and public higher education:

- At the **California Energy Commission**, I led development of regulatory energy-data systems,
  helped move the commission's data infrastructure to AWS, and operated the Title 20 appliance
  certification system.
- At the **California Public Utilities Commission**, I directed the Transportation Carrier Portal,
  which launched in 2021, and architected a claims portal for telecommunications-access and
  broadband programs.
- At the **California Department of Social Services**, I built and operated caregiver-safety,
  licensing-payment, legislative-analysis, and benefits-program systems.
- At **UC Berkeley's Graduate School of Education**, I led application development for the
  equity-focused 21st Century California School Leadership Academy.

I hold an M.S. in Software Engineering from CSU Fullerton, which I completed while working
full-time. I also hold a B.S. in Computer Science from the University of Oregon
and an ITIL Foundation certification.

Based in Davis, California · [Portfolio](https://chelseakr.com) ·
[LinkedIn](https://linkedin.com/in/chelseakr)

## Open source worth opening

These independent projects are public and inspectable. They date from June 2026 onward, when I
began building this portfolio in the open, and I have been working on it close to full time since.
AI agents are part of that workflow: I choose the architecture, write the acceptance criteria,
review the output, and decide whether it is ready to release. That is how this much exists in this
little time, and it is the same discipline I would set for a team adopting these tools.

Most of what follows is a pre-1.0 tool or reference implementation, not evidence of organizational
adoption. Each repository documents what has shipped, what remains experimental, and what still
requires human review. Where someone outside a project has changed its direction, I have said so.

- **[tods-validate](https://github.com/ChelseaKR/tods-validate)** is a deterministic validator for
  the Transit Operational Data Standard. Version 0.8.0 is on PyPI, and the project ships a GitHub
  Action, container image, pre-commit hook, and
  [browser playground](https://chelseakr.github.io/tods-validate/).
- **[GTFS Scorecard](https://github.com/ChelseaKR/gtfs-scorecard)** (live at
  [gtfsscorecard.org](https://gtfsscorecard.org)) publishes daily, plain-language transit-data
  quality grades across a curated registry of more than 2,100 feed records; its status page reports
  the exact current counts. It does not reimplement GTFS validation: correctness findings come from
  MobilityData's canonical validator, and this project adds freshness, completeness, and
  prioritized fixes on top. **Unitrans** (UC Davis / City of Davis) and **Yolobus** (Yolo County
  Transportation District) are running a 90-day pilot of the remediation workflow. It also ships a
  GitHub Marketplace Action and a read-only MCP server.
- **[ctdl-validate](https://github.com/ChelseaKR/ctdl-validate)** is a deterministic structural
  validator for CTDL JSON-LD, the national credential-data standard: CTID grammar, identifier
  kinds, reference resolution, domain and range, and inverse consistency, with every finding
  cited to the published schema.
- **[disclosed](https://github.com/ChelseaKR/disclosed)** grades US higher-education institutions
  on what they disclose rather than how they perform, across the complete 6,163-institution IPEDS
  directory and a 600-institution College Scorecard sample, with applicability rules that keep
  denominators honest.
- **[fhir-scorecard](https://github.com/ChelseaKR/fhir-scorecard)** grades payer FHIR discovery
  endpoints daily under the CMS interoperability rules, every finding citing the specification
  text or the stated convention it applies, drift tracked between runs. Unauthenticated surfaces
  only, never patient data.
- **[Afterward](https://github.com/ChelseaKR/afterward)** (formerly Camino, live at
  [afterward.chelseakr.com](https://afterward.chelseakr.com)) joins 3,266 California training
  programs to their federally reported outcomes and the state's occupation and wage projections,
  built entirely from public data. More than a third publish no outcome data, and the site says so
  rather than rendering an absence as a zero. No account, no tracking, English and Spanish from
  the first release.
- **[NearMiss](https://github.com/ChelseaKR/nearmiss)** is a beta road-safety analysis toolkit that
  uses exposure-normalized rates, confidence intervals, and statistically controlled hotspot
  detection instead of treating raw report density as risk.
- **[Swelter](https://github.com/ChelseaKR/swelter)** ([live demo](https://chelseakr.github.io/swelter/),
  refreshed daily on real data) is a beta reference system for community heat and air quality,
  with correction provenance, a bilingual dashboard, and OGC SensorThings exports.
- **[ledger](https://github.com/ChelseaKR/ledger)** is a beta, privacy-first digital-preservation
  tool using BagIt, PREMIS, Dublin Core, encrypted contributor identities, and consent-based
  disclosure. It contains synthetic and consented fixtures only.
- **[outcome-receipts](https://github.com/ChelseaKR/outcome-receipts)** is a beta tool for
  nonprofit funder reports where every figure carries a receipt: a deterministic query, a
  data-slice hash, and a fail-closed grounding gate that blocks export if a number cannot be
  traced to evidence.
- **[habitable](https://github.com/ChelseaKR/habitable)** is an alpha, offline-first tool for
  tenant unions that makes habitability evidence tamper-evident with content hashes and RFC 3161
  timestamps, then syncs peer-to-peer over an end-to-end-encrypted CRDT; an optional relay only
  ever carries ciphertext.

### What outside review has changed

These projects have few stars. What they have instead is a record of being corrected in public:

- **Scope.** [Jannis (derhuerst)](https://github.com/derhuerst), a longtime open transit-data
  maintainer, [argued](https://github.com/ChelseaKR/gtfs-scorecard/issues/194) that GTFS
  Scorecard's scoring belonged in MobilityData's canonical validator rather than in yet another
  dashboard. He was substantially right. I surveyed the closest existing tools, kept the canonical
  validator as the correctness engine, declined to push subjective letter grades into an official
  project where they would look like guidance, de-emphasized the overlapping dashboard features,
  and narrowed this project to the handoff nobody else covers: a named fix request, a comparable
  recheck of the same published feed, and reproducible closure evidence.
- **Scoring.** The producer of the MRC de Joliette feed
  [pushed back](https://github.com/ChelseaKR/gtfs-scorecard/issues/180) on a recommendation to
  populate `trip_headsign` on loop routes. They were right: GTFS Best Practices discourage
  repeating the route name, and the twelve blank headsigns in that feed were all single-pattern
  frequency templates. I changed the rule so that verifiable case is credited instead of flagged.

Upstream, I have merged a specification example fix into
[MobilityData's TODS](https://github.com/MobilityData/transit-operational-data-standard/pull/147)
and an entry into [awesome-transit](https://github.com/MobilityData/awesome-transit/pull/387), with
a [conformance-language clarification](https://github.com/MobilityData/transit-operational-data-standard/pull/156)
and a [Transitland feed-archival PR](https://github.com/transitland/transitland-atlas/pull/2098)
still open.

## How I lead and build

I lead at portfolio altitude and stay technically deep: I set architecture, challenge assumptions,
and understand delivery risk. Grit is not a staffing model: I build clear ownership, strong
managers, useful standards, and systems that do not depend on one heroic person.

My current technical center of gravity is TypeScript, Python, React and Next.js, AWS, PostgreSQL,
data interoperability, applied AI evaluation, and delivery systems. Earlier work also spans C# and
.NET, Salesforce, Snowflake, Azure, GCP, and Natural/ADABAS modernization.

I treat accessibility, privacy, security, operability, and multilingual delivery as engineering
requirements. For AI systems, that means evidence-constrained generation, explicit refusal,
adversarial testing, disaggregated evaluation, cost controls, feature flags, and human review for
legal, policy, subject-matter, and accessibility judgments.

## What I will and won't work on

- I won't work on weapons, warfare, policing, mass surveillance, or technology that profits from
  incarceration.
- I look for organizations whose work helps people routinely failed by public systems, and whose
  leadership reflects the communities they serve.
- I won't use AI to decide whether someone gets a job, benefit, service, or opportunity. It can
  support a person's decision, but that person should be able to inspect the evidence, correct bad
  information, and make the final call.
- I collect as little personal data as practical and prefer local or offline tools when they fit.
- I separate sources, calculations, and interpretation. When a system does not know, it should say
  so.

## Selected coverage and recognition

In 2026, the Labor Market Information Institute gave NJDOL its Best State LMI Focus on Impact and
Sustainability award for the department's evidence-based approach and MyCareer.NJ.gov. The
platform has been featured by Fast Company and the Royal Statistical Society's Real World Data
Science. The Harvard Kennedy School's Project on Workforce described its Training Explorer as a
"promising potential model," and Credential Engine has featured its CTDL publishing work. The
platform was also nominated for a NASWA Workforce Innovation Award. I was a registered member of
Credential Engine's CTDL Advisory Group from January 2025 to July 2026, and in 2023 I joined a
Digital Services Coalition roundtable on AI and machine learning in federal and civic technology.

## What I'm looking for

I'm interested in engineering leadership roles (VP of Engineering, Head of Engineering, Senior
Director, Director, or Principal Engineering Manager) and independent consulting engagements in
the same domains while I search. I want to lead teams and managers, shape
architecture and delivery systems, and build reliable, accessible technology in public health,
workforce and social services, energy and utilities, government digital services, or responsible
AI.

Reach me at [chelseakr.com](https://chelseakr.com) or on
[LinkedIn](https://linkedin.com/in/chelseakr).

[b-py]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white
[b-ts]: https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white
[b-react]: https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB
[b-aws]: https://img.shields.io/badge/AWS-232F3E?logo=amazonwebservices&logoColor=white
[b-pg]: https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white
[b-public-systems]: https://img.shields.io/badge/public_systems-engineering_leadership-0F766E
[b-accessibility]: https://img.shields.io/badge/accessibility-built_in-2563EB
[b-ai-review]: https://img.shields.io/badge/AI-evidence_%2B_human_review-7C3AED
[b-open-to]: https://img.shields.io/badge/open_to-engineering_leadership_%2B_consulting-0A7D39
[b-trans]: https://img.shields.io/badge/trans_rights-are_human_rights-F5A9B8?labelColor=5BCEFA
