---
id: 2026092024
created: 2026-09-20T20:04:00+02:00
tags:
  - plugin
  - opencode
  - token-optimization
agents:
  - opencode
---


# OpenCode Snip

## Overview
OpenCode Snip is an OpenCode plugin that automatically prefixes shell commands with the `snip` binary to reduce LLM token consumption by 60-90%. It filters verbose bash output (npm install logs, pytest output, docker build logs) so only the essential parts reach the agent's context window. This is one of the most impactful token-optimization plugins for OpenCode, with users reporting up to 96% reduction in per-request token usage.

## Installation
```bash
# 1. Install the snip binary
brew install edouard-claude/tap/snip
# or
go install github.com/edouard-claude/snip/cmd/snip@latest

# 2. Add the plugin to opencode.json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-snip@latest"]
}
```

## Configuration
```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-snip@latest"]
}
```

## Use Cases
- Reducing token costs on bash-heavy sessions (npm, pytest, docker, maven)
- Keeping context window focused on code rather than build output
- Extending effective context capacity without upgrading model tiers
- CI/CD pipeline runs where output verbosity is high

## Compatibility
- **Agent:** [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md)
- **Versions:** OpenCode v1.x+

## Related Plugins
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md), [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)

## Sources
- [GitHub](https://github.com/VincentHardouin/opencode-snip)
- [Token Optimization Guide](https://developer.upsun.com/posts/ai/opencode-token-optimization)
