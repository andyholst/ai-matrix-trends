#!/usr/bin/env python3
"""
Verify vault links are working correctly.
"""

import os
import re

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")

def build_file_map():
    file_map = {}
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                fname = f.replace('.md', '')
                file_map[fname.lower()] = fname
                if ' - ' in fname:
                    title = fname.split(' - ', 1)[1]
                    file_map[title.lower().replace(' ', '-')] = fname
    
    file_map['moc-trending-agents'] = 'MOC-Trending-Agents'
    file_map['moc-plugin-ecosystem'] = 'MOC-Plugin-Ecosystem'
    file_map['moc-architecture-patterns'] = 'MOC-Architecture-Patterns'
    file_map['moc-trend-radar'] = 'MOC-Trend-Radar'
    
    return file_map

def verify():
    file_map = build_file_map()
    issues = 0
    total = 0
    
    for folder in ['03 - Agents', '04 - Plugins', '05 - Architecture', '06 - Use Cases', '09 - Trend Radar/Heating Up', '09 - Trend Radar/Stable', '09 - Trend Radar/Emerging']:
        folder_path = os.path.join(VAULT_DIR, folder)
        if not os.path.exists(folder_path):
            continue
        for f in os.listdir(folder_path):
            if f.endswith('.md'):
                total += 1
                path = os.path.join(folder_path, f)
                with open(path) as fh:
                    content = fh.read()
                
                fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
                if fm_match:
                    fm = fm_match.group(1)
                    links_match = re.search(r'^links:\n((?:\s*-\s*"\[\[.*?\]\]"\n?)+)', fm, re.MULTILINE)
                    if links_match:
                        links = re.findall(r'"\[\[(.*?)\]\]"', links_match.group(1))
                        for link in links:
                            if ' - ' in link:
                                title = link.split(' - ', 1)[1].lower().replace(' ', '-')
                            else:
                                title = link.lower().replace(' ', '-')
                            if title not in file_map and 'moc' not in title:
                                print(f"BROKEN: {folder}/{f} -> [[{link}]]")
                                issues += 1
    
    print(f"\nVerified {total} notes, {issues} issues")
    return issues == 0

if __name__ == '__main__':
    os.chdir(VAULT_DIR)
    if verify():
        print("✓ VAULT IS CLEAN")
    else:
        print("✗ VAULT HAS ISSUES - Run fix_all_links.py first")
        exit(1)
