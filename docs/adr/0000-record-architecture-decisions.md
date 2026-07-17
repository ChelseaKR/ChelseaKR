# 0. Record architecture decisions

## Status

Accepted

## Context

This repository is my GitHub profile README. It makes few decisions, but the
ones it does make — what the profile claims about my projects, which standards
apply to a documentation-only repository, and why — should not live only in PR
threads. The portfolio-wide conformance tooling also expects each repository to
carry its own decision log rather than pointing at another repo's.

## Decision

We will record architecture decisions in **Architecture Decision Records
(ADRs)** using the format described by Michael Nygard.

- Each ADR is a short Markdown file in `docs/adr/`, numbered sequentially and
  named `NNNN-title-in-kebab-case.md`.
- Each ADR has the sections **Title**, **Status**, **Context**, **Decision**,
  and **Consequences**.
- **Status** is one of *Proposed*, *Accepted*, *Deprecated*, or *Superseded*.
  A superseded ADR is not deleted; it is marked superseded and points to the
  ADR that replaces it, and the replacement points back.
- ADRs are immutable once accepted, except to change their status. A new
  decision is a new ADR, not an edit to an old one.

## Consequences

- The reasoning behind repository-level decisions (like which standards this
  repo declares N/A) is preserved and versioned next to the content it
  governs.
- Given the scope of this repository, the log is expected to stay very small.
