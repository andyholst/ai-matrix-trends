---
id: 202609202000
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - tool
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



# Browser Use MCP

## Overview
Browser Use MCP is a local Model Context Protocol server that gives AI coding agents direct browser automation capabilities. It exposes low-level tools for navigation, clicking, typing, content extraction, and session management. The server runs in stdio mode on your machine and connects to any MCP-compatible agent — Claude Code, Claude Desktop, Cursor, Windsurf, and OpenCode. It uses your own LLM API keys (OpenAI or Anthropic) to drive the agent loop.

## Installation
```bash
# For Claude Code
claude mcp add browser-use -- uvx --from 'browser-use[cli]' browser-use --mcp

# For Claude Desktop / Cursor, add to the MCP config:
# ~/.cursor/mcp.json or claude_desktop_config.json
{
  "mcpServers": {
    "browser-use": {
      "command": "uvx",
      "args": ["--from", "browser-use[cli]", "browser-use", "--mcp"],
      "env": {
        "OPENAI_API_KEY": "your-key"
      }
    }
  }
}
```

## Configuration
```json
{
  "mcpServers": {
    "browser-use": {
      "command": "uvx",
      "args": ["--from", "browser-use[cli]", "browser-use", "--mcp"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key",
        "BROWSER_USE_HEADLESS": "true"
      }
    }
  }
}
```

Key environment variables: `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` (one required), `BROWSER_USE_HEADLESS` (set to `false` to see the browser), `BROWSER_USE_LOGGING_LEVEL=DEBUG` for troubleshooting.

## Use Cases
- Web scraping and data extraction from dynamic pages
- Automated testing and QA of web applications
- Filling forms or interacting with web UIs on behalf of the user
- Research tasks that require browsing multiple pages
- Any agent task that needs a real browser environment

## Compatibility
- **Agent:** [202609202000 - Claude Code](../03%20-%20Agents/202609202000%20-%20Claude%20Code.md), [202609202000 - Cursor](../03%20-%20Agents/202609202000%20-%20Cursor.md), [202609200800 - Windsurf](../03%20-%20Agents/202609200800%20-%20Windsurf.md), [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md)
- **Versions:** browser-use 0.4+, Python 3.10+, uv
- **Dependencies:** Chrome or Chromium, uvx

## Related Plugins
- [202609202000 - Browser Use MCP](202609202000%20-%20Browser%20Use%20MCP.md) — Community fork with skills system and deep research workflow
- [202609202011 - Chrome DevTools MCP](202609202011%20-%20Chrome%20DevTools%20MCP.md) — Chrome DevTools team's MCP for debugging and performance
- [202609202000 - MCP Proxy Aggregator Pattern](../05%20-%20Architecture/202609202000%20-%20MCP%20Proxy%20Aggregator%20Pattern.md) — Safari-only MCP server for macOS users

## Sources
- [Browser Use Docs: MCP Server](https://docs.browser-use.com/open-source/customize/integrations/mcp-server)
- [Browser Use GitHub](https://github.com/browser-use/browser-use)

## Related
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md)
- [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)
