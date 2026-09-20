---
id: 2026092032
created: 2026-09-20T32:00:00+02:00
tags:
  - architecture
  - cost-optimization
  - model-routing
links:
  - "[Bidirectional MCP Agent Pattern](./05%20-%20Architecture/2026092030%20-%20Bidirectional%20MCP%20Agent%20Pattern.md)"
  - "[Event-Driven Agent Concurrency Pattern](./05%20-%20Architecture/2026092031%20-%20Event-Driven%20Agent%20Concurrency%20Pattern.md)"
  - "[MCP Gateway Aggregation Layer](./05%20-%20Architecture/202609202023%20-%20MCP%20Gateway%20Aggregation%20Layer.md)"
---

# Tiered Routing / Model Cascade Pattern

## Core Idea
A multi-layer classifier that routes each request to the cheapest capable model tier — cheap deterministic checks (regex, keyword matching) run first, then a small cheap model classifies ambiguous cases, and only what survives both reaches the full expensive reasoning model. Reduces inference costs by 60-85% while maintaining 90-95% of frontier model quality.

## How It Works
```
Request ──►┌──────────────────┐
           │  Layer 1: Regex  │  ◄── Zero tokens, catches navigational intent
           │  / Rule-Based    │      ("where's my order", "cancel appointment")
           └────────┬─────────┘
                    │ (if ambiguous)
                    ▼
           ┌──────────────────┐
           │  Layer 2: Cheap  │  ◄── ~10 tokens, temperature 0.1
           │  Model Classifier│      (Gemini Flash / Haiku)
           │  (intent only)   │
           └────────┬─────────┘
                    │ (if still ambiguous)
                    ▼
           ┌──────────────────┐
           │  Layer 3: Full   │  ◄── Frontier model (Opus / GPT-4)
           │  Reasoning Model │      (only ~10-40% of requests)
           └──────────────────┘
```

1. **Layer 1 — Deterministic pre-filter**: Local regex or keyword matching catches navigational/structured intent at zero token cost. Handles 40%+ of incoming messages before any model call.
2. **Layer 2 — Cheap classifier**: A small, fast model (10 tokens, temperature 0.1) classifies ambiguous cases — is this a simple extraction or does it need deep reasoning?
3. **Layer 3 — Frontier model**: Only requests that survive both filters reach the expensive reasoning model.
4. **Fallback with shared validation**: When the primary model is overloaded, a fallback model stands in — but both paths run through the same validation function before a response is accepted.

## When to Use
- High-volume agent systems where inference cost is the dominant constraint
- Traffic with a skewed distribution (many simple requests, few complex ones)
- Multi-agent systems where each agent step can be routed independently
- Production systems where a 5-25x cost ratio exists between model tiers

## Tradeoffs
- **Pros:**
  - 60-85% cost reduction while maintaining 90-95% of frontier quality
  - Each layer is independently measurable and tunable
  - Composes with caching, prompt optimization, and budget controls
  - Fallback path ensures availability during overload
- **Cons:**
  - Adds latency for multi-layer classification (mitigated by Layer 1 being instant)
  - Requires traffic analysis to tune thresholds
  - Risk of under-routing (sending complex requests to cheap models)
  - Fallback validation must be shared to avoid quality degradation

## Examples
- Customer support agent: 70% of requests routed to Flash ($0.30/M tokens), 20% to Sonnet ($3/M), 10% to Opus ($15/M) — reducing average cost from $15 to ~$2.10 per million tokens (86% reduction)
- Google AI Agents Challenge: a three-layer classifier where Layer 1 (regex) handled 40%+ of messages before any model call
- RouteLLM research: routing 85% of queries to cheaper models while maintaining 95% of GPT-4 quality on MT-Bench

## Anti-Patterns to Avoid
- **Skipping validation on fallback**: If the fallback path doesn't run the same validation as the primary path, you're shipping two different products
- **Routing across cost tiers without availability checks**: A query that needs the top tier has paid for three model calls if each tier is unavailable
- **Ignoring tail latency**: Cheaper models with 2x latency can hurt UX — test p95 and p99

## Related Patterns
- [2026092030 - Bidirectional MCP Agent Pattern](./05%20-%20Architecture/2026092030%20-%20Bidirectional%20MCP%20Agent%20Pattern.md) — tiered routing can sit in front of a bidirectional MCP server to reduce per-call costs
- [2026092031 - Event-Driven Agent Concurrency Pattern](./05%20-%20Architecture/2026092031%20-%20Event-Driven%20Agent%20Concurrency%20Pattern.md) — event-driven agents can each apply tiered routing independently
- [202609202023 - MCP Gateway Aggregation Layer](./05%20-%20Architecture/202609202023%20-%20MCP%20Gateway%20Aggregation%20Layer.md) — gateway can enforce tiered routing across all backend agents

## Sources
- Google Developers Blog: "4 engineering patterns behind the strongest AI Agents Challenge submissions" (Sept 2026) — https://developers.googleblog.com/4-engineering-patterns-behind-the-strongest-ai-agents-challenge-submissions/
- RouteLLM research (arXiv:2406.18665) — up to 3.66x cost savings while retaining 95% of GPT-4 quality
- Splunk: "How to Reduce Agent Cost by Model Routing" — https://www.splunk.com/en_us/blog/artificial-intelligence/reduce-agent-cost-by-model-routing.html
