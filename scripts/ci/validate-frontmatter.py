#!/usr/bin/env python3
"""
validate-frontmatter.py - Validate frontmatter structure and deduplicate links.
Stage 2 of CI pipeline.
"""

import os
import re
import sys
from collections import Counter

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Files to skip
SKIP_FILES = {
    'AGENTS.md',
    '.obsidian/templates/moc.md',
    '.obsidian/templates/agent-profile.md',
    '.obsidian/templates/plugin-profile.md',
    '.obsidian/templates/architecture-pattern.md',
    '.obsidian/templates/atomic-note.md',
    'scripts/daily-scan-prompt.md',
}

def validate_file(filepath):
    """Validate frontmatter of a single file"""
    errors = []
    
    if any(skip in filepath for skip in SKIP_FILES):
        return errors
    
    with open(filepath) as f:
        content = f.read()
    
    # Check frontmatter exists
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        if not filepath.endswith('README.md') and not filepath.endswith('AGENTS.md'):
            errors.append("  Missing frontmatter")
        return errors
    
    fm = fm_match.group(1)
    
    # Check for duplicate links
    links_match = re.search(r'^links:\n((?:\s*-\s*"\[\[.*?\]\]"\n?)+)', fm, re.MULTILINE)
    if links_match:
        links = re.findall(r'"\[\[(.*?)\]\]"', links_match.group(1))
        link_counts = Counter(links)
        duplicates = {l: c for l, c in link_counts.items() if c > 1}
        if duplicates:
            errors.append(f"  Duplicate links: {duplicates}")
    
    return errors

def main():
    print("STAGE 2: Frontmatter Validation")
    print("=" * 60)
    
    total_errors = 0
    files_with_errors = 0
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                errors = validate_file(filepath)
                if errors:
                    files_with_errors += 1
                    total_errors += len(errors)
                    rel_path = os.path.relpath(filepath, VAULT_DIR)
                    print(f"\n{rel_path}:")
                    for error in errors:
                        print(error)
    
    print(f"\n{'=' * 60}")
    print(f"Files with errors: {files_with_errors}")
    print(f"Total errors: {total_errors}")
    
    if total_errors > 0:
        sys.exit(1)
    else:
        print("✓ All frontmatter valid")
        sys.exit(0)

if __name__ == '__main__':
    os.chdir(VAULT_DIR)
    main()