---
id: 202609200104
created: 2026-09-20T10:04:00+02:00
tags:
  - trend
  - emerging
  - protocol
  - a2a
  - acp
aliases:
  - Agent-to-Agent Communication
links:
  - "[Layered Protocol Stack MCP A2A Streamable HTTP](./05%20-%20Architecture/202609202004%20-%20Layered%20Protocol%20Stack%20MCP%20A2A%20Streamable%20HTTP.md)"
  - "[Agent Portability via Agent Client Protocol](./05%20-%20Architecture/202609202005%20-%20Agent%20Portability%20via%20Agent%20Client%20Protocol.md)"
---

# Agent-to-Agent Communication Protocols

## Core Idea
New protocols (A2A, ACP) are emerging to enable agents to communicate with each other, not just with tools — enabling multi-agent orchestration.

## Details
- **A2A (Agent-to-Agent)**: Google's protocol for cross-agent communication
- **ACP (Agent Client Protocol)**: Standardizes agent-to-host integration
- **Current state**: Early adoption, few production deployments
- **Watch for**: Interop between frameworks, vendor neutrality

## Evidence
- Google announced A2A protocol in early 2026
- JetBrains adopting ACP for IDE integration
- Anthropic's MCP adding multi-agent features

## Related Patterns
- [[202609202004 - Layered Protocol Stack MCP A2A Streamable HTTP]] — Three-layer stack
- [[202609202005 - Agent Portability via Agent Client Protocol]] — Agent-to-host standard
- [[202609202020 - Orchestrator-Worker Delegation Pattern]] — Multi-agent orchestration

## Sources
- [Google A2A Protocol](https://github.com/google/A2A)
- [Agent Client Protocol](https://agentclientprotocol.com/)
