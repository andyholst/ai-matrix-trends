#!/usr/bin/env python3
"""
Aggregate trending data across all vault notes.
Scores trends based on mention frequency, source quality, and recency.
"""

import os
import re
import json
from datetime import datetime, timedelta
from collections import Counter

VAULT = os.path.expanduser("~/repository/git/ai-matrix-trends")
DATA_FILE = os.path.join(VAULT, "08 - Projects", "trend-data.json")

def extract_trends_from_notes():
    """Scan all notes for trending signals"""
    trends = Counter()
    sources = {}
    
    # Scan agents folder
    agents_dir = os.path.join(VAULT, "03 - Agents")
    if os.path.exists(agents_dir):
        for f in os.listdir(agents_dir):
            if f.endswith('.md'):
                path = os.path.join(agents_dir, f)
                with open(path) as fh:
                    content = fh.read()
                
                # Extract title
                title_match = re.search(r'^# (.+)', content, re.MULTILINE)
                if title_match:
                    name = title_match.group(1)
                    
                    # Count GitHub stars mentioned
                    stars = re.findall(r'(\d+)[,.]?(\d+)?[,.]?(\d+)?\+?\s*(?:stars?|⭐)', content)
                    stars_num = 0
                    if stars:
                        try:
                            stars_num = int(''.join([g for g in stars[0] if g]))
                        except:
                            pass
                    
                    # Count mentions
                    mentions = len(re.findall(r'\b' + re.escape(name) + r'\b', content, re.IGNORECASE))
                    
                    # Extract tags
                    tags_match = re.search(r'^tags:\n((?:\s*-\s*.+\n?)+)', content, re.MULTILINE)
                    tags = []
                    if tags_match:
                        tags = [t.strip().strip('-').strip() for t in tags_match.group(1).strip().split('\n')]
                    
                    # Score
                    score = 0
                    score += min(stars_num // 1000, 50)  # Max 50 from stars
                    score += mentions * 5  # 5 points per mention
                    if 'cli' in tags:
                        score += 10
                    if 'mcp' in tags:
                        score += 15
                    if 'trending' in tags:
                        score += 20
                    
                    trends[name] = score
                    sources[name] = {
                        'type': 'agent',
                        'stars': stars_num,
                        'mentions': mentions,
                        'tags': tags,
                        'score': score,
                        'file': f'03 - Agents/{f}'
                    }
    
    # Scan plugins folder
    plugins_dir = os.path.join(VAULT, "04 - Plugins")
    if os.path.exists(plugins_dir):
        for f in os.listdir(plugins_dir):
            if f == '00 - Plugin Master Index.md':
                continue
            if f.endswith('.md'):
                path = os.path.join(plugins_dir, f)
                with open(path) as fh:
                    content = fh.read()
                
                title_match = re.search(r'^# (.+)', content, re.MULTILINE)
                if title_match:
                    name = title_match.group(1)
                    
                    # Stars
                    stars = re.findall(r'(\d+)[,.]?(\d+)?[,.]?(\d+)?\+?\s*(?:stars?|⭐)', content)
                    stars_num = 0
                    if stars:
                        try:
                            stars_num = int(''.join([g for g in stars[0] if g]))
                        except:
                            pass
                    
                    # Mentions
                    mentions = len(re.findall(r'\b' + re.escape(name) + r'\b', content, re.IGNORECASE))
                    
                    # Tags
                    tags_match = re.search(r'^tags:\n((?:\s*-\s*.+\n?)+)', content, re.MULTILINE)
                    tags = []
                    if tags_match:
                        tags = [t.strip().strip('-').strip() for t in tags_match.group(1).strip().split('\n')]
                    
                    # Score
                    score = 0
                    score += min(stars_num // 500, 40)  # Max 40 from stars
                    score += mentions * 3
                    if 'mcp' in tags:
                        score += 20
                    if 'trending' in tags:
                        score += 25
                    
                    trends[name] = score
                    sources[name] = {
                        'type': 'plugin',
                        'stars': stars_num,
                        'mentions': mentions,
                        'tags': tags,
                        'score': score,
                        'file': f'04 - Plugins/{f}'
                    }
    
    return trends, sources

def get_top_trends(n=5):
    """Get top N trending items"""
    trends, sources = extract_trends_from_notes()
    top = trends.most_common(n)
    
    result = []
    for name, score in top:
        if name in sources:
            item = sources[name]
            item['name'] = name
            result.append(item)
    
    return result

def update_trend_radar():
    """Update Trend Radar with scored trends"""
    top = get_top_trends(10)
    
    # Separate into categories
    heating = []
    stable = []
    emerging = []
    
    for item in top:
        if item['score'] >= 50:
            heating.append(item)
        elif item['score'] >= 20:
            stable.append(item)
        else:
            emerging.append(item)
    
    # Update Trend Radar notes
    for item in heating:
        path = os.path.join(VAULT, "09 - Trend Radar", "Heating Up", f"{item['file'].split('/')[-1]}")
        if os.path.exists(path):
            with open(path) as f:
                content = f.read()
            # Update score in content
            content = re.sub(r'score:\s*\d+', f'score: {item["score"]}', content)
            with open(path, 'w') as f:
                f.write(content)

def main():
    print("AGGREGATING TRENDING DATA")
    print("=" * 60)
    
    trends, sources = extract_trends_from_notes()
    
    print(f"Total items tracked: {len(trends)}")
    print()
    
    # Top 10
    print("TOP 10 TRENDING:")
    for i, (name, score) in enumerate(trends.most_common(10), 1):
        item = sources[name]
        print(f"  {i}. {name} (score: {score}, type: {item['type']}, stars: {item['stars']})")
    
    # Update data file
    data = {
        'last_updated': datetime.now().isoformat(),
        'items': {name: sources[name] for name in trends}
    }
    
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"\nData saved to {DATA_FILE}")
    
    # Update Trend Radar
    update_trend_radar()
    print("Trend Radar updated")

if __name__ == '__main__':
    main()
