#!/usr/bin/env python3
"""
update-plugin-master-index.py - Generate comprehensive Plugin Master Index.
Creates separate tables for each agent CLI with ALL plugins/extensions.
Run by cron job after collect_agent_plugins.py.

Compatibility detection:
1. frontmatter agents: [..] field (agent keys)
2. Compatibility section **Agent:** line (wikilinks like [[202609202000 - Claude Code]])
3. Body text scanning for agent names
4. MCP-compatible plugins (tag: mcp) with "any MCP-compatible" text work with ALL MCP agents
"""

import os
import re
import json
from datetime import datetime
from collections import defaultdict

VAULT = os.path.expanduser("~/repository/git/ai-matrix-trends")
PLUGINS_DIR = os.path.join(VAULT, "04 - Plugins")
INDEX_FILE = os.path.join(PLUGINS_DIR, "00 - Plugin Master Index.md")

# Agent definitions: key -> display_name
AGENTS = {
    'claude-code': 'Claude Code',
    'opencode': 'OpenCode',
    'hermes': 'Hermes Agent',
    'cursor': 'Cursor',
    'codex': 'Codex',
    'windsurf': 'Windsurf',
    'aider': 'Aider',
    'gemini-cli': 'Gemini CLI',
    'github-copilot': 'GitHub Copilot',
    'kilo-code': 'Kilo Code',
    'roocode': 'RooCode',
    'jetbrains-junie': 'JetBrains Junie',
}

# All agents that support MCP servers
MCP_AGENTS = ['claude-code', 'opencode', 'hermes', 'cursor', 'codex', 'windsurf', 'aider', 'gemini-cli', 'github-copilot', 'kilo-code', 'roocode', 'jetbrains-junie']

# Wikilink patterns for each agent in **Agent:** lines
AGENT_WIKILINKS = {
    'claude-code': ['202609202000 - Claude Code', '202609202000 - Claude'],
    'opencode': ['202609200758 - OpenCode', '202609200758 - Open'],
    'hermes': ['202609200759 - Hermes Agent', '202609200759 - Hermes'],
    'cursor': ['202609202000 - Cursor'],
    'codex': ['202609202000 - Codex'],
    'windsurf': ['202609200800 - Windsurf'],
    'aider': ['202609202000 - Aider'],
    'gemini-cli': ['2026092011 - Gemini CLI', '202609202002 - Gemini CLI'],
    'github-copilot': ['202609202001 - GitHub Copilot Agent'],
    'kilo-code': ['2026092014 - Kilo Code', '202609202003 - Kilo Code'],
    'roocode': ['202609202004 - RooCode'],
    'jetbrains-junie': ['202609202005 - JetBrains Junie'],
}

def scan_all_plugins():
    """Scan all plugin notes and extract data, deduplicating by title (keeps highest scored version)"""
    plugins_by_title = {}
    
    if not os.path.exists(PLUGINS_DIR):
        return []
    
    for f in sorted(os.listdir(PLUGINS_DIR)):
        if not f.endswith('.md') or f.startswith('00 -'):
            continue
        
        filepath = os.path.join(PLUGINS_DIR, f)
        with open(filepath) as fh:
            content = fh.read()
        
        # Extract title
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
        
        # === COMPATIBILITY DETECTION ===
        compat_agents = set()
        
        # 1. Check frontmatter agents: field (contains agent keys)
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            agents_match = re.search(r'agents:\s*\[(.*?)\]', fm, re.DOTALL)
            if agents_match:
                agents_str = agents_match.group(1).lower()
                for agent_key in AGENTS:
                    if agent_key in agents_str:
                        compat_agents.add(agent_key)
        
        # 2. Check Compatibility section **Agent:** line (contains wikilinks)
        compat_section = re.search(r'## Compatibility.*?\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
        if compat_section:
            compat_text = compat_section.group(1)
            # Look for **Agent:** line with wikilinks
            agent_line = re.search(r'\*\*Agent:\*\*\s*(.+?)(?:\n|$)', compat_text)
            if agent_line:
                agent_line_text = agent_line.group(1)
                # Check for wikilinks for each agent
                for agent_key, wikilinks in AGENT_WIKILINKS.items():
                    for wl in wikilinks:
                        if wl in agent_line_text:
                            compat_agents.add(agent_key)
                            break
            
            # Check for "any MCP-compatible" or "all MCP-compatible"
            compat_lower = compat_text.lower()
            if 'any mcp-compatible' in compat_lower or 'all mcp-compatible' in compat_lower or 'any mcp compatible' in compat_lower:
                for agent_key in MCP_AGENTS:
                    compat_agents.add(agent_key)
        
        # 3. Scan body text for agent mentions
        body_match = re.search(r'^---\n.*?\n---\n(.*)', content, re.DOTALL)
        if body_match:
            body_text = body_match.group(1).lower()
            agent_keywords = {
                'claude-code': ['claude code', 'claude-code', 'claudecode'],
                'opencode': ['opencode', 'open code', 'open-code'],
                'hermes': ['hermes agent', 'hermes-agent', 'hermes'],
                'cursor': ['cursor'],
                'codex': ['openai codex', 'codex'],
                'windsurf': ['windsurf'],
                'aider': ['aider'],
                'gemini-cli': ['gemini cli', 'gemini-cli'],
                'github-copilot': ['github copilot', 'copilot'],
                'kilo-code': ['kilo code', 'kilo-code', 'kilocode'],
                'roocode': ['roocode', 'roo code', 'roo-code'],
                'jetbrains-junie': ['jetbrains junie', 'junie', 'jetbrains air'],
            }
            for agent_key, keywords in agent_keywords.items():
                if agent_key not in compat_agents:
                    for kw in keywords:
                        if kw in body_text:
                            compat_agents.add(agent_key)
                            break
        
        # 4. If plugin has mcp tag and mentions "any MCP-compatible" in body, add all MCP agents
        tags_match = re.search(r'^tags:\n((?:-\s*.+\n?)+)', content, re.MULTILINE)
        tags = []
        if tags_match:
            tags = [t.strip().strip('-').strip() for t in tags_match.group(1).strip().split('\n')]
        
        if 'mcp' in tags:
            full_text = content.lower()
            if 'any mcp-compatible' in full_text or 'all mcp-compatible' in full_text or 'works with any' in full_text:
                for agent_key in MCP_AGENTS:
                    compat_agents.add(agent_key)
        
        # Score
        score = 0
        score += min(stars_num // 1000, 50)
        score += len(compat_agents) * 20
        if 'mcp' in tags:
            score += 15
        if 'trending' in tags:
            score += 20
        
        # Status based on score
        if score >= 50:
            status = "Heating Up"
        elif score >= 20:
            status = "Stable"
        else:
            status = "Emerging"
        
        # Description — extract from first paragraph after Overview
        desc_match = re.search(r'## Overview\n+(.+?)(?=\n## |\Z)', content, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""
        if '.' in description:
            description = description[:description.index('.') + 1]
        description = description.replace('\n', ' ').strip()
        
        # Deduplicate: keep only the highest scored version of each title
        title_key = title.lower()
        plugin_data = {
            'title': title,
            'file': f,
            'rel_path': f"./{f.replace(' ', '%20')}",
            'stars': stars_num,
            'agents': sorted(compat_agents),
            'score': score,
            'tags': tags,
            'status': status,
            'description': description,
        }
        
        if title_key in plugins_by_title:
            existing = plugins_by_title[title_key]
            if score > existing['score'] or (score == existing['score'] and len(description) > len(existing['description'])):
                plugins_by_title[title_key] = plugin_data
        else:
            plugins_by_title[title_key] = plugin_data
    
    return list(plugins_by_title.values())

def generate_agent_table(agent_key, agent_name, plugins):
    """Generate a complete table for a specific agent with ALL its plugins"""
    agent_plugins = [p for p in plugins if agent_key in p['agents']]
    
    if not agent_plugins:
        return f"### {agent_name}\n\n*No plugins tracked yet. Run daily scan to collect plugins.*\n\n"
    
    agent_plugins.sort(key=lambda x: x['score'], reverse=True)
    
    table = f"### {agent_name}\n\n"
    table += f"*All plugins/extensions for {agent_name} — {len(agent_plugins)} total*\n\n"
    table += "| # | Plugin | Score | Stars | Status | Description |\n"
    table += "|---|--------|-------|-------|--------|-------------|\n"
    
    for i, p in enumerate(agent_plugins, 1):
        stars_str = f"⭐ {p['stars']:,}" if p['stars'] > 0 else "—"
        desc = p['description'][:80] + ('...' if len(p['description']) > 80 else '')
        table += f"| {i} | [{p['title']}]({p['rel_path']}) | {p['score']} | {stars_str} | {p['status']} | {desc} |\n"
    
    table += "\n"
    return table

def generate_cross_agent_table(plugins):
    """Generate cross-agent compatibility matrix for top plugins"""
    top_plugins = sorted(plugins, key=lambda x: x['score'], reverse=True)[:20]
    
    table = "## 📊 Cross-Agent Compatibility Matrix\n\n"
    table += "*Top 20 plugins by score — which agents they support*\n\n"
    
    agent_names = [AGENTS[k] for k in AGENTS]
    table += "| Plugin | " + " | ".join(agent_names) + " | Score |\n"
    table += "|" + "|".join(["--------" for _ in range(len(AGENTS) + 1)]) + "|-------|\n"
    
    for p in top_plugins:
        row = f"| [{p['title']}]({p['rel_path']}) |"
        for agent_key in AGENTS:
            if agent_key in p['agents']:
                row += " ✅ |"
            else:
                row += " — |"
        row += f" {p['score']} |"
        table += row + "\n"
    
    table += "\n"
    return table

def generate_trending_table(plugins):
    """Generate trending plugins table"""
    trending = [p for p in plugins if p['status'] == 'Heating Up']
    trending.sort(key=lambda x: x['score'], reverse=True)
    
    table = "## 🔥 Trending Plugins (Heating Up)\n\n"
    table += "*Rapid growth signals — score >= 50*\n\n"
    table += "| # | Plugin | Score | Stars | Agents | Description |\n"
    table += "|---|--------|-------|-------|--------|-------------|\n"
    
    for i, p in enumerate(trending[:15], 1):
        stars_str = f"⭐ {p['stars']:,}" if p['stars'] > 0 else "—"
        agent_names = [AGENTS[a] for a in p['agents'][:3] if a in AGENTS]
        agents_str = ', '.join(agent_names) if agent_names else '—'
        if len(p['agents']) > 3:
            agents_str += f" +{len(p['agents'])-3}"
        desc = p['description'][:60] + ('...' if len(p['description']) > 60 else '')
        table += f"| {i} | [{p['title']}]({p['rel_path']}) | {p['score']} | {stars_str} | {agents_str} | {desc} |\n"
    
    if not trending:
        table += "*No trending plugins yet. Run daily scan to collect plugins.*\n"
    
    table += "\n"
    return table

def generate_stable_table(plugins):
    """Generate stable plugins table"""
    stable = [p for p in plugins if p['status'] == 'Stable']
    stable.sort(key=lambda x: x['score'], reverse=True)
    
    table = "## 📈 Stable Plugins (Established)\n\n"
    table += "*Established patterns — score 20-49*\n\n"
    table += "| # | Plugin | Score | Stars | Agents | Description |\n"
    table += "|---|--------|-------|-------|--------|-------------|\n"
    
    for i, p in enumerate(stable[:15], 1):
        stars_str = f"⭐ {p['stars']:,}" if p['stars'] > 0 else "—"
        agent_names = [AGENTS[a] for a in p['agents'][:3] if a in AGENTS]
        agents_str = ', '.join(agent_names) if agent_names else '—'
        if len(p['agents']) > 3:
            agents_str += f" +{len(p['agents'])-3}"
        desc = p['description'][:60] + ('...' if len(p['description']) > 60 else '')
        table += f"| {i} | [{p['title']}]({p['rel_path']}) | {p['score']} | {stars_str} | {agents_str} | {desc} |\n"
    
    if not stable:
        table += "*No stable plugins yet.*\n"
    
    table += "\n"
    return table

def generate_emerging_table(plugins):
    """Generate emerging plugins table"""
    emerging = [p for p in plugins if p['status'] == 'Emerging']
    emerging.sort(key=lambda x: x['score'], reverse=True)
    
    table = "## 🌱 Emerging Plugins (Watch List)\n\n"
    table += "*Early signals — score < 20*\n\n"
    table += "| # | Plugin | Score | Stars | Agents | Description |\n"
    table += "|---|--------|-------|-------|--------|-------------|\n"
    
    for i, p in enumerate(emerging[:15], 1):
        stars_str = f"⭐ {p['stars']:,}" if p['stars'] > 0 else "—"
        agent_names = [AGENTS[a] for a in p['agents'][:3] if a in AGENTS]
        agents_str = ', '.join(agent_names) if agent_names else '—'
        desc = p['description'][:60] + ('...' if len(p['description']) > 60 else '')
        table += f"| {i} | [{p['title']}]({p['rel_path']}) | {p['score']} | {stars_str} | {agents_str} | {desc} |\n"
    
    if not emerging:
        table += "*No emerging plugins yet.*\n"
    
    table += "\n"
    return table

def generate_category_table(plugins):
    """Generate plugins grouped by category"""
    categories = defaultdict(list)
    for p in plugins:
        tags_str = ','.join(p['tags'])
        if 'mcp' in tags_str:
            categories['MCP Servers'].append(p)
        elif 'browser' in tags_str or 'web' in tags_str:
            categories['Browser & Web'].append(p)
        elif 'memory' in tags_str or 'context' in tags_str:
            categories['Context & Memory'].append(p)
        elif 'code' in tags_str or 'editing' in tags_str:
            categories['Code Editing'].append(p)
        elif 'debug' in tags_str:
            categories['Debugging'].append(p)
        elif 'deploy' in tags_str or 'ci' in tags_str:
            categories['Deployment & CI/CD'].append(p)
        else:
            categories['Other'].append(p)
    
    table = "## 🗂️ Plugins by Category\n\n"
    
    for cat_name, cat_plugins in sorted(categories.items()):
        cat_plugins.sort(key=lambda x: x['score'], reverse=True)
        table += f"### {cat_name}\n\n"
        table += "| # | Plugin | Score | Stars | Agents |\n"
        table += "|---|--------|-------|-------|--------|\n"
        for i, p in enumerate(cat_plugins[:10], 1):
            stars_str = f"⭐ {p['stars']:,}" if p['stars'] > 0 else "—"
            agent_names = [AGENTS.get(a, a) for a in p['agents'][:2]]
            agents_str = ', '.join(agent_names) if agent_names else '—'
            table += f"| {i} | [{p['title']}]({p['rel_path']}) | {p['score']} | {stars_str} | {agents_str} |\n"
        table += "\n"
    
    return table

def generate_master_index():
    """Generate the complete Plugin Master Index"""
    plugins = scan_all_plugins()
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    content = f"""---
tags:
  - moc
  - plugin
  - ai-tools
  - index
links:
  - "[[202609202000 - Browser Use MCP]]"
  - "[[202609202000 - Jev Agent Router]]"
---

# AI Plugins & Extensions — Master Index

*Comprehensive index of all plugins/extensions for AI coding agents — Last updated: {date_str}*

**Total plugins tracked:** {len(plugins)}
**Agents covered:** {', '.join(AGENTS.values())}

---

## 📋 Table of Contents

1. [Trending Plugins](#trending-plugins-heating-up)
2. [Stable Plugins](#stable-plugins-established)
3. [Emerging Plugins](#emerging-plugins-watch-list)
4. [By Agent Ecosystem](#by-agent-ecosystem)
5. [By Category](#plugins-by-category)
6. [Cross-Agent Matrix](#cross-agent-compatibility-matrix)

---

"""
    
    content += generate_trending_table(plugins)
    content += "---\n\n"
    
    content += generate_stable_table(plugins)
    content += "---\n\n"
    
    content += generate_emerging_table(plugins)
    content += "---\n\n"
    
    content += "## 🔌 By Agent Ecosystem\n\n"
    content += "*Complete plugin lists for each agent CLI*\n\n"
    
    for agent_key, agent_name in AGENTS.items():
        content += generate_agent_table(agent_key, agent_name, plugins)
    
    content += "---\n\n"
    
    content += generate_category_table(plugins)
    content += "---\n\n"
    
    content += generate_cross_agent_table(plugins)
    content += "---\n\n"
    
    content += f"""## 📈 Statistics

| Metric | Value |
|--------|-------|
| Total plugins | {len(plugins)} |
| Heating Up | {len([p for p in plugins if p['status'] == 'Heating Up'])} |
| Stable | {len([p for p in plugins if p['status'] == 'Stable'])} |
| Emerging | {len([p for p in plugins if p['status'] == 'Emerging'])} |
| MCP servers | {len([p for p in plugins if 'mcp' in p['tags']])} |
| Cross-agent (2+) | {len([p for p in plugins if len(p['agents']) >= 2])} |

---

## 🔗 Related

- [[README]] — vault dashboard
- [[04 - Plugins/|All Plugins]] — all plugin notes
- [[05 - Architecture/|Architecture]] — architecture patterns
- [[09 - Trend Radar/|Trend Radar]] — trend analysis
"""
    
    with open(INDEX_FILE, 'w') as f:
        f.write(content)
    
    print(f"Updated Plugin Master Index: {len(plugins)} plugins tracked")
    print(f"  Heating Up: {len([p for p in plugins if p['status'] == 'Heating Up'])}")
    print(f"  Stable: {len([p for p in plugins if p['status'] == 'Stable'])}")
    print(f"  Emerging: {len([p for p in plugins if p['status'] == 'Emerging'])}")
    for agent_key, agent_name in AGENTS.items():
        count = len([p for p in plugins if agent_key in p['agents']])
        print(f"  {agent_name}: {count} plugins")

if __name__ == '__main__':
    os.chdir(VAULT)
    generate_master_index()
