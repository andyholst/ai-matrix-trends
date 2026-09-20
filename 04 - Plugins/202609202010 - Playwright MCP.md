---
id: 202609202010
created: 2026-09-20T20:10:00+02:00
tags:
  - plugin
  - mcp
  - browser-automation
links:
  - "[Claude Code](../03%20-%20Agents/202609202000%20-%20Claude%20Code.md)"
  - "[Cursor](../03%20-%20Agents/202609202000%20-%20Cursor.md)"
  - "[Windsurf](../03%20-%20Agents/202609200800%20-%20Windsurf.md)"
  - "[OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md)"
---

# Playwright MCP

## Overview
Playwright MCP is Microsoft's official Model Context Protocol server that gives AI coding agents full browser automation capabilities. It exposes 24 structured tools for navigation, clicking, typing, form filling, screenshots, and accessibility snapshots. Unlike vision-based approaches, it uses the accessibility tree for page state, making it token-efficient and deterministic. It supports Chromium, Firefox, WebKit, and Edge, and runs on Node.js 18+.

## Installation
```bash
# For Claude Code
claude mcp add playwright -- npx @playwright/mcp@latest

# For Cursor / Windsurf / VS Code, add to MCP config:
# ~/.cursor/mcp.json or equivalent
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

## Configuration
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "env": {
        "PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH": "/path/to/chromium"
      }
    }
  }
}
```

## Use Cases
- End-to-end testing with natural language goals
- Web scraping with structured data extraction
- Form filling and multi-step workflows
- Accessibility auditing via snapshot analysis
- Regression testing through scripted browser sessions

## Compatibility
- **Agent:** [202609202000 - Claude Code](../03%20-%20Agents/202609202000%20-%20Claude%20Code.md), [202609202000 - Cursor](../03%20-%20Agents/202609202000%20-%20Cursor.md), [202609200800 - Windsurf](../03%20-%20Agents/202609200800%20-%20Windsurf.md), [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md)
- **Versions:** Node.js 18+, Playwright MCP 0.0.82+

## Related Plugins
- [202609202000 - Browser Use MCP](202609202000%20-%20Browser%20Use%20MCP.md) — alternative browser automation MCP
- [202609202000 - Jev Agent Router](202609202000%20-%20Jev%20Agent%20Router.md) — context management for long browser sessions

## Sources
- [GitHub](https://github.com/microsoft/playwright-mcp)
- [npm](https://www.npmjs.com/package/@playwright/mcp)

## Related
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md)
- [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)
