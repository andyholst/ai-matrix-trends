#!/usr/bin/env python3
"""
validate-link-quality.py - Validate quality of frontmatter links.
Stage 9 of CI pipeline.
FAILS when links contain MOC references or other non-note links.
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))

# Files to skip
SKIP_FILES = [
    'AGENTS.md',
    'README.md', 
    'LICENSE',
    'daily-scan-prompt.md',
]

SKIP_FOLDERS = [
    '.obsidian',
    'scripts/ci',
    '00 - Inbox',
]

# Patterns that indicate non-note links (fishy)
FISHY_PATTERNS = [
    'MOC-',           # MOC references belong in body, not frontmatter links
    'MOC:',           # MOC colon format
]

def validate_file(filepath):
    """Check if file has fishy frontmatter links"""
    errors = []
    
    # Skip certain files
    for skip in SKIP_FILES:
        if skip in filepath:
            return errors
    
    # Skip certain folders
    for folder in SKIP_FOLDERS:
        if folder in filepath:
            return errors
    
    with open(filepath) as f:
        content = f.read()
    
    # Parse frontmatter
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return errors
    
    fm = fm_match.group(1)
    
    # Find links section
    links_match = re.search(r'^links:\n((?:\s*-\s*"\[\[.*?\]\]"\n?)+)', fm, re.MULTILINE)
    if not links_match:
        return errors
    
    links = re.findall(r'"\[\[(.*?)\]\]"', links_match.group(1))
    
    for link in links:
        # Check for fishy patterns
        for pattern in FISHY_PATTERNS:
            if pattern in link:
                errors.append(f"  Fishy link: [[{link}]] (contains '{pattern}' - MOCs should be in body, not frontmatter)")
    
    return errors

def main():
    print("STAGE 9: Link Quality Validation")
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
    print(f"Files with fishy links: {files_with_errors}")
    print(f"Total fishy links: {total_errors}")
    
    if total_errors > 0:
        print(f"✗ FAIL: {total_errors} fishy links detected")
        print("  MOC references should be in body (## Related), not frontmatter links:")
        sys.exit(1)
    else:
        print("✓ All links are high quality")
        sys.exit(0)

if __name__ == '__main__':
    main()