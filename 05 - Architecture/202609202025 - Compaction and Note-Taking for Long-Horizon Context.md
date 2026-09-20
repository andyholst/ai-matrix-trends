---
id: 202609202025
created: 2026-09-20T20:25:00+02:00
tags:
  - architecture
  - context-engineering
  - compaction
  - memory
  - long-horizon
aliases:
links:
  - "[[202609202021 - Context Compaction and Structured Note-Taking]]"
  - "[[MOC-Trending-Agents]]"
  - "[[202609202024 - Orchestrator Worker Multi-Agent Delegation]]"
  - "[[202609202000 - Claude Code]]"
---

# Compaction and Note-Taking for Long-Horizon Context

## Core Idea
Two complementary context-management strategies — compaction (summarizing conversation history in-place) and structured note-taking (persisting state to external files) — that keep long-horizon agents coherent beyond the context window limit.

## How It Works
**Compaction** triggers when the conversation approaches the context window limit. The message history is passed to the model with a summarization prompt that preserves architectural decisions, unresolved bugs, and key implementation details while discarding redundant tool outputs. The compressed summary plus the N most recently accessed files become the new context. Claude Code uses this approach, keeping the five most recent files alongside the summary.

**Structured note-taking** (agentic memory) writes persistent notes to files outside the context window — a to-do list, a NOTES.md, or a progress tracker. These files are read back into context at the start of each new session or when the agent needs to reorient. This pattern enables coherence across context resets: the agent reads its own notes and continues multi-hour work without losing track of objectives, dependencies, or completed steps.

```
Session 1: [long conversation] ──► compaction ──► [summary + 5 files]
                                                       │
Session 2: agent reads notes.md ──► reorients ──► continues work
```

## When to Use
- Tasks that span hours or multiple sessions (large codebase migrations, research projects)
- Agents that need to track progress across many tool calls
- Workflows where context resets are inevitable (session limits, token budgets)
- Any long-horizon agent that must maintain goal-directed behavior over time

## Tradeoffs
- **Pros:** Enables arbitrarily long tasks, reduces token cost vs. full history, notes are human-readable and editable, works with any model
- **Cons:** Compaction can lose subtle but critical context (over-aggressive summarization), notes require a filesystem or virtual filesystem, adds I/O overhead, compaction prompt tuning is model-specific

## Examples
- Claude Code's compaction + five-file context continuation
- Claude playing Pokémon: maintains tallies, maps, and combat strategies across thousands of steps via notes
- Enterprise expense agents: pruning to last 5 tool calls + summarization achieved 91.6% completion vs. 71% for full history (arXiv:2606.10209)

## Related Patterns
- [[202609202021 - Context Compaction and Structured Note-Taking]]
- [[MOC-Trending-Agents]]
- [[202609202024 - Orchestrator Worker Multi-Agent Delegation]]

## Sources
- Anthropic Engineering: "Effective context engineering for AI agents" (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- arXiv:2606.10209 — "Less Context, Better Agents: Efficient Context Engineering for Long-Horizon Tool-Using LLM Agents"
- Sequoia Capital: "Context Engineering Our Way to Long-Horizon Agents" — Harrison Chase interview (https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase)
