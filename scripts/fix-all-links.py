#!/usr/bin/env python3
"""
fix-all-links.py - Comprehensive link fixing script.
Goes through all vault files and:
1. Resolves short-name wikilinks to full filenames
2. Deduplicates frontmatter links
3. Creates placeholder files for missing targets
4. Fixes body wikilinks in ## Related sections
5. Is idempotent (safe to run multiple times)
"""

import os
import re
from datetime import datetime
from collections import defaultdict

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")

# Short name -> filename mappings
SHORT_NAME_MAP = {
    'claude code': '202609202000 - Claude Code',
    'claude-code': '202609202000 - Claude Code',
    'codex': '202609202000 - Codex',
    'openai codex': '202609202000 - Codex',
    'openai-codex': '202609202000 - Codex',
    'opencode': '202609200758 - OpenCode',
    'hermes': '202609200759 - Hermes Agent',
    'hermes agent': '202609200759 - Hermes Agent',
    'hermes-agent': '202609200759 - Hermes Agent',
    'cursor': '202609202000 - Cursor',
    'cline': '202609202000 - Cline',
    'aider': '202609202000 - Aider',
    'windsurf': '202609200800 - Windsurf',
    'github copilot': '202609202001 - GitHub Copilot Agent',
    'github-copilot': '202609202001 - GitHub Copilot Agent',
    'gemini cli': '202609202002 - Gemini CLI',
    'gemini-cli': '202609202002 - Gemini CLI',
    'jetbrains junie': '202609202005 - JetBrains Junie',
    'kilo code': '202609202003 - Kilo Code',
    'kilo-code': '202609202003 - Kilo Code',
    'roocode': '202609202004 - RooCode',
    'vscode': '202609202000 - Cursor',
    'browser use': '202609202000 - Browser Use MCP',
    'browser-use': '202609202000 - Browser Use MCP',
    'firecrawl': '202609202000 - Firecrawl MCP Server',
    'context7': '202609200803 - Context7 MCP',
    'fal': '202609200804 - FAL MCP Server',
    'playwright': '202609202010 - Playwright MCP',
    'chrome devtools': '202609202011 - Chrome DevTools MCP',
    'chrome-devtools': '202609202011 - Chrome DevTools MCP',
    'auto permission': '202609200807 - Claude Code Auto Permission',
    'auto-permission': '202609200807 - Claude Code Auto Permission',
    'jev': '202609202000 - Jev Agent Router',
    'jev agent': '202609202000 - Jev Agent Router',
    'jev-agent': '202609202000 - Jev Agent Router',
    'devin': '202609202000 - Devin',
    'pi': '202609202004 - Pi',
    'vellum': '202609200910 - Vellum',
    'amazon q': '202609200911 - Amazon Q Developer',
    'nimbalyst': '202609200912 - Nimbalyst',
    'replit': '202609200913 - Replit Agent',
    'jetbrains air': '202609200914 - JetBrains Air',
    'amp': '2026092010 - Amp',
    'qwen code': '2026092011 - Qwen Code',
    'factory droids': '2026092012 - Factory Droids',
    'zencoder': '2026092013 - Zencoder',
    'magicrew': '2026092014 - MagiCrew',
    'claw code': '2026092010 - Claw Code',
    'swe-2': '202609202015 - SWE-2',
    'swe2': '202609202015 - SWE-2',
    'devin desktop': '202609202025 - Devin Desktop',
    'pareto': '202609202045 - Pareto',
    'muse code': '202609202055 - Muse Code',
    'google antigravity': '202609202001 - Google Antigravity',
    'augment': '202609202002 - Augment',
    'aws kiro': '202609202003 - AWS Kiro',
}

# MOC mappings
MOC_MAP = {
    'moc-trending-agents': '07 - Structure/MOC-Trending-Agents.md',
    'moc-plugin-ecosystem': '07 - Structure/MOC-Plugin-Ecosystem.md',
    'moc-architecture-patterns': '07 - Structure/MOC-Architecture-Patterns.md',
    'moc-trend-radar': '07 - Structure/MOC-Trend-Radar.md',
}

def build_file_map():
    """Build comprehensive file lookup map"""
    file_map = {}
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                fname = f.replace('.md', '')
                rel_path = os.path.relpath(os.path.join(root, f), VAULT_DIR)
                
                # Map full filename
                file_map[fname.lower()] = rel_path
                
                # Map by title only
                if ' - ' in fname:
                    title = fname.split(' - ', 1)[1]
                    file_map[title.lower()] = rel_path
    
    return file_map

def resolve_link(link_text, file_map):
    """Resolve a wikilink to actual filename"""
    link_lower = link_text.lower().strip()
    
    # Check MOCs first
    if link_lower in MOC_MAP:
        return MOC_MAP[link_lower]
    
    # Check short name map
    if link_lower in SHORT_NAME_MAP:
        target = SHORT_NAME_MAP[link_lower]
        if target.lower() in file_map:
            return file_map[target.lower()]
    
    # Check if already a full filename
    if link_lower in file_map:
        return file_map[link_lower]
    
    # Check if it's a title that exists
    if link_lower in file_map:
        return file_map[link_lower]
    
    return None

def create_placeholder_file(title, folder):
    """Create a placeholder note for missing targets"""
    # Determine folder based on title keywords
    if 'mcp' in title.lower() or 'plugin' in title.lower():
        target_folder = os.path.join(VAULT_DIR, "04 - Plugins")
    elif 'agent' in title.lower() or 'cli' in title.lower():
        target_folder = os.path.join(VAULT_DIR, "03 - Agents")
    elif 'pattern' in title.lower() or 'architecture' in title.lower():
        target_folder = os.path.join(VAULT_DIR, "05 - Architecture")
    else:
        target_folder = os.path.join(VAULT_DIR, "00 - Inbox")
    
    os.makedirs(target_folder, exist_ok=True)
    
    # Generate timestamp
    ts = datetime.now().strftime('%Y%m%d%H%M')
    filename = f"{ts} - {title}.md"
    filepath = os.path.join(target_folder, filename)
    
    if os.path.exists(filepath):
        return filepath
    
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
[Auto-created placeholder for {title}]

## Sources
-
"""
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"  Created placeholder: {filepath}")
    return filepath

def fix_frontmatter_links(filepath, file_map):
    """Fix and deduplicate frontmatter links"""
    with open(filepath) as f:
        content = f.read()
    
    # Parse frontmatter
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return False
    
    fm = fm_match.group(1)
    
    # Find links field
    links_match = re.search(r'^links:\n((?:\s*-\s*"\[\[.*?\]\]"\n?)+)', fm, re.MULTILINE)
    if not links_match:
        return False
    
    links_text = links_match.group(1)
    links = re.findall(r'"\[\[(.*?)\]\]"', links_text)
    
    if not links:
        return False
    
    # Deduplicate and resolve links
    seen = set()
    fixed_links = []
    changed = False
    
    for link in links:
        # Resolve short names
        resolved = resolve_link(link, file_map)
        
        if resolved:
            # Get the filename from the resolved path
            fname = os.path.basename(resolved).replace('.md', '')
            if fname.lower() not in seen:
                seen.add(fname.lower())
                fixed_links.append(fname)
                if fname != link:
                    changed = True
        else:
            # Keep original if can't resolve
            if link.lower() not in seen:
                seen.add(link.lower())
                fixed_links.append(link)
    
    if not changed and len(fixed_links) == len(links):
        return False
    
    # Rebuild links section — markdown links, file-relative to the containing file
    from urllib.parse import quote
    from_dir = os.path.dirname(filepath)
    fixed_entries = []
    for l in fixed_links:
        # l is either a resolved full filename or an unresolved link text
        resolved = resolve_link(l, file_map)
        if resolved:
            target = resolved if resolved.endswith('.md') else resolved + '.md'
            rel = os.path.relpath(os.path.join(VAULT_DIR, target), from_dir)
            title = l.split(' - ', 1)[1] if ' - ' in l else l
            fixed_entries.append(f'  - "[{title}](./{quote(rel, safe="/._-")})"')
        else:
            # Unresolvable: keep as wikilink marker for the fixer to report
            fixed_entries.append(f'  - "[[{l}]]"')
    new_links_text = '\n'.join(fixed_entries)
    new_fm = fm.replace(links_text, new_links_text)
    new_content = content.replace(fm, new_fm)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    return True

def fix_body_wikilinks(filepath, file_map):
    """Fix wikilinks in body text (## Related sections)"""
    with open(filepath) as f:
        content = f.read()
    
    original = content
    
    # Find all wikilinks in body
    links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    
    for link in links:
        # Skip if already resolved (has timestamp)
        if re.match(r'\d{12,14} - ', link):
            continue
        
        # Skip MOCs
        if 'moc' in link.lower():
            continue
        
        # Try to resolve
        resolved = resolve_link(link, file_map)
        
        if resolved:
            # Get filename from path
            fname = os.path.basename(resolved).replace('.md', '')
            if fname != link:
                content = content.replace(f'[[{link}]]', f'[[{fname}]]')
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    
    return False

def main():
    print("FIXING ALL LINKS IN VAULT")
    print("=" * 60)
    
    file_map = build_file_map()
    print(f"Built file map: {len(file_map)} entries")
    
    fixed_frontmatter = 0
    fixed_body = 0
    errors = 0
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                
                try:
                    if fix_frontmatter_links(filepath, file_map):
                        fixed_frontmatter += 1
                    
                    if fix_body_wikilinks(filepath, file_map):
                        fixed_body += 1
                except Exception as e:
                    print(f"  ERROR: {filepath}: {e}")
                    errors += 1
    
    print(f"\nFixed frontmatter links in: {fixed_frontmatter} files")
    print(f"Fixed body wikilinks in: {fixed_body} files")
    print(f"Errors: {errors}")

if __name__ == '__main__':
    os.chdir(VAULT_DIR)
    main()