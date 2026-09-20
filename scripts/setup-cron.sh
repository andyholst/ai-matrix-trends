#!/bin/bash
# scripts/setup-cron.sh
# Sets up the AI Matrix Trends daily scan cron jobs.
# Creates separate cron jobs for each stage.
# Run once after cloning the repo.

set -euo pipefail

VAULT_DIR="${HOME}/repository/git/ai-matrix-trends"
PROFILE="ai-matrix-trends"
HERMES_SCRIPTS_DIR="${HOME}/hermes/profiles/${PROFILE}/scripts"

echo "→ Setting up AI Matrix Trends cron jobs"
echo "  Profile: ${PROFILE}"
echo "  Vault:   ${VAULT_DIR}"
echo ""

# Ensure Hermes scripts directory exists
mkdir -p "${HERMES_SCRIPTS_DIR}"

# Copy stage scripts to Hermes profile
echo "→ Copying stage scripts to ${HERMES_SCRIPTS_DIR}/"
for script in stage-2-links.py stage-3-scoring.py stage-4-indexes.py; do
  cp -f "${VAULT_DIR}/scripts/${script}" "${HERMES_SCRIPTS_DIR}/${script}"
  chmod +x "${HERMES_SCRIPTS_DIR}/${script}"
  echo "  ✓ Copied ${script}"
done

# Copy CI scripts (used by stage-4 as safety-net link fixer)
echo "→ Copying CI scripts to ${HERMES_SCRIPTS_DIR}/ci/"
mkdir -p "${HERMES_SCRIPTS_DIR}/ci"
for script in fix-links-relative.py validate-links.py validate-link-quality.py; do
  cp -f "${VAULT_DIR}/scripts/ci/${script}" "${HERMES_SCRIPTS_DIR}/ci/${script}"
  chmod +x "${HERMES_SCRIPTS_DIR}/ci/${script}"
  echo "  ✓ Copied ci/${script}"
done
echo ""

# ===== STAGE 1: Research (0 20 * * *) =====
# Stage 1 is agent-based (needs delegate_task to spawn sub-agents)
echo "→ Stage 1: Research streams (20:00)"
EXISTING1="$(hermes cron list --profile ai-matrix-trends 2>/dev/null | grep -c 'Trends.*Stage 1' || true)"
if [[ "${EXISTING1}" -gt 0 ]]; then
  echo "  ⚠ Stage 1 job exists, skipping."
else
  hermes cron create '0 20 * * *' \
    --profile "${PROFILE}" \
    --name 'Trends Stage 1 - Research' \
    --deliver origin \
    "You are the AI Matrix Trends vault agent. Read ${VAULT_DIR}/AGENTS.md for vault rules. Read ${VAULT_DIR}/scripts/daily-scan-prompt.md for scan workflow. Execute Stage 1: Launch 4 parallel research streams via delegate_task (Streams A: Agents, B: Plugins for ALL 50+ agents, C: Architecture, D: Use Cases). Each sub-agent must use FULL FILENAMES for wikilinks like [[202609202000 - Claude Code]]. After all streams complete, report summary."
  echo "  ✓ Stage 1 created"
fi

# ===== STAGE 2: Link Resolution (30 20 * * *) =====
echo "→ Stage 2: Link resolution (20:30)"
EXISTING2="$(hermes cron list --profile ai-matrix-trends 2>/dev/null | grep -c 'Trends.*Stage 2' || true)"
if [[ "${EXISTING2}" -gt 0 ]]; then
  echo "  ⚠ Stage 2 job exists, skipping."
else
  hermes cron create '30 20 * * *' \
    --profile "${PROFILE}" \
    --name 'Trends Stage 2 - Links' \
    --script "stage-2-links.py" \
    --no-agent \
    --deliver origin
  echo "  ✓ Stage 2 created"
fi

# ===== STAGE 3: Scoring (45 20 * * *) =====
echo "→ Stage 3: Scoring (20:45)"
EXISTING3="$(hermes cron list --profile ai-matrix-trends 2>/dev/null | grep -c 'Trends.*Stage 3' || true)"
if [[ "${EXISTING3}" -gt 0 ]]; then
  echo "  ⚠ Stage 3 job exists, skipping."
else
  hermes cron create '45 20 * * *' \
    --profile "${PROFILE}" \
    --name 'Trends Stage 3 - Scoring' \
    --script "stage-3-scoring.py" \
    --no-agent \
    --deliver origin
  echo "  ✓ Stage 3 created"
fi

# ===== STAGE 4: Indexes & Commit (0 21 * * *) =====
echo "→ Stage 4: Indexes & commit (21:00)"
EXISTING4="$(hermes cron list --profile ai-matrix-trends 2>/dev/null | grep -c 'Trends.*Stage 4' || true)"
if [[ "${EXISTING4}" -gt 0 ]]; then
  echo "  ⚠ Stage 4 job exists, skipping."
else
  hermes cron create '0 21 * * *' \
    --profile "${PROFILE}" \
    --name 'Trends Stage 4 - Indexes' \
    --script "stage-4-indexes.py" \
    --no-agent \
    --deliver origin
  echo "  ✓ Stage 4 created"
fi

echo ""
echo "✓ All 4 cron jobs configured"
echo "  20:00 - Stage 1: Research (parallel sub-agents)"
echo "  20:30 - Stage 2: Link resolution & verification"
echo "  20:45 - Stage 3: Scoring & aggregation"
echo "  21:00 - Stage 4: Indexes, MOCs, README, commit & push"