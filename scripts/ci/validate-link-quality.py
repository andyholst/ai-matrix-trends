#!/usr/bin/env python3
"""
validate-link-quality.py - Validate quality of all links in vault.
Stage 9 of CI pipeline.
FAILS when:
1. Any wikilink [[...]] found (should be markdown link [title](path))
2. Link target files don't exist
"""

import os
import re
import sys

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
    '07 - Structure',  # MOCs use wikilinks intentionally
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
                # Add without .md extension
                file_map[fname.lower()] = rel_path
                # Also add with .md extension for matching
                file_map[fname.lower() + '.md'] = rel_path
                if ' - ' in fname:
                    title = fname.split(' - ', 1)[1]
                    file_map[title.lower()] = rel_path
                    file_map[title.lower() + '.md'] = rel_path
    # Add special mappings for common references
    file_map['readme.md'] = 'README.md'
    file_map['readme'] = 'README.md'
    
    return file_map

def validate_file(filepath, file_map):
    """Check if file has any wikilinks (should be markdown links)"""
    errors = []
    
    for skip in SKIP_FILES:
        if skip in filepath:
            return errors
    
    for folder in SKIP_FOLDERS:
        if folder in filepath:
            return errors
    
    with open(filepath) as f:
        content = f.read()
    
    # Find ALL wikilinks in the entire file
    wikilinks = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    
    for link in wikilinks:
        link_lower = link.lower().strip()
        
        # Check if target exists
        if link_lower not in file_map:
            errors.append(f"  Missing target: [[{link}]] (file does not exist)")
        else:
            # Target exists but wikilink should be markdown link
            target_path = file_map[link_lower]
            encoded_path = target_path.replace(' ', '%20')
            title = link.split(' - ', 1)[1] if ' - ' in link else link
            errors.append(f"  Wikilink: [[{link}]] (should be markdown: [{title}](./{encoded_path}))")
    
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
        print("  - All [[wikilinks]] should be markdown links [title](path)")
        print("  - Missing target files should be created")
        sys.exit(1)
    else:
        print("✓ All links are high quality")
        sys.exit(0)

if __name__ == '__main__':
    main()