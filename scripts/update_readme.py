#!/usr/bin/env python3
"""
update_readme.py - Update README.md with comprehensive scored tables.
Top Plugins & Extensions shows top 5 plugins FOR EACH of the top 5 agents.
"""

import os
import re
import json
from datetime import datetime

VAULT = os.path.expanduser("~/repository/git/ai-matrix-trends")
DATA_FILE = os.path.join(VAULT, "08 - Projects", "trend-data.json")

# Top 5 agents to show plugin tables for
TOP_AGENTS = [
    ('claude-code', 'Claude Code', '202609202000 - Claude Code.md'),
    ('opencode', 'OpenCode', '202609200758 - OpenCode.md'),
    ('hermes', 'Hermes Agent', '202609200759 - Hermes Agent.md'),
    ('cursor', 'Cursor', '202609202000 - Cursor.md'),
    ('codex', 'Codex', '202609202000 - Codex.md'),
]

def load_trend_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {'items': {}}

def get_top_items(item_type, n=5):
    data = load_trend_data()
    items = data.get('items', {})
    filtered = {k: v for k, v in items.items() if v.get('type') == item_type}
    sorted_items = sorted(filtered.items(), key=lambda x: x[1].get('score', 0), reverse=True)
    return sorted_items[:n]

def generate_table_header():
    return "| # | Name | Score | Type | Stars | Status |\n|---|------|-------|------|-------|--------|"

def generate_table_row(i, name, item):
    score = item.get('score', 0)
    item_type = item.get('type', 'unknown')
    stars = item.get('stars', '—')
    if score >= 50:
        status = "Heating Up"
    elif score >= 20:
        status = "Stable"
    else:
        status = "Emerging"
    filename = item.get('file', '')
    title = os.path.basename(filename).replace('.md', '')
    encoded = filename.replace(' ', '%20')
    return f"| {i} | [{title}](./{encoded}) | {score} | {item_type} | {stars} | {status} |"

def clean_duplicates(content):
    headers = [(m.start(), m.group()) for m in re.finditer(r'^## .+', content, re.MULTILINE)]
    seen = set()
    to_remove = []
    for pos, header in headers:
        normalized = re.sub(r'[^\w\s]', '', header).strip().lower()
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

def get_all_agents():
    data = load_trend_data()
    items = data.get('items', {})
    agents = [(name, info) for name, info in items.items() if info.get('type') == 'agent']
    agents.sort(key=lambda x: x[1].get('score', 0), reverse=True)
    return agents

def scan_plugins():
    """Scan plugin files for agent compatibility"""
    plugins_dir = os.path.join(VAULT, "04 - Plugins")
    plugins = {}
    if not os.path.exists(plugins_dir):
        return plugins
    
    for f in sorted(os.listdir(plugins_dir)):
        if not f.endswith('.md') or f.startswith('00 -'):
            continue
        filepath = os.path.join(plugins_dir, f)
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
        
        # Mentions
        mentions = len(re.findall(r'\b' + re.escape(title) + r'\b', content, re.IGNORECASE))
        
        # Agents from frontmatter
        compat_agents = set()
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            for agent_key, agent_file in [(a, b) for a, b, c in TOP_AGENTS]:
                if agent_key in fm.lower():
                    compat_agents.add(agent_key)
        
        # Tags
        tags_match = re.search(r'^tags:\n((?:  - .+\n?)+)', content, re.MULTILINE)
        tags = []
        if tags_match:
            tags = [t.strip().strip('-').strip() for t in tags_match.group(1).strip().split('\n') if t.strip()]
        
        # Score
        score = min(stars_num // 1000, 50) + mentions * 5
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
            'score': score,
            'tags': tags,
            'agents': list(compat_agents),
            'category': category,
        }
    
    return plugins

def generate_top_plugins_per_agent(plugins):
    """Generate Top Plugins & Extensions section with top 5 for each of top 5 agents"""
    section = "## 🔌 Top Plugins & Extensions\n\n"
    section += "*Top 5 plugins for each of the top 5 AI tools/CLIs*\n\n"
    
    for agent_key, agent_name, agent_file in TOP_AGENTS:
        # Get plugins for this agent (specific first, then common, sorted by score)
        agent_plugins = {
            k: v for k, v in plugins.items()
            if agent_key in v.get('agents', [])
        }
        
        # Sort: specific first, then by score
        def sort_key(item):
            data = item[1]
            cat = data.get('category', 'common')
            return (0 if cat == 'specific' else 1, -data['score'], -data['stars'])
        
        sorted_plugins = sorted(agent_plugins.items(), key=sort_key)
        
        section += f"### {agent_name}\n\n"
        section += f"| # | Plugin | Score | Stars | Type |\n"
        section += "|---|--------|-------|-------|------|\n"
        
        for i, (name, data) in enumerate(sorted_plugins[:5], 1):
            file_path = f"04 - Plugins/{data['file']}"
            encoded = file_path.replace(' ', '%20')
            stars_str = f"⭐ {data['stars']:,}" if data['stars'] > 0 else "—"
            section += f"| {i} | [{data['title']}](./{encoded}) | {data['score']} | {stars_str} | {', '.join(data['tags'][:2])} |\n"
        
        if not sorted_plugins:
            section += "*No plugins found yet.*\n"
        
        section += "\n"
    
    return section

def generate_agent_tools_section():
    """Generate the full Agent Tools & CLIs section with all agents ranked"""
    agents = get_all_agents()
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    section = f"## 🛠️ Agent Tools & CLIs\n\n"
    section += f"*All {len(agents)} tracked agent tools/CLIs ranked by score — Last updated: {date_str}*\n\n"
    
    section += "| # | Agent | Score | Stars | Status | Tags |\n"
    section += "|---|-------|-------|-------|--------|------|\n"
    
    for i, (name, item) in enumerate(agents, 1):
        score = item.get('score', 0)
        stars = item.get('stars', 0)
        stars_str = f"⭐ {stars:,}" if stars > 0 else "—"
        status = "Heating Up" if score >= 50 else "Stable" if score >= 20 else "Emerging"
        tags = ', '.join(item.get('tags', [])[:3]) if item.get('tags') else "—"
        file_path = item.get('file', '')
        encoded = file_path.replace(' ', '%20')
        title = os.path.basename(file_path).replace('.md', '')
        section += f"| {i} | [{title}](./{encoded}) | {score} | {stars_str} | {status} | {tags} |\n"
    
    return section

def update_readme():
    os.chdir(VAULT)
    
    with open(os.path.join(VAULT, 'README.md')) as f:
        content = f.read()
    
    content = clean_duplicates(content)
    
    # Scan plugins for per-agent tables
    plugins = scan_plugins()
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    # Build new Trending Agents section
    agents = get_top_items('agent', 5)
    agents_section = f"""## 🚀 Trending Agents

*Top 5 scored trending — Last updated: {date_str}*

*See [Agent Master Index](./03%20-%20Agents/00%20-%20Agent%20Master%20Index.md) for complete list*

{generate_table_header()}
"""
    for i, (name, item) in enumerate(agents, 1):
        agents_section += generate_table_row(i, name, item) + "\n"
    agents_section += "\n"
    
    # Build Agent Tools & CLIs section
    agent_tools_section = generate_agent_tools_section()
    
    # Build NEW Top Plugins & Extensions section (top 5 per top 5 agent)
    plugins_section = generate_top_plugins_per_agent(plugins)
    
    # Build Trend Radar section
    data = load_trend_data()
    items = data.get('items', {})
    all_sorted = sorted(items.items(), key=lambda x: x[1].get('score', 0), reverse=True)
    
    heating_up = [(k, v) for k, v in all_sorted if v.get('score', 0) >= 50][:5]
    stable = [(k, v) for k, v in all_sorted if 20 <= v.get('score', 0) < 50][:5]
    emerging = [(k, v) for k, v in all_sorted if v.get('score', 0) < 20][:5]
    
    def build_subsection(title, data_list):
        section = f"### {title}\n\n"
        section += generate_table_header() + "\n"
        for i, (name, item) in enumerate(data_list, 1):
            section += generate_table_row(i, name, item) + "\n"
        return section + "\n"
    
    radar_section = f"""## 📊 Trend Radar

*Last updated: {date_str}*

"""
    radar_section += build_subsection("Heating Up", heating_up)
    radar_section += build_subsection("Stable", stable)
    radar_section += build_subsection("Emerging", emerging)
    
    # === REPLACE SECTIONS IN README ===
    
    # Replace Trending Agents
    if '## 🚀 Trending Agents' in content:
        content = re.sub(
            r'## 🚀 Trending Agents\n.*?(?=\n## |\Z)',
            agents_section,
            content,
            flags=re.DOTALL
        )
    
    # Replace Agent Tools & CLIs
    if '## 🛠️ Agent Tools & CLIs' in content:
        content = re.sub(
            r'## 🛠️ Agent Tools & CLIs\n.*?(?=\n## |\Z)',
            agent_tools_section,
            content,
            flags=re.DOTALL
        )
    
    # Replace Top Plugins & Extensions
    if '## 🔌 Top Plugins' in content:
        content = re.sub(
            r'## 🔌 Top Plugins[^\n]*\n.*?(?=\n## |\Z)',
            plugins_section,
            content,
            flags=re.DOTALL
        )
    
    # Replace Trend Radar
    if '## 📊 Trend Radar' in content:
        content = re.sub(
            r'## 📊 Trend Radar\n.*?(?=\n## |\Z)',
            radar_section,
            content,
            flags=re.DOTALL
        )
    
    # Update date
    content = re.sub(r'\*Last refreshed: .*\*', f'*Last refreshed: {date_str}*', content)
    
    with open(os.path.join(VAULT, 'README.md'), 'w') as f:
        f.write(content)
    
    print("README.md updated with scored tables")
    print(f"Top 5 Agents: {[a[0] for a in agents]}")
    print(f"Plugins tracked: {len(plugins)}")

if __name__ == '__main__':
    update_readme()
