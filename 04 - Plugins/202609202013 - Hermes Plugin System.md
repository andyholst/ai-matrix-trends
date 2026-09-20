---
id: 202609202013
created: 2026-09-20T20:13:00+02:00
tags:
  - plugin
  - hermes
  - architecture
links:
  - [[202609202000 - Jev Agent Router]]
  - [[202609202000 - OpenCode Supermemory]]
---

# Hermes Plugin System

## Overview
Hermes Agent has a comprehensive plugin system for adding custom tools, hooks, and integrations without modifying core code. Plugins are Python packages dropped into `~/.hermes/plugins/` with a `plugin.yaml` manifest. The system supports tools, lifecycle hooks, slash commands, CLI commands, platform adapters (Discord, Telegram, Signal), memory backends, context-compression engines, image/video generation providers, and MCP server bridges. Plugins can be distributed via pip using entry points.

## Installation
```bash
# Manual installation
git clone https://github.com/42-evey/hermes-plugins
cp -r hermes-plugins/evey-* ~/.hermes/plugins/

# Or install from the plugin catalog
hermes plugins install <plugin-name>

# Enable in config
# ~/.hermes/config.yaml
plugins:
  enabled:
    - my-plugin
```

## Configuration
```yaml
# ~/.hermes/plugins/my-plugin/plugin.yaml
name: my-plugin
version: "1.0.0"
description: My custom plugin
requires_env:
  - MY_API_KEY
```

## Use Cases
- Adding custom tools via `ctx.register_tool()`
- Registering lifecycle hooks with `ctx.register_hook()`
- Creating slash commands with `ctx.register_command()`
- Adding gateway platforms via `ctx.register_platform()`
- Implementing memory backends by subclassing `MemoryProvider`
- Registering context-compression engines via `ctx.register_context_engine()`

## Compatibility
- **Agent:** [[202609200759 - Hermes Agent]]
- **Versions:** Hermes Agent 1.0+

## Related Plugins
- [[202609202000 - Jev Agent Router]] — example plugin using the system
- [[202609202000 - OpenCode Supermemory]] — alternative memory approach

## Sources
- [Hermes Plugin Docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins)
- [Plugin Catalog](https://hermes-agent.nousresearch.com/docs/plugins)
- [Evey's Hermes Plugins](https://github.com/42-evey/hermes-plugins)
