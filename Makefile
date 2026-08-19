# This is a profile-README repository: the only artifact is Markdown prose.
# `make verify` runs everything that can be checked mechanically here.

.PHONY: verify lint names links

verify: lint links names

lint:
	npx --yes markdownlint-cli2@0.18.1

# Fails if any Markdown here names or links a repository that is not public.
# Needs an authenticated `gh`, and fails rather than skipping without one:
# the list of what is public changes outside this repository, so a committed
# copy of it would be the very thing that goes stale.
names:
	python3 tools/check_repo_names.py

# Fails if a URL here does not resolve for a logged-out visitor, or resolves
# somewhere other than where it says. Needs no credentials, on purpose: it is
# meant to see what a stranger sees. A GitHub redirect that changes the path is
# a renamed repository, which answers 200 and so passes a status-only check --
# that is the failure this exists to catch.
links:
	python3 tools/check_links.py
