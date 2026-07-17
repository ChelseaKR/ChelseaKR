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

This lints all Markdown in the repository with markdownlint (the same check
the pre-commit hook runs; install it with `pre-commit install`). It must exit
clean.
