---
id: 2026092031
created: 2026-09-20T31:00:00+02:00
tags:
  - architecture
  - sub-agent
  - orchestration
links:
  - "[[202609202001 - Context Engineering for Long-Horizon Agents]]"
  - "[[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]"
---

# Sub-Agent Delegation Pattern

## Core Idea
A parent orchestrator agent decomposes a task into focused sub-tasks and delegates each to a specialized child agent with a self-contained prompt, isolated context window, and scoped tools, then aggregates the condensed results.

## How It Works
The parent agent receives a user request and breaks it into independent or dependent sub-tasks. For each sub-task, it writes a self-contained prompt describing the work, spawns a fresh child agent with access to required tools, and the child executes in its own clean context window. The child returns only a condensed summary (typically 1,000–2,000 tokens) back to the parent, not the full execution trajectory.

Key properties:
- **Prompt self-containment** — the child cannot see the parent's context; everything it needs must be in the prompt. This forces clean decomposition.
- **Context isolation** — each sub-agent explores extensively (potentially tens of thousands of tokens) but the parent only sees the distilled result.
- **Hierarchical delegation** — sub-agents can spawn their own sub-agents (teams of teams), enabling 3x deeper decomposition without exploding any single context window.
- **Parallel execution** — independent sub-agents run concurrently; dependent ones wait for prerequisite results.

The parent manages the dependency graph manually, tracking which sub-agents have completed and which are still running.

## When to Use
- Tasks decomposable into clear, focused sub-tasks
- When the parent's context would be polluted by raw tool outputs (grep results, file contents)
- When different sub-tasks need different model capabilities or tool sets
- When parallel execution of independent sub-tasks speeds up the overall workflow

## Tradeoffs
- **Pros:** Context isolation per agent; specialization; parallel execution for independent tasks; cost-neutral at scale; parent context stays lean
- **Cons:** Parent must manually manage dependency graph; no peer messaging between sub-agents; no shared task list; requires careful file scoping to avoid conflicts; vague delegation produces vague results

## Examples
- [[202609202000 - Claude Code]] — Task tool spawns sub-agents with markdown-defined briefs
- Spring AI — Task tool implementation inspired by Claude Code's subagents, model-agnostic

## Related Patterns
- [[2026092030 - Context Engineering]], [[2026092032 - Agent Teams Pattern]], [[202609202020 - Orchestrator-Worker Delegation Pattern]]

## Sources
- https://addyosmani.com/blog/code-agent-orchestra/
- https://spring.io/blog/2026/01/27/spring-ai-agentic-patterns-4-task-subagents/
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
