---
id: 202609202014
created: 2026-09-20T20:14:00+02:00
tags:
  - plugin
  - opencode
  - all-in-one
links:
  - [[MOC-Plugin-Ecosystem]]
  - [[MOC-Trending-Agents]]
  - [[202609200758 - OpenCode]]
---

# OpenCode Oh-My-Openagent

## Overview
Oh-My-Openagent is the most prominent all-in-one plugin in the OpenCode ecosystem. It adds background agents, pre-built LSP/AST/MCP tools, curated agent packs, and Claude Code compatibility. The plugin provides 10 visible agents (Bob, Coder, Strategist, Critic, Guard, Researcher, Designer, Manager, Brainstormer, Vision) plus hidden Sub and Agent Skills. It is widely regarded as the single most impactful OpenCode plugin for advanced workflows.

## Installation
```bash
# Add to OpenCode config
# ~/.config/opencode/config.json
{
  "plugin": ["oh-my-opencode"]
}
```

## Configuration
```json
{
  "plugin": ["oh-my-opencode"],
  "agent": {
    "default": "coder",
    "background": true
  }
}
```

## Use Cases
- Multi-agent orchestration with specialized roles
- Background task execution without blocking the main session
- Claude Code-compatible skill workflows
- LSP and AST tooling for code analysis
- Curated agent packs for common development patterns

## Compatibility
- **Agent:** [[202609200758 - OpenCode]]
- **Versions:** OpenCode 2.x+

## Related Plugins
- [[202609202000 - OpenCode Supermemory]] — persistent memory layer
- [[202609202000 - OpenCode Firecrawl]] — web scraping integration

## Sources
- [GitHub](https://github.com/ohmyopencode/oh-my-opencode)
- [OpenCode Ecosystem](https://opencode.ai/docs/ecosystem/)
- [Awesome OpenCode](https://github.com/awesome-opencode/awesome-opencode)
