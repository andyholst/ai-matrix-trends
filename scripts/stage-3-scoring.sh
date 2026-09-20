#!/bin/bash
# Stage 3: Scoring & Aggregation
# Runs after link resolution
# Schedule: Daily at 20:45 (after Stage 2)

set -e

VAULT_DIR="$HOME/repository/git/ai-matrix-trends"
SCRIPTS_DIR="$VAULT_DIR/scripts"
cd "$VAULT_DIR"

echo "============================================"
echo "Stage 3: Scoring & Aggregation"
echo "$(date)"
echo "============================================"

echo "Step 3a: Aggregating trend scores..."
python3 "$SCRIPTS_DIR/aggregate-trends.py"

echo "Step 3b: Collecting agent plugins..."
python3 "$SCRIPTS_DIR/collect_agent_plugins.py"

echo "Stage 3 complete"