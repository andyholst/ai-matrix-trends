# AI Matrix Trends

> A living Obsidian vault tracking trending AI coding agents, architecture patterns, plugins, and tooling.

---

## 🚀 Trending Agents

| Agent | Ecosystem | Stars | Description |
|-------|-----------|-------|-------------|
|[Hermes Agent](./03%20-%20Agents/202609200759%20-%20Hermes%20Agent.md) | Nous Research | ⭐ 247k+ | Self-hosted general-purpose agent, self-improving |
|[OpenCode](./03%20-%20Agents/202609200758%20-%20OpenCode.md) | Open source | ⭐ 182k+ | Open-source CLI agent, 75+ providers, desktop app |
|[Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md) | Anthropic | — | CLI agent with MCP integration and multi-file editing |
|[Codex](./03%20-%20Agents/202609202000%20-%20Codex.md) | OpenAI | — | Cloud-native agent with sandboxed execution |
|[Cursor](./03%20-%20Agents/202609202000%20-%20Cursor.md) | Anysphere | — | IDE-integrated AI agent with codebase indexing |
|[Cline](./03%20-%20Agents/202609202000%20-%20Cline.md) | Cline Bot | ⭐ 35k+ | VS Code extension with autonomous capabilities |
|[Aider](./03%20-%20Agents/202609202000%20-%20Aider.md) | Aider-AI | ⭐ 25k+ | Terminal pair-programming agent with repo mapping |
| [Windsurf](./03%20-%20Agents/202609200800%20-%20Windsurf.md) | Cognition | — | IDE folded into Devin Desktop, SWE-2 model |
| [GitHub Copilot Agent](./03%20-%20Agents/202609202001%20-%20GitHub%20Copilot%20Agent.md) | Microsoft/GitHub | — | Agentic coding surface in VS Code, Visual Studio, JetBrains |
| [Gemini CLI](./03%20-%20Agents/202609202002%20-%20Gemini%20CLI.md) | Google | — | Terminal-first AI coding agent, free tier |
| [Kilo Code](./03%20-%20Agents/202609202003%20-%20Kilo%20Code.md) | Kilo | — | VS Code agent focused on context control |
| [RooCode](./03%20-%20Agents/202609202004%20-%20RooCode.md) | RooCode Inc | — | Reliability-first VS Code agent for large monorepos |
| [JetBrains Junie](./03%20-%20Agents/202609202005%20-%20JetBrains%20Junie.md) | JetBrains | — | Native IDE agent for IntelliJ, PyCharm, WebStorm |
| Pi | Pi AI | — | Conversational coding agent by Inflection alumni |

---

## 🔌 Top Plugins & Extensions

### Hermes Ecosystem
|[Jev Agent Router](./04%20-%20Plugins/202609202000%20-%20Jev%20Agent%20Router.md) | Typesafe context engine with agent_route MCP server | ✅ Active |
|[Hermes Kanban Dashboard](./04%20-%20Plugins/202609200805%20-%20Hermes%20Kanban%20Dashboard.md) | Multi-agent work queue | ✅ Active |
| [Hermes Curator](./04%20-%20Plugins/202609200806%20-%20Hermes%20Curator.md) | Session memory consolidation | ✅ Active |
| [Hermes Plugin System](./04%20-%20Plugins/202609202013%20-%20Hermes%20Plugin%20System.md) | Comprehensive plugin architecture for Hermes Agent | ✅ Active |

### OpenCode Ecosystem
|[OpenCode Firecrawl](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Firecrawl.md) | Firecrawl CLI wrapper with file-based results | ✅ Active |
| [OpenCode Supermemory](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Supermemory.md) | Persistent cross-session memory via Supermemory | ✅ Active |
| [OpenCode Dynamic Context Pruning](./04%20-%20Plugins/202609202012%20-%20OpenCode%20Dynamic%20Context%20Pruning.md) | Token reduction plugin, 60-90% savings | ✅ Active |
| [OpenCode Oh-My-Openagent](./04%20-%20Plugins/202609202014%20-%20OpenCode%20Oh-My-Openagent.md) | All-in-one plugin with 10 specialized agents | ✅ Active |

### Cross-Agent Plugins
|[Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md) | Claude, Cursor, Windsurf, OpenCode | Browser automation |
|[Firecrawl MCP Server](./04%20-%20Plugins/202609202000%20-%20Firecrawl%20MCP%20Server.md) | All MCP-compatible | Web scrape/search/crawl/map/parse tools |
|[Context7 MCP](./04%20-%20Plugins/202609200803%20-%20Context7%20MCP.md) | Claude, Cursor, Windsurf, OpenCode | Live library documentation |
| [FAL MCP Server](./04%20-%20Plugins/202609200804%20-%20FAL%20MCP%20Server.md) | Claude, Cursor, Windsurf, OpenCode | 1,000+ generative models |
| [Playwright MCP](./04%20-%20Plugins/202609202010%20-%20Playwright%20MCP.md) | Claude, Cursor, Windsurf, VS Code, OpenCode | Microsoft's official browser automation MCP |
| [Chrome DevTools MCP](./04%20-%20Plugins/202609202011%20-%20Chrome%20DevTools%20MCP.md) | Claude, Cursor, Windsurf, VS Code | Google's official DevTools Protocol MCP |
| [Claude Code Auto Permission](./04%20-%20Plugins/202609200807%20-%20Claude%20Code%20Auto%20Permission.md) | Claude Code | Server-evaluated tool call permissions |

---

## 🏗️ Architecture Patterns

### Core Patterns
| [MCP Proxy Aggregator Pattern](./05%20-%20Architecture/202609202000%20-%20MCP%20Proxy%20Aggregator%20Pattern.md) | Namespaced routing across upstream MCP servers | Emerging |
| [Context Engineering for Long-Horizon Agents](./05%20-%20Architecture/202609202001%20-%20Context%20Engineering%20for%20Long-Horizon%20Agents.md) | Compaction, structured notes, just-in-time retrieval | Growing |
| [Multi-Agent Orchestration with Guardrail Layering](./05%20-%20Architecture/202609202002%20-%20Multi-Agent%20Orchestration%20with%20Guardrail%20Layering.md) | Fan-out/fan-in with validation layers | Emerging |
| [MCP Apps Interactive UI Protocol](./05%20-%20Architecture/202609202003%20-%20MCP%20Apps%20Interactive%20UI%20Protocol.md) | Agents render interactive UI components in host | Emerging |
| [Layered Protocol Stack MCP A2A HTTP](./05%20-%20Architecture/202609202004%20-%20Layered%20Protocol%20Stack%20MCP%20A2A%20Streamable%20HTTP.md) | MCP + A2A + HTTP three-layer stack | Growing |
| [Agent Portability via ACP](./05%20-%20Architecture/202609202005%20-%20Agent%20Portability%20via%20Agent%20Client%20Protocol.md) | Decoupling agents from editor plugins | Emerging |
| [Orchestrator-Worker Delegation Pattern](./05%20-%20Architecture/202609202020%20-%20Orchestrator-Worker%20Delegation%20Pattern.md) | Task decomposition with heterogeneous model tiers | Emerging |
| [Context Compaction and Structured Note-Taking](./05%20-%20Architecture/202609202021%20-%20Context%20Compaction%20and%20Structured%20Note-Taking.md) | Compaction + agentic memory for long-horizon tasks | Growing |
| [MCP Hybrid Client-Server Architecture](./05%20-%20Architecture/202609202022%20-%20MCP%20Hybrid%20Client-Server%20Architecture.md) | LLMs on both MCP server and client for flexibility | Emerging |

---

## 🛠️ Configuration Snippets & Use Cases

- [Claude Code Plugin Distribution for Team Workflow Standardization](./06%20-%20Use%20Cases/202609202000%20-%20Claude%20Code%20Plugin%20Distribution%20for%20Team%20Workflow%20Standardization.md)
- [Claude Code Hooks for CI/CD Automation](./06%20-%20Use%20Cases/202609202001%20-%20Claude%20Code%20Hooks%20for%20CI-CD%20Automation.md)
- [Multi-Server MCP Orchestration for Cross-Tool Workflows](./06%20-%20Use%20Cases/202609202002%20-%20Multi-Server%20MCP%20Orchestration%20for%20Cross-Tool%20Workflows.md)
- [Context7 MCP for Live Library Documentation](./06%20-%20Use%20Cases/202609202003%20-%20Context7%20MCP%20for%20Live%20Library%20Documentation.md)
- [Chrome DevTools MCP for End-to-End Browser Debugging](./06%20-%20Use%20Cases/202609202004%20-%20Chrome%20DevTools%20MCP%20for%20End-to-End%20Browser%20Debugging.md)
- [Auto-Commit Checkpoint Workflow with Stop Hooks and Git](./06%20-%20Use%20Cases/202609202005%20-%20Auto-Commit%20Checkpoint%20Workflow%20with%20Stop%20Hooks%20and%20Git.md)
- [Project-Level Rules for AI Code Standardization](./06%20-%20Use%20Cases/202609202030%20-%20Project-Level%20Rules%20for%20AI%20Code%20Standardization.md)
- [Throwaway Scripts and One-Off Automation](./06%20-%20Use%20Cases/202609202031%20-%20Throwaway%20Scripts%20and%20One-Off%20Automation.md)
- [Agentic Debugging with CLI Observability](./06%20-%20Use%20Cases/202609202032%20-%20Agentic%20Debugging%20with%20CLI%20Observability.md)

---

## 📊 Trend Radar

### Heating Up 🔥
- MCP server ecosystem explosion (100+ community servers)
- Multi-agent workflows via delegation
- Containerized agent sandboxes (Docker profiles)
- Skill/plugin marketplaces maturing
- Browser automation MCPs (Playwright, Chrome DevTools)

### Stable 📈
- Tool-calling as standard interface
- RAG + context compression patterns
- IDE integrations (VS Code, JetBrains, Zed)
- Context engineering for long-horizon tasks

### Emerging 🌱
- Agent-to-agent communication protocols (A2A, ACP)
- Verifiable execution (cryptographic proof)
- Federated agent networks
- Personal agent memory systems
- Hybrid client-server MCP architectures

---

## 📁 Vault Structure

```
ai-matrix-trends/
├── 00 - Inbox/           # Raw observations → triage
├── 01 - Fleeting/        # Quick capture
├── 02 - Literature/      # Source material
├── 03 - Agents/          # Agent profiles & configs
├── 04 - Plugins/         # Plugin documentation
├── 05 - Architecture/    # Pattern notes
├── 06 - Use Cases/       # Real-world workflows
├── 07 - Structure/       # Maps of Content (MOCs)
├── 08 - Projects/        # Time-bound work
└── 99 - Attachments/     # Images, PDFs
```

---

## 🔄 Maintenance

This README is the vault's **dashboard**. It refreshes daily via cron job at 20:00.

> **Open this vault in Obsidian** for the full linked experience — every note has install guides, config snippets, and real-world patterns.

---

*Last refreshed: 2026-09-20 20:35*
*Agent profile: ai-matrix-trends*
*Cron job: [AI Matrix Trends - Daily Trend Scan](./scripts/daily-scan-prompt.md)*
