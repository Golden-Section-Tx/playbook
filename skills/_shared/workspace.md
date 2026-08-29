# The workspace — shared contract

Every founder-facing skill reads from and writes to `workspace/` at the root of
the fork. This file is the contract between them. Read it before writing to
anything in there.

## Layout

```
workspace/
  README.md              the only tracked file — explains the folder to a human
  company-context.md     written by context-interview, kept current by the others
  commitments.md         the plays you have committed to run, and where each stands
  plays/<slug>/          one folder per play in progress
    plan.md              the assigned, dated plan run-play produced
    notes.md             what actually happened
    artifacts/           filled templates, drafts, whatever the play produces
  reviews/               artifact-review outputs, one per review
  mistake-log.md         mistake-watch history, newest first
```

Everything in `workspace/` is yours and never leaves your machine. See
"Privacy" below — it is a real constraint on how these skills behave, not a
disclaimer.

## Rules every skill follows

1. **Read the context first.** If `workspace/company-context.md` is missing,
   do not invent one silently: say it is missing, offer `context-interview`,
   and either proceed with what the founder tells you inline or stop. Never
   fabricate a fit input to fill a gap.

2. **Age each claim, not the file.** A context refreshed last week can rest on a
   cash figure from five months ago. Use the `As of` column. When a prescription
   leans on a claim, state that claim's age, not the file's.

3. **Write back what you learn.** Any skill that discovers a fit input, a
   coverage fact, or a conflict updates `company-context.md` in the same run and
   bumps `refreshed:`. This is how the context gets good without a second
   interview. Update in place, and where you overwrite a value, keep the old one
   in the Known conflicts table if the two disagree rather than silently
   replacing it.

4. **`[not asked]` is not `[absent]`.** Only write `[absent]` when something was
   actually checked. Downgrading an unknown to an absence is how a plan ends up
   prescribing work that already exists.

5. **Commitments are the founder's, not the assistant's.** Nothing enters
   `commitments.md` without the founder saying yes to it. A skill may propose;
   only a person commits.

6. **Append and date.** Logs and notes append. When you replace a block, move
   the old one below with its date. A founder should be able to see what they
   believed three months ago and what changed.

## commitments.md

The register of plays in progress — the heart of the loop. One row per play.

| Play | Category | Committed | Owner | Status | Next checkpoint | Prevents |
|---|---|---|---|---|---|---|

`Status` runs: `committed` → `in progress` → `running` (the artifact exists and
its cadence is being held) → `lapsed` (it existed and the cadence stopped) →
`done` (for plays that genuinely end).

`lapsed` is the most useful value in the table and the one an assistant will
want to avoid writing. A play that produced an artifact nobody has updated in
two quarters is not running, and saying so is the point of tracking it.

## Privacy — the part that constrains behavior

`workspace/` is gitignored, so nothing in it is committed or pushed by default.
That protects a founder who never thinks about it, but it is not absolute, and
skills should behave as though it isn't:

- **Never paste workspace content into anything bound for the upstream repo.**
  Not into a play, a mistake, a field report, an issue, a commit message, or a
  branch name.
- **Anything contributed upstream is anonymized at the moment of writing**, not
  cleaned up afterwards. No company name, no founder name, no figure specific
  enough to identify either.
- **Contributions are built on a clean branch off upstream**, never on the
  branch where the workspace has been in use — a pull request carries every
  commit on its branch, not just the file you meant to change.
- If a founder asks to commit their workspace deliberately, tell them plainly
  what that means: a fork is one visibility change away from public, and git
  history keeps what you delete. Point them at a private repository instead.

`scripts/check_private.py` at the repo root reports exactly what would leave the
machine. When a founder is about to push or open a pull request, run it.
