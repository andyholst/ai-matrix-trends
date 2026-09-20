---
id: 202609202022
created: 2026-09-20T20:22:00+02:00
tags:
  - architecture
aliases:
  - MCP Hybrid Architecture
  - Hybrid LLM Placement Pattern
links:
links:
  - "[Context Engineering for Long-Horizon Agents](./05%20-%20Architecture/202609202001%20-%20Context%20Engineering%20for%20Long-Horizon%20Agents.md)"
  - "[Multi-Agent Orchestration with Guardrail Layering](./05%20-%20Architecture/202609202002%20-%20Multi-Agent%20Orchestration%20with%20Guardrail%20Layering.md)"
---

# MCP Hybrid Client-Server Architecture

## Core Idea
A hybrid Model Context Protocol architecture places LLMs on both the MCP server (for reusable, centralized agent capabilities) and the MCP client (for dynamic, context-aware orchestration), balancing reusability with flexibility.

## How It Works
The hybrid model combines two placement strategies:

**Server-side LLMs (Reusable AI Agents):** Each MCP server hosts an LLM with tools, prompts, and resources. The server acts as a pluggable microservice — the client calls tools the server exposes. This provides centralized maintenance, model updates, and reuse across many systems.

**Client-side LLMs (Dynamic Orchestration):** The MCP client runs its own LLM for dynamic orchestration — deciding which server tools to call, in what order, and how to combine results. This enables context-aware, adaptive workflows.

**Hybrid flow:**
1. The client LLM receives a user request and plans which server tools to invoke.
2. MCP servers execute specialized tasks (sentiment analysis, data retrieval, generation) and return results.
3. The client LLM synthesizes results, potentially calling additional servers or refining the plan.
4. Server-Sent Events (SSE) provide real-time progress updates for long-running tasks.

## When to Use
- Systems needing both reusable, specialized agent capabilities and dynamic orchestration.
- Multi-agent ecosystems where new agents (translation, summarization) are added as MCP servers without disrupting workflows.
- Scenarios requiring real-time progress updates via SSE for long-running operations.
- Enterprise environments wanting centralized model management with client-side flexibility.

## Tradeoffs
- **Pros:**
  - Scalable through asynchronous processing and horizontal scaling.
  - Maintainable — clear separation of concerns, independent agent deployment.
  - Reusable — agents support many use cases as pluggable MCP servers.
  - Responsive — SSE provides real-time progress updates.
- **Cons:**
  - Network latency and privacy concerns when data must travel to servers.
  - Tighter coupling risk if agents are exposed as traditional SDKs instead of MCP tools.
  - Increased architectural complexity from managing both client and server LLMs.

## Examples
- [[202609202004 - Layered Protocol Stack MCP A2A Streamable HTTP]] — How MCP fits into a broader protocol stack including A2A and Streamable HTTP.
- [[202609202005 - Agent Portability via Agent Client Protocol]] — Agent Client Protocol as an alternative to MCP for client-side orchestration.

## Related Patterns
- [[202609202000 - MCP Proxy Aggregator Pattern]] — Proxy aggregators as an intermediary between clients and MCP servers.

## Sources
- https://developer.ibm.com/articles/mcp-architecture-patterns-ai-systems/
- https://arxiv.org/abs/2606.30317
- https://modelcontextprotocol.io/specification/2026-07-28
