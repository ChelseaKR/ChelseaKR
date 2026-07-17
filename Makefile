# This is a profile-README repository: the only artifact is Markdown prose.
# `make verify` runs everything that can be checked mechanically here.

.PHONY: verify lint

verify: lint

lint:
	npx --yes markdownlint-cli2@0.18.1
