<!--
  This pull request is PUBLIC from the moment it opens, and it cannot be
  unpublished. Closing it does not remove it. Before you submit, check that
  nothing in the branch name, the commit messages, the diff, or the text below
  identifies a company, a founder, or an individual.
-->

## What this changes

<!-- One or two sentences. -->

## Type

- [ ] New mistake
- [ ] New play
- [ ] Edit to an existing mistake or play
- [ ] Template added or corrected
- [ ] Story added
- [ ] Governance, licensing, or tooling

## Provenance

<!--
  Required. Where the substance came from, stated at a level that identifies
  nobody. Good: "Generalised from four portfolio observations, 2026."
  Good: "Corrects an error in the CAC formula." Good: "My own company, and I'm
  happy to be named as the contributor."
  Not acceptable: any company name, any founder name, any figure specific
  enough to identify a company.
-->

Source:

## Checks

- [ ] `npm run build` exits clean, and I have committed everything it regenerated
- [ ] No generated content edited by hand (nothing between `GS:` markers, no
      `**Prevented by**` lines, nothing in `dist/` or `plays/README.md`)
- [ ] New mistakes use the next unused number; no existing number was changed
- [ ] Any new template file is in `templates/` and referenced from a play
- [ ] Nothing here identifies a company or a person, and nothing is quoted
      verbatim from a private conversation
- [ ] I have signed the [CLA](../CLA.md), or will when the bot asks

## For Golden Section reviewers

- [ ] Confidentiality: nothing identifying, in the diff **or** in this pull
      request's own text and metadata
- [ ] The mistake is a specific behaviour with a specific consequence, not a
      category of risk
- [ ] The play can be scheduled — steps, owners, honest effort estimate
- [ ] Voice matches the existing entries
