#!/usr/bin/env python3
"""
ci-pipeline.py - Main CI pipeline for AI Matrix Trends vault.
Uses relative paths to work in any environment.
Exit code 0 = green, 1 = red.
"""

import subprocess
import sys
import os

# Use the directory where this script lives as the CI dir
CI_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.dirname(CI_DIR)

STAGES = [
    ("Stage 1: Link Validation", "validate-links.py"),
    ("Stage 2: Frontmatter Validation", "validate-frontmatter.py"),
    ("Stage 3: Duplicate Detection", "validate-duplicates.py"),
    ("Stage 4: Tag Validation", "validate-tags.py"),
    ("Stage 5: Index Completeness", "validate-index-completeness.py"),
    ("Stage 6: Orphan Detection", "validate-orphans.py"),
    ("Stage 7: Template Consistency", "validate-templates.py"),
    ("Stage 8: Markdown Formatting", "validate-formatting.py"),
]

def main():
    print("=" * 60)
    print("AI MATRIX TRENDS - CI PIPELINE")
    print(f"Vault: {VAULT_DIR}")
    print("=" * 60)
    
    all_passed = True
    
    for stage_name, script in STAGES:
        script_path = os.path.join(CI_DIR, script)
        if not os.path.exists(script_path):
            print(f"\n⚠ Script not found: {script}")
            continue
            
        print(f"\n{'=' * 60}")
        print(stage_name)
        print('=' * 60)
        
        result = subprocess.run(
            [sys.executable, script_path],
            cwd=VAULT_DIR,
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        
        if result.returncode != 0:
            all_passed = False
            print(f"✗ {stage_name} FAILED")
        else:
            print(f"✓ {stage_name} PASSED")
    
    print(f"\n{'=' * 60}")
    if all_passed:
        print("✓ ALL STAGES PASSED - PIPELINE GREEN")
        sys.exit(0)
    else:
        print("✗ PIPELINE RED")
        sys.exit(1)

if __name__ == '__main__':
    main()