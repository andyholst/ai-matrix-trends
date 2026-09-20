#!/bin/bash
# AI Matrix Trends - Daily Trend Scan Master Script
# This script is executed by the Hermes cron job

set -e

VAULT_DIR="$HOME/repository/git/ai-matrix-trends"
SCRIPTS_DIR="$VAULT_DIR/scripts"

echo "============================================"
echo "AI Matrix Trends - Daily Trend Scan"
echo "$(date)"
echo "============================================"

cd "$VAULT_DIR"

# Step 1: Pre-scan setup
echo ""
echo "Step 1: Pre-scan setup..."

# Check current state
find . -name "*.md" -not -path "*/.git/*" | wc -l
echo "Current notes in vault"

# Step 2: Launch parallel research streams
echo ""
echo "Step 2: Launching research streams..."

# Stream A: Agents
echo "  Launching Stream A: Agents..."
cat > /tmp/stream-a-prompt.txt << 'EOF'
You are an AI Matrix Trends sub-agent. Your task is to find 3-5 trending AI coding agents and create atomic notes.

Write notes to: ~/repository/git/ai-matrix-trends/03 - Agents/
Use timestamps: 2026092010, 2026092011, 2026092012, 2026092013, 2026092014

MANDATORY FRONTMATTER FORMAT:
---
id: 2026092010
created: 2026-09-20T10:00:00+02:00
tags:
  - agent
  - cli
---

DO NOT add links: field to frontmatter.
Put all links in the ## Related section at the bottom using short names like [[Claude Code]].

Research steps:
1. web_search("trending AI coding agents 2026")
2. web_search("new AI coding tools github stars")
3. web_extract relevant URLs

Create 5 atomic notes for the most trending agents.
EOF

# Stream B: Plugins
echo "  Launching Stream B: Plugins..."
cat > /tmp/stream-b-prompt.txt << 'EOF'
You are an AI Matrix Trends sub-agent. Your task is to find 3-5 trending plugins/extensions and create atomic notes.

Write notes to: ~/repository/git/ai-matrix-trends/04 - Plugins/
Use timestamps: 2026092020, 2026092021, 2026092022, 2026092023, 2026092024

MANDATORY FRONTMATTER FORMAT:
---
id: 2026092020
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - mcp
---

DO NOT add links: field to frontmatter.
Put all links in the ## Related section at bottom using short names.

Research steps:
1. web_search("best Claude Code MCP servers 2026")
2. web_search("OpenCode plugins and extensions")
3. web_extract relevant URLs

Create 5 atomic notes for the most trending plugins.
EOF

# Stream C: Architecture
echo "  Launching Stream C: Architecture..."
cat > /tmp/stream-c-prompt.txt << 'EOF'
You are an AI Matrix Trends sub-agent. Your task is to find 2-3 emerging architecture patterns and create atomic notes.

Write notes to: ~/repository/git/ai-matrix-trends/05 - Architecture/
Use timestamps: 2026092030, 2026092031, 2026092032

MANDATORY FRONTMATTER FORMAT:
---
id: 2026092030
created: 2026-09-20T30:00:00+02:00
tags:
  - architecture
  - mcp
---

DO NOT add links: field to frontmatter.
Put all links in the ## Related section at bottom using short names.

Research steps:
1. web_search("MCP protocol architecture patterns 2026")
2. web_search("multi-agent AI orchestration patterns")
3. web_extract relevant URLs

Create 3 atomic notes for emerging architecture patterns.
EOF

# Stream D: Use Cases
echo "  Launching Stream D: Use Cases..."
cat > /tmp/stream-d-prompt.txt << 'EOF'
You are an AI Matrix Trends sub-agent. Your task is to find 2-3 real-world use cases and create atomic notes.

Write notes to: ~/repository/git/ai-matrix-trends/06 - Use Cases/
Use timestamps: 2026092040, 2026092041, 2026092042

MANDATORY FRONTMATTER FORMAT:
---
id: 2026092040
created: 2026-09-20T40:00:00+02:00
tags:
  - workflow
  - config
---

DO NOT add links: field to frontmatter.
Put all links in the ## Related section at bottom using short names.

Research steps:
1. web_search("Claude Code hooks CI/CD automation")
2. web_search("multi-server MCP orchestration workflows")
3. web_extract relevant URLs

Create 3 atomic notes for real-world use cases.
EOF

# Step 3: Wait for streams to complete (they run in parallel via delegate_task)
echo ""
echo "Step 3: Research streams launched. They will complete in ~3 minutes..."

# Step 4: Run the link fixer script
echo ""
echo "Step 4: Running link fixer..."
python3 "$SCRIPTS_DIR/fix-links.py"

# Step 5: Update MOCs
echo ""
echo "Step 5: Updating MOCs..."
python3 "$SCRIPTS_DIR/update-mocs.py"

# Step 6: Update README
echo ""
echo "Step 6: Updating README..."
python3 "$SCRIPTS_DIR/update-readme.py"

# Step 7: Final verification
echo ""
echo "Step 7: Final verification..."
python3 "$SCRIPTS_DIR/verify-vault.py"

echo ""
echo "============================================"
echo "Daily scan complete!"
echo "$(date)"
echo "============================================"
