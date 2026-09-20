#!/usr/bin/env python3
"""
collect_agent_plugins.py - Collect and score plugins/extensions for each agent.
Creates a comprehensive table in README.md showing which plugins work with which agents.

Scoring:
- Cross-agent compatibility (works with 2+ agents = +20 points)
- GitHub stars/installs (1 point per 1000 stars, max 50)
- Mention frequency (5 points per mention)
- Tag bonuses (mcp=+15, trending=+20)
"""

import os
import re
import json
from datetime import datetime
from collections import defaultdict

VAULT = os.path.expanduser("~/repository/git/ai-matrix-trends")
AGENTS = {
    'claude-code': '202609202000 - Claude Code.md',
    'opencode': '202609200758 - OpenCode.md',
    'hermes': '202609200759 - Hermes Agent.md',
    'cursor': '202609202000 - Cursor.md',
    'codex': '202609202000 - Codex.md',
}
PLUGINS_DIR = os.path.join(VAULT, "04 - Plugins")

def scan_plugins():
    """Scan all plugin notes and extract compatibility data"""
    plugins = {}
    
    if not os.path.exists(PLUGINS_DIR):
        return plugins
    
    for f in sorted(os.listdir(PLUGINS_DIR)):
        if not f.endswith('.md') or f.startswith('00 -'):
            continue
        
        filepath = os.path.join(PLUGINS_DIR, f)
        with open(filepath) as fh:
            content = fh.read()
        
        # Extract metadata
        title_match = re.search(r'^# (.+)', content, re.MULTILINE)
        title = title_match.group(1) if title_match else f.replace('.md', '')
        
        # Stars
        stars_match = re.findall(r'(\d+)[,.]?(\d+)?[,.]?(\d+)?\+?\s*(?:stars?|⭐|installs?)', content, re.IGNORECASE)
        stars_num = 0
        if stars_match:
            try:
                stars_num = int(''.join([g for g in stars_match[0] if g]))
            except:
                pass
        
        # Compatibility (from Compatibility section or frontmatter agents field)
        compat_agents = set()
        compat_section = re.search(r'## Compatibility.*?\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
        if compat_section:
            for agent_key, agent_file in AGENTS.items():
                agent_name = agent_file.split(' - ')[1].replace('.md', '')
                if agent_name.lower() in compat_section.group(1).lower():
                    compat_agents.add(agent_key)
        
        # Also check frontmatter
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            agents_match = re.search(r'agents:\s*\[(.*?)\]', fm, re.DOTALL)
            if agents_match:
                for agent_key in AGENTS:
                    if agent_key in agents_match.group(1).lower():
                        compat_agents.add(agent_key)
        
        # Score
        score = 0
        score += min(stars_num // 1000, 50)
        score += len(compat_agents) * 20
        
        # Tags
        tags_match = re.search(r'^tags:\n((?:\s*-\s*.+\n?)+)', content, re.MULTILINE)
        tags = []
        if tags_match:
            tags = [t.strip().strip('-').strip() for t in tags_match.group(1).strip().split('\n')]
        
        if 'mcp' in tags:
            score += 15
        if 'trending' in tags:
            score += 20
        
        plugins[f.replace('.md', '')] = {
            'title': title,
            'file': f,
            'stars': stars_num,
            'agents': list(compat_agents),
            'score': score,
            'tags': tags,
        }
    
    return plugins

def generate_agent_table(agent_key, agent_name, plugins):
    """Generate a Markdown table for a specific agent"""
    # Filter plugins that support this agent
    agent_plugins = {k: v for k, v in plugins.items() if agent_key in v.get('agents', [])}
    
    # Sort by score
    sorted_plugins = sorted(agent_plugins.items(), key=lambda x: x[1]['score'], reverse=True)
    
    table = f"### {agent_name}\n\n"
    table += f"*Top plugins/extensions for {agent_name}*\n\n"
    table += "| # | Plugin | Score | Stars | Type |\n"
    table += "|---|--------|-------|-------|------|\n"
    
    for i, (name, data) in enumerate(sorted_plugins[:5], 1):
        file_path = f"04 - Plugins/{data['file']}"
        encoded = file_path.replace(' ', '%20')
        table += f"| {i} | [{data['title']}](./{encoded}) | {data['score']} | {data['stars'] if data['stars'] else '—'} | {', '.join(data['tags'][:2])} |\n"
    
    if not sorted_plugins:
        table += "*No plugins found yet. Run daily scan to collect plugins.*\n"
    
    table += "\n"
    return table

def update_readme_agent_plugins():
    """Update README.md with per-agent plugin tables"""
    plugins = scan_plugins()
    
    readme_path = os.path.join(VAULT, 'README.md')
    with open(readme_path) as f:
        content = f.read()
    
    # Generate per-agent tables
    agent_tables = "## 🔌 Plugins by Agent\n\n"
    agent_tables += f"*Top 5 scored plugins for each agentic tool — Last updated: {datetime.now().strftime('%Y-%m-%d')}*\n\n"
    
    for agent_key, agent_file in AGENTS.items():
        agent_name = agent_file.split(' - ')[1].replace('.md', '')
        agent_tables += generate_agent_table(agent_key, agent_name, plugins)
    
    # Also add cross-agent comparison table
    agent_tables += "## 📊 Plugin Compatibility Matrix\n\n"
    agent_tables += "| Plugin | " + " | ".join(AGENTS.keys()) + " | Score |\n"
    agent_tables += "|--------|" + "|".join(["------" for _ in AGENTS]) + "|-------|\n"
    
    # Sort all plugins by score
    sorted_all = sorted(plugins.items(), key=lambda x: x[1]['score'], reverse=True)
    
    for name, data in sorted_all[:10]:
        row = f"| [{data['title']}](./04%20-%20Plugins/{data['file'].replace(' ', '%20')}) |"
        for agent_key in AGENTS:
            if agent_key in data.get('agents', []):
                row += " ✅ |"
            else:
                row += " — |"
        row += f" {data['score']} |"
        agent_tables += row + "\n"
    
    agent_tables += "\n---\n"
    
    # Replace or add section
    if '## 🔌 Plugins by Agent' in content:
        # Replace existing
        pattern = r'(## 🔌 Plugins by Agent\n)(.*?)(?=\n## [^🔌]|\Z)'
        content = re.sub(pattern, agent_tables, content, flags=re.DOTALL)
    else:
        content += agent_tables
    
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"Updated README with per-agent plugin tables")
    print(f"Total plugins tracked: {len(plugins)}")
    for agent_key, agent_file in AGENTS.items():
        count = len([p for p in plugins.values() if agent_key in p.get('agents', [])])
        print(f"  {agent_file.split(' - ')[1].replace('.md', '')}: {count} plugins")

def main():
    os.chdir(VAULT)
    update_readme_agent_plugins()

if __name__ == '__main__':
    main()
