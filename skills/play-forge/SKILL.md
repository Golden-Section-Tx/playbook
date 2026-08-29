---
name: play-forge
description: Author a Golden Section play or mistake to this repository's exact template — canonical frontmatter key order, closed vocabularies, body conventions measured from the corpus, mistake numbering, a dependency-free validator, and the path from draft to pull request. Use when writing a new play, improving an existing one, drafting a new mistake, or preparing a contribution to the playbook repo.
---

# play-forge

Turn a validated pattern into a **play** — or a validated behavior into a numbered **mistake** — shaped like the 70 that are already here, so what you open as a pull request is mergeable rather than merely well-intentioned.

Pairs with `play-hunt`, which finds the candidates this skill writes up.

## Read these three files first

Do not write a play from a description of the format, including this one. The format is three files in this skill:

| File | What it is |
|---|---|
| [`references/play-template.md`](references/play-template.md) | The scaffold. Copy it and fill it in. Correct key order, correct markers. |
| [`references/play-anatomy.md`](references/play-anatomy.md) | Every field rule and every body convention, with how many of the 70 plays use each. The authority on everything the JSON schema cannot express. |
| [`scripts/check_play.py`](scripts/check_play.py) | The validator. Run it before you commit. No dependencies. |

Then read the nearest three existing plays in the category you are writing for. The template gets the structure right; only the real plays get the voice right.

## The corpus

```bash
git clone https://github.com/golden-section-tx/playbook.git
cd playbook && npm install
```

- `dist/playbook-full.md` — every mistake and play body in one file. Grep this first.
- `MISTAKES.md` — the numbered list with permanent `#mNNN` anchors.
- `plays/<category>/*.md` — the 70, one file each.
- `schema/play.schema.json` — the frontmatter contract.
- `CONTRIBUTING.md` — what gets accepted and what gets declined.

Working without a clone, the two files you cannot do without:

```bash
curl -sS -O https://raw.githubusercontent.com/golden-section-tx/playbook/main/dist/playbook-full.md
curl -sS -O https://raw.githubusercontent.com/golden-section-tx/playbook/main/MISTAKES.md
```

## Steps — authoring a play

1. **Grep the corpus for the nearest existing play.** If one already produces this artifact, the contribution is an *improvement to that play*, not a new play — write the edit instead. Restatements are the most commonly rejected contribution; improvements are the easiest to merge.

2. **Run the gate.** A play tells someone what to do on Monday morning:
   - Who owns it? (a role from the players vocabulary, not "the team")
   - How often does it recur?
   - What are the steps, in order?
   - What does it cost to stand up, in story points?

   All four must answer. If it cannot be scheduled, it is an essay. Also declined at source: generic startup advice, anything that reads as marketing for a product or service, and material that is not about B2B vertical software.

3. **Copy `references/play-template.md`** to `plays/<category>/<slug>.md` and fill it in. The two things authors get wrong: `templates:` sits **before** `summary:`, not at the end; and the key order is fixed — every one of the 70 plays uses it.

4. **Write the body to the measured shape**, not to a remembered one. `references/play-anatomy.md` carries the counts; the short version:
   - **Opening prose**, one to four paragraphs (66/70). The case for why this matters, second person, to a founder who is busy. One earned observation — what you know from watching it go wrong.
   - **`> **The goal:** …`** (64/70). One sentence naming the artifact the play produces. Colon inside the bold.
   - **`#### Background`** (33/70). Optional. A framework or set of options the steps would otherwise have to teach.
   - **`#### Steps`** — no trailing colon (57 of the 63 plays that have the section). Numbered, plain imperative prose. Bolded step labels like `1. **Prepare:**` appear in only 4 of 70; they are for sequences with named phases, not the default. Four spaces per level of nesting.
   - **The last step is the recurrence** — who owns the artifact once it exists, at what cadence, and what they look at. A play with no recurrence step is a project.
   - **`#### Notes`**, **`#### Best Practices`**, **`#### Troubleshooting`** — all optional. Troubleshooting appears in 16 of 70: failure modes in the founder's own voice, italicised, then answered plainly.
   - **`**How Golden Section can help:**`** appears in exactly one play, and `***Prerequisites:***` in one. Omit both unless there is something specific and true to say.
   - **Never write a `<!-- GS:LINKS -->` block.** The build generates it.

5. **Validate.**

   ```bash
   python3 skills/play-forge/scripts/check_play.py plays/<category>/<slug>.md --corpus .
   ```

   It checks required fields, key order, the closed vocabularies, slug-equals-filename, category-equals-folder, uniqueness of `order`/`slug`/`anchor` against the corpus, that every `preventsMistakes` number exists in `MISTAKES.md`, that every referenced template is on disk, the body conventions above, and a short list of filler phrases. Errors fail; warnings are conventions the corpus itself breaks occasionally and are worth a second look rather than obedience.

   It passes all 70 existing plays, so a failure on yours means yours is the outlier.

## Steps — authoring a mistake

Mistakes are shorter and stricter. `references/play-anatomy.md` has the full rules; the entry is:

```markdown
### <a id="m162"></a>162 · The mistake, stated as a behavior

`Executive · Sales & Marketing`

One to three sentences. What happens, and why it costs something.
```

- Next unused number. **Numbers are permanent** — `#m016` is cited from goldensection.com and from every fork. Never renumber, never reuse a retired number. The anchor is the number zero-padded to three digits.
- Categories come from a closed set, and they are **plural** where the play categories are singular: Executive · Sales & Marketing · Customers · Operations · Development · Vendors.
- State a **behavior with a consequence**, not a category of risk. "Letting customers dictate the terms" is a mistake; "contract risk" is not.
- Leave out the `**Prevented by**` line. The build writes it from the plays' `preventsMistakes`.
- A mistake worth adding has been watched happen — more than once, or once vividly. Keep the evidence in your own notes; it does not go in the entry.

## From draft to pull request

```bash
git checkout -b play/<slug>
# add plays/<category>/<slug>.md — or edit MISTAKES.md for a mistake
python3 skills/play-forge/scripts/check_play.py plays/<category>/<slug>.md --corpus .
npm run build      # regenerates cross-links, validates, reports — must exit clean
git add -A && git commit
```

Commit whatever the build regenerates; CI runs `npm run build --check` and fails on stale output. Then run the anonymization check below, because a pull request here is public the moment it opens and cannot be unpublished. Fill in the pull request template honestly, especially the provenance line.

First-time contributors sign the CLA — a bot handles it, and it takes a click. Read `CLA.md` first; it grants Golden Section broad rights, including use in commercial products.

## Guardrails

- **Anonymize, without exception.** No company name, no founder name, no figure specific enough to identify either — not in the play, not in a story, not in a branch name, a commit message, or a pull request description. A founder's own story is told with their written permission or not at all.
- **Never edit generated content**: anything between `<!-- GS:… start -->` and `<!-- GS:… end -->`, the `**Prevented by**` lines in `MISTAKES.md`, `plays/README.md`, or anything in `dist/`. Edits there are discarded on the next build.
- **The graph has one source of truth** — `preventsMistakes:` in the play's frontmatter. To link a play to a mistake, add the number there and rebuild. Never hand-write a link in the other direction.
- **A template is not the play.** The spreadsheet is the artifact; the play is the process that produces something true to put in it. Do not ship a play whose whole content is "fill in the template".
- **Re-measure rather than trust this file.** The counts in `references/play-anatomy.md` describe the corpus as it was when this skill shipped. After a release that adds plays, re-run the measurement before treating a convention as settled.
- Content here is CC BY-SA 4.0 and the scripts are MIT; the Golden Section name, logo, and marks are not licensed. Anything drafted with this skill inherits those terms.
