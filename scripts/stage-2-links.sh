#!/bin/bash
# Stage 2: Link Resolution & Fixing
# Runs after research streams complete
# Schedule: Daily at 20:30 (after Stage 1)

set -e

VAULT_DIR="$HOME/repository/git/ai-matrix-trends"
SCRIPTS_DIR="$VAULT_DIR/scripts"
cd "$VAULT_DIR"

echo "============================================"
echo "Stage 2: Link Resolution & Fixing"
echo "$(date)"
echo "============================================"

echo "Step 2a: Resolving wikilinks..."
python3 "$SCRIPTS_DIR/resolve_wikilinks.py"

echo "Step 2b: Fixing broken links..."
python3 "$SCRIPTS_DIR/fix_all_links.py"

echo "Step 2c: Verifying vault links..."
python3 "$SCRIPTS_DIR/verify-vault.py"

echo "Stage 2 complete"