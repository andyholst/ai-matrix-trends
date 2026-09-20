#!/usr/bin/env python3
"""
fix-master-index-links.py - Fix frontmatter links in Master Index files.
Ensures all files referenced in tables are listed in the links: field.
Run after update-agent-master-index.py and update-plugin-master-index.py.
"""

import os
import re

VAULT = os.path.expanduser("~/repository/git/ai-matrix-trends")

INDEX_FILES = [
    os.path.join(VAULT, "03 - Agents", "00 - Agent Master Index.md"),
    os.path.join(VAULT, "04 - Plugins", "00 - Plugin Master Index.md"),
]

def extract_linked_files(content):
    """Extract all markdown links [text](path.md) from content"""
    # Match markdown links: [text](./path.md) or [text](path.md)
    links = re.findall(r'\]\(([^)]+\.md)\)', content)
    # Extract just the filename
    files = []
    for link in links:
        # Remove ./ prefix and %20 encoding
        clean = link.replace('./', '').replace('%20', ' ')
        # Get just the filename
        fname = os.path.basename(clean)
        if fname and fname not in files:
            files.append(fname)
    return files

def fix_frontmatter_links(filepath):
    """Fix the links: field in frontmatter to match all referenced files"""
    with open(filepath) as f:
        content = f.read()
    
    # Extract all markdown links from the body
    linked_files = extract_linked_files(content)
    
    if not linked_files:
        print(f"  No links found in {os.path.basename(filepath)}")
        return
    
    # Parse frontmatter
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        print(f"  No frontmatter in {os.path.basename(filepath)}")
        return
    
    fm = fm_match.group(1)
    
    # Extract existing links
    links_match = re.search(r'^links:\n((?:\s*-\s*"\[\[.*?\]\]"\n?)+)', fm, re.MULTILINE)
    existing_links = []
    if links_match:
        existing_links = re.findall(r'"\[\[(.*?)\]\]"', links_match.group(1))
    
    # Convert linked files to wikilink format
    new_links = []
    for fname in linked_files:
        # Remove .md extension for wikilink
        link_text = fname.replace('.md', '')
        if link_text not in existing_links and link_text not in new_links:
            new_links.append(link_text)
    
    if not new_links:
        print(f"  {os.path.basename(filepath)}: links already complete ({len(existing_links)} links)")
        return
    
    # Build new links section
    all_links = existing_links + new_links
    links_lines = '\n'.join([f'  - "[[{l}]]"' for l in all_links])
    new_links_section = f'links:\n{links_lines}'
    
    # Replace in frontmatter
    if links_match:
        new_fm = fm.replace(links_match.group(0), new_links_section)
    else:
        new_fm = fm + '\nlinks:\n' + links_lines
    
    # Replace in content
    new_content = content.replace(fm, new_fm)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    print(f"  {os.path.basename(filepath)}: added {len(new_links)} links (total: {len(all_links)})")

def main():
    print("Fixing Master Index frontmatter links...")
    for filepath in INDEX_FILES:
        if os.path.exists(filepath):
            fix_frontmatter_links(filepath)
        else:
            print(f"  {filepath} not found")

if __name__ == '__main__':
    os.chdir(VAULT)
    main()
