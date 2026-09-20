#!/usr/bin/env python3
"""
update_readme.py - Update README.md with comprehensive scored trend tables.
Run AFTER aggregate-trends.py to populate all tables.

This script is idempotent — it cleans up any duplicate sections before writing.
"""

import os
import re
import json
from datetime import datetime

VAULT = os.path.expanduser("~/repository/git/ai-matrix-trends")
DATA_FILE = os.path.join(VAULT, "08 - Projects", "trend-data.json")

def load_trend_data():
    """Load trend data from JSON"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {'items': {}}

def get_top_items(item_type, n=5):
    """Get top N items for a type"""
    data = load_trend_data()
    items = data.get('items', {})
    
    # Filter by type
    filtered = {k: v for k, v in items.items() if v.get('type') == item_type}
    
    # Sort by score
    sorted_items = sorted(filtered.items(), key=lambda x: x[1].get('score', 0), reverse=True)
    
    return sorted_items[:n]

def generate_table_header():
    """Generate Markdown table header"""
    return "| # | Name | Score | Type | Stars | Status |\n|---|------|-------|------|-------|--------|"

def generate_table_row(i, name, item):
    """Generate a Markdown table row"""
    score = item.get('score', 0)
    item_type = item.get('type', 'unknown')
    stars = item.get('stars', '—')
    
    # Determine status based on score
    if score >= 50:
        status = "Heating Up"
    elif score >= 20:
        status = "Stable"
    else:
        status = "Emerging"
    
    # Extract title from filename
    filename = item.get('file', '')
    title = os.path.basename(filename).replace('.md', '')
    
    encoded = filename.replace(' ', '%20')
    return f"| {i} | [{title}](./{encoded}) | {score} | {item_type} | {stars} | {status} |"

def clean_duplicates(content):
    """Remove duplicate sections, keeping only the first occurrence of each."""
    # Find all section headers and their positions
    headers = [(m.start(), m.group()) for m in re.finditer(r'^## .+', content, re.MULTILINE)]
    
    seen = set()
    to_remove = []
    
    for pos, header in headers:
        # Normalize header for comparison (remove emojis for matching)
        normalized = re.sub(r'[^\w\s]', '', header).strip().lower()
        if normalized in seen:
            to_remove.append((pos, header))
        else:
            seen.add(normalized)
    
    # Remove duplicates (from end to start to preserve positions)
    for pos, header in reversed(to_remove):
        # Find where this duplicate section ends (next ## or end)
        next_section = content.find('\n## ', pos + 1)
        if next_section == -1:
            next_section = len(content)
        content = content[:pos] + content[next_section:]
    
    return content

def update_readme():
    """Update README.md with scored trend tables"""
    os.chdir(VAULT)
    
    # Read current README
    with open(os.path.join(VAULT, 'README.md')) as f:
        content = f.read()
    
    # Clean up any duplicate sections first
    content = clean_duplicates(content)
    
    # Get top items for each category
    agents = get_top_items('agent', 5)
    plugins = get_top_items('plugin', 5)
    
    print(f"Top 5 Agents: {[a[0] for a in agents]}")
    print(f"Top 5 Plugins: {[p[0] for p in plugins]}")
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    # Build new Trending Agents section
    agents_section = f"""## 🚀 Trending Agents

*Top 5 scored trending — Last updated: {date_str}*

{generate_table_header()}
"""
    for i, (name, item) in enumerate(agents, 1):
        agents_section += generate_table_row(i, name, item) + "\n"
    agents_section += "\n"
    
    # Build new Plugins section
    plugins_section = f"""## 🔌 Top Plugins & Extensions

*Top 5 scored trending — Last updated: {date_str}*

{generate_table_header()}
"""
    for i, (name, item) in enumerate(plugins, 1):
        plugins_section += generate_table_row(i, name, item) + "\n"
    plugins_section += "\n"
    
    # Build new Trend Radar section
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

if __name__ == '__main__':
    update_readme()
