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

# OpenCode Supermemory

## Overview
OpenCode Supermemory is a plugin that gives OpenCode agents persistent memory across sessions. It uses the Supermemory engine to store project configuration, architecture decisions, error solutions, user preferences, and learned patterns. On session start, relevant memories are injected into the agent's context automatically. The plugin also detects phrases like "remember" or "save this" to trigger automatic storage, and summarizes sessions at 80% context capacity to prevent data loss.

## Installation
```bash
# Install the plugin
bunx opencode-supermemory@latest install

# For non-interactive / LLM-driven setups
bunx opencode-supermemory@latest install --no-tui

# Authenticate via browser login
bunx opencode-supermemory@latest login
```

For self-hosted Supermemory (fully local, no cloud):
```bash
npx supermemory local
# Then set apiKey and base URL in ~/.config/opencode/supermemory.jsonc
```

## Configuration
```jsonc
// ~/.config/opencode/supermemory.jsonc
{
  "apiKey": "sm_...",                    // Or use SUPERMEMORY_API_KEY env var
  "similarityThreshold": 0.6,            // Minimum match score (0-1)
  "maxMemories": 5,                      // Memories injected per session start
  "maxProjectMemories": 10,              // Project memory listings
  "maxProfileItems": 5,                  // Profile facts injected
  "injectProfile": true,                 // Include user preferences
  "compactionThreshold": 0.80            // Context usage ratio for summarization
}
```

Memory scopes: `user` (cross-project) and `project` (isolated to current project). Content inside `<private>` tags never persists.

## Use Cases
- Long-running projects where context continuity matters
- Remembering architecture decisions and coding conventions across sessions
- Building up a knowledge base of common errors and solutions
- Personalizing the agent to your coding style over time
- Onboarding to a new codebase by pre-loading project memory

## Compatibility
- **Agent:** [[202609200758 - OpenCode]], [[202609202000 - Claude Code]] (via separate plugin)
- **Versions:** OpenCode 1.0+, bun or npx
- **Dependencies:** Supermemory account or self-hosted instance

## Related Plugins
- [[202609200758 - OpenCode]] — Same plugin, Claude Code variant
- [[202609200805 - Hermes Kanban Dashboard]] — Memory dashboard for Hermes
- [[202609200805 - Hermes Kanban Dashboard]] — Local memory visualization for Hermes

## Sources
- [Supermemory Docs: OpenCode](https://supermemory.ai/docs/integrations/opencode)
- [OpenCode Supermemory GitHub](https://github.com/supermemoryai/opencode-supermemory)
- [Supermemory Blog: OpenCode Memory](https://supermemory.ai/blog/opencode-memory/)
