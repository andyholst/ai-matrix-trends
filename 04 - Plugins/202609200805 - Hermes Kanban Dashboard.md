---
id: 202609200805
created: 2026-09-20T08:05:00+02:00
tags:
  - plugin
  - hermes
  - tool
links:
  - [[MOC-Plugin-Ecosystem]]
  - [[MOC-Trending-Agents]]
---

# Hermes Kanban Dashboard

## Overview
The Kanban Dashboard is a built-in Hermes Agent plugin that provides a visual Kanban board UI for the multi-agent dispatcher. It enables durable multi-agent task management — tasks survive restarts, can be fanned out to worker agents, and track progress across columns (e.g., backlog, in-progress, review, done). The dashboard ships as a Hermes dashboard tab and is opt-in. It is the primary interface for managing long-running, parallel agent workflows where multiple workers collaborate on a shared task queue.

## Installation
```bash
# Install Hermes with web and PTY support
pip install 'hermes-agent[web,pty]'

# Enable the kanban plugin
hermes plugins enable kanban/dashboard

# Load the orchestrator and worker skills
hermes skills load devops/kanban-orchestrator
hermes skills load devops/kanban-worker

# Start the dashboard
hermes dashboard
```

## Configuration
```yaml
# In your Hermes config.yaml
plugins:
  kanban/dashboard:
    enabled: true
```

## Use Cases
- Multi-agent task fan-out — dispatch tasks from the board to worker agents
- Long-running work that must survive agent restarts
- Visual progress tracking for parallel agent pipelines
- Coordinating sub-agents on large refactors or research tasks

## Compatibility
**Agent:** [[Hermes]]
**Versions:** Hermes Agent 1.0+ (requires `hermes-agent[web,pty]`)
**Dependencies:** pip, PTY support

## Related Plugins
- [[202609200806 - Hermes Curator]] — Pair with Curator for lifecycle management of the skills used by Kanban workers
- [[202609202000 - Jev Agent Router]] — Use Jev for intelligent routing decisions within Kanban workflows

## Sources
- [Hermes Docs: Built-in Plugins](https://hermes-agent.nousresearch.com/docs/user-guide/features/built-in-plugins)
- [Firecrawl: 9 Best Hermes Tools](https://www.firecrawl.dev/blog/best-hermes-plugins)
