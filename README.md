# Hi, I'm Chelsea Kelly-Reif 🏳️‍⚧️

**Senior Director of Engineering. I lead teams, write code, and build public-interest software.**

At [Coforma](https://coforma.io), I lead a 23-person engineering structure with six direct reports,
including engineering managers and directors, and own the company-wide healthcare engineering
portfolio. I also stay hands-on as engineering lead and principal engineer for
[MyCareer.NJ.gov](https://mycareer.nj.gov), a bilingual statewide workforce platform used by about
1.7 million New Jersey residents. I stay close to architecture, accessibility, reliability, and
the people doing the work.

I've spent the last decade building civic technology. Much of that work is unglamorous but
important: turning policy into software, fixing messy data, making public services accessible, and
keeping them secure and reliable. I also work on open data standards, including CTDL for workforce
credentials and FHIR for health data.

Before Coforma, I built public systems inside California government at the Department of Social
Services, Energy Commission, and Public Utilities Commission, and led application development at
UC Berkeley.

Based in Davis, California · [Portfolio](https://chelseakr.com) ·
[LinkedIn](https://linkedin.com/in/chelseakr)

> Most projects here are betas or reference implementations. They are not proof of production use
> or adoption. Each README says what works, what does not, and what still needs human review.

## Projects worth opening

### Transit data, policy, and public delivery

- **[Transit Delivery Atlas](https://github.com/ChelseaKR/transit-delivery-atlas).** A close,
  source-linked reading of California Executive Order N-7-26. The signed order, my analysis, and
  unanswered questions are kept separate. [Explore the atlas](https://transit.chelseakr.com).
- **[GTFS Scorecard](https://github.com/ChelseaKR/gtfs-scorecard).** Live, plain-language quality
  scorecards for 1,100+ U.S. and Canadian GTFS feeds, with GTFS-Realtime monitoring where available,
  a fail-closed CI gate, and a read-only MCP server. [Visit gtfsscorecard.org](https://gtfsscorecard.org).
- **[tods-validate](https://github.com/ChelseaKR/tods-validate).** A published TODS v1.0–v2.1
  validator for the CLI, GitHub Actions, pre-commit, browser, Docker, and LSP workflows. It includes
  auto-fix, GTFS drift diagnostics, and a
  [merged upstream standards correction](https://github.com/MobilityData/transit-operational-data-standard/pull/147).
- **[Fare Policy Assistant](https://github.com/ChelseaKR/fare-policy-assistant).** A reduced-fare
  reference assistant for five California transit agencies. It answers in English and Spanish,
  cites dated sources, and explains policy without deciding whether someone qualifies. The repo
  includes a public 201-case evaluation and a separate black-box audit.
- **[NearMiss](https://github.com/ChelseaKR/nearmiss).** The live Conflict Atlas combines reviewed
  2020–2024 NHTSA FARS evidence for all 50 states and D.C. with open tools for statistically honest
  road-hazard and near-miss analysis. It normalizes by exposure, reports uncertainty, and uses real
  hotspot statistics instead of treating a heat map as proof.
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
  every figure is reproducible from deterministic SQL and unsupported narrative claims are stopped
  by a fail-closed grounding gate.

### Evidence, rights, and community control

- **[habitable](https://github.com/ChelseaKR/habitable).** A working alpha reference implementation
  for tenant unions to keep encrypted habitability records with RFC 3161 timestamps, chain of
  custody, peer-to-peer sync, a bilingual local web app, and independently verifiable packets.
  There is no central store of tenants' personal data. It has not had an independent security or
  legal review or a real tenant-union pilot, so do not rely on it in a real legal matter yet.
- **[ledger](https://github.com/ChelseaKR/ledger).** A private community archive for queer history
  and mutual-aid knowledge. It uses established preservation formats, and contributors choose what
  is public, community-only, or sealed.

### Climate, community data, and product systems

- **[Swelter](https://github.com/ChelseaKR/swelter).** A maintained reference implementation for
  neighborhood heat and air-quality sensing, with calibration, accessible bilingual maps and
  alerts, and OGC SensorThings export. Its live demo uses current Copernicus data for 337 California
  cities and physical low-cost sensors in Stuttgart, with source and provisional-data limits shown
  on screen.
- **[Davis Bike Hazard Map](https://github.com/ChelseaKR/davis-bike-hazard-map).** A private-beta,
  offline-first cycling-hazard PWA with privacy-preserving photo intake, safer routing, saved-route
  alerts, moderation, and handoff to the city's 311 system.
- **[Family Greenhouse](https://github.com/ChelseaKR/family-greenhouse).** A React and TypeScript
  household plant-care PWA with Capacitor mobile shells and a serverless AWS backend. Commercial
  activity is on hold: it remains a technical demonstration and is not accepting new registrations
  or payments, offering paid plans, conducting launch activity, or doing customer outreach.
- **Personal tools that keep their data local:**
  [Olive Bark Logger](https://github.com/ChelseaKR/olive-bark-logger) and
  [Queer the Stacks](https://github.com/ChelseaKR/queer-the-stacks).
- **This site:** [chelseakr.com](https://chelseakr.com) is bilingual and tests against WCAG 2.2 AAA
  criteria in CI. Manual assistive-technology review and external conformance review remain
  separate human gates.

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

## What I'm looking for

I'm interested in W-2 engineering people-management roles—VP, Head of Engineering, Director, or
Senior/Principal Engineering Manager—where I can lead people and managers, stay close to the
architecture, and build reliable, accessible public-interest technology. My strongest domains are
energy and utilities, public health, workforce systems, social services, and responsible AI.

Reach me through [chelseakr.com](https://chelseakr.com) or
[LinkedIn](https://linkedin.com/in/chelseakr).

## Standards Conformance

My portfolio repositories are developed against a shared set of engineering standards. This
repository is documentation only — a profile README — so most of those standards do not apply
here; they apply (and are declared) in the individual project repositories linked above.

| Standard | Status |
|---|---|
| Responsible-Tech Framework | Applies — the "What I will and won't work on" section above is the load-bearing statement; claims about projects are kept honest and dated |
| Code Quality | N/A — README-only profile repository; no executable source or dependency graph |
| Security & Supply-Chain | N/A — README-only profile repository; no executable or deployable supply-chain surface (reporting channel in [SECURITY.md](SECURITY.md)) |
| CI/CD | N/A — GitHub-rendered profile README; no build, deployment, or versioned artifact |
| Observability | N/A — no runtime service or application surface |
| Accessibility | N/A — no owned HTML surface; content is rendered by GitHub |
| Internationalization | N/A — personal profile content, not a civic/public-service user workflow (see [docs/I18N.md](docs/I18N.md)) |
| AI Evaluation | N/A — no LLM/model component |
| Documentation | Applies — this README, [CHANGELOG.md](CHANGELOG.md), [SECURITY.md](SECURITY.md), and the ADR log in [docs/adr/](docs/adr/) |
| Quality & Metrics | N/A — no executable product or service metrics |
| Release & Versioning | N/A — no versioned artifact is released from the profile repository (see [ADR 0001](docs/adr/0001-no-release-and-versioning-process.md)) |

CITATION.cff — N/A (profile README; nothing citable). Prose checks run via `make verify`
(markdownlint) and the matching pre-commit hook.
