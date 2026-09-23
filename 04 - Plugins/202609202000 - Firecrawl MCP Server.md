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

# Firecrawl MCP Server

## Overview
The official Firecrawl MCP Server brings web scraping, crawling, and search capabilities to any MCP-compatible AI coding agent. It provides a clean set of tools — `firecrawl_scrape`, `firecrawl_search`, `firecrawl_crawl`, `firecrawl_map`, `firecrawl_parse`, and `firecrawl_agent` — that let agents fetch live web content as structured markdown instead of relying on stale training data or snippets. The server runs via npx and only needs a Firecrawl API key.

## Installation
```bash
# Add to any MCP-compatible client (Claude Code, Cursor, Codex, Windsurf, OpenCode)
# Via npx (no global install needed)
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-YOUR_API_KEY"
      }
    }
  }
}
```

## Configuration
```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-your-key-here"
      }
    }
  }
}
```

Set `FIRECRAWL_API_KEY` in your environment or `.env` file. The key is `fc-` prefixed. Available tools: `firecrawl_scrape` (single URL to markdown/HTML/structured), `firecrawl_search` (web search with content), `firecrawl_crawl` (full site crawl), `firecrawl_map` (URL discovery), `firecrawl_parse` (extract structured data from pages), `firecrawl_agent` (autonomous agent with prompt + schema).

## Use Cases
- Research workflows that need current web content
- Competitive analysis by scraping pricing or feature pages
- Building datasets from web sources
- Monitoring sites for changes via crawl
- Answering questions that require live information beyond the agent's training cutoff

## Compatibility
- **Agent:** [202609202000 - Claude Code](../03%20-%20Agents/202609202000%20-%20Claude%20Code.md), [202609202000 - Cursor](../03%20-%20Agents/202609202000%20-%20Cursor.md), [202609202000 - Codex](../03%20-%20Agents/202609202000%20-%20Codex.md), [202609200800 - Windsurf](../03%20-%20Agents/202609200800%20-%20Windsurf.md), [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md)
- **Versions:** Any MCP-compatible client
- **Dependencies:** Node.js 18+, npx, Firecrawl API key

## Related Plugins
- [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md) — OpenCode-specific wrapper around the same CLI
- [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md) — Alternative web search plugin for OpenCode
- [202609202000 - MCP Proxy Aggregator Pattern](../05%20-%20Architecture/202609202000%20-%20MCP%20Proxy%20Aggregator%20Pattern.md) — Unified MCP gateway that includes scraping tools

## Sources
- [Firecrawl MCP Server GitHub](https://github.com/firecrawl/firecrawl-mcp-server)
- [Firecrawl Docs: AI MCPs](https://www.firecrawl.dev/use-cases/ai-mcps)
- [Firecrawl Blog: Best MCP Servers](https://www.firecrawl.dev/blog/best-mcp-servers-for-developers)

## Related
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md)
- [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)
