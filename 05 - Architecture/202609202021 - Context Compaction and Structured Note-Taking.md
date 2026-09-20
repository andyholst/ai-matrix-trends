---
id: 202609202021
created: 2026-09-20T20:21:00+02:00
tags:
  - architecture
aliases:
  - Context Compaction Pattern
  - Agentic Memory Pattern
links:
links:
  - "[[202609202001 - Context Engineering for Long-Horizon Agents]]"
  - "[[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]"
---

# Context Compaction and Structured Note-Taking

## Core Idea
Long-horizon agents manage finite context windows by (1) compacting conversation history into summaries and (2) writing structured notes to persistent memory outside the context window for later retrieval.

## How It Works
Two complementary techniques address context overflow:

**Compaction:** When a conversation nears the context window limit, the message history is passed to the model to summarize and compress critical details — architectural decisions, unresolved bugs, implementation state — while discarding redundant tool outputs. The agent continues with the compressed context plus the N most recently accessed items. Pruning to the last 5 tool call/response pairs plus summarization achieved 91.6% task completion vs 71% for full-history in enterprise benchmarks.

**Structured note-taking (agentic memory):** The agent regularly writes notes to persistent storage (a file, NOTES.md, or a memory tool). These notes are pulled back into context at later turns. This provides durable memory across context resets with minimal overhead. Examples include to-do lists, progress tallies, and strategic notes.

**Sub-agent isolation:** Rather than one agent maintaining state across an entire project, specialized sub-agents handle focused tasks with clean context windows. Each returns only a condensed summary (1,000–2,000 tokens) to the main agent.

## When to Use
- Tasks spanning tens of minutes to multiple hours (large codebase migrations, research projects).
- Workflows with iterative development and clear milestones.
- Scenarios where context window limits cause reliability degradation or "context rot."
- Agents that need to maintain coherence across summarization boundaries.

## Tradeoffs
- **Pros:**
  - Prevents context overflow and stale-state errors.
  - Reduces token consumption and inference cost (535K vs 1.48M tokens in benchmarks).
  - Enables hours-long autonomous operation with coherent state.
- **Cons:**
  - Compaction can lose subtle but critical context whose importance emerges later.
  - Note-taking requires disciplined structure to avoid noise.
  - Multi-agent coordination adds orchestration overhead and prompt complexity.

## Examples
- [[MOC-Trending-Agents]] — Broader context engineering strategies including compaction and sub-agent architectures.
- [[202609202002 - Multi-Agent Orchestration with Guardrail Layering]] — Sub-agent isolation as a guardrail mechanism.

## Related Patterns
- [[202609202000 - MCP Proxy Aggregator Pattern]] — Proxy aggregators can enforce context budgets on tool responses.

## Sources
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://arxiv.org/abs/2606.10209
- https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase
