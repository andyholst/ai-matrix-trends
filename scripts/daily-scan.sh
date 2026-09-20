#!/bin/bash
# AI Matrix Trends - Daily Scan
# Runs all 4 stages sequentially
# Schedule: Daily at 20:00

set -e

VAULT_DIR="$HOME/repository/git/ai-matrix-trends"
SCRIPTS_DIR="$VAULT_DIR/scripts"
cd "$VAULT_DIR"

echo "============================================"
echo "AI Matrix Trends - Daily Scan"
echo "$(date)"
echo "============================================"

# Stage 1: Research (create notes directly via Python)
echo ""
echo "Stage 1: Research..."
python3 "$SCRIPTS_DIR/stage-1-research.py"

# Stage 2: Link Resolution
echo ""
echo "Stage 2: Link Resolution..."
python3 "$SCRIPTS_DIR/resolve_wikilinks.py"
python3 "$SCRIPTS_DIR/fix_all_links.py"
python3 "$SCRIPTS_DIR/verify-vault.py"

# Stage 3: Scoring
echo ""
echo "Stage 3: Scoring..."
python3 "$SCRIPTS_DIR/aggregate-trends.py"
python3 "$SCRIPTS_DIR/collect_agent_plugins.py"

# Stage 4: Indexes & Commit
echo ""
echo "Stage 4: Indexes & Commit..."
python3 "$SCRIPTS_DIR/update-mocs.py"
python3 "$SCRIPTS_DIR/update-plugin-master-index.py"
python3 "$SCRIPTS_DIR/update-agent-master-index.py"
python3 "$SCRIPTS_DIR/update_readme.py"
python3 "$SCRIPTS_DIR/fix-master-index-links.py"
python3 "$SCRIPTS_DIR/verify-vault.py"

echo ""
echo "Committing and pushing..."
git add -A
git commit -m "Daily scan: $(date +%Y-%m-%d)"
git push

echo ""
echo "============================================"
echo "Daily scan complete!"
echo "============================================"