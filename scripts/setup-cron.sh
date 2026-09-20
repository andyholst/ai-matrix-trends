#!/usr/bin/env bash
# scripts/setup-cron.sh
# Sets up the daily AI Matrix Trends trend scan cron job.
# Run once after cloning the repo.
#
# Usage: bash scripts/setup-cron.sh

set -euo pipefail

VAULT_DIR="${HOME}/repository/git/ai-matrix-trends"
PROFILE="ai-matrix-trends"
SCHEDULE="0 20 * * *"
JOB_NAME="AI Matrix Trends - Daily Trend Scan"

PROMPT="You are the AI Matrix Trends vault agent.

1. Read ${VAULT_DIR}/AGENTS.md to understand vault structure, note templates, and rules.
2. Read ${VAULT_DIR}/scripts/daily-scan-prompt.md for the daily scan instructions.
3. Execute the workflow EXACTLY as described in the scan prompt file.

CRITICAL: After research streams complete, run these Python scripts in EXACT ORDER:
  1. cd ${VAULT_DIR} && python3 scripts/resolve_wikilinks.py
  2. cd ${VAULT_DIR} && python3 scripts/fix_all_links.py
  3. cd ${VAULT_DIR} && python3 scripts/aggregate-trends.py
  4. cd ${VAULT_DIR} && python3 scripts/collect_agent_plugins.py
  5. cd ${VAULT_DIR} && python3 scripts/update_readme.py
  6. cd ${VAULT_DIR} && python3 scripts/verify-vault.py
  7. cd ${VAULT_DIR} && python3 scripts/update-mocs.py

NEVER skip any script. NEVER change the order. NEVER delete files.

Vault path: ${VAULT_DIR}"

echo "→ Setting up cron job: ${JOB_NAME}"
echo "  Schedule: ${SCHEDULE} (daily at 20:00)"
echo "  Profile:  ${PROFILE}"
echo "  Vault:    ${VAULT_DIR}"
echo ""

# Check if job already exists
EXISTING="$(hermes cron list 2>/dev/null | grep -c "${JOB_NAME}" || true)"
if [[ "${EXISTING}" -gt 0 ]]; then
  echo "⚠ Cron job '${JOB_NAME}' already exists. Updating prompt..."
  hermes cron edit "$(hermes cron list --json 2>/dev/null | python3 -c "import sys,json; jobs=json.load(sys.stdin); print([j['id'] for j in jobs if j['name']=='${JOB_NAME}'][0])" 2>/dev/null || echo "5b0d68d1f40e")" \
    --prompt "${PROMPT}" \
    --deliver origin
  echo "✓ Cron job updated."
  exit 0
fi

hermes cron create "${SCHEDULE}" \
  --profile "${PROFILE}" \
  --prompt "${PROMPT}" \
  --name "${JOB_NAME}" \
  --deliver origin

echo ""
echo "✓ Cron job created. Run 'hermes cron list' to verify."
