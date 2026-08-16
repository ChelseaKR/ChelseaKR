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

This runs two checks, and both must exit clean:

- `make lint` lints all Markdown with markdownlint (the same check the
  pre-commit hook runs; install it with `pre-commit install`).
- `make names` fails if any Markdown here names or links one of my
  repositories that is not public. It reads the live list from `gh repo list`,
  so it needs an authenticated `gh`, and it fails rather than skips without
  one. It catches bare project names in prose, not just links, because that is
  how this has actually gone wrong.
