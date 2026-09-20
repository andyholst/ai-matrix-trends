# AI Matrix Trends

> A living Obsidian vault tracking trending AI coding agents, architecture patterns, plugins, and tooling.

---

## 🚀 Trending Agents

| Agent | Ecosystem | Stars | Description |
|-------|-----------|-------|-------------|
| [Hermes Agent](./03%20-%20Agents/202609200759%20-%20Hermes%20Agent.md) | Nous Research | ⭐ 247k+ | Self-hosted general-purpose agent, self-improving |
| [OpenCode](./03%20-%20Agents/202609200758%20-%20OpenCode.md) | Open source | ⭐ 182k+ | Open-source CLI agent, 75+ providers, desktop app |
| [Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md) | Anthropic | — | CLI agent with MCP integration and multi-file editing |
| [Codex](./03%20-%20Agents/202609202000%20-%20Codex.md) | OpenAI | — | Cloud-native agent with sandboxed execution |
| [Cursor](./03%20-%20Agents/202609202000%20-%20Cursor.md) | Anysphere | — | IDE-integrated AI agent with codebase indexing |
| [Cline](./03%20-%20Agents/202609202000%20-%20Cline.md) | Cline Bot | ⭐ 35k+ | VS Code extension with autonomous capabilities |
| [Aider](./03%20-%20Agents/202609202000%20-%20Aider.md) | Aider-AI | ⭐ 25k+ | Terminal pair-programming agent with repo mapping |
| [Windsurf](./03%20-%20Agents/202609200800%20-%20Windsurf.md) | Cognition | — | IDE folded into Devin Desktop, SWE-2 model |
| [GitHub Copilot Agent](./03%20-%20Agents/202609202001%20-%20GitHub%20Copilot%20Agent.md) | Microsoft/GitHub | — | Agentic coding surface in VS Code, Visual Studio, JetBrains |
| [Gemini CLI](./03%20-%20Agents/202609202002%20-%20Gemini%20CLI.md) | Google | — | Terminal-first AI coding agent, free tier |
| [Kilo Code](./03%20-%20Agents/202609202003%20-%20Kilo%20Code.md) | Kilo | — | VS Code agent focused on context control |
| [RooCode](./03%20-%20Agents/202609202004%20-%20RooCode.md) | RooCode Inc | — | Reliability-first VS Code agent for large monorepos |
| [JetBrains Junie](./03%20-%20Agents/202609202005%20-%20JetBrains%20Junie.md) | JetBrains | — | Native IDE agent for IntelliJ, PyCharm, WebStorm |
| [Devin](./03%20-%20Agents/202609202000%20-%20Devin.md) | Cognition | — | Cloud-native autonomous agent, issue-to-PR workflow |
| [Google Antigravity](./03%20-%20Agents/202609202001%20-%20Google%20Antigravity.md) | Google | — | Gemini 3-based agentic IDE, 47% awareness |
| [Augment](./03%20-%20Agents/202609202002%20-%20Augment.md) | Augment Code | — | Code-intelligence platform for enterprise teams |
| [AWS Kiro](./03%20-%20Agents/202609202003%20-%20AWS%20Kiro.md) | Amazon | — | Spec-driven agentic environment for AWS-centric teams |
| [Pi](./03%20-%20Agents/202609202004%20-%20Pi.md) | Pi AI | — | Lightweight open-source CLI agent, multi-provider + local model support |

---

## 🔌 Top Plugins & Extensions

### Hermes Ecosystem
| Plugin | Description | Status |
|--------|-------------|--------|
| [Jev Agent Router](./04%20-%20Plugins/202609202000%20-%20Jev%20Agent%20Router.md) | Typesafe context engine with agent_route MCP server | ✅ Active |
| [Hermes Kanban Dashboard](./04%20-%20Plugins/202609200805%20-%20Hermes%20Kanban%20Dashboard.md) | Multi-agent work queue | ✅ Active |
| [Hermes Curator](./04%20-%20Plugins/202609200806%20-%20Hermes%20Curator.md) | Session memory consolidation | ✅ Active |
| [Hermes Plugin System](./04%20-%20Plugins/202609202013%20-%20Hermes%20Plugin%20System.md) | Comprehensive plugin architecture for Hermes Agent | ✅ Active |

### OpenCode Ecosystem
| Plugin | Description | Status |
|--------|-------------|--------|
| [OpenCode Firecrawl](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Firecrawl.md) | Firecrawl CLI wrapper with file-based results | ✅ Active |
| [OpenCode Supermemory](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Supermemory.md) | Persistent cross-session memory via Supermemory | ✅ Active |
| [OpenCode Dynamic Context Pruning](./04%20-%20Plugins/202609202012%20-%20OpenCode%20Dynamic%20Context%20Pruning.md) | Token reduction plugin, 60-90% savings | ✅ Active |
| [OpenCode Oh-My-Openagent](./04%20-%20Plugins/202609202014%20-%20OpenCode%20Oh-My-Openagent.md) | All-in-one plugin with 10 specialized agents | ✅ Active |

### Cross-Agent Plugins
| Plugin | Agents | Description |
|--------|--------|-------------|
| [Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md) | Claude, Cursor, Windsurf, OpenCode | Browser automation |
| [Firecrawl MCP Server](./04%20-%20Plugins/202609202000%20-%20Firecrawl%20MCP%20Server.md) | All MCP-compatible | Web scrape/search/crawl/map/parse tools |
| [Context7 MCP](./04%20-%20Plugins/202609200803%20-%20Context7%20MCP.md) | Claude, Cursor, Windsurf, OpenCode | Live library documentation |
| [FAL MCP Server](./04%20-%20Plugins/202609200804%20-%20FAL%20MCP%20Server.md) | Claude, Cursor, Windsurf, OpenCode | 1,000+ generative models |
| [Playwright MCP](./04%20-%20Plugins/202609202010%20-%20Playwright%20MCP.md) | Claude, Cursor, Windsurf, VS Code, OpenCode | Microsoft's official browser automation MCP |
| [Chrome DevTools MCP](./04%20-%20Plugins/202609202011%20-%20Chrome%20DevTools%20MCP.md) | Claude, Cursor, Windsurf, VS Code | Google's official DevTools Protocol MCP |
| [Claude Code Auto Permission](./04%20-%20Plugins/202609200807%20-%20Claude%20Code%20Auto%20Permission.md) | Claude Code | Server-evaluated tool call permissions |

---

## 🏗️ Architecture Patterns

### Core Patterns
| Pattern | Description | Status |
|---------|-------------|--------|
| [MCP Proxy Aggregator Pattern](./05%20-%20Architecture/202609202000%20-%20MCP%20Proxy%20Aggregator%20Pattern.md) | Namespaced routing across upstream MCP servers | Emerging |
| [Context Engineering for Long-Horizon Agents](./05%20-%20Architecture/202609202001%20-%20Context%20Engineering%20for%20Long-Horizon%20Agents.md) | Compaction, structured notes, just-in-time retrieval | Growing |
| [Multi-Agent Orchestration with Guardrail Layering](./05%20-%20Architecture/202609202002%20-%20Multi-Agent%20Orchestration%20with%20Guardrail%20Layering.md) | Fan-out/fan-in with validation layers | Emerging |
| [MCP Apps Interactive UI Protocol](./05%20-%20Architecture/202609202003%20-%20MCP%20Apps%20Interactive%20UI%20Protocol.md) | Agents render interactive UI components in host | Emerging |
| [Layered Protocol Stack MCP A2A HTTP](./05%20-%20Architecture/202609202004%20-%20Layered%20Protocol%20Stack%20MCP%20A2A%20Streamable%20HTTP.md) | MCP + A2A + HTTP three-layer stack | Growing |
| [Agent Portability via ACP](./05%20-%20Architecture/202609202005%20-%20Agent%20Portability%20via%20Agent%20Client%20Protocol.md) | Decoupling agents from editor plugins | Emerging |
| [Orchestrator-Worker Delegation Pattern](./05%20-%20Architecture/202609202020%20-%20Orchestrator-Worker%20Delegation%20Pattern.md) | Task decomposition with heterogeneous model tiers | Emerging |
| [Context Compaction and Structured Note-Taking](./05%20-%20Architecture/202609202021%20-%20Context%20Compaction%20and%20Structured%20Note-Taking.md) | Compaction + agentic memory for long-horizon tasks | Growing |
| [MCP Hybrid Client-Server Architecture](./05%20-%20Architecture/202609202022%20-%20MCP%20Hybrid%20Client-Server%20Architecture.md) | LLMs on both MCP server and client for flexibility | Emerging |
| [MCP Gateway Aggregation Layer](./05%20-%20Architecture/202609202023%20-%20MCP%20Gateway%20Aggregation%20Layer.md) | Gateway federating multiple MCP servers behind one client endpoint | Emerging |
| [Orchestrator Worker Multi-Agent Delegation](./05%20-%20Architecture/202609202024%20-%20Orchestrator%20Worker%20Multi-Agent%20Delegation.md) | Lead agent dispatching stateless workers with clean context windows | Emerging |
| [Compaction and Note-Taking for Long-Horizon Context](./05%20-%20Architecture/202609202025%20-%20Compaction%20and%20Note-Taking%20for%20Long-Horizon%20Context.md) | Compaction + external notes for coherence beyond context limits | Growing |

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
- [CI/CD Pipeline Automation with Claude Code Hooks and GitHub Actions](./06%20-%20Use%20Cases/202609202030%20-%20CI-CD%20Pipeline%20Automation%20with%20Claude%20Code%20Hooks%20and%20GitHub%20Actions.md)
- [Multi-Server MCP Orchestration for Enterprise Agent Workflows](./06%20-%20Use%20Cases/202609202031%20-%20Multi-Server%20MCP%20Orchestration%20for%20Enterprise%20Agent%20Workflows.md)
- [Custom Skills and Slash Commands as Team Workflow Accelerators](./06%20-%20Use%20Cases/202609202032%20-%20Custom%20Skills%20and%20Slash%20Commands%20as%20Team%20Workflow%20Accelerators.md)

---

## 📊 Trend Radar

| Heating Up 🔥 | Summary |
|---------------|---------|
|[MCP Server Ecosystem Explosion](./09%20-%20Trend%20Radar/Heating%20Up/202609200100%20-%20MCP%20Server%20Ecosystem%20Explosion.md) | 100+ community servers, new ones shipping weekly |
|[Terminal Agent Wars](./09%20-%20Trend%20Radar/Heating%20Up/202609200101%20-%20Terminal%20Agent%20Wars.md) | Claude Code vs OpenCode vs Codex vs Cline |

| Stable 📈 | Summary |
|-----------|---------|
|[Tool-Calling as Standard Interface](./09%20-%20Trend%20Radar/Stable/202609200102%20-%20Tool-Calling%20as%20Standard%20Interface.md) | All agents use structured tool-calling |
|[Containerized Agent Sandboxes](./09%20-%20Trend%20Radar/Stable/202609200103%20-%20Containerized%20Agent%20Sandboxes.md) | Docker isolation for agent safety |

| Emerging 🌱 | Summary |
|-------------|---------|
|[Agent-to-Agent Communication Protocols](./09%20-%20Trend%20Radar/Emerging/202609200104%20-%20Agent-to-Agent%20Communication%20Protocols.md) | A2A, ACP enabling multi-agent orchestration |
|[Personal Agent Memory Systems](./09%20-%20Trend%20Radar/Emerging/202609200105%20-%20Personal%20Agent%20Memory%20Systems.md) | Cross-session memory and personalization |

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
├── 09 - Trend Radar/     # Trend analysis
│   ├── Heating Up/       # Rapid growth signals
│   ├── Stable/           # Established patterns
│   └── Emerging/         # Early signals
└── 99 - Attachments/     # Images, PDFs
```

---

## 🔄 Maintenance

This README is the vault's **dashboard**. It refreshes daily via cron job at 20:00.

> **Open this vault in Obsidian** for the full linked experience — every note has install guides, config snippets, and real-world patterns.

---

*Last refreshed: 2026-09-20 20:45*
*Agent profile: ai-matrix-trends*
*Cron job: [AI Matrix Trends - Daily Trend Scan](./scripts/daily-scan-prompt.md)*
