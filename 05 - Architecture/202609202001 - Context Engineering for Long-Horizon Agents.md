---
id: 202609202001
created: 2026-09-20T20:00:00+02:00
tags:
  - architecture
  - workflow
  - config
links:
  - [[mcp-proxy-aggregator-pattern]]
  - [[multi-agent-orchestration-patterns]]
---

# Context Engineering for Long-Horizon Agents

## Core Idea
The discipline of curating the smallest possible set of high-signal tokens that maximize the likelihood of a desired outcome, treating context as a finite attention budget rather than an unbounded resource.

## How It Works
Context engineering encompasses three primary strategies for managing the LLM context window over long tasks:

### 1. Compaction
When a conversation approaches the context window limit, summarize its contents and reinitiate a new context window with the summary. The art lies in selecting what to keep vs. discard. Recommended approach:
- Start by maximizing recall in the compaction prompt (capture everything relevant)
- Then iterate to improve precision (eliminate superfluous content)
- One of the safest lightweight forms is tool result clearing — once a tool result is deep in history, the agent rarely needs to see the raw output again

Claude Code implements this by passing message history to the model to summarize, preserving architectural decisions and unresolved bugs while discarding redundant tool outputs. The agent continues with compressed context plus the five most recently accessed files.

### 2. Structured Note-Taking (Agentic Memory)
The agent regularly writes notes persisted to memory outside the context window, then pulls them back in when needed. Examples:
- A to-do list tracking progress across complex tasks
- A NOTES.md file maintaining critical dependencies
- File-based memory systems (Claude Code's memory tool, launched in public beta with Sonnet 4.5)

After context resets, the agent reads its own notes and continues multi-hour work sequences. This enables long-horizon strategies impossible when keeping everything in context.

### 3. Sub-Agent Architectures
Specialized sub-agents handle focused tasks with clean context windows. The main agent coordinates with a high-level plan while sub-agents perform deep technical work. Each sub-agent might explore extensively (tens of thousands of tokens) but returns only a condensed summary (1,000-2,000 tokens).

```
Lead Agent (high-level plan)
  ├── Sub-agent A: Deep code exploration → summary
  ├── Sub-agent B: Database query analysis → summary
  └── Sub-agent C: API integration testing → summary
```

This achieves separation of concerns: detailed search context stays isolated within sub-agents while the lead agent synthesizes results.

### Just-in-Time Context Retrieval
Rather than pre-processing all data up front, agents maintain lightweight identifiers (file paths, queries, links) and use tools to dynamically load data at runtime. Claude Code uses this approach: CLAUDE.md files are dropped into context up front, while glob and grep allow just-in-time navigation. This mirrors human cognition — we use file systems and bookmarks rather than memorizing entire corpuses.

## When to Use
- **Compaction**: Tasks requiring extensive back-and-forth where conversational flow matters
- **Note-taking**: Iterative development with clear milestones and persistent state needs
- **Sub-agent architectures**: Complex research and analysis where parallel exploration pays dividends
- **Just-in-time retrieval**: Large datasets where loading everything would exceed context; the agent can write targeted queries and use head/tail to analyze incrementally

## Tradeoffs
- **Pros:**
  - Enables tasks spanning hours or days that exceed any context window
  - Context rot mitigation — smaller contexts maintain higher attention precision
  - Sub-agent isolation prevents detailed exploration from polluting the lead agent's context
  - Progressive disclosure: agents incrementally discover relevant context through exploration
- **Cons:**
  - Runtime exploration is slower than pre-computed retrieval
  - Overly aggressive compaction can lose subtle but critical context
  - Sub-agent summaries are lossy by design
  - Just-in-time retrieval requires careful tool design and heuristics to avoid wasted exploration
  - Without proper guidance, agents can misuse tools, chase dead-ends, or fail to identify key information

## Context Rot and Attention Budget
Research on needle-in-a-haystack benchmarking has uncovered "context rot": as token count increases, the model's ability to accurately recall information decreases. This stems from the transformer architecture's n² pairwise relationships for n tokens — attention gets stretched thin. The implication is a performance gradient rather than a hard cliff, but every new token depletes the attention budget.

## Examples
- Claude Code: compaction + note-taking (CLAUDE.md) + just-in-time retrieval (glob/grep)
- Claude Plays Pokémon: maintains precise tallies across thousands of game steps, develops maps of explored regions, remembers combat strategies
- Anthropic's multi-agent research system: sub-agents explore extensively but return only condensed summaries to the lead agent

## Related Patterns
- [[mcp-proxy-aggregator-pattern]] — the scoped variant's retrieval step is itself a context engineering challenge
- [[multi-agent-orchestration-patterns]] — sub-agent architectures are a form of multi-agent orchestration
- [[tool-orchestrator-mcp-pattern]] — composite tools reduce context burden by returning single summaries

## Sources
- Anthropic, "Effective context engineering for AI agents" (September 2025)
- Anthropic, "How we built our multi-agent research system"
- Chroma Research, "Context Rot: How Increasing Token Counts Degrades LLM Performance"
