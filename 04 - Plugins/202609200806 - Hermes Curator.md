---
id: 202609200806
created: 2026-09-20T08:06:00+02:00
tags:
  - plugin
  - hermes
  - tool
links:
  - "[[MOC-Plugin-Ecosystem]]"
  - "[[MOC-Trending-Agents]]"
---

# Hermes Curator

## Overview
Curator is a built-in Hermes Agent plugin that automatically manages the skill catalog — pruning stale skills, archiving unused ones, and optionally consolidating redundant skills into umbrella skills. It runs on a configurable cycle (default 7 days), tracks skill provenance (agent-created vs bundled vs unmanaged), and maintains a full audit ledger of every mutation. Curator solves the problem of skill bloat in long-running Hermes deployments where agents continuously create new skills but never clean up old ones. It supports dry-run previews, manual pinning, and rollback from snapshots.

## Installation
```bash
# Enable the curator plugin
hermes plugins enable curator

# Check status
hermes curator status

# Run a prune cycle (dry-run first)
hermes curator run --dry-run
hermes curator run

# Take a backup before running
hermes curator backup
```

## Configuration
```yaml
curator:
  enabled: true
  interval_hours: 168          # 7 days
  min_idle_hours: 2
  stale_after_days: 14
  archive_after_days: 30
  consolidate: false           # LLM umbrella-building pass — opt-in
  prune_builtins: false        # opt in to archiving unused bundled skills
```

## Use Cases
- Automatic cleanup of agent-created skills that have gone stale
- Auditing skill provenance (who created what, when)
- Rolling back skill changes via snapshot restore
- Bulk-pruning skills idle for N days
- Adopting unmanaged skills into curator governance

## Compatibility
**Agent:** [[202609200759 - Hermes Agent]]
**Versions:** Hermes Agent 1.0+
**Dependencies:** None (built-in)

## Related Plugins
- [[202609202506 - Hermes Kanban Dashboard]] — Kanban workers create skills; Curator keeps the catalog clean
- [[202609202000 - Jev Agent Router]] — Jev can help decide which skills to prune or consolidate

## Sources
- [Hermes Docs: Curator](https://hermes-agent.nousresearch.com/docs/user-guide/features/curator)
- [YouTube: Hermes Agent Curator Guide](https://www.youtube.com/watch?v=SpFgS7WlCJc)
