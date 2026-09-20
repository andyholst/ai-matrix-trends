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
    """Get all .md files in folder, sorted"""
    folder_path = os.path.join(VAULT_DIR, folder)
    if not os.path.exists(folder_path):
        return []
    return sorted([f.replace('.md', '') for f in os.listdir(folder_path) if f.endswith('.md')])

def extract_existing_entries(content):
    """Extract all wikilink entries from MOC content"""
    entries = set()
    links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    for link in links:
        entries.add(link.strip().lower())
    return entries

def deduplicate_moc_content(content):
    """Remove duplicate wikilinks from MOC while preserving structure"""
    lines = content.split('\n')
    seen = set()
    new_lines = []
    
    for line in lines:
        match = re.match(r'^(\s*-\s*)\[\[([^\]|]+)(?:\|[^\]]+)?\]\](\s*.*)$', line)
        if match:
            prefix = match.group(1)
            link = match.group(2).strip()
            suffix = match.group(3)
            
            link_lower = link.lower()
            
            if link_lower in seen:
                continue
            else:
                seen.add(link_lower)
                new_lines.append(line)
        else:
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
            content += f"- [[{note}]] - [auto-summary]\n"
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
            for note in to_add:
                new_lines.append(f"- [[{note}]] - [auto-summary]")
            
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