---
id: 2026092022
created: 2026-09-20T22:00:00+02:00
tags:
  - plugin
  - mcp
agents:
  - claude-code
  - opencode
  - cursor
  - codex
  - windsurf
  - aider
  - gemini-cli
  - github-copilot
  - kilo-code
  - roocode
  - jetbrains-junie
  - cline
  - hermes
---



# Browserbase MCP

## Overview
Browserbase MCP gives AI coding agents access to cloud-hosted, headless browsers via the Model Context Protocol. Built on Stagehand, it enables agents to navigate pages, click elements, fill forms, and extract content without running a local browser. The self-hosted npm package was archived in July 2026; the project now operates as a hosted HTTP endpoint at `https://mcp.browserbase.com/mcp`. With 3.4k+ stars, it is the cloud counterpart to Playwright MCP.

## Key Features
- **Cloud browsers:** Headless browser instances running in Browserbase's cloud
- **Stagehand integration:** Natural language or code-based browser automation
- **Session persistence:** Keep sessions alive across multiple agent interactions
- **Context management:** Reuse browser contexts with `--contextId`
- **Stealth mode:** Verified identity for sites that block headless browsers
- **Custom models:** Configure LLM provider (OpenAI, Anthropic, etc.) for Stagehand

## Installation
```bash
# Claude Code / Cursor (HTTP - hosted endpoint)
claude mcp add browserbase --transport http https://mcp.browserbase.com/mcp

# Claude Desktop
{
  "mcpServers": {
    "browserbase": {
      "url": "https://mcp.browserbase.com/mcp"
    }
  }
}
```

## Configuration
- `BROWSERBASE_API_KEY` — Browserbase API key
- `BROWSERBASE_PROJECT_ID` — Browserbase project ID
- `--modelName` — LLM for Stagehand (default: google/gemini-2.5-flash-lite)
- `--modelApiKey` — API key for custom model provider
- `--verified` — Enable verified identity (stealth mode)
- `--keepAlive` — Enable session keep-alive
- `--contextId` — Reuse a specific browser context

## Use Cases
- Browser automation for cloud-hosted agents that cannot run local browsers
- Web scraping with persistent sessions and login state
- Testing web applications from CI/CD pipelines
- Multi-step web workflows (form filling, navigation, data extraction)

## Compatibility
- **Agent:** Claude Code, Claude Desktop, Cursor, Windsurf, VS Code, OpenCode
- **Transports:** HTTP (hosted endpoint)
- **Auth:** Browserbase API key
- **Status:** Self-hosted package archived July 2026; use hosted endpoint

## Related
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md)
- [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md)
- [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)

## Sources
- [Browserbase MCP](https://github.com/browserbase/mcp-server-browserbase)
- [Browserbase MCP Docs](https://docs.browserbase.com/integrations/mcp/introduction)
