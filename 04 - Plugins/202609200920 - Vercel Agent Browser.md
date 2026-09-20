---
id: 202609200920
created: 2026-09-20T09:20:00+02:00
tags:
  - plugin
  - browser-automation
  - cli
links:
  - "[Playwright MCP](./04%20-%20Plugins/202609202010%20-%20Playwright%20MCP.md)"
  - "[Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md)"
  - "[Chrome DevTools MCP](./04%20-%20Plugins/202609202011%20-%20Chrome%20DevTools%20MCP.md)"
---

# Vercel Agent Browser

## Overview
Vercel Agent Browser is a browser automation CLI purpose-built for AI coding agents. Written in Rust (89%), it provides snapshot-based element selection optimized for LLMs, enabling agents to navigate, click, type, and extract data from web pages. With 42.9k GitHub stars and 125+ contributors, it has become a go-to tool for developers integrating browser automation into AI coding workflows. It supports both local engines (Playwright, Puppeteer) and cloud providers (Browserbase, Browserless, Browser Use, Kernel).

## Installation
```bash
# Install via npm
npm install -g agent-browser

# Or via cargo
cargo install agent-browser

# For Claude Code MCP integration
claude mcp add agent-browser -- npx agent-browser-mcp
```

## Configuration
```json
{
  "engine": "playwright",
  "provider": "browserbase",
  "headless": true,
  "snapshotFormat": "aria",
  "timeout": 30000
}
```

## Use Cases
- AI-driven web scraping and data extraction
- Automated E2E testing with natural language goals
- Browser-based research tasks for coding agents
- Form filling and multi-step web workflows
- Cloud browser session management with provider failover

## Compatibility
- **Agent:** [[202609202000 - Claude Code]], [[202609202000 - Cursor]], [[202609200758 - OpenCode]]
- **Versions:** Node.js 18+, Rust 1.75+

## Related Plugins
- [[202609202010 - Playwright MCP]] — alternative browser automation via MCP
- [[202609202000 - Browser Use MCP]] — Python-based browser agent
- [[202609202011 - Chrome DevTools MCP]] — Chrome DevTools Protocol MCP server

## Sources
- [GitHub](https://github.com/vercel-labs/agent-browser)
- [npm](https://www.npmjs.com/package/agent-browser)
- [Bright Data](https://brightdata.com/blog/ai/best-agent-browsers)

## Related
- [[MOC-Plugin-Ecosystem]]
- [[MOC-Trending-Agents]]
