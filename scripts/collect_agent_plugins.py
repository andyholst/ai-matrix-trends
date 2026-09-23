#!/usr/bin/env python3
"""
collect_agent_plugins.py - Build per-agent plugin tables and common MCP table.
- Per-agent tables: Best plugins for this agent (specific first, then common MCP)
- Common MCP table: All universal MCP plugins
- Compatibility matrix: Mix of specific and common plugins
"""

import os
import re
from datetime import datetime

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
TOP_AGENTS = ['claude-code', 'opencode', 'hermes', 'cursor', 'codex', 'windsurf']


def scan_plugins():
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

        stars_match = re.findall(r'(\d+)[,.]?(\d+)?[,.]?(\d+)?\+?\s*(?:stars?|⭐|installs?)', content, re.IGNORECASE)
        stars_num = 0
        if stars_match:
            try:
                stars_num = int(''.join([g for g in stars_match[0] if g]))
            except:
                pass

        mentions = len(re.findall(r'\b' + re.escape(title) + r'\b', content, re.IGNORECASE))

        # Compatibility - ONLY frontmatter agents: field
        compat_agents = set()
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            agents_match = re.search(r'agents:\s*\[(.*?)\]', fm, re.DOTALL)
            if agents_match:
                agents_text = agents_match.group(1).lower()
                for agent_key, agent_file in AGENTS.items():
                    agent_name = agent_file.split(' - ')[1].replace('.md', '').lower()
                    if agent_key in agents_text or agent_name in agents_text:
                        compat_agents.add(agent_key)
            else:
                agents_match = re.search(r'agents:\s*\n((?:\s*-\s*.+\n?)+)', fm, re.MULTILINE)
                if agents_match:
                    agents_text = agents_match.group(1).lower()
                    for agent_key, agent_file in AGENTS.items():
                        agent_name = agent_file.split(' - ')[1].replace('.md', '').lower()
                        if agent_key in agents_text or agent_name in agents_text:
                            compat_agents.add(agent_key)

        tags_match = re.search(r'^tags:\n((?:[-\s]+.+\n?)+)', content, re.MULTILINE)
        tags = []
        if tags_match:
            tags = [t.strip().strip('-').strip() for t in tags_match.group(1).strip().split('\n') if t.strip()]

        # Score based on QUALITY (stars, mentions, MCP bonus)
        # Agent-specific plugins get a massive bonus to always appear first
        num_agents = len(compat_agents)
        if num_agents <= 2:
            # Agent-specific: huge bonus (100+) + quality
            score = 100 + min(stars_num // 1000, 50) + mentions * 5
        elif num_agents >= 10:
            # Universal MCP: no bonus, just quality
            score = min(stars_num // 1000, 50) + mentions * 5
        else:
            # Mid-range: small bonus
            score = 50 + min(stars_num // 1000, 50) + mentions * 5
        
        if 'mcp' in tags:
            score += 15
        if 'trending' in tags:
            score += 20

        num_agents = len(compat_agents)
        if num_agents <= 2:
            category = 'specific'
        elif num_agents >= 5:
            category = 'common'
        else:
            category = 'niche'

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


def generate_agent_table(agent_key, agent_name, plugins):
    """Top plugins for this agent — specific first, then best common MCP"""
    agent_plugins = {
        k: v for k, v in plugins.items()
        if agent_key in v.get('agents', [])
    }

    # Sort: specific first (by score), then common (by score)
    def sort_key(item):
        data = item[1]
        cat = data.get('category', 'common')
        return (0 if cat == 'specific' else 1, -data['score'], -data['stars'])

    sorted_plugins = sorted(agent_plugins.items(), key=sort_key)

    table = f"### {agent_name}\n\n"
    table += f"*Top plugins/extensions for {agent_name}*\n\n"
    table += "| # | Plugin | Score | Stars | Type |\n"
    table += "|---|--------|-------|-------|------|\n"

    for i, (name, data) in enumerate(sorted_plugins[:8], 1):
        file_path = f"04 - Plugins/{data['file']}"
        encoded = file_path.replace(' ', '%20')
        stars_str = f"⭐ {data['stars']:,}" if data['stars'] > 0 else "—"
        table += f"| {i} | [{data['title']}](./{encoded}) | {data['score']} | {stars_str} | {', '.join(data['tags'][:2])} |\n"

    if not sorted_plugins:
        table += "*No plugins found yet.*\n"

    table += "\n"
    return table


def generate_common_mcp_table(plugins):
    """All universal MCP plugins with scores"""
    common = {k: v for k, v in plugins.items() if v.get('category') == 'common'}
    sorted_common = sorted(common.items(), key=lambda x: (-x[1]['score'], -x[1]['stars']))

    table = "## 🔌 Common MCP Plugins\n\n"
    table += "*Universal MCP servers that work across all major AI agents*\n\n"
    table += "| # | Plugin | Score | Stars | Agents | Type |\n"
    table += "|---|--------|-------|-------|--------|------|\n"

    for i, (name, data) in enumerate(sorted_common[:20], 1):
        file_path = f"04 - Plugins/{data['file']}"
        encoded = file_path.replace(' ', '%20')
        stars_str = f"⭐ {data['stars']:,}" if data['stars'] > 0 else "—"
        table += f"| {i} | [{data['title']}](./{encoded}) | {data['score']} | {stars_str} | {data['num_agents']} | {', '.join(data['tags'][:2])} |\n"

    if not sorted_common:
        table += "*No common MCP plugins found yet.*\n"

    table += "\n"
    return table


def generate_compact_matrix(plugins):
    """Compatibility matrix — mix of specific and common plugins, top 20 by score"""
    top_agents = ['claude-code', 'opencode', 'cursor', 'codex', 'hermes', 'windsurf']
    top_agent_labels = {
        'claude-code': 'Claude Code', 'opencode': 'OpenCode', 'cursor': 'Cursor',
        'codex': 'Codex', 'hermes': 'Hermes', 'windsurf': 'Windsurf',
    }

    # Get top 20 plugins by score (mix of specific and common)
    sorted_all = sorted(plugins.items(), key=lambda x: (-x[1]['score'], -x[1]['stars']))[:20]

    matrix = "## 📊 Plugin Compatibility Matrix\n\n"
    matrix += "*Top plugins vs. major agents — ✅ = compatible, · = not yet supported*\n\n"
    header = "| Plugin | " + " | ".join(top_agent_labels[k] for k in top_agents) + " |"
    sep = "|" + "|".join(["--------" for _ in range(len(top_agents) + 1)]) + "|"
    matrix += header + "\n" + sep + "\n"

    for name, data in sorted_all:
        title = data['title']
        if len(title) > 22:
            title = title[:19] + "…"
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
    plugins = scan_plugins()

    readme_path = os.path.join(VAULT, 'README.md')
    with open(readme_path) as f:
        content = f.read()

    # Build new section
    new_section = "## 🔌 Plugins by Agent\n\n"
    new_section += f"*Top plugins for each tool — Last updated: {datetime.now().strftime('%Y-%m-%d')}*\n\n"

    # Per-agent tables
    for agent_key in TOP_AGENTS:
        agent_name = AGENTS[agent_key].split(' - ')[1].replace('.md', '')
        new_section += generate_agent_table(agent_key, agent_name, plugins)

    # Common MCP table
    new_section += generate_common_mcp_table(plugins)

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
        count = len([p for p in plugins.values() if agent_key in p.get('agents', '')])
        print(f"  {agent_name}: {count} plugins")


if __name__ == '__main__':
    os.chdir(VAULT)
    update_readme()
