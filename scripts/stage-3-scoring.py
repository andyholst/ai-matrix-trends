#!/usr/bin/env python3
"""
Stage 3: Scoring & Aggregation
Runs after link resolution.
Schedule: Daily at 20:45 (after Stage 2)
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
    print("Stage 3: Scoring & Aggregation")
    print("=" * 60)

    print("\nStep 3a: Aggregating trend scores...")
    run("aggregate-trends.py")

    print("\nStep 3b: Collecting agent plugins...")
    run("collect_agent_plugins.py")

    print("\nStage 3 complete")

if __name__ == '__main__':
    main()
