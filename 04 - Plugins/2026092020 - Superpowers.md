---
id: 2026092020
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - claude-code
  - skills
agents:
  - claude-code
---

# Superpowers

## Overview
Superpowers is an agentic skills framework and software development methodology packaged as a Claude Code plugin. It provides a curated collection of skills covering the full development lifecycle — brainstorming, planning, test-driven development, systematic debugging, code review, and worktree management. With 200K+ GitHub stars, it is one of the most popular community-built plugin frameworks for Claude Code.

## Installation
```bash
# From the official Claude marketplace
/plugin install superpowers@claude-plugins-official

# Or via npx skills CLI
npx skills add obra/superpowers
```

## Configuration
```yaml
# No mandatory config — skills are invoked on demand
# Available skills include:
#   - brainstorming
#   - planning
#   - tdd (test-driven development)
#   - systematic-debugging
#   - code-review
#   - worktrees
#   - subagent-driven-development
```

## Use Cases
- Structured feature development from idea to shipped code
- Enforcing TDD workflows inside Claude Code sessions
- Parallel subagent execution via git worktrees
- Systematic debugging with root-cause analysis steps
- Code review with actionable feedback loops

## Compatibility
- **Agent:** [202609202000 - Claude Code](../03%20-%20Agents/202609202000%20-%20Claude%20Code.md)
- **Versions:** Claude Code v2.x+

## Related Plugins
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md), [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)

## Sources
- [GitHub](https://github.com/obra/superpowers)
- [Official Marketplace](https://claude.com/plugins/superpowers)
