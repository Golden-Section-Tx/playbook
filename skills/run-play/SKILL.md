---
name: run-play
description: Turns one play the company has committed to into a working plan — tasks derived from the play's own steps, assigned to real people by the roles the play names, dated, with the recurring work scheduled — delivered into the task manager they already use, as a CSV import, or as a PDF with one page per person. Use when someone has decided to run a play and wants it scheduled rather than read.
---

# run-play

A play read is a play not run. This skill takes one play the founder has
committed to and turns it into assigned, dated work in whatever system their
team actually opens.

It runs after `playbook-triage` has selected the play and the founder has said
yes to it. It is the last skill in the founder loop and the one with the most
power to do damage, because it is where a play gets adapted to a company with
nobody checking. Read the two rules under "Do not hollow the play" before
anything else.

## Before you plan

1. **Read the whole play body.** Not the index row. The steps, the background,
   the troubleshooting section — the plan is derived from them, and the
   troubleshooting section usually predicts exactly where this company will
   struggle.
2. **Read `workspace/company-context.md`** for roles, stage, and what already
   exists. If the play is already `Running` in the coverage table, stop and say
   so: this is a cadence correction, and `artifact-review` is the better skill.
3. **Confirm the commitment.** The play should be in `workspace/commitments.md`.
   If it isn't, ask before building a plan for work nobody agreed to.

## Building the plan

**Tasks come from the play's own steps.** Each numbered step becomes one task,
in order, keeping the play's language rather than paraphrasing it. Where a step
has sub-points, those become the task's checklist, not separate tasks — the step
is the unit of work the play intended.

**Dependencies follow the step order**, plus anything the body names as a
prerequisite. A step that requires an artifact from an earlier step does not
start until that one lands.

**The recurring work is a task too.** Nearly every play ends in a cadence: who
owns the artifact once it exists, at what interval, and what they look at. Turn
that into a recurring task at the play's `frequency`, starting one interval
after the last setup task. This is the difference between a project that
finishes and a play that runs, and it is the part a founder is most likely to
drop.

**Dates** anchor to a start date the founder gives you. Space the tasks by the
play's `initialEffort` — a 21 SP play is not a week — and respect what else the
context says the team has committed to. Say what you assumed.

## Assignment — the part that goes wrong

The play names roles in `players`. Map each to a real person using the context's
roles table.

**When the play names a role the company does not have, that is a decision, not
a routing problem.** The failure mode — and it is the default failure mode — is
to quietly assign everything to the founder, producing a plan with fourteen
tasks on one person that dies in week two.

So, when a role is absent, put the question to the founder:

- Who covers this, by name?
- Or does the play wait until that role exists?
- Or does an outside party cover it — a fractional CFO, a bookkeeper, counsel?

If the founder takes it, take it seriously: add the effort to their load, and
say what it displaces. "You are now carrying 13 SP of this play on top of the
two commitments already in your register" is the sentence that prevents a dead
plan.

Where the context has no name for a role that does exist, ask. Do not assign to
a title — nobody opens a task assigned to "CS Lead."

## Delivering it

Use what they already have. Ask once, and take the answer:

1. **Their task manager, if you can reach it.** If a connector or integration
   for their tool is available in this session, create the tasks there. **Show
   the full plan and get an explicit yes before creating anything**, and never
   assign to another person's account without the founder confirming that
   mapping. Creating fourteen tasks in someone's Monday morning without warning
   is a way to lose their trust in one move.
2. **A CSV they import.** Works everywhere, needs no access to their systems,
   and is the right default when no connector exists. Match the destination
   tool's import columns — most take a variant of task, assignee, due date,
   description, and a parent or section. Say which tool the file is shaped for.
3. **A markdown checklist** in `workspace/plays/<slug>/plan.md`, which is
   written either way as the record.
4. **A PDF, one page per person.** Not a consolation prize — for a ten-person
   company it is often better than a task manager. One overview page: the play,
   why it matters in two sentences from the play's own opening, the artifact it
   produces, and the schedule. Then one page per assignee with only their
   actions, their dates, and the one line explaining why their part matters.
   A founder can hand those across a desk.

Whatever the channel, `workspace/plays/<slug>/plan.md` holds the canonical plan,
and `workspace/commitments.md` moves the play to `in progress` with a first
checkpoint date.

## Do not hollow the play

Two rules, and they are the reason this skill is written carefully.

**Name the spine before you adapt anything.** In one line: what this play would
be pointless without. Derive it from the body — the artifact it produces and the
discipline that makes the artifact true. For a cash flow forecast it is
founder-owned conservative assumptions that minimize the capital needed to reach
self-funding; the spreadsheet is not the spine. Write that line into the plan
before writing a single task.

Then adapt only the surface: who owns it when the named role is absent, what the
minimum honest version is at this stage, what cadence this team can actually
hold. **If an adaptation would touch the spine, the company is not ready to run
this play — say that instead of shipping a comfortable version of it.** A
hollowed-out play is worse than no play, because everyone believes it is covered.

**State the spine as an invariant, not as the play's own example of it.** Plays
are written for the common case. A play that says "minimize capital to reach
$5–15M ARR" is expressing an invariant — minimize capital to reach self-funding
— through a growth-stage instance of it. A company that is contracting
substitutes breakeven and runs the same play. Reading the instance literally
would tell them the play does not apply, which is the opposite of the truth.

## Guardrails

- **One play at a time.** A plan covering three plays is a plan nobody executes.
- **Never create, assign, or notify without an explicit yes** on the full plan
  as it will appear.
- **Do not invent effort.** The play's story points are the estimate; where you
  split them across tasks, say that is what you did.
- **Record what actually happens.** `workspace/plays/<slug>/notes.md` takes the
  real dates, the adaptations, and the effort actually spent. Three months later
  that file is what `field-report` contributes back, and effort-actual against
  the play's estimate is the most useful thing a company can give the corpus.
- **The plan is not the play.** Keep a link to the play in the plan so anyone can
  read the reasoning rather than just the tasks.
- Nothing from `workspace/` goes into a commit, a branch name, or anything bound
  upstream — see `_shared/workspace.md`.
