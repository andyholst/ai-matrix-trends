#!/usr/bin/env python3
"""
validate-orphans.py - Detect orphan notes that aren't linked from anywhere.
Stage 6 of CI pipeline.
FAILS the pipeline when orphans are detected (not just a warning).
"""

import os
import re
import sys

# Get the vault root directory (3 levels up from this script)
SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
CI_DIR = os.path.dirname(SCRIPT_DIR)
VAULT_DIR = os.path.dirname(CI_DIR)

def build_file_map():
    """Build map of all existing files: lowered_filename -> relative_path"""
    file_map = {}
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                fname = f.replace('.md', '')
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, VAULT_DIR)
                # Store by lowered filename
                file_map[fname.lower()] = rel_path
    return file_map

def find_linked_files():
    """Find all files that are linked from other files (wikilinks + frontmatter)"""
    linked = set()
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                with open(filepath) as fh:
                    content = fh.read()
                
                # Find all wikilinks in body
                wikilinks = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
                for link in wikilinks:
                    linked.add(link.strip().lower())
                
                # Find frontmatter links
                fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
                if fm_match:
                    fm = fm_match.group(1)
                    links_match = re.search(r'^links:\n((?:\s*-\s*"\[\[.*?\]\]"\n?)+)', fm, re.MULTILINE)
                    if links_match:
                        links = re.findall(r'"\[\[(.*?)\]\]"', links_match.group(1))
                        for link in links:
                            linked.add(link.strip().lower())
    
    return linked

def main():
    print("STAGE 6: Orphan Detection")
    print("=" * 60)
    print(f"Vault: {VAULT_DIR}")
    
    file_map = build_file_map()
    linked_files = find_linked_files()
    
    # Files to skip (indexes, MOCs, templates, scripts)
    skip_patterns = ['00 -', 'MOC-', 'AGENTS.md', 'README.md', 'LICENSE', 
                     'daily-scan-prompt.md', 'scripts/ci/', '.obsidian/templates/']
    
    orphans = []
    for fname, rel_path in file_map.items():
        # Skip index files, templates, and scripts
        if any(pattern in rel_path for pattern in skip_patterns):
            continue
        
        # Check if file is linked (by full filename)
        if fname not in linked_files:
            # Also check by title only (after " - ")
            title = fname.split(' - ', 1)[1] if ' - ' in fname else fname
            if title not in linked_files:
                orphans.append(rel_path)
    
    print(f"Total files: {len(file_map)}")
    print(f"Linked files: {len(linked_files)}")
    print(f"Orphan files: {len(orphans)}")
    
    if orphans:
        print("\nOrphan files (not linked from anywhere):")
        for orphan in sorted(orphans):
            print(f"  {orphan}")
    
    print(f"\n{'=' * 60}")
    if orphans:
        print(f"✗ FAIL: {len(orphans)} orphan files detected")
        print("  These notes should be linked from other notes or indexed in MOCs")
        sys.exit(1)
    else:
        print("✓ No orphan files")
        sys.exit(0)

if __name__ == '__main__':
    main()