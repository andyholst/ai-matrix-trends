#!/usr/bin/env python3
"""
validate-links.py - Validate all wikilinks point to existing files.
Stage 1 of CI pipeline.
"""

import os
import re
import sys

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")

# Files to skip
SKIP_FILES = {
    'AGENTS.md',
    '.obsidian/templates/moc.md',
    '.obsidian/templates/agent-profile.md',
    '.obsidian/templates/plugin-profile.md',
    '.obsidian/templates/architecture-pattern.md',
    'scripts/daily-scan-prompt.md',
}

def build_file_map():
    """Build map of all existing files"""
    file_map = {}
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                fname = f.replace('.md', '')
                rel_path = os.path.relpath(os.path.join(root, f), VAULT_DIR)
                file_map[fname.lower()] = rel_path
                if ' - ' in fname:
                    title = fname.split(' - ', 1)[1]
                    file_map[title.lower()] = rel_path
    return file_map

def validate_file(filepath, file_map):
    """Validate all links in a single file"""
    errors = []
    
    # Skip template files
    if any(skip in filepath for skip in SKIP_FILES):
        return errors
    
    # Skip index files (they have different link structure)
    if '00 -' in filepath or 'Master Index' in filepath:
        return errors
    
    with open(filepath) as f:
        content = f.read()
    
    # Check frontmatter links
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        fm = fm_match.group(1)
        links_match = re.search(r'^links:\n((?:\s*-\s*"\[\[.*?\]\]"\n?)+)', fm, re.MULTILINE)
        if links_match:
            links = re.findall(r'"\[\[(.*?)\]\]"', links_match.group(1))
            for link in links:
                if link.lower() not in file_map:
                    errors.append(f"  Frontmatter: [[{link}]] -> NOT FOUND")
    
    # Check body wikilinks
    body_sections = content.split('\n## ')
    for section in body_sections[1:]:
        links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', section)
        for link in links:
            link_lower = link.lower().strip()
            if link_lower not in file_map:
                # Skip template placeholders
                if '[' in link or ']' in link or '{{' in link:
                    continue
                # Skip folder links (end with /)
                if link.endswith('/'):
                    continue
                errors.append(f"  Body: [[{link}]] -> NOT FOUND")
    
    return errors

def main():
    print("STAGE 1: Link Validation")
    print("=" * 60)
    
    file_map = build_file_map()
    print(f"Built file map: {len(file_map)} entries")
    
    total_errors = 0
    files_with_errors = 0
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                errors = validate_file(filepath, file_map)
                if errors:
                    files_with_errors += 1
                    total_errors += len(errors)
                    rel_path = os.path.relpath(filepath, VAULT_DIR)
                    print(f"\n{rel_path}:")
                    for error in errors:
                        print(error)
    
    print(f"\n{'=' * 60}")
    print(f"Files with errors: {files_with_errors}")
    print(f"Total broken links: {total_errors}")
    
    if total_errors > 0:
        sys.exit(1)
    else:
        print("✓ All links valid")
        sys.exit(0)

if __name__ == '__main__':
    os.chdir(VAULT_DIR)
    main()