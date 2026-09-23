#!/usr/bin/env python3
"""
collect_agent_plugins.py - Build per-agent plugin tables and common MCP table.
- Per-agent tables: agent-specific plugins ONLY (no universal MCP duplicates)
- Common MCP table: universal MCP plugins that work across many agents
- Both sorted by quality/stars, not just agent count
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
    'windsurf': '202609200800 - Windsurf.md',
    'aider': '202609202000 - Aider.md',
    'gemini-cli': '202609202002 - Gemini CLI.md',
    'github-copilot': '202609202001 - GitHub Copilot Agent.md',
    'kilo-code': '2026092014 - Kilo Code.md',
    'roocode': '202609202004 - RooCode.md',
    'jetbrains-junie': '202609202005 - JetBrains Junie.md',
    'cline': '202609202000 - Cline.md',
}
PLUGINS_DIR = os.path.join(VAULT, "04 - Plugins")

# Only show these agents in per-agent tables (the "top tier")
TOP_AGENTS = ['claude-code', 'opencode', 'hermes', 'cursor', 'codex', 'windsurf']

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
        
        # Mentions (rough proxy for quality/popularity)
        mentions = len(re.findall(r'\b' + re.escape(title) + r'\b', content, re.IGNORECASE))
        
        # Compatibility - ONLY from frontmatter agents: field
        compat_agents = set()
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            # Try bracketed array: agents: [claude-code, opencode]
            agents_match = re.search(r'agents:\s*\[(.*?)\]', fm, re.DOTALL)
            if agents_match:
                agents_text = agents_match.group(1).lower()
                for agent_key, agent_file in AGENTS.items():
                    agent_name = agent_file.split(' - ')[1].replace('.md', '').lower()
                    if agent_key in agents_text or agent_name in agents_text:
                        compat_agents.add(agent_key)
            else:
                # Try YAML list format
                agents_match = re.search(r'agents:\s*\n((?:\s*-\s*.+\n?)+)', fm, re.MULTILINE)
                if agents_match:
                    agents_text = agents_match.group(1).lower()
                    for agent_key, agent_file in AGENTS.items():
                        agent_name = agent_file.split(' - ')[1].replace('.md', '').lower()
                        if agent_key in agents_text or agent_name in agents_text:
                            compat_agents.add(agent_key)
        
        # Tags
        tags_match = re.search(r'^tags:\n((?:[-\s]+.+\n?)+)', content, re.MULTILINE)
        tags = []
        if tags_match:
            tags = [t.strip().strip('-').strip() for t in tags_match.group(1).strip().split('\n') if t.strip()]
        
        # Score based on QUALITY (stars, mentions), not agent count
        score = 0
        score += min(stars_num // 1000, 50)  # Stars: up to 50 pts
        score += mentions * 5  # Mentions: 5 pts each
        if 'mcp' in tags:
            score += 15  # MCP bonus
        if 'trending' in tags:
            score += 20  # Trending bonus
        
        # Categorize
        num_agents = len(compat_agents)
        if num_agents <= 2:
            category = 'specific'  # Agent-specific
        elif num_agents >= 5:
            category = 'common'  # Universal MCP
        else:
            category = 'niche'  # A few agents
        
        plugins[f.replace('.md', '')] = {
            'title': title,
            'file': f,
            'stars': stars_num,
            'mentions': mentions,
            'agents': list(compat_agents),
            'score': score,
            'tags': tags,
            'category': category,
            'num_agents': num_agents,
        }
    
    return plugins


def generate_agent_specific_table(agent_key, agent_name, plugins):
    """Generate a table of top plugins for this agent.
    Mix of: agent-specific plugins + top universal MCP plugins, sorted by quality."""
    
    # Get all plugins that support this agent
    agent_plugins = {
        k: v for k, v in plugins.items() 
        if agent_key in v.get('agents', [])
    }
    
    # Sort by: category (specific first), then score (quality), then stars
    def sort_key(item):
        name, data = item
        cat = data.get('category', 'common')
        score = data.get('score', 0)
        stars = data.get('stars', 0)
        # specific=0 (first), niche=1, common=2
        cat_order = {'specific': 0, 'niche': 1, 'common': 2}
        return (cat_order.get(cat, 2), -score, -stars)
    
    sorted_plugins = sorted(agent_plugins.items(), key=sort_key)
    
    table = f"### {agent_name}\n\n"
    table += f"*Top plugins/extensions for {agent_name}*\n\n"
    table += "| # | Plugin | Score | Stars | Type |\n"
    table += "|---|--------|-------|-------|------|\n"
    
    for i, (name, data) in enumerate(sorted_plugins[:7], 1):
        file_path = f"04 - Plugins/{data['file']}"
        encoded = file_path.replace(' ', '%20')
        stars_str = f"⭐ {data['stars']:,}" if data['stars'] > 0 else "—"
        table += f"| {i} | [{data['title']}](./{encoded}) | {data['score']} | {stars_str} | {', '.join(data['tags'][:2])} |\n"
    
    if not sorted_plugins:
        table += "*No plugins found yet.*\n"
    
    table += "\n"
    return table


def generate_common_mcp_table(plugins):
    """Generate table of common MCP plugins (universal, 5+ agents)"""
    common = {
        k: v for k, v in plugins.items() 
        if v.get('category') == 'common'
    }
    
    # Sort by score (quality), then by stars
    sorted_common = sorted(common.items(), key=lambda x: (-x[1]['score'], -x[1]['stars']))
    
    table = "## 🔌 Common MCP Plugins\n\n"
    table += "*Universal MCP servers that work across all major AI agents*\n\n"
    table += "| # | Plugin | Score | Stars | Agents | Type |\n"
    table += "|---|--------|-------|-------|--------|------|\n"
    
    for i, (name, data) in enumerate(sorted_common[:15], 1):
        file_path = f"04 - Plugins/{data['file']}"
        encoded = file_path.replace(' ', '%20')
        stars_str = f"⭐ {data['stars']:,}" if data['stars'] > 0 else "—"
        num_agents = data.get('num_agents', 0)
        table += f"| {i} | [{data['title']}](./{encoded}) | {data['score']} | {stars_str} | {num_agents} | {', '.join(data['tags'][:2])} |\n"
    
    if not sorted_common:
        table += "*No common MCP plugins found yet.*\n"
    
    table += "\n"
    return table


def generate_compact_matrix(plugins):
    """Generate compact compatibility matrix for top agents"""
    top_agents = ['claude-code', 'opencode', 'cursor', 'codex', 'hermes', 'windsurf']
    top_agent_labels = {
        'claude-code': 'Claude Code',
        'opencode': 'OpenCode',
        'cursor': 'Cursor',
        'codex': 'Codex',
        'hermes': 'Hermes',
        'windsurf': 'Windsurf',
    }
    
    # Get top common MCP plugins
    common = {k: v for k, v in plugins.items() if v.get('category') == 'common'}
    sorted_common = sorted(common.items(), key=lambda x: (-x[1]['score'], -x[1]['stars']))[:10]
    
    matrix = "## 📊 Plugin Compatibility Matrix\n\n"
    matrix += "*Top common MCP plugins vs. major agents*\n\n"
    header = "| Plugin | " + " | ".join(top_agent_labels[k] for k in top_agents) + " |"
    sep = "|" + "|".join(["--------" for _ in range(len(top_agents) + 1)]) + "|"
    matrix += header + "\n" + sep + "\n"
    
    for name, data in sorted_common:
        title = data['title']
        if len(title) > 25:
            title = title[:22] + "…"
        encoded = f"./04%20-%20Plugins/{data['file'].replace(' ', '%20')}"
        row = f"| [{title}]({encoded}) |"
        for agent_key in top_agents:
            if agent_key in data.get('agents', []):
                row += " ✅ |"
            else:
                row += " · |"
        matrix += row + "\n"
    
    matrix += "\n---\n"
    return matrix


def update_readme():
    """Update README.md with all plugin tables"""
    plugins = scan_plugins()
    
    readme_path = os.path.join(VAULT, 'README.md')
    with open(readme_path) as f:
        content = f.read()
    
    # Build new section
    new_section = "## 🔌 Plugins by Agent\n\n"
    new_section += f"*Agent-specific plugins for each tool — Last updated: {datetime.now().strftime('%Y-%m-%d')}*\n\n"
    
    # Per-agent tables (specific plugins only)
    for agent_key in TOP_AGENTS:
        agent_file = AGENTS[agent_key]
        agent_name = agent_file.split(' - ')[1].replace('.md', '')
        new_section += generate_agent_specific_table(agent_key, agent_name, plugins)
    
    # Compact matrix
    new_section += generate_compact_matrix(plugins)
    
    # Replace existing section
    if '## 🔌 Plugins by Agent' in content:
        content = re.sub(
            r'## 🔌 Plugins by Agent\n.*?(?=\n## [^🔌]|\Z)',
            new_section,
            content,
            flags=re.DOTALL
        )
    else:
        content += new_section
    
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"Total plugins tracked: {len(plugins)}")
    print(f"  Agent-specific: {len([p for p in plugins.values() if p.get('category') == 'specific'])}")
    print(f"  Common MCP: {len([p for p in plugins.values() if p.get('category') == 'common'])}")
    for agent_key in TOP_AGENTS:
        agent_name = AGENTS[agent_key].split(' - ')[1].replace('.md', '')
        count = len([p for p in plugins.values() if agent_key in p.get('agents', '') and p.get('category') == 'specific'])
        print(f"  {agent_name}: {count} specific plugins")


if __name__ == '__main__':
    os.chdir(VAULT)
    update_readme()
