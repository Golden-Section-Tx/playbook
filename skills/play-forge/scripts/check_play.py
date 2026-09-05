#!/usr/bin/env python3
"""Validate a draft play against the Golden Section playbook contract.

Checks the frontmatter schema, the closed vocabularies, the canonical key order,
and the body conventions that schema/play.schema.json cannot express. Also
cross-checks a corpus directory when one is given: uniqueness of order/slug/
anchor, that every preventsMistakes number exists, and that every referenced
template file is on disk.

No third-party dependencies. Python 3.8+.

    python3 check_play.py DRAFT.md
    python3 check_play.py DRAFT.md --corpus /path/to/playbook
    python3 check_play.py --corpus /path/to/playbook --all   # regression-check the corpus

Exit status is 0 when there are no errors. Warnings never fail the run.
"""

from __future__ import annotations

import argparse
import os
import re
import sys

KEY_ORDER = [
    "order", "slug", "anchor", "title", "h1", "category", "players",
    "initialEffort", "ongoingEffort", "frequency", "stage", "templates",
    "summary", "keywords", "questions", "preventsMistakes", "format",
]
REQUIRED = [k for k in KEY_ORDER if k not in ("templates", "format")]
LIST_FIELDS = {"keywords", "questions", "preventsMistakes"}

CATEGORIES = ["executive", "sales-marketing", "customer", "operations",
              "development", "vendor"]
PLAYERS = ["Founder", "Exec Team", "Board", "CFO", "COO", "CTO", "Legal",
           "Sales Lead", "SDR", "CS Lead", "Product", "Product Manager",
           "Engineering Lead", "DevOps", "Security Lead", "Implementation",
           "Implementation Lead"]
# Mirrors EFFORT_SCALE in scripts/build.mjs; kept here so this checker runs
# standalone against one file. Change both together. EFFORT.md is the prose.
EFFORT = ["1 SP", "2 SP", "3 SP", "5 SP", "8 SP", "13 SP", "21 SP", "34 SP",
          "—", "-", "--"]
FREQUENCY = ["Continuous", "Weekly", "Monthly", "Quarterly", "Bi-Annually",
             "Annual", "As Needed", "Per Customer", "Per Project"]
STAGE = ["Pre-Revenue", "Early Traction", "Growth", "All Stages"]

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TEMPLATE_RE = re.compile(r"^[0-9]+\.[0-9]+-[a-z0-9-]+\.xlsx$")
BINDER_BY_CATEGORY = {"executive": "1", "sales-marketing": "2", "customer": "3",
                      "operations": "4", "development": "5", "vendor": "6"}


class Report:
    def __init__(self) -> None:
        self.errors: list = []
        self.warnings: list = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def split_frontmatter(text: str):
    """Return (frontmatter_text, body) or (None, text) when absent."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 3)
    if end == -1:
        return None, text
    return text[4:end + 1], text[end + 5:]


def parse_frontmatter(fm: str, rep: Report) -> dict:
    """Parse the flat subset of YAML the plays use. Keeps key order."""
    data: dict = {}
    order: list = []
    current = None
    for raw in fm.split("\n"):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("  - ") or raw.startswith("- "):
            item = raw.split("- ", 1)[1].strip()
            if current is None:
                rep.error(f"frontmatter: list item with no key: {raw!r}")
                continue
            if current == "templates":
                m = re.match(r"file:\s*(.+)$", item)
                if m:
                    data[current].append({"file": m.group(1).strip()})
                else:
                    rep.error(f"templates: expected 'file:' first, got {item!r}")
            else:
                data[current].append(item)
            continue
        if raw.startswith("    ") and current == "templates":
            m = re.match(r"\s*name:\s*(.+)$", raw)
            if m and data["templates"]:
                data["templates"][-1]["name"] = m.group(1).strip()
            continue
        m = re.match(r"^([A-Za-z][A-Za-z0-9_]*):\s*(.*)$", raw)
        if not m:
            rep.error(f"frontmatter: cannot parse line {raw!r}")
            continue
        key, value = m.group(1), m.group(2).strip()
        order.append(key)
        current = key
        if value == "":
            data[key] = []
        else:
            data[key] = value
            current = None
    data["__order__"] = order
    return data


def unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def check_frontmatter(data: dict, path: str, rep: Report) -> None:
    order = data.get("__order__", [])

    for key in REQUIRED:
        if key not in data:
            rep.error(f"missing required field: {key}")
    for key in order:
        if key not in KEY_ORDER:
            rep.error(f"unknown field: {key}")

    known = [k for k in order if k in KEY_ORDER]
    expected = [k for k in KEY_ORDER if k in known]
    if known != expected:
        rep.error("frontmatter key order is wrong.\n"
                  f"    found:    {', '.join(known)}\n"
                  f"    expected: {', '.join(expected)}")

    def val(key):
        v = data.get(key)
        return unquote(v) if isinstance(v, str) else v

    if "order" in data:
        try:
            int(str(val("order")))
        except ValueError:
            rep.error(f"order must be an integer, got {val('order')!r}")

    stem = os.path.splitext(os.path.basename(path))[0]
    slug = val("slug")
    if slug:
        if not SLUG_RE.match(slug):
            rep.error(f"slug must be kebab-case, got {slug!r}")
        if stem not in ("play-template", slug):
            rep.error(f"slug {slug!r} must equal the filename stem {stem!r}")

    anchor = val("anchor")
    if anchor and not SLUG_RE.match(anchor):
        rep.error(f"anchor must be kebab-case, got {anchor!r}")

    category = val("category")
    if category and category not in CATEGORIES:
        rep.error(f"category {category!r} not in {CATEGORIES}")
    parent = os.path.basename(os.path.dirname(os.path.abspath(path)))
    if category and parent in CATEGORIES and parent != category:
        rep.error(f"category {category!r} does not match folder {parent!r}")

    players = val("players")
    if players:
        for role in [p.strip() for p in players.split(",")]:
            if role not in PLAYERS:
                rep.warn(f"player {role!r} is not in the existing vocabulary — "
                         "coin a new role only if none is honest")

    for key in ("initialEffort", "ongoingEffort"):
        v = val(key)
        if v is not None and v not in EFFORT:
            rep.error(f"{key} {v!r} is not a value on the effort scale "
                      "(1/2/3/5/8/13/21/34 SP) or an em dash — see EFFORT.md")

    if val("frequency") and val("frequency") not in FREQUENCY:
        rep.error(f"frequency {val('frequency')!r} not in {FREQUENCY}")
    if val("stage") and val("stage") not in STAGE:
        rep.error(f"stage {val('stage')!r} not in {STAGE}")

    h1 = val("h1")
    if h1 and not h1.lower().startswith("how to"):
        rep.warn(f"h1 usually starts with 'How to' — got {h1!r}")

    summary = val("summary")
    if isinstance(summary, str):
        if len(summary) < 40:
            rep.error("summary must be at least 40 characters")
        if "\n" in summary.strip():
            rep.warn("summary should be one paragraph")

    for key in LIST_FIELDS:
        v = data.get(key)
        if key in data and not isinstance(v, list):
            rep.error(f"{key} must be a list")
        elif isinstance(v, list) and not v:
            if key == "preventsMistakes":
                rep.warn("preventsMistakes is empty — allowed, but a play that "
                         "prevents no catalogued mistake is unusual")
            else:
                rep.error(f"{key} must have at least one entry")

    for n in data.get("preventsMistakes", []) or []:
        if not re.match(r"^\d+$", str(n).strip()):
            rep.error(f"preventsMistakes entry {n!r} is not an integer")

    for q in data.get("questions", []) or []:
        if not q.rstrip().endswith("?"):
            rep.warn(f"question does not end in a question mark: {q!r}")
    for k in data.get("keywords", []) or []:
        if k != k.lower() and not re.search(r"\b[A-Z]{2,}\b", k):
            rep.warn(f"keywords are lowercase except acronyms — got {k!r}")

    for t in data.get("templates", []) or []:
        f = unquote(t.get("file", ""))
        if not TEMPLATE_RE.match(f):
            rep.error(f"template filename {f!r} must look like "
                      "'2.40-pricing-matrix-template.xlsx'")
        elif category in BINDER_BY_CATEGORY and \
                not f.startswith(BINDER_BY_CATEGORY[category] + "."):
            rep.error(f"template {f!r} has the wrong binder number for "
                      f"category {category!r} (expected "
                      f"{BINDER_BY_CATEGORY[category]}.x)")
        if not t.get("name"):
            rep.error(f"template {f!r} is missing its display name")
        elif len(unquote(t["name"])) < 4:
            rep.error(f"template name {t['name']!r} is too short")

    if "format" in data and unquote(str(data["format"])) != "html":
        rep.error("format, if present, must be 'html'")


def check_body(body: str, rep: Report, strict: bool = True) -> None:
    """strict=True for a new draft; False when regression-checking built plays."""
    def fail(msg):
        rep.error(msg) if strict else rep.warn(msg)

    generated = re.search(r"<!-- GS:LINKS start.*?GS:LINKS end -->", body,
                          re.S)
    if generated:
        if strict:
            rep.warn("draft carries a GS:LINKS block. Harmless — the build "
                     "overwrites it — but a new play does not need one")
        body = body[:generated.start()] + body[generated.end():]
    elif "<!-- GS:LINKS" in body:
        rep.error("unterminated GS:LINKS marker — the build will not "
                  "recognize it")
    if re.search(r"^\*\*Prevents\*\*", body, re.M):
        rep.error("hand-written 'Prevents' line outside the generated block — "
                  "the graph comes from preventsMistakes, and this will be "
                  "duplicated on the next build")

    if not re.search(r"^> \*\*The [Gg]oal:?\*\*:?", body, re.M):
        fail("missing the goal callout. 57 of 70 plays carry "
                  "'> **The goal:** …' naming the artifact the play produces")

    if not re.search(r"^#### Steps", body, re.M):
        fail("missing a '#### Steps' section")
    elif re.search(r"^#### Steps:\s*$", body, re.M):
        rep.warn("'#### Steps' without a colon is the corpus convention "
                 "(50 of 56)")

    for heading in re.findall(r"^(#{1,3}) ", body, re.M):
        fail(f"body uses an h{len(heading)} heading — plays use '####' "
             f"for section headings")

    first = re.search(r"^(####|>)", body, re.M)
    lead = body[:first.start()] if first else body
    if len(lead.strip()) < 200:
        rep.warn("the opening is under 200 characters — 59 of 70 plays open "
                 "with one to four paragraphs making the case")

    steps = re.search(r"^#### Steps.*?(?=^#### |\Z)", body, re.M | re.S)
    if steps:
        numbered = re.findall(r"^\d+\. ", steps.group(0), re.M)
        if len(numbered) < 2:
            fail("the Steps section needs at least two numbered steps")
        else:
            tail = steps.group(0).rstrip().split("\n")
            last = " ".join(tail[-6:]).lower()
            if not re.search(r"iterat|ongoing|owner|own it|update|cadence|"
                             r"review|codif|quarterly|monthly|weekly|annual",
                             last):
                rep.warn("the last step usually names the recurrence — who "
                         "owns the artifact, at what cadence, and what they "
                         "look at. A play with no recurrence step is a project")

    for bad in ("in today's", "in the modern", "fast-paced", "it is important "
                "to note", "leverage synergies", "at the end of the day"):
        if bad in body.lower():
            rep.warn(f"filler phrase in the body: {bad!r}")


def cross_check(data: dict, path: str, corpus: str, rep: Report,
                strict: bool = True) -> None:
    plays_dir = os.path.join(corpus, "plays")
    if not os.path.isdir(plays_dir):
        rep.error(f"--corpus {corpus!r} has no plays/ directory")
        return

    seen = {"order": {}, "slug": {}, "anchor": {}}
    for category in sorted(os.listdir(plays_dir)):
        cdir = os.path.join(plays_dir, category)
        if not os.path.isdir(cdir):
            continue
        for name in sorted(os.listdir(cdir)):
            if not name.endswith(".md") or name == "README.md":
                continue
            other = os.path.join(cdir, name)
            if os.path.abspath(other) == os.path.abspath(path):
                continue
            fm, _ = split_frontmatter(open(other, encoding="utf-8").read())
            if not fm:
                continue
            quiet = Report()
            od = parse_frontmatter(fm, quiet)
            for key in seen:
                v = od.get(key)
                if isinstance(v, str):
                    seen[key][unquote(v)] = other

    for key in seen:
        v = data.get(key)
        if isinstance(v, str) and unquote(v) in seen[key]:
            rep.error(f"{key} {unquote(v)!r} is already used by "
                      f"{os.path.relpath(seen[key][unquote(v)], corpus)}")

    if strict and data.get("order") and str(unquote(str(data["order"]))).isdigit():
        highest = max([int(o) for o in seen["order"] if str(o).isdigit()] or [0])
        if int(unquote(str(data["order"]))) <= highest:
            rep.warn(f"order {data['order']} is at or below the highest in the "
                     f"corpus ({highest}); the next unused integer is "
                     f"{highest + 1} unless this play belongs mid-sequence")

    mistakes_file = os.path.join(corpus, "MISTAKES.md")
    if os.path.isfile(mistakes_file):
        text = open(mistakes_file, encoding="utf-8").read()
        known = {int(n) for n in re.findall(r'<a id="m0*(\d+)"></a>', text)}
        for n in data.get("preventsMistakes", []) or []:
            if str(n).strip().isdigit() and int(str(n).strip()) not in known:
                rep.error(f"preventsMistakes {n} does not exist in MISTAKES.md "
                          f"(highest is {max(known) if known else 0})")
    else:
        rep.warn("no MISTAKES.md in the corpus — mistake numbers unchecked")

    tdir = os.path.join(corpus, "templates")
    for t in data.get("templates", []) or []:
        f = unquote(t.get("file", ""))
        if f and not os.path.isfile(os.path.join(tdir, f)):
            rep.error(f"template {f!r} is not in {os.path.relpath(tdir, corpus)}/")


def check_file(path: str, corpus: str = None, strict: bool = True) -> Report:
    rep = Report()
    text = open(path, encoding="utf-8").read()
    fm, body = split_frontmatter(text)
    if fm is None:
        rep.error("no frontmatter found — a play opens with a '---' block")
        return rep
    data = parse_frontmatter(fm, rep)
    check_frontmatter(data, path, rep)
    check_body(body, rep, strict)
    if corpus:
        cross_check(data, path, corpus, rep, strict)
    return rep


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft", nargs="?", help="the play file to check")
    ap.add_argument("--corpus", help="path to a playbook clone or mirror")
    ap.add_argument("--all", action="store_true",
                    help="check every play in --corpus instead of a draft")
    args = ap.parse_args()

    if args.all:
        if not args.corpus:
            print("--all needs --corpus", file=sys.stderr)
            return 2
        targets = []
        plays = os.path.join(args.corpus, "plays")
        for category in sorted(os.listdir(plays)):
            cdir = os.path.join(plays, category)
            if os.path.isdir(cdir):
                targets += [os.path.join(cdir, n) for n in sorted(os.listdir(cdir))
                            if n.endswith(".md") and n != "README.md"]
    elif args.draft:
        targets = [args.draft]
    else:
        ap.print_help()
        return 2

    failed = 0
    for path in targets:
        rep = check_file(path, args.corpus, strict=not args.all)
        label = os.path.relpath(path)
        if rep.errors or rep.warnings:
            print(f"\n{label}")
            for e in rep.errors:
                print(f"  ERROR   {e}")
            for w in rep.warnings:
                print(f"  warn    {w}")
        if rep.errors:
            failed += 1

    print()
    if len(targets) > 1:
        print(f"{len(targets) - failed}/{len(targets)} files clean")
    if failed:
        print(f"{failed} file(s) with errors — fix these before committing.")
        return 1
    print("No errors. Run `npm run build` in the repository before committing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
