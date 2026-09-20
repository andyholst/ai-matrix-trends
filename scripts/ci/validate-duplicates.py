#!/usr/bin/env python3
"""
validate-duplicates.py - Check for duplicate files with same title in same folder.
Stage 3 of CI pipeline.
"""

import os
import re
import sys
from collections import Counter

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    print("STAGE 3: Duplicate File Detection")
    print("=" * 60)
    
    total_dupes = 0
    folders_with_dupes = 0
    
    for folder in ['03 - Agents', '04 - Plugins', '05 - Architecture', 
                   '06 - Use Cases', '07 - Structure',
                   '09 - Trend Radar/Heating Up', '09 - Trend Radar/Stable', '09 - Trend Radar/Emerging']:
        folder_path = os.path.join(VAULT_DIR, folder)
        if not os.path.exists(folder_path):
            continue
        
        titles = Counter()
        for f in os.listdir(folder_path):
            if f.endswith('.md') and not f.startswith('00 -'):
                # Extract title
                if ' - ' in f:
                    title = f.split(' - ', 1)[1].replace('.md', '').lower()
                else:
                    title = f.replace('.md', '').lower()
                titles[title] += 1
        
        dupes = {t: c for t, c in titles.items() if c > 1}
        if dupes:
            folders_with_dupes += 1
            total_dupes += sum(c - 1 for c in dupes.values())
            print(f"\n{folder}:")
            for title, count in dupes.items():
                print(f"  DUPLICATE: {title} ({count} files)")
                # List the files
                for f in os.listdir(folder_path):
                    if f.endswith('.md') and not f.startswith('00 -'):
                        if ' - ' in f:
                            t = f.split(' - ', 1)[1].replace('.md', '').lower()
                        else:
                            t = f.replace('.md', '').lower()
                        if t == title:
                            print(f"    - {f}")
    
    print(f"\n{'=' * 60}")
    print(f"Folders with duplicates: {folders_with_dupes}")
    print(f"Total duplicate files: {total_dupes}")
    
    if total_dupes > 0:
        sys.exit(1)
    else:
        print("✓ No duplicate files")
        sys.exit(0)

if __name__ == '__main__':
    os.chdir(VAULT_DIR)
    main()