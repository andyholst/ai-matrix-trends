---
id: 202609200807
created: 2026-09-20T08:07:00+02:00
tags:
  - plugin
  - claude-code
  - tool
links:
  - "[[MOC-Plugin-Ecosystem]]"
  - "[[MOC-Trending-Agents]]"
---

# Claude Code Auto Permission

## Overview
Auto Permission is a Claude Code permission mode introduced in v2.1.259 (September 2026) that lets the server evaluate each agent or MCP tool call and decide whether to run it, deny it, or pause for user approval. Unlike the existing `acceptEdits` or `bypassPermissions` modes, auto mode uses background safety checks to verify that tool actions align with the user's original request — catching risky or off-task behavior without requiring manual approval for every call. The same release also introduced `managedMcpServers`, which lets organizations provide HTTP/SSE MCP servers to all users without filesystem deployment. Together, these features represent a shift toward server-governed agent safety.

## Installation
```bash
# Update Claude Code to v2.1.259+
claude update

# Set permission mode to auto in settings
# ~/.claude/settings.json
{
  "permissions": {
    "defaultMode": "auto"
  }
}

# Managed MCP servers (admin-managed, deployed to all users)
{
  "managedMcpServers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

## Configuration
```json
{
  "permissions": {
    "defaultMode": "auto"
  },
  "managedMcpServers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

## Use Cases
- Reducing approval fatigue for routine tool calls while maintaining safety
- Enterprise MCP server deployment without touching user filesystems
- Auditing tool calls via `agent.tool_use` and `agent.mcp_tool_use` events with `evaluation` fields
- Background safety checks that pause for approval when actions deviate from the request

## Compatibility
**Agent:** [[202609202000 - Claude Code]]
**Versions:** v2.1.259+
**Dependencies:** Claude Pro/Max or API access

## Related Plugins
- [[202609200803 - Context7 MCP]] — A prime candidate for managedMcpServers deployment
- [[202609200804 - FAL MCP Server]] — Deploy as a managed server for org-wide media generation

## Sources
- [Claude Platform Release Notes](https://platform.claude.com/docs/en/release-notes/overview)
- [Claude Code v2.1.259 changelog](https://code.claude.com/docs/en/whats-new)
- [managedMcpServers setting](https://www.getclaudeskills.com/blog/claude-code-managed-mcp-servers-setting)
