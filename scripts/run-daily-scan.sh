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

# Stream A: Agents (find 5 new agents)
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
links:
  - "[[full-filename-1]]"
  - "[[full-filename-2]]"
---

ALWAYS USE FULL FILENAMES FOR WIKILINKS: [[202609202000 - Claude Code]] NOT [[Claude Code]]

Research steps:
1. web_search("trending AI coding agents 2026")
2. web_search("new AI coding tools github stars")
3. web_extract relevant URLs

Create 5 atomic notes for the most trending agents.
EOF

# Stream B: Plugins for EACH major agent (comprehensive)
echo "  Launching Stream B: Plugins (per-agent research)..."
cat > /tmp/stream-b-prompt.txt << 'EOF'
You are an AI Matrix Trends sub-agent. Your task is to find the MOST POPULAR plugins/extensions for EACH major AI coding agent.

Write notes to: ~/repository/git/ai-matrix-trends/04 - Plugins/
Use timestamps: 2026092020 through 2026092029

MANDATORY FRONTMATTER FORMAT:
---
id: 2026092020
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - mcp
agents:
  - claude-code
  - opencode
links:
  - "[[full-filename-1]]"
  - "[[full-filename-2]]"
---

ALWAYS USE FULL FILENAMES FOR WIKILINKS: [[202609202000 - Claude Code]] NOT [[Claude Code]]

CRITICAL: For EACH plugin you create, you MUST include a ## Compatibility section with:
**Agent:** [[202609202000 - Claude Code]], [[202609200758 - OpenCode]], etc.

Research steps (search for plugins for EACH agent):
1. web_search("best Claude Code MCP servers plugins 2026")
2. web_search("best OpenCode plugins extensions 2026")
3. web_search("best Cursor AI plugins MCP 2026")
4. web_search("best Codex OpenAI plugins 2026")
5. web_search("best Windsurf plugins MCP 2026")
6. web_search("best Aider plugins 2026")
7. web_search("best Gemini CLI plugins 2026")
8. web_search("best GitHub Copilot plugins 2026")
9. web_search("Hermes Agent plugins extensions 2026")
10. web_search("best Kilo Code plugins 2026")
11. web_search("best RooCode plugins 2026")
12. web_search("best JetBrains Junie plugins 2026")
13. web_search("popular MCP servers 2026")
14. web_search("trending AI coding agent plugins 2026")
15. web_extract relevant URLs

Create 10+ atomic notes covering plugins for ALL major agents.
Each plugin note MUST have:
- ## Compatibility section with **Agent:** line listing supported agents
- agents: field in frontmatter with agent keys
- Tags including mcp if applicable
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
links:
  - "[[full-filename-1]]"
  - "[[full-filename-2]]"
---

ALWAYS USE FULL FILENAMES FOR WIKILINKS: [[202609202000 - Claude Code]] NOT [[Claude Code]]

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
links:
  - "[[full-filename-1]]"
  - "[[full-filename-2]]"
---

ALWAYS USE FULL FILENAMES FOR WIKILINKS: [[202609202000 - Claude Code]] NOT [[Claude Code]]

Research steps:
1. web_search("Claude Code hooks CI/CD automation")
2. web_search("multi-server MCP orchestration workflows")
3. web_extract relevant URLs

Create 3 atomic notes for real-world use cases.
EOF

# Step 3: Wait for streams to complete (they run in parallel via delegate_task)
echo ""
echo "Step 3: Research streams launched. They will complete in ~3 minutes..."

# Step 4: Run link resolvers and fixers (IN ORDER — matches daily-scan-prompt.md)
echo ""
echo "Step 4/7: Resolving wikilinks..."
python3 "$SCRIPTS_DIR/resolve_wikilinks.py"

echo ""
echo "Step 5/7: Fixing all broken links..."
python3 "$SCRIPTS_DIR/fix_all_links.py"

echo ""
echo "Step 6/7: Aggregating trend scores..."
python3 "$SCRIPTS_DIR/aggregate-trends.py"

echo ""
echo "Step 7/7a: Collecting agent plugins..."
python3 "$SCRIPTS_DIR/collect_agent_plugins.py"

echo ""
echo "Step 7/7b: Updating README tables..."
python3 "$SCRIPTS_DIR/update_readme.py"

echo ""
echo "Step 7/7d: Verifying vault links..."
python3 "$SCRIPTS_DIR/verify-vault.py"

echo ""
echo "Step 7/7e: Updating MOCs..."
python3 "$SCRIPTS_DIR/update-mocs.py"

echo ""
echo "Step 7/7f: Updating Plugin Master Index..."
python3 "$SCRIPTS_DIR/update-plugin-master-index.py"

echo ""
echo "Step 7/7g: Updating Agent Master Index..."
python3 "$SCRIPTS_DIR/update-agent-master-index.py"

echo ""
echo "Step 7/7h: Fixing Master Index links..."
python3 "$SCRIPTS_DIR/fix-master-index-links.py"

echo ""
echo "============================================"
echo "Daily scan complete!"
echo "$(date)"
echo "============================================"