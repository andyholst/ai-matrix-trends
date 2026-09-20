---
id: 2026092030
created: 2026-09-20T30:00:00+02:00
tags:
  - architecture
  - context-engineering
links:
  - "[[202609202001 - Context Engineering for Long-Horizon Agents]]"
  - "[[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]"
---

# Context Engineering

## Core Idea
Context engineering is the discipline of curating the smallest possible set of high-signal tokens that maximize the likelihood of a desired agent outcome, treating context as a finite resource with diminishing marginal returns.

## How It Works
Context engineering replaces prompt engineering as the primary lever for agent quality. The agent loop generates data each turn, and context must be cyclically refined. Key strategies include:

- **Just-in-time retrieval** — maintain lightweight identifiers (file paths, stored queries, links) and load data into context at runtime via tools rather than pre-loading everything up front.
- **Compaction** — summarize or drop older message history to maintain conversational flow for long-horizon tasks.
- **Note-taking / external memory** — the agent writes to a NOTES.md or file system to track progress across complex tasks, preserving critical context that would otherwise be lost across dozens of tool calls.
- **Sub-agent isolation** — specialized sub-agents handle focused tasks with clean context windows, returning only condensed summaries (1,000–2,000 tokens) to the parent.
- **KV-cache optimization** — keep prompt prefixes stable, make context append-only, and avoid dynamic tool changes mid-iteration to maximize cache hit rates.
- **Tool masking** — use a state machine to mask token logits during decoding, preventing the model from selecting invalid actions without removing tool definitions from context.
- **File system as context** — treat the file system as unlimited, persistent, externalized memory that the agent reads and writes on demand.

## When to Use
- Long-horizon agent tasks where context window fills up
- Agents with large tool sets (MCP servers) that cause action-selection degradation
- Multi-step workflows where intermediate observations are large (web pages, PDFs)
- Production systems where KV-cache hit rate directly impacts latency and cost

## Tradeoffs
- **Pros:** Dramatically reduces context rot; improves attention focus; enables longer tasks; reduces token costs via caching; keeps the main agent's context lean
- **Cons:** Requires careful engineering of compaction and retrieval logic; irreversible compression risks information loss; adds complexity to the agent loop; tool masking requires constrained decoding support

## Examples
- [[202609202000 - Claude Code]] — uses compaction, memory tool, and sub-agent isolation
- [[Manus]] — file system as context, KV-cache optimization, tool masking via state machine

## Related Patterns
- [[2026092031 - Sub-Agent Delegation Pattern]], [[2026092032 - Agent Teams Pattern]], [[MCP Protocol]]

## Sources
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
