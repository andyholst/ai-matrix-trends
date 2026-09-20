#!/usr/bin/env python3
"""
validate-orphans.py - Detect orphan notes that aren't linked from anywhere.
Stage 6 of CI pipeline.
"""

import os
import re
import sys

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def build_file_map():
    """Build map of all existing files"""
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

def find_linked_files():
    """Find all files that are linked from other files"""
    linked = set()
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                with open(filepath) as fh:
                    content = fh.read()
                
                # Find all wikilinks
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
    
    file_map = build_file_map()
    linked_files = find_linked_files()
    
    # Files to skip (indexes, MOCs, templates)
    skip_patterns = ['00 -', 'MOC-', 'AGENTS.md', 'README.md', 'LICENSE', 'daily-scan-prompt.md']
    
    orphans = []
    for fname, rel_path in file_map.items():
        # Skip index files and templates
        if any(pattern in rel_path for pattern in skip_patterns):
            continue
        
        # Check if file is linked
        if fname not in linked_files:
            # Check if title is linked
            if ' - ' in fname:
                title = fname.split(' - ', 1)[1]
                if title in linked_files:
                    continue
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
        # Orphans are warnings, not failures
        print("⚠ Orphans detected (warning only)")
        sys.exit(0)
    else:
        print("✓ No orphan files")
        sys.exit(0)

if __name__ == '__main__':
    os.chdir(VAULT_DIR)
    main()