---
id: 2026092023
created: 2026-09-20T20:03:00+02:00
tags:
  - plugin
  - mcp
  - claude-code
  - cursor
  - codebase-intelligence
agents:
  - claude-code
  - opencode
  - cursor
  - codex
  - windsurf
  - aider
  - gemini-cli
  - github-copilot
  - kilo-code
  - roocode
  - jetbrains-junie
  - cline
  - hermes
---

# CodeGraph MCP

## Overview
CodeGraph is an MCP server that converts your codebase into a knowledge graph, enabling AI agents to understand code structure, relationships, and dependencies at a semantic level. It uses tree-sitter AST parsing across 42+ languages and stores the graph in SQLite (or FalkorDB for larger projects). Agents can query the graph to find call chains, detect circular dependencies, and navigate large codebases without reading every file.

## Installation
```bash
# Install the CLI
npm install -g codegraph

# Auto-register with Claude Code, Cursor, Codex CLI, and OpenCode
codegraph init

# Or add manually to any MCP config:
{
  "mcpServers": {
    "codegraph": {
      "command": "codegraph",
      "args": ["serve"]
    }
  }
}
```

## Configuration
```json
{
  "mcpServers": {
    "codegraph": {
      "command": "codegraph",
      "args": ["serve"]
    }
  }
}
```

## Use Cases
- Semantic code navigation — "find all callers of this function" across the entire repo
- Dependency analysis and circular dependency detection
- Impact analysis before refactoring
- Onboarding acceleration for new developers (and agents)
- Codebase Q&A without loading full files into context

## Compatibility
- **Agent:** [202609202000 - Claude Code](../03%20-%20Agents/202609202000%20-%20Claude%20Code.md), [202609202000 - Cursor](../03%20-%20Agents/202609202000%20-%20Cursor.md), [202609202000 - Codex](../03%20-%20Agents/202609202000%20-%20Codex.md), [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md)
- **Versions:** Claude Code v2.x+, current Cursor/Codex/OpenCode

## Related Plugins
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md), [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)

## Sources
- [GitHub](https://github.com/Phoenixrr2113/codebase-graph)
- [Guide](https://tosea.ai/blog/codegraph-claude-code-cursor-guide-2026)
