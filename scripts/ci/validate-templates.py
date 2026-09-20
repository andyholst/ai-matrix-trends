#!/usr/bin/env python3
"""
validate-templates.py - Validate template files have correct structure.
Stage 7 of CI pipeline.
"""

import os
import re
import sys

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TEMPLATE_FILES = [
    '.obsidian/templates/moc.md',
    '.obsidian/templates/agent-profile.md',
    '.obsidian/templates/plugin-profile.md',
    '.obsidian/templates/architecture-pattern.md',
]

def validate_template(filepath):
    """Validate a template file"""
    errors = []
    
    if not os.path.exists(filepath):
        errors.append(f"  Template not found: {filepath}")
        return errors
    
    with open(filepath) as f:
        content = f.read()
    
    # Check for required sections
    if '# {{title}}' not in content and '# ' not in content:
        errors.append("  Missing title placeholder")
    
    if '## Overview' not in content:
        errors.append("  Missing Overview section")
    
    if '## Sources' not in content:
        errors.append("  Missing Sources section")
    
    return errors

def main():
    print("STAGE 7: Template Consistency")
    print("=" * 60)
    
    total_errors = 0
    
    for template in TEMPLATE_FILES:
        filepath = os.path.join(VAULT_DIR, template)
        errors = validate_template(filepath)
        if errors:
            total_errors += len(errors)
            print(f"\n{template}:")
            for error in errors:
                print(error)
    
    print(f"\n{'=' * 60}")
    if total_errors > 0:
        sys.exit(1)
    else:
        print("✓ All templates valid")
        sys.exit(0)

if __name__ == '__main__':
    os.chdir(VAULT_DIR)
    main()