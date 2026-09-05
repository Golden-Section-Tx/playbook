# Field report — template

Copy everything below the line into a blank issue on
`github.com/golden-section-tx/playbook`, titled `Field report: <play-slug>`.
Fill it in, delete the guidance comments, and read it once more for names and
numbers before you post. The issue is public the moment it opens.

Guidance sits in `<!-- comments -->`, the way the repository's own issue
templates do it. Leave a field out rather than guess at it — an empty field is
information, an invented one is not.

---

**Play**

<!-- The slug exactly as the filename spells it, e.g. saas-cash-flow-forecast.
     Not the title. -->

**Basis**

<!-- How many companies, how many runs, over how long. Be blunt: "One company,
     one run, four months" is a fine answer and tells the maintainers exactly
     how much weight to put on the rest. -->

**Stage when we ran it**

- [ ] Pre-Revenue
- [ ] Early Traction
- [ ] Growth

<!-- The stage you were at when you ran it, not the stage printed on the play.
     If they differ, that is itself a finding — say so under "What the play got
     wrong". -->

---

## Effort

<!-- The most valuable section here. It is how the story points get accurate,
     and you can answer it completely honestly without revealing anything about
     your company.

     Give person-days — EFFORT.md maps the scale (3 SP = one day, 13 SP = one
     person-week, 34 SP = three), so person-days land straight against the
     estimate. Points are fine if that is how your team sizes; pick one unit
     and label it. A point is one person's working time, so two people for a
     day is two days. "Ongoing" is ONE recurrence, not the year. -->

|  | Play says | We actually spent |
|---|---|---|
| Initial (standing it up) | | |
| Ongoing (per recurrence) | | |

**Elapsed time and availability**

<!-- Effort and calendar are different numbers and both are useful. How long
     did it take end to end, and roughly how much of the week did the owner
     actually have for it? Five person-days over six weeks at half a day a
     week is not a bad estimate — it is a scheduling fact the plan should
     have anticipated. -->

**Where the time actually went**

<!-- The part the estimate missed. Waiting on someone else, pre-work the play
     assumed was done, a step that took four sessions instead of one, data that
     had to be rebuilt before step 1 was possible. -->

**If we stopped partway**

<!-- Which step you stopped at, and what you had spent by then. A play people
     abandon at step 6 has a step-6 problem, and nobody upstream can see it. -->

---

## What happened

**What we adapted, and why it was necessary**

<!-- The change, then the reason. A change without a reason is noise; the reason
     is what lets a maintainer decide whether the play should change or whether
     your situation was unusual. One bullet per adaptation. -->

**What it produced**

<!-- The artifact that exists now and didn't before — the model, the register,
     the dashboard, the document. "Nothing" is a legitimate and useful answer.
     Describe the artifact; do not paste it. -->

**Did the cadence hold**

<!-- The play's frequency against what actually happened after the first month.
     Say which month it slipped, who was meant to own it, and what displaced it.
     "Ran twice, then stopped when the quarter closed" is the answer everyone
     recognizes and nobody writes down. -->

**Outcome at 30 days**

**Outcome at 90 days**

<!-- What changed because the play ran — a decision made differently, a number
     that moved, a problem caught early, nothing at all. "Too early to say" is a
     real answer. Keep figures relative, never absolute. -->

**Did the mistake recur anyway**

<!-- Take the numbers from the play's preventsMistakes and answer each one:
     prevented, recurred anyway, or not yet tested. A play that ran properly and
     did not prevent its mistake is the single most useful line in this report.

     e.g.
     - #m016 — prevented; the forecast caught it two months out.
     - #m073 — recurred anyway; the play produces the number, but nothing in it
       makes anyone act on the number. -->

---

## What the play got wrong

**Wrong**

<!-- A step that is out of order, a formula that does not work, an estimate that
     is not close, a stage that is too early or too late. -->

**Missing**

<!-- What you had to work out yourself that the play should have told you. -->

**Assumed a role we don't have**

<!-- The play names players. If it assumes a CFO, a CS Lead, or a Product
     Manager and you have none, say who ended up doing it and what that cost.
     This is the most common reason a play does not survive contact with a
     twelve-person company. -->

**Would we run it again**

<!-- Yes, no, or yes-with-the-adaptation-above. One line. -->

---

## Provenance

Source:

<!-- Required, and stated at a level that identifies nobody. Good: "One run at
     one company, 2026." Good: "Three runs across two portfolio companies over
     18 months." Not acceptable: a company name, a person's name, or a figure
     specific enough to identify either. -->

## Before posting

- [ ] No company name, person's name, customer name, or investor name anywhere
      in this text — including the title
- [ ] No figure specific enough to identify a company; revenue, headcount, and
      customer counts are relative or absent
- [ ] Nothing quoted verbatim from a private conversation, board packet, or
      customer call
- [ ] Nothing pasted from `workspace/`
- [ ] The founder has read this exact text and said yes to posting it
