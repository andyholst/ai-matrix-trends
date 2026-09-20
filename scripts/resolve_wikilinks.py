#!/usr/bin/env python3
"""
resolve_wikilinks.py - Resolve ALL short-name wikilinks to actual filenames.
Uses EXACT matching only to prevent creating duplicates.
"""

import os
import re

VAULT = os.path.expanduser("~/repository/git/ai-matrix-trends")
EXCLUDE_FILES = ['AGENTS.md', 'README.md', 'LICENSE', 'daily-scan-prompt.md']

def build_map():
    """Build lookup map with exact matches only"""
    by_title = {}
    
    for root, dirs, files in os.walk(VAULT):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                fname = f.replace('.md', '')
                if ' - ' in fname:
                    title = fname.split(' - ', 1)[1]
                    # Only exact title matches (case-insensitive)
                    by_title[title.lower()] = fname
                    # With spaces replaced by hyphens
                    by_title[title.lower().replace(' ', '-')] = fname
    
    # Known short name mappings (exact only)
    by_title.update({
        'claude code': '202609202000 - Claude Code',
        'claude-code': '202609202000 - Claude Code',
        'codex': '202609202000 - Codex',
        'openai codex': '202609202000 - Codex',
        'openai-codex': '202609202000 - Codex',
        'cursor': '202609202000 - Cursor',
        'windsurf': '202609200800 - Windsurf',
        'opencode': '202609200758 - OpenCode',
        'hermes': '202609200759 - Hermes Agent',
        'hermes agent': '202609200759 - Hermes Agent',
        'hermes-agent': '202609200759 - Hermes Agent',
        'aider': '202609202000 - Aider',
        'cline': '202609202000 - Cline',
        'github copilot': '202609202001 - GitHub Copilot Agent',
        'github-copilot': '202609202001 - GitHub Copilot Agent',
        'gemini cli': '202609202002 - Gemini CLI',
        'gemini-cli': '202609202002 - Gemini CLI',
        'vscode': '202609202000 - Cursor',
        'browser use': '202609202000 - Browser Use MCP',
        'browser-use': '202609202000 - Browser Use MCP',
        'firecrawl': '202609202000 - Firecrawl MCP Server',
        'context7': '202609200803 - Context7 MCP',
        'fal': '202609200804 - FAL MCP Server',
        'kanban': '202609200805 - Hermes Kanban Dashboard',
        'curator': '202609200806 - Hermes Curator',
        'jev': '202609202000 - Jev Agent Router',
        'jev agent': '202609202000 - Jev Agent Router',
        'jev-agent': '202609202000 - Jev Agent Router',
        'playwright': '202609202010 - Playwright MCP',
        'chrome devtools': '202609202011 - Chrome DevTools MCP',
        'chrome-devtools': '202609202011 - Chrome DevTools MCP',
        'auto permission': '202609200807 - Claude Code Auto Permission',
        'auto-permission': '202609200807 - Claude Code Auto Permission',
    })
    
    return by_title

def resolve_link(link, by_title):
    """Resolve a wikilink to actual filename using exact matching only"""
    link_lower = link.lower().strip()
    
    # Direct lookup
    if link_lower in by_title:
        return by_title[link_lower]
    
    # Try with hyphens instead of spaces
    link_hyphenated = link_lower.replace(' ', '-')
    if link_hyphenated in by_title:
        return by_title[link_hyphenated]
    
    # If it already has a timestamp prefix, keep it
    if ' - ' in link:
        title_part = link.split(' - ', 1)[1].lower()
        if title_part in by_title:
            return by_title[title_part]
    
    return None

def fix_file(filepath, by_title):
    """Fix all wikilinks in a file"""
    with open(filepath) as f:
        content = f.read()
    
    original = content
    fixes = 0
    
    # Find all wikilinks
    links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    
    for link in links:
        # Skip MOCs
        if 'moc' in link.lower():
            continue
        
        # Skip links that already have timestamps (they're already resolved)
        if re.match(r'\d{12,14} - ', link):
            continue
        
        actual = resolve_link(link, by_title)
        if actual and actual != link:
            # Replace the wikilink with the resolved version
            content = content.replace(f'[[{link}]]', f'[[{actual}]]')
            fixes += 1
    
    if fixes > 0:
        with open(filepath, 'w') as f:
            f.write(content)
    
    return fixes

def main():
    print("RESOLVING ALL WIKILINKS TO ACTUAL FILENAMES")
    print("=" * 60)
    
    os.chdir(VAULT)
    by_title = build_map()
    print(f"Built map: {len(by_title)} entries")
    
    total_fixes = 0
    files_fixed = 0
    
    folders = ['03 - Agents', '04 - Plugins', '05 - Architecture', 
               '06 - Use Cases', '09 - Trend Radar/Heating Up', 
               '09 - Trend Radar/Stable', '09 - Trend Radar/Emerging',
               '07 - Structure']
    
    for folder in folders:
        fp = os.path.join(VAULT, folder)
        if not os.path.exists(fp):
            continue
        for f in sorted(os.listdir(fp)):
            if f.endswith('.md') and f not in EXCLUDE_FILES:
                filepath = os.path.join(fp, f)
                fixes = fix_file(filepath, by_title)
                if fixes > 0:
                    print(f"  {folder}/{f}: {fixes} fixes")
                    total_fixes += fixes
                    files_fixed += 1
    
    print(f"\nTotal: {total_fixes} fixes in {files_fixed} files")

if __name__ == '__main__':
    main()