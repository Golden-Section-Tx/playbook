#!/usr/bin/env node
/**
 * GOLDEN SECTION PLAYBOOK — build and validate
 * ---------------------------------------------------------------------------
 * The play files are the single source of truth for the play↔mistake graph.
 * Each play declares `preventsMistakes:` in its frontmatter; this script
 * derives every link in the other direction, so no relationship is ever
 * maintained in two places.
 *
 * It regenerates, in place:
 *   - the `**Prevented by**` line under each entry in MISTAKES.md
 *   - the counts block at the top of MISTAKES.md
 *   - the generated footer in every play (its mistakes + its templates)
 *   - plays/README.md — the index
 *   - dist/playbook-full.md — the whole corpus as one file
 *
 * And validates:
 *   - required frontmatter on every play; unique slug / anchor / order
 *   - every `preventsMistakes` number exists in MISTAKES.md
 *   - every referenced template file exists; no template goes unreferenced
 *   - every generated relative link resolves on disk
 *
 * Usage:  node scripts/build.mjs          write changes
 *         node scripts/build.mjs --check  fail if anything is out of date (CI)
 *
 * No dependencies. Node 18+.
 */

import { readFileSync, writeFileSync, readdirSync, existsSync, mkdirSync } from 'node:fs';
import { join, dirname, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const CHECK = process.argv.includes('--check');

const CATEGORIES = ['executive', 'sales-marketing', 'customer', 'operations', 'development', 'vendor'];
const CATEGORY_LABEL = {
  'executive': 'Executive',
  'sales-marketing': 'Sales & Marketing',
  'customer': 'Customer',
  'operations': 'Operations',
  'development': 'Development',
  'vendor': 'Vendor',
};
const REQUIRED_FM = ['order', 'slug', 'anchor', 'title', 'h1', 'category',
                     'players', 'initialEffort', 'ongoingEffort', 'frequency',
                     'stage', 'summary'];

const errors = [];
const warnings = [];
const stale = [];
const err = (m) => errors.push(m);
const warn = (m) => warnings.push(m);

/* ------------------------------------------------------------ frontmatter --- */

/** Minimal parser for the frontmatter dialect this repo uses: scalars,
 *  `- item` lists, and `- key: value` object lists. Not general YAML. */
function parseFrontmatter(raw, where) {
  const out = {};
  const lines = raw.split('\n');
  let key = null;

  for (const line of lines) {
    if (!line.trim() || line.trim().startsWith('#')) continue;

    const scalar = line.match(/^([A-Za-z][\w-]*):\s*(.*)$/);
    if (scalar) {
      key = scalar[1];
      const val = scalar[2].trim();
      out[key] = val === '' ? [] : stripQuotes(val);
      continue;
    }

    const objItem = line.match(/^\s+-\s+([A-Za-z][\w-]*):\s*(.*)$/);
    if (objItem && key) {
      if (!Array.isArray(out[key])) out[key] = [];
      out[key].push({ [objItem[1]]: stripQuotes(objItem[2].trim()) });
      continue;
    }

    const objCont = line.match(/^\s+([A-Za-z][\w-]*):\s*(.*)$/);
    if (objCont && key && Array.isArray(out[key]) && out[key].length &&
        typeof out[key][out[key].length - 1] === 'object') {
      out[key][out[key].length - 1][objCont[1]] = stripQuotes(objCont[2].trim());
      continue;
    }

    const item = line.match(/^\s+-\s+(.*)$/);
    if (item && key) {
      if (!Array.isArray(out[key])) out[key] = [];
      out[key].push(stripQuotes(item[1].trim()));
      continue;
    }

    warn(`${where}: could not parse frontmatter line: ${line.trim().slice(0, 60)}`);
  }
  return out;
}

const stripQuotes = (s) =>
  (s.startsWith('"') && s.endsWith('"')) || (s.startsWith("'") && s.endsWith("'"))
    ? s.slice(1, -1) : s;

function splitDoc(text, where) {
  const m = text.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!m) { err(`${where}: missing frontmatter`); return null; }
  return { fmRaw: m[1], body: m[2] };
}

/* ------------------------------------------------------------------ load --- */

const plays = [];
for (const cat of CATEGORIES) {
  const dir = join(ROOT, 'plays', cat);
  if (!existsSync(dir)) { err(`missing category directory plays/${cat}`); continue; }
  for (const file of readdirSync(dir).filter((f) => f.endsWith('.md') && f !== 'README.md').sort()) {
    const rel = `plays/${cat}/${file}`;
    const text = readFileSync(join(dir, file), 'utf8');
    const doc = splitDoc(text, rel);
    if (!doc) continue;
    const fm = parseFrontmatter(doc.fmRaw, rel);

    for (const k of REQUIRED_FM) {
      if (fm[k] === undefined || fm[k] === '') err(`${rel}: missing frontmatter '${k}'`);
    }
    if (fm.category !== cat) err(`${rel}: category '${fm.category}' does not match its folder`);
    if (fm.slug && `${fm.slug}.md` !== file) err(`${rel}: slug '${fm.slug}' does not match filename`);

    plays.push({ rel, path: join(dir, file), fm, body: doc.body, fmRaw: doc.fmRaw });
  }
}

for (const field of ['slug', 'anchor', 'order']) {
  const seen = new Map();
  for (const p of plays) {
    const v = String(p.fm[field]);
    if (seen.has(v)) err(`duplicate ${field} '${v}': ${seen.get(v)} and ${p.rel}`);
    else seen.set(v, p.rel);
  }
}

/* --------------------------------------------------------- MISTAKES.md ----- */

const mistakesPath = join(ROOT, 'MISTAKES.md');
const mistakesRaw = readFileSync(mistakesPath, 'utf8');

const ENTRY_RE = /^### <a id="m(\d{3})"><\/a>(\d+) · (.+)$/;
const mLines = mistakesRaw.split('\n');
const entryStarts = [];
mLines.forEach((line, i) => { if (ENTRY_RE.test(line)) entryStarts.push(i); });
if (!entryStarts.length) err('MISTAKES.md: no entries matched the expected heading format');

const headerLines = mLines.slice(0, entryStarts[0]);
const mistakes = entryStarts.map((start, idx) => {
  const end = idx + 1 < entryStarts.length ? entryStarts[idx + 1] : mLines.length;
  const [, anchorNum, num, title] = mLines[start].match(ENTRY_RE);
  if (Number(anchorNum) !== Number(num)) {
    err(`MISTAKES.md #${num}: anchor m${anchorNum} does not match the number`);
  }
  return { number: Number(num), title, anchor: `m${anchorNum}`,
           lines: mLines.slice(start, end) };
});

{
  const nums = mistakes.map((m) => m.number);
  const dupes = nums.filter((n, i) => nums.indexOf(n) !== i);
  if (dupes.length) err(`MISTAKES.md: duplicate numbers ${[...new Set(dupes)].join(', ')}`);
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] <= nums[i - 1]) err(`MISTAKES.md: #${nums[i]} is out of ascending order`);
  }
}
const mistakeByNumber = new Map(mistakes.map((m) => [m.number, m]));

/* ------------------------------------------------- the graph, one way in --- */

const reverse = new Map();            // mistake number -> [play, …]
for (const p of plays) {
  const declared = Array.isArray(p.fm.preventsMistakes) ? p.fm.preventsMistakes : [];
  const clean = [];
  for (const rawN of declared) {
    const n = Number(rawN);
    if (!Number.isInteger(n)) { err(`${p.rel}: preventsMistakes entry '${rawN}' is not a number`); continue; }
    if (!mistakeByNumber.has(n)) { err(`${p.rel}: preventsMistakes #${n} does not exist in MISTAKES.md`); continue; }
    if (clean.includes(n)) { warn(`${p.rel}: preventsMistakes lists #${n} twice`); continue; }
    clean.push(n);
    if (!reverse.has(n)) reverse.set(n, []);
    reverse.get(n).push(p);
  }
  p.prevents = clean.sort((a, b) => a - b);
}

for (const [, list] of reverse) {
  list.sort((a, b) => Number(a.fm.order) - Number(b.fm.order));
}

const unmapped = mistakes.filter((m) => !reverse.has(m.number));

/* ------------------------------------------------------------ templates --- */

const templatesDir = join(ROOT, 'templates');
const onDisk = existsSync(templatesDir)
  ? new Set(readdirSync(templatesDir).filter((f) => !f.startsWith('.') && f !== 'README.md'))
  : new Set();
const referenced = new Set();

for (const p of plays) {
  const list = Array.isArray(p.fm.templates) ? p.fm.templates : [];
  p.templates = [];
  for (const t of list) {
    if (typeof t !== 'object' || !t.file) { err(`${p.rel}: malformed templates entry`); continue; }
    if (!onDisk.has(t.file)) err(`${p.rel}: template '${t.file}' is not in templates/`);
    referenced.add(t.file);
    p.templates.push({ file: t.file, name: t.name || t.file });
  }
}
for (const f of onDisk) {
  if (!referenced.has(f)) warn(`templates/${f} is not referenced by any play`);
}

/* -------------------------------------------------------------- writing --- */

const pending = [];
function emit(absPath, next) {
  const rel = relative(ROOT, absPath);
  const prev = existsSync(absPath) ? readFileSync(absPath, 'utf8') : null;
  if (prev === next) return;
  if (CHECK) { stale.push(rel); return; }
  mkdirSync(dirname(absPath), { recursive: true });
  writeFileSync(absPath, next, 'utf8');
  pending.push(rel);
}

const mistakeLink = (n, from) => {
  const m = mistakeByNumber.get(n);
  return `[#${n} ${m.title}](${from}MISTAKES.md#${m.anchor})`;
};

/* --- the shared counts block, kept identical in MISTAKES.md and README.md - */
const countBlock = (() => {
  const counts = CATEGORIES.map((c) => {
    const n = plays.filter((p) => p.fm.category === c).length;
    return `${CATEGORY_LABEL[c]} ${n}`;
  }).join(' · ');
  return [
    '<!-- GS:COUNTS start -->',
    `**${mistakes.length} mistakes · ${plays.length} plays · ${onDisk.size} templates.**  `,
    `Plays by category: ${counts}.  `,
    `${mistakes.length - unmapped.length} of ${mistakes.length} mistakes have at least one play mapped.`,
    '<!-- GS:COUNTS end -->',
  ].join('\n');
})();

const COUNTS_RE = /<!-- GS:COUNTS start -->[\s\S]*?<!-- GS:COUNTS end -->/;

/* --- README.md: refresh its counts block ------------------------------- */
{
  const readmePath = join(ROOT, 'README.md');
  if (existsSync(readmePath)) {
    const prev = readFileSync(readmePath, 'utf8');
    if (!COUNTS_RE.test(prev)) warn('README.md: no GS:COUNTS block to refresh');
    else emit(readmePath, prev.replace(COUNTS_RE, countBlock));
  } else {
    err('README.md is missing');
  }
}

/* --- MISTAKES.md: refresh the counts block and every Prevented by line --- */
{
  let header = headerLines.join('\n').replace(COUNTS_RE, countBlock);

  const rebuilt = mistakes.map((m) => {
    // drop any previously generated line, then re-append a fresh one
    const kept = m.lines.filter(
      (l) => !l.startsWith('**Prevented by**') && !l.startsWith('_No play is mapped'),
    );
    while (kept.length && kept[kept.length - 1].trim() === '') kept.pop();

    const list = reverse.get(m.number);
    const line = list
      ? `**Prevented by** · ${list.map((p) => `[${p.fm.title}](${p.rel})`).join(' · ')}`
      : '_No play is mapped to this mistake yet._';

    return [...kept, '', line, ''].join('\n');
  }).join('\n');

  emit(mistakesPath, `${header}\n${rebuilt}`.replace(/\n{3,}/g, '\n\n').trimEnd() + '\n');
}

/* --- each play: regenerate its generated footer ------------------------- */
const LINKS_START = '<!-- GS:LINKS start — generated by scripts/build.mjs, do not edit by hand -->';
const LINKS_END = '<!-- GS:LINKS end -->';

for (const p of plays) {
  const bits = [];
  if (p.prevents.length) {
    bits.push(`**Prevents** · ${p.prevents.map((n) => mistakeLink(n, '../../')).join(' · ')}`);
  }
  if (p.templates.length) {
    bits.push(`**Templates** · ${p.templates
      .map((t) => `[${t.name}](../../templates/${encodeURI(t.file)})`).join(' · ')}`);
  }
  bits.push(`**Category** · [${CATEGORY_LABEL[p.fm.category]}](../README.md) · ` +
            `**Effort** · ${p.fm.initialEffort} initial, ${p.fm.ongoingEffort} ongoing · ` +
            `**Cadence** · ${p.fm.frequency}`);

  const footer = [LINKS_START, '', '---', '', bits.join('\n\n'), '', LINKS_END].join('\n');

  let body = p.body;
  const existing = body.indexOf(LINKS_START);
  if (existing !== -1) body = body.slice(0, existing);
  body = body.replace(/\s+$/, '');

  emit(p.path, `---\n${p.fmRaw}\n---\n${body}\n\n${footer}\n`);
}

/* --- plays/README.md ---------------------------------------------------- */
{
  const out = [
    '# Vertical SaaS Plays',
    '',
    `${plays.length} plays across six categories. Each play is one Markdown file:`,
    'what to do, who does it, how long it takes, and which mistakes it prevents.',
    '',
    'Generated by `scripts/build.mjs` — do not edit by hand.',
    '',
    `See also: [the mistakes list](../MISTAKES.md) · [templates](../templates/)`,
    '',
  ];

  for (const cat of CATEGORIES) {
    const inCat = plays.filter((p) => p.fm.category === cat)
      .sort((a, b) => Number(a.fm.order) - Number(b.fm.order));
    if (!inCat.length) continue;
    out.push(`## ${CATEGORY_LABEL[cat]}`, '');
    out.push('| Play | Owners | Cadence | Initial | Ongoing | Prevents |');
    out.push('|---|---|---|---|---|---|');
    for (const p of inCat) {
      const prevents = p.prevents.length
        ? p.prevents.map((n) => `[${n}](../MISTAKES.md#${mistakeByNumber.get(n).anchor})`).join(' ')
        : '—';
      out.push(`| [${p.fm.title}](${cat}/${p.fm.slug}.md) | ${p.fm.players} | ` +
               `${p.fm.frequency} | ${p.fm.initialEffort} | ${p.fm.ongoingEffort} | ${prevents} |`);
    }
    out.push('');
  }
  emit(join(ROOT, 'plays', 'README.md'), out.join('\n'));
}

/* --- dist/playbook-full.md --------------------------------------------- */
{
  const out = [
    '# The Golden Section Playbook — complete corpus',
    '',
    `${plays.length} plays and ${mistakes.length} mistakes for building a B2B vertical SaaS company,`,
    'in one file.',
    '',
    '**Source:** https://github.com/golden-section-tx/playbook',
    '**Attribution:** Golden Section — https://goldensection.com',
    '**License:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).',
    'You may share and adapt this material, including commercially, provided you give',
    'credit to Golden Section and license your adaptations under the same terms.',
    'The Golden Section name, logo and marks are not licensed. For alternative terms,',
    'ask: https://github.com/golden-section-tx/playbook/issues',
    '',
    'Generated by `scripts/build.mjs` — do not edit.',
    '',
    '---',
    '',
    '# Part I — The mistakes',
    '',
  ];

  for (const m of mistakes) {
    const list = reverse.get(m.number);
    out.push(`## Mistake ${m.number} · ${m.title}`, '');
    const detail = m.lines.slice(1)
      .filter((l) => !l.startsWith('**Prevented by**') && !l.startsWith('_No play is mapped'))
      .join('\n').trim();
    if (detail) out.push(detail, '');
    if (list) out.push(`Prevented by: ${list.map((p) => p.fm.title).join(', ')}.`, '');
  }

  out.push('---', '', '# Part II — The plays', '');
  for (const cat of CATEGORIES) {
    const inCat = plays.filter((p) => p.fm.category === cat)
      .sort((a, b) => Number(a.fm.order) - Number(b.fm.order));
    if (!inCat.length) continue;
    out.push(`## ${CATEGORY_LABEL[cat]}`, '');
    for (const p of inCat) {
      out.push(`### ${p.fm.h1}`, '');
      out.push(`**Play:** ${p.fm.title} · **Owners:** ${p.fm.players} · ` +
               `**Cadence:** ${p.fm.frequency} · **Stage:** ${p.fm.stage} · ` +
               `**Effort:** ${p.fm.initialEffort} initial, ${p.fm.ongoingEffort} ongoing`, '');
      out.push(`**Summary:** ${p.fm.summary}`, '');
      if (p.prevents.length) {
        out.push(`**Prevents mistakes:** ${p.prevents.map((n) =>
          `#${n} ${mistakeByNumber.get(n).title}`).join('; ')}`, '');
      }
      if (p.templates.length) {
        out.push(`**Templates:** ${p.templates.map((t) => t.name).join(', ')}`, '');
      }
      const body = p.body.split(LINKS_START)[0].trim();
      out.push(body, '');
    }
  }
  emit(join(ROOT, 'dist', 'playbook-full.md'), out.join('\n').replace(/\n{4,}/g, '\n\n\n') + '\n');
}

/* --- llms.txt ----------------------------------------------------------- */
{
  const out = [
    '# The Golden Section Playbook',
    '',
    `> ${plays.length} plays and ${mistakes.length} mistakes for building a B2B vertical SaaS`,
    '> company, from a firm that has watched over 400 of them. Every mistake is',
    '> paired with the play that prevents it.',
    '',
    'Licensed CC BY-SA 4.0. Attribute to Golden Section (https://goldensection.com).',
    'Adaptations must carry the same license. Golden Section names and marks are not',
    'licensed. Alternative terms on request: open an issue.',
    '',
    '## Whole corpus in one file',
    '',
    `- [dist/playbook-full.md](dist/playbook-full.md): everything below, single file, with attribution and license in its header. Prefer this for ingestion.`,
    '',
    '## Primary documents',
    '',
    `- [MISTAKES.md](MISTAKES.md): all ${mistakes.length} mistakes, numbered, with permanent #mNNN anchors and the plays that prevent each.`,
    `- [plays/README.md](plays/README.md): index of all ${plays.length} plays with owners, cadence, and effort.`,
    '- [templates/](templates/): 59 working Excel models, mapped to plays.',
    '- [CONTRIBUTING.md](CONTRIBUTING.md): how to propose a change.',
    '- [GOVERNANCE.md](GOVERNANCE.md): who can change this and how.',
    '',
    '## Plays by category',
    '',
  ];
  for (const cat of CATEGORIES) {
    const inCat = plays.filter((p) => p.fm.category === cat)
      .sort((a, b) => Number(a.fm.order) - Number(b.fm.order));
    if (!inCat.length) continue;
    out.push(`### ${CATEGORY_LABEL[cat]}`, '');
    for (const p of inCat) {
      out.push(`- [${p.fm.title}](plays/${cat}/${p.fm.slug}.md): ${p.fm.summary}`);
    }
    out.push('');
  }
  emit(join(ROOT, 'llms.txt'), out.join('\n'));
}

/* --------------------------------------------------------------- report --- */

const orphans = plays.filter((p) => !p.prevents.length).map((p) => p.fm.slug);

console.log(`plays            ${plays.length}`);
console.log(`mistakes         ${mistakes.length}`);
console.log(`templates        ${onDisk.size} on disk, ${referenced.size} referenced`);
console.log(`graph edges      ${plays.reduce((n, p) => n + p.prevents.length, 0)}`);
console.log(`unmapped mistakes ${unmapped.length}${unmapped.length ? ' → ' + unmapped.map((m) => m.number).join(', ') : ''}`);
console.log(`plays w/o mistakes ${orphans.length}${orphans.length ? ' → ' + orphans.join(', ') : ''}`);

if (warnings.length) {
  console.log(`\n${warnings.length} warning(s):`);
  for (const w of warnings) console.log(`  ! ${w}`);
}

if (errors.length) {
  console.error(`\n${errors.length} error(s):`);
  for (const e of errors) console.error(`  ✗ ${e}`);
  process.exit(1);
}

if (CHECK) {
  if (stale.length) {
    console.error(`\n${stale.length} file(s) are out of date — run \`npm run build\` and commit:`);
    for (const s of stale) console.error(`  ✗ ${s}`);
    process.exit(1);
  }
  console.log('\nup to date');
} else {
  console.log(`\n${pending.length} file(s) written`);
}
