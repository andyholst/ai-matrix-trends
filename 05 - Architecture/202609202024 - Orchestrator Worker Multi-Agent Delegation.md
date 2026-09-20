---
id: 202609202024
created: 2026-09-20T20:24:00+02:00
tags:
  - architecture
  - multi-agent
  - orchestration
  - delegation
aliases:
links:
  - "[[202609202020 - Orchestrator-Worker Delegation Pattern]]"
  - "[[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]"
  - "[[202609202000 - Claude Code]]"
---

# Orchestrator-Worker Multi-Agent Delegation

## Core Idea
A lead orchestrator agent decomposes a task into subtasks and dispatches them to stateless worker agents, each with a specialized toolset and clean context window, then synthesizes results.

## How It Works
The orchestrator receives the user's goal, plans a decomposition (e.g., "analyze logs, query DB, generate report"), and invokes worker agents as tool calls. Workers are stateless — they receive only the subtask description and return a condensed result (typically 1,000–2,000 tokens). The orchestrator maintains the global context, decides when workers are needed, and merges their outputs into a final response. Workers can run in parallel when subtasks are independent. The orchestrator's system prompt encodes the planning logic and worker-selection heuristics.

```
User Goal ──► Orchestrator ──┬── Worker A (logs)    ──► result A
                             ├── Worker B (database) ──► result B
                             └── Worker C (report)   ──► result C
                                       │
                              Orchestrator synthesizes ──► Final response
```

## When to Use
- Tasks span multiple independent domains (e.g., code review + DB query + docs update)
- Subtasks are large enough to pollute a single context window if run sequentially
- You need parallel execution for latency reduction
- Workers need distinct tool permissions or model configurations

## Tradeoffs
- **Pros:** Strong context isolation per worker, parallel execution, worker specialization (different models/tools), clear separation of concerns
- **Cons:** One extra model call per orchestration hop, orchestrator becomes a bottleneck and single point of failure, result synthesis quality depends on orchestrator's prompt, harder to debug distributed traces

## Examples
- Anthropic's multi-agent research system (lead Claude Opus 4 + Sonnet 4 subagents) showed 90.2% improvement over single-agent on complex research
- A coding harness that delegates "search codebase" to one worker, "run tests" to another, and "update docs" to a third

## Related Patterns
- [[202609202020 - Orchestrator-Worker Delegation Pattern]]
- [[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]
- [[MOC-Trending-Agents]]

## Sources
- Anthropic Engineering: "How we built our multi-agent research system" (https://www.anthropic.com/engineering/multi-agent-research-system)
- LangChain Blog: "Choosing the Right Multi-Agent Architecture" (https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture)
- Azure Architecture Center: "AI agent orchestration patterns" (https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)

## Related
- [[MOC-Trending-Agents]]
