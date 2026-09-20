#!/usr/bin/env python3
"""
resolve_wikilinks.py - Resolve ALL short-name wikilinks to actual filenames.
Replaces [[Short Name]] with [[YYYYMMDDHHMM - Actual Title]] in all notes.
"""

import os
import re
import json

VAULT = os.path.expanduser("~/repository/git/ai-matrix-trends")
EXCLUDE_FILES = ['AGENTS.md', 'README.md', 'LICENSE', 'daily-scan-prompt.md']

def build_map():
    """Build comprehensive lookup map"""
    by_title = {}
    
    for root, dirs, files in os.walk(VAULT):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                fname = f.replace('.md', '')
                if ' - ' in fname:
                    title = fname.split(' - ', 1)[1]
                    # Exact title
                    by_title[title.lower()] = fname
                    # Normalized
                    by_title[title.lower().replace(' ', '-').replace("'", "")] = fname
                    # Without special chars
                    clean = re.sub(r'[^a-z0-9\s-]', '', title.lower())
                    by_title[clean] = fname
                    by_title[clean.replace(' ', '-')] = fname
    
    # MOCs
    by_title['moc-trending-agents'] = 'MOC-Trending-Agents'
    by_title['moc-plugin-ecosystem'] = 'MOC-Plugin-Ecosystem'
    by_title['moc-architecture-patterns'] = 'MOC-Architecture-Patterns'
    by_title['moc-trend-radar'] = 'MOC-Trend-Radar'
    
    # Common short names
    by_title.update({
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
        'github-copilot': '202609202001 - GitHub Copilot Agent',
        'gemini-cli': '202609202002 - Gemini CLI',
        'vscode': '202609202000 - Cursor',
        'browser-use': '202609202000 - Browser Use MCP',
        'firecrawl': '202609202000 - Firecrawl MCP Server',
        'context7': '202609200803 - Context7 MCP',
        'fal': '202609200804 - FAL MCP Server',
        'kanban': '202609200805 - Hermes Kanban Dashboard',
        'curator': '202609200806 - Hermes Curator',
        'jev': '202609202000 - Jev Agent Router',
        'jev-agent': '202609202000 - Jev Agent Router',
        'playwright': '202609202010 - Playwright MCP',
        'chrome-devtools': '202609202011 - Chrome DevTools MCP',
        'auto-permission': '202609200807 - Claude Code Auto Permission',
    })
    
    return by_title

def resolve_link(link, by_title):
    """Resolve a wikilink to actual filename"""
    link_lower = link.lower().replace(' ', '-').replace("'", "")
    
    # Direct title match
    if link_lower in by_title:
        return by_title[link_lower]
    
    # Without timestamp
    if ' - ' in link:
        title = link.split(' - ', 1)[1].lower().replace(' ', '-').replace("'", "")
        if title in by_title:
            return by_title[title]
    
    # Partial match
    for key, val in by_title.items():
        if link_lower in key or key in link_lower:
            return val
    
    # Word-level partial
    words = link_lower.replace('-', ' ').split()
    for word in words:
        if len(word) > 3 and word in by_title:
            return by_title[word]
    
    return None

def fix_file(filepath, by_title):
    """Fix all wikilinks in a file"""
    with open(filepath) as f:
        content = f.read()
    
    original = content
    fixes = 0
    
    # Find all wikilinks in body AND frontmatter
    links = re.findall(r'\[\[([^\]]+)\]\]', content)
    
    for link in links:
        # Skip MOCs
        if 'moc' in link.lower():
            continue
        
        actual = resolve_link(link, by_title)
        if actual and actual != link:
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
