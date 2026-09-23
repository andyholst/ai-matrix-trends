---
id: 202609200924
created: 2026-09-20T09:24:00+02:00
tags:
  - plugin
  - opencode
  - browser-automation
agents:
  - opencode
---

# OpenCode Chromium Browser

## Overview
OpenCode Chromium Browser is a browser automation plugin for OpenCode that controls real Chromium-based browsers using a readable Manifest V3 extension and a Node.js native messaging host. Unlike MCP-based approaches, it communicates over local sockets with no MCP server required. It supports multi-tab parallel actions and provides declarative click, type, query, and snapshot primitives. The plugin was originally developed by DJOCKER-FACE and later migrated to Quindart-com/opencode-chromium, where it continues as an open-source project.

## Installation
```bash
# Add to OpenCode config
# ~/.config/opencode/config.json

{
  "plugin": ["opencode-chromium"]
}

# Install the browser extension from the Chrome Web Store
# or load unpacked from the repository
```

## Configuration
```json
{
  "plugin": ["opencode-chromium"],
  "chromium": {
    "browserPath": "/usr/bin/chromium",
    "headless": false,
    "multiTab": true,
    "nativeMessagingHost": "~/.config/opencode/chromium-host"
  }
}
```

## Use Cases
- Browser automation without MCP server overhead
- Multi-tab parallel web interactions
- Declarative web scraping and testing
- Form filling and workflow automation
- Integration with existing Chromium profiles

## Compatibility
- **Agent:** [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md)
- **Versions:** OpenCode 2.x+, Chromium 120+, Node.js 18+

## Related Plugins
- [202609202010 - Playwright MCP](202609202010%20-%20Playwright%20MCP.md) — MCP-based browser automation
- [202609202011 - Chrome DevTools MCP](202609202011%20-%20Chrome%20DevTools%20MCP.md) — Chrome DevTools Protocol MCP
- [202609202000 - Browser Use MCP](202609202000%20-%20Browser%20Use%20MCP.md) — Python-based browser agent

## Sources
- [GitHub](https://github.com/Quindart-com/opencode-chromium)
- [Awesome OpenCode](https://github.com/awesome-opencode/awesome-opencode)
- [OpenCode Ecosystem](https://opencode.ai/docs/ecosystem/)

## Related
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md)
- [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)
