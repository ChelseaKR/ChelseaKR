# This is a profile-README repository: the only artifact is Markdown prose.
# `make verify` runs everything that can be checked mechanically here.

.PHONY: verify lint names

verify: lint names

lint:
	npx --yes markdownlint-cli2@0.18.1

# Fails if any Markdown here names or links a repository that is not public.
# Needs an authenticated `gh`, and fails rather than skipping without one:
# the list of what is public changes outside this repository, so a committed
# copy of it would be the very thing that goes stale.
names:
	python3 tools/check_repo_names.py
