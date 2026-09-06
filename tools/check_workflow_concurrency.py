#!/usr/bin/env python3
"""Fail if a workflow that runs on a push to a branch shares one concurrency slot.

The failure this exists to catch
--------------------------------
A ``concurrency`` group holds **one running run and exactly one pending run**. A
third arrival evicts the pending one, and the evicted run never dispatches a
single job. So a group keyed on the ref alone --

    concurrency:
      group: verify-${{ github.ref }}

-- gives *every commit on ``main``* the same slot, because ``github.ref`` is
``refs/heads/main`` for all of them. Push three commits in quick succession and
the middle one is dropped: no jobs, no annotations, no red X. It reads as
``cancelled``, or as simply absent, and **never as a failure**, so nothing
surfaces it and no one goes looking.

``cancel-in-progress`` does not decide whether this happens. It only decides
whether the loss is visible: ``true`` cancels the run the first commit was still
executing, ``false`` silently evicts the second from the pending slot. Both lose
a verdict. This checker therefore says nothing about ``cancel-in-progress`` and
must not be read as endorsing either value.

The fix is to make the key vary per commit on a push while staying per-ref on a
pull request, so that branch supersession -- the thing the group is *for* --
still works:

    group: verify-${{ github.ref }}-${{ github.event_name == 'pull_request' && 'pr' || github.sha }}

What is deliberately out of scope
---------------------------------
* **A workflow with no ``concurrency:`` block at all.** No group means no shared
  slot, so no run can be evicted from one. That is not this defect. If such a
  workflow later gains a ref-only group, this checker sees it then.
* **A push trigger that targets only tags.** Every tag is a unique ref, so a
  ref-only key already gives each release its own slot. This is derived from the
  trigger rather than hard-coded, so a workflow that later adds a branch push
  loses the exemption automatically.
* **Workflows whose answer converges**, listed by name in ``CONVERGING`` with a
  reason. An OpenSSF score is a property of the repository, not of a commit, so
  the newest run is the answer and the run it replaced was not a different one.
  This repository has none; the list is empty and the guard below keeps it
  honest rather than letting an empty list pass for free.

Why this cannot pass by finding nothing
---------------------------------------
Every rule below is vacuous if the sweep returns an empty set -- a glob that
matches nothing, or a trigger filter that excludes everything, would report
success having checked no files. That is the shape of check this repository
keeps writing down that it will not ship. So the sweep asserts it found
``verify.yml`` on a push trigger before any rule runs, and the run fails if it
did not.

Usage
-----
``python3 tools/check_workflow_concurrency.py`` from the repository root, or
``make concurrency``. ``--workflows`` points it at another directory, which is
how the negative control in the pull request that added this file was run.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

#: Workflows that may key on the ref alone because successive runs converge on
#: one answer, as ``{filename: reason}``. Empty here on purpose: this repository
#: runs no such workflow. An entry must still trigger on push, or the guard in
#: ``check`` fails -- an exemption for a workflow that no longer runs is an
#: exemption nobody is checking.
CONVERGING: dict[str, str] = {}

#: The sweep must find these, or it has collapsed and every rule passes for free.
EXPECTED_ON_PUSH = {"verify.yml"}


def top_level_block(text: str, key: str) -> str | None:
    """The body of a top-level ``key:`` mapping, or ``None`` if there is none.

    Anchored at column zero so a ``concurrency:`` nested inside a job -- which is
    a different thing with different consequences -- is never mistaken for the
    workflow-level one this checks.
    """
    match = re.search(
        rf"^{re.escape(key)}:[ \t]*\n((?:[ \t]+[^\n]*\n|[ \t]*\n)*)",
        text,
        re.MULTILINE,
    )
    return match.group(1) if match else None


def push_block(text: str) -> str | None:
    """The body of the ``push:`` trigger, or ``None`` if the workflow has none."""
    on = top_level_block(text, "on")
    if on is None:
        return None
    match = re.search(
        r"^([ \t]+)push:[ \t]*\n((?:\1[ \t]+[^\n]*\n|[ \t]*\n)*)", on, re.MULTILINE
    )
    if match is None:
        # `on: [push, pull_request]` and `on: push` are flow style, not a block.
        return "" if re.search(r"^on:.*\bpush\b", text, re.MULTILINE) else None
    return match.group(2)


def concurrency_group(text: str) -> str | None:
    """The workflow-level concurrency group expression, or ``None``."""
    block = top_level_block(text, "concurrency")
    if block is None:
        return None
    match = re.search(r"^[ \t]*group:[ \t]*(.+?)[ \t]*$", block, re.MULTILINE)
    return match.group(1) if match else None


def pushes_to_a_branch(block: str) -> bool:
    """Whether a ``push:`` trigger can fire for a branch rather than only a tag.

    A bare ``push:`` with no filter fires for every branch, so the absence of a
    ``tags:`` key is the permissive case, not the exempt one.
    """
    has_tags = re.search(r"^[ \t]*tags(-ignore)?:", block, re.MULTILINE) is not None
    has_branches = (
        re.search(r"^[ \t]*branches(-ignore)?:", block, re.MULTILINE) is not None
    )
    return has_branches or not has_tags


def check(workflows: Path) -> int:
    files = sorted(workflows.glob("*.yml")) + sorted(workflows.glob("*.yaml"))
    if not files:
        print(
            f"check_workflow_concurrency: no workflows found under {workflows} -- "
            "refusing to report success having checked nothing",
            file=sys.stderr,
        )
        return 1

    on_push: dict[str, str] = {}
    for path in files:
        text = path.read_text(encoding="utf-8")
        block = push_block(text)
        if block is not None and pushes_to_a_branch(block):
            on_push[path.name] = text

    missing_sweep = EXPECTED_ON_PUSH - set(on_push)
    if missing_sweep:
        print(
            "check_workflow_concurrency: the sweep did not find "
            f"{sorted(missing_sweep)} on a branch push. Either the workflow was "
            "renamed or its trigger changed -- until this list is updated to "
            "match, every rule below would pass by checking nothing.",
            file=sys.stderr,
        )
        return 1

    failures: list[str] = []

    for name, reason in CONVERGING.items():
        if name not in on_push:
            failures.append(
                f"{name} is listed as converging but no longer runs on a branch "
                "push, so the exemption covers nothing"
            )
        elif not reason:
            failures.append(f"{name} is exempt with no reason recorded")

    checked = 0
    for name, text in sorted(on_push.items()):
        if name in CONVERGING:
            continue
        group = concurrency_group(text)
        if group is None:
            # No group, no shared slot. Documented above as out of scope.
            continue
        checked += 1
        if "github.sha" not in group:
            failures.append(
                f"{name} keys its concurrency group on the ref alone "
                f"({group}), so every commit pushed to main competes for one "
                "slot and a burst of merges drops a verdict with no run to show "
                "for it. Append: "
                "-${{ github.event_name == 'pull_request' && 'pr' || github.sha }}"
            )
        elif "pull_request" not in group:
            failures.append(
                f"{name} varies its group per commit but does not keep pull "
                f"requests on a per-ref group ({group}), so two pushes to one "
                "branch would both run instead of the later superseding the "
                "earlier"
            )

    if not checked and not CONVERGING:
        print(
            "check_workflow_concurrency: every push-triggered workflow declares "
            "no concurrency group, so this run asserted nothing. That is a "
            "collapsed sweep, not a pass.",
            file=sys.stderr,
        )
        return 1

    for failure in failures:
        print(f"  FAIL {failure}", file=sys.stderr)

    print(
        f"check_workflow_concurrency: {len(on_push)} workflow(s) run on a branch "
        f"push, {checked} declare a concurrency group, "
        f"{len(CONVERGING)} exempt as converging, {len(failures)} broken."
    )
    if failures:
        print("check_workflow_concurrency: FAIL", file=sys.stderr)
        return 1
    print("check_workflow_concurrency: OK")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--workflows",
        type=Path,
        default=Path(__file__).resolve().parent.parent / ".github" / "workflows",
        help="directory of workflow files to check (default: .github/workflows)",
    )
    args = parser.parse_args()
    return check(args.workflows)


if __name__ == "__main__":
    raise SystemExit(main())
