#!/usr/bin/env python3
"""
Update MOCs with new notes from vault folders.
Run after fix-all-links.py.
Idempotent - running multiple times produces the same result.
"""

import os
import re

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")

MOC_MAPPINGS = {
    '03 - Agents': '07 - Structure/MOC-Trending-Agents.md',
    '04 - Plugins': '07 - Structure/MOC-Plugin-Ecosystem.md',
    '05 - Architecture': '07 - Structure/MOC-Architecture-Patterns.md',
    '06 - Use Cases': '07 - Structure/MOC-Use-Cases.md',
    '09 - Trend Radar': '07 - Structure/MOC-Trend-Radar.md',
}

def get_notes_in_folder(folder):
    """Get all .md files in folder (including subfolders), sorted"""
    folder_path = os.path.join(VAULT_DIR, folder)
    if not os.path.exists(folder_path):
        return []
    notes = []
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            if f.endswith('.md') and not f.startswith('00 -'):
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, VAULT_DIR)
                notes.append(rel_path.removesuffix('.md'))
    return sorted(notes)

def extract_existing_entries(content):
    """Extract all link entries from MOC content (wikilinks + markdown links)"""
    entries = set()
    # Wikilinks
    links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    for link in links:
        entries.add(link.strip().lower())
    # Markdown links
    md_links = re.findall(r'\]\(([^)]+)\)', content)
    for link in md_links:
        if not link.startswith('http'):
            entries.add(link.strip().lower().replace('%20', ' '))
    return entries

def deduplicate_moc_content(content):
    """Remove duplicate links from MOC (wikilinks + markdown links)"""
    lines = content.split('\n')
    seen = set()
    new_lines = []
    
    for line in lines:
        # Check for wikilinks
        match = re.match(r'^(\s*-\s*)\[\[([^\]|]+)(?:\|[^\]]+)?\]\](\s*.*)$', line)
        if match:
            link = match.group(2).strip()
            link_lower = link.lower()
            if link_lower in seen:
                continue
            seen.add(link_lower)
            new_lines.append(line)
            continue
        
        # Check for markdown links
        match = re.match(r'^(\s*-\s*)\[([^\]]+)\]\(([^)]+)\)(\s*.*)$', line)
        if match:
            link = match.group(3).strip().replace('%20', ' ').lower()
            if link in seen:
                continue
            seen.add(link)
            new_lines.append(line)
            continue
        
        new_lines.append(line)
    
    return '\n'.join(new_lines)

def update_moc(folder, moc_file):
    """Update a MOC file with notes from a folder (idempotent)"""
    moc_path = os.path.join(VAULT_DIR, moc_file)
    notes = get_notes_in_folder(folder)
    
    if not os.path.exists(moc_path):
        content = f"""---
tags:
  - moc
---

# MOC: {os.path.basename(folder)}

## Overview
Auto-generated Map of Content for {folder}.

## Key Notes
"""
        for note in notes:
            # note is vault-root-relative; MOC lives in 07 - Structure/
            moc_dir = os.path.dirname(moc_path)
            link_path = os.path.relpath(os.path.join(VAULT_DIR, note + '.md'), moc_dir)
            content += f"- [{note}](./{link_path.replace(' ', '%20')}) - [auto-summary]\n"
    else:
        with open(moc_path) as f:
            content = f.read()
        
        existing = extract_existing_entries(content)
        
        to_add = []
        for note in notes:
            if note.lower() not in existing:
                to_add.append(note)
        
        if to_add:
            lines = content.split('\n')
            insert_idx = len(lines)
            for i, line in enumerate(lines):
                if line.startswith('## ') and 'Key Notes' not in line and i > 0:
                    insert_idx = i
                    break
            
            new_lines = []
            moc_dir = os.path.dirname(moc_path)
            for note in to_add:
                link_path = os.path.relpath(os.path.join(VAULT_DIR, note + '.md'), moc_dir)
                new_lines.append(f"- [{note}](./{link_path.replace(' ', '%20')}) - [auto-summary]")
            
            lines = lines[:insert_idx] + new_lines + lines[insert_idx:]
            content = '\n'.join(lines)
    
    content = deduplicate_moc_content(content)
    
    with open(moc_path, 'w') as f:
        f.write(content)
    
    print(f"Updated {moc_file} with {len(notes)} notes from {folder}")

def main():
    print("UPDATING MOCS")
    print("=" * 60)
    os.chdir(VAULT_DIR)
    
    for folder, moc_file in MOC_MAPPINGS.items():
        update_moc(folder, moc_file)

if __name__ == '__main__':
    main()