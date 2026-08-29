# Your workspace

**Everything in this folder is about your company, and none of it is ever sent
anywhere.** This README is the only file in here that git tracks. Everything
else you or the skills create stays on your machine.

If you are reading this in a fresh fork, the folder is empty apart from this
file. It fills up as you use the skills.

## What lands here

| | |
|---|---|
| `company-context.md` | What the skills know about your company — stage, numbers, who you have, which plays you already run. Written by `context-interview`, kept current by the others. |
| `commitments.md` | The plays you have committed to run, and where each one stands. |
| `plays/<play-name>/` | One folder per play in progress: the plan, notes on what actually happened, and whatever the play produces. |
| `reviews/` | `artifact-review` output — what you already have, held against the play that governs it. |
| `mistake-log.md` | `mistake-watch` history, so you can see what has been live for three months running. |

Think of it as a small operating record: what is true about the company, what
you decided to fix, and what happened. It is plain markdown, so it is yours to
read, edit, grep, or delete without any tool's permission.

## Why it never leaves

The repository's `.gitignore` excludes everything in this folder except this
file. So when you commit, push, or open a pull request to send an improvement
back to Golden Section, your ARR, your cash position, your churn, and your
people's names do not go with it.

**Two things that ignoring does not protect you from**, worth knowing once:

1. **If a file gets committed anyway** — you force-added it, or it was committed
   before the rule existed — then git tracks it from then on and the ignore rule
   stops applying to it.
2. **Git history keeps what you delete.** Removing a file in a later commit does
   not remove it from the history, and pushing a branch sends the whole history
   of that branch.

So there is a check rather than a promise:

```bash
python3 scripts/check_private.py
```

Run it before you push anything. It tells you exactly what would leave your
machine, and if something private is tracked, staged, or sitting in history, it
says so and tells you how to fix it. It changes nothing on its own.

## If you want this backed up or shared with a cofounder

Reasonable — it is a useful record. Do it deliberately, not by committing it
here:

- Put the folder in Dropbox, iCloud, Drive, or whatever you already use, and
  symlink it in; or
- Keep your fork **private** on GitHub and remove the `workspace` lines from
  `.gitignore`. A private fork is fine. The risk is only in a public one, and a
  fork's visibility can be changed by anyone with admin on it.

What you should not do is commit it to a public fork and rely on nobody looking.

## Contributing back without leaking

If you want to send Golden Section a field report or an improved play, the
skills build that contribution on a **clean branch taken from upstream**, not
from the branch you have been working in. That matters, because a pull request
carries every commit on its branch, not just the file you meant to change.

`field-report` and `play-forge` do this for you, show you the exact text before
anything is submitted, and anonymize as they write rather than cleaning up
afterward. Nothing is submitted without you saying yes to it.

There are two nets, and they catch different things. `check_private.py` runs on
your machine and catches your own company data before it leaves. A scan runs on
the pull request itself and checks the diff against a blocklist Golden Section
maintains. Neither replaces reading your own diff before you open it — a public
pull request cannot be unpublished.
