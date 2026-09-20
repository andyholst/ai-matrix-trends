---
id: 202609202005
created: 2026-09-20T20:05:00+02:00
tags:
  - architecture
  - acp
  - protocol
  - portability
links:
  - "[MCP Proxy Aggregator Pattern](./05%20-%20Architecture/202609202000%20-%20MCP%20Proxy%20Aggregator%20Pattern.md)"
  - "[Multi-Agent Orchestration with Guardrail Layering](./05%20-%20Architecture/202609202002%20-%20Multi-Agent%20Orchestration%20with%20Guardrail%20Layering.md)"
---

# Agent Portability via Agent Client Protocol (ACP)

## Core Idea
A protocol that decouples AI agents from specific editor or environment plugins, allowing the same agent to run inside any host that implements the ACP client interface — the agent becomes portable across editors, IDEs, and tools without per-platform integration work.

## How It Works
ACP inverts the traditional integration model. Instead of building a plugin for each editor (VS Code extension, JetBrains plugin, Zed integration), the agent implements the ACP server interface. The editor or host environment becomes the ACP client and drives the interaction.

```
Traditional model (N×M):
  Agent A → [VS Code ext, JetBrains plugin, Zed integration, ...]
  Agent B → [VS Code ext, JetBrains plugin, Zed integration, ...]

ACP model (N+M):
  Agent A → [ACP server] ←──→ [ACP client: VS Code, JetBrains, Zed, ...]
  Agent B → [ACP server] ←──→ [ACP client: VS Code, JetBrains, Zed, ...]
```

The protocol defines how the client discovers agent capabilities, sends user input, receives agent responses, and manages session state. The agent is environment-agnostic; the client handles UI rendering, file system access, and editor-specific features.

Key insight from Zed Industries: maintaining a VS Code extension for goose proved painful — the extension lagged behind agent evolution, causing breakage. ACP eliminates this by making the editor the client and the agent the server, so the editor always has the latest agent capabilities without re-packaging.

## When To Use
- Building an agent product that should work across multiple editors and IDEs
- Teams where developers use different editors but need consistent agent behavior
- Agent platforms that want to avoid per-platform plugin maintenance
- Scenarios where agent capabilities evolve faster than plugin release cycles can keep up

## Tradeoffs
**Pros:**
- One agent implementation works across all ACP-supporting hosts
- Eliminates per-platform plugin maintenance burden
- Agent capability updates ship once to the agent, not to N plugins
- Zed, JetBrains, and other editors have adopted ACP

**Cons:**
- Less editor-specific integration than a native plugin can provide
- ACP is less mature than MCP; acronym overlap causes confusion
- Not all editors support ACP yet — coverage is growing but incomplete
- The host environment must implement ACP client capabilities, which requires editor-side investment
- Limited awareness compared to MCP; fewer tutorials and community resources

## Examples
- [[202609200758 - OpenCode]] — goose running inside Zed editor via ACP instead of a VS Code extension
- [[202609200759 - Hermes Agent]] — JetBrains IDEs adopting ACP for AI assistant integration
- Agents that need to operate across design tools, browsers, and other platforms beyond editors
- Terminal agents that want to be accessible from any ACP-supporting host

## Anti-Patterns to Avoid
- **Assuming universal ACP support**: Building ACP-only when your users' editors don't implement it
- **Ignoring MCP compatibility**: ACP and MCP solve different problems (agent-to-host vs. agent-to-tool); agents may need both
- **Over-relying on host capabilities**: Expecting ACP clients to provide tool calling and MCP-like features

## Related Patterns
- [[202609202000 - MCP Proxy Aggregator Pattern]] — ACP handles the host-agent interface; MCP handles the agent-tool interface; they are complementary
- [[202609202002 - Multi-Agent Orchestration with Guardrail Layering]] — portable agents can participate in orchestration regardless of host environment

## Sources
- Agent Client Protocol (agentclientprotocol.com)
- DEV.to, "My Predictions for MCP and AI-Assisted Coding in 2026" — agent portability prediction
- Zed Industries — introducing ACP model
- JetBrains AI Assistant ACP adoption
