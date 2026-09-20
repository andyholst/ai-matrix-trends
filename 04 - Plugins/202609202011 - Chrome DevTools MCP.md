---
id: 202609202011
created: 2026-09-20T20:11:00+02:00
tags:
  - plugin
  - mcp
  - browser-automation
  - debugging
links:
  - "[Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)"
  - "[Cursor](./03%20-%20Agents/202609202000%20-%20Cursor.md)"
  - "[Windsurf](./03%20-%20Agents/202609200800%20-%20Windsurf.md)"
---

# Chrome DevTools MCP

## Overview
Chrome DevTools MCP is Google's official MCP server for controlling a live Chrome browser. It exposes DevTools Protocol capabilities as structured tools: console message inspection, network request monitoring, performance traces, Lighthouse audits, heap snapshots, and screenshots. It attaches to an existing Chrome instance, preserving active logins and extensions. With 52k+ GitHub stars and 1.9M weekly npm downloads, it is the most popular browser debugging MCP server.

## Installation
```bash
# For Claude Code
claude mcp add chrome-devtools -- npx @modelcontextprotocol/server-chrome-devtools

# Or add to MCP config:
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-chrome-devtools"]
    }
  }
}
```

## Configuration
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-chrome-devtools",
        "--browserUrl", "http://localhost:9222"
      ]
    }
  }
}
```

## Use Cases
- Debugging running applications via console and network inspection
- Performance profiling with trace recording
- Lighthouse accessibility and SEO audits
- Memory leak detection via heap snapshots
- Cookie and storage debugging

## Compatibility
- **Agent:** [[202609202000 - Claude Code]], [[202609202000 - Cursor]], [[202609200800 - Windsurf]], [[202609202000 - Cursor]]
- **Versions:** Node.js LTS, Chrome 112+

## Related Plugins
- [[202609202010 - Playwright MCP]] — alternative for headless automation
- [[202609202000 - Browser Use MCP]] — alternative for persistent profiles

## Sources
- [GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [Chrome DevTools for Agents](https://developer.chrome.com/docs/devtools/agents)

## Related
- [[MOC-Plugin-Ecosystem]]
- [[MOC-Trending-Agents]]
