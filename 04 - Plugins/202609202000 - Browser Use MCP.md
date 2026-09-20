---
id: 202609202000
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - tool
  - mcp
links:
  - "[[MOC-Plugin-Ecosystem]]"
  - "[[MOC-Trending-Agents]]"
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
- **Agent:** [[202609202000 - Claude Code]], [[202609202000 - Cursor]], [[202609200800 - Windsurf]], [[202609200758 - OpenCode]]
- **Versions:** browser-use 0.4+, Python 3.10+, uv
- **Dependencies:** Chrome or Chromium, uvx

## Related Plugins
- [[202609202000 - Browser Use MCP]] — Community fork with skills system and deep research workflow
- [[202609202011 - Chrome DevTools MCP]] — Chrome DevTools team's MCP for debugging and performance
- [[202609202000 - MCP Proxy Aggregator Pattern]] — Safari-only MCP server for macOS users

## Sources
- [Browser Use Docs: MCP Server](https://docs.browser-use.com/open-source/customize/integrations/mcp-server)
- [Browser Use GitHub](https://github.com/browser-use/browser-use)
