#!/usr/bin/env python3
"""
ci-pipeline.py - Main CI pipeline for AI Matrix Trends vault.
Validates all markdown files and reports issues.
Exit code 0 = green, 1 = red.
"""

import subprocess
import sys
import os

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")
CI_DIR = os.path.join(VAULT_DIR, "scripts", "ci")

STAGES = [
    ("Stage 1: Link Validation", "validate-links.py"),
    ("Stage 2: Frontmatter Validation", "validate-frontmatter.py"),
    ("Stage 3: Duplicate Detection", "validate-duplicates.py"),
    ("Stage 4: Tag Validation", "validate-tags.py"),
]

def main():
    print("=" * 60)
    print("AI MATRIX TRENDS - CI PIPELINE")
    print("=" * 60)
    
    all_passed = True
    
    for stage_name, script in STAGES:
        print(f"\n{'=' * 60}")
        print(stage_name)
        print('=' * 60)
        
        result = subprocess.run(
            [sys.executable, os.path.join(CI_DIR, script)],
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
    os.chdir(VAULT_DIR)
    main()