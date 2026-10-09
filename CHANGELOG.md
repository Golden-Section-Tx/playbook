# Changelog

Substantive changes to the plays and the mistakes list. Generated-file churn is
not recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Mistake numbers are permanent and are never reused, so a removed mistake is
recorded as removed rather than renumbered.

## [Unreleased]

### Added

- **Play 74, AI Vendor Continuity** (`plays/vendor/saas-ai-vendor-continuity.md`)
  — Vendor, quarterly, CTO/Founder/CFO. Ranks the ways a company loses access to
  the models its product depends on, in the order they actually happen: commercial
  deprioritization first, capability drift second, physical or regulatory
  interruption last. Sets the rule that a failover which has never carried
  production traffic is not a failover, sizes committed capacity against the
  revenue at risk, and lists the documents that separate an owner-operator from a
  reseller.
- **Mistake 170, Assuming your model vendor will keep selling you capacity.**
- **Five sales and management plays**, numbers 82 to 86. **Sales Triad** reduces a
  sales plan to three decisions on one page, who you sell to (company and title),
  what you say and how you reach them, and has the founder test all three by
  dialing a list of about 2,000 in-profile prospects and talking to dozens.
  **Outbound Channel Test** runs each outbound channel, live or automated, as a
  time-boxed test against floors written in advance. **Sales Call Review** scores
  a weekly sample of recorded calls against five gating questions and tracks
  touches per closed deal by rep. **Sales Leader Hiring Trigger** sets the
  conditions, budget and 90-day plan for hiring a sales leader, and warns against
  promoting the top rep by default. **Underperformer Consequence Ladder** (Executive)
  is a written four-rung ladder with a shortcut for dishonesty.
- **Cross-references** from Go-to-Market Strategy (12) to Sales Triad and from
  Sales Org Chart (27) to Sales Leader Hiring Trigger and Sales Call Review. No
  other existing play text changed.

- **The Exit Playbook** (`EXIT-PLAYBOOK.md`) — a sequence of eight executive plays
  that takes a founder from defining the exit to negotiating it, with an
  introduction and a guide to where to start by time to exit. Builds on the
  existing Meaningful Exit Plan (72) and adds plays 75 to 81:
  **Exit Roadmap** (a dated exit window and gaps sequenced by lead time, structural
  work first), **Exit Data Room**, **Founder Independence (The Vacation Test)**,
  **Pre-Sale Value Levers**, **Selecting an Investment Banker**,
  **Running the Company During a Sale** and **Negotiating the Exit**. Number 74
  is AI Vendor Continuity, below.
- **Skill `leader-time-audit`** — a leader's stated priorities against where
  their calendar, meetings and email show the time went.

- **Play 70, Board Meeting Preparation** (`plays/executive/saas-board-meeting-prep.md`)
  — Executive, quarterly, Founder/Board/CFO. Covers what goes in front of a board
  before the meeting and what the meeting itself is for: the plan of record, the
  packet, the recorded walkthrough sent a week ahead, and an agenda built backwards
  from one or two decisions the founder is genuinely unsure about.
- **Mistake 168, Building the board meeting to win approval instead of to get help.**
- **`EFFORT.md`** — what the story points on every play mean. A point is one
  person's working time; the scale runs 1 SP (one meeting) to 34 SP (three
  person-weeks) with a person-day column. Also states what the points do *not*
  do: they size one play rather than summing across several, and they say
  nothing about elapsed time. Generated from `EFFORT_SCALE` in
  `scripts/build.mjs`, which now also rejects an off-scale effort value and
  renders the legend into `plays/README.md` and `dist/playbook-full.md`.
- **A `Days/wk` column** in the "Who we have" table of
  `skills/_shared/company-context.template.md` — how much of a week each owner
  can give to playbook work. `context-interview` asks for it, and it is what
  turns an effort estimate into a date.

### Changed

- **Stale counts corrected.** Hand-authored counts moved to 86 plays, 170 mistakes and 60
  templates in `README.md`, `package.json`, `templates/README.md` and the three
  skills that quote them (`play-hunt`, `context-interview`, `field-report`).
  `llms.txt` now takes its template count from `templates/` instead of a
  hard-coded 59. The measured counts in `skills/play-forge/references/play-anatomy.md`
  are dated 2026-08-26 and were left as measured. Two derived figures were
  recomputed from the graph: mistakes with exactly one preventing play in
  `playbook-triage` (was 59, now 53) and mistakes with no play in `mistake-watch`
  (was twelve, now four).
- **Play 7, Board of Directors** — the "Create the content plan" step no longer
  carries its own packet contents list and 48-hour send window. Both now live in
  Board Meeting Preparation, and the step points there. The four items unique to
  the old list (operational statistics, gross margin and support hours by customer)
  were folded into the new play's contents so nothing was lost.
- Hand-authored counts in `README.md`, `CONTRIBUTING.md` and `package.json` brought
  up to 70 plays and 168 mistakes. They had been stale at 63 and 161 since the
  1.0.0 release.
- **`run-play` schedules off the play's own estimates.** A new "Effort and dates"
  section converts `initialEffort` to person-days, divides by the owner's
  `Days/wk` for the elapsed span, distributes the days across the play's steps,
  and schedules the recurrence at `ongoingEffort` per occurrence with the annual
  figure quoted once. The "do not invent effort" guardrail now says to convert
  it and show the arithmetic, and adds a rule to escalate rather than quietly
  stretch dates when the arithmetic does not fit.
- **`playbook-triage` prices prescriptions in person-days**, not points, since
  the point-to-day curve is not linear and points do not sum. Ongoing load is
  now annualized against the cadence and set against the team's `Days/wk`.
- **`field-report` asks for actuals in person-days**, and for elapsed time and
  availability as separate figures. It previously told contributors there was no
  defined conversion and not to invent one — true until `EFFORT.md` existed.
- `play-hunt`, `play-forge` and `schema/play.schema.json` link to `EFFORT.md`
  rather than restating the vocabulary, and `play-forge` now asks an author to
  say the estimate out loud as a duration before writing the number.
- **`mistake-watch` grades against what a mistake actually names.** From a field
  test: #8, *No meeting cadence with sales*, was graded `confirmed` off notes
  from a sales meeting that happened and skipped the pipeline — dated, quotable
  evidence that argues against #8 rather than for it. The skill already carried
  the rule, and already used #8 as its example, but the rule sat in prose while
  the grade table asked only for "a quote or a figure, with a date and a
  source". The `confirmed` row now also requires that the evidence be of the
  behavior the mistake names; a new step 6 makes the assistant write out what
  the evidence shows against what the mistake claims before grading, and then
  go looking for the number that does fit. 46 of the 168 titles are phrased as
  absences and the skill now says so, because every one of them will accept
  evidence that a process merely ran badly. Two matching guardrails added, and
  a play whose artifact exists but whose cadence stopped now routes to `lapsed`
  in `commitments.md` rather than `[absent]` in coverage.
- **`mistake-watch` output** opens with a one-line summary — live, new, and the
  most expensive one by name — strictly derived from the sections beneath it,
  for readers meeting the report for the first time. The "Also live" section now
  specifies its markdown table with a header and separator row instead of an
  inline list of column names, which is why it was rendering collapsed.

### Notes

- Mistake 70, *Mistaking communication brevity for clarity*, now has a play mapped
  to it for the first time. Unmapped mistakes drop from 13 to 12: 3, 18, 40, 41,
  62, 82, 98, 99, 105, 110, 140, 146.
- 267 play-mistake edges, up from 257.

## [1.0.0] — 2026-08-23

First public release.

### Added

- **`MISTAKES.md`** — all 161 mistakes, each with a permanent `#mNNN` anchor,
  its category, and the plays that prevent it. Lifted out of the hand-authored
  HTML on goldensection.com, which had been the only home for them.
- **`plays/`** — 63 plays across six categories: Executive 11,
  Sales & Marketing 21, Customer 8, Operations 8, Development 13, Vendor 2. One
  Markdown file each, with structured frontmatter carrying owners, effort in
  story points, cadence, stage, and the mistakes the play prevents.
- **`templates/`** — 59 Excel templates, binder-numbered, mapped to plays by
  slug.
- **`scripts/build.mjs`** — generates every cross-reference from the plays'
  `preventsMistakes` frontmatter, so the play↔mistake graph has exactly one
  source of truth and cannot drift. Also validates frontmatter, anchors,
  numbering, and template references, and fails CI when committed generated
  output is stale.
- **`dist/playbook-full.md`** — the whole corpus as one file, with attribution
  and license in its header so both travel with the text.
- Governance and licensing: [CC BY-SA 4.0](LICENSE) for content,
  [MIT](LICENSE-CODE) for tooling, marks reserved in [NOTICE](NOTICE),
  [CLA](CLA.md) for inbound contributions, [GOVERNANCE.md](GOVERNANCE.md) for
  merge authority.

### Notes

- 227 play↔mistake edges, matching the website's own count exactly — the
  extraction lost nothing.
- 14 mistakes have no play mapped yet: 3, 18, 40, 41, 62, 70, 81, 82, 98, 99,
  105, 110, 140, 146. They are marked in place. Pairing them is open work.
- 7 plays are not mapped to any mistake: company insurance, customer
  onboarding, support metrics, license register, open-source register, security
  documentation, security process. Also open work — several of these plainly
  prevent mistakes that exist in the list.
- `stories/` is empty by design; it fills as stories can be told with the
  identifying detail properly removed.
