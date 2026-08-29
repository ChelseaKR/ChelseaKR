#!/usr/bin/env python3
"""Fail if this public profile names a repository that is not public.

Why this exists, and why a link checker is not enough
-----------------------------------------------------
On 2026-08-15 three projects were named in this repository's prose --- in
``CHANGELOG.md`` and ``docs/I18N.md`` --- after their repositories had been made
private. None of the three was a link. A link checker would have found nothing,
because unauthenticated GitHub returns 404 only for a URL, and there was no URL:
the failure was bare project names sitting in sentences.

So this checks two different things, and the second one is the point:

1. Every ``github.com/ChelseaKR/<name>`` link resolves to a repository that is
   public and not archived.
2. No **name** of a non-public repository appears anywhere in the Markdown,
   linked or not, in slug form (``civic-rag-starter-kit``) or in prose form
   (``Civic RAG Starter Kit``).

"Non-public" means private *or* archived. An archived repository is read-only,
and a hiring manager who clicks through to one learns something other than what
the sentence promised.

Fail-closed
-----------
The source of truth is ``gh repo list``, queried live. A committed copy of the
list is exactly the thing that goes stale and causes this bug, so there is not
one. If ``gh`` is missing, unauthenticated, or returns nothing, this exits
non-zero and says so. A check that could not run is not a check that passed.

That last sentence has a second edge, and it is the one that bites in CI. A
token scoped to a single repository -- GitHub Actions' default ``GITHUB_TOKEN``
is one -- can call ``gh repo list`` successfully and get back only the *public*
repositories. Nothing errors. The watchlist of non-public names comes back
empty, every name in the prose passes trivially, and the check reports OK while
having looked for nothing. So an inventory with zero non-public repositories in
it is treated as an inventory that could not be read, not as an account with
nothing to hide. ``--inventory-may-be-public-only`` says otherwise, for the day
that is genuinely true.

Usage
-----
``python3 tools/check_repo_names.py`` from the repository root, or ``make names``.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

OWNER = "ChelseaKR"

# Names that are ordinary English in this repository's subject matter, and so
# cannot be matched as project references without constant false alarms. Each
# one is a real non-public repository; each is listed with the reason its name
# is unusable as a signal. Adding a name here is a deliberate, reviewable act.
TOO_GENERIC = {
    # "My personal site" appears in the changelog as a description, not a repo.
    "personal-site",
    # "portfolio standards sweep" is the name of a work item in the changelog.
    "portfolio-standards",
    # A career profile says "resume" for reasons that have nothing to do with
    # the 2016 LaTeX repository of that name.
    "resume",
    # The repository is ChelseaKR.com; the string is also the live site's
    # domain, which is linked here on purpose.
    "chelseakr.com",
}

# Repositories that are not public but that Chelsea has decided may be named in
# prose anyway, describing the work rather than pointing at a repository. Keep
# this empty unless she has actually made that call for a given project.
NAMEABLE_ANYWAY: set[str] = set()

LINK_RE = re.compile(
    r"github\.com/" + re.escape(OWNER) + r"/([A-Za-z0-9._-]+)",
    re.IGNORECASE,
)


def repo_inventory() -> tuple[set[str], dict[str, str]]:
    """Return (public_and_active, {name: reason-it-is-not-public})."""
    try:
        raw = subprocess.run(
            [
                "gh",
                "repo",
                "list",
                OWNER,
                "--limit",
                "500",
                "--json",
                "name,visibility,isArchived",
            ],
            capture_output=True,
            text=True,
            timeout=120,
            check=True,
        ).stdout
    except FileNotFoundError:
        sys.exit(
            "check_repo_names: `gh` is not installed, so the repository list "
            "could not be read. This is a FAILURE, not a skip: the check that "
            "could not run is not a check that passed."
        )
    except subprocess.CalledProcessError as exc:
        sys.exit(
            "check_repo_names: `gh repo list` failed (is gh authenticated?).\n"
            f"{exc.stderr.strip()}"
        )
    except subprocess.TimeoutExpired:
        sys.exit("check_repo_names: `gh repo list` timed out.")

    repos = json.loads(raw)
    if not repos:
        sys.exit("check_repo_names: `gh repo list` returned no repositories.")

    public: set[str] = set()
    withheld: dict[str, str] = {}
    for repo in repos:
        name = repo["name"]
        archived = repo["isArchived"]
        private = repo["visibility"].upper() != "PUBLIC"
        if private and archived:
            withheld[name] = "private and archived"
        elif private:
            withheld[name] = "private"
        elif archived:
            withheld[name] = "archived, so read-only"
        else:
            public.add(name)
    return public, withheld


def linked_state(slug: str, token: str | None) -> tuple[str, str]:
    """What a logged-out visitor gets for ``github.com/ChelseaKR/<slug>``.

    Asks the public API about one named repository, which needs no credentials.
    A token, when present, is used only to raise the anonymous rate limit --
    never to see more than a stranger would. A repository the token cannot see
    answers 404 either way, which is the answer we want.
    """
    request = urllib.request.Request(
        f"https://api.github.com/repos/{OWNER}/{slug}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": f"{OWNER}-profile-check-repo-names",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.loads(response.read())
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return "missing", "not public (private, renamed, or deleted)"
        if exc.code in (403, 429):
            sys.exit(
                f"check_repo_names: the GitHub API answered {exc.code} for "
                f"{OWNER}/{slug}, which is the anonymous rate limit rather than "
                "an answer about the repository. That is a FAILURE, not a skip: "
                "a check that could not run is not a check that passed."
            )
        return "missing", f"HTTP {exc.code} {exc.reason}"
    except (urllib.error.URLError, TimeoutError) as exc:
        sys.exit(f"check_repo_names: could not reach the GitHub API: {exc}")

    if data.get("archived"):
        return "archived", "archived, so read-only"
    if data.get("private"):
        return "missing", "private"
    full = data.get("full_name", "")
    if full.lower() != f"{OWNER}/{slug}".lower():
        return "renamed", f"renamed; it is now {full}"
    return "public", "public"


def check_links_only(root: Path, files: list[Path]) -> int:
    """Run only the half of this check that needs no privileged inventory.

    ``make names`` has two halves (see the module docstring). The second --
    bare project names in prose -- needs a token that can see private
    repositories, which CI does not have. The first -- every linked repository
    is public and not archived -- needs nothing but the public API, and had
    been skipped along with it. This runs that half, and says plainly that the
    other one did not run rather than reporting a clean pass over both.
    """
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or None
    found: dict[str, list[str]] = {}
    for path in files:
        rel = path.relative_to(root)
        for lineno, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for slug in LINK_RE.findall(line):
                found.setdefault(slug.rstrip(".,);:"), []).append(f"{rel}:{lineno}")

    # Finding no links at all is not a pass. This profile is made of them.
    if not found:
        print(
            f"check_repo_names: no {OWNER} repository links found in "
            f"{len(files)} Markdown file(s). That is not a pass -- this profile "
            "links its projects, so finding none means the file selection is "
            "broken.",
            file=sys.stderr,
        )
        return 1

    failures: list[str] = []
    for slug in sorted(found):
        state, reason = linked_state(slug, token)
        if state != "public":
            for where in found[slug]:
                failures.append(f"{where}: links to {OWNER}/{slug}, which is {reason}")

    if failures:
        print(
            f"check_repo_names: FAIL --- {len(failures)} link(s) to "
            "repositories that are not public and active:\n",
            file=sys.stderr,
        )
        for failure in sorted(set(failures)):
            print(f"  {failure}", file=sys.stderr)
        return 1

    print(
        f"check_repo_names: links OK --- {len(found)} linked {OWNER} "
        f"repositor(y/ies) across {len(files)} Markdown file(s) are public and "
        "not archived."
    )
    print(
        "check_repo_names: NOT CHECKED --- bare project names in prose. That "
        "half needs a token that can see private repositories; set "
        "INVENTORY_TOKEN and drop --links-only to run it. This run says "
        "nothing about it."
    )
    return 0


def prose_pattern(name: str) -> re.Pattern[str]:
    """Match a repo slug and the ways prose writes it.

    ``civic-rag-starter-kit`` also matches ``Civic RAG Starter Kit`` and
    ``civic_rag_starter_kit``. Word boundaries are explicit so that
    ``family-greenhouse`` does not match inside ``family-greenhouse-poc``.
    """
    tokens = [re.escape(t) for t in re.split(r"[-_.\s]+", name) if t]
    joined = r"[-_.\s]*".join(tokens)
    return re.compile(rf"(?<![A-Za-z0-9]){joined}(?![A-Za-z0-9])", re.IGNORECASE)


def markdown_files(root: Path) -> list[Path]:
    tracked = subprocess.run(
        ["git", "ls-files", "*.md", "**/*.md"],
        capture_output=True,
        text=True,
        cwd=root,
        check=True,
    ).stdout.split()
    return sorted({root / p for p in tracked})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--inventory-may-be-public-only",
        action="store_true",
        help=(
            "Accept an inventory containing no non-public repositories. "
            "Without this, an empty watchlist is read as a token that cannot "
            "see private repositories rather than as an account without any."
        ),
    )
    parser.add_argument(
        "--links-only",
        action="store_true",
        help=(
            "Check only that every linked repository is public and not "
            "archived, using the public API and no privileged inventory. "
            "Reports that the bare-name half did not run."
        ),
    )
    args = parser.parse_args()

    root = Path(
        subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    )
    if args.links_only:
        return check_links_only(root, markdown_files(root))

    public, withheld = repo_inventory()
    if not withheld and not args.inventory_may_be_public_only:
        sys.exit(
            "check_repo_names: the inventory came back with "
            f"{len(public)} public repositories and no non-public ones, so "
            "there is nothing to watch for and this check would pass without "
            "looking at anything.\n"
            "That is what a repository-scoped token looks like -- GitHub "
            "Actions' default GITHUB_TOKEN, for instance, lists only public "
            "repositories and reports no error. Authenticate `gh` as an "
            "account that can see the private ones.\n"
            "If every repository really is public now, pass "
            "--inventory-may-be-public-only."
        )
    checked = {
        name: reason
        for name, reason in withheld.items()
        if name.lower() not in TOO_GENERIC and name not in NAMEABLE_ANYWAY
    }
    patterns = {name: prose_pattern(name) for name in checked}

    failures: list[str] = []
    files = markdown_files(root)

    for path in files:
        rel = path.relative_to(root)
        for lineno, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for slug in LINK_RE.findall(line):
                slug = slug.rstrip(".,);:")
                if slug in public:
                    continue
                reason = withheld.get(slug, "not a repository of this owner")
                failures.append(
                    f"{rel}:{lineno}: links to {OWNER}/{slug}, which is {reason}"
                )
            for name, pattern in patterns.items():
                match = pattern.search(line)
                if match:
                    failures.append(
                        f"{rel}:{lineno}: names {name!r} "
                        f"(as {match.group(0)!r}), which is {checked[name]}"
                    )

    if failures:
        print(
            f"check_repo_names: FAIL --- {len(failures)} reference(s) to "
            f"repositories that are not public:\n",
            file=sys.stderr,
        )
        for failure in sorted(set(failures)):
            print(f"  {failure}", file=sys.stderr)
        print(
            "\nEither make the repository public, or remove the reference. If a "
            "name is ordinary English rather than a project reference, add it to "
            "TOO_GENERIC with the reason; if Chelsea has decided a private "
            "project may be described in prose, add it to NAMEABLE_ANYWAY.",
            file=sys.stderr,
        )
        return 1

    print(
        f"check_repo_names: OK --- {len(files)} Markdown file(s) checked "
        f"against {len(public)} public repositories; "
        f"{len(checked)} non-public name(s) watched for."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
