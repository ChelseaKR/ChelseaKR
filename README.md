# Hi, I'm Chelsea 🏳️‍⚧️

I'm a public-interest software engineer building trustworthy data systems for transit agencies, nonprofits, and communities, mainly in Python and TypeScript.

I design for real constraints: accessible interfaces, privacy by design, reproducible evidence, fail-closed checks, and explicit limits on what a system can prove.

Based in Davis, California · [Portfolio & consulting](https://chelseakr.com) · [LinkedIn](https://linkedin.com/in/chelseakr)

## Selected work

> This independent R&D portfolio began in June 2026. Unless marked otherwise, projects are pre-1.0 beta or reference implementations; each repository documents its evidence, known limits, and review or deployment gates.

### Open standards, transit & safe streets

- **[tods-validate](https://github.com/ChelseaKR/tods-validate)** — [TODS](https://github.com/MobilityData/transit-operational-data-standard) v1.0.0–v2.1.0 validator for command-line, GitHub Actions, pre-commit, browser, and Docker workflows, with LSP support. I also contributed a [merged fix](https://github.com/MobilityData/transit-operational-data-standard/pull/147) upstream.
- **[gtfs-scorecard](https://github.com/ChelseaKR/gtfs-scorecard)** — Live beta with plain-language quality scorecards for 1,100+ U.S. and Canadian GTFS feeds and GTFS-Realtime monitoring where available, powered by MobilityData's validator and a fail-closed CI gate. [Visit gtfsscorecard.org](https://gtfsscorecard.org).
- **[nearmiss](https://github.com/ChelseaKR/nearmiss)** — Reference implementation for reproducible road-hazard analysis, demonstrated with synthetic Davis and Riverside data and known-answer hotspot benchmarks; includes multi-source ingestion and a QGIS plugin.
- **[fare-policy-assistant](https://github.com/ChelseaKR/fare-policy-assistant)** — California reduced-fare reference assistant designed to answer in EN/ES from dated, cited sources, with a public 201-case evaluation across nine suites.
- **[davis-bike-hazard-map](https://github.com/ChelseaKR/davis-bike-hazard-map)** — Private-beta, offline-first hazard reporting and safer routing for Davis cyclists, with privacy-preserving photos, saved-route alerts, moderation, and Open311/GOGov handoff.

### Trustworthy civic data & AI

- **[constituent-reconciler](https://github.com/ChelseaKR/constituent-reconciler)** — Offline-first nonprofit record resolution with OCR, probabilistic matching, human review, consent-aware exports, a VAWA/FVPSA privacy pack, and tamper-evident provenance.
- **[outcome-receipts](https://github.com/ChelseaKR/outcome-receipts)** — Reproducible funder reporting: deterministic SQL backs every figure, and a fail-closed grounding gate blocks unreceipted numeric claims. Bilingual exports support keyed signing and a hash-chained ledger; releases carry Sigstore provenance.

### Community evidence & environmental justice

- **[ledger](https://github.com/ChelseaKR/ledger)** — Privacy-first preservation for queer histories and mutual-aid knowledge, using open archival standards, fixity audits, encrypted replication, and consent-based selective disclosure.
- **[habitable](https://github.com/ChelseaKR/habitable)** — Alpha, local-first evidence system for tenant unions, with end-to-end encryption, RFC 3161 timestamps, hash-linked chain of custody, peer-to-peer sync, reproducible builds, and independently verifiable packets.
- **[swelter](https://github.com/ChelseaKR/swelter)** — Replicable open-source reference implementation for neighborhood heat and air-quality sensing, with calibration tooling, accessible bilingual maps and alerts, clearly labeled real-data demos, and OGC SensorThings export.
- **[olive-bark-logger](https://github.com/ChelseaKR/olive-bark-logger)** — Offline noise monitor for Raspberry Pi and the browser, with reference-offset calibration and documented provenance; it records sound-level events—never audio—and produces accessible evidence reports.

### Personal software & infrastructure

- **[personal-site](https://github.com/ChelseaKR/personal-site)** — Live bilingual portfolio and consulting site with static prerendering, WCAG 2.2 AAA checks, cookieless analytics, and a serverless AWS Bedrock chat backend.
- **[queer-the-stacks](https://github.com/ChelseaKR/queer-the-stacks)** — Private-by-design reading dashboard and explainable recommender for Calibre and KOReader, with self-hosting, diverse-shelf analytics, and shareable progress cards.
- **[family-greenhouse](https://github.com/ChelseaKR/family-greenhouse)** — Pre-1.0 React/TypeScript plant-care PWA with a [live web demo](https://familygreenhouse.net), shared schedules and history, reminders, an implemented serverless AWS backend, and buildable Capacitor mobile shells that are not yet store-released.

## How I build

I use AI agents as implementation collaborators while retaining responsibility for architecture, standards, threat models, evaluations, acceptance criteria, and release decisions. Legal, policy, subject-matter, and manual accessibility reviews remain human gates and are labeled when pending.
