#!/usr/bin/env python3
"""
validate-link-quality.py - Validate quality of all links in vault.
Stage 9 of CI pipeline.
FAILS when:
1. Any wikilink [[...]] found (should be markdown link [title](path))
2. Markdown links point to non-existent files
"""

import os
import re
import sys
from urllib.parse import unquote

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))

SKIP_FILES = [
    'AGENTS.md',
    'README.md',
    'LICENSE',
    'daily-scan-prompt.md',
]

SKIP_FOLDERS = [
    '.obsidian',
    'scripts/ci',
    '00 - Inbox',
]

def build_file_map():
    """Build map of all existing files: lowered_filename -> relative_path"""
    file_map = {}
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                fname = f.removesuffix('.md')
                rel_path = os.path.relpath(os.path.join(root, f), VAULT_DIR)
                file_map[fname.lower()] = rel_path
                file_map[fname.lower() + '.md'] = rel_path
                if ' - ' in fname:
                    title = fname.split(' - ', 1)[1]
                    file_map[title.lower()] = rel_path
                    file_map[title.lower() + '.md'] = rel_path
    file_map['readme.md'] = 'README.md'
    file_map['readme'] = 'README.md'
    return file_map

def validate_file(filepath, file_map):
    """Validate ALL links in a file"""
    errors = []
    for skip in SKIP_FILES:
        if skip in filepath:
            return errors
    for folder in SKIP_FOLDERS:
        if folder in filepath:
            return errors
    with open(filepath) as f:
        content = f.read()
    
    # Strip code blocks so links inside fences are not checked
    body = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    
    # Strip frontmatter so Obsidian [[...]] links aren't flagged
    fm_match = re.match(r'^---\n.*?\n---\n', content, flags=re.DOTALL)
    if fm_match:
        body = content[fm_match.end():]
    else:
        body = content
    
    # === Check wikilinks [[...]] ===
    wikilinks = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', body)
    for link in wikilinks:
        link_lower = link.lower().strip()
        if link_lower not in file_map:
            errors.append(f"  Missing target: [[{link}]] (file does not exist)")
        else:
            target_path = file_map[link_lower]
            encoded_path = target_path.replace(' ', '%20')
            title = link.split(' - ', 1)[1] if ' - ' in link else link
            errors.append(f"  Wikilink: [[{link}]] (should be markdown: [{title}](./{encoded_path}))")
    
    # === Check markdown links [text](path) — FILE-RELATIVE (GitHub behavior) ===
    from_dir = os.path.dirname(filepath)
    for link in re.findall(r'\]\(([^)]+)\)', body):
        if link.startswith(('http://', 'https://', '#', 'mailto:')):
            continue
        clean = unquote(link.split('#')[0])
        if not clean:
            continue
        target = os.path.normpath(os.path.join(from_dir, clean))
        if os.path.isfile(target) or os.path.isdir(target):
            continue
        resolved = os.path.relpath(target, VAULT_DIR)
        errors.append(f"  Markdown link: {link} -> NOT FOUND (resolves to: {resolved})")
    
    return errors

def main():
    print("STAGE 9: Link Quality Validation")
    print("=" * 60)
    file_map = build_file_map()
    print(f"Built file map: {len(file_map)} entries")
    total_errors = 0
    files_with_errors = 0
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                errors = validate_file(filepath, file_map)
                if errors:
                    files_with_errors += 1
                    total_errors += len(errors)
                    rel_path = os.path.relpath(filepath, VAULT_DIR)
                    print(f"\n{rel_path}:")
                    for error in errors:
                        print(error)
    print(f"\n{'=' * 60}")
    print(f"Files with errors: {files_with_errors}")
    print(f"Total errors: {total_errors}")
    if total_errors > 0:
        print(f"✗ FAIL: {total_errors} link quality issues detected")
        sys.exit(1)
    else:
        print("✓ All links are high quality")
        sys.exit(0)

if __name__ == '__main__':
    main()
