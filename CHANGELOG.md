# Changelog

Substantive changes to the plays and the mistakes list. Generated-file churn is
not recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Mistake numbers are permanent and are never reused, so a removed mistake is
recorded as removed rather than renumbered.

## [Unreleased]

### Added

- **Play 70, Board Meeting Preparation** (`plays/executive/saas-board-meeting-prep.md`)
  — Executive, quarterly, Founder/Board/CFO. Covers what goes in front of a board
  before the meeting and what the meeting itself is for: the plan of record, the
  packet, the recorded walkthrough sent a week ahead, and an agenda built backwards
  from one or two decisions the founder is genuinely unsure about.
- **Mistake 168, Building the board meeting to win approval instead of to get help.**

### Changed

- **Play 7, Board of Directors** — the "Create the content plan" step no longer
  carries its own packet contents list and 48-hour send window. Both now live in
  Board Meeting Preparation, and the step points there. The four items unique to
  the old list (operational statistics, gross margin and support hours by customer)
  were folded into the new play's contents so nothing was lost.
- Hand-authored counts in `README.md`, `CONTRIBUTING.md` and `package.json` brought
  up to 70 plays and 168 mistakes. They had been stale at 63 and 161 since the
  1.0.0 release.

### Notes

- Mistake 70, *Mistaking communication brevity for clarity*, now has a play mapped
  to it for the first time. Unmapped mistakes drop from 13 to 12: 3, 18, 40, 41,
  62, 82, 98, 99, 105, 110, 140, 146.
- 267 play-mistake edges, up from 257.

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
  and license in its header so both travel with the text.
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
  onboarding, support metrics, license register, open-source register, security
  documentation, security process. Also open work — several of these plainly
  prevent mistakes that exist in the list.
- `stories/` is empty by design; it fills as stories can be told with the
  identifying detail properly removed.
