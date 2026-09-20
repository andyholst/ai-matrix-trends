---
id: 202609202002
created: 2026-09-20T20:00:00+02:00
tags:
  - architecture
  - workflow
  - config
links:
  - [[202609202000 - MCP Proxy Aggregator Pattern]]
  - [[AGENTS]]
---

# Multi-Agent Orchestration with Guardrail Layering

## Core Idea
A combination of fan-out/fan-in orchestration (parallel specialist agents with aggregated results) and guardrail layering (controls at four execution points: user input, tool calls, tool responses, and final output) to build production-ready multi-agent systems that are both fast and safe.

## How It Works

### Fan-Out/Fan-In Orchestration
Multiple agents execute simultaneously on independent subtasks. A dispatcher sends work out, and a collector aggregates results using voting, weighted merging, or LLM-based synthesis.

```
Dispatcher
  ├── Agent A (security review) ──┐
  ├── Agent B (style review) ─────┤
  ├── Agent C (performance review)┤── Collector (aggregation)
  └── Agent D (test generation) ──┘
```

Key design decisions:
- The orchestrator uses a capable model while workers use cheaper, task-specific ones (40-60% cost reduction)
- Aggregation strategies: voting (majority wins), weighted merging (by confidence), or LLM-based synthesis (a capable model merges outputs)
- For code review: concurrent review across security, style, and performance can cut wall-clock time by 75%

### Guardrail Layering (P11)
Rather than a single output-only check, guardrails are placed at four execution points:

1. **User input**: Validate and sanitize incoming user queries (prompt injection detection, content filtering, scope validation)
2. **Tool calls**: Validate tool call parameters before execution (allowlists, rate limits, budget checks, circuit breakers)
3. **Tool responses**: Sanitize tool outputs before they enter agent context (strip injected content, redact secrets, enforce size limits)
4. **Final output**: Validate the agent's response before returning to the user (safety classifiers, factual consistency checks, format enforcement)

```
User Input → [Guardrail 1: Input validation]
           → Agent Processing
           → [Guardrail 2: Tool call validation]
           → Tool Execution
           → [Guardrail 3: Tool response sanitization]
           → Agent Reasoning
           → [Guardrail 4: Final output validation]
           → User
```

### Bounded Execution / Circuit Breaker (P10)
Complementary to guardrail layering, bounded execution sets hard limits:
- Maximum step limits per agent
- Tool-call caps per session
- Idempotent tool design (safe to retry)
- Circuit breakers that halt execution when error rates exceed thresholds

## When to Use
- **Fan-out/fan-in**: Four or more independent tasks where wall-clock time matters; concurrent code review, multi-perspective financial analysis, parallel research across domains
- **Guardrail layering**: Any production agent system handling user-facing interactions or operating on sensitive data
- **Bounded execution**: Systems where runaway costs or infinite loops are a risk

## How to Pick the Right Orchestration Pattern
Start with the simplest pattern that fits. Princeton NLP found that a single agent matched or outperformed multi-agent systems on 64% of benchmarked tasks when given the same tools and context. Multi-agent adds 2.1 percentage points of accuracy at roughly double the cost.

| Pattern | When | Watch Out For |
|---|---|---|
| Orchestrator-worker | Known task decomposition | Orchestrator context overflow at 4+ workers |
| Sequential pipeline | Fixed linear steps | Error propagation, 3x token cost |
| Fan-out/fan-in | 4+ independent tasks | Rate limits, race conditions, aggregation errors |
| Multi-agent debate | Quality > speed | Conversation loops, sycophancy cascading |
| Dynamic handoff | Unpredictable routing | Infinite handoff loops, context loss |
| Adaptive planning | Open-ended problems | Goal drift, wasted compute on backtracking |

## Tradeoffs
- **Pros:**
  - 75% wall-clock reduction for independent parallel tasks
  - Cost savings of 40-60% by using cheaper models for workers
  - Multiple guardrail layers catch failures before they reach users
  - Bounded execution prevents runaway costs and infinite loops
  - Concurrent code review across security, style, and performance perspectives
- **Cons:**
  - API rate limits: 15 concurrent agents at 150 req/s can exceed a 100 req/s limit even when each agent is individually within limits
  - Race conditions on shared state scale quadratically (N agents = N(N-1)/2 potential conflicts)
  - LLM-based aggregation can hallucinate consensus that doesn't exist in underlying results
  - Guardrail layering adds latency at each checkpoint
  - 40% of multi-agent pilots fail within six months of production deployment

## Examples
- Concurrent code review: security, style, and performance agents run in parallel, then a collector synthesizes findings
- Financial analysis: fundamental, technical, sentiment, and ESG agents analyze the same security simultaneously
- Wells Fargo uses orchestrator-worker to give 35,000 bankers access to 1,700 procedures in 30 seconds (down from 10 minutes)
- Salesforce Agentforce 2.0 implements orchestrator-worker through the Atlas Reasoning Engine
- Microsoft documents an SRE using adaptive planning: the manager consults diagnostic and infrastructure agents, then pivots the entire plan when diagnostics reveal a database issue

## Anti-Patterns to Avoid
- **Output-only guardrails**: Checking only the final output while ignoring tool call parameters and tool responses
- **Unbounded execution**: No step limits or circuit breakers, allowing infinite loops
- **Over-architecting**: Using multi-agent when a single agent with the same tools would suffice

## Related Patterns
- [[202609202000 - MCP Proxy Aggregator Pattern]] — aggregated tool servers may feed into multi-agent pipelines
- [[AGENTS]] — orchestration context management uses the same compaction and note-taking strategies
- [[202609202020 - Orchestrator-Worker Delegation Pattern]] — composite tools that wrap multi-system workflows for agent workers

## Sources
- Beam AI, "6 Multi-Agent Orchestration Patterns for Production (2026)"
- Microsoft Azure Architecture Center, "AI agent design patterns"
- Augment Code, "Agentic Design Patterns: 2026 Pattern Catalog"
- Princeton NLP, multi-agent benchmarking study (2025)
