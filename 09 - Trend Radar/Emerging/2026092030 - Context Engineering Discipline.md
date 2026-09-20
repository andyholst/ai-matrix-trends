---
id: 2026092030
created: 2026-09-20T30:00:00+02:00
tags:
  - trend
  - architecture
  - context-engineering
links:
  - "[Context Engineering](./05%20-%20Architecture/2026092030%20-%20Context%20Engineering.md)"
  - "[Context Engineering for Long-Horizon Agents](./05%20-%20Architecture/202609202001%20-%20Context%20Engineering%20for%20Long-Horizon%20Agents.md)"
---

# Context Engineering Discipline

## Core Idea
Context engineering has emerged as a distinct discipline — curating the smallest possible set of high-signal tokens that maximize the likelihood of a desired agent outcome — replacing prompt engineering as the primary lever for agent quality.

## Details
The discipline encompasses just-in-time retrieval (load data at runtime via tools), compaction (summarize older history), note-taking (external memory via files), sub-agent isolation (clean context windows for focused tasks), KV-cache optimization (stable prefixes, append-only context), tool masking (state machines to prevent invalid actions), and file system as context (unlimited persistent memory).

Anthropic, Manus, and other leading agent builders have published detailed guidance on context engineering. The field is moving from ad-hoc prompt tuning to systematic context curation with measurable outcomes.

## Implications
As agent tasks grow longer and more complex, context engineering becomes the critical skill for agent developers. The discipline's principles — compaction, retrieval, isolation — are becoming standard practice. Agents that master context engineering will outperform those with larger context windows but poorer curation.

## Related
- [2026092030 - Context Engineering](./05%20-%20Architecture/2026092030%20-%20Context%20Engineering.md)
- [202609202001 - Context Engineering for Long-Horizon Agents](./05%20-%20Architecture/202609202001%20-%20Context%20Engineering%20for%20Long-Horizon%20Agents.md)
- [2026092031 - Sub-Agent Delegation Pattern](./05%20-%20Architecture/2026092031%20-%20Sub-Agent%20Delegation%20Pattern.md)

## Sources
- [Anthropic — Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Manus — Context Engineering Lessons](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
