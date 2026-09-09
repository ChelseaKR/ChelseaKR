# The confident zero

*A defect class, with receipts. Every instance below is in one of my own public repositories,
and every one is checkable by clicking through.*

**A claim that cannot come out differently is not a measurement.**

That is the whole thesis, and this page is the evidence for it. Over the last three weeks I
found the same defect in repository after repository, in code I had written, reviewed and
believed. It has one shape:

> A read that did not happen, a value that was suppressed, a fetch that failed, or a set that
> was never populated, published as if it were a measurement.

I have been calling it **absence rendered as a value**. The reason it survives review is that
its output is *well formed*. It is not a crash, a null, or a stack trace. It is a percentage,
a `PASS`, an exit code of `0`, a 95% confidence interval — the exact shape the honest answer
would take, indistinguishable from it at every point downstream.

The diagnosis is not new. "Null is not zero" and "absence of evidence is not evidence of
absence" are old sayings. What is worth publishing is not the saying; it is the collection of
real instances underneath it, and what actually found them.

## Nine receipts

### 1. A shred gate that authorised destruction on the strength of an empty check

[`ledger`](https://github.com/ChelseaKR/ledger) is a digital preservation system for a
community archive. It has a lockdown mode for a raid or a seizure, and one of the things
lockdown can do is shred the local identity vault — the file that could out contributors if
the disk were taken. That is irreversible, so the module's own docstring stated the safety
property in terms:

> Shredding is disabled unless `verify_backup_location` confirms at least
> `min_verified_replicas` of the configured off-box replica locations restore clean.

`verify_backup_location` ended like this:

```python
bags = tuple(BagFixity(name, report.ok, report.checked) for name, report in reports)
all_ok = all(bag.ok for bag in bags)
return BackupVerification(str(backup), ok=all_ok, reason="" if all_ok else "fixity-failed", ...)
```

`all([])` is `True`. A replica holding a config file and a vault file but **none of the
archive's content** audited zero bags, took the `True` branch, and came back `ok=True` with
an empty reason string — because there was no failure to report. The gate that exists to
prove the archive survived was satisfied by a replica that proved nothing, and therefore
authorised the shred. The module's current docstring puts it in exactly those terms: a partial
rsync, an emptied replica disk, or a copy that stopped after the metadata *"read as 'your
archive survived' and authorised the destruction of the only real copy."*

The safety property the module documented was not enforced by the code implementing it.
The fix is [pull request 207](https://github.com/ChelseaKR/ledger/pull/207), commit
[`b7d5fe3`](https://github.com/ChelseaKR/ledger/commit/b7d5fe3), with a three-state
`FixityStatus` rather than a flipped boolean: `verified`, `failed`, and `could-not-verify`.
"Your replica is empty" and "your replica is corrupt" call for opposite responses, so they
are now different reason codes.
[`src/ledger/lockdown.py`](https://github.com/ChelseaKR/ledger/blob/main/src/ledger/lockdown.py)
carries the whole account in its docstring, including the sentence I would keep if I could
keep only one: *the explicit `not bags` is the whole defect in miniature.*

### 2. A published 95% confidence interval that was actually 68%

[`mrf-honest`](https://github.com/ChelseaKR/mrf-honest) grades hospital price-transparency
files and publishes a Wilson interval beside every rate. The constant behind every one of
those intervals was `Z_95`, and nothing checked its value.

Setting `Z_95 = 1.0` left all 31 statistics tests passing. So did `Z_95 = 2.5`. At `z = 1.0`,
5-of-10 renders as `(0.3492, 0.6508)` — a 68% interval published under a 95% label.

The reason is the sharpest lesson in this whole set: **every existing test was a property
test, and properties hold for any `z`.** Monotonicity, symmetry, containment, ordering — all
true whatever the constant is. Property-based testing is excellent and it cannot catch a
wrong constant, because a wrong constant does not break any property; it just moves the
answer.

The rule that follows: **if a number is published, at least one test must pin its value
against a literal.** It is now one line —
[`tests/test_statistics.py`](https://github.com/ChelseaKR/mrf-honest/blob/master/tests/test_statistics.py)
asserts `Z_95 == 1.959963984540054` against line 26 of
[`statistics.py`](https://github.com/ChelseaKR/mrf-honest/blob/master/src/mrf_honest/statistics.py)
— and it is the only test in that file that would have caught it.

### 3. `"up": "false"` counted as a day the endpoint answered

[`fhir-scorecard`](https://github.com/ChelseaKR/fhir-scorecard) publishes an availability
percentage for named healthcare organisations' public FHIR endpoints. It keeps a rolling
window of `{"date": ..., "up": ...}` observations, and both readers of that window tested
truthiness:

```python
reachable = sum(1 for o in observations if o.get("up"))       # drift
Observation(date=str(item.get("date")), up=bool(item.get("up")))  # archive
```

Every non-empty string is truthy in Python. So an entry carrying the **string** `"false"`
counted as a day the endpoint answered, and the published availability figure about a real,
named organisation went up.

The symmetric half is the part I would have got wrong on my own: an entry with **no** verdict
counted as a recorded outage nobody observed. The fix could not be "drop unreadable entries
from the numerator", because that converts an unreadable record into an outage — the same
defect pointed the other way. An unreadable entry now leaves both the numerator and the
denominator. Commit
[`a3b6675`](https://github.com/ChelseaKR/fhir-scorecard/commit/a3b6675); the reasoning
lives in
[`drift.py`](https://github.com/ChelseaKR/fhir-scorecard/blob/main/src/fhir_scorecard/drift.py).

### 4. A Spanish page that said the monthly fare was $35 when it is $70

[`fare-policy-assistant`](https://github.com/ChelseaKR/fare-policy-assistant) answers rider
questions about reduced-fare policy over a corpus of California transit agencies. Its
`facts.jsonl` is the table a numeric claim in an answer gets checked against. Four rows from
that committed file, side by side:

```text
program="Monthly GoPass (31 Days)"  rider_class="Regular Fixed Route"   price=70.0   correct
program="Monthly GoPass (31 Days)"  rider_class="Discount Fixed Route"  price=35.0   correct
program=",00 — Pago sin contacto Viaje único 2 horas Diario válido …"
                                    rider_class="regular"               price=35.0   WRONG
program=",00"                       rider_class=""                      price=35.0   garbage
```

The money pattern was `\$\s?\d+(?:\.\d{2})?`, which stops at the comma in `$ 35,00`. It
matched `$ 35` and left the orphan `,00` to be picked up as the *label* of the next row. The
Spanish rider-class vocabulary was English-only, so the discount half of the Spanish table
fell through to a prose fallback, and the discount price arrived carrying the regular label.

A Spanish-speaking rider budgeting from that page would have been told a $70 pass costs $35,
next to a correct English row saying $70. The parse failure did not read as a failure. It
read as a fare. Commit
[`0103f39`](https://github.com/ChelseaKR/fare-policy-assistant/commit/0103f39) reads
both decimal conventions and refuses any row it cannot resolve into a real
`(program, rider_class, price)` triple.

### 5. A harness that scored silence at 1.0000

This one is already in [the README](../README.md), and it belongs here because it is the
cleanest specimen. [`plumbline`](https://github.com/ChelseaKR/plumbline) is a fail-closed
audit harness. A target that answered nothing at all — 174 empty responses on the demo
bundle at the time — scored a perfect `1.0000` on five separate suites: groundedness,
privacy, representational harms, fairness and cross-language consistency. The gate returned
`PASS` and exit `0`.

Each of those five checks is phrased as *the absence of a bad thing*. An empty response never
contains a bad thing. So it never matches, so it passes. The first fix tested
`response.strip()` and did not close the case of a single period, an emoji, or a zero-width
space — all non-empty strings, all equally devoid of content, all scoring the same perfect
mark. "Not empty" and "contains something a check can read" are different properties.

### 6. A diff tool that reported "No published value moved" having compared nothing

[`wildfire-service-territory-overlap`](https://github.com/ChelseaKR/wildfire-service-territory-overlap)
publishes coverage counts over California's wildfire damage-inspection records, and the whole
point of its refresh diff is that a published number cannot change quietly. It compares two
artifacts leaf by leaf and prints a verdict.

Two empty objects agree on every one of their zero values. So the tool reported
`0 values compared`, printed `No published value moved.`, and exited `0` — *the same verdict
and the same exit code* as the 4,370-value comparison it was written for. A build that failed
and wrote `null` would have passed for a refresh in which nothing moved.

It now refuses three inputs before printing anything: a side that is not a JSON object, a
comparison in which no value was compared, and two paths that are the same file. Each exits
`2` with nothing on stdout, so a caller reading `--json` never receives an object describing a
comparison that was not made. The reasoning is in the module docstring of
[`artifact_diff.py`](https://github.com/ChelseaKR/wildfire-service-territory-overlap/blob/main/src/wildfire_service_territory_overlap/artifact_diff.py),
and its best line is *nothing compared is not nothing moved*.

### 7. A missing key that would have re-minted 134 stable identifiers, and exited 0

[`chalkline`](https://github.com/ChelseaKR/chalkline) publishes California educator
credential authorisations as CTDL JSON-LD. Identifier stability is the entire promise: a
CTID, once minted for a thing, must keep pointing at that thing.

`load_ledger` read the committed key-to-CTID mapping with `document.get("ctids", {})`. Two
different absences arrived at that line as the same empty dict: **no ledger file at all**,
which is a real and correct state for a repository before its first mint, and **a ledger file
whose `ctids` key had been renamed, dropped in a merge, or truncated away**, which is a file
the function cannot read.

Downstream, `mint_missing` treats every key in an empty mapping as unassigned, mints a fresh
UUIDv4 for each, and `save_ledger` writes the result over the file. A corrupted ledger would
therefore have been *repaired* by re-minting all 134 identifiers, exiting `0`, and reporting
the new count as a successful run, with none of the committed CTIDs surviving.
[`ctid.py`](https://github.com/ChelseaKR/chalkline/blob/main/src/chalkline/ctid.py) now keeps
the two absences apart, and says why in the error message.

### 8. A test that could not see the value it was written to catch

[`homeroom`](https://github.com/ChelseaKR/homeroom) renders California school data as
bilingual pages. A suppressed measure must render as *not published*, never as zero — that is
in the project's own description.

`float("nan")` succeeds. NaN is also the single most common way an upstream export writes *no
value* — so the string that says most clearly that nothing was measured parsed cleanly into a
reported figure. The test that should have caught it was well written and blind by
construction: it looks for numbers with

```python
NUMBER = re.compile(r"\d[\d,]*(?:\.\d+)?")
```

and `nan` has no digits. The test was correct. It could not fail on this input, and that is a
different thing from passing.
[`tests/test_pages.py`](https://github.com/ChelseaKR/homeroom/blob/main/tests/test_pages.py)
still holds that regex; the fix was at the boundary, in
[`measures.py`](https://github.com/ChelseaKR/homeroom/blob/main/src/homeroom/measures.py),
where `nan`, `inf`, `1_0`, `1e3` and non-ASCII digits now stop the build instead of becoming
figures.

### 9. A verdict computed over zero gates

[`gauntlet`](https://github.com/ChelseaKR/gauntlet) is a merge-blocking evaluation gate. Its
run verdict was `all(gate.passed for gate in self.gates)`, and `all()` over an empty set of
gates is `True` — so a result set containing no gates rendered `PASS` and reported
`passed=true` to the GitHub Action **while the body of the same document said "No gate ran.
This pack establishes nothing about the target."**

The document was right and the machine-readable field was wrong, which is the same
narrowest-surface pattern as above: the human-readable prose carried the absence and the
field the automation reads did not. It is also the same vacuous `all()` as receipt 1, in a
tool whose only job is to block a merge. The current shape is worth reading because of what
it does *not* do:
[`results.py`](https://github.com/ChelseaKR/gauntlet/blob/main/src/gauntlet/results.py)
carries a `verdict_withheld` field — a reason string, not a boolean — checked immediately
before the `all()`. A verdict that must not be rendered is represented as a reason for not
rendering it, rather than as a `False` that would be indistinguishable from a real failure.

## What these have in common, and it is not the `all()`

Two of nine turn on `all([])`. The rest do not. What all nine share is a fixture problem:

**Every fixture carried the populated case.** Every one of these code paths was tested, and
every test supplied the input under which the defect cannot appear. The archive fixture had
bags in it. The diff fixture had values in it. The availability fixture had booleans in it.
The suite fixture had gates in it. Nothing in any of those suites was wrong. They were
answering a question that was not the one at risk.

That is why a static rule finds so few of them, which I will come back to.

There is a second, quieter pattern: **the narrowest output surface is the one that lies.**
Receipt 9 is the clearest case — a document reading "No gate ran. This pack establishes
nothing about the target." above a machine-readable field saying `passed=true`. The prose had
room for the absence and carried it; the field a CI job actually reads did not. Whichever
surface is narrowest — a one-line summary, a boolean, an exit code — is the one that has to
be able to say *nothing was learned*, and it is the one that usually cannot.

## The vocabulary problem, measured

Once you start fixing these, you need a word for "we did not learn anything here", and there
is no standard one. So everybody invents it, repeatedly.

I ran a lexical scan over the first-party source of my own public repositories on 2026-09-07:
43 of my 44 public repositories are checked out locally; the scan looked at 1,862 source
files under `src/`, `lib/`, `app/`, `tools/` and similar directories, skipping tests,
fixtures, vendored code and build output, for any of 34 absence tokens as whole words. The
result:

| Measure | Count |
|---|---:|
| Repositories scanned | 43 |
| Repositories carrying at least one absence token | 42 |
| Repositories carrying five or more distinct tokens | 28 |
| Distinct tokens from the 34-token lexicon in use | 29 |
| Repositories using `not_comparable` | 4 |

That is a coarse instrument and I would not defend the exact numbers to a decimal place — a
token can appear in a comment, and a repository can spell one concept two ways. The shape is
what matters, and the shape is that essentially every project invented this vocabulary
independently, and no two invented the same one.

The named vocabularies are checkable, and reading them side by side is more useful than the
census:

| The need | The answer, and where |
|---|---|
| A cell absent for different reasons | `CellState = PRESENT / EXPLICIT_UNKNOWN / NOT_RECORDED` — [`perimeter/src/perimeter/cells.py:61`](https://github.com/ChelseaKR/perimeter/blob/main/src/perimeter/cells.py) |
| A figure that may not be a figure | `MeasureStatus = REPORTED / SUPPRESSED / NOT_REPORTED` — [`homeroom/src/homeroom/measures.py:55`](https://github.com/ChelseaKR/homeroom/blob/main/src/homeroom/measures.py) |
| A rule that was applicable and did not run | `SkipReason` — [`ceqa-preflight/src/ceqa_preflight/models.py:37`](https://github.com/ChelseaKR/ceqa-preflight/blob/main/src/ceqa_preflight/models.py) |
| A verdict that must not be rendered | `verdict_withheld` — [`gauntlet/src/gauntlet/results.py:129`](https://github.com/ChelseaKR/gauntlet/blob/main/src/gauntlet/results.py) |
| A report qualified by its own scope | `RunCoverage` — [`tods-validate/src/tods_validate/rules/__init__.py:991`](https://github.com/ChelseaKR/tods-validate/blob/main/src/tods_validate/rules/__init__.py) |
| A vocabulary that deliberately has no such word | `Verdict = PASS / FAIL`, absent data fails closed — [`sprout/src/sprout/eval/suite.py:47`](https://github.com/ChelseaKR/sprout/blob/main/src/sprout/eval/suite.py) |

The last row is the one that makes this a design table rather than a style rule. **There are
two correct answers, not one.** Widen the vocabulary so the state can be named, or fail closed
so it cannot be reached. `sprout` chose the second deliberately and says so in its module
docstring. Any write-up of this that does not lead with "or fail closed" will push people to
add a `NOT_RUN` member to enums that do not need one, which raises the branch count and makes
everything harder to read for no gain.

## The part where I built the detector and it did not work

I wrote a static detector for this class — a semgrep pack plus two AST checks — and ran it
across the portfolio. Because most of the defects were already fixed by then, I reconstructed
the **pre-fix** versions of nine files out of `git` into a scratch corpus so the detector had
something real to find. Against twelve confirmed instances, eleven of them testable this way,
it caught **five at the exact line**, using three different rules, one of which is
unshippable.

The two rules worth keeping are narrow. "An outcome enum with a verdict-shaped member and no
absence member" produced exactly one report across the whole portfolio, and it was a defect
already on the list — zero false positives, zero new findings. "A verdict returned straight
from an unguarded `all()`" produced six hits across thirteen repositories, three of them in
`ledger`, including
[`lockdown.py`](https://github.com/ChelseaKR/ledger/blob/main/src/ledger/lockdown.py) at the
exact line of receipt 1 — **nineteen days before it was fixed**. The audit recorded it as a
structural fact rather than a defect, because nobody had checked whether the audit could
actually return empty in practice. It could.

Everything else measured badly:

- A rule for bare `float()` at a boundary caught the `homeroom` defect at the exact line, and
  918 other things. There is no mechanical way to distinguish a boundary parse from an
  arithmetic cast.
- A rule for `max()` over two failure populations had 100% recall and 20% precision. Adding
  the obvious precision filter took recall to zero. There is no version of that rule that is
  both usable and useful.
- The rule for two-way identity tests on a multi-state enum produced its **highest** alert
  volume on `perimeter` — the repository that models absence best — because a project with a
  three-state cell type compares enum members constantly and correctly. Its noise was
  inversely proportional to the bug it was looking for.

The last one is the observation I have not seen made elsewhere, and it is the reason I did
not ship the pack as a linter. A tool that claims to cover "absence rendered as a value" and
silently passes on the shapes it cannot see would be an instance of its own bug class: a gate
reporting clean because it only looked in one bucket.

**The honest summary is that the sweep was worth far more than the tool, and the tool's best
rule was the one I could not ship.** Six of the eleven defects are missing *checks* rather
than missing *states* — the absence of a guard between two correct lines, the absence of a
`Content-Length` comparison, the absence of a `coverage` parameter on one of four output
formatters. An absent check is not a token. It has no location. There is nothing to match.

*The detector run summarised in this section is from an internal audit dated 2026-08-19 that
is not published, so unlike everything else on this page you cannot re-run it from a
repository. Either that audit's measurement tables ship alongside this page, or this section
comes out.*

## What actually finds them

Running the thing with nothing in it.

Since a static rule cannot see a missing check, the only reliable instrument is to supply the
input the fixture never supplies — the empty archive, the empty diff, the dead endpoint, the
suppressed cell — and see whether the gate still says yes. That is a test convention, not a
lint rule, and it generalises to a discipline: **a check is not trusted until it has been
observed failing.**

That discipline has its own write-up, with the procedure and the six distinct ways a negative
control can lie to you: *Observed failing, or it is not a gate*, in `plumbline`'s `docs/`
directory. `plumbline` also carries the discipline as a committed artifact rather than a
description of one —
[`proof/matrix.md`](https://github.com/ChelseaKR/plumbline/blob/main/proof/matrix.md) records
every suite being observed failing on a defect planted for it.

## What I am not claiming

- **That this is a new idea.** It is not. The contribution here is a set of measured instances
  with the fix commits attached, and a negative result about tooling for them.
- **That any of this is widely used.** My public repositories have 48 stars between them. The
  work is worth reading because it is checkable, not because anyone has adopted it.
- **That anyone else publishes numbers like this.** Every instance above is from my own
  repositories, found in my own code, and that is deliberate: it is what makes the class
  discussable without pointing at people who have no duty to defend the artifacts they
  publish.
- **That the class is now handled.** Two more sites of the same shape are open in `ledger`
  alone and recorded rather than patched, because each changes a published contract: a
  `/healthz` endpoint that answers `all_verified` over zero bags, and a hand-off manifest that
  tells a volunteer inheriting the archive *"All bags verified intact at hand-off time."* over
  the same nothing. Those are decisions, not defects.

---

*Text on this page is CC BY 4.0, like the rest of this repository's prose. The code it quotes
is under each project's own license.*
