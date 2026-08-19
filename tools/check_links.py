#!/usr/bin/env python3
"""Fail if a URL in this profile does not resolve for a logged-out visitor.

Why a status code is not enough
-------------------------------
The failure this exists to catch is not a 404. It is a **redirect that returns
200**. GitHub forwards a renamed repository forever, so a link written before a
rename keeps working and keeps showing the old name:

    github.com/ChelseaKR/permit-pathways  ->  github.com/ChelseaKR/permit-bearings
    github.com/ChelseaKR/camino           ->  github.com/ChelseaKR/afterward

Three repositories were renamed in the six weeks before this file was written,
and every stale link to them answered ``200 OK``. A checker that only reads the
status code would have called all three healthy while the profile named
projects that no longer exist under those names. So a redirect that changes the
path on ``github.com`` is a **failure** here, and the message names the target
so the fix is a copy-and-paste.

What this does not do, and why
------------------------------
This is deliberately **unauthenticated**. It sees exactly what a hiring manager
who is not logged in sees: a private or archived-to-private repository answers
404, and that is the result we want, because 404 is what they would get too.

It is the second of two checks, and they cover different failures:

* ``tools/check_repo_names.py`` (``make names``) reads the live repository
  inventory with an authenticated ``gh``. It catches bare project **names** in
  prose with no URL attached, and links to repositories that are public but
  *archived* -- archived repositories still answer 200, so this file cannot see
  them.
* This file (``make links``) needs no credentials and no inventory. It catches
  moved paths, renamed repositories, dead deep links into a repository's files,
  and dead links to sites that are not GitHub at all -- none of which the
  inventory check looks at.

Neither one subsumes the other. Run both; ``make verify`` does.

Hosts that cannot be checked
----------------------------
A few hosts refuse automated requests and answer 404 or 403 to anything that is
not a logged-in browser, for a URL that is perfectly good in a real one. Those
are listed in ``UNCHECKABLE`` with the reason, and are reported by name in the
output as **not checked** rather than folded silently into the pass count. A
check that quietly skipped them would be the thing this repository keeps
writing down that it will not ship: a check that cannot fail.

Usage
-----
``python3 tools/check_links.py`` from the repository root, or ``make links``.
``--timeout`` and ``--workers`` are available for slow networks.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

# A logged-out person reading this profile is using a browser, so ask the way a
# browser asks. Several public-sector sites sit behind a WAF that answers 403 to
# a default library user agent and 200 to this one; mycareer.nj.gov is one.
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

# Hosts that answer automated requests with a status that says nothing about
# whether the URL is good. Each entry is a deliberate, reviewable exemption and
# must carry the reason it is here.
UNCHECKABLE: dict[str, str] = {
    "www.linkedin.com": (
        "LinkedIn answers 404 or 999 to any client that is not a logged-in "
        "browser, including for profiles that resolve fine in one. The status "
        "carries no information, so it is not read as one. Verify this link by "
        "opening it while logged out of LinkedIn."
    ),
    "linkedin.com": "See www.linkedin.com.",
}

URL_RE = re.compile(r"https?://[^\s)<>\]\"'`]+")

# Trailing punctuation that belongs to the sentence, not to the URL.
TRAILING = ".,;:!?'\"`"

GITHUB_HOSTS = {"github.com", "www.github.com"}


@dataclass(frozen=True)
class Site:
    """One URL and every place in the Markdown that writes it."""

    url: str
    where: tuple[str, ...]


@dataclass
class Result:
    site: Site
    status: str  # "ok" | "fail" | "moved" | "notice" | "unchecked"
    detail: str


def repo_root() -> Path:
    return Path(
        subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    )


def markdown_files(root: Path) -> list[Path]:
    tracked = subprocess.run(
        ["git", "ls-files", "*.md", "**/*.md"],
        capture_output=True,
        text=True,
        cwd=root,
        check=True,
    ).stdout.split()
    return sorted({root / p for p in tracked})


def collect(root: Path, files: list[Path]) -> list[Site]:
    """Every distinct URL in the tracked Markdown, with its source lines."""
    found: dict[str, list[str]] = {}
    for path in files:
        rel = path.relative_to(root)
        lines = path.read_text(encoding="utf-8").splitlines()
        for lineno, line in enumerate(lines, start=1):
            for raw in URL_RE.findall(line):
                url = raw.rstrip(TRAILING)
                found.setdefault(url, []).append(f"{rel}:{lineno}")
    return [Site(url, tuple(where)) for url, where in sorted(found.items())]


def canonical(url: str) -> tuple[str, str]:
    """(host, path) with the differences that are not a move flattened away.

    A trailing slash and a ``www.`` prefix are the same page; a different path
    is a different page. Query and fragment are dropped: a fragment never
    reaches the server, and none of the links here carry a meaningful query.
    """
    parts = urlsplit(url)
    host = parts.netloc.lower().removeprefix("www.")
    path = parts.path.rstrip("/")
    return host, path


def fetch(url: str, timeout: float) -> tuple[int, str]:
    """Return (status, final URL) following redirects, or raise."""
    request = urllib.request.Request(
        url,
        method="GET",
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        # Read a little so the connection closes cleanly; the body is not used.
        response.read(2048)
        return response.status, response.geturl()


def check(site: Site, timeout: float) -> Result:
    host = urlsplit(site.url).netloc.lower()
    if host in UNCHECKABLE:
        return Result(site, "unchecked", UNCHECKABLE[host])

    try:
        status, final = fetch(site.url, timeout)
    except urllib.error.HTTPError as exc:
        return Result(site, "fail", f"HTTP {exc.code} {exc.reason}")
    except urllib.error.URLError as exc:
        return Result(site, "fail", f"did not connect: {exc.reason}")
    except Exception as exc:  # noqa: BLE001 - any failure to reach it is a failure
        return Result(site, "fail", f"did not connect: {exc}")

    if status >= 400:
        return Result(site, "fail", f"HTTP {status}")

    if canonical(final) != canonical(site.url):
        moved_on_github = urlsplit(site.url).netloc.lower() in GITHUB_HOSTS
        # A GitHub redirect that changes the path is a rename or a move, and the
        # profile is still printing the old name. That is the bug this catches.
        return Result(
            site,
            "moved" if moved_on_github else "notice",
            f"redirects to {final}",
        )

    return Result(site, "ok", f"HTTP {status}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    root = repo_root()
    files = markdown_files(root)
    sites = collect(root, files)
    if not sites:
        print(
            "check_links: no URLs found in the tracked Markdown. That is not a "
            "pass -- this profile is made of links, so finding none means the "
            "check did not look where it meant to.",
            file=sys.stderr,
        )
        return 1

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda s: check(s, args.timeout), sites))

    by_status: dict[str, list[Result]] = {}
    for result in results:
        by_status.setdefault(result.status, []).append(result)

    def report(results: list[Result], heading: str, stream) -> None:
        if not results:
            return
        print(f"\n{heading}", file=stream)
        for result in sorted(results, key=lambda r: r.site.url):
            print(f"  {result.site.url}", file=stream)
            print(f"    {result.detail}", file=stream)
            print(f"    written at {', '.join(result.site.where)}", file=stream)

    report(
        by_status.get("fail", []),
        "Did not resolve for a logged-out visitor:",
        sys.stderr,
    )
    report(
        by_status.get("moved", []),
        "Moved on GitHub -- the profile is printing a name that no longer "
        "exists. Update the link to the target shown:",
        sys.stderr,
    )
    report(
        by_status.get("notice", []),
        "Resolved, but not at the URL written. Not a failure; worth a look:",
        sys.stdout,
    )
    report(
        by_status.get("unchecked", []),
        "NOT CHECKED -- these hosts refuse automated requests, so this run "
        "says nothing about whether they work. Open them by hand:",
        sys.stdout,
    )

    broken = len(by_status.get("fail", [])) + len(by_status.get("moved", []))
    print(
        f"\ncheck_links: {len(sites)} distinct URL(s) in "
        f"{len(files)} Markdown file(s) -- "
        f"{len(by_status.get('ok', []))} resolved, "
        f"{len(by_status.get('notice', []))} redirected, "
        f"{len(by_status.get('unchecked', []))} not checkable, "
        f"{broken} broken."
    )
    if broken:
        print("check_links: FAIL", file=sys.stderr)
        return 1
    print("check_links: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
