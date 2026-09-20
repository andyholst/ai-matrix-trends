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
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] — MCP server embeds its own LLM as a self-contained reusable agent
- [[202609200931 - Adaptive Planning Magentic Orchestration Pattern]] — Manager agent dynamically builds and pivots a task plan
- [[202609200932 - Fan-Out Fan-In Parallel Agent Pattern]] — Dispatcher fans out to N parallel agents, collector aggregates
- [[2026092030 - Bidirectional MCP Agent Pattern]] — Agent as both MCP client and server simultaneously
- [[2026092031 - Event-Driven Agent Concurrency Pattern]] — Pub/sub event bus for async agent coordination
- [[2026092032 - Tiered Routing Model Cascade Pattern]] — Multi-layer classifier routing to cheapest capable model
- [[2026092030 - Context Engineering]] — Curating minimal high-signal token sets for agent context
- [[2026092031 - Sub-Agent Delegation Pattern]] — Parent orchestrator delegating to isolated child agents
- [[2026092031 - Agent Teams Pattern]] — Parallel agents with shared task lists and peer messaging
- [[MCP Protocol]] — Standardized tool/resource interface
- [[202609202002 - Multi-Agent Orchestration with Guardrail Layering]] — Coordinator + specialist trees
- [[2026092030 - Context Engineering]] — Dynamic context curation
- [[Tool-Calling Patterns]] — Structured function invocation
- [[Guardrails & Safety]] — Approval modes, sandboxing

## Clusters

### Communication
- [[202609202000 - MCP Proxy Aggregator Pattern]]
- [[202609202004 - Layered Protocol Stack MCP A2A Streamable HTTP]]
- [[202609202005 - Agent Portability via Agent Client Protocol]]
- [[202609202022 - MCP Hybrid Client-Server Architecture]]
- [[202609202023 - MCP Gateway Aggregation Layer]]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]]
- [[MCP Protocol]]
- [[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]
- [[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]
- [[202609202020 - Orchestrator-Worker Delegation Pattern]]
- [[202609202024 - Orchestrator Worker Multi-Agent Delegation]]
- [[202609200931 - Adaptive Planning Magentic Orchestration Pattern]]
- [[202609200932 - Fan-Out Fan-In Parallel Agent Pattern]]
- [[2026092031 - Sub-Agent Delegation Pattern]]
- [[2026092031 - Agent Teams Pattern]]

### Context Management
- [[202609202001 - Context Engineering for Long-Horizon Agents]]
- [[202609202021 - Context Compaction and Structured Note-Taking]]
- [[202609202025 - Compaction and Note-Taking for Long-Horizon Context]]
- [[2026092030 - Context Engineering]]
- [[2026092030 - Context Engineering]]
- [[Tool-Calling Patterns]]

### UI & Interaction
- [[202609202003 - MCP Apps Interactive UI Protocol]]

### Safety
- [[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]
- [[Guardrails & Safety]]

### Cost Optimization
- [[2026092032 - Tiered Routing Model Cascade Pattern]]

### Event-Driven & Bidirectional
- [[2026092030 - Bidirectional MCP Agent Pattern]]
- [[2026092031 - Event-Driven Agent Concurrency Pattern]]

## Related MOCs
- [[MOC: Trending Agents]]
- [[MOC: Plugin Ecosystem]]
- [[00 - AI Architecture Master Index]] - [auto-summary]
- [[2026092030 - Context Engineering]] - [auto-summary]
- [[2026092031 - Sub-Agent Delegation Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[202609202035 - Dynamic Handoff Pattern]] - [auto-summary]
- [[202609202045 - Multi-Agent Debate Pattern]] - [auto-summary]
- [[202609202055 - Verifiable Execution Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200951 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[202609200930 - MCP Server-Side LLM Reusable Agent Pattern]] - [auto-summary]
- [[2026092031 - Agent Teams Pattern]] - [auto-summary]
- [[2026092032 - Agent Teams Pattern]] - [auto-summary]
