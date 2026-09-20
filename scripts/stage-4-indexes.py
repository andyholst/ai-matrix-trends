#!/usr/bin/env python3
"""
Stage 4: Indexes, MOCs, README & Commit
Runs after scoring.
Schedule: Daily at 21:00 (after Stage 3)
"""

import subprocess
import sys
import os
from datetime import datetime

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

def run_shell(cmd):
    """Run a shell command and check for errors"""
    result = subprocess.run(
        cmd,
        cwd=VAULT_DIR,
        capture_output=True,
        text=True,
        shell=True
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if result.returncode != 0:
        print(f"ERROR: command failed: {cmd}")
        sys.exit(1)

def main():
    print("=" * 60)
    print("Stage 4: Indexes, MOCs, README & Commit")
    print("=" * 60)

    print("\nStep 4a: Updating MOCs...")
    run("update-mocs.py")

    print("\nStep 4b: Updating Plugin Master Index...")
    run("update-plugin-master-index.py")

    print("\nStep 4c: Updating Agent Master Index...")
    run("update-agent-master-index.py")

    print("\nStep 4d: Updating README...")
    run("update_readme.py")

    print("\nStep 4e: Fixing Master Index links...")
    run("fix-master-index-links.py")

    print("\nStep 4f: Final verification...")
    run("verify-vault.py")

    print("\nStep 4g: Committing and pushing...")
    today = datetime.now().strftime('%Y-%m-%d')
    run_shell("git add -A")
    run_shell(f"git commit -m 'Daily scan: {today}'")
    run_shell("git push")

    print("\nStage 4 complete - daily scan finished!")

if __name__ == '__main__':
    main()
