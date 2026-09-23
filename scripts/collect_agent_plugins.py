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
    'windsurf': '202609200800 - Windsurf.md',
    'aider': '202609202000 - Aider.md',
    'gemini-cli': '202609202002 - Gemini CLI.md',
    'github-copilot': '202609202001 - GitHub Copilot Agent.md',
    'kilo-code': '2026092014 - Kilo Code.md',
    'roocode': '202609202004 - RooCode.md',
    'jetbrains-junie': '202609202005 - JetBrains Junie.md',
    'cline': '202609202000 - Cline.md',
    'factory-code': '202609202065 - Factory Code.md',
    'sweep-ai': '202609202075 - Sweep AI.md',
    'greptile': '202609202085 - Greptile.md',
    'openhands': '202609202095 - OpenHands.md',
    'continue-dev': '202609202105 - Continue.dev.md',
    'sourcegraph-cody': '202609202115 - Sourcegraph Cody.md',
    'tabnine': '202609202125 - Tabnine.md',
    'mintlify': '202609202135 - Mintlify.md',
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
        
        # Compatibility - ONLY from frontmatter agents: field
        # Do NOT match body text (mentions != compatibility)
        compat_agents = set()
        
        # Check frontmatter - handle both YAML list and bracketed array
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
                # Try YAML list format:
                # agents:
                #   - claude-code
                #   - "202609202000 - Claude Code"
                agents_match = re.search(r'agents:\s*\n((?:\s*-\s*.+\n?)+)', fm, re.MULTILINE)
                if agents_match:
                    agents_text = agents_match.group(1).lower()
                    for agent_key, agent_file in AGENTS.items():
                        agent_name = agent_file.split(' - ')[1].replace('.md', '').lower()
                        if agent_key in agents_text or agent_name in agents_text:
                            compat_agents.add(agent_key)
        
        # Score
        score = 0
        score += min(stars_num // 1000, 50)
        # Cross-agent bonus: more agents = more points, but diminishing returns
        num_agents = len(compat_agents)
        if num_agents <= 2:
            score += 60  # Agent-specific plugins get big bonus
        elif num_agents <= 5:
            score += 40
        elif num_agents <= 10:
            score += 20
        else:
            score += 10  # Universal MCP plugins get small bonus
        
        # Tags
        tags_match = re.search(r'^tags:\n((?:[-\s]+.+\n?)+)', content, re.MULTILINE)
        tags = []
        if tags_match:
            tags = [t.strip().strip('-').strip() for t in tags_match.group(1).strip().split('\n') if t.strip()]
        
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
    
    # Sort: agent-specific plugins first (fewer total agents = more specific), then by score
    def sort_key(item):
        name, data = item
        num_agents = len(data.get('agents', []))
        score = data.get('score', 0)
        # Prioritize: fewer agents (more specific), then higher score
        # Use negative score for descending sort, but primary sort is specificity
        return (num_agents, -score)
    
    sorted_plugins = sorted(agent_plugins.items(), key=sort_key)
    
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

def clean_duplicates(content):
    """Remove duplicate sections, keeping only the first occurrence of each."""
    headers = [(m.start(), m.group()) for m in re.finditer(r'^## .+', content, re.MULTILINE)]
    
    seen = set()
    to_remove = []
    
    for pos, header in headers:
        normalized = re.sub(r'[^\w\s-]', '', header).strip().lower()
        if normalized in seen:
            to_remove.append((pos, header))
        else:
            seen.add(normalized)
    
    for pos, header in reversed(to_remove):
        next_section = content.find('\n## ', pos + 1)
        if next_section == -1:
            next_section = len(content)
        content = content[:pos] + content[next_section:]
    
    return content

def update_readme_agent_plugins():
    """Update README.md with per-agent plugin tables"""
    plugins = scan_plugins()
    
    readme_path = os.path.join(VAULT, 'README.md')
    with open(readme_path) as f:
        content = f.read()
    
    # Clean up any duplicate sections first
    content = clean_duplicates(content)
    
    # Generate per-agent tables
    agent_tables = "## 🔌 Plugins by Agent\n\n"
    agent_tables += f"*Top 5 scored plugins for each agentic tool — Last updated: {datetime.now().strftime('%Y-%m-%d')}*\n\n"
    
    for agent_key, agent_file in AGENTS.items():
        agent_name = agent_file.split(' - ')[1].replace('.md', '')
        agent_tables += generate_agent_table(agent_key, agent_name, plugins)
    
    # Generate cross-agent comparison matrix (compact, top 6 agents)
    top_agents = ['claude-code', 'opencode', 'cursor', 'codex', 'hermes', 'windsurf']
    top_agent_labels = {
        'claude-code': 'Claude Code',
        'opencode': 'OpenCode',
        'cursor': 'Cursor',
        'codex': 'Codex',
        'hermes': 'Hermes',
        'windsurf': 'Windsurf',
    }
    
    sorted_all = sorted(plugins.items(), key=lambda x: x[1]['score'], reverse=True)[:15]
    
    matrix = "## 📊 Plugin Compatibility Matrix\n\n"
    matrix += "*Top plugins vs. major agents — ✅ = compatible, · = not yet supported*\n\n"
    header = "| Plugin | " + " | ".join(top_agent_labels[k] for k in top_agents) + " | Total |"
    sep = "|" + "|".join(["--------" for _ in range(len(top_agents) + 2)]) + "|"
    matrix += header + "\n" + sep + "\n"
    
    for name, data in sorted_all[:15]:
        title = data['title']
        if len(title) > 28:
            title = title[:25] + "…"
        encoded = f"./04%20-%20Plugins/{data['file'].replace(' ', '%20')}"
        row = f"| [{title}]({encoded}) |"
        total = len(data.get('agents', []))
        for agent_key in top_agents:
            if agent_key in data.get('agents', []):
                row += " ✅ |"
            else:
                row += " · |"
        row += f" {total} |"
        matrix += row + "\n"
    
    matrix += "\n> **Full per-agent breakdowns:** See [Plugin Master Index](04%20-%20Plugins/00%20-%20Plugin%20Master%20Index.md) for complete tables.\n"
    matrix += "---\n"
    
    agent_tables += matrix
    
    # Replace or add section
    if '## 🔌 Plugins by Agent' in content:
        # Replace existing
        pattern = r'## 🔌 Plugins by Agent\n.*?(?=\n## [^🔌]|\Z)'
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
