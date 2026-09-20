---
id: 202609202004
created: 2026-09-20T20:04:00+02:00
tags:
  - architecture
  - mcp
  - a2a
  - protocol
  - transport
links:
  - "[[202609202000 - MCP Proxy Aggregator Pattern]]"
  - "[[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]"
---

# Layered Protocol Stack: MCP + A2A + Streamable HTTP

## Core Idea
An emerging three-layer protocol architecture for agentic AI: MCP (Model Context Protocol) for agent-to-tool communication, A2A (Agent-to-Agent) for agent-to-agent coordination, and Streamable HTTP as the transport backbone. Together they form a complete stack for building interoperable agent systems.

## How It Works
The stack separates concerns that monolithic agent frameworks conflate:

```
┌─────────────────────────────────────┐
│  Layer 3: Commerce / Transactions   │  ACP, UCP (emerging)
├─────────────────────────────────────┤
│  Layer 2: Agent Coordination (A2A) │  Agent-to-Agent protocol
├─────────────────────────────────────┤
│  Layer 1: Tool Access (MCP)         │  Agent-to-tool protocol
├─────────────────────────────────────┤
│  Transport: Streamable HTTP         │  JSON-RPC 2.0 over HTTP
└─────────────────────────────────────┘
```

**Layer 1 — MCP (Model Context Protocol):** Standardizes how agents connect to external tools, data sources, and services. Collapses the N×M integration problem to N+M. As of April 2026: 97 million monthly SDK downloads, 10,000+ public MCP servers, governed by the Agentic AI Foundation under the Linux Foundation. The Python SDK alone crossed 164 million monthly downloads.

**Layer 2 — A2A (Agent-to-Agent):** Google-initiated protocol for agent-to-agent communication. Formally released as A2A v1.0 in April 2026 after the MCP Dev Summit. Enables heterogeneous agents from different vendors to discover each other, negotiate capabilities, and delegate tasks without shared framework dependencies. Agents expose agent cards (capability descriptors); clients discover and route to appropriate agents.

**Transport — Streamable HTTP:** The current standard transport for remote MCP and A2A connections. Replaces the older SSE transport. Uses JSON-RPC 2.0, supports OAuth 2.1 with PKCE and Dynamic Client Registration for authentication. Enables both request-response and streaming interaction patterns.

## When To Use
- Building multi-vendor agent ecosystems where agents from different providers must collaborate
- Enterprise platforms that need both tool access (MCP) and agent coordination (A2A)
- Any new agent architecture that should be protocol-aligned rather than framework-locked
- Scenarios requiring transport-level interoperability across cloud and on-premises deployments

## Tradeoffs
**Pros:**
- Protocol-level interoperability across vendors (OpenAI, Anthropic, Google, AWS all participate)
- Clean separation of concerns: tools vs. coordination vs. transport
- Governance under Linux Foundation ensures vendor neutrality
- A2A v1.0 reached production standard in April 2026
- Streamable HTTP replaces fragmented transport approaches

**Cons:**
- A2A is still maturing — ecosystem tooling lags MCP by 12-18 months
- Multi-layer stack adds conceptual complexity; many teams only need MCP
- Protocol versions may not align (MCP and A2A release cycles are independent)
- Security model across layers is still being defined (how do A2A authentication and MCP OAuth interact?)

## Examples
- [[2026092012 - OpenCode]] — Enterprise multi-agent platforms using MCP for tool access and A2A for cross-team agent delegation
- [[202609200759 - Hermes Agent]] — AWS Kiro and Amazon Q Developer CLI sharing MCP config format
- Docker MCP Toolkit running MCP servers in isolated containers with OAuth
- Accenture's Trusted Agent Huddle for multi-system agent collaboration across enterprises

## Anti-Patterns to Avoid
- **Framework lock-in**: Building on a specific agent framework's SDK instead of protocol-level abstractions
- **Skipping transport governance**: Not implementing OAuth 2.1 and Dynamic Client Registration for remote servers
- **Premature A2A adoption**: Using A2A for simple orchestration that MCP alone handles

## Related Patterns
- [[202609202000 - MCP Proxy Aggregator Pattern]] — aggregators may expose both MCP and A2A interfaces
- [[202609202002 - Multi-Agent Orchestration with Guardrail Layering]] — A2A provides the inter-agent communication layer that orchestration patterns rely on

## Sources
- Truthifi, "The state of MCP 2026: how AI agents connect to your data" (February 2026)
- Model Context Protocol specification (modelcontextprotocol.io)
- Agentic AI Foundation (Linux Foundation) — 150 member organizations as of April 2026
- A2A v1.0 release (April 2026)
- MCP Dev Summit North America (April 2026, 1,200 attendees, 95 sessions)
