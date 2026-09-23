# AI Matrix Trends — Agent Operating Manual

## Purpose

This is an Obsidian vault for **AI Matrix Trends**, a knowledge system tracking **trending AI coding agents, architecture patterns, plugins, and tooling**. The primary focus:

- **Trending AI coding agents** — Claude Code, OpenAI Codex, OpenCode, Hermes, Cursor, Cline, Aider, Windsurf, and emerging players
- **Architecture patterns** — agent orchestration, tool-calling patterns, context engineering, multi-agent workflows, guardrails
- **Plugins & extensions** — Hermes plugins (jev, mcp, skills), Claude Code extensions, Codex integrations, OpenCode plugins
- **Configuration & setup** — installation guides, config snippets, use-case patterns, real-world workflows

The agent (Hermes) operates within this vault using the **Zettelkasten method** — every insight is an atomic note, richly linked, progressively refined into higher-order structure.

## Agent Mission

The agent's primary role is to **gather, track, and document trending AI coding agents, their architecture patterns, plugins, and configurations**. This means:

1. **Discover** — Continuously scan for trending tools, plugins, and patterns (GitHub stars, social buzz, community adoption)
2. **Analyze** — Evaluate what makes them popular: architecture, UX, integrations, use-case fit
3. **Document** — Create atomic notes with installation, configuration, and real-world usage patterns
4. **Synthesize** — Connect trends to broader patterns (e.g., "every new agent is adopting MCP servers")
5. **Maintain** — Keep notes current as tools evolve; refactor when understanding deepens

### Key Agent Profiles to Track
- **Claude Code** — Anthropic's CLI agent
- **OpenAI Codex** — OpenAI's cloud/agent system
- **OpenCode** — Open-source coding agent
- **Hermes** — Nous Research agent (this agent)
- **Cursor** — IDE-integrated agent
- **Cline** — VS Code extension agent
- **Aider** — Terminal pair-programming agent
- **Windsurf** — Codeium's agent
- **Pi** — Another coding agent
- **Factory Code** — Enterprise autonomous coding agent
- **Sweep AI** — GitHub-integrated AI agent for PRs
- **Greptile** — Codebase intelligence agent
- **OpenHands** — Open-source autonomous software engineer
- **Continue.dev** — VS Code/JetBrains AI assistant
- **Sourcegraph Cody** — Code graph-powered agent
- **Tabnine** — AI code completion agent
- **Mintlify** — Documentation automation agent

### What Makes a Note "Trending"
- Rapid GitHub star growth
- Community adoption (Reddit, HN, Twitter mentions)
- New architecture patterns (e.g., MCP, multi-agent)
- Plugin ecosystem expansion
- Real-world workflow integrations

## Vault Philosophy

1. **One idea per note.** Every note captures a single concept, signal, trend, or data point. Splitting is always better than combining.
2. **Own words.** Notes are written in the agent's own synthesis — never raw copy-paste. If a source must be preserved, embed it as a blockquote with attribution.
3. **Dense linking.** Every note should link to at least 2–3 related notes. The web of links is the value.
4. **Progressive refinement.** Notes are living — they get revisited, restructured, expanded. This is expected and encouraged.
5. **Evergreen over ephemeral.** Permanent notes aim to be timeless; time-sensitive material lives in the inbox/fleeting layer with a clear expiry path.

---

## Vault Structure

```
ai-matrix-trends/
├── .obsidian/              # Obsidian vault config
├── 00 - Inbox/             # Raw, unprocessed observations
├── 01 - Fleeting/          # Quick thoughts, reminders, half-baked ideas
├── 02 - Literature/        # Source material (articles, docs, talks)
├── 03 - Agents/            # Agent profiles (Claude Code, Codex, Hermes, etc.)
├── 04 - Plugins/           # Plugin & extension documentation
├── 05 - Architecture/      # Architecture patterns (MCP, multi-agent, context engineering)
├── 06 - Use Cases/         # Real-world workflows, config snippets, integrations
├── 07 - Structure/         # MOCs, indexes, dashboards
├── 08 - Projects/          # Time-bound work
├── 09 - Trend Radar/       # Trend analysis
│   ├── Heating Up/         # Rapid growth signals
│   ├── Stable/             # Established patterns
│   └── Emerging/           # Early signals, watch list
├── 99 - Attachments/       # Images, PDFs, exported files
├── AGENTS.md               # This file
└── LICENSE
```

### Folder Roles

| Folder | Purpose | Retention |
|--------|---------|-----------|
| `00 - Inbox` | Drop zone for new signals. Agent triages here first. | Processed within a session |
| `01 - Fleeting` | Quick capture, reminders, half-formed ideas. | Promoted or archived |
| `02 - Literature` | Source material with attribution. | Permanently kept |
| `03 - Agents` | One note per agent. Installation, config, capabilities, quirks. | Updated as agents evolve |
| `04 - Plugins` | One note per plugin. Config, use-cases, compatibility. | Updated as plugins change |
| `05 - Architecture` | Pattern notes. MCP, context engineering, tool-calling, guardrails. | Evergreen |
| `06 - Use Cases` | Real-world workflows. How to combine tools, integrations, setups. | Evergreen |
| `07 - Structure` | Maps of Content organizing everything above. | Updated as vault grows |
| `08 - Projects` | Time-bound work (e.g., "evaluate Q4 agent landscape"). | Archived after completion |
| `99 - Attachments` | Binary assets, images, PDFs. | Linked from notes |

---

## Note Naming Convention

Atomic notes use a **timestamp prefix** for sortability and uniqueness:

```
YYYYMMDDHHMM - Descriptive title in sentence case.md
```

Examples:
- `202609201430 - Mixture of Experts architecture variants.md`
- `202609201445 - Llama 4 benchmark results vs GPT-5.md`
- `202609201500 - Anthropic constitutional AI method evolution.md`

**Why timestamp + sentence case?** Timestamps give chronological context and prevent filename collisions. Sentence case titles are readable and wiki-link friendly.

---

## Note Templates

### Atomic Note Template (Default)

```markdown
---
id: {{date:YYYYMMDDHHmm}}
created: {{date:YYYY-MM-DDTHH:mm:ss+02:00}}
tags:
  - trend
  - tool
aliases:
links:
---

# {{title}}

## Core Idea
[One sentence capturing the single idea]

## Details
[2–4 paragraphs: what it is, why it matters, key differentiators]

## Implications
[So what? What does this enable or change?]

## Related
- [[]]

## Sources
-
```

### Agent Profile Template (for `03 - Agents/`)

```markdown
---
id: {{date:YYYYMMDDHHmm}}
created: {{date:YYYY-MM-DDTHH:mm:ss+02:00}}
tags:
  - agent
aliases:
links:
---

# [Agent Name]

## Overview
[One paragraph: what this agent is, who made it, its positioning]

## Installation
```bash
# install command(s)
```

## Core Capabilities
- [Capability 1]
- [Capability 2]

## Configuration
```yaml
# key config snippet
```

## Key Plugins/Extensions
- [202609202000 - Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md)

## Strengths
-

## Weaknesses
-

## Use Cases
-

## Related Agents
- [202609200758 - OpenCode](./03%20-%20Agents/202609200758%20-%20OpenCode.md)

## Sources
- [Official Docs](url)
- [GitHub](url)
```

### Plugin Profile Template (for `04 - Plugins/`)

```markdown
---
id: {{date:YYYYMMDDHHmm}}
created: {{date:YYYY-MM-DDTHH:mm:ss+02:00}}
tags:
  - plugin
aliases:
links:
---

# [Plugin Name]

## Overview
[What it does, which agent(s) it supports]

## Installation
```bash
# install command
```

## Configuration
```yaml
# config snippet
```

## Use Cases
-

## Compatibility
- **Agent:** [202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)
- **Versions:** x.x.x+

## Related Plugins
- [202609200803 - Context7 MCP](./04%20-%20Plugins/202609200803%20-%20Context7%20MCP.md)

## Sources
- [GitHub](url)
- [Docs](url)
```

### Architecture Pattern Template (for `05 - Architecture/`)

```markdown
---
id: {{date:YYYYMMDDHHmm}}
created: {{date:YYYY-MM-DDTHH:mm:ss+02:00}}
tags:
  - architecture
aliases:
links:
---

# [Pattern Name]

## Core Idea
[One sentence on what this pattern is]

## How It Works
[Diagram description or flow]

## When to Use
-

## Tradeoffs
- **Pros:**
- **Cons:**

## Examples
- [202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)

## Related Patterns
- [202609202000 - MCP Proxy Aggregator Pattern](./05%20-%20Architecture/202609202000%20-%20MCP%20Proxy%20Aggregator%20Pattern.md)

## Sources
-
```

### Field Definitions

| Field | Purpose |
|-------|---------|
| `id` | Timestamp ID matching filename |
| `created` | ISO 8601 creation date |
| `tags` | Flat tag list — no hierarchy. Use kebab-case |
| `aliases` | Alternative titles Obsidian can match via `[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)` |
| `links` | Explicit list of strongly related permanent notes |
| `Core Idea` | The one-liner — if you can only read one sentence |
| `Details` | The meat — own words, blockquotes for source material |
| `Implications` | Forward-looking — why this matters |
| `Related` | Wikilinks to other permanent notes |
| `Sources` | Attribution when synthesizing external content |

---

## Tag Taxonomy (controlled vocabulary)

Use these tags consistently. Add new ones only when a theme recurs.

### Type Tags
- `trend` — a directional shift in the AI landscape
- `signal` — a data point that may indicate a trend
- `tool` — a software, library, or platform
- `paper` — academic research output
- `model` — a specific ML model
- `method` — a technique, algorithm, or approach
- `company` — organization-specific activity
- `person` — notable individual
- `event` — conference, announcement, milestone

### Status Tags
- `seedling` — new, underdeveloped note (fleeting → permanent transition)
- `evergreen` — mature, reviewed, stable
- `refactoring` — currently being restructured
- `deprecated` — superseded or no longer relevant (keep for traceability)

### Domain Tags
- `agent` — AI coding agents (Claude Code, Codex, Hermes, OpenCode, etc.)
- `plugin` — extensions and plugins for AI coding tools
- `config` — configuration, settings, setup guides
- `workflow` — use-case patterns, real-world applications
- `architecture` — agent architecture patterns, orchestration, MCP
- `cli` — command-line interface patterns, tools
- `tool` — a software, library, or platform (general)
- `mcp` — Model Context Protocol servers and integrations
- `tui` — terminal UI patterns and tools
- `gateway` — messaging platform integrations
- `vector-database` — vector DB integrations (Pinecone, Weaviate)
- `graph-database` — graph DB integrations (Neo4j)
- `data-warehouse` — analytics/warehouse integrations (Snowflake, BigQuery)
- `project-management` — PM tool integrations (Jira, Asana, Monday.com)
- `monitoring` — observability integrations (Sentry, Datadog)
- `browser` — browser automation plugins
- `search` — search engine integrations (Exa, Firecrawl)
- `devops` — DevOps/CI-CD integrations
- `containers` — container orchestration (Docker, Kubernetes)

---

## Map of Content (MOC) Rules

Structure notes in `04 - Structure/` organize permanent notes into thematic clusters.

### MOC Template

```markdown
---
tags:
  - moc
---

# MOC: [Theme Name]

## Overview
[2 sentences on what this map covers]

## Key Notes
- [202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md) — [one-line summary]
- [202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md) — [one-line summary]

## Clusters
### Sub-theme A
- [202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)
- [202609200758 - OpenCode](./03%20-%20Agents/202609200758%20-%20OpenCode.md)

### Sub-theme B
- [202609202000 - Cursor](./03%20-%20Agents/202609202000%20-%20Cursor.md)

## Open Questions
- What is the relationship between X and Y?

## Related MOCs
- [MOC-Trending-Agents](./07%20-%20Structure/MOC-Trending-Agents.md)
```

### MOC Maintenance

- Create a new MOC when a theme has **5+** related permanent notes
- MOCs should be updated when a new note joins their cluster
- Each permanent note should link to at least one MOC
- MOCs link to each other where themes intersect

---

## Agent Workflow

### When Adding New Knowledge

1. **Ingest** → Drop raw observation into `00 - Inbox/` with a timestamp-prefixed filename
2. **Triagate** → Determine if this is fleeting, literature, or permanent material
3. **Atomize** → Split compound ideas into separate notes (one idea each)
4. **Link** → Every new note must link to at least 2 existing notes (or note why it's an orphan)
5. **Tag** → Apply controlled vocabulary tags
6. **MOC update** → Add to relevant Map of Content if the theme exists; create new MOC if threshold reached
7. **Refactor** → After batch ingestion, revisit earlier notes to strengthen links, merge duplicates, or split oversized notes

### Wikilink Resolution (CRITICAL)

Sub-agents write notes with short-name wikilinks like `[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)` for readability. The merge step MUST resolve these to actual filenames before completing.

**Rules:**
- `[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)` must resolve to `[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)` (the actual file)
- `[202609202000 - Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md)` must resolve to `[202609202000 - Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md)`
- `[202609200758 - OpenCode](./03%20-%20Agents/202609200758%20-%20OpenCode.md)` must resolve to `[202609200758 - OpenCode](./03%20-%20Agents/202609200758%20-%20OpenCode.md)`
- Always search all folders to find the matching filename
- If no exact match exists, find the closest partial match
- If no match exists at all, link to the most relevant MOC

**Detailed wikilink resolution table:**

| Source Link | Resolution Logic | Target Link |
|-------------|------------------|-------------|
| `[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)` | Find file with "Claude Code" in name | `[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)` |
| `[202609202000 - Codex](./03%20-%20Agents/202609202000%20-%20Codex.md)` or `[202609202000 - Codex](./03%20-%20Agents/202609202000%20-%20Codex.md)` | Find file with "Codex" in name | `[202609202000 - Codex](./03%20-%20Agents/202609202000%20-%20Codex.md)` |
| `[202609200758 - OpenCode](./03%20-%20Agents/202609200758%20-%20OpenCode.md)` | Find file with "OpenCode" in name | `[202609200758 - OpenCode](./03%20-%20Agents/202609200758%20-%20OpenCode.md)` |
| `[202609200759 - Hermes Agent](./03%20-%20Agents/202609200759%20-%20Hermes%20Agent.md)` or `[202609200759 - Hermes Agent](./03%20-%20Agents/202609200759%20-%20Hermes%20Agent.md)` | Find file with "Hermes" in name | `[202609200759 - Hermes Agent](./03%20-%20Agents/202609200759%20-%20Hermes%20Agent.md)` |
| `[202609202000 - Cursor](./03%20-%20Agents/202609202000%20-%20Cursor.md)` | Find file with "Cursor" in name | `[202609202000 - Cursor](./03%20-%20Agents/202609202000%20-%20Cursor.md)` |
| `[202609202000 - Cline](./03%20-%20Agents/202609202000%20-%20Cline.md)` | Find file with "Cline" in name | `[202609202000 - Cline](./03%20-%20Agents/202609202000%20-%20Cline.md)` |
| `[202609202000 - Aider](./03%20-%20Agents/202609202000%20-%20Aider.md)` | Find file with "Aider" in name | `[202609202000 - Aider](./03%20-%20Agents/202609202000%20-%20Aider.md)` |
| `[202609200800 - Windsurf](./03%20-%20Agents/202609200800%20-%20Windsurf.md)` | Find file with "Windsurf" in name | `[202609200800 - Windsurf](./03%20-%20Agents/202609200800%20-%20Windsurf.md)` |
| `[202609202000 - Cursor](./03%20-%20Agents/202609202000%20-%20Cursor.md)` | Closest editor agent → Cursor | `[202609202000 - Cursor](./03%20-%20Agents/202609202000%20-%20Cursor.md)` |
| `[202609202001 - GitHub Copilot Agent](./03%20-%20Agents/202609202001%20-%20GitHub%20Copilot%20Agent.md)` | Find file with "Copilot" or "GitHub" | `[202609202001 - GitHub Copilot Agent](./03%20-%20Agents/202609202001%20-%20GitHub%20Copilot%20Agent.md)` |
| `[202609202002 - Gemini CLI](./03%20-%20Agents/202609202002%20-%20Gemini%20CLI.md)` | Find file with "Gemini" | `[202609202002 - Gemini CLI](./03%20-%20Agents/202609202002%20-%20Gemini%20CLI.md)` |
| `[202609202005 - JetBrains Junie](./03%20-%20Agents/202609202005%20-%20JetBrains%20Junie.md)` | Find file with "Junie" or "JetBrains" | `[202609202005 - JetBrains Junie](./03%20-%20Agents/202609202005%20-%20JetBrains%20Junie.md)` |
| `[2026092014 - Kilo Code](./03%20-%20Agents/2026092014%20-%20Kilo%20Code.md)` | Find file with "Kilo" | `[2026092014 - Kilo Code](./03%20-%20Agents/2026092014%20-%20Kilo%20Code.md)` |
| `[202609202004 - RooCode](./03%20-%20Agents/202609202004%20-%20RooCode.md)` | Find file with "Roo" | `[202609202004 - RooCode](./03%20-%20Agents/202609202004%20-%20RooCode.md)` |
| `[202609202004 - Pi](./03%20-%20Agents/202609202004%20-%20Pi.md)` | Pi agent not yet created → link to MOC | `[MOC-Trending-Agents](./07%20-%20Structure/MOC-Trending-Agents.md)` |
| `[202609202000 - Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md)` | Find file with "Browser Use" | `[202609202000 - Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md)` |
| `[202609202000 - Firecrawl MCP Server](./04%20-%20Plugins/202609202000%20-%20Firecrawl%20MCP%20Server.md)` | Find file with "Firecrawl MCP" | `[202609202000 - Firecrawl MCP Server](./04%20-%20Plugins/202609202000%20-%20Firecrawl%20MCP%20Server.md)` |
| `[202609200803 - Context7 MCP](./04%20-%20Plugins/202609200803%20-%20Context7%20MCP.md)` | Find file with "Context7" | `[202609200803 - Context7 MCP](./04%20-%20Plugins/202609200803%20-%20Context7%20MCP.md)` |
| `[202609200804 - FAL MCP Server](./04%20-%20Plugins/202609200804%20-%20FAL%20MCP%20Server.md)` | Find file with "FAL MCP" | `[202609200804 - FAL MCP Server](./04%20-%20Plugins/202609200804%20-%20FAL%20MCP%20Server.md)` |
| `[202609200805 - Hermes Kanban Dashboard](./04%20-%20Plugins/202609200805%20-%20Hermes%20Kanban%20Dashboard.md)` | Find file with "Kanban" | `[202609200805 - Hermes Kanban Dashboard](./04%20-%20Plugins/202609200805%20-%20Hermes%20Kanban%20Dashboard.md)` |
| `[202609200806 - Hermes Curator](./04%20-%20Plugins/202609200806%20-%20Hermes%20Curator.md)` | Find file with "Curator" | `[202609200806 - Hermes Curator](./04%20-%20Plugins/202609200806%20-%20Hermes%20Curator.md)` |
| `[202609202000 - Jev Agent Router](./04%20-%20Plugins/202609202000%20-%20Jev%20Agent%20Router.md)` | Find file with "Jev" | `[202609202000 - Jev Agent Router](./04%20-%20Plugins/202609202000%20-%20Jev%20Agent%20Router.md)` |
| `[202609202010 - Playwright MCP](./04%20-%20Plugins/202609202010%20-%20Playwright%20MCP.md)` | Find file with "Playwright" | `[202609202010 - Playwright MCP](./04%20-%20Plugins/202609202010%20-%20Playwright%20MCP.md)` |
| `[202609202011 - Chrome DevTools MCP](./04%20-%20Plugins/202609202011%20-%20Chrome%20DevTools%20MCP.md)` | Find file with "Chrome DevTools" | `[202609202011 - Chrome DevTools MCP](./04%20-%20Plugins/202609202011%20-%20Chrome%20DevTools%20MCP.md)` |
| `[202609202000 - OpenCode Firecrawl](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Firecrawl.md)` | Find file with "OpenCode Firecrawl" | `[202609202000 - OpenCode Firecrawl](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Firecrawl.md)` |
| `[202609202000 - OpenCode Supermemory](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Supermemory.md)` | Find file with "Supermemory" | `[202609202000 - OpenCode Supermemory](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Supermemory.md)` |
| `[202609202000 - OpenCode Firecrawl](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Firecrawl.md)` | Closest OpenCode plugin | `[202609202000 - OpenCode Firecrawl](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Firecrawl.md)` |
| `[202609202000 - OpenCode Firecrawl](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Firecrawl.md)` | Closest OpenCode plugin | `[202609202000 - OpenCode Firecrawl](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Firecrawl.md)` |
| `[202609200805 - Hermes Kanban Dashboard](./04%20-%20Plugins/202609200805%20-%20Hermes%20Kanban%20Dashboard.md)` | Closest Hermes plugin | `[202609200805 - Hermes Kanban Dashboard](./04%20-%20Plugins/202609200805%20-%20Hermes%20Kanban%20Dashboard.md)` |
| `[202609200805 - Hermes Kanban Dashboard](./04%20-%20Plugins/202609200805%20-%20Hermes%20Kanban%20Dashboard.md)` | Closest memory/dashboard plugin | `[202609200805 - Hermes Kanban Dashboard](./04%20-%20Plugins/202609200805%20-%20Hermes%20Kanban%20Dashboard.md)` |
| `[202609202000 - Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md)` | Closest browser MCP | `[202609202000 - Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md)` |
| `[202609202011 - Chrome DevTools MCP](./04%20-%20Plugins/202609202011%20-%20Chrome%20DevTools%20MCP.md)` | Closest devtools MCP | `[202609202011 - Chrome DevTools MCP](./04%20-%20Plugins/202609202011%20-%20Chrome%20DevTools%20MCP.md)` |
| `[202609202000 - Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md)` | Closest browser MCP | `[202609202000 - Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md)` |
| `[202609202000 - MCP Proxy Aggregator Pattern](./05%20-%20Architecture/202609202000%20-%20MCP%20Proxy%20Aggregator%20Pattern.md)` | Find file with "Proxy Aggregator" | `[202609202000 - MCP Proxy Aggregator Pattern](./05%20-%20Architecture/202609202000%20-%20MCP%20Proxy%20Aggregator%20Pattern.md)` |
| `[202609202001 - Context Engineering for Long-Horizon Agents](./05%20-%20Architecture/202609202001%20-%20Context%20Engineering%20for%20Long-Horizon%20Agents.md)` | Find file with "Context Engineering" | `[202609202001 - Context Engineering for Long-Horizon Agents](./05%20-%20Architecture/202609202001%20-%20Context%20Engineering%20for%20Long-Horizon%20Agents.md)` |
| `[202609202002 - Multi-Agent Orchestration with Guardrail Layering](./05%20-%20Architecture/202609202002%20-%20Multi-Agent%20Orchestration%20with%20Guardrail%20Layering.md)` | Find file with "Multi-Agent Orchestration" | `[202609202002 - Multi-Agent Orchestration with Guardrail Layering](./05%20-%20Architecture/202609202002%20-%20Multi-Agent%20Orchestration%20with%20Guardrail%20Layering.md)` |
| `[202609202003 - MCP Apps Interactive UI Protocol](./05%20-%20Architecture/202609202003%20-%20MCP%20Apps%20Interactive%20UI%20Protocol.md)` | Find file with "Interactive UI" | `[202609202003 - MCP Apps Interactive UI Protocol](./05%20-%20Architecture/202609202003%20-%20MCP%20Apps%20Interactive%20UI%20Protocol.md)` |
| `[202609202004 - Layered Protocol Stack MCP A2A Streamable HTTP](./05%20-%20Architecture/202609202004%20-%20Layered%20Protocol%20Stack%20MCP%20A2A%20Streamable%20HTTP.md)` | Find file with "Layered Protocol" | `[202609202004 - Layered Protocol Stack MCP A2A Streamable HTTP](./05%20-%20Architecture/202609202004%20-%20Layered%20Protocol%20Stack%20MCP%20A2A%20Streamable%20HTTP.md)` |
| `[202609202005 - Agent Portability via Agent Client Protocol](./05%20-%20Architecture/202609202005%20-%20Agent%20Portability%20via%20Agent%20Client%20Protocol.md)` | Find file with "Agent Portability" | `[202609202005 - Agent Portability via Agent Client Protocol](./05%20-%20Architecture/202609202005%20-%20Agent%20Portability%20via%20Agent%20Client%20Protocol.md)` |
| `[202609202020 - Orchestrator-Worker Delegation Pattern](./05%20-%20Architecture/202609202020%20-%20Orchestrator-Worker%20Delegation%20Pattern.md)` | Find file with "Orchestrator" | `[202609202020 - Orchestrator-Worker Delegation Pattern](./05%20-%20Architecture/202609202020%20-%20Orchestrator-Worker%20Delegation%20Pattern.md)` |
| `[202609202021 - Context Compaction and Structured Note-Taking](./05%20-%20Architecture/202609202021%20-%20Context%20Compaction%20and%20Structured%20Note-Taking.md)` | Find file with "Context Compaction" | `[202609202021 - Context Compaction and Structured Note-Taking](./05%20-%20Architecture/202609202021%20-%20Context%20Compaction%20and%20Structured%20Note-Taking.md)` |
| `[202609202022 - MCP Hybrid Client-Server Architecture](./05%20-%20Architecture/202609202022%20-%20MCP%20Hybrid%20Client-Server%20Architecture.md)` | Find file with "Hybrid Client-Server" | `[202609202022 - MCP Hybrid Client-Server Architecture](./05%20-%20Architecture/202609202022%20-%20MCP%20Hybrid%20Client-Server%20Architecture.md)` |
| `[202609202001 - Claude Code Hooks for CI-CD Automation](./06%20-%20Use%20Cases/202609202001%20-%20Claude%20Code%20Hooks%20for%20CI-CD%20Automation.md)` | Find file with "CI/CD" | `[202609202001 - Claude Code Hooks for CI-CD Automation](./06%20-%20Use%20Cases/202609202001%20-%20Claude%20Code%20Hooks%20for%20CI-CD%20Automation.md)` |
| `[202609202000 - Claude Code Plugin Distribution for Team Workflow Standardization](./06%20-%20Use%20Cases/202609202000%20-%20Claude%20Code%20Plugin%20Distribution%20for%20Team%20Workflow%20Standardization.md)` | Find file with "Plugin Distribution" | `[202609202000 - Claude Code Plugin Distribution for Team Workflow Standardization](./06%20-%20Use%20Cases/202609202000%20-%20Claude%20Code%20Plugin%20Distribution%20for%20Team%20Workflow%20Standardization.md)` |
| `[202609202002 - Multi-Server MCP Orchestration for Cross-Tool Workflows](./06%20-%20Use%20Cases/202609202002%20-%20Multi-Server%20MCP%20Orchestration%20for%20Cross-Tool%20Workflows.md)` | Find file with "Multi-Server MCP" | `[202609202002 - Multi-Server MCP Orchestration for Cross-Tool Workflows](./06%20-%20Use%20Cases/202609202002%20-%20Multi-Server%20MCP%20Orchestration%20for%20Cross-Tool%20Workflows.md)` |
| `[202609200758 - OpenCode](./03%20-%20Agents/202609200758%20-%20OpenCode.md)` | Wrong timestamp → actual file | `[202609200758 - OpenCode](./03%20-%20Agents/202609200758%20-%20OpenCode.md)` |
| `[202609200759 - Hermes Agent](./03%20-%20Agents/202609200759%20-%20Hermes%20Agent.md)` | Wrong timestamp → actual file | `[202609200759 - Hermes Agent](./03%20-%20Agents/202609200759%20-%20Hermes%20Agent.md)` |

**Important:** Wikilinks with wrong timestamps should resolve to the actual file. Check all folders systematically.

**Process:**
1. Use `search_files(pattern="\\[\\[.*\\]\\]", ...)` to find all wikilinks
2. For each `[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)` find the actual file using the table above as reference
3. Apply fix with `patch(path=..., old_string="[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)", new_string="[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)")`
4. Repeat until zero orphans remain

### Refactoring Rules

Refactoring is expected. When restructuring:

- **Never delete content** — split into new notes or move to `01 - Fleeting/` if it loses relevance
- **Preserve wikilinks** — if a filename changes, update all `[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)` across the vault
- **Update MOCs** — rename or re-point any MOC references to moved notes
- **Leave traces** — if a note is superseded, add a `replaced-by: [202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)` frontmatter field

### When to Create vs Link

| Situation | Action |
|-----------|--------|
| New concept, no existing note | Create new atomic note |
| Related to 1–2 existing notes | Link to them |
| Related to 5+ notes | Create/update a MOC |
| Repeats existing note | Merge — add new info to existing, delete duplicate |
| Part of a larger trend | Link to the trend note + add trend as tag |
| A correction to existing note | Edit the note, add update timestamp in frontmatter |

---

## Obsidian Configuration

The `.obsidian/` directory should contain:

```json
// .obsidian/app.json
{
  "alwaysUpdateLinks": true,
  "newLinkMode": "relative",
  "useMarkdownLinks": false,
  "attachmentFolderPath": "99 - Attachments",
  "newFileLocation": "folder",
  "newFileFolderPath": "00 - Inbox"
}
```

```json
// .obsidian/templates/core.json
{
  "templateFolderPath": ".obsidian/templates"
}
```

---

## Output Expectations

When the agent produces work in this vault:

1. **All notes are atomic** — no note exceeds what one idea needs
2. **Every note is linked** — minimum 2 outbound links for permanent notes
3. **Frontmatter is complete** — id, created, tags, links all populated
4. **Sources are attributed** — blockquotes + links for any external material
5. **MOCs are current** — no orphan notes in clusters of 5+
6. **Timestamps are accurate** — creation dates reflect when the note was written, not the source date



## Trend Scoring and README Tables

The cron job MUST maintain comprehensive scored trend tables in README.md:

### Required README Tables
1. **🚀 Trending Agents** - Top 5 scored agents
2. **🔌 Top Plugins & Extensions** - Top 5 scored plugins
3. **📊 Trend Radar** - Three sub-tables:
   - 🔥 Heating Up (score >= 50)
   - 📈 Stable (score 20-49)
   - 🌱 Emerging (score < 20)

### Table Format
Each table MUST use this exact format:
```
| # | Name | Score | Type | Stars | Status |
|---|------|-------|------|-------|--------|
| 1 | [Title](./path) | 130 | agent | 50k+ | Heating Up |
```

### Scoring Algorithm
Items are scored based on:
- GitHub stars (1 point per 1000 stars, max 50)
- Mention frequency (5 points per mention)
- Tag bonuses (cli=+10, mcp=+15, trending=+20)
- Source quality (HN/Reddit mentions score higher)

### Scripts for Trend Management
- `scripts/aggregate-trends.py` - Scores all items
- `scripts/update_readme.py` - Updates README tables with scored data




## Daily Scan Scripts (CRITICAL)

The cron job runs in **8 stages**:

### Stage 1: Research (20:00)
`stage-1-research.py` — Creates new agent and plugin notes from hardcoded lists (no web search, no delegate_task).

### Stage 2: Link Resolution (20:30)
`stage-2-links.py` — Fixes links after research completes:
1. `resolve_wikilinks.py` — Resolves remaining short-name wikilinks
2. `fix-all-links.py` — Comprehensive link fixing (dedup + resolve + create missing; emits markdown links)
3. `verify-vault.py` — Verifies all links resolve

### Stage 3: Scoring (20:45)
`stage-3-scoring.py` — Aggregates trend scores:
1. `aggregate-trends.py` — Scores items based on stars/mentions/tags
2. `collect_agent_plugins.py` — Builds per-agent plugin tables

### Stage 4: Indexes & Commit (21:00)
`stage-4-indexes.py` — Updates all indexes and pushes:
1. `update-mocs.py` — Updates Maps of Content (idempotent, deduplicated)
2. `update-plugin-master-index.py` — Generates Plugin Master Index (deduplicated)
3. `update-agent-master-index.py` — Generates Agent Master Index (deduplicated)
4. `update_readme.py` — Updates README tables
5. `fix-master-index-links.py` — Fixes Master Index frontmatter links (markdown, file-relative)
6. `fix-links-relative.py` — Rewrites any vault-root-style link to file-relative (safety net)
7. `verify-vault.py` — Final verification
8. `git add -A && git commit && git push`

**NEVER skip any script. NEVER change the order. NEVER delete files.**

### Script Details

| Script | Purpose | Output |
|--------|---------|--------|
| fix_all_links.py | Fixes frontmatter + body wikilinks | Fixed files |
| aggregate-trends.py | Scores all items | trend-data.json |
| collect_agent_plugins.py | Builds per-agent plugin tables | Updated README |
| update_readme.py | Updates Trend Radar tables | Updated README |
| verify-vault.py | Verifies all links work | Console output |


## Frontmatter Links Requirement (CRITICAL)

Every note's frontmatter MUST contain at least 2 links in the `links:` field,
in standard Markdown format with FILE-RELATIVE paths:

```markdown
---
id: 2026092010
created: 2026-09-20T10:00:00+02:00
tags:
  - agent
  - cli
links:
  - "[Gemini CLI](../03%20-%20Agents/202609202002%20-%20Gemini%20CLI.md)"
---
```

(The example above is for a note in `04 - Plugins/`. From a note in the same
folder, the path would be `202609202002%20-%20Gemini%20CLI.md` with no `../`.)

**Sub-Agent Rules:**
- **ALWAYS USE FULL FILENAMES** — `202609202000 - Claude Code`, never short names
- **ALWAYS CHECK FOR EXISTING FILES FIRST** — use `search_files` before writing
- **ALWAYS ADD `links:` FIELD TO FRONTMATTER** — with 2+ markdown links (file-relative)
- **NEVER CREATE DUPLICATES** — if a note exists, `patch()` it instead of writing new

**How agents avoid broken links:**
1. Before writing: `search_files(pattern="*", target="files", path="03 - Agents")` to see what exists
2. Use full filenames for ALL links — both in frontmatter `links:` and body `## Related`
3. Links are file-relative: from a note in a subfolder, prefix `../` to reach another folder
4. Verify target files exist before linking to them

The vault is a living system. Small, frequent, well-linked notes beat large, infrequent ones. Refactoring is growth.

---

## Wikilink vs Markdown Link Rules

**All links everywhere are standard Markdown** `[title](path)` — never `[[wikilinks]]`.

**Link paths are FILE-RELATIVE (GitHub behavior):** a link resolves relative to the
directory of the file containing it, NOT the vault root. This is how GitHub renders
links, and the CI pipeline validates links the same way.

Examples:
- From `04 - Plugins/2026092023 - CodeGraph MCP.md` to an agent note:
  `[Claude Code](../03%20-%20Agents/202609202000%20-%20Claude%20Code.md)`
- Between notes in the same folder:
  `[Browser Use MCP](202609202000%20-%20Browser%20Use%20MCP.md)`
- From `README.md` (vault root) into a folder:
  `[Claude Code](03%20-%20Agents/202609202000%20-%20Claude%20Code.md)`

**Rules:**
1. `%20`-encode spaces in link paths.
2. Always verify the target file exists before linking. If the file doesn't exist, either create it or link to an existing note.
3. If you write or see a link with a vault-root-style path (`./03 - Agents/...`) inside a note that lives in a subfolder, run `python3 scripts/ci/fix-links-relative.py` to rewrite it correctly.

**Auto-fix:** `scripts/ci/fix-links-relative.py` rewrites any link that resolves
against the vault root but not against the containing file's directory. It is
idempotent and safe to run any time.

---

### Trend Radar (in README.md and `09 - Trend Radar/`)

The Trend Radar is the vault's analysis of where AI coding agent trends are heading. It has three categories, each with its own folder:

**Heating Up 🔥** (`09 - Trend Radar/Heating Up/`) — Recent, rapid growth:
- New tools/plugins with >5k GitHub stars/week
- HN front page or Reddit r/LocalLMAI top posts
- New architecture patterns gaining adoption
- Major player releases (Claude Code, OpenAI Codex)

**Stable 📈** (`09 - Trend Radar/Stable/`) — Established patterns:
- Tool-calling as standard interface
- RAG + context compression
- IDE integrations
- MCP as universal protocol
- Containerized agent sandboxes

**Emerging 🌱** (`09 - Trend Radar/Emerging/`) — Early signals:
- Agent-to-agent communication (A2A, ACP)
- Verifiable execution
- Federated agent networks
- Personal memory systems
- Interactive UI protocols (MCP Apps)

**Maintenance rules:**
1. Always analyze new findings from all 4 streams
2. Move items between categories based on evidence
3. Add new items with citations from research
4. Remove outdated items
5. Use `patch()` to update README.md
6. Create atomic notes in the appropriate Trend Radar folder for each new trend signal

---

## 🔌 Plugins & Extensions (Critical Section)

Modern AI plugins and extensions are documented in `04 - Plugins/`. This vault tracks:

### Categories
- **Trending**: Rapid growth, high community adoption (Browser Use, Firecrawl, Context7)
- **Stable**: Established patterns, steady adoption (Jev, Hermes Kanban, MCP servers)
- **Emerging**: Early signals, watch list (Oh-My-Openagent, Auto Permission)

### Master Indexes
**All plugins are indexed in:** `04 - Plugins/00 - Plugin Master Index.md`
**All agents are indexed in:** `03 - Agents/00 - Agent Master Index.md`

### Compatibility Detection Rules
The `update-plugin-master-index.py` script detects compatibility via:
1. Frontmatter `agents:` field — uses agent keys (e.g., `hermes`, `claude-code`, `opencode`)
2. `**Agent:**` line in Compatibility section — uses wikilinks (e.g., `[202609200759 - Hermes Agent](./03%20-%20Agents/202609200759%20-%20Hermes%20Agent.md)`)
3. Body text scanning — matches agent names mentioned in notes
4. MCP-compatible detection — plugins tagged `mcp` with "any MCP-compatible" text work with ALL MCP agents (Claude Code, OpenCode, Hermes, Cursor, Codex, Windsurf, Aider, Gemini CLI, GitHub Copilot, Kilo Code, RooCode, JetBrains Junie)

### Maintenance rules:
1. Add new plugins to both `04 - Plugins/` and the master index
2. Categorize by trending/stable/emerging based on adoption data
3. Link to supported agents (Claude Code, OpenCode, Hermes, Cursor, Codex)
4. Update the comparison table when new plugins are added
5. Track plugin growth in Trend Radar

---

## Architecture Patterns (Critical Section)

Modern AI architecture patterns are documented in `05 - Architecture/`. This vault tracks:

### Core Patterns
- **Single-Agent**: CLI agents with tool loops
- **Multi-Agent**: Orchestrator-worker, peer-to-peer, hierarchical
- **MCP Server**: Universal tool/resource interface
- **Context Engineering**: Jev system, compaction, RAG

### Emerging Patterns
- MCP Proxy Aggregator
- MCP Apps Interactive UI
- Agent Portability (ACP)
- Verifiable Execution
- Federated Agent Networks

### Master Index
**All architecture patterns are indexed in:** `05 - Architecture/00 - AI Architecture Master Index.md`

**Maintenance rules:**
1. Add new patterns to both `05 - Architecture/` and the master index
2. Update the comparison table when adoption levels change
3. Link to related agents/plugins/MOCs
4. Track emerging patterns in Trend Radar




## File Deletion Prevention (CRITICAL)

**NEVER DELETE FILES.** No agent, sub-agent, or script should ever delete a `.md` note file.

**Rules:**
1. If a note already exists for a topic, UPDATE it (use `patch()`) instead of creating a duplicate
2. If a note has a duplicate timestamp, rename one (e.g., `2026092010` → `2026092015`) instead of deleting
3. Scripts should NEVER contain `os.remove()`, `subprocess.run(['rm', ...])`, or any file deletion commands
4. Sub-agents should NEVER be instructed to "remove", "delete", "clean up", or "deduplicate" files
5. The only exception is manifest files in `08 - Projects/scan-manifests/` which can be cleaned up after processing

**If a sub-agent reports a duplicate:**
- Rename one file to use a different timestamp
- Merge content if appropriate
- NEVER delete either file

## Link Verification Rules

Every note must have at least 2 working outbound links. No exceptions.

**Definition of "working link":**
- `[wikilink](./00%20-%20Inbox/202609202033%20-%20wikilink.md)` points to a file that actually exists in the vault
- `[markdown link](url)` points to a valid relative path

**How to verify:**
1. Read note content
2. Extract all `[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)` links
3. For each link, search filesystem for matching file
4. If match not found, resolve to actual filename using partial matching
5. Apply fix with `patch()`

**README-specific:**
1. All links must be Markdown format (not wikilinks)
2. All links must point to existing files
3. No duplicate entries (timestamped version takes precedence over short-name)

---

## Link Verification Using Obsidian Skill

The Obsidian skill is Hermes's filesystem vault tool. There's no standalone Obsidian CLI — the agent uses `search_files`, `read_file`, and `patch()` to verify and fix links.

**How the merge agent identifies orphans:**

1. **Extract all wikilinks** from every note:
   ```
   search_files(pattern="\\[\\[.*\\]\\]", target="content", path="03 - Agents", file_glob="*.md")
   search_files(pattern="\\[\\[.*\\]\\]", target="content", path="04 - Plugins", file_glob="*.md")
   search_files(pattern="\\[\\[.*\\]\\]", target="content", path="05 - Architecture", file_glob="*.md")
   search_files(pattern="\\[\\[.*\\]\\]", target="content", path="06 - Use Cases", file_glob="*.md")
   ```

2. **Build a file map** by walking all vault folders and noting every `.md` filename

3. **Cross-reference** each `[wikilink](./00%20-%20Inbox/202609202033%20-%20wikilink.md)` against the file map:
   - Direct match: `[202609200758 - OpenCode](./03%20-%20Agents/202609200758%20-%20OpenCode.md)` matches `03 - Agents/202609200758 - OpenCode.md`
   - Short-name match: `[202609200758 - OpenCode](./03%20-%20Agents/202609200758%20-%20OpenCode.md)` partially matches → resolve to actual filename
   - No match: orphan → fix with `patch()` or replace with closest existing file

4. **Fix orphans** using `patch()`:
   ```
   patch(path="04 - Plugins/202609202000 - Firecrawl MCP Server.md",
         old_string="[202609202000 - OpenCode Firecrawl](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Firecrawl.md)",
         new_string="[202609202000 - OpenCode Firecrawl](./04%20-%20Plugins/202609202000%20-%20OpenCode%20Firecrawl.md)")
   ```

5. **Repeat** until zero orphans remain.

**Why this works:**
- `search_files` extracts every wikilink from the DOM/text
- The agent reads each note's content and compares against filesystem
- `patch()` updates links without overwriting existing content
- The Obsidian skill's wikilink convention (`[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)`) is preserved for Obsidian vault navigation

---

## Required Skills & Tools

**Skills:**
- `skill_view(name="obsidian")` — vault operations, wikilink conventions, read/write/append

**Research tools (Firecrawl enabled in this profile):**
- `web_search(query)` — search for trending tools, plugins, patterns
- `web_extract([urls])` — scrape content from specific pages for detailed info

**File operations:**
- `search_files(pattern, target, path)` — find files or content
- `read_file(path)` — read before editing
- `write_file(path, content)` — create new files (notes, manifests)
- `patch(path, old_string, new_string)` — edit existing files
- `terminal(command)` — git operations, cleanup

---

## Cron Jobs

The daily scan runs as **4 separate cron jobs** (stages), each running after the previous completes:

| Time | Job | Script | What it does |
|------|-----|--------|--------------|
| 20:00 | Trends Stage 1 - Research | `stage-1-research.py` | Creates agent/plugin notes from hardcoded lists |
| 20:30 | Trends Stage 2 - Links | `stage-2-links.py` | Resolves wikilinks, fixes broken links |
| 20:45 | Trends Stage 3 - Scoring | `stage-3-scoring.py` | Aggregates trend scores, collects agent plugins |
| 21:00 | Trends Stage 4 - Indexes | `stage-4-indexes.py` | Updates MOCs, Master Indexes, README, commits |

Setup: `bash scripts/setup-cron.sh` (run once after cloning)

### Stage 1: Research (20:00)
`stage-1-research.py` — Creates new agent and plugin notes from hardcoded lists (no web search, no delegate_task).

### Stage 2: Link Resolution
1. `resolve_wikilinks.py` — Resolves short-name wikilinks to full filenames
2. `fix_all_links.py` — Fixes broken wikilinks
3. `verify-vault.py` — Verifies all links resolve

### Stage 3: Scoring
1. `aggregate-trends.py` — Scores items based on stars/mentions/tags
2. `collect_agent_plugins.py` — Builds per-agent plugin tables

### Stage 4: Indexes & Commit
1. `update-mocs.py` — Updates Maps of Content
2. `update-plugin-master-index.py` — Generates Plugin Master Index
3. `update-agent-master-index.py` — Generates Agent Master Index
4. `update_readme.py` — Updates README tables
5. `fix-master-index-links.py` — Fixes Master Index frontmatter links
6. `verify-vault.py` — Final verification
7. `git add -A && git commit && git push`

**NEVER skip any script. NEVER change the order. NEVER delete files.**

---

## Parallel Execution (Future Work)

The current pipeline runs stages sequentially. The following describes the **target architecture** for parallel research via `delegate_task` — not yet implemented.

### What Can Be Parallelized
Each of these is independent and can run as a separate sub-agent:

| Stream | Research Focus |
|--------|----------------|
| **Stream A: Agent Profiles** | Search for trending AI coding agents — new releases, GitHub stars, community buzz |
| **Stream B: Plugin Ecosystem** | Scan plugin/extension updates across Hermes, Claude Code, OpenCode, Codex |
| **Stream C: Architecture Patterns** | Discover new patterns — MCP servers, multi-agent orchestration, context engineering |
| **Stream D: Use Cases** | Find real-world workflows, config snippets, integration tutorials |

### Parallel Workflow (Target)

```
┌─────────────────────────────────────────────────────────┐
│  Cron Job Trigger (daily 20:00)                         │
│  Reads vault state, identifies gaps                     │
└───────────────────────┬─────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
   Stream A        Stream B        Stream C
   Agents          Plugins         Architecture
        │               │               │
        └───────────────┼───────────────┘
                        ▼
              ┌─────────────────┐
              │  Merge Results  │
              │  Deduplicate    │
              │  Update MOCs    │
              │  Update README  │
              │  Commit & Push  │
              └─────────────────┘
```

### Sub-Agent Task Spec (Target)

Each parallel sub-agent receives:
- A **specific research question** (e.g., "Find 3 trending AI agents released this week")
- A **target folder** to write notes into
- A **template reference** for note structure
- A **max tool call limit** (keep bounded)

### Post-Parallel Merge (Target)

After all sub-agents complete:
1. **Deduplicate** — merge notes on the same topic
2. **Cross-link** — connect notes across streams
3. **Update MOCs** — add new notes to relevant Maps of Content
4. **Refresh README** — update trend tables, radar, and links
5. **Commit** — single atomic commit with all new content
