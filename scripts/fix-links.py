#!/usr/bin/env python3
"""
AI Matrix Trends - Vault Link Fixer
This script fixes all broken links in the vault deterministically.
Run by the cron job after research streams complete.
"""

import os
import re
import subprocess

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")

def build_file_map():
    """Build title -> actual filename map"""
    file_map = {}
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                fname = f.replace('.md', '')
                # Exact filename
                file_map[fname.lower()] = fname
                # Title only (after timestamp)
                if ' - ' in fname:
                    title = fname.split(' - ', 1)[1]
                    file_map[title.lower().replace(' ', '-').replace("'", "")] = fname
    
    # MOCs
    file_map['moc-trending-agents'] = 'MOC-Trending-Agents'
    file_map['moc-plugin-ecosystem'] = 'MOC-Plugin-Ecosystem'
    file_map['moc-architecture-patterns'] = 'MOC-Architecture-Patterns'
    file_map['moc-trend-radar'] = 'MOC-Trend-Radar'
    
    return file_map

def resolve_link(link_text, file_map):
    """Resolve a wikilink short name to actual filename"""
    if ' - ' in link_text:
        title = link_text.split(' - ', 1)[1]
    else:
        title = link_text
    
    title_key = title.lower().replace(' ', '-').replace("'", "")
    
    if title_key in file_map:
        return file_map[title_key]
    
    # Partial match
    for key, val in file_map.items():
        if title_key in key or key in title_key:
            return val
    
    return None

def fix_frontmatter_links(filepath, content, file_map):
    """Fix links in frontmatter"""
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return content, 0
    
    fm = fm_match.group(1)
    fixes = 0
    
    # Check for existing links field
    links_match = re.search(r'^links:\n((?:\s*-\s*"\[\[.*?\]\]"\n?)+)', fm, re.MULTILINE)
    
    if links_match:
        # Fix existing links
        links_text = links_match.group(1)
        links = re.findall(r'"\[\[(.*?)\]\]"', links_text)
        new_links = []
        
        for link in links:
            resolved = resolve_link(link, file_map)
            if resolved and resolved != link:
                new_links.append(f'  - "[[{resolved}]]"')
                fixes += 1
            else:
                new_links.append(f'  - "[[{link}]]"')
        
        if fixes > 0:
            old_section = links_match.group(0)
            new_section = 'links:\n' + '\n'.join(new_links)
            content = content.replace(fm, fm.replace(old_section, new_section))
    else:
        # No links field - add one
        # Find 2 other notes in same folder
        folder = os.path.dirname(filepath)
        other_notes = []
        for f2 in os.listdir(folder):
            if f2.endswith('.md') and f2 != os.path.basename(filepath):
                other_notes.append(f2.replace('.md', ''))
        
        if len(other_notes) >= 2:
            links_str = '\n'.join([f'  - "[[{n}]]"' for n in other_notes[:2]])
            # Add links field before end of frontmatter
            content = content.replace(
                f'---\n{fm}\n---',
                f'---\n{fm}\nlinks:\n{links_str}\n---'
            )
            fixes += 1
    
    return content, fixes

def fix_body_links(filepath, content, file_map):
    """Fix wikilinks in body text"""
    body_match = re.search(r'^---\n.*?\n---\n(.*)', content, re.DOTALL)
    if not body_match:
        return content, 0
    
    body = body_match.group(1)
    links = re.findall(r'\[\[([^\]]+)\]\]', body)
    fixes = 0
    
    for link in links:
        resolved = resolve_link(link, file_map)
        if resolved and resolved != link:
            content = content.replace(f'[[{link}]]', f'[[{resolved}]]')
            fixes += 1
    
    return content, fixes

def fix_readme_links(content):
    """Fix README Markdown links (ensure proper format)"""
    # README links are already in [text](./path.md) format - just verify they exist
    links = re.findall(r'\]\(([^)]+)\)', content)
    fixes = 0
    
    for link in links:
        if link.startswith('./'):
            path = link[2:].replace('%20', ' ')
            if not os.path.exists(os.path.join(VAULT_DIR, path)):
                # Try to find the file
                filename = os.path.basename(path)
                for root, dirs, files in os.walk(VAULT_DIR):
                    if '/.git' in root:
                        continue
                    for f in files:
                        if f == filename:
                            # Found it - update path
                            new_link = os.path.relpath(os.path.join(root, f), VAULT_DIR)
                            new_link = './' + new_link.replace(' ', '%20')
                            content = content.replace(link, new_link)
                            fixes += 1
                            break
    
    return content, fixes

def commit_and_push(message="Daily scan: fix all links"):
    """Commit and push all changes"""
    subprocess.run(['git', 'add', '-A'], cwd=VAULT_DIR, check=True)
    subprocess.run(['git', 'commit', '-m', message], cwd=VAULT_DIR, check=True)
    subprocess.run(['git', 'push'], cwd=VAULT_DIR, check=True)

def main():
    print("VAULT LINK FIXER")
    print("=" * 60)
    
    os.chdir(VAULT_DIR)
    
    file_map = build_file_map()
    total_fixes = 0
    files_fixed = 0
    
    for folder in ['03 - Agents', '04 - Plugins', '05 - Architecture', 
                   '06 - Use Cases', '09 - Trend Radar/Heating Up', 
                   '09 - Trend Radar/Stable', '09 - Trend Radar/Emerging']:
        folder_path = os.path.join(VAULT_DIR, folder)
        if not os.path.exists(folder_path):
            continue
        
        for f in sorted(os.listdir(folder_path)):
            if f.endswith('.md'):
                filepath = os.path.join(folder_path, f)
                with open(filepath) as fh:
                    content = fh.read()
                
                # Fix frontmatter links
                content, fm_fixes = fix_frontmatter_links(filepath, content, file_map)
                
                # Fix body links
                content, body_fixes = fix_body_links(filepath, content, file_map)
                
                fixes = fm_fixes + body_fixes
                if fixes > 0:
                    with open(filepath, 'w') as fh:
                        fh.write(content)
                    total_fixes += fixes
                    files_fixed += 1
                    print(f"  Fixed {fixes} links in {folder}/{f}")
    
    # Fix README
    readme_path = os.path.join(VAULT_DIR, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path) as fh:
            content = fh.read()
        content, readme_fixes = fix_readme_links(content)
        if readme_fixes > 0:
            with open(readme_path, 'w') as fh:
                fh.write(content)
            total_fixes += readme_fixes
            print(f"  Fixed {readme_fixes} links in README.md")
    
    print(f"\nTotal: {total_fixes} fixes across {files_fixed} files")
    
    # Commit
    commit_and_push()
    print("Committed and pushed")

if __name__ == '__main__':
    main()
