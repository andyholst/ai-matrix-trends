---
id: 2026092023
created: 2026-09-20T20:03:00+02:00
tags:
  - plugin
  - mcp
  - claude-code
  - cursor
  - codebase-intelligence
links:
  - "[[202609202000 - Browser Use MCP]]"
  - "[[202609202000 - Jev Agent Router]]"
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
- **Agent:** [[202609202000 - Claude Code]], [[202609202000 - Cursor]], [[202609202000 - Codex]], [[202609200758 - OpenCode]]
- **Versions:** Claude Code v2.x+, current Cursor/Codex/OpenCode

## Related Plugins
- [[MOC-Plugin-Ecosystem]], [[MOC-Trending-Agents]]

## Sources
- [GitHub](https://github.com/Phoenixrr2113/codebase-graph)
- [Guide](https://tosea.ai/blog/codegraph-claude-code-cursor-guide-2026)
