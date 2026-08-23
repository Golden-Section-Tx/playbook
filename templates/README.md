# Templates

59 working Excel models, one or more attached to a play. These are the actual
spreadsheets — formulas, structure, worked examples — not screenshots or
outlines of spreadsheets.

Each play's page links its own templates. The full mapping lives in the
`templates:` list in each play's frontmatter, which is the single source of
truth; `scripts/build.mjs` fails the build if a play references a file that is
not here, and warns about any file here that no play references.

## The binder numbers

The `1.10`, `2.40`, `5.63` prefixes come from Golden Section's original
playbook binder, and they map to the six categories:

| Prefix | Category |
|---|---|
| `1.x` | Executive |
| `2.x` | Sales & Marketing |
| `3.x` | Customer |
| `4.x` | Operations |
| `5.x` | Development |
| `6.x` | Vendor |

The numbers are kept because founders who worked from the binder still refer to
plays by them, and because they sort correctly.

## Using them

Download, open, replace the example figures with your own. They are built to be
edited, not admired.

Two things worth saying plainly:

**Check the formulas before you rely on one.** These are working models that
have been used with real companies, not audited financial instruments. A model
that is right for one company's unit economics can be quietly wrong for
another's. Read what each formula does before it drives a decision.

**A template is not the play.** The spreadsheet is the artefact; the play is the
process that produces something true to put in it. Filling in a cash flow
forecast template without doing the unit-economics work behind it produces a
confident-looking file and no better decisions.

## License

Same as the rest of the content: [CC BY-SA 4.0](../LICENSE). Use them, adapt
them, build commercial work with them — credit Golden Section, and license your
adaptations under the same terms. The Golden Section name and marks are not
licensed; see [NOTICE](../NOTICE).

## Contributing a template

Drop the `.xlsx` in this folder, keeping the binder number and using a
lowercase hyphenated name, then add it to the owning play's `templates:` list
and run `npm run build`. Details in
[CONTRIBUTING.md](../CONTRIBUTING.md).

Corrections to existing templates — a broken formula, a wrong reference, an
assumption that no longer holds — are the most useful contribution anyone can
make here.
