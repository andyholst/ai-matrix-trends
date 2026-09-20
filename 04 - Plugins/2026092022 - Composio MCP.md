---
id: 2026092022
created: 2026-09-20T20:02:00+02:00
tags:
  - plugin
  - mcp
  - claude-code
  - integrations
links:
  - "[Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md)"
  - "[Jev Agent Router](./04%20-%20Plugins/202609202000%20-%20Jev%20Agent%20Router.md)"
---

# Composio MCP

## Overview
Composio is a universal integration layer that gives AI coding agents secure access to 1,500+ external applications (GitHub, Linear, Jira, Slack, Figma, Sentry, HubSpot, etc.) through a single MCP connection. Instead of configuring each app's API separately, Composio handles authentication (OAuth), tool discovery, and action execution. It is available as a Claude Code plugin and also works with Cursor, Codex, and other MCP-compliant agents.

## Installation
```bash
# Add the Composio marketplace in Claude Code
/plugin marketplace add ComposioHQ/composio-plugin-cc

# Install the plugin
/plugin install composio@composio

# Or install the CLI manually
curl -fsSL https://composio.dev/install | sh
composio login
```

## Configuration
```json
{
  "mcpServers": {
    "composio": {
      "type": "http",
      "url": "https://connect.composio.dev/mcp"
    }
  }
}
```

## Use Cases
- Cross-app workflows: create Linear issues from Claude, update Jira tickets, post to Slack
- Unified OAuth — authenticate once, access 1500+ apps
- PR review and issue triage with full repo context
- Sales and GTM workflows (HubSpot, Gmail, Calendar)
- Design-to-code pipelines via Figma integration

## Compatibility
- **Agent:** [[202609202000 - Claude Code]], [[202609202000 - Cursor]], [[202609202000 - Codex]]
- **Versions:** Any MCP-compliant agent

## Related Plugins
- [[MOC-Plugin-Ecosystem]], [[MOC-Trending-Agents]]

## Sources
- [Docs](https://docs.composio.dev/docs/claude-code-plugin)
- [Website](https://composio.dev)
