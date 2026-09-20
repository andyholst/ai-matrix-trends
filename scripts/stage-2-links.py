#!/usr/bin/env python3
"""
Stage 2: Link Resolution & Fixing
Runs after research streams complete.
Schedule: Daily at 20:30 (after Stage 1)
"""

import subprocess
import sys
import os

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")
SCRIPTS_DIR = os.path.join(VAULT_DIR, "scripts")

def run(script):
    """Run a Python script and check for errors"""
    result = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS_DIR, script)],
        cwd=VAULT_DIR,
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if result.returncode != 0:
        print(f"ERROR: {script} failed with code {result.returncode}")
        sys.exit(1)

def main():
    print("=" * 60)
    print("Stage 2: Link Resolution & Fixing")
    print("=" * 60)

    print("\nStep 2a: Resolving wikilinks...")
    run("resolve_wikilinks.py")

    print("\nStep 2b: Fixing broken links...")
    run("fix_all_links.py")

    print("\nStep 2c: Verifying vault links...")
    run("verify-vault.py")

    print("\nStage 2 complete")

if __name__ == '__main__':
    main()
