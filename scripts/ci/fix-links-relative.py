#!/usr/bin/env python3
"""
fix-links-relative.py - Rewrite all markdown links so they resolve relative to
the CONTAINING FILE's directory (GitHub behavior), not the vault root.

For every [text](path) link in every .md file:
- If the target resolves relative to the file's own dir -> keep
- Else if it resolves relative to the vault root -> rewrite to correct
  file-relative path (../dir/file.md), %20-encoded
- Else -> leave untouched (missing target; validators will report it)

Idempotent: running twice produces the same result.
"""

import os
import re
import sys
from urllib.parse import quote, unquote

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))

SKIP_DIRS = {'.git', '.obsidian', '__pycache__'}
SKIP_FILES = {'AGENTS.md'}  # AGENTS.md has example links; do not rewrite

MD_LINK_RE = re.compile(r'\]\(([^)\s]+)\)')

def encode_path(rel):
    """URL-encode a relative path (spaces -> %20), keeping / and . intact."""
    return quote(rel, safe='/._-')

def resolve(from_dir, link):
    """Return absolute path of link resolved from from_dir, or None."""
    clean = unquote(link.split('#')[0])
    if not clean:
        return None
    return os.path.normpath(os.path.join(from_dir, clean))

def fix_file(filepath):
    """Fix all markdown links in one file. Returns (rewritten, missing)."""
    rel_file = os.path.relpath(filepath, VAULT_DIR)
    if os.path.basename(filepath) in SKIP_FILES:
        return 0, 0
    with open(filepath) as f:
        content = f.read()

    # Strip code blocks so we never rewrite links inside ``` fences
    segments = re.split(r'(```.*?```)', content, flags=re.DOTALL)

    rewritten = 0
    missing = 0
    from_dir = os.path.dirname(filepath)

    for i, seg in enumerate(segments):
        if i % 2 == 1:  # inside code fence
            continue

        def repl(m):
            nonlocal rewritten, missing
            link = m.group(1)
            if link.startswith(('http://', 'https://', '#', 'mailto:')):
                return m.group(0)
            # File-relative resolution first
            target = resolve(from_dir, link)
            if target and (os.path.isfile(target) or os.path.isdir(target)):
                return m.group(0)  # already correct
            # Vault-root resolution (the broken pattern)
            stripped = unquote(link.split('#')[0]).lstrip('./')
            anchor = ('#' + link.split('#')[1]) if '#' in link else ''
            root_target = os.path.normpath(os.path.join(VAULT_DIR, stripped))
            if os.path.isfile(root_target) or os.path.isdir(root_target):
                new_rel = os.path.relpath(root_target, from_dir)
                rewritten += 1
                return f']({encode_path(new_rel)}{anchor})'
            missing += 1
            return m.group(0)

        segments[i] = MD_LINK_RE.sub(repl, seg)

    new_content = ''.join(segments)
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
    return rewritten, missing

def main():
    print("FIXING LINKS (file-relative resolution)")
    print("=" * 60)
    total_rewritten = 0
    total_missing = 0
    files_changed = 0
    missing_by_file = {}

    for root, dirs, files in os.walk(VAULT_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        if '/scripts' in root.replace(VAULT_DIR, ''):
            continue
        for f in sorted(files):
            if not f.endswith('.md'):
                continue
            r, m = fix_file(os.path.join(root, f))
            total_rewritten += r
            total_missing += m
            if r:
                files_changed += 1
            if m:
                missing_by_file[os.path.relpath(os.path.join(root, f), VAULT_DIR)] = m

    print(f"Files rewritten: {files_changed}")
    print(f"Links rewritten: {total_rewritten}")
    print(f"Links with missing targets: {total_missing}")
    if missing_by_file:
        print("\nFiles with missing targets (need manual attention or creation):")
        for fp in sorted(missing_by_file):
            print(f"  {fp}: {missing_by_file[fp]}")

if __name__ == '__main__':
    main()
