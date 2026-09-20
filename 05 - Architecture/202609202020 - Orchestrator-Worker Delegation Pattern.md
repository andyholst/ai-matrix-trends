---
id: 202609202020
created: 2026-09-20T20:20:00+02:00
tags:
  - architecture
aliases:
  - Orchestrator-Worker Pattern
  - Manager-Worker Pattern
links:
links:
  - "[Context Engineering for Long-Horizon Agents](./05%20-%20Architecture/202609202001%20-%20Context%20Engineering%20for%20Long-Horizon%20Agents.md)"
  - "[Multi-Agent Orchestration with Guardrail Layering](./05%20-%20Architecture/202609202002%20-%20Multi-Agent%20Orchestration%20with%20Guardrail%20Layering.md)"
---

# Orchestrator-Worker Delegation Pattern

## Core Idea
A capable orchestrator agent decomposes a task into subtasks, delegates each to a specialist worker agent, and assembles the results — enabling cost optimization through heterogeneous model tiers.

## How It Works
1. The orchestrator receives a user request and decomposes it into discrete subtasks.
2. Each subtask is dispatched to a worker agent (a cheaper, task-specific model or a domain specialist).
3. Workers execute in isolation, often with clean context windows and scoped tools.
4. The orchestrator aggregates worker outputs, resolves conflicts, and returns a unified result.

This pattern works when the subtask decomposition is known at design time and a single accountability point is desired. The orchestrator uses a capable model (e.g., GPT-5, Claude Opus) while workers use cheaper, faster models (e.g., Haiku, GPT-4o-mini), cutting costs 40–60%.

## When to Use
- Cross-functional workflows with clear task decomposition (customer service routing, multi-domain research).
- Scenarios needing a single point of accountability for the overall result.
- Cost-sensitive deployments where a single capable model is too expensive for every subtask.
- Parallelizable subtasks that can run concurrently.

## Tradeoffs
- **Pros:**
  - Cost savings of 40–60% by using cheaper worker models.
  - Clean separation of concerns; workers are independently deployable and testable.
  - Scalable — add new workers for new domains without changing the orchestrator.
- **Cons:**
  - Orchestrator is a single point of failure; misclassification compounds at scale.
  - Context window overflow at the orchestrator when aggregating results from 4+ workers.
  - Latency from decomposition + aggregation LLM calls on top of every worker call.

## Examples
- [202609202002 - Multi-Agent Orchestration with Guardrail Layering](./05%20-%20Architecture/202609202002%20-%20Multi-Agent%20Orchestration%20with%20Guardrail%20Layering.md) — Guardrail layering applied to orchestrator-worker pipelines.
- [MOC-Trending-Agents](./07%20-%20Structure/MOC-Trending-Agents.md) — Managing orchestrator context across many worker handoffs.

## Related Patterns
- [202609202000 - MCP Proxy Aggregator Pattern](./05%20-%20Architecture/202609202000%20-%20MCP%20Proxy%20Aggregator%20Pattern.md) — Worker agents exposed behind an MCP proxy for tool-based delegation.

## Sources
- https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
