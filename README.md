### Hi, I'm Chelsea 🏳️‍⚧️

I build public-interest technology for people who need systems to be legible, trustworthy, and usable under real constraints. My work spans open standards, transit data, community evidence, environmental sensing, and nonprofit infrastructure.

Across those domains, I use the same engineering discipline: verifiable claims instead of green-checkmark theater, accessibility (WCAG 2.2) as a baseline, privacy-by-design for sensitive data, and explicit limits on what a system proves.

Based in Davis, CA. Site: [chelseakr.com](https://chelseakr.com) · [LinkedIn](https://linkedin.com/in/chelseakr)

---

#### Open-source standards work

- **[Transit Operational Data Standard](https://github.com/MobilityData/transit-operational-data-standard)** — Contributor to the open standard; author of the independent **[tods-validate](https://github.com/ChelseaKR/tods-validate)** validator, spanning TODS v1.0.0–v2.1.0 and released as a CLI, GitHub Action, pre-commit hook, browser playground, VS Code client, and Docker image.

#### Transit, mobility & safe streets

- **[gtfs-scorecard](https://github.com/ChelseaKR/gtfs-scorecard)** — Live, plain-language GTFS and GTFS-Realtime quality scorecards for 1,100+ US and Canadian feeds, backed by the MobilityData validator and a fail-closed CI gate. [Visit gtfsscorecard.org](https://gtfsscorecard.org).
- **[nearmiss](https://github.com/ChelseaKR/nearmiss)** — Open road-hazard dataset and reproducible safe-streets analysis using exposure-normalized rates, confidence intervals, and benchmark-validated hotspot statistics, with multi-source ingestion (BikeMaps, SimRa) and a QGIS plugin.
- **[fare-policy-assistant](https://github.com/ChelseaKR/fare-policy-assistant)** — Bilingual EN/ES California reduced-fare assistant that answers only from dated, cited sources, with a public 201-case, nine-suite evaluation harness for groundedness, refusal, and multilingual parity.
- **[davis-bike-hazard-map](https://github.com/ChelseaKR/davis-bike-hazard-map)** — Private-beta, offline-first cycling-hazard PWA with privacy-preserving photo intake, safer routing, push alerts on saved routes, moderation, and handoff to the city's 311 system (Open311/GOGov).

#### Trustworthy civic AI & data systems

- **[constituent-reconciler](https://github.com/ChelseaKR/constituent-reconciler)** — Offline-first nonprofit record-resolution pipeline with OCR, probabilistic matching, a human review gate, consent-aware CiviCRM, Salesforce, and webhook export, a VAWA/FVPSA domestic-violence privacy pack, Docker self-host, and tamper-evident provenance.
- **[outcome-receipts](https://github.com/ChelseaKR/outcome-receipts)** — Funder reports where every figure is reproducible from deterministic SQL and unsupported narrative claims are stopped by a fail-closed grounding gate, with accessible bilingual EN/ES charts and a Sigstore-signed, tamper-evident export bundle.

#### Community memory, evidence & environmental justice

- **[ledger](https://github.com/ChelseaKR/ledger)** — Privacy-first archive for queer histories and mutual-aid knowledge, using BagIt, PREMIS, Dublin Core, fixity audits, encrypted replication, OAI-PMH/METS interoperability, and consent-based selective disclosure.
- **[habitable](https://github.com/ChelseaKR/habitable)** — Alpha, local-first habitability-evidence system for tenant unions with end-to-end encryption, RFC 3161 timestamps, hash-linked chain of custody, peer-to-peer sync, reproducible Sigstore-attested builds, and independently verifiable packets.
- **[swelter](https://github.com/ChelseaKR/swelter)** — Open-source reference implementation, replicable by any neighborhood, for community heat and air-quality sensing, with calibration, accessible bilingual maps and alerts, real-world demo data, and OGC SensorThings export.
- **[olive-bark-logger](https://github.com/ChelseaKR/olive-bark-logger)** — On-device noise monitor with rigorous sensor calibration that records sound-level events but never audio, runs offline on Raspberry Pi or in a browser, and produces accessible evidence reports.

#### Personal systems & infrastructure

- **[personal-site](https://github.com/ChelseaKR/personal-site)** — Live bilingual portfolio and consulting-services site with WCAG 2.2 AAA checks, static prerendering, cookieless analytics, and a serverless AWS Bedrock chat backend.
- **[family-greenhouse](https://github.com/ChelseaKR/family-greenhouse)** — Released household plant-care app (React/TypeScript PWA plus native iOS/Android) with shared schedules and care history, multimodal reminders, photo-based plant identification, Stripe subscription tiers, a public API, and a serverless AWS architecture.

---

#### How I build

I use AI agents as implementation collaborators inside a process I design and own: architecture, standards, threat models, evaluations, acceptance criteria, and release decisions. The repositories are built against a self-authored standards corpus covering accessibility, privacy, security, and honesty in claims. Work that needs legal, policy, subject-matter, or manual accessibility review is gated and labeled rather than presented as independently certified.

Most of this independent portfolio has been built in public since June 2026. Each repository states its maturity, evidence, known limits, and what remains before production use.
