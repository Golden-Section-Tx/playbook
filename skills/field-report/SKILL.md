---
name: field-report
description: Turn a play the company actually ran into an anonymized field report sent back to the Golden Section playbook as a GitHub issue or a pull request — real effort against the story-point estimate, what was adapted and why, whether the cadence held, and what the play got wrong. Use after running or abandoning a play, when a run diverged from the play as written, or when a founder wants to give something back upstream.
---

# field-report

You ran the play. Standing it up took half again what the estimate said. You cut a step because you have no CS Lead. The artifact got built, held for six weeks, and then nobody updated it.

That is the most useful thing anyone can send this corpus, and almost nobody sends it. The 70 plays were written from watching companies operate; they get better the same way. This skill turns one run of one play into a structured, anonymized report and gets it upstream — as an issue, or a pull request.

It is the only skill in this set whose output leaves your machine, so read the anonymization section first. Pairs with [`play-forge`](../play-forge/SKILL.md), which owns authoring — when the report has become a proposed edit to the play, hand off to it.

## Report the failures

"We ran this and it didn't work, and here is why" is worth more than a success story, and it is the report founders swallow. A play that cost a quarter and produced a spreadsheet nobody opened has a defect — a wrong estimate, a missing prerequisite, a step assuming a role a twelve-person company doesn't have. Say so plainly if the founder is only offering the wins, then write the loss down.

## What you need before writing

- **The play as written** — `plays/<category>/<slug>.md`, or `dist/playbook-full.md`. Take `initialEffort`, `ongoingEffort`, `frequency`, `stage`, and `preventsMistakes` from the file, never from memory.
- **The run** — `workspace/plays/<slug>/notes.md` and `plan.md`, the row in `workspace/commitments.md`, and `workspace/mistake-log.md`.
- **The founder**, for what the workspace doesn't hold — real hours, what happened at 90 days, whether they would run it again.

Read the workspace. Never paste from it. See [`_shared/workspace.md`](../_shared/workspace.md).

## Anonymize while you write, not afterward

There is no cleanup pass. A pull request there is public the moment it opens and cannot be unpublished — closing it does not remove it, and neither does deleting the branch.

- No company name, no person's name, no customer or investor name.
- No figure specific enough to identify either. "ARR roughly doubled the year before we ran it" is fine. An ARR number, a headcount plus a city, a named vertical with four players in it — not fine.
- Nothing identifying in a **branch name, commit message, commit author line, file path, or issue title**. The metadata is as public as the diff.
- No verbatim quotes from private conversations, board packets, or customer calls.

Write it anonymous the first time. Redaction afterward is how names survive.

## The report

One report per play. The fill-in structure is [`references/report-template.md`](references/report-template.md) — copy it, fill it, paste it.

| Field | What it carries |
|---|---|
| **Play** | The slug, exactly as the filename spells it. |
| **Basis** | How many companies, how many runs, over how long. |
| **Stage when we ran it** | `Pre-Revenue` · `Early Traction` · `Growth` — the stage you were at, not the one on the play. |
| **Effort** | Estimate against actual, initial and ongoing. See below. |
| **What we adapted** | The change, and why it was necessary. A change with no reason is noise. |
| **What it produced** | The artifact that exists now and didn't before, or the honest absence of one. |
| **Did the cadence hold** | The play's `frequency` against what happened after the first month. |
| **Outcome at 30 and 90 days** | Where known. `Too early to say` beats a guess. |
| **Did the mistake recur anyway** | Each number in `preventsMistakes`, answered. |
| **What the play got wrong** | Wrong, missing, or assuming a role you don't have. |

State the basis in the first line. One run at one company is an anecdote and should say so — maintainers can weigh an honest anecdote, not one dressed as a pattern. Three runs across two companies is a different claim; make it as one.

## Effort is the field that matters

It is how the corpus's story points get accurate, it takes ten minutes, and a founder can answer it completely honestly without revealing anything about their company.

- Give **initial** and **ongoing** separately. A play whose stand-up is fair but whose recurrence costs triple has a different defect from one simply underestimated.
- Story points here are Fibonacci — 1, 2, 3, 5, 8, 13, 21, 34. Give points if your team sizes in points, hours or person-days if that is what you track, and label which. The corpus does not define a point in hours, so do not convert.
- Report the **whole** cost — the two weeks the artifact sat waiting on someone, and the pre-work the play assumed you had done.
- If you stopped partway, say what you spent and where. A play people quit at step 6 has a step-6 problem.

## Issue or pull request

**Default to an issue**, especially for a first contribution. Lower friction, nothing to build, no signature needed, and the maintainers can shape it into what the corpus needs. `CONTRIBUTING.md` says outright that a paragraph of substance in an issue is a complete contribution.

There is no field-report issue template in the repository. Open a blank issue, title it `Field report: <play-slug>`, and paste the filled template. (`.github/ISSUE_TEMPLATE/mistake-report.md` is for a missing mistake, not this.)

**Take the pull request path only when the founder wants to write the change themselves** and can name the line that changes. A report is not a diff. The moment it is really a proposed edit — a corrected `initialEffort`, a rewritten step, a wrong `stage` — hand off to `play-forge`.

On the CLA — nothing is signed to open an issue; the bot prompts on your first pull request. Read [`CLA.md`](https://github.com/golden-section-tx/playbook/blob/main/CLA.md) anyway: it defines a contribution to include what you write in an issue, and grants Golden Section broad rights, including use in commercial products. Content is CC BY-SA 4.0, the scripts MIT, the name and marks not licensed.

## Show the founder the text, then ask

**Never submit anything silently. Ever.**

Before an issue is opened, a branch pushed, or a pull request created, put the exact final text in front of the founder — body, title, branch name, commit message, provenance line — and get an explicit yes. Not "shall I file this?" but the words themselves, as they will appear in public. If you cannot show it, do not send it. If the founder hesitates, the hesitation is usually a detail that would have identified them; find it and cut it rather than reassure them.

## Building a pull request safely

Only after the founder has said yes to the text.

```bash
git remote add upstream https://github.com/golden-section-tx/playbook.git
git fetch upstream
git checkout -b report/<play-slug> upstream/main    # clean, off upstream
```

Never build on the branch the workspace has been used in. A pull request carries **every commit on its branch**, not just the file you meant to change — one stray commit touching `workspace/` and the company's context is public and permanent.

Before pushing:

```bash
python3 scripts/check_private.py        # what would leave the machine
npm run build                           # must exit clean; commit what it regenerates
git log --oneline upstream/main..HEAD   # every commit message and author line
git diff upstream/main..HEAD            # the whole diff, not a summary
```

If your fork predates `check_private.py`, read the last two by hand, every line. Fill in the pull request template honestly, especially the provenance line — `One run at one company, 2026` is the right level of detail.

A scan also runs on the pull request itself, checking the diff against a blocklist Golden Section maintains. It is a backstop on their side, not a substitute for the four commands above — it does not know your company's name, only theirs. If it fails, the instruction is to **close the pull request rather than amend it**: a public pull request cannot be unpublished.

## Guardrails

- **Anonymized at the moment of writing, without exception.** No names, no identifying figures, nothing in metadata. A founder's own story is told with their written permission or not at all.
- **Explicit yes before anything is submitted**, with the exact text shown.
- **Clean branch off upstream**, never the workspace branch.
- **Don't dress up a single run.** State the basis and let the maintainers weigh it.
- **Don't report on a play you didn't run.** A view with no run behind it is an issue in your own words, not a field report.
- **Never edit generated content** — anything between `GS:` markers, the `**Prevented by**` lines, `plays/README.md`, `dist/`.
- Declined however honest: generic startup advice, marketing, restatements, anything not about B2B vertical software.
