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
3. Execute the workflow exactly as described in the scan prompt file.

Vault path: ${VAULT_DIR}"

echo "→ Setting up cron job: ${JOB_NAME}"
echo "  Schedule: ${SCHEDULE} (daily at 20:00)"
echo "  Profile:  ${PROFILE}"
echo "  Vault:    ${VAULT_DIR}"
echo ""

# Check if job already exists
EXISTING="$(hermes cron list 2>/dev/null | grep -c "${JOB_NAME}" || true)"
if [[ "${EXISTING}" -gt 0 ]]; then
  echo "⚠ Cron job '${JOB_NAME}' already exists. Skipping."
  echo "  Run 'hermes cron list' to view existing jobs."
  exit 0
fi

hermes cron create "${SCHEDULE}" \
  --profile "${PROFILE}" \
  --prompt "${PROMPT}" \
  --name "${JOB_NAME}" \
  --deliver all

echo ""
echo "✓ Cron job created. Run 'hermes cron list' to verify."
