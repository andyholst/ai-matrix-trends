---
id: 202609202125
created: 2026-09-20T21:25:00+02:00
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

# Cloudflare MCP

## Overview
Cloudflare MCP is the official Model Context Protocol server for the Cloudflare developer platform. It gives AI coding agents access to Workers, KV, R2, D1, Pages, and other Cloudflare resources. Agents can deploy workers, manage DNS, inspect cache rules, and query analytics — all from the terminal. Supports HTTP transport with OAuth or API token auth.

## Installation
```bash
# Claude Code
claude mcp add cloudflare -- npx -y @cloudflare/mcp-server

# Or use the hosted endpoint
# https://mcp.cloudflare.com/mcp
```

## Configuration
```yaml
mcpServers:
  cloudflare:
    type: http
    url: https://mcp.cloudflare.com/mcp
    headers:
      Authorization: Bearer ${CLOUDFLARE_API_TOKEN}
    # Or local stdio:
    # command: npx
    # args: ["-y", "@cloudflare/mcp-server"]
    # env:
    #   CLOUDFLARE_API_TOKEN: ${CLOUDFLARE_API_TOKEN}
    #   CLOUDFLARE_ACCOUNT_ID: ${CLOUDFLARE_ACCOUNT_ID}
```

## Use Cases
- Deploying and managing Cloudflare Workers
- Inspecting KV and R2 storage buckets
- Managing DNS records and cache rules
- Querying analytics and security events

## Compatibility
- **Agent:** [202609202000 - Claude Code](../03%20-%20Agents/202609202000%20-%20Claude%20Code.md), [202609202000 - Cursor](../03%20-%20Agents/202609202000%20-%20Cursor.md), [202609202000 - Codex](../03%20-%20Agents/202609202000%20-%20Codex.md)
- **Versions:** MCP spec 2025-03-26+

## Related Plugins
- [202609202000 - Browser Use MCP](202609202000%20-%20Browser%20Use%20MCP.md)
- [2026092020 - GitHub MCP Server](2026092020%20-%20GitHub%20MCP%20Server.md)

## Sources
- [GitHub](https://github.com/cloudflare/mcp-server-cloudflare)
- [Docs](https://developers.cloudflare.com/mcp/)
