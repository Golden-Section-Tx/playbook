---
name: context-interview
description: Interviews the founder for fifteen minutes and writes the result to workspace/company-context.md, the file every other skill in this repo reads — stage, numbers, roles, which plays already run, and where the company's own sources disagree with each other. Use when setting up the playbook for a company for the first time, when the context file is missing or stale, or when someone asks to refresh what the assistant knows about the business.
---

# context-interview

Fifteen minutes, once, and every other skill in this repo stops giving generic
advice. That is the whole trade, and it is worth saying to the founder in those
words before starting.

The output is `workspace/company-context.md`. It stays on the founder's machine
— see `_shared/workspace.md`, which governs how every skill here reads and
writes it.

## Run it on the clock

Fifteen minutes, hard stop. You own the clock, and a short interview that
finishes beats a thorough one that gets abandoned at minute forty.

- **Call the time out loud** at each block boundary: "eight minutes — moving on."
- **One question at a time.** Never a list. A list costs three minutes to answer
  and gets answered badly.
- **Park tangents.** Say "parked," write it into the open questions, continue.
  A founder who starts explaining their competitive landscape is not being
  difficult; they are answering the question they wish you had asked. Park it.
- **At 15:00 you stop**, finished or not. Write the file with everything
  unanswered marked `[not asked]`. A half-filled context file that exists beats
  a complete one that doesn't.

## Ask in order of what changes the advice

The order is not arbitrary. These five change which plays come back more than
everything else combined, so a founder who bails at minute six still leaves with
a usable file.

**0:00–0:02 — What are you, and what hurts.** What you sell, to whom, in which
vertical. Then: what is the thing that, if it were fixed, would make this
quarter go differently? Take the answer as given. Do not diagnose it yet.

**0:02–0:06 — The numbers.** ARR, growth, gross margin, cash, runway,
profitability, retention. Ask for the date on each — "as of when?" — because a
figure without a date cannot be aged later, and aging is what stops a skill
prescribing off a number from last spring.

**0:06–0:09 — Who you actually have.** Walk the roles: founder, exec team,
board, CFO, COO, CTO, sales lead, SDR, CS lead, product manager, engineering
lead, legal. For each, a name or a no. Fractional and part-time count as yes,
with a note — the plays care whether someone owns the thing, not how many hours
they own it for.

Then one follow-up on the two or three names that came up most: **how much of a
week can that person actually give to this, on top of their job?** Half a day,
one day, two. It goes in the `Days/wk` column, and it is the only number that
turns a play's effort estimate into a date — `run-play` needs it to schedule anything and `playbook-triage` needs it
to know what the company can carry — and a founder guessing `0.5` is worth far
more than a blank. Do not walk all twelve roles for this; get the people who
will actually own plays and move on.

**0:09–0:13 — What you already run.** Not "do you have a process for X" — every
founder says yes to that. Ask what exists as an artifact and when it was last
updated. "Is there a cash flow model, and when did someone last put actuals in
it?" The gap between having a spreadsheet and running a play is the whole
subject of this repo.

Mark what you learn as `Running`, `[absent]`, or `[not asked]`. **Only write
`[absent]` when it was actually checked.** Most cells will be `[not asked]` and
that is correct — you have fifteen minutes and there are 70 plays.

**0:13–0:15 — The conflict question, then close.** Ask it exactly like this:
*"If I asked your CRM and your accountant for last quarter's revenue, would they
give me the same number?"*

That single question does more work than any other in the interview. It is
mistake #85 in the list, it is the most common unforced error in the corpus, and
founders never volunteer it. Whatever the answer, write it into Known conflicts.
A hesitation is an answer.

## Ask for documents, not recitation

Any time a founder is about to recite numbers from memory, offer the shortcut:
*"Rather than tell me — is there a board deck, a P&L, a cohort sheet I could
read?"* Faster, more accurate, and it turns the interview into handing over
files rather than an exam.

Read what they give you, fill what it covers, and spend the recovered minutes on
the roles and coverage sections, which no document answers.

## Never guess

The rules in `_shared/workspace.md` are not stylistic. A fabricated fit input
does not stay in this file — it propagates into a prescription, into a plan,
into tasks assigned to real people. `[not asked]` is a real value. `conflict:`
with both figures is better than picking the one that sounds right.

When a founder does not know a number, that is itself information: a company
that cannot state its net revenue retention in an interview does not have a
retention instrument, whatever the coverage table says.

## Close it useful

Do not end with "context saved." Fifteen minutes that concludes with a filing
confirmation feels like paperwork, and the founder will not come back.

End with three things, in under a minute:

1. **The two or three mistakes you already suspect**, by number and name, each
   with the one thing they said that made you suspect it. No prescription yet —
   that is `playbook-triage`.
2. **The single question you most want answered** before the next run, and why
   it would change the advice.
3. **What to do next**: run `playbook-triage` for what to actually do about it.

## Writing the file

Copy `_shared/company-context.template.md` to `workspace/company-context.md` and
fill it. Set `refreshed:` to today. Every value carries its own `As of` date and
source — "founder, in interview" is a legitimate source, and a more honest one
than implying a document that wasn't read.

If the file already exists, this is a **refresh, not a re-interview**. Read it
first, ask only about what has gone stale or changed, and confirm the rest in
one pass. Where a new answer contradicts an old value, do not silently
overwrite: put both in Known conflicts with their dates, and ask which is right.
A founder correcting last quarter's number is the single most useful thing this
skill ever captures.

## When to run it again

- The numbers block, quarterly — or the week after a raise, a layoff, or a
  pricing change.
- The roles block, whenever someone senior joins or leaves — and the days-a-week
  numbers whenever the team's load visibly changes, since every date this
  repo produces is computed off them.
- Everything, if six months have passed.

`artifact-review` and `mistake-watch` keep parts of the file current as a side
effect of being used, so a company running those regularly will need this less
often than a company that ran it once and stopped.
