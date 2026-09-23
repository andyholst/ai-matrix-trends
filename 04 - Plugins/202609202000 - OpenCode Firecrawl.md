---
id: 202609202000
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - tool
  - config
agents:
  - opencode
---



# OpenCode Firecrawl

## Overview
OpenCode Firecrawl is a plugin that integrates Firecrawl's web scraping, crawling, and search capabilities directly into OpenCode, the open-source terminal AI coding agent. It wraps the Firecrawl CLI and exposes tools like `firecrawl search`, `firecrawl scrape`, `firecrawl crawl`, `firecrawl map`, and `firecrawl interact` (for live browser sessions). The plugin writes results to files rather than flooding the context window, which keeps token usage manageable during research-heavy tasks.

## Installation
```bash
# Add to your OpenCode config
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-firecrawl"]
}

# Install the Firecrawl CLI globally
npm install -g firecrawl-cli

# Or use npx for on-demand use without global install
npx -y firecrawl-cli@latest init --all --browser
```

## Configuration
```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-firecrawl"]
}
```

Set `FIRECRAWL_API_KEY` in your environment for authenticated higher-rate access. Without a key, the plugin works with shared public-IP rate limits. The `--browser` flag during init enables the `firecrawl interact` tool for live browser sessions.

## Use Cases
- Researching current documentation or release notes without leaving the editor
- Scraping competitor pricing or feature pages into comparison tables
- Crawling a documentation site to find all pages mentioning a specific feature
- Building a local knowledge base from web sources
- Answering "what's the latest..." questions with live data

## Compatibility
- **Agent:** [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md)
- **Versions:** OpenCode 1.0+, Node.js 18+
- **Dependencies:** firecrawl-cli (npm), Firecrawl API key (recommended)

## Related Plugins
- [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md) — Alternative search/scrape plugin using Tavily
- [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md) — Native web search with citation grounding
- [202609202000 - Firecrawl MCP Server](202609202000%20-%20Firecrawl%20MCP%20Server.md) — The MCP-server version for non-OpenCode agents

## Sources
- [OpenCode Firecrawl GitHub](https://github.com/firecrawl/opencode-firecrawl)
- [OpenCode Ecosystem Docs](https://opencode.ai/docs/ecosystem/)
- [Firecrawl Blog: Best OpenCode Skills](https://www.firecrawl.dev/blog/best-opencode-skills)

## Related
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md)
- [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)
