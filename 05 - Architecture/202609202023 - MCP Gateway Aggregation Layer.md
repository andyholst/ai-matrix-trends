---
id: 202609202023
created: 2026-09-20T20:23:00+02:00
tags:
  - architecture
  - MCP
  - gateway
  - protocol
aliases:
links:
  - "[[202609202000 - MCP Proxy Aggregator Pattern]]"
  - "[[202609202004 - Layered Protocol Stack MCP A2A Streamable HTTP]]"
  - "[[202609202022 - MCP Hybrid Client-Server Architecture]]"
---

# MCP Gateway Aggregation Layer

## Core Idea
A single gateway process that federates multiple MCP servers behind one client-facing protocol endpoint, handling routing, auth, and capability discovery.

## How It Works
The gateway sits between an MCP client (typically an LLM harness or IDE) and a fleet of backend MCP servers (each exposing tools, resources, or prompts). It performs capability discovery at startup by querying each upstream server's `tools/list` and `resources/list`, merges them into a unified catalog, and applies namespacing (e.g., `server-name/tool-name`) to avoid collisions. Incoming `tools/call` requests are routed to the correct upstream based on the namespace prefix. The gateway also terminates OAuth, injects credentials per-upstream, and can rate-limit or audit-log traffic before forwarding.

```
Client ──► Gateway ──┬── MCP Server A (tools)
                     ├── MCP Server B (resources)
                     └── MCP Server C (prompts)
```

## When to Use
- You need to expose 3+ MCP servers through a single connection point
- Different upstreams require different credentials or OAuth scopes
- You need centralized audit logging for tool invocations
- Capability discovery must be filtered (e.g., hiding internal tools from external clients)

## Tradeoffs
- **Pros:** Single connection for clients, unified auth, centralized observability, ability to hide/restrict upstream capabilities
- **Cons:** Added latency hop, single point of failure, requires namespace management to prevent tool-name collisions, gateway must be kept in sync with upstream capability changes

## Examples
- An IDE that aggregates filesystem, database, and CI/CD MCP servers behind one gateway
- A multi-tenant SaaS that exposes per-customer tool subsets through the same gateway infrastructure

## Related Patterns
- [[202609202000 - MCP Proxy Aggregator Pattern]]
- [[202609202004 - Layered Protocol Stack MCP A2A Streamable HTTP]]
- [[202609202022 - MCP Hybrid Client-Server Architecture]]

## Sources
- IBM Developer: "Model Context Protocol architecture patterns for multi-agent AI systems" (https://developer.ibm.com/articles/mcp-architecture-patterns-ai-systems/)
- WorkOS: "Everything your team needs to know about MCP in 2026" (https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026)
- MCP Specification (https://modelcontextprotocol.io/specification/2026-07-28)
