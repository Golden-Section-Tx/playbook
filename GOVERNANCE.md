# Governance

This repository is public to read, fork, and propose to. Only Golden Section
changes what is in it.

## Who can merge

Merge authority sits with the **`@golden-section-tx/playbook-maintainers`** team
— Golden Section's general partners and their delegates. This is enforced
mechanically, not by convention:

- **Write access is limited to the `playbook-maintainers` team.** Nobody else
  can push to this repository at all. Anyone may fork it and open a pull
  request; only a maintainer can merge one. This is the control that matters,
  and it holds regardless of every other rule here.
- `main` cannot be deleted and cannot be force-pushed — by anyone, maintainers
  and organisation administrators included. That rule exists to make an
  accident unrecoverable-proof, not to restrain anyone.
- **Outside contributions arrive as a pull request** and cannot merge until
  continuous integration passes.

**Where this is currently weaker than it will be.** Stated plainly, so nobody
reads more into it than is there.

Golden Section maintainers can push directly to `main` today. With a
single-member team that is a deliberate trade: GitHub does not let anyone
approve their own pull request, so a mandatory-review rule would make the
repository unmergeable by the only person able to merge it, and routing every
one-line correction through a self-approved pull request would be ceremony
rather than review. The audit trail is the commit history, which is public and
permanent.

When a second maintainer joins, both halves change together: the direct-push
bypass comes off, and pull requests begin requiring one approving review from a
code owner — see [CODEOWNERS](CODEOWNERS), which is already written and
validating cleanly for exactly that moment. That is when "GP approval" becomes
a mechanism rather than a practice.

## The two internal contributors

Two Golden Section systems propose changes to this repository. Neither can merge.

**Dougal's knowledge vault.** Golden Section's internal knowledge base pushes a
branch and opens a pull request when a play is revised or a new mistake
graduates from observation into the list. Reviewed like any other pull request.

**LookingGlass.** Golden Section's operating-partner platform surfaces
generalisable insight from partner conversations. That insight passes through
LookingGlass's own subject-matter-expert review and general-partner approval
*before* it becomes a pull request here. The LookingGlass team is responsible
for anonymisation and confidentiality on their side of that boundary: no
company names, no attributable detail, no verbatim quotes from any
conversation, ever. A pull request that carries identifying detail is a
confidentiality failure, not a formatting problem — close it, do not fix it in
place, because a public pull request cannot be unpublished.

## What crosses into this repository, and what does not

Generalised plays, mistakes, and templates cross. Company-specific material
does not — not financials, not benchmark data derived from identifiable
companies, not anything traceable to a particular founder or conversation.

The line is deliberate. The knowledge is open. The tooling that applies it to a
specific company's numbers is not.

## Downstream consumers

Publication flows one way, out of this repository:

- **[goldensection.com](https://goldensection.com)** — reconciled against this
  repository manually, on Golden Section's own schedule. The website is
  downstream and never writes back.
- **LookingGlass** ingests this repository at a tagged commit, so any guidance
  it gives a founder can be traced to a public, verifiable source. It ingests
  the upstream repository only, never a fork.
- **Forks** pull. They cannot push.

## Releases

Substantive changes are tagged. Each release regenerates
[`dist/playbook-full.md`](dist/playbook-full.md), the single-file corpus, and
attaches it as a release asset. Downstream consumers pin to a tag rather than
tracking `main`, so a merge never changes anything live without a deliberate
step.

## Changing this document

Like everything else here: a pull request, approved by a code owner.
