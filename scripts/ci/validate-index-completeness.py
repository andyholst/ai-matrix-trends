#!/usr/bin/env python3
"""
validate-index-completeness.py - Validate that all notes are indexed in MOCs.
Stage 5 of CI pipeline.
"""

import os
import re
import sys

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")

MOC_MAPPINGS = {
    '03 - Agents': '07 - Structure/MOC-Trending-Agents.md',
    '04 - Plugins': '07 - Structure/MOC-Plugin-Ecosystem.md',
    '05 - Architecture': '07 - Structure/MOC-Architecture-Patterns.md',
    '09 - Trend Radar': '07 - Structure/MOC-Trend-Radar.md',
}

def extract_moc_entries(moc_content):
    """Extract all wikilink entries from MOC"""
    entries = set()
    links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', moc_content)
    for link in links:
        entries.add(link.strip().lower())
    return entries

def get_folder_notes(folder_path):
    """Get all note filenames in a folder"""
    notes = set()
    if not os.path.exists(folder_path):
        return notes
    for f in os.listdir(folder_path):
        if f.endswith('.md') and not f.startswith('00 -'):
            notes.add(f.replace('.md', '').lower())
    return notes

def main():
    print("STAGE 5: Index Completeness")
    print("=" * 60)
    
    total_missing = 0
    folders_with_missing = 0
    
    for folder, moc_file in MOC_MAPPINGS.items():
        folder_path = os.path.join(VAULT_DIR, folder)
        moc_path = os.path.join(VAULT_DIR, moc_file)
        
        if not os.path.exists(moc_path):
            print(f"  WARNING: MOC file not found: {moc_file}")
            continue
        
        with open(moc_path) as f:
            moc_content = f.read()
        
        moc_entries = extract_moc_entries(moc_content)
        folder_notes = get_folder_notes(folder_path)
        
        missing = folder_notes - moc_entries
        
        if missing:
            folders_with_missing += 1
            total_missing += len(missing)
            print(f"\n{folder}:")
            for note in sorted(missing):
                print(f"  MISSING FROM MOC: {note}")
    
    print(f"\n{'=' * 60}")
    print(f"Folders with missing entries: {folders_with_missing}")
    print(f"Total missing from MOCs: {total_missing}")
    
    if total_missing > 0:
        sys.exit(1)
    else:
        print("✓ All notes indexed")
        sys.exit(0)

if __name__ == '__main__':
    os.chdir(VAULT_DIR)
    main()