---
tags:
  - moc
---

# MOC: Architecture Patterns

## Overview
A map of the core architectural patterns powering modern AI coding agents.

## Key Notes
- [[202609202000 - MCP Proxy Aggregator Pattern]] — Namespaced routing across upstream MCP servers
- [[202609202001 - Context Engineering for Long-Horizon Agents]] — Compaction, structured notes, just-in-time retrieval
- [[202609202002 - Multi-Agent Orchestration with Guardrail Layering]] — Fan-out/fan-in with validation layers
- [[202609202003 - MCP Apps Interactive UI Protocol]] — Agents render interactive UI components in host
- [[202609202004 - Layered Protocol Stack MCP A2A Streamable HTTP]] — MCP + A2A + HTTP three-layer stack
- [[202609202005 - Agent Portability via Agent Client Protocol]] — Decoupling agents from editor plugins
- [[202609202020 - Orchestrator-Worker Delegation Pattern]] — Task decomposition with heterogeneous model tiers
- [[202609202021 - Context Compaction and Structured Note-Taking]] — Compaction + agentic memory for long-horizon tasks
- [[202609202022 - MCP Hybrid Client-Server Architecture]] — LLMs on both MCP server and client for flexibility
- [[202609202023 - MCP Gateway Aggregation Layer]] — Gateway federating multiple MCP servers behind one client endpoint
- [[202609202024 - Orchestrator Worker Multi-Agent Delegation]] — Lead agent dispatching stateless workers with clean context windows
- [[202609202025 - Compaction and Note-Taking for Long-Horizon Context]] — Compaction + external notes for coherence beyond context limits
- [[MCP Protocol]] — Standardized tool/resource interface
- [[Multi-Agent Orchestration]] — Coordinator + specialist trees
- [[Context Engineering]] — Dynamic context curation
- [[Tool-Calling Patterns]] — Structured function invocation
- [[Guardrails & Safety]] — Approval modes, sandboxing

## Clusters

### Communication
- [[202609202000 - MCP Proxy Aggregator Pattern]]
- [[202609202004 - Layered Protocol Stack MCP A2A Streamable HTTP]]
- [[202609202005 - Agent Portability via Agent Client Protocol]]
- [[202609202022 - MCP Hybrid Client-Server Architecture]]
- [[202609202023 - MCP Gateway Aggregation Layer]]
- [[MCP Protocol]]
- [[Multi-Agent Orchestration]]
- [[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]
- [[202609202020 - Orchestrator-Worker Delegation Pattern]]
- [[202609202024 - Orchestrator Worker Multi-Agent Delegation]]

### Context Management
- [[202609202001 - Context Engineering for Long-Horizon Agents]]
- [[202609202021 - Context Compaction and Structured Note-Taking]]
- [[202609202025 - Compaction and Note-Taking for Long-Horizon Context]]
- [[Context Engineering]]
- [[Tool-Calling Patterns]]

### UI & Interaction
- [[202609202003 - MCP Apps Interactive UI Protocol]]

### Safety
- [[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]
- [[Guardrails & Safety]]

## Related MOCs
- [[MOC: Trending Agents]]
- [[MOC: Plugin Ecosystem]]
