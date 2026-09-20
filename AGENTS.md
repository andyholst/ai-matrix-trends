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
- [[link-to-plugin]]

## Strengths
-

## Weaknesses
-

## Use Cases
- 

## Related Agents
- [[link-to-comparable-agent]]

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
- **Agent:** [[agent-name]]
- **Versions:** x.x.x+

## Related Plugins
- [[link-to-related-plugin]]

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
- [[agent-that-uses-this]]

## Related Patterns
- [[link-to-related-pattern]]

## Sources
-
```

### Field Definitions

| Field | Purpose |
|-------|---------|
| `id` | Timestamp ID matching filename |
| `created` | ISO 8601 creation date |
| `tags` | Flat tag list — no hierarchy. Use kebab-case |
| `aliases` | Alternative titles Obsidian can match via `[[wikilinks]]` |
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
- [[YYYYMMDDHHMM - Note title]] — [one-line summary]
- [[YYYYMMDDHHMM - Note title]] — [one-line summary]

## Clusters
### Sub-theme A
- [[note-link-1]]
- [[note-link-2]]

### Sub-theme B
- [[note-link-3]]

## Open Questions
- What is the relationship between X and Y?

## Related MOCs
- [[MOC: Related theme]]
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

Sub-agents write notes with short-name wikilinks like `[[Claude Code]]` for readability. The merge step MUST resolve these to actual filenames before completing.

**Rules:**
- `[[Claude Code]]` must resolve to `[[202609202000 - Claude Code]]` (the actual file)
- `[[Browser Use MCP]]` must resolve to `[[202609202000 - Browser Use MCP]]`
- `[[OpenCode]]` must resolve to `[[202609200758 - OpenCode]]`
- Always search all folders to find the matching filename
- If no exact match exists, find the closest partial match
- If no match exists at all, link to the most relevant MOC

**Detailed wikilink resolution table:**

| Source Link | Resolution Logic | Target Link |
|-------------|------------------|-------------|
| `[[Claude Code]]` | Find file with "Claude Code" in name | `[[202609202000 - Claude Code]]` |
| `[[Codex]]` or `[[OpenAI Codex]]` | Find file with "Codex" in name | `[[202609202000 - Codex]]` |
| `[[OpenCode]]` | Find file with "OpenCode" in name | `[[202609200758 - OpenCode]]` |
| `[[Hermes]]` or `[[Hermes Agent]]` | Find file with "Hermes" in name | `[[202609200759 - Hermes Agent]]` |
| `[[Cursor]]` | Find file with "Cursor" in name | `[[202609202000 - Cursor]]` |
| `[[Cline]]` | Find file with "Cline" in name | `[[202609202000 - Cline]]` |
| `[[Aider]]` | Find file with "Aider" in name | `[[202609202000 - Aider]]` |
| `[[Windsurf]]` | Find file with "Windsurf" in name | `[[202609200800 - Windsurf]]` |
| `[[VS Code]]` | Closest editor agent → Cursor | `[[202609202000 - Cursor]]` |
| `[[GitHub Copilot]]` | Find file with "Copilot" or "GitHub" | `[[202609202001 - GitHub Copilot Agent]]` |
| `[[Gemini CLI]]` | Find file with "Gemini" | `[[202609202002 - Gemini CLI]]` |
| `[[JetBrains Junie]]` | Find file with "Junie" or "JetBrains" | `[[202609202005 - JetBrains Junie]]` |
| `[[Kilo Code]]` | Find file with "Kilo" | `[[202609202003 - Kilo Code]]` |
| `[[RooCode]]` | Find file with "Roo" | `[[202609202004 - RooCode]]` |
| `[[Pi]]` | Pi agent not yet created → link to MOC | `[[MOC-Trending-Agents]]` |
| `[[Browser Use MCP]]` | Find file with "Browser Use" | `[[202609202000 - Browser Use MCP]]` |
| `[[Firecrawl MCP Server]]` | Find file with "Firecrawl MCP" | `[[202609202000 - Firecrawl MCP Server]]` |
| `[[Context7 MCP]]` | Find file with "Context7" | `[[202609200803 - Context7 MCP]]` |
| `[[FAL MCP Server]]` | Find file with "FAL MCP" | `[[202609200804 - FAL MCP Server]]` |
| `[[Hermes Kanban Dashboard]]` | Find file with "Kanban" | `[[202609200805 - Hermes Kanban Dashboard]]` |
| `[[Hermes Curator]]` | Find file with "Curator" | `[[202609200806 - Hermes Curator]]` |
| `[[Jev Agent Router]]` | Find file with "Jev" | `[[202609202000 - Jev Agent Router]]` |
| `[[Playwright MCP]]` | Find file with "Playwright" | `[[202609202010 - Playwright MCP]]` |
| `[[Chrome DevTools MCP]]` | Find file with "Chrome DevTools" | `[[202609202011 - Chrome DevTools MCP]]` |
| `[[OpenCode Firecrawl]]` | Find file with "OpenCode Firecrawl" | `[[202609202000 - OpenCode Firecrawl]]` |
| `[[OpenCode Supermemory]]` | Find file with "Supermemory" | `[[202609202000 - OpenCode Supermemory]]` |
| `[[opencode-tavily]]` | Closest OpenCode plugin | `[[202609202000 - OpenCode Firecrawl]]` |
| `[[opencode-websearch-cited]]` | Closest OpenCode plugin | `[[202609202000 - OpenCode Firecrawl]]` |
| `[[hermes-memory-wiki]]` | Closest Hermes plugin | `[[202609200805 - Hermes Kanban Dashboard]]` |
| `[[mnemosyne-dashboard]]` | Closest memory/dashboard plugin | `[[202609200805 - Hermes Kanban Dashboard]]` |
| `[[mcp-browser-use]]` | Closest browser MCP | `[[202609202000 - Browser Use MCP]]` |
| `[[chrome-devtools-mcp]]` | Closest devtools MCP | `[[202609202011 - Chrome DevTools MCP]]` |
| `[[safari-mcp]]` | Closest browser MCP | `[[202609202000 - Browser Use MCP]]` |
| `[[MCP Proxy Aggregator Pattern]]` | Find file with "Proxy Aggregator" | `[[202609202000 - MCP Proxy Aggregator Pattern]]` |
| `[[Context Engineering for Long-Horizon Agents]]` | Find file with "Context Engineering" | `[[202609202001 - Context Engineering for Long-Horizon Agents]]` |
| `[[Multi-Agent Orchestration with Guardrail Layering]]` | Find file with "Multi-Agent Orchestration" | `[[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]` |
| `[[MCP Apps Interactive UI Protocol]]` | Find file with "Interactive UI" | `[[202609202003 - MCP Apps Interactive UI Protocol]]` |
| `[[Layered Protocol Stack MCP A2A Streamable HTTP]]` | Find file with "Layered Protocol" | `[[202609202004 - Layered Protocol Stack MCP A2A Streamable HTTP]]` |
| `[[Agent Portability via Agent Client Protocol]]` | Find file with "Agent Portability" | `[[202609202005 - Agent Portability via Agent Client Protocol]]` |
| `[[Orchestrator-Worker Delegation Pattern]]` | Find file with "Orchestrator" | `[[202609202020 - Orchestrator-Worker Delegation Pattern]]` |
| `[[Context Compaction and Structured Note-Taking]]` | Find file with "Context Compaction" | `[[202609202021 - Context Compaction and Structured Note-Taking]]` |
| `[[MCP Hybrid Client-Server Architecture]]` | Find file with "Hybrid Client-Server" | `[[202609202022 - MCP Hybrid Client-Server Architecture]]` |
| `[[Claude Code Hooks for CI-CD Automation]]` | Find file with "CI/CD" | `[[202609202001 - Claude Code Hooks for CI-CD Automation]]` |
| `[[Claude Code Plugin Distribution for Team Workflow Standardization]]` | Find file with "Plugin Distribution" | `[[202609202000 - Claude Code Plugin Distribution for Team Workflow Standardization]]` |
| `[[Multi-Server MCP Orchestration for Cross-Tool Workflows]]` | Find file with "Multi-Server MCP" | `[[202609202002 - Multi-Server MCP Orchestration for Cross-Tool Workflows]]` |
| `[[20260920200758 - OpenCode]]` | Wrong timestamp → actual file | `[[202609200758 - OpenCode]]` |
| `[[20260920200759 - Hermes Agent]]` | Wrong timestamp → actual file | `[[202609200759 - Hermes Agent]]` |

**Important:** Wikilinks with wrong timestamps should resolve to the actual file. Check all folders systematically.

**Process:**
1. Use `search_files(pattern="\\[\\[.*\\]\\]", ...)` to find all wikilinks
2. For each `[[link_text]]` find the actual file using the table above as reference
3. Apply fix with `patch(path=..., old_string="[[link_text]]", new_string="[[actual filename]]")`
4. Repeat until zero orphans remain

### Refactoring Rules

Refactoring is expected. When restructuring:

- **Never delete content** — split into new notes or move to `01 - Fleeting/` if it loses relevance
- **Preserve wikilinks** — if a filename changes, update all `[[links]]` across the vault
- **Update MOCs** — rename or re-point any MOC references to moved notes
- **Leave traces** — if a note is superseded, add a `replaced-by: [[new-note]]` frontmatter field

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

The vault is a living system. Small, frequent, well-linked notes beat large, infrequent ones. Refactoring is growth.

---

## Wikilink vs Markdown Link Rules

**Inside notes (`03 - Agents/`, `04 - Plugins/`, etc.):**
Use Obsidian `[[wikilinks]]` — e.g., `[[202609202000 - Claude Code]]`

**In README.md:**
GitHub does NOT render `[[wikilinks]]` as clickable. Use standard Markdown:
- `[Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)`
- `[Firecrawl MCP](./04%20-%20Plugins/202609202000%20-%20Firecrawl%20MCP.md)`

**Always verify the target file exists** before linking. If the file doesn't exist, either create it or link to an existing note.

---

## Link Verification Rules

Every note must have at least 2 working outbound links. No exceptions.

**Definition of "working link":**
- `[[wikilink]]` points to a file that actually exists in the vault
- `[markdown link](url)` points to a valid relative path

**How to verify:**
1. Read note content
2. Extract all `[[...]]` links
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

3. **Cross-reference** each `[[wikilink]]` against the file map:
   - Direct match: `[[202609200758 - OpenCode]]` matches `03 - Agents/202609200758 - OpenCode.md`
   - Short-name match: `[[OpenCode]]` partially matches → resolve to actual filename
   - No match: orphan → fix with `patch()` or replace with closest existing file

4. **Fix orphans** using `patch()`:
   ```
   patch(path="04 - Plugins/202609202000 - Firecrawl MCP Server.md",
         old_string="[[opencode-tavily]]",
         new_string="[[202609202000 - OpenCode Firecrawl]]")
   ```

5. **Repeat** until zero orphans remain.

**Why this works:**
- `search_files` extracts every wikilink from the DOM/text
- The agent reads each note's content and compares against filesystem
- `patch()` updates links without overwriting existing content
- The Obsidian skill's wikilink convention (`[[Note Name]]`) is preserved for Obsidian vault navigation

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

## Daily Trend Scan

For the daily scan workflow, see `scripts/daily-scan-prompt.md`.
The cron job reads AGENTS.md first, then executes the scan prompt instructions.

---

## Parallel Execution

When running automated trend scans (e.g., via cron job), maximize throughput by running research streams in **parallel** using `delegate_task`.

### What Can Be Parallelized
Each of these is independent and can run as a separate sub-agent:

| Stream | Research Focus |
|--------|----------------|
| **Stream A: Agent Profiles** | Search for trending AI coding agents — new releases, GitHub stars, community buzz |
| **Stream B: Plugin Ecosystem** | Scan plugin/extension updates across Hermes, Claude Code, OpenCode, Codex |
| **Stream C: Architecture Patterns** | Discover new patterns — MCP servers, multi-agent orchestration, context engineering |
| **Stream D: Use Cases** | Find real-world workflows, config snippets, integration tutorials |

### Parallel Workflow

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

### Sub-Agent Task Spec

Each parallel sub-agent receives:
- A **specific research question** (e.g., "Find 3 trending AI agents released this week")
- A **target folder** to write notes into
- A **template reference** for note structure
- A **max tool call limit** (keep bounded)

### Post-Parallel Merge

After all sub-agents complete:
1. **Deduplicate** — merge notes on the same topic
2. **Cross-link** — connect notes across streams
3. **Update MOCs** — add new notes to relevant Maps of Content
4. **Refresh README** — update trend tables, radar, and links
5. **Commit** — single atomic commit with all new content
