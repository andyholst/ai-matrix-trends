---
id: 202609202000
created: 2026-09-20T20:00:00+02:00
tags:
  - architecture
  - mcp
  - workflow
links:
  - [[AGENTS]]
  - [[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]
---

# MCP Proxy Aggregator Pattern

## Core Idea
A proxy server that connects to multiple upstream MCP servers and presents them as a single endpoint, using namespaced tool routing and optional per-request tool filtering to keep the visible tool catalog within LLM selection accuracy limits.

## How It Works
The proxy server maintains connections to N upstream MCP servers. On initialization, it fetches the tool list from each upstream, prefixes each tool name with a namespace (e.g., `github__create_pr`), and routes incoming tool calls by splitting the namespace prefix. Two variants exist:

- **Static-merge**: Surfaces the union of all upstream tools at once. Simple but degrades LLM selection accuracy once the merged catalog exceeds 10-15 tools (production data shows accuracy drops below 90% between 10-15 tools for Haiku, 20-30 for Sonnet).
- **Scoped**: Exposes only the subset of upstream tools relevant to the current task, using per-request retrieval-over-tools. This is the recommended variant when aggregation would push context past the tool-count limit.

```
Client → Proxy Aggregator → [MCP Server A, MCP Server B, MCP Server C]
         (namespaced routing)
         github__create_pr → Server A
         slack__post_message → Server B
```

The scoped variant adds a retrieval step: given the current task context, it selects the most relevant subset of tools from the full catalog before exposing them to the LLM. This retrieval must be fast and accurate to avoid adding latency.

## When to Use
- An agent needs capabilities from many distinct MCP servers but the client has connection limits
- An operator needs centralized authentication and audit logging across a fleet
- The combined tool catalog would exceed the LLM's reliable selection threshold (~10-15 tools)
- Building an enterprise MCP gateway or developer platform backend

## Tradeoffs
- **Pros:**
  - Simplifies client configuration (one endpoint instead of many)
  - Enables centralized auth, rate limiting, and audit logging
  - Scoped variant prevents tool-count degradation in LLM selection
  - Supports tool discovery across a large server fleet
- **Cons:**
  - Single point of failure — if the proxy goes down, all upstream servers are unreachable
  - Adds one network hop to every call (~30ms p50 same-region, modeled)
  - Namespace collisions require careful governance
  - Upstream server failures surface through the aggregate, complicating debugging
  - Scoped variant adds a per-request retrieval step that must itself be fast and accurate

## Examples
- Enterprise MCP gateways that aggregate internal tool servers
- Developer platforms exposing curated tool sets to AI assistants
- Multi-domain AI assistant backends (e.g., combining GitHub, Slack, Jira, and CRM tools)
- The ANSYR voice AI platform uses a Proxy Aggregator (Server-E) for multi-tenant tool routing

## Anti-Patterns to Avoid
- **Static merge with >15 tools**: Causes LLM selection accuracy to drop below 90%
- **God Tool**: A single `do_anything(action, params)` tool that collapses selection accuracy
- **Unsanitized resource content**: Returning user-generated data without stripping injected content

## Related Patterns
- [[202609202000 - MCP Proxy Aggregator Pattern]] — the upstream servers being aggregated often follow this pattern
- [[202609202020 - Orchestrator-Worker Delegation Pattern]] — composite tools that wrap multi-system workflows
- [[AGENTS]] — the scoped variant's retrieval step is itself a context engineering challenge

## Sources
- Rodrigues & Vas, "MCP Server Architecture Patterns for LLM-Integrated Applications" (arXiv:2606.30317, 2026)
- Model Context Protocol specification (modelcontextprotocol.io/specification/2025-11-25)
- Gan & Sun, "RAG-MCP: Mitigating prompt bloat in LLM tool selection via retrieval-augmented generation" (arXiv:2505.03275, 2025)
