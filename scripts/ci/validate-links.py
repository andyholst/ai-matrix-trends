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
    """Build map of all existing files with lowercase keys"""
    file_map = {}
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                fname = f.replace('.md', '')
                rel_path = os.path.relpath(os.path.join(root, f), VAULT_DIR)
                # Store with lowercase key
                file_map[fname.lower()] = rel_path
                if ' - ' in fname:
                    title = fname.split(' - ', 1)[1]
                    file_map[title.lower()] = rel_path
    
    # Add special mappings
    file_map['readme'] = 'README.md'
    file_map['moc-plugin-ecosystem'] = '07 - Structure/MOC-Plugin-Ecosystem.md'
    file_map['moc-trending-agents'] = '07 - Structure/MOC-Trending-Agents.md'
    file_map['moc-architecture-patterns'] = '07 - Structure/MOC-Architecture-Patterns.md'
    file_map['moc-trend-radar'] = '07 - Structure/MOC-Trend-Radar.md'
    file_map['moc-use-cases'] = '07 - Structure/MOC-Use-Cases.md'
    
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
    # Frontmatter links
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        fm = fm_match.group(1)
        links_match = re.search(r'^links:\n((?:\s*-\s*"\[\[.*?\]\]"\n?)+)', fm, re.MULTILINE)
        if links_match:
            links = re.findall(r'"\[\[(.*?)\]\]"', links_match.group(1))
            for link in links:
                if link.lower() not in file_map:
                    errors.append(f"  Wikilink (frontmatter): [[{link}]] -> NOT FOUND")
    
    # Body wikilinks
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
        # Skip external links
        if link.startswith('http://') or link.startswith('https://'):
            continue
        
        # Skip anchors
        if link.startswith('#'):
            continue
        
        # Clean the link path
        clean = link
        
        # Remove ./ or ../
        if clean.startswith('./'):
            clean = clean[2:]
        elif clean.startswith('../'):
            clean = clean[3:]
        
        # Decode %20 and lowercase for matching
        clean_lower = clean.replace('%20', ' ').lower()
        
        # Remove trailing slash for directory links
        if clean_lower.endswith('/'):
            clean_lower = clean_lower.rstrip('/')
        
        # Remove .md extension
        if clean_lower.endswith('.md'):
            clean_no_ext = clean_lower[:-3]
        else:
            clean_no_ext = clean_lower
        
        # Check if file exists in file_map
        if clean_no_ext in file_map:
            continue
        
        # Check if it's a directory (folder link)
        test_dir = os.path.join(VAULT_DIR, clean_no_ext)
        if os.path.isdir(test_dir):
            continue
        
        # Check if file exists on filesystem (case-insensitive)
        found = False
        for root, dirs, files in os.walk(VAULT_DIR):
            if '/.git' in root:
                continue
            for f in files:
                if f.endswith('.md') and f.lower() == os.path.basename(clean_no_ext) + '.md':
                    found = True
                    break
            if found:
                break
        
        if not found:
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