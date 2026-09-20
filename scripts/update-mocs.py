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
    # Find all [[...]] patterns
    links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    for link in links:
        entries.add(link.strip())
    return entries

def update_moc(folder, moc_file):
    """Update a MOC file with notes from a folder (idempotent)"""
    moc_path = os.path.join(VAULT_DIR, moc_file)
    notes = get_notes_in_folder(folder)
    
    if not os.path.exists(moc_path):
        # Create new MOC
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
        # Read existing MOC
        with open(moc_path) as f:
            content = f.read()
        
        # Extract all existing entries (deduplicate)
        existing = extract_existing_entries(content)
        
        # Build set of expected entries (current files in folder)
        expected = set(notes)
        
        # Find entries to add (in expected but not in existing)
        # But we need to normalize: both should be full filenames
        to_add = []
        for note in notes:
            # Check if this note or its resolved form already exists
            note_lower = note.lower()
            found = False
            for existing_entry in existing:
                if existing_entry.lower() == note_lower:
                    found = True
                    break
            if not found:
                to_add.append(note)
        
        # Add new notes at the end of Key Notes section (before ## Clusters or end)
        if to_add:
            # Find where to insert (after ## Key Notes, before next ## section)
            lines = content.split('\n')
            insert_idx = len(lines)
            for i, line in enumerate(lines):
                if line.startswith('## ') and 'Key Notes' not in line and i > 0:
                    insert_idx = i
                    break
            
            # Insert new notes before the next section
            new_lines = []
            for note in to_add:
                new_lines.append(f"- [[{note}]] - [auto-summary]")
            
            lines = lines[:insert_idx] + new_lines + lines[insert_idx:]
            content = '\n'.join(lines)
    
    # Deduplicate entries throughout the file
    content = deduplicate_moc_entries(content)
    
    with open(moc_path, 'w') as f:
        f.write(content)
    
    print(f"Updated {moc_file} with {len(notes)} notes from {folder}")

def deduplicate_moc_entries(content):
    """Remove duplicate wikilinks from MOC while preserving structure"""
    lines = content.split('\n')
    seen = set()
    new_lines = []
    
    for line in lines:
        # Check if this line contains a wikilink
        match = re.match(r'^(\s*-\s*)\[\[([^\]|]+)(?:\|[^\]]+)?\]\](\s*.*)$', line)
        if match:
            prefix = match.group(1)
            link = match.group(2).strip()
            suffix = match.group(3)
            
            # Normalize for comparison
            link_lower = link.lower()
            
            if link_lower in seen:
                # Skip duplicate
                continue
            else:
                seen.add(link_lower)
                new_lines.append(line)
        else:
            new_lines.append(line)
    
    return '\n'.join(new_lines)

def main():
    print("UPDATING MOCS")
    print("=" * 60)
    os.chdir(VAULT_DIR)
    
    for folder, moc_file in MOC_MAPPINGS.items():
        update_moc(folder, moc_file)

if __name__ == '__main__':
    main()