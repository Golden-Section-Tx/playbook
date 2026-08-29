# Skills

Eight agent skills for working this corpus. They are plain Markdown instructions
— no code, no dependencies, no keys — so they run in Claude Code, in the Claude
desktop and web apps, and in anything else that reads a `SKILL.md`.

The corpus tells you what to do. These tell you **which of it applies to you,
right now, and what to do about it on Monday.**

## For founders

| Skill | What it does |
|---|---|
| [`context-interview`](context-interview/SKILL.md) | Fifteen minutes on the clock, once. Writes `workspace/company-context.md`, which every other skill reads. |
| [`playbook-triage`](playbook-triage/SKILL.md) | Which of the 168 mistakes are live in your company, at most three plays to run now in the right order, and what you are choosing to skip — with the mistake each skip accepts. |
| [`artifact-review`](artifact-review/SKILL.md) | The cash model, pricing matrix, or ARR schedule you already have, held against the play that governs it. Grades it Running, Nominal, Hollow, or Absent. |
| [`run-play`](run-play/SKILL.md) | One play into assigned, dated work — in your task manager, as a CSV import, or as a PDF with one page per person. |
| [`mistake-watch`](mistake-watch/SKILL.md) | Your own meeting notes and records against the 168, monthly, so a mistake live for three runs looks different from a new one. |
| [`field-report`](field-report/SKILL.md) | What actually happened when you ran a play, contributed back anonymized. Including — especially — when it didn't work. |

## For operators, advisors, and contributors

| Skill | What it does |
|---|---|
| [`play-hunt`](play-hunt/SKILL.md) | Meeting transcripts across many companies against the corpus: mistakes in progress, and patterns that deserve to become plays. For someone watching a portfolio, not a single company. |
| [`play-forge`](play-forge/SKILL.md) | Author a play or a mistake to this repository's exact contract — scaffold, measured conventions, a validator, and the path to a pull request. |

`play-forge` ships three reference files that are useful on their own:

| File | What it is |
|---|---|
| [`play-forge/references/play-template.md`](play-forge/references/play-template.md) | The scaffold. Correct frontmatter key order, correct body markers. |
| [`play-forge/references/play-anatomy.md`](play-forge/references/play-anatomy.md) | Every field rule and body convention, with how many of the 70 plays use each. |
| [`play-forge/scripts/check_play.py`](play-forge/scripts/check_play.py) | `python3 check_play.py DRAFT.md --corpus .` — validates a draft. No dependencies. Passes all 70 existing plays. |

## Shared

| File | What it is |
|---|---|
| [`_shared/workspace.md`](_shared/workspace.md) | The contract every founder skill obeys: where things are written, how claims are aged, why `[not asked]` is not `[absent]`, and what never leaves the machine. |
| [`_shared/company-context.template.md`](_shared/company-context.template.md) | The context file's schema. |

## Where to start

**`playbook-triage`.** It works before you have set anything up — five questions
asked out loud and a provisional answer. Do the interview second, once you have
decided this is worth fifteen minutes.

If you would rather start from something concrete than from questions about your
company, run `artifact-review` on whatever spreadsheet you argue about most. It
is usually the fastest way to see whether this corpus has anything to tell you.

## Using them

**In Claude Code**, copy the folders into `.claude/skills/` in your project, or
into `~/.claude/skills/` for every project:

```bash
git clone https://github.com/golden-section-tx/playbook.git
mkdir -p ~/.claude/skills
cp -r playbook/skills/*/ ~/.claude/skills/
```

Then ask by name — "run playbook-triage", "review this cash model" — or just
describe the work; each skill's `description` is what makes it trigger.

**Anywhere else**, paste the `SKILL.md` in as instructions, or zip a folder as a
`.skill` file if your client installs those.

**Without an assistant at all**, read them. The six-test bar in `play-hunt` and
the grading scale in `artifact-review` both work fine in a notebook.

## Your company's data

Everything the founder skills learn is written to
[`workspace/`](../workspace/README.md) at the root of your fork, which is
gitignored and never contributed back. Before you push anything, run:

```bash
python3 scripts/check_private.py
```

It reports exactly what would leave your machine and fails if anything private
is tracked, staged, in your history, or riding on a contribution branch. The
full reasoning is in [`_shared/workspace.md`](_shared/workspace.md) and in the
[workspace README](../workspace/README.md).

## Contributing to the skills

Same terms as the rest of the repository — see
[CONTRIBUTING.md](../CONTRIBUTING.md). Improvements are the easiest contributions
to merge, and these have been used against a real portfolio but not against
yours. If a step is wrong for how your company works, that is worth an issue.

Content is [CC BY-SA 4.0](../LICENSE); the scripts are [MIT](../LICENSE-CODE).
The Golden Section name and marks are not licensed; see [NOTICE](../NOTICE).
