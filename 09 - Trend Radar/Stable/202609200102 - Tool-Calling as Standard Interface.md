---
id: 202609200102
created: 2026-09-20T10:02:00+02:00
tags:
  - trend
  - stable
  - architecture
  - tool-calling
aliases:
  - Tool-Calling as Standard
links:
  - "[[202609202000 - Claude Code]]"
  - "[[202609202000 - Cursor]]"
---

# Tool-Calling as Standard Interface

## Core Idea
All modern AI coding agents now use structured tool-calling as their primary interaction model, making it a settled pattern rather than a differentiator.

## Details
- **Universal adoption**: Claude Code, Codex, OpenCode, Cursor, Cline all use tool-calling
- **Structured inputs**: JSON Schema validation on tool inputs
- **Streaming**: Tool calls stream in real-time for responsive UX
- **Multi-tool**: Agents can invoke multiple tools in parallel

## Why It's Stable
This pattern has crossed the chasm from "innovation" to "requirement." No serious agent launches without tool-calling support.

## Related Patterns
- [[202609202000 - MCP Proxy Aggregator Pattern]] — Namespaced tool routing
- [[MOC-Trending-Agents]] — Tools for context curation

## Sources
- [Anthropic Tool Use Docs](https://docs.anthropic.com/en/docs/tool-use)
