---
id: 2026092040
created: 2026-09-20T40:00:00+02:00
tags:
  - workflow
  - multi-agent
  - orchestration

---

# Multi-Agent Team Orchestration for Parallel Development

## Overview

Multi-agent team orchestration is the practice of running multiple AI coding agents in parallel, each with its own context window, file scope, and area of responsibility, while a developer (or lead agent) coordinates from above. This pattern has emerged as the primary way to scale AI-assisted coding beyond the single-agent ceiling.

## The Shift: Conductor to Orchestrator

The mental model has shifted from pair programming (one agent, synchronous, context-window-limited) to managing an agent team (multiple agents, asynchronous, specialized). Addy Osmani frames this as the shift from "conductor" to "orchestrator" — the codebase becomes the canvas, not a conversation thread.

## Why Multi-Agent?

Three walls motivate the move beyond a single agent:

- **Context overload** — Large codebases overwhelm a single context window. Multiple agents each carry their own context.
- **No specialization** — A focused agent that only handles the data layer writes better database code than a generalist juggling the entire codebase.
- **No coordination** — Agents need shared task lists, dependency tracking, and communication channels to work together.

Four compounding benefits: parallelism (3x throughput), specialization (focused context), isolation (git worktrees prevent conflicts), and compound learning (AGENTS.md accumulates patterns across sessions).

## Key Patterns

### Pattern 1: Subagents (Focused Delegation)

The simplest multi-agent pattern. A parent orchestrator uses the Task tool to spawn specialized child agents. Each subagent gets a specific brief and file ownership. Zero setup required — available today in Claude Code and Codex.

### Pattern 2: Agent Teams (True Parallel Execution)

Multiple coordinated sessions with a shared task list and inter-agent messaging, managed by a lead agent. Claude Code's experimental Agent Teams feature enables this with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. VS Code now supports running Claude, Codex, and Copilot agents side by side with parallel subagents.

### Pattern 3: Git Worktrees for Isolation

Each agent gets its own git worktree — a separate branch and working directory. No merge conflicts while agents work. Tools like Conductor (Melty Labs) handle this automatically, running multiple Claude Code and Codex agents in parallel with a visual dashboard and diff-first review UI.

### Pattern 4: The Factory Model (Production Line)

A six-step production line: Plan (specs with acceptance criteria) → Spawn (create team, assign agents) → Monitor (check progress every 5-10 minutes) → Verify (run tests, review code) → Integrate (merge branches) → Retro (update AGENTS.md with new patterns).

## Tools

- **Claude Code Agent Teams** — Experimental feature for coordinated multi-agent sessions
- **Codex Symphony** — Issue tracker as control plane, assigns an agent to every open ticket
- **Conductor (Melty Labs)** — Visual dashboard for running multiple agents in parallel with worktrees
- **VS Code Multi-Agent** — Run Claude, Codex, and Copilot agents in parallel with subagent support
- **oh-my-claudecode** — Orchestration layer on top of Claude Code using plugins, hooks, skills, and agent teams

## Practical Tips

- Set WIP limits: 3-5 agents is the sweet spot (more than you can review is waste)
- Define kill criteria: if an agent is stuck 3+ iterations on the same error, stop and reassign
- One file, one owner: never let two agents edit the same file
- Cap fan-out at what you can actually verify — more agents means more tokens and more review

## Related
- [[MOC-Architecture-Patterns]]
- [[MOC-Trending-Agents]]

- [[MOC-Architecture-Patterns]]
- [[MOC-Trending-Agents]]
