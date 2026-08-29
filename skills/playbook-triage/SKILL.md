---
name: playbook-triage
description: Diagnoses which of the 168 Golden Section mistakes are live in your company, prescribes at most three plays to run now in prerequisite order, states plainly what is being skipped and which numbered mistake each skip accepts, and records in workspace/commitments.md only the plays you explicitly say yes to — use when deciding what to run this quarter, when the playbook feels like 63 things at once, or when someone asks "where do we start".
---

# playbook-triage

Sixty-three plays, 168 mistakes, one quarter, one team that is already busy. Triage is the skill that turns that into three things and a written record of what you chose not to do.

The hard part is not finding a play worth running. Almost all of them are. The hard part is being honest about the sixty you are skipping, so that when one of those mistakes lands you recognize it as a decision you made rather than a surprise.

Pairs with `run-play`, which turns a committed play into an assigned plan.

## What it reads

| Source | Why |
|---|---|
| `workspace/company-context.md` | Fit inputs, roles, play coverage, conflicts. Read `_shared/workspace.md` before you write anything back. |
| `plays/README.md` | Owners, cadence, initial and ongoing story points, and the mistakes each play prevents. |
| `MISTAKES.md` | The numbered list. Cite by number and anchor — `#142`, `#m142` — because numbers are permanent and titles are not. |
| The bodies of every candidate play | Non-negotiable. Prerequisites, and what step one actually produces, live only here. |

The corpus, if there isn't a clone at hand:

```bash
git clone https://github.com/golden-section-tx/playbook.git
```

## Steps

1. **Read the context and age every claim it carries.** Not the file — the claim. A context refreshed last week can rest on a cash figure from five months ago. When the prescription leans on a number, print that number's `As of` date next to it.

2. **List the mistakes that look live.** Work from "what hurts most this quarter", from the fit inputs, and from the `Absent (checked)` column of play coverage. Aim for eight to fifteen candidates, each by number. Mark each `confirmed` (something in the context says so), `likely` (the pattern fits), or `suspected`.

3. **Map mistakes to plays.** Use `preventsMistakes` in the play frontmatter, or the generated `Prevented by` lines in `MISTAKES.md` — same graph, one direction each. Count preventers per mistake while you are there; you need that number in step 8.

4. **Read the bodies of the plays that survive.** Every one. This is where prescriptions go wrong.

5. **Note the stage, then set it aside.** See below — it is a note, never a filter.

6. **Price it in story points** against who actually owns what.

7. **Cut to three, in prerequisite order.**

8. **Write the output**, including the "Not now" section, and stop. Nothing enters `commitments.md` until the founder says yes.

## Unknown coverage gets a conditional prescription, never a question

Most honest context files are mostly `[not asked]`. A rule that converts unknowns into questions returns an empty page, which is worse than a wrong answer because it looks careful.

So prescribe anyway, and carry the uncertainty in the wording:

> **Run Cash Flow Forecast** (Executive · Founder, CFO · 13 SP initial, 8 SP ongoing, monthly). Coverage is `[not asked]`. If a model already exists and is updated monthly with actuals, this is a cadence correction rather than a build — roughly 3 SP, and step 5 is the whole of it.

Then put the coverage question on the ask list. One prescription, one question, no gate.

`[absent]` is a finding; `[not asked]` is a question. Never quietly promote one to the other to make a prescription look better founded.

## Conflicts outrank unknowns

A `conflict:` row is worse than a blank one. Two ARR figures, two churn numbers, two runway estimates — all of them read as certain, and one of them is wrong.

Any prescription resting on a conflicted input is **provisional**, labeled as such. Resolving the conflict becomes the first question on the ask list, ahead of every coverage question. A disagreement about your own numbers is itself a finding, and often the most useful one in the run.

## Stage is a note, and the tax runs one way

Verify this against the corpus rather than trusting the count here — 26 plays are tagged `Pre-Revenue`, 28 `Early Traction`, only 8 `Growth`, and one (Executive Execution) `All Stages`. There is no dense set of late-stage plays to graduate into.

The consequence: **a Pre-Revenue play at a Growth company is not a mismatch. It is a skipped foundation**, and it is frequently the highest-leverage thing available — Budget Creation, Sales Philosophy, Pricing Matrix, the Vendor Contract Register. Prescribe it without apology, and say what it costs to have skipped it this long.

The tax runs the other way. A `Growth` play at a Pre-Revenue company — Quality Management System at 21 SP, Sales Metrics by Role, Channel Partnerships — usually is premature, and the note should say what has to be true first.

Never filter the candidate list by stage. Note it in one clause and move on.

## Prerequisites come from bodies, not from memory

Read the play, then decide. Three failure modes, all seen in real runs:

- **The prerequisite is inside the play.** Cash Flow Forecast's step 1 *is* the unit-economics whiteboard session. Prescribing Unit Economics first spends 8 SP to buy a step the founder is about to run anyway.
- **The prerequisite is genuinely missing.** Then the prerequisite *is* the prescription, and the play that needs it moves to "Not now" with a named condition. Pipeline Management & Review builds on the PDCA loop from Quality Management System and on stage criteria from Pipeline Creation; without those it becomes a status meeting.
- **The prerequisite does not exist in the corpus.** Four executive plays name a Strategic Planning playbook as a prerequisite, and there is no Strategic Planning play. Say so in the output rather than substituting a play that sounds close. It is also a decent candidate for `play-hunt`.

## Capacity, in story points

Sum the `initial` effort of the prescription. Add the `ongoing` effort of everything already `running` in `commitments.md`, at its cadence — 8 SP monthly is not a rounding error. Then look at the `Owners` column against the "Who we have" table.

Two founders and a CTO cannot absorb 60 SP of initial build plus three new monthly cadences, however good each play is. If the arithmetic is implausible, cut to two plays, or one, and say which number made you cut. A prescription nobody has the hours for produces the same outcome as no prescription, minus the honesty.

Where a role is `✗`, name the human who will actually own it. A play with no owner is not committed.

## The "Not now" section is the point

Mandatory. For every play you considered and cut: the play, the mistake numbers that cut accepts, and the condition that would bring it back.

| Not now | Accepts | Revisit when |
|---|---|---|
| Contract Playbook | [#21](../../MISTAKES.md#m021), [#51](../../MISTAKES.md#m051), [#80](../../MISTAKES.md#m080), [#90](../../MISTAKES.md#m090), [#121](../../MISTAKES.md#m121) | First deal above ACV where a customer redlines the MSA |

**Sole-preventer escalation.** 67 of the 168 mistakes have exactly one play preventing them. Where a cut accepts a mistake you marked `confirmed`, whose cost is high, and whose *only* preventer in the corpus is the play being cut, that acceptance does not sit in the table. Pull it above the table, in one sentence, with the condition that would reverse it. Cutting Cash Flow Forecast at a company with nine months of runway accepts [#142](../../MISTAKES.md#m142) and [#136](../../MISTAKES.md#m136) with nothing else in the corpus standing behind them.

And note the floor: 12 mistakes have no preventing play at all. If a live mistake is one of them, no prescription will cover it — say that instead of prescribing something adjacent.

## With no context file

Do not gate on `context-interview`. Ask five questions inline, answer provisionally, then offer the interview.

1. What hurts most this quarter?
2. ARR, growth rate, and runway in months — and when was each last true?
3. Who owns sales, customer success, and finance today?
4. Which of these already run — a cash model, a KPI meeting, a pipeline review, a contract playbook?
5. What did you already try that did not stick?

Label the output provisional, keep it to two plays rather than three, and end with the offer.

## Writing to commitments.md

Only after an explicit yes, and only the plays that got one. A skill proposes; a person commits. Append one row per committed play in the shape `_shared/workspace.md` defines — play, category, date committed, owner, `committed`, next checkpoint, mistake numbers prevented.

In the same run, write back what you learned: coverage facts discovered while asking, any conflict surfaced, new open questions. Bump `refreshed:`. Never overwrite a value with a new one silently — if they disagree, both go in Known conflicts.

Nothing from `workspace/` goes near the upstream repo. If a pattern here is worth contributing, it is anonymized when written, not cleaned up later — `field-report` handles that path.

## Hand-offs

| Next | When |
|---|---|
| `run-play` | A play is committed and needs an assigned, dated plan. |
| `artifact-review` | Coverage says something exists. Review it before rebuilding it — most "we already do that" artifacts are a version behind the play. |
| `context-interview` | The ask list is longer than the prescription. |
| `mistake-watch` | Track whether the accepted mistakes in "Not now" start showing up. |
