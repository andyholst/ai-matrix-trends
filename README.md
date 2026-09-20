# AI Matrix Trends

> A living Obsidian vault tracking trending AI coding agents, architecture patterns, plugins, and tooling.

---

## 🚀 Trending Agents

*Top 5 scored trending — Last updated: 2026-09-20*

*See [Agent Master Index](./03%20-%20Agents/00%20-%20Agent%20Master%20Index.md) for complete list*

| # | Name | Score | Type | Stars | Status |
|---|------|-------|------|-------|--------|
| 1 | [202609202000 - Aider](./03%20-%20Agents/202609202000%20-%20Aider.md) | 130 | agent | 0 | Heating Up |
| 2 | [202609200912 - Nimbalyst](./03%20-%20Agents/202609200912%20-%20Nimbalyst.md) | 110 | agent | 0 | Heating Up |
| 3 | [202609202000 - Cursor](./03%20-%20Agents/202609202000%20-%20Cursor.md) | 105 | agent | 0 | Heating Up |
| 4 | [202609202000 - Devin](./03%20-%20Agents/202609202000%20-%20Devin.md) | 100 | agent | 0 | Heating Up |
| 5 | [202609202000 - Codex](./03%20-%20Agents/202609202000%20-%20Codex.md) | 95 | agent | 0 | Heating Up |


## 🔌 Top Plugins & Extensions

*Top 5 scored trending — Last updated: 2026-09-20*

*See [Plugin Master Index](./04%20-%20Plugins/00%20-%20Plugin%20Master%20Index.md) for complete per-agent tables*

| # | Name | Score | Type | Stars | Status |
|---|------|-------|------|-------|--------|
| 1 | [2026092021 - Sentry MCP](./04%20-%20Plugins/2026092021%20-%20Sentry%20MCP.md) | 33 | plugin | 858 | Stable |
| 2 | [2026092022 - Browserbase MCP](./04%20-%20Plugins/2026092022%20-%20Browserbase%20MCP.md) | 32 | plugin | 0 | Stable |
| 3 | [202609202000 - Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md) | 29 | plugin | 0 | Stable |
| 4 | [202609200804 - FAL MCP Server](./04%20-%20Plugins/202609200804%20-%20FAL%20MCP%20Server.md) | 29 | plugin | 0 | Stable |
| 5 | [202609202010 - Playwright MCP](./04%20-%20Plugins/202609202010%20-%20Playwright%20MCP.md) | 29 | plugin | 0 | Stable |


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
| [MCP Server-Side LLM Reusable Agent Pattern](./05%20-%20Architecture/202609200930%20-%20MCP%20Server-Side%20LLM%20Reusable%20Agent%20Pattern.md) | MCP server embeds its own LLM as a self-contained reusable agent | Emerging |
| [Adaptive Planning (Magentic) Orchestration Pattern](./05%20-%20Architecture/202609200931%20-%20Adaptive%20Planning%20Magentic%20Orchestration%20Pattern.md) | Manager agent dynamically builds and pivots a task plan | Emerging |
| [Fan-Out / Fan-In Parallel Agent Pattern](./05%20-%20Architecture/202609200932%20-%20Fan-Out%20Fan-In%20Parallel%20Agent%20Pattern.md) | Dispatcher fans out to N parallel agents, collector aggregates | Emerging |
| [Bidirectional MCP Agent Pattern](./05%20-%20Architecture/2026092030%20-%20Bidirectional%20MCP%20Agent%20Pattern.md) | Agent as both MCP client and server simultaneously | Emerging |
| [Event-Driven Agent Concurrency Pattern](./05%20-%20Architecture/2026092031%20-%20Event-Driven%20Agent%20Concurrency%20Pattern.md) | Pub/sub event bus for async agent coordination | Emerging |
| [Tiered Routing Model Cascade Pattern](./05%20-%20Architecture/2026092032%20-%20Tiered%20Routing%20Model%20Cascade%20Pattern.md) | Multi-layer classifier routing to cheapest capable model | Emerging |
| [Context Engineering](./05%20-%20Architecture/2026092030%20-%20Context%20Engineering.md) | Curating minimal high-signal token sets for agent context | Growing |
| [Sub-Agent Delegation Pattern](./05%20-%20Architecture/2026092031%20-%20Sub-Agent%20Delegation%20Pattern.md) | Parent orchestrator delegating to isolated child agents | Emerging |
| [Agent Teams Pattern](./05%20-%20Architecture/2026092032%20-%20Agent%20Teams%20Pattern.md) | Parallel agents with shared task lists and peer messaging | Emerging |

**Full index:** [AI Architecture Master Index](./05%20-%20Architecture/00%20-%20AI%20Architecture%20Master%20Index.md) (12 patterns, comparison table, protocol analysis)

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
- [Multi-Agent Team Orchestration for Parallel Development](./06%20-%20Use%20Cases/2026092040%20-%20Multi-Agent%20Team%20Orchestration%20for%20Parallel%20Development.md)
- [AI-Powered Automated Code Review and QA](./06%20-%20Use%20Cases/2026092041%20-%20AI-Powered%20Automated%20Code%20Review%20and%20QA.md)
- [Automated Documentation Generation and Maintenance](./06%20-%20Use%20Cases/2026092042%20-%20Automated%20Documentation%20Generation%20and%20Maintenance.md)
- [Spec-Driven Development with Spec Kit](./06%20-%20Use%20Cases/2026092040%20-%20Spec-Driven%20Development%20with%20Spec%20Kit.md)
- [Git Worktree Isolation for Parallel AI Agents](./06%20-%20Use%20Cases/2026092041%20-%20Git%20Worktree%20Isolation%20for%20Parallel%20AI%20Agents.md)
- [CLAUDE.md as Runtime Configuration for Agent Behavior](./06%20-%20Use%20Cases/2026092042%20-%20CLAUDE.md%20as%20Runtime%20Configuration%20for%20Agent%20Behavior.md)

---

## 📊 Trend Radar

*Last updated: 2026-09-20*

### Heating Up

| # | Name | Score | Type | Stars | Status |
|---|------|-------|------|-------|--------|
| 1 | [202609202000 - Aider](./03%20-%20Agents/202609202000%20-%20Aider.md) | 130 | agent | 0 | Heating Up |
| 2 | [202609200912 - Nimbalyst](./03%20-%20Agents/202609200912%20-%20Nimbalyst.md) | 110 | agent | 0 | Heating Up |
| 3 | [202609202000 - Cursor](./03%20-%20Agents/202609202000%20-%20Cursor.md) | 105 | agent | 0 | Heating Up |
| 4 | [202609202000 - Devin](./03%20-%20Agents/202609202000%20-%20Devin.md) | 100 | agent | 0 | Heating Up |
| 5 | [202609202000 - Codex](./03%20-%20Agents/202609202000%20-%20Codex.md) | 95 | agent | 0 | Heating Up |

### Stable

| # | Name | Score | Type | Stars | Status |
|---|------|-------|------|-------|--------|
| 1 | [202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md) | 45 | agent | 0 | Stable |
| 2 | [202609202025 - Devin Desktop](./03%20-%20Agents/202609202025%20-%20Devin%20Desktop.md) | 40 | agent | 0 | Stable |
| 3 | [202609202045 - Pareto](./03%20-%20Agents/202609202045%20-%20Pareto.md) | 35 | agent | 0 | Stable |
| 4 | [2026092021 - Sentry MCP](./04%20-%20Plugins/2026092021%20-%20Sentry%20MCP.md) | 33 | plugin | 858 | Stable |
| 5 | [2026092022 - Browserbase MCP](./04%20-%20Plugins/2026092022%20-%20Browserbase%20MCP.md) | 32 | plugin | 0 | Stable |

### Emerging

| # | Name | Score | Type | Stars | Status |
|---|------|-------|------|-------|--------|
| 1 | [2026092020 - Superpowers](./04%20-%20Plugins/2026092020%20-%20Superpowers.md) | 18 | plugin | 0 | Emerging |
| 2 | [2026092011 - Gemini CLI](./03%20-%20Agents/2026092011%20-%20Gemini%20CLI.md) | 15 | agent | 0 | Emerging |
| 3 | [202609202005 - JetBrains Junie](./03%20-%20Agents/202609202005%20-%20JetBrains%20Junie.md) | 15 | agent | 0 | Emerging |
| 4 | [202609200911 - Amazon Q Developer](./03%20-%20Agents/202609200911%20-%20Amazon%20Q%20Developer.md) | 15 | agent | 0 | Emerging |
| 5 | [202609200914 - JetBrains Air](./03%20-%20Agents/202609200914%20-%20JetBrains%20Air.md) | 15 | agent | 0 | Emerging |


## 📁 Vault Structure

```
ai-matrix-trends/
├── 00 - Inbox/           # Raw observations → triage
├── 01 - Fleeting/        # Quick capture
├── 02 - Literature/      # Source material
├── 03 - Agents/          # Agent profiles & configs
│   └── 00 - Agent Master Index.md  # Top 5 + complete agent list
├── 04 - Plugins/         # Plugin documentation
│   └── 00 - Plugin Master Index.md # Per-agent plugin tables
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

**Complete Lists:**
- [Agent Master Index](./03%20-%20Agents/00%20-%20Agent%20Master%20Index.md) — Top 5 trending + complete agent list (38 agents)
- [Plugin Master Index](./04%20-%20Plugins/00%20-%20Plugin%20Master%20Index.md) — Per-agent plugin tables (42 plugins)
- [Trend Radar](../09%20-%20Trend%20Radar/) — Trend analysis

> **Open this vault in Obsidian** for the full linked experience — every note has install guides, config snippets, and real-world patterns.

---

*Last refreshed: 2026-09-20*
*Agent profile: ai-matrix-trends*
*Cron job: [AI Matrix Trends - Daily Trend Scan](./scripts/daily-scan-prompt.md)*

## 🔌 Plugins by Agent

*Top 5 scored plugins for each agentic tool — Last updated: 2026-09-20*

### Claude Code

*Top plugins/extensions for Claude Code*

| # | Plugin | Score | Stars | Type |
|---|--------|-------|-------|------|
| 1 | [GitHub MCP Server](./04%20-%20Plugins/2026092020%20-%20GitHub%20MCP%20Server.md) | 80 | — |  |
| 2 | [Firecrawl MCP Server](./04%20-%20Plugins/202609202000%20-%20Firecrawl%20MCP%20Server.md) | 80 | — |  |
| 3 | [CodeGraph MCP](./04%20-%20Plugins/2026092023%20-%20CodeGraph%20MCP.md) | 80 | — |  |
| 4 | [Claude Code Code Review](./04%20-%20Plugins/2026092023%20-%20Claude%20Code%20Code%20Review.md) | 70 | 438525 |  |
| 5 | [Context7 MCP](./04%20-%20Plugins/202609200803%20-%20Context7%20MCP.md) | 60 | — |  |

### OpenCode

*Top plugins/extensions for OpenCode*

| # | Plugin | Score | Stars | Type |
|---|--------|-------|-------|------|
| 1 | [GitHub MCP Server](./04%20-%20Plugins/2026092020%20-%20GitHub%20MCP%20Server.md) | 80 | — |  |
| 2 | [Firecrawl MCP Server](./04%20-%20Plugins/202609202000%20-%20Firecrawl%20MCP%20Server.md) | 80 | — |  |
| 3 | [CodeGraph MCP](./04%20-%20Plugins/2026092023%20-%20CodeGraph%20MCP.md) | 80 | — |  |
| 4 | [Context7 MCP](./04%20-%20Plugins/202609200803%20-%20Context7%20MCP.md) | 60 | — |  |
| 5 | [FAL MCP Server](./04%20-%20Plugins/202609200804%20-%20FAL%20MCP%20Server.md) | 60 | — |  |

### Hermes Agent

*Top plugins/extensions for Hermes Agent*

| # | Plugin | Score | Stars | Type |
|---|--------|-------|-------|------|
| 1 | [Jev Agent Router](./04%20-%20Plugins/202609202000%20-%20Jev%20Agent%20Router.md) | 40 | — |  |
| 2 | [Hermes Kanban Dashboard](./04%20-%20Plugins/202609200805%20-%20Hermes%20Kanban%20Dashboard.md) | 20 | — |  |
| 3 | [Hermes Curator](./04%20-%20Plugins/202609200806%20-%20Hermes%20Curator.md) | 20 | — |  |
| 4 | [Hermes Plugin System](./04%20-%20Plugins/202609202013%20-%20Hermes%20Plugin%20System.md) | 20 | — |  |

### Cursor

*Top plugins/extensions for Cursor*

| # | Plugin | Score | Stars | Type |
|---|--------|-------|-------|------|
| 1 | [GitHub MCP Server](./04%20-%20Plugins/2026092020%20-%20GitHub%20MCP%20Server.md) | 80 | — |  |
| 2 | [Firecrawl MCP Server](./04%20-%20Plugins/202609202000%20-%20Firecrawl%20MCP%20Server.md) | 80 | — |  |
| 3 | [CodeGraph MCP](./04%20-%20Plugins/2026092023%20-%20CodeGraph%20MCP.md) | 80 | — |  |
| 4 | [Context7 MCP](./04%20-%20Plugins/202609200803%20-%20Context7%20MCP.md) | 60 | — |  |
| 5 | [FAL MCP Server](./04%20-%20Plugins/202609200804%20-%20FAL%20MCP%20Server.md) | 60 | — |  |

### Codex

*Top plugins/extensions for Codex*

| # | Plugin | Score | Stars | Type |
|---|--------|-------|-------|------|
| 1 | [GitHub MCP Server](./04%20-%20Plugins/2026092020%20-%20GitHub%20MCP%20Server.md) | 80 | — |  |
| 2 | [Firecrawl MCP Server](./04%20-%20Plugins/202609202000%20-%20Firecrawl%20MCP%20Server.md) | 80 | — |  |
| 3 | [CodeGraph MCP](./04%20-%20Plugins/2026092023%20-%20CodeGraph%20MCP.md) | 80 | — |  |
| 4 | [Exa MCP](./04%20-%20Plugins/202609202025%20-%20Exa%20MCP.md) | 60 | — |  |
| 5 | [Supabase MCP](./04%20-%20Plugins/202609202035%20-%20Supabase%20MCP.md) | 60 | — |  |

## 📊 Plugin Compatibility Matrix

| Plugin | claude-code | opencode | hermes | cursor | codex | Score |
|--------|--------|--------|--------|--------|-------|
| [GitHub MCP Server](./04%20-%20Plugins/2026092020%20-%20GitHub%20MCP%20Server.md) | ✅ | ✅ | — | ✅ | ✅ | 80 |
| [Firecrawl MCP Server](./04%20-%20Plugins/202609202000%20-%20Firecrawl%20MCP%20Server.md) | ✅ | ✅ | — | ✅ | ✅ | 80 |
| [CodeGraph MCP](./04%20-%20Plugins/2026092023%20-%20CodeGraph%20MCP.md) | ✅ | ✅ | — | ✅ | ✅ | 80 |
| [Claude Code Code Review](./04%20-%20Plugins/2026092023%20-%20Claude%20Code%20Code%20Review.md) | ✅ | — | — | — | — | 70 |
| [Context7 MCP](./04%20-%20Plugins/202609200803%20-%20Context7%20MCP.md) | ✅ | ✅ | — | ✅ | — | 60 |
| [FAL MCP Server](./04%20-%20Plugins/202609200804%20-%20FAL%20MCP%20Server.md) | ✅ | ✅ | — | ✅ | — | 60 |
| [Vercel Agent Browser](./04%20-%20Plugins/202609200920%20-%20Vercel%20Agent%20Browser.md) | ✅ | ✅ | — | ✅ | — | 60 |
| [Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md) | ✅ | ✅ | — | ✅ | — | 60 |
| [Playwright MCP](./04%20-%20Plugins/202609202010%20-%20Playwright%20MCP.md) | ✅ | ✅ | — | ✅ | — | 60 |
| [Exa MCP](./04%20-%20Plugins/202609202025%20-%20Exa%20MCP.md) | ✅ | — | — | ✅ | ✅ | 60 |

---

