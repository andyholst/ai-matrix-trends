#!/usr/bin/env python3
"""
Update README.md with current vault state.
Run after fix-links.py and update-mocs.py.
"""

import os
import re

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")

def get_notes_in_folder(folder):
    """Get all .md files in folder, sorted"""
    folder_path = os.path.join(VAULT_DIR, folder)
    if not os.path.exists(folder_path):
        return []
    return sorted([f.replace('.md', '') for f in os.listdir(folder_path) if f.endswith('.md')])

def format_readme_link(text, path):
    """Format a Markdown link for README"""
    encoded_path = path.replace(' ', '%20')
    return f"[text](./{encoded_path})"

def update_readme():
    """Update README.md"""
    readme_path = os.path.join(VAULT_DIR, 'README.md')
    
    # Read current README
    with open(readme_path) as f:
        content = f.read()
    
    # Update Trend Radar section
    heating_up = get_notes_in_folder('09 - Trend Radar/Heating Up')
    stable = get_notes_in_folder('09 - Trend Radar/Stable')
    emerging = get_notes_in_folder('09 - Trend Radar/Emerging')
    
    # Update Heating Up table
    for note in heating_up:
        # Extract title
        if ' - ' in note:
            title = note.split(' - ', 1)[1]
        else:
            title = note
        # Check if already in README
        if title not in content:
            # Add to Trend Radar Heating Up
            path = f'09 - Trend Radar/Heating Up/{note}.md'
            link = f'[{title}](./{path.replace(" ", "%20")})'
            # Find the Heating Up section and add
            if '### Heating Up 🔥' in content:
                # Add after the header
                idx = content.index('### Heating Up 🔥')
                # Find the end of the section
                next_section = content.find('### ', idx + 1)
                if next_section > 0:
                    content = content[:next_section] + f'- {link} - Trending\n' + content[next_section:]
    
    # Update date
    content = re.sub(r'\*Last refreshed: .*\*', f'*Last refreshed: {os.popen("date +%Y-%m-%d").read().strip()}*', content)
    
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"Updated README.md")

def main():
    print("UPDATING README")
    print("=" * 60)
    os.chdir(VAULT_DIR)
    update_readme()

if __name__ == '__main__':
    main()
