---
name: artifact-review
description: Checks something a company already has — a cash model, a pricing matrix, an ARR schedule, a roadmap, a contract register — against the play that governs it, and returns whether it satisfies the play's purpose, which steps are evidenced, and which mistakes are still live despite having it. Use when someone asks whether what they have is good enough, wants a spreadsheet or document reviewed, or claims they already run a play.
---

# artifact-review

Most companies have more artifacts than plays. There is a spreadsheet called
"cash model" that nobody has put actuals in since March, a pricing matrix that
was built once and never revisited, an ARR schedule that counts unsigned deals.
Having the file is not running the play, and the gap between the two is where
the mistakes live.

This skill closes that gap in one direction: take a thing that exists, hold it
against the play that governs it, and say plainly whether it does the job.

It is also the cheapest way to make the context file honest. Every review turns
a `[not asked]` into a finding — see "Write it back" below, which is not an
afterthought but half the point of the skill.

## What you need

- **The artifact.** A spreadsheet, a document, a screenshot, a link, or a
  description of what it contains if that is all that is available. A described
  artifact yields a weaker review, and the output should say so.
- **The play.** If the founder names it, use it. If not, find it: match on what
  the artifact is trying to be, using `plays/README.md` and the `keywords` and
  `questions` in each play's frontmatter. Confirm the match before reviewing —
  reviewing a pricing sheet against the wrong play wastes everyone's time.
- **The play's body**, read in full. The frontmatter cannot tell you what the
  play is for; the body can.
- **`workspace/company-context.md`** if it exists, for stage and roles. The
  review works without it.

## How to review

1. **State the play's purpose in one line** before looking hard at the artifact
   — what the play exists to produce, and what it would be pointless without.
   Write this down first. Deciding it after reading the artifact means grading
   the artifact against itself.

2. **Walk the play's steps against the artifact.** For each numbered step, mark
   it **evidenced** (the artifact shows this was done), **missing** (it wasn't),
   or **not visible** (it may have happened outside the file). Be strict about
   the difference between the second and third: a cash model does not show you
   whether the founder ran the whiteboard session, and claiming it does is
   inventing evidence.

3. **Compare against the play's template** where it has one. The 59 templates in
   `templates/` are working models — structure, formulas, worked examples. A
   founder's artifact does not need to match the template's shape, but a
   template column that has no counterpart anywhere in their file is usually a
   real omission rather than a stylistic difference.

4. **Check the mistakes.** Every play declares the mistakes it prevents. For
   each, ask whether *this* artifact actually prevents it. This is where the
   review earns its keep: an ARR schedule that includes unsigned pipeline does
   not prevent #75, and a cash model built on best-case assumptions does not
   prevent #16 no matter how detailed it is. Having the artifact and still
   holding the mistake is the most valuable finding this skill produces.

5. **Grade it.** One of four:
   - **Running** — satisfies the play's purpose and its cadence is being held.
   - **Nominal** — the artifact exists and is broadly right, but the cadence has
     lapsed or a step is missing. Name what would make it Running.
   - **Hollow** — it looks like the artifact but does not do the job. The
     dangerous one, because everyone believes the play is covered.
   - **Absent** — what was reviewed is a different thing than the play produces.

   Say which, in one word, before the detail. A founder should be able to read
   the first line and know.

6. **Check the cadence, always.** Almost every play ends in a recurrence, and
   recurrence is what fails first. When was this last updated, by whom, and does
   that match the play's `frequency`? An artifact last touched two quarters ago
   is Nominal at best regardless of how good it is.

## What to say

Lead with the grade and the one-line reason. Then:

- **What it does well.** Specific, not encouraging. If the unit economics behind
  the model are sound, say that; it tells the founder what not to touch.
- **What is missing**, ordered by what it costs — each tied to the play step it
  comes from, and to the mistake it leaves live.
- **The one change** that would move the grade up a level. One. A list of nine
  fixes gets none of them done.
- **Cadence and owner** — who keeps this current, at what interval, starting
  when. Absent that, the review will be true again in a year.

Do not rewrite the artifact unless asked. The review's job is to tell the truth
about it; `run-play` is the skill that rebuilds one.

## Write it back

Every review is an answered question, and the context file should absorb it. In
the same run:

- Move the play from `[not asked]` to `Running` or `Absent` in the coverage
  table, with the review's date.
- Add any fit input the artifact revealed — an ARR figure, a churn rate, an ACV
  — with its `As of` date and the artifact as its source.
- Where the artifact's numbers contradict what the context already says, do not
  overwrite. Put both in Known conflicts with their dates. A cash model saying
  one thing and the context saying another is a finding in itself.
- Bump `refreshed:`.
- File the review at `workspace/reviews/<play-slug>-<date>.md`.

A company that reviews four artifacts has a better context file than any
fifteen-minute interview could produce, because the answers came from documents
rather than memory.

## Guardrails

- **Grade the artifact, not the founder.** The tone is a mechanic looking at an
  engine, not an examiner. Say the hard thing plainly and once — "this model
  cannot tell you when you run out of cash" — then move to what fixes it.
- **A Hollow grade needs its evidence in the same breath.** Never assert that
  something looks right but isn't without showing exactly which step or which
  mistake it fails.
- **Never invent evidence from a described artifact.** If the founder is telling
  you what is in the file rather than showing you, every finding is provisional
  and the review says so at the top.
- **Do not grade against a better artifact you have imagined.** The bar is the
  play, which is deliberately achievable. A model that satisfies the play and
  offends your sense of elegance is Running.
- **One play per review.** An artifact serving two plays gets two reviews; the
  grades are usually different, and averaging them helps nobody.
- Where the play itself is wrong for this company — it assumes a role they will
  never have, or a motion they do not run — that is worth capturing for
  `field-report` rather than held against the artifact.
