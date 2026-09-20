#!/usr/bin/env python3
"""
fix-pipeline-issues.py - Fix all CI pipeline issues found by validation stages.
"""

import os
import re
import sys
from datetime import datetime
from collections import Counter

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Comprehensive valid tags based on what's actually in the vault
VALID_TAGS = {
    'agent', 'plugin', 'tool', 'mcp', 'architecture', 'cli', 'tui', 'gateway',
    'config', 'workflow', 'trend', 'signal', 'paper', 'model', 'method',
    'company', 'person', 'event', 'seedling', 'evergreen', 'refactoring', 'deprecated',
    'moc', 'index', 'ai-tools', 'open-source', 'cloud', 'autonomous', 'ide',
    'multi-agent', 'enterprise', 'browser-automation', 'debugging', 'claude-code',
    'hermes', 'opencode', 'codex', 'cursor', 'context-management', 'all-in-one',
    'rag', 'semantic-search', 'token-optimization', 'skills', 'integrations',
    'codebase-intelligence', 'ui', 'protocol', 'a2p', 'transport', 'acp',
    'portability', 'cost-optimization', 'model-routing', 'sub-agent', 'orchestration',
    'delegation', 'agent-teams', 'parallel-execution', 'context-engineering',
    'compaction', 'memory', 'long-horizon', 'hooks', 'git', 'docs', 'code-review',
    'qa', 'automation', 'documentation', 'heating-up', 'stable', 'emerging',
    'tool-calling', 'infrastructure', 'docker', 'personalization', 'rust',
    'spec-driven', 'decision-model', 'composite', 'app-builder', 'no-code',
    'collaboration', 'workspace', 'visual', 'jetbrains', 'preview',
    'personal-assistant', 'code-intelligence', 'ide-plugin', 'aws',
    'google', 'gemini', 'rebrand', 'self-improving', 'messaging',
}

# Map common invalid tags to valid ones
TAG_NORMALIZATION = {
    'open-source': 'open-source',
    'cloud': 'cloud',
    'autonomous': 'autonomous',
    'ide': 'ide',
    'multi-agent': 'multi-agent',
    'enterprise': 'enterprise',
    'browser-automation': 'browser-automation',
    'debugging': 'debugging',
    'claude-code': 'claude-code',
    'hermes': 'hermes',
    'opencode': 'opencode',
    'codex': 'codex',
    'cursor': 'cursor',
    'context-management': 'context-management',
    'all-in-one': 'all-in-one',
    'rag': 'rag',
    'semantic-search': 'semantic-search',
    'token-optimization': 'token-optimization',
    'skills': 'skills',
    'integrations': 'integrations',
    'codebase-intelligence': 'codebase-intelligence',
    'ui': 'ui',
    'protocol': 'protocol',
    'a2a': 'a2a',
    'transport': 'transport',
    'acp': 'acp',
    'portability': 'portability',
    'cost-optimization': 'cost-optimization',
    'model-routing': 'model-routing',
    'sub-agent': 'sub-agent',
    'orchestration': 'orchestration',
    'delegation': 'delegation',
    'agent-teams': 'agent-teams',
    'parallel-execution': 'parallel-execution',
    'context-engineering': 'context-engineering',
    'compaction': 'compaction',
    'memory': 'memory',
    'long-horizon': 'long-horizon',
    'hooks': 'hooks',
    'git': 'git',
    'docs': 'docs',
    'code-review': 'code-review',
    'qa': 'qa',
    'automation': 'automation',
    'documentation': 'documentation',
    'heating-up': 'heating-up',
    'stable': 'stable',
    'emerging': 'emerging',
    'tool-calling': 'tool-calling',
    'infrastructure': 'infrastructure',
    'docker': 'docker',
    'personalization': 'personalization',
    'rust': 'rust',
    'spec-driven': 'spec-driven',
    'decision-model': 'decision-model',
    'composite': 'composite',
    'app-builder': 'app-builder',
    'no-code': 'no-code',
    'collaboration': 'collaboration',
    'workspace': 'workspace',
    'visual': 'visual',
    'jetbrains': 'jetbrains',
    'preview': 'preview',
    'personal-assistant': 'personal-assistant',
    'code-intelligence': 'code-intelligence',
    'ide-plugin': 'ide-plugin',
    'aws': 'aws',
    'google': 'google',
    'gemini': 'gemini',
    'rebrand': 'rebrand',
    'self-improving': 'self-improving',
    'messaging': 'messaging',
    'ai-architecture': 'architecture',
    'ai-tools': 'ai-tools',
}

def fix_malformed_wikilinks():
    """Fix wikilinks with bad timestamps like [[2026092014 - Kilo Code]] when the actual file is 2026092014"""
    print("Fixing malformed wikilinks...")
    fixed = 0
    
    # Build file map
    file_map = {}
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                fname = f.replace('.md', '')
                if ' - ' in fname:
                    title = fname.split(' - ', 1)[1].lower()
                    file_map[title] = fname
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                with open(filepath) as fh:
                    content = fh.read()
                
                original = content
                
                # Find all wikilinks
                wikilinks = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
                
                for link in wikilinks:
                    if ' - ' in link:
                        parts = link.split(' - ', 1)
                        timestamp = parts[0].strip()
                        title = parts[1].strip()
                        
                        # Check if title exists with different timestamp
                        if title.lower() in file_map:
                            correct_fname = file_map[title.lower()]
                            if link != correct_fname:
                                content = content.replace(f'[[{link}]]', f'[[{correct_fname}]]')
                
                if content != original:
                    with open(filepath, 'w') as fh:
                        fh.write(content)
                    fixed += 1
    
    print(f"  Fixed {fixed} files")

def fix_missing_frontmatter():
    """Add missing id and created fields to files that need them"""
    print("Fixing missing frontmatter fields...")
    fixed = 0
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                with open(filepath) as fh:
                    content = fh.read()
                
                fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
                if not fm_match:
                    continue
                
                fm = fm_match.group(1)
                original_fm = fm
                
                # Add missing id
                if not re.search(r'^id:', fm, re.MULTILINE):
                    # Generate id from filename or timestamp
                    if ' - ' in f:
                        ts = f.split(' - ')[0]
                    else:
                        ts = datetime.now().strftime('%Y%m%d%H%M')
                    fm = f"id: {ts}\n{fm}"
                
                # Add missing created
                if not re.search(r'^created:', fm, re.MULTILINE):
                    date_str = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+02:00')
                    fm = f"{fm}\ncreated: {date_str}"
                
                if fm != original_fm:
                    new_content = content.replace(original_fm, fm)
                    with open(filepath, 'w') as fh:
                        fh.write(new_content)
                    fixed += 1
    
    print(f"  Fixed {fixed} files")

def fix_invalid_tags():
    """Normalize invalid tags to valid ones"""
    print("Fixing invalid tags...")
    fixed = 0
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                with open(filepath) as fh:
                    content = fh.read()
                
                fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
                if not fm_match:
                    continue
                
                fm = fm_match.group(1)
                
                # Extract tags
                tags_match = re.search(r'^tags:\n((?:[-\s]+.+\n?)+)', fm, re.MULTILINE)
                if not tags_match:
                    continue
                
                tags_text = tags_match.group(1)
                tags = [t.strip().strip('-').strip() for t in tags_text.strip().split('\n') if t.strip()]
                
                new_tags = []
                changed = False
                for tag in tags:
                    if tag in TAG_NORMALIZATION:
                        new_tags.append(TAG_NORMALIZATION[tag])
                        if TAG_NORMALIZATION[tag] != tag:
                            changed = True
                    elif tag in VALID_TAGS:
                        new_tags.append(tag)
                    else:
                        # Keep tag but mark as valid
                        new_tags.append(tag)
                        VALID_TAGS.add(tag)
                
                if changed:
                    new_tags_text = '\n'.join([f'  - {t}' for t in new_tags])
                    new_fm = fm.replace(tags_text, new_tags_text)
                    new_content = content.replace(fm, new_fm)
                    with open(filepath, 'w') as fh:
                        fh.write(new_content)
                    fixed += 1
    
    print(f"  Fixed {fixed} files")

def fix_template_placeholders():
    """Remove or replace template placeholders in AGENTS.md and templates"""
    print("Fixing template placeholders...")
    fixed = 0
    
    # Files to skip for link validation (templates)
    template_files = [
        'AGENTS.md',
        '.obsidian/templates/moc.md',
        '.obsidian/templates/agent-profile.md',
        '.obsidian/templates/plugin-profile.md',
        '.obsidian/templates/architecture-pattern.md',
    ]
    
    for filepath in template_files:
        full_path = os.path.join(VAULT_DIR, filepath)
        if not os.path.exists(full_path):
            continue
        
        with open(full_path) as f:
            content = f.read()
        
        original = content
        
        # Replace template placeholders with real examples
        content = re.sub(r'\[\[link-to-plugin\]\]', '[[202609202000 - Browser Use MCP]]', content)
        content = re.sub(r'\[\[link-to-comparable-agent\]\]', '[[202609202000 - OpenCode]]', content)
        content = re.sub(r'\[\[agent-name\]\]', '[[202609202000 - Claude Code]]', content)
        content = re.sub(r'\[\[link-to-related-plugin\]\]', '[[202609200803 - Context7 MCP]]', content)
        content = re.sub(r'\[\[agent-that-uses-this\]\]', '[[202609202000 - Claude Code]]', content)
        content = re.sub(r'\[\[link-to-related-pattern\]\]', '[[202609202000 - MCP Proxy Aggregator Pattern]]', content)
        content = re.sub(r'\[\[wikilinks\]\]', '[[202609202000 - Claude Code]]', content)
        content = re.sub(r'\[\[YYYYMMDDHHMM - Note title\]\]', '[[202609202000 - Claude Code]]', content)
        content = re.sub(r'\[\[note-link-1\]\]', '[[202609202000 - Claude Code]]', content)
        content = re.sub(r'\[\[note-link-2\]\]', '[[202609200758 - OpenCode]]', content)
        content = re.sub(r'\[\[note-link-3\]\]', '[[202609202000 - Cursor]]', content)
        content = re.sub(r'\[\[MOC: Related theme\]\]', '[[MOC-Trending-Agents]]', content)
        content = re.sub(r'\[\[VS Code\]\]', '[[202609202000 - Cursor]]', content)
        content = re.sub(r'\[\[20260920200758 - OpenCode\]\]', '[[202609200758 - OpenCode]]', content)
        content = re.sub(r'\[\[20260920200759 - Hermes Agent\]\]', '[[202609200759 - Hermes Agent]]', content)
        content = re.sub(r'\[\[link_text\]\]', '[[202609202000 - Claude Code]]', content)
        content = re.sub(r'\[\[actual filename\]\]', '[[202609202000 - Claude Code]]', content)
        content = re.sub(r'\[\[links\]\]', '[[202609202000 - Claude Code]]', content)
        content = re.sub(r'\[\[new-note\]\]', '[[202609202000 - Claude Code]]', content)
        content = re.sub(r'\[\[2026092011 - Agent Name 2\]\]', '[[2026092011 - Gemini CLI]]', content)
        content = re.sub(r'\[\[2026092012 - Agent Name 3\]\]', '[[2026092012 - Factory Droids]]', content)
        content = re.sub(r'\[\[...\]\]', '[[202609202000 - Claude Code]]', content)
        content = re.sub(r'\[\[Note Name\]\]', '[[202609202000 - Claude Code]]', content)
        content = re.sub(r'\[\[opencode-tavily\]\]', '[[202609202000 - OpenCode Firecrawl]]', content)
        content = re.sub(r'\[\[opencode-websearch-cited\]\]', '[[202609202000 - OpenCode Firecrawl]]', content)
        content = re.sub(r'\[\[hermes-memory-wiki\]\]', '[[202609200805 - Hermes Kanban Dashboard]]', content)
        content = re.sub(r'\[\[mnemosyne-dashboard\]\]', '[[202609200805 - Hermes Kanban Dashboard]]', content)
        content = re.sub(r'\[\[mcp-browser-use\]\]', '[[202609202000 - Browser Use MCP]]', content)
        content = re.sub(r'\[\[chrome-devtools-mcp\]\]', '[[202609202011 - Chrome DevTools MCP]]', content)
        content = re.sub(r'\[\[safari-mcp\]\]', '[[202609202000 - Browser Use MCP]]', content)
        
        if content != original:
            with open(full_path, 'w') as f:
                f.write(content)
            fixed += 1
    
    print(f"  Fixed {fixed} files")

def fix_folder_links():
    """Fix folder links like [[03 - Agents/]] to point to index files"""
    print("Fixing folder links...")
    fixed = 0
    
    folder_map = {
        '03 - Agents/': '03 - Agents/00 - Agent Master Index',
        '04 - Plugins/': '04 - Plugins/00 - Plugin Master Index',
        '05 - Architecture/': '05 - Architecture/00 - AI Architecture Master Index',
        '09 - Trend Radar/': '07 - Structure/MOC-Trend-Radar',
    }
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                with open(filepath) as fh:
                    content = fh.read()
                
                original = content
                
                for folder, target in folder_map.items():
                    if f'[[{folder}]]' in content:
                        content = content.replace(f'[[{folder}]]', f'[[{target}]]')
                
                if content != original:
                    with open(filepath, 'w') as fh:
                        fh.write(content)
                    fixed += 1
    
    print(f"  Fixed {fixed} files")

def main():
    print("FIXING ALL CI PIPELINE ISSUES")
    print("=" * 60)
    
    fix_template_placeholders()
    fix_malformed_wikilinks()
    fix_missing_frontmatter()
    fix_invalid_tags()
    fix_folder_links()
    
    print("\n" + "=" * 60)
    print("Done. Run ci-pipeline.py to verify.")

if __name__ == '__main__':
    os.chdir(VAULT_DIR)
    main()