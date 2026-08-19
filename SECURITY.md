# Security policy

This repository contains my GitHub profile README, its supporting
documentation, and two small standard-library Python scripts under `tools/`
that check the prose against reality. It ships no package, has no third-party
dependencies, and runs no deployed service, so there is no conventional
vulnerability surface here. The projects linked from the README each carry
their own `SECURITY.md` with a real threat model — please report code
vulnerabilities to the affected project, not here.

The one thing here that runs on GitHub's infrastructure is
`.github/workflows/verify.yml`. It is `contents: read` only, takes no input
from a pull request, and the only secret it can see is `INVENTORY_TOKEN`,
which needs nothing beyond read access to repository metadata.

## What to report here

- Inaccurate or misleading security claims in the profile text (for example, a
  project described as more hardened or more reviewed than it actually is).
- A link in the README that has started pointing somewhere unexpected or
  malicious (link rot, domain takeover, typosquat).
- Anything in this repository's history that looks like an accidentally
  committed secret or piece of personal data.

## How to report

Email **<ckellyreif@gmail.com>** with `ChelseaKR profile security` in the
subject, or open a public issue on this repository if the problem is not
sensitive (bad links usually are not). Expect an acknowledgement within a few
days; this is a personal repository maintained on volunteer time.
