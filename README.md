# The Golden Section Playbook

**70 plays and 168 mistakes for building a B2B vertical SaaS company.**

Golden Section has spent more than a decade operating alongside vertical SaaS
founders, and has watched over 400 companies make the same mistakes in roughly
the same order. This repository is the working record of both halves of that:
every mistake we have seen, and the play that prevents each one.

It is the same material we use with our own portfolio. It is open because a
mistake nobody warned you about is a bad reason to lose a company.

Dougal Cameron's [letter to founders](LETTER-TO-FOUNDERS.md) covers why we
published it, and how to tell the advice that is worth taking from the advice
that is merely loud.

<!-- GS:COUNTS start -->
**168 mistakes · 70 plays · 59 templates.**  
Plays by category: Executive 12 · Sales & Marketing 23 · Customer 11 · Operations 8 · Development 13 · Vendor 3.  
156 of 168 mistakes have at least one play mapped.
<!-- GS:COUNTS end -->

## Start here

| | |
|---|---|
| **[MISTAKES.md](MISTAKES.md)** | All 168, numbered, with the plays that prevent each one. Start here if something already hurts. |
| **[plays/](plays/README.md)** | The 70 plays, one Markdown file each — what to do, who owns it, how long it takes. Start here if you are building rather than firefighting. |
| **[templates/](templates/)** | 59 working Excel templates, one or more per play. The actual models, not screenshots of them. |
| **[EFFORT.md](EFFORT.md)** | What the story points on every play mean, in person-days — and what they do not mean. Read before scheduling anything. |
| **[dist/playbook-full.md](dist/playbook-full.md)** | The entire corpus as one file. For feeding to an AI, or reading on a plane. |
| **[skills/](skills/README.md)** | Eight agent skills that work the corpus with you — interview, triage, review what you have, turn a play into assigned work, watch for mistakes, contribute back. Plain Markdown, no dependencies. |

Every mistake links to its plays and every play links back to its mistakes, so
you can enter from either side. Mistake anchors are stable — `MISTAKES.md#m016`
will always be *Running out of cash*, whatever the wording becomes.

## How to actually use it

**If you are a founder.** Read the mistakes list once, end to end. It takes
about twenty minutes and it is the highest-return twenty minutes in here —
not because you will remember all 168, but because you will recognize three of
them as things happening in your company right now. Then run those plays.

**If you are an operator or advisor.** The plays carry effort estimates in story
points and a cadence, so they can be scheduled rather than admired. A point is
one person's working time and `13 SP` is one person-week — [EFFORT.md](EFFORT.md)
has the scale, including what it will not tell you. Category hubs are in
[plays/README.md](plays/README.md).

**If you are an AI agent, or you are pointing one at this.** Use
[`dist/playbook-full.md`](dist/playbook-full.md) — the whole corpus in one file,
with attribution and license in its header so both travel with the text. There
is also [`llms.txt`](llms.txt) at the repository root.

**If you want your own copy.** Fork it. To stay current:

```bash
git remote add upstream https://github.com/golden-section-tx/playbook.git
git pull upstream main
```

Your fork is yours. If you improve something and want it back in here, open a
pull request — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Using this with an AI assistant

The corpus is text, so any assistant can read it — point one at
[`dist/playbook-full.md`](dist/playbook-full.md) and ask it questions today.

What that does not do is tell you *which* of the plays you should run, in
what order, given the company you actually have. The [`skills/`](skills/README.md)
folder is eight small instruction files that do. Copy them into your assistant,
and it can interview you, work out which of the mistakes on the list are live in your
business right now, prescribe two or three plays rather than all of them, check
the spreadsheets you already have against the plays that govern them, and turn a
play into dated tasks assigned to real people.

They are plain Markdown. No code, no keys, no service to sign up for, nothing
that stops working when we stop maintaining it.

### Your company's information stays on your machine

For any of that to be useful, the assistant has to know things about your
company: revenue, cash, churn, who works there, what is broken this quarter.
That has to live somewhere, so it lives in a folder called
[`workspace/`](workspace/README.md) inside your copy of this repository.

**Nothing in `workspace/` is ever sent back to us.** Concretely:

- `.gitignore` excludes everything in that folder, so it is not committed and not
  pushed. Only its README is tracked.
- The skills are instructed never to put anything from it into a commit, a
  branch name, an issue, or a pull request.
- When you contribute something back — a field report, a fix to a play — the
  skill builds it on a fresh branch taken from this repository, not from the
  branch you have been working in. That matters, because a pull request carries
  every commit on its branch, not just the file you meant to change.
- Nothing is ever submitted without showing you the exact text first and waiting
  for you to say yes.

Two honest caveats, because "it's gitignored" is a weaker promise than it sounds.
Ignoring a file has no effect once git is already tracking it — so a file that
gets committed once, by accident or by force, stays committed. And git history
keeps what you delete, so removing a file later does not remove it from the
history you would push.

So there is a check, not just a promise:

```bash
python3 scripts/check_private.py
```

Run it before you push. It tells you exactly what would leave your machine, and
if something private is tracked, staged, sitting in your history, or riding
along on a contribution branch, it says so and tells you how to fix it. It
changes nothing by itself. It needs only Python 3.

If you would rather keep your workspace in version control — it is a useful
record, and a cofounder may want it — make your fork **private** and delete the
`workspace` lines from `.gitignore`. That is a perfectly good setup. The risk
lies only in a public fork.

### What the skills are

| For founders | |
|---|---|
| `context-interview` | Fifteen minutes, once. Writes what your assistant knows about your company. |
| `playbook-triage` | Which mistakes are live, the two or three plays to run now, and what you are choosing to skip. |
| `artifact-review` | Your cash model, pricing matrix, or ARR schedule, held against the play that governs it. |
| `run-play` | One play into assigned, dated work — in your task manager, as a CSV, or as a PDF with a page per person. |
| `mistake-watch` | Your own meeting notes against the mistakes list, monthly, so you can see what has been live for a quarter. |
| `field-report` | What actually happened when you ran a play, sent back anonymized. This is how the corpus gets better. |

| For operators, advisors, and contributors | |
|---|---|
| `play-hunt` | Meetings across many companies against the corpus, hunting patterns that deserve to be plays. |
| `play-forge` | Write a play or a mistake to this repository's contract, and open the pull request. |

Start with `playbook-triage` — it works before you have done anything else, on
five questions asked out loud. The interview is what you do second, when you
have decided this is worth fifteen minutes.

## License, plainly

The content — plays, mistakes, templates — is licensed
**[CC BY-SA 4.0](LICENSE)**. You may use it, adapt it, and build commercial
things with it. Two conditions: credit Golden Section, and license your
adaptations under the same terms so they stay available to the founders who come
after you.

The scripts and schemas are [MIT](LICENSE-CODE). The Golden Section name, logo
and marks are **not** licensed — see [NOTICE](NOTICE).

**If ShareAlike is a genuine obstacle to getting this in front of founders, ask
us.** Open an issue. We grant alternative terms for founder-serving uses and the
answer is usually yes. We would rather this reach people than win an argument
about licensing.

One clarification, since it comes up: Golden Section retains full rights in its
own material and holds a broad license to all contributions (see
[CLA.md](CLA.md)). The CC BY-SA grant is what we offer the public; it does not
constrain Golden Section's own use of this material, including in our own
products. Nothing here is a promise that our tools are open source. The
knowledge is.

## Contributing and governance

Anyone may open a pull request. Merge authority sits with Golden Section's
general partners — see [GOVERNANCE.md](GOVERNANCE.md) for who and why, and
[CONTRIBUTING.md](CONTRIBUTING.md) for what a good contribution looks like.

Contributions require signing the [CLA](CLA.md), which the bot will prompt for on
your first pull request.

## Where this comes from, and where it goes

The plays and mistakes are also published at
[goldensection.com](https://goldensection.com) — this repository is upstream of
that, not a copy of it. Changes land here first.

Golden Section is a capital-efficient growth equity firm investing in B2B
vertical SaaS. If reading this list makes you want to talk to someone about your
company rather than fix it alone, that is what we do.

---

*Maintained by Golden Section · [goldensection.com](https://goldensection.com)*
