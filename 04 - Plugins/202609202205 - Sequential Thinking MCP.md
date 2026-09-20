---
id: 202609202205
created: 2026-09-20T22:05:00+02:00
tags:
  - plugin
  - mcp
links:
  - "[Superpowers](./04%20-%20Plugins/2026092020%20-%20Superpowers.md)"
  - "[Jev Agent Router](./04%20-%20Plugins/202609202000%20-%20Jev%20Agent%20Router.md)"
---

# Sequential Thinking MCP

## Overview
Sequential Thinking MCP is an official Anthropic reference server that gives AI agents a structured scratchpad for multi-step reasoning. Instead of trying to hold an entire chain of thought in context, the agent can write intermediate reasoning steps to a persistent scratchpad and retrieve them on demand. This reduces token usage and improves reasoning quality for complex, planning-heavy tasks.

## Installation
```bash
# Claude Code
claude mcp add sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking

# Or add to any MCP client
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

## Configuration
```yaml
mcpServers:
  sequential-thinking:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    # No API key required — runs entirely local
```

## Use Cases
- Complex multi-step problem solving
- Planning large refactors or architectural decisions
- Debugging with structured hypothesis tracking
- Any task where the agent needs to "think out loud" across many steps

## Compatibility
- **Agent:** [[202609202000 - Claude Code]], [[202609202000 - Cursor]], [[202609202000 - Codex]]
- **Versions:** MCP spec 2025-03-26+

## Related Plugins
- [[2026092020 - Superpowers]]
- [[202609202000 - Jev Agent Router]]

## Sources
- [GitHub](https://github.com/modelcontextprotocol/servers)
- [Docs](https://modelcontextprotocol.io/docs/concepts/tools)
