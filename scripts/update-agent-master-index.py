#!/usr/bin/env python3
"""
update-agent-master-index.py - Generate comprehensive Agent Master Index.
Creates the top 5 trending agents table + complete list of all agents.
Run by cron job after aggregate-trends.py.
"""

import os
import re
import json
from datetime import datetime

VAULT = os.path.expanduser("~/repository/git/ai-matrix-trends")
AGENTS_DIR = os.path.join(VAULT, "03 - Agents")
INDEX_FILE = os.path.join(AGENTS_DIR, "00 - Agent Master Index.md")
DATA_FILE = os.path.join(VAULT, "08 - Projects", "trend-data.json")

def load_trend_data():
    """Load trend data from JSON"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {'items': {}}

def scan_all_agents():
    """Scan all agent notes and extract comprehensive data"""
    agents = []
    
    if not os.path.exists(AGENTS_DIR):
        return agents
    
    for f in sorted(os.listdir(AGENTS_DIR)):
        if not f.endswith('.md') or f.startswith('00 -'):
            continue
        
        filepath = os.path.join(AGENTS_DIR, f)
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
        
        # Tags
        tags_match = re.search(r'^tags:\n((?:-\s*.+\n?)+)', content, re.MULTILINE)
        tags = []
        if tags_match:
            tags = [t.strip().strip('-').strip() for t in tags_match.group(1).strip().split('\n')]
        
        # Score from trend data
        trend_data = load_trend_data()
        trend_items = trend_data.get('items', {})
        score = trend_items.get(title, {}).get('score', 0)
        
        # Also compute score if not in trend data
        if score == 0:
            score += min(stars_num // 1000, 50)
            if 'cli' in tags:
                score += 10
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
        
        # Links count
        links_match = re.findall(r'\[\[([^\]]+)\]\]', content)
        links_count = len(links_match)
        
        # Provider/company
        provider = ""
        provider_match = re.search(r'\|\s*\w+\s*\|\s*([^|]+?)\s*\|', content)
        if provider_match:
            provider = provider_match.group(1).strip()
        
        agents.append({
            'title': title,
            'file': f,
            'rel_path': f"./{f.replace(' ', '%20')}",
            'stars': stars_num,
            'score': score,
            'tags': tags,
            'status': status,
            'description': description,
            'links_count': links_count,
            'provider': provider,
        })
    
    return agents

def generate_top5_table(agents):
    """Generate top 5 trending agents table"""
    sorted_agents = sorted(agents, key=lambda x: x['score'], reverse=True)
    top5 = sorted_agents[:5]
    
    table = "## 🏆 Top 5 Trending Agents\n\n"
    table += "*Highest scored trending AI coding agents — updated daily*\n\n"
    table += "| # | Agent | Score | Stars | Status | Description |\n"
    table += "|---|-------|-------|-------|--------|-------------|\n"
    
    for i, a in enumerate(top5, 1):
        stars_str = f"⭐ {a['stars']:,}" if a['stars'] > 0 else "—"
        desc = a['description'][:80] + ('...' if len(a['description']) > 80 else '')
        table += f"| {i} | [{a['title']}]({a['rel_path']}) | {a['score']} | {stars_str} | {a['status']} | {desc} |\n"
    
    table += "\n"
    return table

def generate_complete_list(agents):
    """Generate complete list of all agents"""
    sorted_agents = sorted(agents, key=lambda x: x['score'], reverse=True)
    
    table = "## 📋 Complete Agent List\n\n"
    table += f"*All {len(agents)} tracked AI coding agents — sorted by score*\n\n"
    table += "| # | Agent | Score | Stars | Status | Tags | Links |\n"
    table += "|---|-------|-------|-------|--------|------|-------|\n"
    
    for i, a in enumerate(sorted_agents, 1):
        stars_str = f"⭐ {a['stars']:,}" if a['stars'] > 0 else "—"
        tags_str = ', '.join(a['tags'][:3]) if a['tags'] else '—'
        table += f"| {i} | [{a['title']}]({a['rel_path']}) | {a['score']} | {stars_str} | {a['status']} | {tags_str} | {a['links_count']} |\n"
    
    table += "\n"
    return table

def generate_status_tables(agents):
    """Generate tables grouped by status"""
    table = "## 📊 By Status\n\n"
    
    for status in ["Heating Up", "Stable", "Emerging"]:
        status_agents = [a for a in agents if a['status'] == status]
        if not status_agents:
            continue
        
        status_agents.sort(key=lambda x: x['score'], reverse=True)
        table += f"### {status} ({len(status_agents)})\n\n"
        table += "| # | Agent | Score | Stars | Description |\n"
        table += "|---|-------|-------|-------|-------------|\n"
        
        for i, a in enumerate(status_agents, 1):
            stars_str = f"⭐ {a['stars']:,}" if a['stars'] > 0 else "—"
            desc = a['description'][:60] + ('...' if len(a['description']) > 60 else '')
            table += f"| {i} | [{a['title']}]({a['rel_path']}) | {a['score']} | {stars_str} | {desc} |\n"
        
        table += "\n"
    
    return table

def generate_tag_tables(agents):
    """Generate tables grouped by tag/tag categories"""
    # Group agents by primary tag
    tag_groups = {}
    for a in agents:
        primary_tag = a['tags'][0] if a['tags'] else 'uncategorized'
        if primary_tag not in tag_groups:
            tag_groups[primary_tag] = []
        tag_groups[primary_tag].append(a)
    
    table = "## 🏷️ By Category\n\n"
    
    for tag, tag_agents in sorted(tag_groups.items()):
        tag_agents.sort(key=lambda x: x['score'], reverse=True)
        table += f"### {tag} ({len(tag_agents)})\n\n"
        table += "| # | Agent | Score | Stars | Status |\n"
        table += "|---|-------|-------|-------|--------|\n"
        
        for i, a in enumerate(tag_agents[:10], 1):
            stars_str = f"⭐ {a['stars']:,}" if a['stars'] > 0 else "—"
            table += f"| {i} | [{a['title']}]({a['rel_path']}) | {a['score']} | {stars_str} | {a['status']} |\n"
        
        table += "\n"
    
    return table

def generate_master_index():
    """Generate the complete Agent Master Index"""
    agents = scan_all_agents()
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    # Count statuses
    heating = len([a for a in agents if a['status'] == 'Heating Up'])
    stable = len([a for a in agents if a['status'] == 'Stable'])
    emerging = len([a for a in agents if a['status'] == 'Emerging'])
    
    content = f"""---
tags:
  - moc
  - agent
  - ai-tools
  - index
links:
  - "[[202609202000 - Claude Code]]"
  - "[[202609200758 - OpenCode]]"
  - "[[202609200759 - Hermes Agent]]"
---

# AI Agents — Master Index

*Comprehensive index of all trending AI coding agents — Last updated: {date_str}*

**Total agents tracked:** {len(agents)}
**Heating Up:** {heating} | **Stable:** {stable} | **Emerging:** {emerging}

---

## 📋 Table of Contents

1. [Top 5 Trending Agents](#top-5-trending-agents)
2. [Complete Agent List](#complete-agent-list)
3. [By Status](#by-status)
4. [By Category](#by-category)
5. [Statistics](#statistics)

---

"""
    
    # Top 5
    content += generate_top5_table(agents)
    content += "---\n\n"
    
    # Complete list
    content += generate_complete_list(agents)
    content += "---\n\n"
    
    # By status
    content += generate_status_tables(agents)
    content += "---\n\n"
    
    # By category
    content += generate_tag_tables(agents)
    content += "---\n\n"
    
    # Stats
    content += f"""## 📈 Statistics

| Metric | Value |
|--------|-------|
| Total agents | {len(agents)} |
| Heating Up | {heating} |
| Stable | {stable} |
| Emerging | {emerging} |
| CLI agents | {len([a for a in agents if 'cli' in a['tags']])} |
| MCP-compatible | {len([a for a in agents if 'mcp' in a['tags']])} |
| With plugins | {len([a for a in agents if a['links_count'] > 2])} |

---

## 🔗 Related

- [README](../../README.md) — vault dashboard
- [03 - Agents/](.) — all agent notes
- [04 - Plugins](../04%20-%20Plugins/) — plugin documentation
- [04 - Plugins/00 - Plugin Master Index](../04%20-%20Plugins/00%20-%20Plugin%20Master%20Index.md) — plugin index
- [09 - Trend Radar](../09%20-%20Trend%20Radar/) — trend analysis
"""
    
    with open(INDEX_FILE, 'w') as f:
        f.write(content)
    
    print(f"Updated Agent Master Index: {len(agents)} agents tracked")
    print(f"  Heating Up: {heating}")
    print(f"  Stable: {stable}")
    print(f"  Emerging: {emerging}")
    
    # Show top 5
    sorted_agents = sorted(agents, key=lambda x: x['score'], reverse=True)
    print(f"\nTop 5:")
    for i, a in enumerate(sorted_agents[:5], 1):
        print(f"  {i}. {a['title']} (score: {a['score']}, status: {a['status']})")

if __name__ == '__main__':
    os.chdir(VAULT)
    generate_master_index()
