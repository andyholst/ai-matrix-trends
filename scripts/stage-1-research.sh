#!/bin/bash
# Stage 1: Research Streams
# Launches 4 parallel research sub-agents via Hermes delegate_task
# Schedule: Daily at 20:00

set -e

VAULT_DIR="$HOME/repository/git/ai-matrix-trends"
cd "$VAULT_DIR"

echo "============================================"
echo "Stage 1: Research Streams"
echo "$(date)"
echo "============================================"

# Stream A: Agents (5 new)
cat > /tmp/stream-a.txt << 'PROMPT'
You are an AI Matrix Trends sub-agent. Find 3-5 trending AI coding agents and create atomic notes.

Write to: ~/repository/git/ai-matrix-trends/03 - Agents/
ALWAYS USE FULL FILENAMES FOR WIKILINKS: [[202609202000 - Claude Code]] NOT [[Claude Code]]

Frontmatter:
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

Search: web_search("trending AI coding agents 2026"), web_search("new AI coding tools github stars 2026")
Create 5 atomic notes with full frontmatter and ## Related section.
PROMPT

# Stream B: Plugins (50+ for all agents)
cat > /tmp/stream-b.txt << 'PROMPT'
You are an AI Matrix Trends sub-agent. Find the MOST POPULAR plugins/extensions for EACH major AI coding agent.

Write to: ~/repository/git/ai-matrix-trends/04 - Plugins/
ALWAYS USE FULL FILENAMES FOR WIKILINKS: [[202609202000 - Claude Code]] NOT [[Claude Code]]

CRITICAL: Research plugins for EACH of these agents: Claude Code, OpenCode, Cursor, Codex, Windsurf, Aider, Gemini CLI, GitHub Copilot, Kilo Code, RooCode, JetBrains Junie, Hermes Agent.

For EACH agent search: web_search("best [agent] plugins 2026"), web_search("[agent] MCP servers 2026"), web_search("[agent] extensions 2026")

Frontmatter MUST include:
---
id: 2026092020
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - mcp
agents:
  - claude-code
  - hermes
links:
  - "[[full-filename-1]]"
---

## Compatibility section with **Agent:** line listing supported agents.
Create 10+ notes covering plugins for ALL agents.
PROMPT

# Stream C: Architecture (3 patterns)
cat > /tmp/stream-c.txt << 'PROMPT'
You are an AI Matrix Trends sub-agent. Find 2-3 emerging architecture patterns and create atomic notes.

Write to: ~/repository/git/ai-matrix-trends/05 - Architecture/
ALWAYS USE FULL FILENAMES FOR WIKILINKS.

Frontmatter:
---
id: 2026092030
created: 2026-09-20T30:00:00+02:00
tags:
  - architecture
  - mcp
links:
  - "[[full-filename-1]]"
---

Search: web_search("MCP protocol architecture patterns 2026"), web_search("multi-agent AI orchestration patterns 2026")
Create 3 atomic notes.
PROMPT

# Stream D: Use Cases (3 workflows)
cat > /tmp/stream-d.txt << 'PROMPT'
You are an AI Matrix Trends sub-agent. Find 2-3 real-world use cases and create atomic notes.

Write to: ~/repository/git/ai-matrix-trends/06 - Use Cases/
ALWAYS USE FULL FILENAMES FOR WIKILINKS.

Frontmatter:
---
id: 2026092040
created: 2026-09-20T40:00:00+02:00
tags:
  - workflow
  - config
links:
  - "[[full-filename-1]]"
---

Search: web_search("Claude Code hooks CI/CD automation 2026"), web_search("multi-server MCP orchestration workflows")
Create 3 atomic notes.
PROMPT

# Launch all 4 streams via Hermes delegate_task
echo "Launching 4 parallel research streams..."
hermes delegate --prompt-file /tmp/stream-a.txt &
hermes delegate --prompt-file /tmp/stream-b.txt &
hermes delegate --prompt-file /tmp/stream-c.txt &
hermes delegate --prompt-file /tmp/stream-d.txt &

echo "All 4 research streams launched in parallel"
echo "Stage 1 complete"