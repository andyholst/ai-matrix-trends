#!/usr/bin/env python3
"""
fix-master-index-links.py - Fix frontmatter links in Master Index files.
Ensures all files in the folder are listed in the links: field.
This script is IDEMPOTENT - running it multiple times produces the same result.
"""

import os
import re

VAULT = os.path.expanduser("~/repository/git/ai-matrix-trends")

INDEX_FILES = [
    (os.path.join(VAULT, "03 - Agents", "00 - Agent Master Index.md"), "03 - Agents"),
    (os.path.join(VAULT, "04 - Plugins", "00 - Plugin Master Index.md"), "04 - Plugins"),
]

def get_files_in_folder(folder_path):
    """Get all filenames (without .md) in a folder, excluding index files"""
    files = set()
    if not os.path.exists(folder_path):
        return files
    for f in os.listdir(folder_path):
        if f.endswith('.md') and not f.startswith('00 -'):
            files.add(f.replace('.md', ''))
    return files

def fix_frontmatter_links(filepath, folder_filter):
    """Fix the links: field in frontmatter to match all files in the folder"""
    with open(filepath) as f:
        content = f.read()
    
    # Parse frontmatter
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        print(f"  No frontmatter in {os.path.basename(filepath)}")
        return
    
    fm = fm_match.group(1)
    
    # Extract existing links from frontmatter (wikilink or markdown format)
    links_match = re.search(r'^links:\n((?:\s*-\s*"(?:\[\[.*?\]\]|\[.*?\]\(.*?\))"\n?)+)', fm, re.MULTILINE)
    existing_links = set()
    if links_match:
        # Wikilinks
        existing_links |= set(re.findall(r'"\[\[(.*?)\]\]"', links_match.group(1)))
        # Markdown links: extract target filename from [title](path)
        for title, path in re.findall(r'"\[([^\]]+)\]\(([^)]+)\)"', links_match.group(1)):
            import os.path as _osp
            from urllib.parse import unquote as _uq
            fname = _osp.basename(_uq(path.split('#')[0]))
            if fname.endswith('.md'):
                fname = fname[:-3]
            existing_links.add(fname)
    
    # Get all files in the target folder (these are the links we need)
    folder_path = os.path.join(VAULT, folder_filter)
    needed_links = get_files_in_folder(folder_path)
    
    # Find missing links
    missing_links = needed_links - existing_links
    
    if not missing_links:
        print(f"  {os.path.basename(filepath)}: links complete ({len(existing_links)} links)")
        return
    
    # Build new links section with ALL links (existing + new), sorted.
    # Markdown format, file-relative to the index file's own folder.
    all_links = sorted(existing_links | missing_links)
    from urllib.parse import quote
    from_dir = os.path.dirname(filepath)
    links_lines = '\n'.join([
        f'  - "[{l.split(" - ", 1)[1] if " - " in l else l}](./{quote(l, safe="/._-")}.md)"'
        for l in all_links
    ])
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
    
    print(f"  {os.path.basename(filepath)}: added {len(missing_links)} links (total: {len(all_links)})")

def main():
    print("Fixing Master Index frontmatter links...")
    for filepath, folder_filter in INDEX_FILES:
        if os.path.exists(filepath):
            fix_frontmatter_links(filepath, folder_filter)
        else:
            print(f"  {filepath} not found")

if __name__ == '__main__':
    os.chdir(VAULT)
    main()