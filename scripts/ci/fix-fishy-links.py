#!/usr/bin/env python3
"""
fix-fishy-links.py - Convert wikilinks to markdown links and create missing targets.
Converts [[...]] format in frontmatter to [title](path) format.
"""

import os
import re
from datetime import datetime

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")

SKIP_FOLDERS = ['.obsidian', 'scripts/ci', '00 - Inbox']

def build_file_map():
    """Build map of all existing files: lowered_filename -> relative_path"""
    file_map = {}
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                fname = f.replace('.md', '')
                rel_path = os.path.relpath(os.path.join(root, f), VAULT_DIR)
                file_map[fname.lower()] = rel_path
                if ' - ' in fname:
                    title = fname.split(' - ', 1)[1]
                    file_map[title.lower()] = rel_path
    return file_map

def create_missing_target(link_text, file_map):
    """Create a placeholder file for a missing link target"""
    link_lower = link_text.lower()
    
    # Don't create MOC files - those should be fixed differently
    if 'moc-' in link_lower or 'moc:' in link_lower:
        return None
    
    # Determine target folder based on link content
    if any(kw in link_lower for kw in ['plugin', 'mcp server', 'mcp']):
        target_folder = '04 - Plugins'
    elif any(kw in link_lower for kw in ['agent', 'cli', 'copilot']):
        target_folder = '03 - Agents'
    elif any(kw in link_lower for kw in ['pattern', 'architecture', 'orchestration']):
        target_folder = '05 - Architecture'
    elif any(kw in link_lower for kw in ['use case', 'workflow', 'hooks']):
        target_folder = '06 - Use Cases'
    else:
        target_folder = '00 - Inbox'
    
    # Generate filename from link text
    # Extract title from "timestamp - title" format or use whole link
    if ' - ' in link_text:
        title = link_text.split(' - ', 1)[1]
    else:
        title = link_text
    
    # Clean title for filename
    safe_title = re.sub(r'[^\w\s-]', '', title).strip()
    ts = datetime.now().strftime('%Y%m%d%H%M')
    filename = f"{ts} - {safe_title}.md"
    filepath = os.path.join(VAULT_DIR, target_folder, filename)
    
    # Create placeholder file
    date_str = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+02:00')
    content = f"""---
id: {ts}
created: {date_str}
tags:
  - placeholder
links:
---

# {title}

## Overview
[Auto-created placeholder for {link_text}]

## Sources
-
"""
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)
    
    # Add to file_map
    new_fname = filename.replace('.md', '')
    file_map[new_fname.lower()] = os.path.relpath(filepath, VAULT_DIR)
    if ' - ' in new_fname:
        t = new_fname.split(' - ', 1)[1]
        file_map[t.lower()] = file_map[new_fname.lower()]
    
    return filepath

def fix_file(filepath, file_map):
    """Convert wikilinks to markdown links in frontmatter"""
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
    
    if not links:
        return False
    
    # Convert wikilinks to markdown links
    new_links = []
    changed = False
    
    for link in links:
        link_lower = link.lower().strip()
        
        # Check if target exists
        if link_lower in file_map:
            # Convert to markdown link
            target_path = file_map[link_lower]
            # Use relative path with %20 for spaces (markdown standard)
            encoded_path = target_path.replace(' ', '%20')
            # Use title part for display
            title = link.split(' - ', 1)[1] if ' - ' in link else link
            new_links.append(f'  - "[{title}](./{encoded_path})"')
            changed = True
        else:
            # Create missing target
            new_target = create_missing_target(link, file_map)
            if new_target:
                # Convert to markdown link
                target_path = file_map[link_lower] if link_lower in file_map else os.path.relpath(new_target, VAULT_DIR)
                encoded_path = target_path.replace(' ', '%20')
                title = link.split(' - ', 1)[1] if ' - ' in link else link
                new_links.append(f'  - "[{title}](./{encoded_path})"')
                changed = True
            else:
                # Keep as-is (MOC link, etc.)
                new_links.append(f'  - "[[{link}]]"')
    
    if not changed:
        return False
    
    # Rebuild frontmatter
    new_links_text = '\n'.join(new_links)
    new_fm = fm.replace(links_text, new_links_text)
    new_content = content.replace(fm, new_fm)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    return True

def main():
    print("Fixing fishy links (converting wikilinks to markdown links)...")
    
    file_map = build_file_map()
    fixed = 0
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        if any(skip in root for skip in SKIP_FOLDERS):
            continue
        
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                if fix_file(filepath, file_map):
                    fixed += 1
                    rel_path = os.path.relpath(filepath, VAULT_DIR)
                    print(f"  Fixed: {rel_path}")
    
    print(f"\nFixed {fixed} files")

if __name__ == '__main__':
    main()