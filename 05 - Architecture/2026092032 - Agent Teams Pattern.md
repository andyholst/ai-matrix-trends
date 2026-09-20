---
id: 2026092032
created: 2026-09-20T32:00:00+02:00
tags:
  - architecture
  - agent-teams
  - parallel-execution
---

# Agent Teams Pattern

## Core Idea
Agent Teams extend sub-agent delegation with coordination primitives: a shared task list with dependency tracking, peer-to-peer messaging between teammates, and file locking to prevent conflicts — enabling true parallel execution of multiple agents working on the same codebase.

## How It Works
The architecture has three layers:

1. **Team Lead** — decomposes work, creates the shared task list, synthesizes results, and monitors progress. The lead does not do implementation work itself.
2. **Shared Task List** — tasks have statuses (pending, in_progress, completed, blocked), explicit dependency tracking, and file locking. When a teammate marks a task complete, any blocked tasks that depended on it automatically unblock.
3. **Teammates** — each is an independent agent instance with its own context window, running in isolated worktrees (git worktrees or tmux panes). Teammates self-claim tasks from the shared list.

Two mechanisms make Agent Teams work:
- **Shared task list with automatic dependency resolution** — when the backend teammate marks the search API as completed, the blocked test-writing task automatically flips to pending and a teammate picks it up.
- **Peer-to-peer messaging** — teammates message each other directly (e.g., backend sends frontend the API contract) without going through the lead, preventing the lead from becoming a coordination bottleneck.

File locking prevents two teammates from editing the same file simultaneously. Each agent works in its own git worktree for isolation.

## When to Use
- Multiple agents working on the same codebase in parallel
- Tasks with interdependent components (backend → frontend → tests)
- When coordination overhead of manual sub-agent management becomes the bottleneck
- When you need automatic dependency resolution and parallel unblocking

## Tradeoffs
- **Pros:** True parallel execution; automatic dependency resolution; peer messaging prevents lead bottleneck; file locking prevents conflicts; compound learning via AGENTS.md
- **Cons:** More complex setup than simple sub-agents; requires git worktrees or similar isolation; WIP limits needed (3–5 agents sweet spot); vague specs multiply errors across the fleet; verification becomes the bottleneck, not generation

## Examples
- [[Claude Code]] — experimental Agent Teams feature (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
- [[Conductor]] — local orchestrator managing agents in isolated worktrees

## Related Patterns
- [[Sub-Agent Delegation]], [[Context Engineering]], [[Orchestrator-Worker]]

## Sources
- https://addyosmani.com/blog/code-agent-orchestra/
