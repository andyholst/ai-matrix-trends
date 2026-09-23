---
id: 2026092020
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - mcp
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

# GitHub MCP Server

## Overview
GitHub's official MCP Server exposes repository, issue, pull request, Actions, and code search capabilities to AI coding agents. With 33.1k+ stars on GitHub, it is one of the most widely adopted MCP servers. It supports both stdio and HTTP (Streamable HTTP) transports, with OAuth authentication for remote use. The server also ships as a Claude Code plugin via the `agent-plugin` package.

## Key Features
- **Repository operations:** Create, fork, and manage repos; search code and files
- **Issues & PRs:** Create, update, and comment on issues and pull requests; merge PRs
- **Actions:** List workflows, trigger runs, download artifacts, view logs
- **Code search:** Semantic search across GitHub code with filters
- **Notifications:** Mark notifications as read, list notifications
- **Security:** Code scanning alerts, secret scanning, Dependabot

## Installation
```bash
# Claude Code (stdio)
claude mcp add github -- npx -y @github/mcp-server

# Claude Code (HTTP/remote)
claude mcp add github --transport http https://api.githubcopilot.com/mcp

# Claude Desktop / Cursor (stdio)
# Add to ~/.cursor/mcp.json or claude_desktop_config.json:
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@github/mcp-server"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token"
      }
    }
  }
}
```

## Configuration
- `GITHUB_PERSONAL_ACCESS_TOKEN` — PAT with appropriate scopes (repo, read:org, etc.)
- `GITHUB_MCP_SERVER_NAME` / `GITHUB_MCP_SERVER_TITLE` — Override server identity for GHES instances
- Supports GitHub Enterprise Server via `GITHUB_API_URL` env var

## Use Cases
- Automate PR creation and code review workflows
- Query CI/CD status and logs from agent conversations
- Search and navigate large codebases without leaving the agent
- Manage issues and project boards programmatically

## Compatibility
- **Agent:** Claude Code, Claude Desktop, Cursor, Windsurf, VS Code, OpenCode, Codex
- **Transports:** stdio (local), Streamable HTTP (remote)
- **Auth:** GitHub PAT or OAuth

## Related
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md)
- [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md)
- [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)

## Sources
- [GitHub MCP Server](https://github.com/github/github-mcp-server)
- [GitHub MCP Server Docs](https://docs.github.com/en/copilot/concepts/mcp)
