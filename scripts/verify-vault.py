#!/usr/bin/env python3
"""
Verify vault links are working correctly.
"""

import os
import re

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")

def build_file_map():
    file_map = {}
    # Include folder paths (for wikilinks like [[03 - Agents/|All Agents]])
    folder_aliases = {
        '03 - agents': '03 - Agents',
        '04 - plugins': '04 - Plugins',
        '05 - architecture': '05 - Architecture',
        '06 - use cases': '06 - Use Cases',
        '07 - structure': '07 - Structure',
        '08 - projects': '08 - Projects',
        '09 - trend radar': '09 - Trend Radar',
        '00 - inbox': '00 - Inbox',
        '01 - fleeting': '01 - Fleeting',
        '02 - literature': '02 - Literature',
        '99 - attachments': '99 - Attachments',
    }
    for alias, folder in folder_aliases.items():
        file_map[alias] = folder
        file_map[folder.lower()] = folder
    
    # Include root-level files
    for f in os.listdir(VAULT_DIR):
        if f.endswith('.md'):
            fname = f.replace('.md', '')
            file_map[fname.lower()] = fname
            file_map[fname.lower().replace(' ', '-')] = fname
            if ' - ' in fname:
                title = fname.split(' - ', 1)[1]
                file_map[title.lower().replace(' ', '-')] = fname
                file_map[title.lower()] = fname
    
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
                            # Handle pipe aliases: [[path|display]] -> match on path
                            if '|' in link:
                                link = link.split('|')[0]
                            # Handle relative path wikilinks: [[..README]] -> README
                            if link.startswith('..'):
                                link = link[2:]
                            # Handle relative path wikilinks: [[03 - Agents/]] -> 03 - Agents
                            if link.endswith('/'):
                                link = link[:-1]
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
