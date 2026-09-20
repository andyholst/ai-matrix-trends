#!/usr/bin/env python3
"""
fix_all_links.py - Comprehensive link fixer for AI Matrix Trends vault.
- Resolves ALL wikilinks ([[Short Name]] -> [[YYYYMMDDHHMM - Actual Title]])
- Fixes frontmatter links
- Fixes body wikilinks
- NEVER deletes files
- Adds missing frontmatter links fields
"""

import os
import re
import sys

VAULT = os.path.expanduser("~/repository/git/ai-matrix-trends")

def build_maps():
    """Build lookup maps from actual vault files"""
    by_exact = {}
    by_title = {}
    by_word = {}
    
    for root, dirs, files in os.walk(VAULT):
        if '/.git' in root:
            continue
        for f in files:
            if not f.endswith('.md'):
                continue
            fname = f.replace('.md', '')
            rel_path = os.path.relpath(os.path.join(root, f), VAULT)
            
            # Exact match
            by_exact[fname.lower()] = fname
            
            # Title (after timestamp)
            if ' - ' in fname:
                title = fname.split(' - ', 1)[1]
                by_title[title.lower()] = fname
                by_title[title.lower().replace(' ', '-').replace("'", "")] = fname
                
                # Word-level
                for word in title.lower().split():
                    if len(word) > 3:
                        by_word[word] = fname
    
    # MOCs
    by_title['moc-trending-agents'] = 'MOC-Trending-Agents'
    by_title['moc-plugin-ecosystem'] = 'MOC-Plugin-Ecosystem'
    by_title['moc-architecture-patterns'] = 'MOC-Architecture-Patterns'
    by_title['moc-trend-radar'] = 'MOC-Trend-Radar'
    
    # Common short names
    short_names = {
        'claude-code': '202609202000 - Claude Code',
        'codex': '202609202000 - Codex',
        'openai-codex': '202609202000 - Codex',
        'cursor': '202609202000 - Cursor',
        'windsurf': '202609200800 - Windsurf',
        'opencode': '202609200758 - OpenCode',
        'hermes': '202609200759 - Hermes Agent',
        'hermes-agent': '202609200759 - Hermes Agent',
        'aider': '202609202000 - Aider',
        'cline': '202609202000 - Cline',
        'vscode': '202609202000 - Cursor',
    }
    by_title.update({k: v for k, v in short_names.items() if v.lower() in [x.lower() for x in by_exact.values()]})
    
    return by_exact, by_title, by_word

def resolve(link, by_exact, by_title, by_word):
    """Resolve a wikilink to actual filename"""
    link_lower = link.lower().replace(' ', '-').replace("'", "")
    
    # Exact
    if link_lower in by_exact:
        return by_exact[link_lower]
    
    # Title
    if link_lower in by_title:
        return by_title[link_lower]
    
    # Without timestamp
    if ' - ' in link:
        title = link.split(' - ', 1)[1].lower().replace(' ', '-').replace("'", "")
        if title in by_title:
            return by_title[title]
        if title in by_exact:
            return by_exact[title]
    
    # Word match
    for word in link_lower.split('-'):
        if word in by_word:
            return by_word[word]
    
    return None

def fix_file(filepath, by_exact, by_title, by_word):
    """Fix all links in a file"""
    with open(filepath) as f:
        content = f.read()
    
    original = content
    fixes = 0
    
    # Fix frontmatter
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        fm = fm_match.group(1)
        
        # Find links section
        links_match = re.search(r'^links:\n((?:\s*-\s*"\[\[.*?\]\]"\n?)+)', fm, re.MULTILINE)
        
        if links_match:
            links_text = links_match.group(1)
            links = re.findall(r'"\[\[(.*?)\]\]"', links_text)
            new_links = []
            
            for link in links:
                actual = resolve(link, by_exact, by_title, by_word)
                if actual and actual != link:
                    new_links.append(f'  - "[[{actual}]]"')
                    fixes += 1
                elif actual:
                    new_links.append(f'  - "[[{link}]]"')
                else:
                    # Find any file containing the link text
                    found = False
                    for root, dirs, files in os.walk(VAULT):
                        if '/.git' in root:
                            continue
                        for f in files:
                            if f.endswith('.md') and link.lower() in f.lower():
                                actual = f.replace('.md', '')
                                new_links.append(f'  - "[[{actual}]]"')
                                fixes += 1
                                found = True
                                break
                        if found:
                            break
                    if not found:
                        new_links.append(f'  - "[[{link}]]"')
            
            old_section = links_match.group(0)
            new_section = 'links:\n' + '\n'.join(new_links)
            content = content.replace(fm, fm.replace(old_section, new_section))
        else:
            # No links field - add one
            folder = os.path.dirname(filepath)
            others = [f2.replace('.md', '') for f2 in os.listdir(folder) 
                      if f2.endswith('.md') and f2 != os.path.basename(filepath)]
            if len(others) >= 2:
                links_str = '\n'.join([f'  - "[[{o}]]"' for o in others[:2]])
                content = content.replace(
                    f'---\n{fm}\n---',
                    f'---\n{fm}\nlinks:\n{links_str}\n---'
                )
                fixes += 1
    
    # Fix body wikilinks
    body_match = re.search(r'^---\n.*?\n---\n(.*)', content, re.DOTALL)
    if body_match:
        body = body_match.group(1)
        body_links = re.findall(r'\[\[([^\]]+)\]\]', body)
        for link in body_links:
            actual = resolve(link, by_exact, by_title, by_word)
            if actual and actual != link:
                content = content.replace(f'[[{link}]]', f'[[{actual}]]')
                fixes += 1
    
    if fixes > 0 and content != original:
        with open(filepath, 'w') as f:
            f.write(content)
    
    return fixes

def main():
    print("FIXING ALL LINKS IN VAULT")
    print("=" * 60)
    
    os.chdir(VAULT)
    
    by_exact, by_title, by_word = build_maps()
    print(f"Built maps: {len(by_exact)} exact, {len(by_title)} title, {len(by_word)} word")
    
    total_fixes = 0
    files_fixed = 0
    
    folders = ['03 - Agents', '04 - Plugins', '05 - Architecture', 
               '06 - Use Cases', '09 - Trend Radar/Heating Up', 
               '09 - Trend Radar/Stable', '09 - Trend Radar/Emerging']
    
    for folder in folders:
        fp = os.path.join(VAULT, folder)
        if not os.path.exists(fp):
            continue
        for f in sorted(os.listdir(fp)):
            if f.endswith('.md'):
                filepath = os.path.join(fp, f)
                fixes = fix_file(filepath, by_exact, by_title, by_word)
                if fixes > 0:
                    print(f"  {folder}/{f}: {fixes} fixes")
                    total_fixes += fixes
                    files_fixed += 1
    
    print(f"\nTotal: {total_fixes} fixes in {files_fixed} files")

if __name__ == '__main__':
    main()
