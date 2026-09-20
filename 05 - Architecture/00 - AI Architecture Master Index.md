---
id: 00
tags:
  - moc
  - architecture
  - architecture
  - indexlinks:
  - "[202609202001 - Context Engineering for Long-Horizon Agents](./05%20-%20Architecture/202609202001%20-%20Context%20Engineering%20for%20Long-Horizon%20Agents.md)"
  - "[202609202002 - Multi-Agent Orchestration with Guardrail Layering](./05%20-%20Architecture/202609202002%20-%20Multi-Agent%20Orchestration%20with%20Guardrail%20Layering.md)"
created: 2026-09-20T18:50:01+02:00
---

# AI Architecture Patterns — Master Index

This is a comprehensive index of modern AI architecture patterns, including LLM systems, agent orchestration, context engineering, and emerging protocols.

---

## 🏗️ Core Agent Architectures

### Single-Agent Pattern
- **CLI Agents**: Claude Code, OpenCode, Aider, Codex, Cursor, Cline, Windsurf
- **Architecture**: Single LLM + tool loop + file system access
- **Strengths**: Simple, fast, direct control
- **Weaknesses**: Limited context, single point of failure

### Multi-Agent Pattern
- **Orchestrator-Worker**: Dispatcher + specialist agents (fan-out/fan-in)
- **Peer-to-Peer**: Agents communicate directly (A2A protocol)
- **Hierarchical**: Manager agents coordinating sub-agents

### Agent + MCP Server Pattern
- **MCP (Model Context Protocol)**: Universal tool/resource interface
- **Client**: Agent (Claude Code, Cursor, etc.)
- **Server**: External tool (Firecrawl, Browser Use, Context7)
- **Transport**: stdio, SSE, Streamable HTTP

---

## 🧠 LLM System Architectures

### Jev Context Engine System
- **Purpose**: Intelligent context curation for LLM sessions
- **Architecture**: Shadow mode → active mode (typesafe Jev provider)
- **Key Insight**: Select what to keep rather than summarizing
- **Performance**: Cuts ~75% of context usage while preserving every user/agent message verbatim
- **Plugin**: `hermes-jev` (gate_mode: advisory, nervous_mode: correct_next)
- **Source**: [keeltrace/hermes-jev](https://github.com/keeltrace/hermes-jev)

### Context Engineering for Long-Horizon Agents
- **Three Strategies**:
  1. **Compaction**: Summarize conversation when approaching context limit
  2. **Progressive Summarization**: Incremental summarization of tool results
  3. **Just-in-Time Retrieval**: Load relevant context on demand
- **Tradeoff**: Recall vs. precision in compaction prompts

### RAG (Retrieval-Augmented Generation)
- **Vector DB**: Store embeddings of codebase/docs
- **Retrieval**: Find relevant chunks for current query
- **Generation**: LLM uses retrieved context
- **Limitation**: Chunking strategy affects quality

---

## 🔗 Protocol Architectures

### MCP (Model Context Protocol)
- **Anthropic's standard** for agent-to-tool communication
- **JSON-RPC 2.0** based
- **Transports**: stdio, SSE, Streamable HTTP
- **13,000+ public servers** as of early 2026
- **97M+ monthly SDK downloads**

### A2A (Agent-to-Agent)
- **Google's protocol** for cross-agent communication
- **Cards**: Agent capabilities advertised via Agent Cards
- **Tasks**: Structured task lifecycle
- **Use case**: Multi-agent orchestration across vendors

### ACP (Agent Client Protocol)
- **JetBrains-led** standard for agent-to-host integration
- **Goal**: Decouple agents from specific IDEs
- **Use case**: Agent runs inside any ACP-supporting editor

### Layered Protocol Stack (MCP + A2A + HTTP)
- **Layer 1**: HTTP (transport)
- **Layer 2**: MCP (tool access)
- **Layer 3**: A2A (agent coordination)
- **Emerging pattern**: Production multi-agent systems

---

## 🧩 Emerging AI Architecture Patterns

### MCP Proxy Aggregator Pattern
- **Purpose**: Connect multiple upstream MCP servers to single client
- **Namespacing**: `github__create_pr` to avoid collisions
- **Two variants**:
  - Static-merge: Union of all tools (degrades past 10-15 tools)
  - Scoped: Per-request tool filtering (recommended)

### MCP Apps Interactive UI Protocol
- **Purpose**: Agents render interactive UI components in host
- **Use case**: Forms, dashboards, visualizations inside agent chat
- **Status**: Emerging, early implementations

### Agent Portability via ACP
- **Goal**: Write agent once, run in any ACP-supporting host
- **Challenge**: Not all editors support ACP yet
- **Status**: Emerging, JetBrains leading adoption

### Verifiable Execution
- **Goal**: Cryptographic proof of agent actions
- **Use case**: Compliance, audit trails, safety
- **Status**: Emerging, research phase

### Federated Agent Networks
- **Goal**: Agents from different vendors work together
- **Challenge**: Protocol standardization, trust
- **Status**: Emerging, early experiments

---

## 🏭 Production Architecture Patterns

### Containerized Agent Sandboxes
- **Docker isolation**: Agents run in containers
- **Benefits**: Reproducibility, security, resource limits
- **Image**: `nikolaik/python-nodejs:python3.11-nodejs20`

### Git-Native Agents
- **Aider pattern**: Every AI edit becomes atomic git commit
- **Benefits**: Revert, diff, audit trail
- **Integration**: Standard git workflow

### Context Compaction + Structured Note-Taking
- **Vault-based**: Atomic notes, densely linked (Zettelkasten)
- **Progressive refinement**: Notes get revisited, restructured
- **Source**: AI Matrix Trends vault methodology

---

## 📊 Comparison: Architecture Patterns

| Pattern | Complexity | Scalability | Safety | Adoption |
|---------|-----------|-------------|--------|----------|
| Single-Agent | Low | Low | Medium | High |
| Multi-Agent | High | High | Medium | Growing |
| MCP + Tools | Medium | Medium | High | High |
| Jev Context | Medium | High | High | Growing |
| RAG | Medium | High | Medium | High |
| MCP Proxy | High | High | Medium | Growing |
| A2A Multi-Agent | Very High | Very High | Low | Emerging |
| ACP Portable | Medium | High | Medium | Emerging |

---

## 🔗 Related Notes in This Vault

### Architecture Patterns (05 - Architecture/)
- [202609202000 - MCP Proxy Aggregator Pattern](./05%20-%20Architecture/202609202000%20-%20MCP%20Proxy%20Aggregator%20Pattern.md)
- [MOC-Trending-Agents](./07%20-%20Structure/MOC-Trending-Agents.md)
- [202609202002 - Multi-Agent Orchestration with Guardrail Layering](./05%20-%20Architecture/202609202002%20-%20Multi-Agent%20Orchestration%20with%20Guardrail%20Layering.md)
- [202609202003 - MCP Apps Interactive UI Protocol](./05%20-%20Architecture/202609202003%20-%20MCP%20Apps%20Interactive%20UI%20Protocol.md)
- [202609202004 - Layered Protocol Stack MCP A2A Streamable HTTP](./05%20-%20Architecture/202609202004%20-%20Layered%20Protocol%20Stack%20MCP%20A2A%20Streamable%20HTTP.md)
- [202609202005 - Agent Portability via Agent Client Protocol](./05%20-%20Architecture/202609202005%20-%20Agent%20Portability%20via%20Agent%20Client%20Protocol.md)
- [202609202020 - Orchestrator-Worker Delegation Pattern](./05%20-%20Architecture/202609202020%20-%20Orchestrator-Worker%20Delegation%20Pattern.md)
- [202609202021 - Context Compaction and Structured Note-Taking](./05%20-%20Architecture/202609202021%20-%20Context%20Compaction%20and%20Structured%20Note-Taking.md)
- [202609202022 - MCP Hybrid Client-Server Architecture](./05%20-%20Architecture/202609202022%20-%20MCP%20Hybrid%20Client-Server%20Architecture.md)
- [202609202023 - MCP Gateway Aggregation Layer](./05%20-%20Architecture/202609202023%20-%20MCP%20Gateway%20Aggregation%20Layer.md)
- [202609202024 - Orchestrator Worker Multi-Agent Delegation](./05%20-%20Architecture/202609202024%20-%20Orchestrator%20Worker%20Multi-Agent%20Delegation.md)
- [202609202025 - Compaction and Note-Taking for Long-Horizon Context](./05%20-%20Architecture/202609202025%20-%20Compaction%20and%20Note-Taking%20for%20Long-Horizon%20Context.md)
- [202609200951 - MCP Server-Side LLM Reusable Agent Pattern](./09%20-%20Trend%20Radar/Emerging/202609200951%20-%20MCP%20Server-Side%20LLM%20Reusable%20Agent%20Pattern.md)
- [202609200931 - Adaptive Planning Magentic Orchestration Pattern](./05%20-%20Architecture/202609200931%20-%20Adaptive%20Planning%20Magentic%20Orchestration%20Pattern.md)
- [202609200932 - Fan-Out Fan-In Parallel Agent Pattern](./05%20-%20Architecture/202609200932%20-%20Fan-Out%20Fan-In%20Parallel%20Agent%20Pattern.md)
- [2026092030 - Bidirectional MCP Agent Pattern](./05%20-%20Architecture/2026092030%20-%20Bidirectional%20MCP%20Agent%20Pattern.md)
- [2026092031 - Event-Driven Agent Concurrency Pattern](./05%20-%20Architecture/2026092031%20-%20Event-Driven%20Agent%20Concurrency%20Pattern.md)
- [2026092032 - Tiered Routing Model Cascade Pattern](./05%20-%20Architecture/2026092032%20-%20Tiered%20Routing%20Model%20Cascade%20Pattern.md)
- [2026092030 - Context Engineering](./05%20-%20Architecture/2026092030%20-%20Context%20Engineering.md)
- [2026092031 - Sub-Agent Delegation Pattern](./05%20-%20Architecture/2026092031%20-%20Sub-Agent%20Delegation%20Pattern.md)
- [2026092031 - Agent Teams Pattern](./09%20-%20Trend%20Radar/Emerging/2026092031%20-%20Agent%20Teams%20Pattern.md)

### Plugins (04 - Plugins/)
- [202609200759 - Hermes Agent](./03%20-%20Agents/202609200759%20-%20Hermes%20Agent.md) — Typesafe context engine for Hermes
- [202609202000 - Jev Agent Router](./04%20-%20Plugins/202609202000%20-%20Jev%20Agent%20Router.md) — Agent routing via Jev
- [202609200803 - Context7 MCP](./04%20-%20Plugins/202609200803%20-%20Context7%20MCP.md) — Live library documentation
- [202609200804 - FAL MCP Server](./04%20-%20Plugins/202609200804%20-%20FAL%20MCP%20Server.md) — Image generation
- [202609202000 - Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md) — Browser automation
- [202609202000 - Firecrawl MCP Server](./04%20-%20Plugins/202609202000%20-%20Firecrawl%20MCP%20Server.md) — Web scraping

### Agents (03 - Agents/)
- [202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md) — Anthropic CLI agent
- [202609200758 - OpenCode](./03%20-%20Agents/202609200758%20-%20OpenCode.md) — Open-source CLI agent
- [202609200759 - Hermes Agent](./03%20-%20Agents/202609200759%20-%20Hermes%20Agent.md) — Nous Research multi-platform agent

---

## 📚 Sources

- [MCP Official](https://modelcontextprotocol.io/)
- [Google A2A Protocol](https://github.com/google/A2A)
- [Agent Client Protocol](https://agentclientprotocol.com/)
- [Hermes Agent Docs](https://hermes-agent.nousresearch.com/)
- [Jev Context Engine](https://github.com/keeltrace/hermes-jev)
