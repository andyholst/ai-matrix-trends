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

# Symlink stage scripts to Hermes profile
echo "→ Symlinking stage scripts to ${HERMES_SCRIPTS_DIR}/"
for script in stage-1-research.sh stage-2-links.sh stage-3-scoring.sh stage-4-indexes.sh; do
  src="${VAULT_DIR}/scripts/${script}"
  dest="${HERMES_SCRIPTS_DIR}/${script}"
  if [[ -L "${dest}" ]]; then
    rm "${dest}"
  elif [[ -f "${dest}" ]]; then
    echo "  ⚠ ${script} already exists, skipping"
    continue
  fi
  ln -s "${src}" "${dest}"
  echo "  ✓ Linked ${script}"
done
echo ""

# ===== STAGE 1: Research (0 20 * * *) =====
echo "→ Stage 1: Research streams (20:00)"
EXISTING1="$(hermes cron list 2>/dev/null | grep -c 'Trends.*Stage 1' || true)"
if [[ "${EXISTING1}" -gt 0 ]]; then
  echo "  ⚠ Stage 1 job exists, skipping."
else
  hermes cron create '0 20 * * *' \
    --profile "${PROFILE}" \
    --name 'Trends Stage 1 - Research' \
    --script "stage-1-research.sh" \
    --no-agent \
    --deliver origin
  echo "  ✓ Stage 1 created"
fi

# ===== STAGE 2: Link Resolution (30 20 * * *) =====
echo "→ Stage 2: Link resolution (20:30)"
EXISTING2="$(hermes cron list 2>/dev/null | grep -c 'Trends.*Stage 2' || true)"
if [[ "${EXISTING2}" -gt 0 ]]; then
  echo "  ⚠ Stage 2 job exists, skipping."
else
  hermes cron create '30 20 * * *' \
    --profile "${PROFILE}" \
    --name 'Trends Stage 2 - Links' \
    --script "stage-2-links.sh" \
    --no-agent \
    --deliver origin
  echo "  ✓ Stage 2 created"
fi

# ===== STAGE 3: Scoring (45 20 * * *) =====
echo "→ Stage 3: Scoring (20:45)"
EXISTING3="$(hermes cron list 2>/dev/null | grep -c 'Trends.*Stage 3' || true)"
if [[ "${EXISTING3}" -gt 0 ]]; then
  echo "  ⚠ Stage 3 job exists, skipping."
else
  hermes cron create '45 20 * * *' \
    --profile "${PROFILE}" \
    --name 'Trends Stage 3 - Scoring' \
    --script "stage-3-scoring.sh" \
    --no-agent \
    --deliver origin
  echo "  ✓ Stage 3 created"
fi

# ===== STAGE 4: Indexes & Commit (0 21 * * *) =====
echo "→ Stage 4: Indexes & commit (21:00)"
EXISTING4="$(hermes cron list 2>/dev/null | grep -c 'Trends.*Stage 4' || true)"
if [[ "${EXISTING4}" -gt 0 ]]; then
  echo "  ⚠ Stage 4 job exists, skipping."
else
  hermes cron create '0 21 * * *' \
    --profile "${PROFILE}" \
    --name 'Trends Stage 4 - Indexes' \
    --script "stage-4-indexes.sh" \
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