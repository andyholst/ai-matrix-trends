---
id: 202609202000
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - tool
  - config
links:
  - [[MOC-Plugin-Ecosystem]]
  - [[MOC-Trending-Agents]]
---

# Jev Agent Router

## Overview
Jev Agent Router is a Hermes plugin that integrates the Jev context engine into Hermes Agent. It provides a skill plus a stdio MCP server (`agent_route`) for intelligent context management. Jev selects what to keep rather than summarizing, cutting roughly 75% of context usage while preserving every user and agent message verbatim — only old tool outputs are candidates for pruning. This makes it especially valuable for long-running sessions where context bloat degrades performance.

## Installation
```bash
# Clone the plugin from the Hermes plugin catalog
hermes plugins install jev-agent-router

# Or install directly from source
git clone https://github.com/NousResearch/hermes-agent ~/.hermes/plugins/jev-agent-router
```

Requires `uv` on PATH. The plugin registers as a skill plus a stdio MCP server started with `uv run` from the checkout directory. It does not register `jev_*` tools on the Hermes side — the MCP server handles routing decisions internally.

## Configuration
```yaml
# In your Hermes config.yaml, the MCP server is auto-discovered.
# No additional configuration needed beyond installing the plugin.
# The agent_route server starts automatically when Hermes boots.
```

## Use Cases
- Long-running agent sessions where context window saturation is a problem
- Multi-step coding tasks that accumulate large tool outputs
- Research workflows that need sustained context without manual summarization
- Anyone running Hermes Desktop who wants automatic context pruning

## Compatibility
- **Agent:** [[Hermes]]
- **Versions:** Hermes Agent 1.0+
- **Dependencies:** uv, Python 3.10+

## Related Plugins
- [[hermes-telemetry]] — Track token savings from context pruning
- [[jekyll-hyde]] — Alternative context optimization approach
- [[skill-router]] — Route skills based on evidence

## Sources
- [Hermes Plugin Catalog](https://hermes-agent.nousresearch.com/docs/plugins)
- [Reddit: Jev Context Engine Integration](https://www.reddit.com/r/hermesagent/comments/1wkpl3q/integrated_the_jev_context_engine_into_hermes/)
