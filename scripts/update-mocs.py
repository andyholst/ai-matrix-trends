#!/usr/bin/env python3
"""
Update MOCs with new notes from vault folders.
Run after fix-links.py.
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

def update_moc(folder, moc_file):
    """Update a MOC file with notes from a folder"""
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
        # Update existing MOC
        with open(moc_path) as f:
            content = f.read()
        
        # Add new notes that aren't already in the MOC
        for note in notes:
            if f'[[{note}]]' not in content:
                content += f"- [[{note}]] - [auto-summary]\n"
    
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
