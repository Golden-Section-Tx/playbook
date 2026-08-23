# Contributing

Pull requests are welcome from anyone. Merge authority sits with Golden
Section's general partners — see [GOVERNANCE.md](GOVERNANCE.md).

Before your first pull request is merged you will be asked to sign the
[Contributor Licence Agreement](CLA.md). A bot handles this; it takes a click.
Read the CLA first — it grants Golden Section broad rights, including the right
to use your contribution in our own commercial products.

## What makes a good contribution

**A mistake worth adding** is one you have watched happen, more than once or
once vividly, in a B2B software company. Not a category of risk — a specific
behaviour with a specific consequence. Compare the tone of the existing 161:
they are short, blunt, and earned.

**A play worth adding** tells someone what to do on Monday morning. Steps,
owners, an honest effort estimate. If it cannot be scheduled, it is an essay,
not a play.

**Improvements to what is here** are the most valuable contributions and the
easiest to merge. A clearer step, a corrected number, a mistake that needs its
paired play, a template that has a bug in a formula.

What we will decline: generic startup advice, anything that reads as marketing
for a product or service, restatements of existing entries, and material that
is not about B2B vertical software.

## Mechanics

### Repository shape

```
MISTAKES.md            all 161, numbered, with stable #mNNN anchors
plays/<category>/      one Markdown file per play, six categories
templates/             the Excel templates, binder-numbered
stories/               longer write-ups attached to individual mistakes
schema/                the frontmatter contracts
scripts/build.mjs      regenerates cross-links and validates everything
dist/                  generated — never edit
```

### Never edit generated content

Two kinds of content are generated and will be overwritten:

- Anything between `<!-- GS:… start -->` and `<!-- GS:… end -->` markers.
- The `**Prevented by**` line under each mistake, and `plays/README.md`, and
  everything in `dist/`.

The play↔mistake graph has exactly one source of truth: the `preventsMistakes:`
list in each play's frontmatter. To link a play to a mistake, add the mistake's
number there and run the build. The reverse links generate themselves. Never
hand-edit a link in `MISTAKES.md` — it will be replaced.

### Adding or editing a play

Copy the nearest existing play, then edit its frontmatter. The contract is in
[`schema/play.schema.json`](schema/play.schema.json), and every field is
required except `templates` and `format`:

```yaml
order: 25                        # position in the overall sequence
slug: saas-pricing-matrix        # must equal the filename
anchor: pricing-matrix           # stable cross-reference id
title: Pricing Matrix            # short label
h1: How to Build a SaaS Pricing Matrix
category: sales-marketing        # must match the containing folder
players: Founder, Sales Lead, CFO
initialEffort: 21 SP
ongoingEffort: 8 SP
frequency: Quarterly
stage: Pre-Revenue
summary: One paragraph, a direct answer, used as the lead everywhere.
keywords:
  - saas pricing
questions:
  - How should I price my SaaS product?
preventsMistakes:
  - 36
templates:                       # optional
  - file: 2.40-pricing-matrix-template.xlsx
    name: Pricing Matrix Template
```

Body conventions: `#### Steps` for section headings, numbered steps, four
spaces per level of nesting, and `> **The goal:** …` for the callout. One play
(`saas-database-selection.md`) carries `format: html` because it needs headings
inside list items.

### Adding or editing a mistake

Mistakes live in `MISTAKES.md` in ascending numeric order. Each entry is:

```markdown
### <a id="m162"></a>162 · The mistake, stated as a behaviour

`Executive · Sales & Marketing`

One to three sentences. What happens, and why it costs something.
```

A new mistake takes the next unused number. **Numbers are permanent** —
`#m016` is cited from the website, from LookingGlass, and from anyone's fork.
Never renumber, never reuse a retired number.

Leave out the `**Prevented by**` line; the build adds it from the plays.

### Adding a template

Drop the `.xlsx` in `templates/`, keeping the binder number and a lowercase
hyphenated name (`2.40-pricing-matrix-template.xlsx`), then add it to the
owning play's `templates:` list. The build fails if a referenced file is
missing and warns about any template no play references.

### Adding a story

A story is a longer write-up of a single mistake — what it looked like, what it
cost, how it was caught. Put it in `stories/` as `mNNN-short-slug.md` and link
it from the mistake's entry. Stories must be anonymised: no company names, no
identifying detail, no numbers specific enough to identify anyone. If a
founder's own story is being told, it is told with their written permission or
not at all.

## Before you open the pull request

```bash
npm run build       # regenerates cross-links, validates, reports
git add -A
```

The build must exit clean. Commit whatever it regenerates — CI runs
`npm run build --check` and fails if the committed output is stale.

Then fill in the pull request template honestly, especially the provenance line.
Pull requests here are public the moment they open, and they cannot be
unpublished. Nothing in a branch name, commit message, diff, or description may
identify a company or a person.

## Reporting something without a pull request

Open an issue. A mistake you have seen and a paragraph about it is a completely
legitimate contribution — someone else can shape it into an entry.
