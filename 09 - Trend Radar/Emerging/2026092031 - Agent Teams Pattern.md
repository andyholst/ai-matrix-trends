---
id: 2026092031
created: 2026-09-20T31:00:00+02:00
tags:
  - trend
  - architecture
  - multi-agent
links:
  - "[[2026092032 - Agent Teams Pattern]]"
  - "[[2026092031 - Sub-Agent Delegation Pattern]]"
---

# Agent Teams Pattern

## Core Idea
Agent Teams extend sub-agent delegation with coordination primitives — shared task lists with dependency tracking, peer-to-peer messaging between teammates, and file locking — enabling true parallel execution of multiple agents working on the same codebase.

## Details
The architecture has three layers: a Team Lead that decomposes work and monitors progress, a Shared Task List with statuses (pending, in_progress, completed, blocked) and automatic dependency resolution, and Teammates that are independent agent instances running in isolated worktrees.

When a teammate marks a task complete, any blocked tasks that depended on it automatically unblock. Teammates can message each other directly (e.g., backend sends frontend the API contract) without going through the lead, preventing the lead from becoming a coordination bottleneck.

## Implications
Agent Teams represent the evolution from simple sub-agent delegation to true multi-agent collaboration. The pattern is being explored experimentally by Claude Code (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) and implemented in tools like Conductor. As agent tasks grow more complex, team-based coordination will become essential.

## Related
- [[2026092032 - Agent Teams Pattern]]
- [[2026092031 - Sub-Agent Delegation Pattern]]
- [[202609202020 - Orchestrator-Worker Delegation Pattern]]

## Sources
- [Addy Osmani — Code Agent Orchestra](https://addyosmani.com/blog/code-agent-orchestra/)
