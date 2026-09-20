#!/bin/bash
# Stage 4: Indexes & MOCs
# Runs after scoring
# Schedule: Daily at 21:00 (after Stage 3)

set -e

VAULT_DIR="$HOME/repository/git/ai-matrix-trends"
SCRIPTS_DIR="$VAULT_DIR/scripts"
cd "$VAULT_DIR"

echo "============================================"
echo "Stage 4: Indexes & MOCs"
echo "$(date)"
echo "============================================"

echo "Step 4a: Updating MOCs..."
python3 "$SCRIPTS_DIR/update-mocs.py"

echo "Step 4b: Updating Plugin Master Index..."
python3 "$SCRIPTS_DIR/update-plugin-master-index.py"

echo "Step 4c: Updating Agent Master Index..."
python3 "$SCRIPTS_DIR/update-agent-master-index.py"

echo "Step 4d: Updating README..."
python3 "$SCRIPTS_DIR/update_readme.py"

echo "Step 4e: Fixing Master Index links..."
python3 "$SCRIPTS_DIR/fix-master-index-links.py"

echo "Step 4f: Final verification..."
python3 "$SCRIPTS_DIR/verify-vault.py"

echo "Step 4g: Committing and pushing..."
git add -A
git commit -m "Daily scan: $(date +%Y-%m-%d)"
git push

echo "Stage 4 complete"