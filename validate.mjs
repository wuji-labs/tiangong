#!/usr/bin/env node
/**
 * Skill repository validator — zero dependencies, runs in CI on every push/PR.
 *
 * Catches the exact class of bug an external NLPM audit (and our own version
 * check) found by hand: manifest drift, version mismatch, missing files,
 * committed node_modules, unparseable JSON. Run from the repo root: `node validate.mjs`.
 * Exits non-zero on any failure so CI goes red.
 */
import { readFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';
import { execSync } from 'node:child_process';

const ROOT = process.cwd();
const fail = [];
const warn = [];
const ok = [];

const read = (p) => readFileSync(resolve(ROOT, p), 'utf8');
const has = (p) => existsSync(resolve(ROOT, p));

function frontmatter(p) {
  const m = read(p).match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!m) return null;
  const fm = {};
  for (const line of m[1].split(/\r?\n/)) {
    const kv = line.match(/^([a-zA-Z_]+):\s*(.*)$/);
    if (kv) fm[kv[1]] = kv[2].replace(/^["']|["']$/g, '').trim();
  }
  return fm;
}
function parseJson(p) {
  try { return JSON.parse(read(p)); } catch (e) { fail.push(`${p}: invalid JSON — ${e.message}`); return null; }
}

// 1. plugin.json
let plugin = null;
if (!has('.claude-plugin/plugin.json')) {
  fail.push('.claude-plugin/plugin.json is missing');
} else {
  plugin = parseJson('.claude-plugin/plugin.json');
  if (plugin) {
    if (!plugin.name) fail.push('plugin.json: missing "name"');
    if (!plugin.version) fail.push('plugin.json: missing "version"');
    else ok.push(`plugin.json version ${plugin.version}`);
  }
}

// 2. main skill file (plugin.skills[0].path or SKILL.md) frontmatter + version sync
const mainSkillPath = (plugin?.skills?.[0]?.path) || 'SKILL.md';
if (!has(mainSkillPath)) {
  fail.push(`main skill file ${mainSkillPath} is missing`);
} else {
  const fm = frontmatter(mainSkillPath);
  if (!fm) fail.push(`${mainSkillPath}: no YAML frontmatter`);
  else {
    if (!fm.name) fail.push(`${mainSkillPath}: frontmatter missing "name"`);
    if (!fm.description) fail.push(`${mainSkillPath}: frontmatter missing "description"`);
    if (fm.description && fm.description.length > 1024)
      warn.push(`${mainSkillPath}: description > 1024 chars (${fm.description.length})`);
    if (fm.version && plugin?.version && fm.version !== plugin.version)
      fail.push(`version drift: ${mainSkillPath}=${fm.version} but plugin.json=${plugin.version}`);
    else if (fm.version) ok.push(`skill version ${fm.version} matches plugin`);
  }
}

// 3. package.json version sync (if present)
if (has('package.json')) {
  const pkg = parseJson('package.json');
  if (pkg && pkg.version && plugin?.version && pkg.version !== plugin.version)
    fail.push(`version drift: package.json=${pkg.version} but plugin.json=${plugin.version}`);
  else if (pkg?.version) ok.push(`package.json version ${pkg.version} matches plugin`);
}

// 4. required files
for (const f of ['README.md', 'LICENSE']) {
  if (!has(f)) fail.push(`${f} is missing`);
  else ok.push(`${f} present`);
}

// 5. no GIT-TRACKED node_modules (a local gitignored symlink is fine; a committed one is not)
try {
  const tracked = execSync('git ls-files node_modules', { cwd: ROOT, encoding: 'utf8' }).trim();
  if (tracked) fail.push('node_modules is git-tracked — must be gitignored, never committed');
  else ok.push('node_modules not git-tracked');
} catch {
  // no git (e.g. tarball) — fall back to: present-and-not-ignored is a problem
  if (has('node_modules') && has('.gitignore') && /(^|\n)\s*node_modules\/?/.test(read('.gitignore')))
    ok.push('node_modules present but gitignored');
  else if (has('node_modules')) warn.push('node_modules present and git unavailable to confirm it is ignored');
  else ok.push('no node_modules');
}

// 6. .gitignore excludes node_modules
if (!has('.gitignore')) warn.push('.gitignore is missing');
else if (!/(^|\n)\s*node_modules\/?/.test(read('.gitignore')))
  warn.push('.gitignore does not list node_modules');
else ok.push('.gitignore excludes node_modules');

// report
for (const o of ok) console.log(`  ok   ${o}`);
for (const w of warn) console.log(`  warn ${w}`);
for (const f of fail) console.error(`  FAIL ${f}`);
if (fail.length) {
  console.error(`\n✗ ${fail.length} validation failure(s).`);
  process.exit(1);
}
console.log(`\n✓ skill repository valid (${ok.length} checks passed${warn.length ? `, ${warn.length} warning(s)` : ''}).`);
