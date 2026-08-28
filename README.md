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
| **[dist/playbook-full.md](dist/playbook-full.md)** | The entire corpus as one file. For feeding to an AI, or reading on a plane. |

Every mistake links to its plays and every play links back to its mistakes, so
you can enter from either side. Mistake anchors are stable — `MISTAKES.md#m016`
will always be *Running out of cash*, whatever the wording becomes.

## How to actually use it

**If you are a founder.** Read the mistakes list once, end to end. It takes
about twenty minutes and it is the highest-return twenty minutes in here —
not because you will remember all 168, but because you will recognize three of
them as things happening in your company right now. Then run those plays.

**If you are an operator or advisor.** The plays carry effort estimates in story
points and a cadence, so they can be scheduled rather than admired. Category
hubs are in [plays/README.md](plays/README.md).

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
