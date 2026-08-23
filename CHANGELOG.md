# Changelog

Substantive changes to the plays and the mistakes list. Generated-file churn is
not recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Mistake numbers are permanent and are never reused, so a removed mistake is
recorded as removed rather than renumbered.

## [Unreleased]

## [1.0.0] — 2026-08-23

First public release.

### Added

- **`MISTAKES.md`** — all 161 mistakes, each with a permanent `#mNNN` anchor,
  its category, and the plays that prevent it. Lifted out of the hand-authored
  HTML on goldensection.com, which had been the only home for them.
- **`plays/`** — 63 plays across six categories: Executive 11,
  Sales & Marketing 21, Customer 8, Operations 8, Development 13, Vendor 2. One
  Markdown file each, with structured frontmatter carrying owners, effort in
  story points, cadence, stage, and the mistakes the play prevents.
- **`templates/`** — 59 Excel templates, binder-numbered, mapped to plays by
  slug.
- **`scripts/build.mjs`** — generates every cross-reference from the plays'
  `preventsMistakes` frontmatter, so the play↔mistake graph has exactly one
  source of truth and cannot drift. Also validates frontmatter, anchors,
  numbering, and template references, and fails CI when committed generated
  output is stale.
- **`dist/playbook-full.md`** — the whole corpus as one file, with attribution
  and licence in its header so both travel with the text.
- Governance and licensing: [CC BY-SA 4.0](LICENSE) for content,
  [MIT](LICENSE-CODE) for tooling, marks reserved in [NOTICE](NOTICE),
  [CLA](CLA.md) for inbound contributions, [GOVERNANCE.md](GOVERNANCE.md) for
  merge authority.

### Notes

- 227 play↔mistake edges, matching the website's own count exactly — the
  extraction lost nothing.
- 14 mistakes have no play mapped yet: 3, 18, 40, 41, 62, 70, 81, 82, 98, 99,
  105, 110, 140, 146. They are marked in place. Pairing them is open work.
- 7 plays are not mapped to any mistake: company insurance, customer
  onboarding, support metrics, licence register, open-source register, security
  documentation, security process. Also open work — several of these plainly
  prevent mistakes that exist in the list.
- `stories/` is empty by design; it fills as stories can be told with the
  identifying detail properly removed.
