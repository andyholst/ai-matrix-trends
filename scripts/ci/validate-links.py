#!/usr/bin/env python3
"""
validate-links.py - Validate ALL links in vault (wikilinks + markdown links).
Stage 1 of CI pipeline.
FAILS when:
1. Wikilinks [[...]] point to non-existent files
2. Markdown links [text](path) point to non-existent files
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))

SKIP_FILES = {
    'AGENTS.md',
    'README.md',
    'LICENSE',
    'daily-scan-prompt.md',
}

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
                if ' - ' in fname:
                    title = fname.split(' - ', 1)[1]
                    file_map[title.lower()] = rel_path
    file_map['readme'] = 'README.md'
    return file_map

def validate_file(filepath, file_map):
    """Validate ALL links in a single file"""
    errors = []
    for skip in SKIP_FILES:
        if skip in filepath:
            return errors
    for folder in SKIP_FOLDERS:
        if folder in filepath:
            return errors
    with open(filepath) as f:
        content = f.read()
    
    # === Check wikilinks [[...]] ===
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        fm = fm_match.group(1)
        links_match = re.search(r'^links:\n((?:\s*-\s*"\[\[.*?\]\]"\n?)+)', fm, re.MULTILINE)
        if links_match:
            links = re.findall(r'"\[\[(.*?)\]\]"', links_match.group(1))
            for link in links:
                if link.lower() not in file_map:
                    errors.append(f"  Wikilink (frontmatter): [[{link}]] -> NOT FOUND")
    
    body_sections = content.split('\n## ')
    for section in body_sections[1:]:
        wikilinks = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', section)
        for link in wikilinks:
            link_lower = link.lower().strip()
            if link_lower not in file_map:
                if '[' in link or ']' in link or '{{' in link:
                    continue
                if link.endswith('/'):
                    continue
                errors.append(f"  Wikilink (body): [[{link}]] -> NOT FOUND")
    
    # === Check markdown links [text](path) ===
    md_links = re.findall(r'\]\(([^)]+)\)', content)
    for link in md_links:
        if link.startswith('http://') or link.startswith('https://'):
            continue
        if link.startswith('#'):
            continue
        clean = link
        if clean.startswith('./'):
            clean = clean[2:]
        elif clean.startswith('../'):
            clean = clean[3:]
        clean_lower = clean.replace('%20', ' ').lower()
        if clean_lower.endswith('/'):
            clean_lower = clean_lower.rstrip('/')
        if clean_lower.endswith('.md'):
            clean_no_ext = clean_lower[:-3]
        else:
            clean_no_ext = clean_lower
        
        # Check 1: full relative path
        if clean_no_ext in file_map:
            continue
        # Check 2: basename only
        fname = os.path.basename(clean_no_ext)
        if fname in file_map:
            continue
        # Check 3: title after " - "
        if ' - ' in fname:
            title = fname.split(' - ', 1)[1]
            if title in file_map:
                continue
        # Check 4: directory link
        test_dir = os.path.join(VAULT_DIR, clean_no_ext)
        if os.path.isdir(test_dir):
            continue
        # Check 5: filesystem
        test_file = os.path.join(VAULT_DIR, clean_no_ext + '.md')
        if os.path.isfile(test_file):
            continue
        
        errors.append(f"  Markdown link: {link} -> NOT FOUND")
    return errors

def main():
    print("STAGE 1: Link Validation (wikilinks + markdown links)")
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
    print(f"Total broken links: {total_errors}")
    if total_errors > 0:
        sys.exit(1)
    else:
        print("✓ All links valid")
        sys.exit(0)

if __name__ == '__main__':
    main()
