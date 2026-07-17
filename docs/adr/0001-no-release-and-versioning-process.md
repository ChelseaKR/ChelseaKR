# 1. No release-and-versioning process for the profile repository

## Status

Accepted

## Context

The portfolio's Release & Versioning standard expects repositories that ship a
versioned artifact to have tagged releases, a changelog with tag parity, and a
tag-triggered release workflow. This repository is my GitHub profile README:
GitHub renders `README.md` from `main` directly, there is no build step, no
package, no container, and nothing a consumer pins to a version. The
portfolio applicability manifest marks REL as not applicable here for that
reason.

## Decision

Release & Versioning is declared N/A for this repository: no versioned
artifact is released from the profile repository, so we will not add version
tags, a release workflow, or semantic versioning. The `main` branch is the
only "release channel"; `CHANGELOG.md` keeps an `[Unreleased]` section noting
significant content changes, without version headings.

## Consequences

- No release automation to maintain or secure for a repo with nothing to ship.
- If this repository ever starts publishing a versioned artifact (it should
  not), this ADR must be superseded and a real release process added.
