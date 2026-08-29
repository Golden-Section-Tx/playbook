---
name: play-hunt
description: Read founder and portfolio meeting transcripts against the Golden Section corpus of 70 plays and 168 mistakes — flag the mistakes visibly in progress, surface new mistake candidates, and hunt new play candidates, each with a short anonymized case study and a scored argument for why it deserves to be a play. Use when reviewing calls, board meetings, or a week of meetings for what the playbook does and does not already cover.
---

# play-hunt

The corpus in this repository came from watching over 400 companies make the same mistakes in roughly the same order. This skill is how that watching continues: read what founders actually said against all 70 plays and 168 mistakes, and come back with three things.

1. The numbered mistakes visibly in progress, with the play that prevents each.
2. The mistakes the list does not have yet.
3. The **new plays worth writing** — each with a short case study and the argument for why it earns a place.

An approved candidate hands to `play-forge`, which owns the drafting and the schema.

## Two modes

- **Single** — one named meeting, founder, or company. Deep read, quote-level evidence.
- **Sweep** — a date range. Every meeting in the window, read together. Cross-meeting recurrence is the point: a pattern seen in two companies is worth more than a vivid one seen in one.

Default to single when a company or meeting is named, sweep when a period is.

## Sources

1. **The corpus.** A clone of this repository, or `dist/playbook-full.md` and `MISTAKES.md` fetched directly:

   ```bash
   curl -sS -O https://raw.githubusercontent.com/golden-section-tx/playbook/main/dist/playbook-full.md
   curl -sS -O https://raw.githubusercontent.com/golden-section-tx/playbook/main/MISTAKES.md
   ```

   Grep these. Never work from a remembered version of the list — the numbers matter and they are permanent.

2. **Transcripts**, from wherever you capture them: a meeting recorder (Fireflies, Otter, Granola, Plaud, Gong, Zoom), a notes database, or plain text files. Where a recorder exposes an API or MCP connector, pull the window directly; where it syncs into a notes tool, read the synced pages. Whatever the source, you need the body of the conversation, not only its summary — summaries drop the sentence that turns out to be the evidence.

3. **Context** — whatever you keep on the company: status memos, board packets, prior notes, and your own watch log from earlier runs. A "new" pattern already in the watch log is a *second observation*, which is a promotion rather than a duplicate.

4. **The attendee list**, when a transcript's speaker labels are ambiguous.

Every finding carries its source and date. A finding without a quote is not a finding.

## Steps

1. Resolve the window and the meeting set. Name what you read at the top of the output — meetings, companies, dates. If a transcript was unavailable, say which and why; do not quietly work from a shorter set.
2. Read each transcript for **operating behavior**, not sentiment. What did they decide, defer, measure, skip, or promise? Skip personal and non-business recordings entirely.
3. **Match against the mistakes.** A match requires a specific observed behavior mapping to a numbered mistake — not a vibe. Note the paired play, and whether the company appears to run it.
4. **Find the gaps.** Where the conversation described real, repeated operating work that no play covers, that is a play candidate. Where it described a costly behavior no numbered mistake names, that is a mistake candidate.
5. **Score every play candidate against the bar** below. Under 4 of 6, it is a watch item, not a candidate.
6. **Write the case study** for each candidate that clears the bar — anonymized at the moment of writing, not later.
7. **File and hand off** as described at the end.

## The bar — what makes a candidate a play

| # | Test | Passes when |
|---|---|---|
| 1 | **Recurrence** | Seen in two or more companies, or once with a cost you can name in dollars, months, or a lost customer. |
| 2 | **Not covered** | The nearest existing play does not produce this artifact. Name that play and say why it isn't it. |
| 3 | **Schedulable** | An owning role, a cadence, ordered steps, and an honest effort estimate all exist. If not, it is an essay. |
| 4 | **Preventive** | It maps to at least one numbered mistake, or to a mistake candidate from this same run. |
| 5 | **In scope** | B2B vertical software. Not generic startup advice, not a restatement of an existing play, not marketing for a service. |
| 6 | **Evidenced** | At least one verbatim quote, with speaker role, date, and source. |

Report the score. `5/6 — fails Recurrence, one company only` is more useful than a confident yes, and it tells the next sweep exactly what to watch for.

## Output

One document, in this order. Findings only — no restatement of the corpus.

**1 · What was read** — meetings, companies, dates, sources, and anything missing.

**2 · Mistakes in progress**

| # | Mistake | Company | Evidence (quote, date) | Preventing play | Running it? |
|---|---|---|---|---|---|

**3 · New play candidates** — the section that matters. For each:

- **Proposed play** — filled in as the frontmatter fields `play-forge` will need, using that skill's closed vocabularies (`play-forge/references/play-anatomy.md`), so drafting never has to go back to the transcript:

  | Field | Value |
  |---|---|
  | `title` / `h1` | Short label · the "How to …" headline |
  | `category` | executive · sales-marketing · customer · operations · development · vendor |
  | `players` | Roles from the vocabulary — Founder, CFO, Sales Lead, CS Lead, CTO, … |
  | `frequency` | Continuous · Weekly · Monthly · Quarterly · Bi-Annually · Annual · As Needed · Per Customer · Per Project |
  | `stage` | Pre-Revenue · Early Traction · Growth · All Stages — earliest stage at which it pays for itself |
  | `initialEffort` / `ongoingEffort` | Fibonacci story points: 1 · 2 · 3 · 5 · 8 · 13 · 21 · 34 SP |
  | `preventsMistakes` | The numbered mistakes it would prevent |
  | The artifact | What the play produces — the thing that exists afterwards that did not before |

  A candidate that cannot fill `players`, `frequency`, and the artifact row is failing test 3 and is a watch item, not a candidate.
- **Case study** — 150–200 words, anonymized, past tense: the situation, what the company did, what it cost or nearly cost, and what a play would have had them do instead. A story, not a transcript summary. This is the part that convinces a reader who was not in the room.
- **Why it should be a play** — the six-test score with the failures named, and one sentence on the mistake it prevents.
- **Nearest existing play** — and the specific reason this is not that.
- **Evidence** — the quotes, with dates and sources.

**4 · New mistake candidates** — stated as a behavior with a consequence, one to three sentences, category, evidence, and the play (existing or proposed) that would prevent it.

**5 · Watch items** — candidates under 4/6, each with the single observation that would promote it. This is the queue the next sweep reads first.

## Keeping the register

Two running files, kept **outside the fork** — they hold company names and quotes, and a fork is one push away from public:

- **`play-candidates.md`** — one row per candidate: play, category, score, companies seen, first seen, status, and the next thing needed. Status runs `watch` → `candidate` → `drafted` → `promoted` → `merged`.
- **`mistake-watch.md`** — the match log (date · company · mistake number · evidence · prescribed play · outcome) and the candidate pen beneath it.

Rows are retired deliberately, by a person, not by an automated run. A candidate that keeps failing the same test for six months is telling you something; deleting it loses that.

## Guardrails

- **Anonymize before anything leaves your notes.** Case studies name no company, no founder, and no figure specific enough to identify either. Inside your own register the names stay, so the evidence remains checkable; the moment a candidate heads toward a pull request, `play-forge`'s anonymization rule governs.
- **Quote, don't paraphrase.** Verbatim, with the date. Mark clearly what the founder said versus what you inferred — inference is allowed, disguising it is not.
- **A candidate is not a play.** Nothing goes to `play-forge` until a person approves it.
- **Never invent a mistake number.** New mistakes are proposed as candidates; numbering happens at authoring time, from the canonical list.
- Transcripts are confidential. What was said in a portfolio meeting stays in your own files, and a personal recording that ended up in the same folder is skipped, not summarized.
- Prefer three well-evidenced candidates to twelve plausible ones. The corpus is worth something because everything in it was earned.
