#!/usr/bin/env python3
"""
update_readme.py - Update README.md with comprehensive scored trend tables.
Run AFTER aggregate-trends.py to populate all tables.
"""

import os
import re
import json
from datetime import datetime
from collections import Counter

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

def update_readme():
    """Update README.md with scored trend tables"""
    os.chdir(VAULT)
    
    # Read current README
    with open(os.path.join(VAULT, 'README.md')) as f:
        content = f.read()
    
    # Get top items for each category
    agents = get_top_items('agent', 5)
    plugins = get_top_items('plugin', 5)
    
    print(f"Top 5 Agents: {[a[0] for a in agents]}")
    print(f"Top 5 Plugins: {[p[0] for p in plugins]}")
    
    # Update Trending Agents section
    if '## Trending Agents' in content:
        # Find and replace the table
        pattern = r'(## Trending Agents\n.*?)(?=\n## |\Z)'
        
        new_section = "## Trending Agents\n\n"
        new_section += f"*Top 5 scored trending - Last updated: {datetime.now().strftime('%Y-%m-%d')}*\n\n"
        new_section += generate_table_header() + "\n"
        
        for i, (name, item) in enumerate(agents, 1):
            new_section += generate_table_row(i, name, item) + "\n"
        
        new_section += "\n"
        
        content = re.sub(pattern, new_section, content, flags=re.DOTALL)
    
    # Update Plugins section
    if '## Top Plugins' in content:
        pattern = r'(## Top Plugins.*?\n.*?)(?=\n## |\Z)'
        
        new_section = "## Top Plugins & Extensions\n\n"
        new_section += f"*Top 5 scored trending - Last updated: {datetime.now().strftime('%Y-%m-%d')}*\n\n"
        new_section += generate_table_header() + "\n"
        
        for i, (name, item) in enumerate(plugins, 1):
            new_section += generate_table_row(i, name, item) + "\n"
        
        new_section += "\n"
        
        content = re.sub(pattern, new_section, content, flags=re.DOTALL)
    
    # Update Trend Radar
    data = load_trend_data()
    items = data.get('items', {})
    
    # Sort all items by score
    all_sorted = sorted(items.items(), key=lambda x: x[1].get('score', 0), reverse=True)
    
    heating_up = [(k, v) for k, v in all_sorted if v.get('score', 0) >= 50][:5]
    stable = [(k, v) for k, v in all_sorted if 20 <= v.get('score', 0) < 50][:5]
    emerging = [(k, v) for k, v in all_sorted if v.get('score', 0) < 20][:5]
    
    trend_section = "## Trend Radar\n\n"
    trend_section += f"*Last updated: {datetime.now().strftime('%Y-%m-%d')}*\n\n"
    
    trend_section += "### Heating Up\n\n"
    trend_section += generate_table_header() + "\n"
    for i, (name, item) in enumerate(heating_up, 1):
        trend_section += generate_table_row(i, name, item) + "\n"
    
    trend_section += "\n### Stable\n\n"
    trend_section += generate_table_header() + "\n"
    for i, (name, item) in enumerate(stable, 1):
        trend_section += generate_table_row(i, name, item) + "\n"
    
    trend_section += "\n### Emerging\n\n"
    trend_section += generate_table_header() + "\n"
    for i, (name, item) in enumerate(emerging, 1):
        trend_section += generate_table_row(i, name, item) + "\n"
    
    # Replace or add Trend Radar section
    if '## Trend Radar' in content:
        pattern = r'(## Trend Radar\n)(.*?)(?=\n## |\Z)'
        content = re.sub(pattern, trend_section, content, flags=re.DOTALL)
    else:
        content += trend_section
    
    # Update date
    content = re.sub(r'\*Last refreshed: .*\*', f'*Last refreshed: {datetime.now().strftime("%Y-%m-%d")}*', content)
    
    with open(os.path.join(VAULT, 'README.md'), 'w') as f:
        f.write(content)
    
    print("README.md updated with scored tables")

if __name__ == '__main__':
    update_readme()
