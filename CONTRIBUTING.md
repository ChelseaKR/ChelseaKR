# Contributing

This is my personal GitHub profile README, so its content is not open to
contribution in the usual sense — the words here are mine. That said,
corrections are very welcome: a broken or hijacked link, a project description
that has drifted out of date, a typo, or a claim that no longer matches the
linked repository.

## How

- Open an issue, or a small PR against `main`, describing what is wrong.
- For anything security-flavored (bad links, leaked data), see
  [SECURITY.md](SECURITY.md).

## Checks

Before pushing, run:

```sh
make verify
```

This runs three checks, and all three must exit clean:

- `make lint` lints all Markdown with markdownlint (the same check the
  pre-commit hook runs; install it with `pre-commit install`).
- `make links` fails if a URL here does not resolve for a logged-out visitor,
  or resolves somewhere other than where it says. It is unauthenticated on
  purpose, so that it sees what a stranger sees. A renamed repository is the
  case it exists for: GitHub forwards the old name forever and answers `200`,
  so a stale link passes a status-only check while the profile keeps printing a
  name that no longer exists.
- `make names` fails if any Markdown here names or links one of my
  repositories that is not public. It reads the live list from `gh repo list`,
  so it needs an authenticated `gh`, and it fails rather than skips without
  one. It catches bare project names in prose, not just links, because that is
  how this has actually gone wrong.

`make lint` and `make links` also run in CI on every pull request and once a
week, because most of what goes wrong here goes wrong without anyone touching
this repository. `make names` needs credentials CI does not have by default; if
an `INVENTORY_TOKEN` secret is not configured, the workflow says out loud that
it did not run rather than reporting a pass.

## License

This repository holds two kinds of work, and they are licensed separately:

- The profile prose — `README.md`, `CHANGELOG.md`, this file, `SECURITY.md`,
  and everything under `docs/` — is
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), in `LICENSE`.
  Quote it or adapt it; keep the attribution.
- The checkers under `tools/` are [Apache-2.0](tools/LICENSE), the same license
  the rest of my portfolio uses for code. If your own profile README keeps
  printing repository names after a rename, take them.

The reasoning is in
[ADR 0003](docs/adr/0003-licensing-splits-prose-from-tools.md). A contribution
is offered under whichever of the two covers the file it touches.
