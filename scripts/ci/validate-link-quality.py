#!/usr/bin/env python3
"""
validate-link-quality.py - Validate quality of frontmatter links.
Stage 9 of CI pipeline.
FAILS when:
1. Links use wikilink format [[...]] instead of markdown [text](path)
2. Link target files don't exist
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))

# Files to skip
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
                fname = f.replace('.md', '')
                rel_path = os.path.relpath(os.path.join(root, f), VAULT_DIR)
                file_map[fname.lower()] = rel_path
                if ' - ' in fname:
                    title = fname.split(' - ', 1)[1]
                    file_map[title.lower()] = rel_path
    return file_map

def validate_file(filepath, file_map):
    """Check if file has fishy frontmatter links"""
    errors = []
    
    # Skip certain files
    for skip in SKIP_FILES:
        if skip in filepath:
            return errors
    
    # Skip certain folders
    for folder in SKIP_FOLDERS:
        if folder in filepath:
            return errors
    
    with open(filepath) as f:
        content = f.read()
    
    # Parse frontmatter
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return errors
    
    fm = fm_match.group(1)
    
    # Find links section
    links_match = re.search(r'^links:\n((?:\s*-\s*"\[\[.*?\]\]"\n?)+)', fm, re.MULTILINE)
    if not links_match:
        return errors
    
    links = re.findall(r'"\[\[(.*?)\]\]"', links_match.group(1))
    
    for link in links:
        # Check if it's a wikilink (should be markdown link)
        # Wikilinks in frontmatter are fishy - they should be markdown links
        errors.append(f"  Wikilink in frontmatter: [[{link}]] (should be markdown link [title](path))")
        
        # Check if target exists
        link_lower = link.lower().strip()
        if link_lower not in file_map:
            errors.append(f"  Missing target: [[{link}]] (file does not exist)")
    
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
        print("  - Wikilinks [[...]] should be markdown links [title](path)")
        print("  - Missing target files should be created")
        sys.exit(1)
    else:
        print("✓ All links are high quality")
        sys.exit(0)

if __name__ == '__main__':
    main()