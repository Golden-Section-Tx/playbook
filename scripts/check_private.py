#!/usr/bin/env python3
"""Check that nothing about your company is about to leave your machine.

Run this before you push, and before you open a pull request:

    python3 scripts/check_private.py

It reports what a push would actually send, and fails if anything private is
tracked by git, staged, sitting in your commit history, or about to ride along
on a branch you are contributing from.

Being gitignored is not the same as being safe. `.gitignore` has no effect on a
file git is already tracking, and deleting a file does not remove it from
history. This script checks for both.

No third-party dependencies. Python 3.8+.

Exit status 0 = clean. 1 = something private would leave. 2 = could not check.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

PRIVATE_DIRS = ["workspace"]
PRIVATE_HINTS = [
    "company-context.md", "commitments.md", "mistake-log.md",
]
SECRET_PATTERNS = [
    (re.compile(r"(?i)\b(api[_-]?key|secret[_-]?key|access[_-]?token)\b"),
     "what looks like an API key or token"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "a private key"),
    (re.compile(r"(?i)\baws_secret_access_key\b"), "an AWS secret"),
]

GREEN, RED, YELLOW, DIM, OFF = "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[0m"
if not sys.stdout.isatty() or os.environ.get("NO_COLOR"):
    GREEN = RED = YELLOW = DIM = OFF = ""


def git(*args, cwd=None):
    """Run a git command; return (ok, stdout)."""
    try:
        out = subprocess.run(["git", *args], cwd=cwd, capture_output=True,
                             text=True, check=False)
    except FileNotFoundError:
        return False, "git is not installed"
    if out.returncode != 0:
        return False, (out.stderr or out.stdout).strip()
    return True, out.stdout


def is_private(path: str) -> bool:
    p = path.replace("\\", "/")
    if any(p == d or p.startswith(d + "/") for d in PRIVATE_DIRS):
        # workspace/README.md is the one tracked file in there, by design
        return not p.endswith("workspace/README.md")
    return os.path.basename(p) in PRIVATE_HINTS


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--upstream", default=None,
                    help="the ref your contribution is measured against "
                         "(default: upstream/main, or origin/main if you have no "
                         "upstream remote)")
    ap.add_argument("--quiet", action="store_true",
                    help="only print problems")
    args = ap.parse_args()

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ok, _ = git("rev-parse", "--git-dir", cwd=root)
    if not ok:
        print(f"{YELLOW}Not a git repository — nothing to check.{OFF}")
        print("If you downloaded this as a zip rather than cloning it, nothing "
              "here can be pushed anywhere, and you are safe by default.")
        return 0

    problems, notes = [], []

    # 1. Tracked private files — the one that actually bites people.
    ok, out = git("ls-files", cwd=root)
    tracked = [l for l in out.splitlines() if l.strip()] if ok else []
    tracked_private = [f for f in tracked if is_private(f)]
    if tracked_private:
        problems.append((
            "Private files are TRACKED by git",
            tracked_private,
            "These will be pushed. .gitignore does not apply to files git is\n"
            "  already tracking. To stop tracking them while keeping them on disk:\n"
            "      git rm --cached -r workspace\n"
            "      git commit -m \"stop tracking workspace\"",
        ))

    # 2. Staged right now.
    ok, out = git("diff", "--cached", "--name-only", cwd=root)
    staged_private = [f for f in out.splitlines() if f.strip() and is_private(f)] if ok else []
    if staged_private:
        problems.append((
            "Private files are STAGED for the next commit",
            staged_private,
            "Unstage them:  git restore --staged workspace",
        ))

    # 3. Anywhere in history — deleting a file does not remove it.
    ok, out = git("log", "--all", "--pretty=format:", "--name-only", cwd=root)
    if ok:
        hist = sorted({l for l in out.splitlines() if l.strip() and is_private(l)})
        if hist:
            problems.append((
                "Private files exist in your git HISTORY",
                hist,
                "Deleting a file does not remove it from history, and pushing this\n"
                "  branch publishes every commit on it. If this repository has never\n"
                "  been pushed anywhere, the simplest fix is to start its history\n"
                "  over:  rm -rf .git && git init\n"
                "  If it HAS been pushed to a fork, treat that data as disclosed and\n"
                "  make the fork private.",
            ))

    # 4. What a contribution branch would actually carry.
    # Contributors have an upstream remote; maintainers working in the canonical
    # repo only have origin. Try both rather than skipping the check.
    base = args.upstream
    if base is None:
        for candidate in ("upstream/main", "origin/main", "origin/HEAD"):
            if git("rev-parse", "--verify", candidate, cwd=root)[0]:
                base = candidate
                break
        base = base or "upstream/main"
    args.upstream = base
    ok, _ = git("rev-parse", "--verify", args.upstream, cwd=root)
    if ok:
        ok2, out = git("diff", "--name-only", f"{args.upstream}...HEAD", cwd=root)
        if ok2:
            changed = [l for l in out.splitlines() if l.strip()]
            carried = [f for f in changed if is_private(f)]
            if carried:
                problems.append((
                    f"Your branch carries private files relative to {args.upstream}",
                    carried,
                    "A pull request sends every commit on the branch, not just the\n"
                    "  file you meant to change. Build the contribution on a clean\n"
                    "  branch instead:\n"
                    "      git fetch upstream\n"
                    "      git checkout -b my-contribution upstream/main\n"
                    "  then copy only the corpus file you are changing onto it.",
                ))
            elif changed and not args.quiet:
                notes.append(f"Branch changes {len(changed)} file(s) vs "
                             f"{args.upstream}, none private:")
                notes.extend(f"    {f}" for f in changed[:20])
                if len(changed) > 20:
                    notes.append(f"    … and {len(changed) - 20} more")
    else:
        notes.append(f"{DIM}No upstream/main or origin/main ref — skipped the "
                     f"contribution check. Add one with:\n"
                     f"    git remote add upstream "
                     f"https://github.com/golden-section-tx/playbook.git\n"
                     f"    git fetch upstream{OFF}")

    # 5. Secrets in tracked files.
    hits = []
    for f in tracked:
        p = os.path.join(root, f)
        if not os.path.isfile(p) or os.path.getsize(p) > 2_000_000:
            continue
        try:
            text = open(p, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        for pat, label in SECRET_PATTERNS:
            if pat.search(text):
                hits.append(f"{f} — {label}")
                break
    if hits:
        problems.append((
            "Tracked files contain something that looks like a credential",
            hits,
            "Check these by hand. If any is real, rotate it — assume anything\n"
            "  committed is compromised.",
        ))

    # 6. Is the ignore rule even in place?
    gi = os.path.join(root, ".gitignore")
    text = open(gi, encoding="utf-8").read() if os.path.isfile(gi) else ""
    if "workspace" not in text:
        problems.append((
            ".gitignore does not mention workspace/",
            [".gitignore"],
            "Your company files are not ignored. Add:\n"
            "      workspace/*\n"
            "      !workspace/README.md",
        ))

    # Report.
    print()
    if problems:
        print(f"{RED}✗ Something private would leave your machine.{OFF}\n")
        for title, files, fix in problems:
            print(f"  {RED}{title}{OFF}")
            for f in files[:15]:
                print(f"    {f}")
            if len(files) > 15:
                print(f"    … and {len(files) - 15} more")
            print(f"  {DIM}Fix:{OFF} {fix}\n")
        print(f"{DIM}Nothing has been changed. Fix the above and run this "
              f"again.{OFF}\n")
        return 1

    for n in notes:
        print(n)
    print(f"\n{GREEN}✓ Clean.{OFF} No company files are tracked, staged, or in "
          f"history.")
    print(f"{DIM}workspace/ stays on this machine. Re-run this before every "
          f"push.{OFF}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
