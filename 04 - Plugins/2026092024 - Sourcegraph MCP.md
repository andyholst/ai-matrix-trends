---
id: 2026092024
created: 2026-09-20T24:00:00+02:00
tags:
  - plugin
  - mcp

---

# Sourcegraph MCP

## Overview
Sourcegraph MCP is the official Model Context Protocol server for Sourcegraph, enabling AI coding agents to perform large-scale code search and cross-repository analysis. It provides agents with the ability to search code, navigate symbols, and understand unfamiliar codebases across entire organizations. Sourcegraph's Cody AI coding assistant uses the same underlying search infrastructure.

## Key Features
- **Code search:** Full-text and regex search across all repositories
- **Symbol navigation:** Find definitions, references, and implementations
- **Cross-repo analysis:** Search and analyze code across multiple repositories
- **Code intelligence:** Precise code navigation with SCIP/LSP-based indexing
- **Repository context:** Understand codebases at scale with metadata
- **Cody integration:** Powers Sourcegraph Cody's code search capabilities

## Installation
```bash
# Claude Code
claude mcp add sourcegraph -- npx -y @sourcegraph/mcp-server

# Claude Desktop / Cursor
{
  "mcpServers": {
    "sourcegraph": {
      "command": "npx",
      "args": ["-y", "@sourcegraph/mcp-server"],
      "env": {
        "SOURCEGRAPH_URL": "https://sourcegraph.com",
        "SOURCEGRAPH_ACCESS_TOKEN": "your-token"
      }
    }
  }
}
```

## Configuration
- `SOURCEGRAPH_URL` — Sourcegraph instance URL (default: https://sourcegraph.com)
- `SOURCEGRAPH_ACCESS_TOKEN` — Sourcegraph access token
- Supports both cloud (sourcegraph.com) and self-hosted Sourcegraph instances

## Use Cases
- Search and navigate large, unfamiliar codebases
- Cross-repository code analysis and refactoring
- Find all usages of a function or symbol across an organization
- Understand code dependencies and architecture
- Onboard new developers to large codebases

## Compatibility
- **Agent:** Claude Code, Claude Desktop, Cursor, Windsurf, VS Code
- **Transports:** stdio
- **Auth:** Sourcegraph access token

## Related
- [[MOC-Plugin-Ecosystem]]
- [[MOC-Trending-Agents]]
- [[MOC-Plugin-Ecosystem]]
- [[MOC-Trending-Agents]]

## Sources
- [Sourcegraph MCP](https://github.com/sourcegraph/sourcegraph/tree/main/mcp)
- [Sourcegraph Docs](https://docs.sourcegraph.com/)
