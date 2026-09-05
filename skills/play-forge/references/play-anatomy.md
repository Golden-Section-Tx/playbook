# Play anatomy

What the plays actually look like, measured rather than remembered.

**Counts below are out of 70 plays and 168 mistakes, measured 2026-08-26.** The
corpus grows — it was 63 and 161 earlier the same day — so read a count as
evidence of a convention, never as a current fact. Re-measure before leaning on
one; `check_play.py --corpus . --all` will tell you if a convention has drifted.

`schema/play.schema.json` in the repository is the authority on the frontmatter;
this file is the authority on everything the schema cannot express.

## Frontmatter

Keys appear in **this exact order** in every play. Only two orderings exist in
the corpus, and they differ solely by whether `templates` is present.

```yaml
order:            # integer, unique across all plays
slug:             # equals the filename stem; permanent
anchor:           # short stable id; permanent
title:            # short label
h1:               # page headline
category:         # must match the containing folder
players:          # comma-separated roles, one string
initialEffort:    # "13 SP" or an em dash
ongoingEffort:    # "5 SP" or an em dash
frequency:
stage:
templates:        # OPTIONAL — sits here, before summary, not at the end
summary:
keywords:         # list
questions:        # list
preventsMistakes: # list of integers
format:           # OPTIONAL — only "html", used by exactly one play
```

`templates` before `summary` is the one field position people get wrong.

### Closed vocabularies

| Field | Allowed values |
|---|---|
| `category` | `executive` · `sales-marketing` · `customer` · `operations` · `development` · `vendor` |
| `players` | Founder · Exec Team · Board · CFO · COO · CTO · Legal · Sales Lead · SDR · CS Lead · Product · Product Manager · Engineering Lead · DevOps · Security Lead · Implementation · Implementation Lead |
| `initialEffort` / `ongoingEffort` | One of the values in [`EFFORT.md`](../../../EFFORT.md), or `—` |
| `frequency` | Continuous · Weekly · Monthly · Quarterly · Bi-Annually · Annual · As Needed · Per Customer · Per Project |
| `stage` | Pre-Revenue · Early Traction · Growth · All Stages |
| `format` | `html` — only where the body needs headings inside list items |

[`EFFORT.md`](../../../EFFORT.md) is the scale, and it is stated in durations
rather than points for a reason. **Before writing either number, say it out
loud as time and see whether you believe it**: 8 SP claims half a person-week,
13 SP a person-week, 34 SP three. A point is one person's working time, so a
step that puts three people in a room for a morning costs a day and a half, not
half a day.

`ongoingEffort` is the cost of a *single* recurrence, never the annual total.
Quoting a year in that field silently multiplies the play's cost by twelve
everywhere downstream.

A 34 that should be an 8 is how a play becomes shelfware; an 8 that should be a
34 is how a founder loses a quarter trusting your estimate. If the honest answer
is above 34 — more than three person-weeks to stand up — the play is more than
one play, and the fix is to split it, not to write `34 SP` and hope.

`stage` is the earliest stage at which the play *pays for itself*, not the
earliest at which it is possible.

### Template file names

`<binder>.<n>-<lowercase-hyphenated-name>-template.xlsx`, and the binder number
carries the category: `1.x` Executive · `2.x` Sales & Marketing · `3.x`
Customer · `4.x` Operations · `5.x` Development · `6.x` Vendor. The build fails
if a referenced file is missing from `templates/` and warns about any file
there that no play references.

## Body

The shape, in order, with how many plays use each part:

| Part | Count | Form |
|---|---|---|
| Opening prose | 66/70 | One to four paragraphs. Two is the mode. Second person, present tense. |
| Goal callout | 64/70 | `> **The goal:** …` — one sentence, naming the artifact. |
| `#### Background` | 33/70 | Framework, options, or context that the steps would otherwise have to teach. |
| `#### Steps` | 63/70 | No trailing colon in 57 of 63 that have the section. Numbered, plain imperative prose. |
| Bolded step labels | 4/70 | `1. **Prepare:**` — only where the sequence has named phases. Not the default. |
| `#### Notes` / `#### Best Practices` | ~5/70 | Practices that do not fit the sequence. |
| `#### Troubleshooting` | 16/70 | Failure modes in the founder's voice, italicised, then answered. |
| `**How Golden Section can help:**` | 1/70 | Rare. Omit unless there is a specific, true thing to say. |
| `***Prerequisites:***` | 1/70 | Rare. Use only where something must be true first. |
| `<!-- GS:LINKS -->` | 70/70 | **Generated.** Never author it. |

Nesting is four spaces per level. Sub-points under a step are questions to
answer or things to gather, not more steps.

The last numbered step is almost always the recurrence — who owns the artifact
once it exists, at what cadence, and what they look at. A play with no
recurrence step is a project.

## Voice

Read the nearest three plays before writing. Then check yours:

- **Second person, direct.** "You will need informed assumptions", not
  "founders should ensure that assumptions are informed".
- **Concrete over abstract.** Name the meeting, the spreadsheet, the role, the
  number, the benchmark source.
- **One earned observation** in the opening — what you know from watching it go
  wrong, not what you know from reading about it.
- **Short sentences carry the weight.** The corpus is blunt. It says
  "self-explanatory… don't do it" where a consultant would spend a paragraph.
- **No filler.** No landscape-setting opener, no summary paragraph at the end,
  no adjective doing no work.
- **Honest about limits.** Where a play does not apply, say so in
  Troubleshooting rather than pretending it always does.

## Mistake entries

`MISTAKES.md`, ascending numeric order, one entry each:

```markdown
### <a id="m162"></a>162 · The mistake, stated as a behavior

`Executive · Sales & Marketing`

One to three sentences. What happens, and why it costs something.
```

- Next unused number. **Numbers are permanent** — cited from goldensection.com
  and from every fork. Never renumber, never reuse a retired number.
- Anchor is the number zero-padded to three digits and must agree with it.
- Categories, joined by ` · `, from: Executive · Sales & Marketing · Customers ·
  Operations · Development · Vendors. (Note the plurals — they differ from the
  play `category` values.)
- A behavior with a consequence, not a category of risk. "Letting customers
  dictate the terms" is a mistake; "contract risk" is not.
- Leave out the `**Prevented by**` line. The build writes it from the plays.
- One of the 168 has no detail sentence, so detail is optional — but write it.

## What the build checks

`npm run build` regenerates every cross-reference and validates. It fails on:
missing or unknown frontmatter fields, `slug` not equal to the filename,
`category` not matching the folder, duplicate `order` / `slug` / `anchor`, a
`preventsMistakes` number that does not exist, a referenced template that is not
on disk, and stale generated output. `scripts/check_play.py` in this skill
catches the same class of error plus the conventions above, without needing the
repository's toolchain installed.
