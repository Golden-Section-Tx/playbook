---
name: mistake-watch
description: Reads your own record of the period — meeting notes, transcripts, standups, a board deck, a Slack export, or just a conversation about the month — against the 168 numbered Golden Section mistakes and reports which are visibly in progress, each with a dated quote or figure, a confirmed or suspected grade, the play that prevents it, and how it moved since the last run. Use monthly, before a board meeting, or after a quarter that got away from you.
---

# mistake-watch

`play-hunt` reads transcripts to find what the corpus is missing. This is the same discipline pointed the other way: read what actually happened at **your** company against the 168 mistakes that are already numbered, and say which ones you are making.

Monthly is the natural cadence. The value is not in any single run — it is in the third one, when a mistake you first flagged in June is still live in August. That is why this skill keeps a log.

## Sources

1. **The corpus.** A clone of the repository, or:

   ```bash
   curl -sS -O https://raw.githubusercontent.com/golden-section-tx/playbook/main/MISTAKES.md
   ```

   Grep it. Never work from a remembered list — the numbers are permanent anchors (`#m001`…`#m161`) and getting one wrong makes the log unreadable later.

2. **Your record of the period.** Whatever exists: meeting notes, transcripts, standups, the board deck, a Slack export, an email thread, or your own memory in conversation. The last one counts — a founder talking through their month is a legitimate source, as long as what comes back out carries dates and specifics.

3. **`workspace/company-context.md`** — for play coverage and fit inputs.

4. **`workspace/mistake-log.md`** — the previous runs. Read this before reading anything else. You are looking for movement, not a fresh diagnosis.

## The bar — what counts as a match

**A match requires a specific observed behavior, with a quote or a figure, and a date.** Not a mood, not a theme, not an inference from tone.

This is the whole skill. There are 168 mistakes and every company is doing something wrong; an assistant that pattern-matches moods onto that list produces a horoscope, and a monthly horoscope is worse than nothing because it trains you to ignore it.

Grade every match:

| Grade | Means | Requires |
|---|---|---|
| **confirmed** | You did this, in the window | A quote or a figure, with a date and a source — **and it has to be evidence of the behavior this mistake names, not an adjacent one** |
| **suspected** | The pattern fits, but the evidence is an absence, or it shows a nearby behavior rather than the one named | Name precisely what you have and what it falls short of, and the one thing that would settle it |
| **closed** | Live in an earlier run; the evidence now says otherwise | What changed, and the date it changed |

The second half of the `confirmed` requirement is the one that gets skipped, because dated evidence *feels* like proof and the grading question quietly becomes "do I have a quote" instead of "a quote of what."

**A gap is a suspected, never a confirmed.** "No one mentioned the pipeline in four weeks of standups" is a real observation about a record and a fair suspicion about #8; it is not proof the meeting isn't happening. An absence in your sources is evidence about your sources.

**A process working badly is not the same finding as a process not existing.** #8 is *No meeting cadence with sales*. A sales meeting that happened and skipped the pipeline is evidence about the quality of that cadence, dated and quotable and entirely real — and it argues against #8 rather than for it, because the meeting took place. That is a `suspected` at most, and usually it is pointing at a different mistake (see step 6).

Watch for this everywhere, not just on #8: **46 of the 168 titles are phrased as absences** — *No…*, *Not…*, *Failing to…*. Every one of them will accept, without complaining, evidence that the thing is merely being done badly. Slow down on that whole class.

If the honest answer for a run is two confirmed and nothing else, that is the answer. Do not pad to look thorough.

## Steps

1. **Read the log.** Note every mistake live at the last run, its grade, and how long it has been live. If there is no log, this is run one — say so in the output and make no trend claims at all.
2. **Read the context.** If `workspace/company-context.md` is missing, proceed, but say plainly what you could not check — chiefly whether they run the preventing play. Do not guess coverage.
3. **Name what you read**, with dates, in section 1 of the output. If a source you expected was missing, say which.
4. **Read for operating behavior**, not sentiment. What was decided, deferred, measured, skipped, or promised. Skip personal and off-topic material entirely — a recording that kept running after the meeting ended, a personal note in a shared folder. Skipped, not summarized, not alluded to.
5. **Match, with evidence.** Grep `MISTAKES.md` for the candidate numbers rather than recalling them. Quote verbatim, with the date.
6. **Test the match against the mistake's own wording, before grading it.** Read the title as written and say which of its words your evidence satisfies. For #8, *No meeting cadence with sales*, the evidence has to bear on whether the cadence **exists**; notes from a meeting that happened do not, however bad the meeting was. Write that sentence down — "the evidence shows X, the mistake claims Y" — and if X and Y are not the same claim, the grade is `suspected` and the difference goes in the evidence cell.

   When they are not the same claim, ask the next question rather than stopping: **which numbered mistake does the evidence actually name?** Grep for it. A cadence that runs but skips the pipeline is a finding about how the preventing play is being run, so check whether it belongs in the context as `lapsed` rather than `absent` — a play whose artifact exists and whose discipline has stopped is the single most useful thing this skill can catch, and it is invisible if the evidence gets filed against an absence mistake instead.
7. **Check the previous run's live list one by one.** Each is still live, closed, or unevidenced this period. "Unevidenced this period" is not closed — say so and keep it live with a note.
8. **Find the preventing play** for every confirmed match, from that mistake's `Prevented by` line in `MISTAKES.md` (generated from each play's `preventsMistakes` frontmatter — that graph is the source of truth, so do not invent a pairing). Then check the context: do they run it, is it absent, or is it unchecked? Fourteen of the 168 have no play mapped. If yours is one, say so — that is a `play-hunt` finding, not a hole in your operation.
9. **Rank by cost** — money, months, or a customer at risk. Not by how confident you feel.
10. **Write the log entry, then the output.**
11. **Update the context** with any coverage fact or fit input the sources revealed, per `_shared/workspace.md`.

## Output

Capped. Reporting fifteen live mistakes is the same as reporting none.

**0 · In one line** — how many are live, how many are new, and the most expensive one by name and number. On a first run, say it is a first run and that there is nothing to compare against. Strictly derived from the sections below: if a fact is not in one of them, it does not belong here. One or two sentences, and never a restatement of the evidence — this exists so a founder opening the report for the first time knows what they are looking at before the detail starts, not to preview it.

**1 · What was read** — sources, dates, and anything missing or skipped.

**2 · Since last run** — one line: new, still live, closed. Then a sentence on anything live three runs or more, named. That sentence is the point of the exercise; a mistake in its third month is a different conversation from a new one, and it should read like one.

**3 · The three that cost the most.** For each, in this order and nothing else:

- The evidence — quote or figure, dated.
- The mistake number and title.
- What it is costing, stated concretely.
- The preventing play, and whether the context says you run it.
- One next step, owned.

**4 · Also live** — everything else, one row each, as a markdown table with this header, verbatim:

```markdown
| # | Mistake | Grade | Runs | Evidence | Preventing play | Running it? |
|---|---|---|---|---|---|---|
| 38 | No agendas for meetings | suspected | 1 | No agenda in any of 4 Aug standup notes; nothing says one wasn't circulated elsewhere — one calendar invite would settle it | KPI & Strategic Meetings | [not asked] |
```

The header row and the `|---|` separator beneath it are both required — without the separator the table renders as one collapsed line in most readers. Keep the columns in that order and do not add any.

**5 · Closed since last run** — what changed, with the date.

**6 · Not checked** — categories your sources said nothing about. A month of sales standups is silent on Development, and silence is not a clean bill of health.

## Voice

Founders read this about themselves. Say the hard thing plainly, once, and then stop. No softening a finding into a suggestion, no stacking three more sentences onto a point that already landed, no moralizing about what it says about the company. Evidence, number, play, next step.

If the evidence is thin, that is a fact about the evidence — report it as one instead of hedging the finding into mush.

## `workspace/mistake-log.md`

This skill owns the file. Newest run at the top, one dated block per run, appended above the last. Never rewrite an old block; a grade you got wrong in June is part of the record.

```markdown
# Mistake log

## 2026-08-29 · monthly · run 3

**Read** — Aug standups (4, 2026-08-04→25), board deck 2026-08-21, #leadership export 2026-08-01→28.
**Movement** — 6 live (2 new, 4 carried), 1 closed.

| # | Mistake | Grade | First seen | Runs | Evidence | Preventing play | Running it? |
|---|---|---|---|---|---|---|---|
| 75 | Counting deals as won before docs are signed | confirmed | 2026-06-27 | 3 | "Northwind's closed" — board deck 2026-08-21; MSA still in redline per legal thread 2026-08-25 | Pipeline Management & Review | no |
| 38 | No agendas for meetings | suspected | 2026-08-29 | 1 | No agenda in any of 4 Aug standup notes; would be settled by one calendar invite | KPI & Strategic Meetings | [not asked] |

**Closed** — 96 · Not using a CRM. In use since 2026-07; 14 of 16 open deals carry a next step (export 2026-08-28). Closed 2026-08-29.
**Not checked** — Development, Vendor. No source touched either.
```

Rules for the file:

- One row per mistake per run. `Runs` is consecutive runs live including this one; reset it to 1 when a closed mistake reappears, and note the reopening.
- `First seen` never changes once written.
- Grade every row. A row without a grade is not a finding.
- On a `suspected` row, the evidence cell carries both halves: what you actually have, and what it falls short of proving. "No agenda in any of 4 Aug standup notes" is half a cell; the example above shows the other half.
- Name plays by their exact title from `plays/README.md`.
- Quotes stay verbatim, with dates. This file holds real names and real numbers, so it lives in `workspace/` and nothing from it is ever pasted into anything bound for the upstream repo.

## Writing back

Update `workspace/company-context.md` in the same run and bump `refreshed:`:

- **Play coverage** you actually observed. Only write `[absent]` when you checked; an unmentioned play is `[not asked]`. Where the evidence shows a play's artifact exists but its discipline has stopped, that is `lapsed` in `commitments.md`, not `[absent]` in coverage — see `_shared/workspace.md`. `lapsed` is the value this skill is best placed to catch and the one an assistant will reach for last.
- **Fit inputs** that appeared with a date — a cash figure in a board deck, a headcount, an ARR number. Carry the `As of` date from the source, not today's.
- **Known conflicts** where a figure disagrees with what the context holds. Record both. Two ARR numbers in one month is itself a finding.
- **Open questions** — the one thing that would settle each `suspected`.

## Handing off

- **`playbook-triage`** owns prescribing a program. This skill does not. When the picture has changed materially since the last triage — a new confirmed mistake in a category that was clean, a preventing play the context says is `lapsed`, or three or more live at once — say so in one line and stop there.
- **`run-play`** for a single play that a confirmed mistake points straight at.
- **`play-hunt`** when you see a costly behavior that no numbered mistake names. Do not invent a number for it; that is a mistake candidate, and numbering happens at authoring time.

## Guardrails

- Never cite a mistake number you have not read in `MISTAKES.md` this run.
- Never report a confirmed match without a dated quote or figure.
- Never grade a mistake that names an absence — *No…*, *Not…*, *Failing to…* — off evidence that the thing happened and went badly. That is a different finding, and often a different number.
- Never treat a silence in the sources as an observation about the company.
- Never claim a trend on the first run.
- Never downgrade an unknown into an absence, in the log or in the context.
- Nothing enters `commitments.md` from this skill. A next step is a proposal until the founder says yes.
