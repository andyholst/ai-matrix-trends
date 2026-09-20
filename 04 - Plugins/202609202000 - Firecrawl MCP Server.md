---
id: 202609202000
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - tool
  - mcp
links:
  - [[MOC-Plugin-Ecosystem]]
  - [[MOC-Trending-Agents]]
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
- **Agent:** [[202609202000 - Claude Code]], [[Cursor]], [[202609202000 - Codex]], [[Windsurf]], [[OpenCode]]
- **Versions:** Any MCP-compatible client
- **Dependencies:** Node.js 18+, npx, Firecrawl API key

## Related Plugins
- [[opencode-firecrawl]] — OpenCode-specific wrapper around the same CLI
- [[opencode-tavily]] — Alternative web search plugin for OpenCode
- [[202609202000 - MCP Proxy Aggregator Pattern]] — Unified MCP gateway that includes scraping tools

## Sources
- [Firecrawl MCP Server GitHub](https://github.com/firecrawl/firecrawl-mcp-server)
- [Firecrawl Docs: AI MCPs](https://www.firecrawl.dev/use-cases/ai-mcps)
- [Firecrawl Blog: Best MCP Servers](https://www.firecrawl.dev/blog/best-mcp-servers-for-developers)
