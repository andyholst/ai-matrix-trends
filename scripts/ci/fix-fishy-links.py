#!/usr/bin/env python3
"""
fix-fishy-links.py - Move MOC references from frontmatter to body.
"""

import os
import re

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")

SKIP_FOLDERS = ['.obsidian', 'scripts/ci', '00 - Inbox']

def fix_file(filepath):
    """Move MOC links from frontmatter to body"""
    with open(filepath) as f:
        content = f.read()
    
    # Parse frontmatter
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return False
    
    fm = fm_match.group(1)
    
    # Find links section
    links_match = re.search(r'^links:\n((?:\s*-\s*"\[\[.*?\]\]"\n?)+)', fm, re.MULTILINE)
    if not links_match:
        return False
    
    links_text = links_match.group(1)
    links = re.findall(r'"\[\[(.*?)\]\]"', links_text)
    
    # Separate MOC links from note links
    moc_links = []
    note_links = []
    
    for link in links:
        if 'MOC-' in link or 'MOC:' in link:
            moc_links.append(link)
        else:
            note_links.append(link)
    
    if not moc_links:
        return False
    
    # Rebuild frontmatter without MOC links
    if note_links:
        new_links_text = '\n'.join([f'  - "[[{l}]]"' for l in note_links])
        new_fm = fm.replace(links_text, new_links_text)
    else:
        # Remove empty links section
        new_fm = fm.replace(links_match.group(0), '')
    
    # Add MOC links to body (after ## Related or at end)
    body = content[fm_match.end():]
    
    # Find ## Related section
    related_match = re.search(r'## Related\n', body)
    if related_match:
        # Add after ## Related
        insert_pos = related_match.end()
        moc_text = '\n'.join([f'- [[{link}]]' for link in moc_links]) + '\n'
        new_body = body[:insert_pos] + moc_text + body[insert_pos:]
    else:
        # Add ## Related section at end
        moc_text = '\n## Related\n' + '\n'.join([f'- [[{link}]]' for link in moc_links]) + '\n'
        new_body = body.rstrip() + '\n' + moc_text
    
    # Rebuild file
    new_content = f'---\n{new_fm}\n---{new_body}'
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    return True

def main():
    print("Fixing fishy links (moving MOC refs from frontmatter to body)...")
    
    fixed = 0
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        if any(skip in root for skip in SKIP_FOLDERS):
            continue
        
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                if fix_file(filepath):
                    fixed += 1
                    rel_path = os.path.relpath(filepath, VAULT_DIR)
                    print(f"  Fixed: {rel_path}")
    
    print(f"\nFixed {fixed} files")

if __name__ == '__main__':
    main()