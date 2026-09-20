#!/usr/bin/env python3
"""
validate-formatting.py - Validate markdown formatting consistency.
Stage 8 of CI pipeline.
"""

import os
import re
import sys

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Files to skip
SKIP_FILES = {
    'AGENTS.md',
    'README.md',
    'LICENSE',
    'daily-scan-prompt.md',
}

# Directories to skip
SKIP_DIRS = {
    '.obsidian',
}

def validate_file(filepath):
    """Validate formatting of a single file"""
    errors = []
    
    # Skip certain files
    if any(skip in filepath for skip in SKIP_FILES):
        return errors
    
    # Skip template directories
    if any(skip in filepath for skip in SKIP_DIRS):
        return errors
    
    # Skip index files
    if '00 -' in filepath or 'Master Index' in filepath:
        return errors
    
    with open(filepath) as f:
        content = f.read()
    
    # Check frontmatter exists
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        errors.append("  Missing frontmatter")
        return errors
    
    # Check for empty lines before frontmatter
    if not content.startswith('---'):
        errors.append("  Frontmatter must start at beginning of file")
    
    # Check for proper heading hierarchy (allow ## to ### jumps)
    headings = re.findall(r'^(#+)\s+(.+)$', content, re.MULTILINE)
    prev_level = 0
    for level_str, title in headings:
        level = len(level_str)
        # Only flag jumps greater than 1 level (e.g., # to ###)
        if level > prev_level + 1 and prev_level > 0:
            errors.append(f"  Heading level jump: {level_str} {title}")
        prev_level = level
    
    # Check for trailing whitespace
    for i, line in enumerate(content.split('\n'), 1):
        if line.rstrip() != line:
            errors.append(f"  Trailing whitespace on line {i}")
    
    # Check for multiple consecutive blank lines
    if '\n\n\n' in content:
        errors.append("  Multiple consecutive blank lines")
    
    return errors

def main():
    print("STAGE 8: Markdown Formatting")
    print("=" * 60)
    
    total_errors = 0
    files_with_errors = 0
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        # Skip template directories
        if any(skip in root for skip in SKIP_DIRS):
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
        print("✓ All files properly formatted")
        sys.exit(0)

if __name__ == '__main__':
    main()