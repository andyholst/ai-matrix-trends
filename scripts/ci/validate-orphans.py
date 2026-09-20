#!/usr/bin/env python3
"""
validate-orphans.py - Detect orphan notes that aren't linked from anywhere.
Stage 6 of CI pipeline.
Checks wikilinks, markdown links, AND MOC references.
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
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
                fname = f.removesuffix('.md')
                rel_path = os.path.relpath(os.path.join(root, f), VAULT_DIR)
                file_map[fname.lower()] = rel_path
    return file_map

def find_linked_files():
    """Find all files that are linked from other files (wikilinks + markdown links)"""
    linked = set()
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                with open(filepath) as fh:
                    content = fh.read()
                
                # Wikilinks
                wikilinks = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
                for link in wikilinks:
                    linked.add(link.strip().lower())
                
                # Markdown links
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
                        clean_lower = clean_lower.removesuffix('.md')
                    linked.add(clean_lower)
                    # Also add just the filename
                    fname = os.path.basename(clean_lower)
                    linked.add(fname)
                
                # Frontmatter wikilinks
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
    
    skip_patterns = ['00 -', 'MOC-', 'AGENTS.md', 'README.md', 'LICENSE', 
                     'daily-scan-prompt.md', 'scripts/ci/', '.obsidian/templates/']
    
    orphans = []
    for fname, rel_path in file_map.items():
        if any(pattern in rel_path for pattern in skip_patterns):
            continue
        if fname not in linked_files:
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
