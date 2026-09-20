#!/usr/bin/env python3
"""
fix_meta_tags.py - Fix all frontmatter meta tags (links) in the vault.
Replaces broken links with actual existing filenames.
"""

import os
import re
import json

VAULT = os.path.expanduser("~/repository/git/ai-matrix-trends")

def build_map():
    """Build complete lookup maps"""
    by_title = {}      # title -> filename
    by_exact = {}      # exact filename -> filename
    by_partial = {}    # partial title -> filename
    
    for root, dirs, files in os.walk(VAULT):
        if '/.git' in root:
            continue
        for f in files:
            if not f.endswith('.md'):
                continue
            full = os.path.join(root, f)
            fname = f.replace('.md', '')
            
            by_exact[fname.lower()] = fname
            
            if ' - ' in fname:
                ts, title = fname.split(' - ', 1)
                by_title[title.lower()] = fname
                by_title[title.lower().replace(' ', '-')] = fname
                # Partial words
                words = title.lower().split()
                for w in words:
                    if len(w) > 3:
                        by_partial[w] = fname
    
    # MOCs
    by_title['moc-trending-agents'] = 'MOC-Trending-Agents'
    by_title['moc-plugin-ecosystem'] = 'MOC-Plugin-Ecosystem'
    by_title['moc-architecture-patterns'] = 'MOC-Architecture-Patterns'
    by_title['moc-trend-radar'] = 'MOC-Trend-Radar'
    
    return by_exact, by_title, by_partial

def resolve(link, by_exact, by_title, by_partial):
    """Resolve a wikilink to actual filename"""
    link_lower = link.lower().replace(' ', '-')
    
    # Exact match
    if link_lower in by_exact:
        return by_exact[link_lower]
    
    # Title match (with or without timestamp)
    if link_lower in by_title:
        return by_title[link_lower]
    
    # Without timestamp prefix
    if ' - ' in link:
        title = link.split(' - ', 1)[1].lower().replace(' ', '-')
        if title in by_title:
            return by_title[title]
        if title in by_exact:
            return by_exact[title]
    
    # Partial match
    for key, val in by_title.items():
        if link_lower in key or key in link_lower:
            return val
    
    for key, val in by_partial.items():
        if link_lower in key or key in link_lower:
            return val
    
    return None

def fix_file(filepath, by_exact, by_title, by_partial):
    """Fix all links in a single file"""
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
                actual = resolve(link, by_exact, by_title, by_partial)
                if actual and actual != link:
                    new_links.append(f'  - "[[{actual}]]"')
                    fixes += 1
                elif actual:
                    new_links.append(f'  - "[[{link}]]"')
                else:
                    # Broken link - find any valid target
                    # Try to find by searching all files
                    found = False
                    for root, dirs, files in os.walk(VAULT):
                        if '/.git' in root:
                            continue
                        for f2 in files:
                            if f2.endswith('.md') and link.lower() in f2.lower():
                                actual = f2.replace('.md', '')
                                new_links.append(f'  - "[[{actual}]]"')
                                fixes += 1
                                found = True
                                break
                        if found:
                            break
                    if not found:
                        new_links.append(f'  - "[[{link}]]"')
            
            # Replace
            old_section = links_match.group(0)
            new_section = 'links:\n' + '\n'.join(new_links)
            content = content.replace(f'---\n{fm}\n---', f'---\n{fm.replace(old_section, new_section)}\n---')
        else:
            # No links field - add one with 2 valid links from same folder
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
            actual = resolve(link, by_exact, by_title, by_partial)
            if actual and actual != link:
                content = content.replace(f'[[{link}]]', f'[[{actual}]]')
                fixes += 1
    
    if fixes > 0:
        with open(filepath, 'w') as f:
            f.write(content)
    
    return fixes

def main():
    print("FIXING ALL META TAGS (FRONTMATTER LINKS)")
    print("=" * 60)
    
    by_exact, by_title, by_partial = build_map()
    print(f"Built map: {len(by_exact)} exact, {len(by_title)} title, {len(by_partial)} partial")
    
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
                fixes = fix_file(filepath, by_exact, by_title, by_partial)
                if fixes > 0:
                    print(f"  {folder}/{f}: {fixes} fixes")
                    total_fixes += fixes
                    files_fixed += 1
    
    print(f"\nTotal: {total_fixes} fixes in {files_fixed} files")

if __name__ == '__main__':
    main()
