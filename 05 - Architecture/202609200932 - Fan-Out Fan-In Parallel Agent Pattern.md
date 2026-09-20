---
id: 202609200932
created: 2026-09-20T09:32:00+02:00
tags:
  - architecture
links:
  - "[Orchestrator-Worker Delegation Pattern](./05%20-%20Architecture/202609202020%20-%20Orchestrator-Worker%20Delegation%20Pattern.md)"
  - "[Orchestrator Worker Multi-Agent Delegation](./05%20-%20Architecture/202609202024%20-%20Orchestrator%20Worker%20Multi-Agent%20Delegation.md)"
---

# Fan-Out / Fan-In Parallel Agent Pattern

## Core Idea
A dispatcher sends the same input (or independent subtasks) to multiple agents running in parallel, then a collector aggregates their results using voting, weighted merging, or LLM-based synthesis — cutting wall-clock time by running independent work concurrently.

## How It Works
```
                    ┌─────────────────┐
                    │   Dispatcher    │
                    │  (splits input) │
                    └────────┬────────┘
           ┌─────────────────┼─────────────────┐
           │                 │                 │
     ┌─────▼─────┐    ┌─────▼─────┐    ┌─────▼─────┐
     │ Agent A   │    │ Agent B   │    │ Agent C   │
     │(Security) │    │(Style)    │    │(Performance)│
     └─────┬─────┘    └─────┬─────┘    └─────┬─────┘
           │                 │                 │
           └─────────────────┼─────────────────┘
                    ┌────────▼────────┐
                    │    Collector    │
                    │ (aggregates via │
                    │ voting/merging/ │
                    │ LLM synthesis)  │
                    └─────────────────┘
```

1. **Fan-out**: The dispatcher distributes work to N agents simultaneously. Agents may receive the same input (multi-perspective analysis) or different subtasks (parallel processing).
2. **Parallel execution**: All agents work independently with no inter-agent communication during execution.
3. **Fan-in**: The collector gathers all results and aggregates them using one of:
   - **Voting**: majority decision (classification, yes/no decisions)
   - **Weighted merging**: weighted average or priority-based combination
   - **LLM-based synthesis**: an LLM merges perspectives into a coherent output
4. **Conflict resolution**: When agents disagree, the aggregation strategy determines the final output (e.g., LLM synthesis can reconcile contradictions).

## When to Use
- Multi-perspective analysis: financial analysis with fundamental, technical, sentiment, and ESG agents
- Concurrent code review across security, style, and performance dimensions
- Any scenario with 4+ independent tasks where wall-clock time matters
- Redundancy and reliability: run the same task on multiple agents and vote
- A/B testing different approaches simultaneously

## Tradeoffs
- **Pros:**
  - Cuts wall-clock time by up to 75% for independent tasks
  - Multi-perspective analysis improves decision quality
  - Natural fit for embarrassingly parallel problems
  - Can improve reliability through redundancy (voting)
- **Cons:**
  - API rate limits: N concurrent agents can collectively exceed capacity even when each is within limits individually
  - Race conditions on shared state scale quadratically: N agents → N(N-1)/2 potential conflicts
  - Aggregation step introduces error — LLM synthesis can hallucinate consensus
  - Resource-intensive: N agents × token cost per agent
  - Requires explicit conflict resolution strategy when agents disagree

## Examples
- Financial analysis: fundamental, technical, sentiment, and ESG agents running in parallel on the same stock
- Code review: security, style, and performance agents reviewing the same PR simultaneously
- Multi-model consensus: running the same prompt on GPT-5, Claude, and Gemini, then voting on the best response

## Related Patterns
- [[202609202020 - Orchestrator-Worker Delegation Pattern]] — orchestrator-worker is sequential delegation; fan-out/fan-in is parallel
- [[202609202024 - Orchestrator Worker Multi-Agent Delegation]] — similar but typically sequential or dependency-ordered
- [[MOC-Trending-Agents]] — context engineering needed to manage the collector's aggregation context

## Sources
- Beam AI: "6 Multi-Agent Orchestration Patterns for Production (2026)" — Fan-out/fan-in (https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production)
- Microsoft Azure Architecture Center: "AI Agent Orchestration Patterns" — Concurrent orchestration (https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)

## Related
- [[MOC-Trending-Agents]]
