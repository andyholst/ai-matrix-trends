#!/usr/bin/env python3
"""
fix-fishy-links.py - Convert all wikilinks to markdown links.
Converts [[title]] and [[title|display]] to [display](./path).
Creates missing target files when needed.
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
    # Add special mappings for common references
    file_map['readme.md'] = 'README.md'
    file_map['readme'] = 'README.md'
    
    return file_map

def create_missing_target(link_text, file_map):
    """Create a placeholder file for a missing link target"""
    link_lower = link_text.lower()
    
    # Determine target folder based on link content
    if any(kw in link_lower for kw in ['plugin', 'mcp']):
        target_folder = '04 - Plugins'
    elif any(kw in link_lower for kw in ['agent', 'cli', 'copilot', 'code']):
        target_folder = '03 - Agents'
    elif any(kw in link_lower for kw in ['pattern', 'architecture', 'orchestration']):
        target_folder = '05 - Architecture'
    elif any(kw in link_lower for kw in ['use case', 'workflow', 'hooks', 'ci-cd']):
        target_folder = '06 - Use Cases'
    elif 'readme' in link_lower:
        return None  # Don't create README
    else:
        target_folder = '00 - Inbox'
    
    # Generate filename from link text
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

def convert_wikilink_to_markdown(wikilink, file_map):
    """Convert a wikilink to markdown link format"""
    # Handle [[title|display]] format
    if '|' in wikilink:
        target, display = wikilink.split('|', 1)
    else:
        target = wikilink
        display = wikilink
    
    target_lower = target.lower().strip()
    display = display.strip()
    
    # Check if target exists
    if target_lower in file_map:
        target_path = file_map[target_lower]
        encoded_path = target_path.replace(' ', '%20')
        return f'[{display}](./{encoded_path})'
    else:
        # Create missing target
        new_target = create_missing_target(target, file_map)
        if new_target:
            # Rebuild file_map entry
            new_fname = os.path.basename(new_target).replace('.md', '')
            file_map[new_fname.lower()] = os.path.relpath(new_target, VAULT_DIR)
            if ' - ' in new_fname:
                t = new_fname.split(' - ', 1)[1]
                file_map[t.lower()] = file_map[new_fname.lower()]
            
            target_path = file_map[target_lower] if target_lower in file_map else file_map[new_fname.lower()]
            encoded_path = target_path.replace(' ', '%20')
            return f'[{display}](./{encoded_path})'
        else:
            # Return original if can't create (README, etc.)
            return f'[[{wikilink}]]'

def fix_file(filepath, file_map):
    """Convert all wikilinks in a file to markdown links"""
    with open(filepath) as f:
        content = f.read()
    
    original = content
    
    # Find all wikilinks
    wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
    
    if not wikilinks:
        return False
    
    for wikilink in wikilinks:
        markdown_link = convert_wikilink_to_markdown(wikilink, file_map)
        if markdown_link != f'[[{wikilink}]]':
            content = content.replace(f'[[{wikilink}]]', markdown_link, 1)
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    
    return False

def main():
    print("Converting all wikilinks to markdown links...")
    
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