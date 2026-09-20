---
id: 2026092021
created: 2026-09-20T20:01:00+02:00
tags:
  - plugin
  - opencode
  - codex
  - mcp
links:
  - "[[202609202503 - Browser Use MCP]]"
  - "[[202609202000 - Jev Agent Router]]"
---

# Oh My OpenAgent

## Overview
Oh My OpenAgent (omo) is a batteries-included agent harness for OpenCode (and a Light edition for Codex CLI). It ships 11 specialized agents (Sisyphus, Oracle, Librarian, Explore, Multimodal Looker, Prometheus, Metis, Momus, Atlas, and more), 54+ lifecycle hooks, 4 built-in MCP servers (websearch, context7, grep_app, lsp), all slash commands, Team Mode, `/goal`, and ultrawork. It is the most downloaded OpenCode plugin with 45K+ installs.

## Installation
```bash
# OpenCode (Ultimate Edition)
# Add to opencode.json:
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["oh-my-opencode@latest"]
}

# Codex CLI (Light Edition)
npx lazycodex-ai install
```

## Configuration
```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["oh-my-opencode@latest"],
  "mcp": {
    "github": {
      "type": "remote",
      "url": "https://api.githubcopilot.com/mcp/",
      "enabled": true
    }
  }
}
```

## Use Cases
- Multi-agent orchestration with specialized roles (coder, reviewer, researcher)
- Team Mode for collaborative agent workflows
- Built-in LSP and Context7 for code intelligence and fresh docs
- `/goal` command for session-scoped objective tracking
- Ultrawork mode for extended autonomous coding sessions

## Compatibility
- **Agent:** [[202609200758 - OpenCode]], [[202609202000 - Codex]]
- **Versions:** OpenCode v1.x+, Codex CLI

## Related Plugins
- [[MOC-Plugin-Ecosystem]], [[MOC-Trending-Agents]]

## Sources
- [GitHub](https://github.com/code-yeongyu/oh-my-openagent)
- [OpenCode Plugins](https://opencode.im/plugin/oh-my-opencode)
