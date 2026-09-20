# AI Matrix Trends — Daily Scan Instructions

This file is the daily scan workflow for the AI Matrix Trends vault.
The cron job reads AGENTS.md first for context, then this file for instructions.

**Important:** After each major step, run `git add -A && git commit -m "..." && git push` to persist progress. If the Hermes agent fails mid-scan, completed work is already on remote.

---

## Pre-Scan Setup

1. **Load required skills:**
   ```
   skill_view(name="obsidian")
   ```
   This gives you vault operations (read, write, wikilinks).

2. **Load research tools.** This profile has Firecrawl enabled. Use:
   - `web_search(query)` — search for trending tools
   - `web_extract([urls])` — scrape content from specific pages

3. Read `AGENTS.md` in the vault root for vault structure, templates, and rules.
4. Read note templates:
   ```
   read_file(path=".obsidian/templates/agent-profile.md")
   read_file(path=".obsidian/templates/plugin-profile.md")
   read_file(path=".obsidian/templates/architecture-pattern.md")
   read_file(path=".obsidian/templates/atomic-note.md")
   ```
5. Check existing vault state:
   ```bash
   search_files(pattern="*.md", target="files", path="03 - Agents")
   search_files(pattern="*.md", target="files", path="04 - Plugins")
   search_files(pattern="*.md", target="files", path="05 - Architecture")
   search_files(pattern="*.md", target="files", path="06 - Use Cases")
   ```
6. Read existing MOCs and README to understand current vault state:
   ```
   read_file(path="07 - Structure/MOC-Trending-Agents.md")
   read_file(path="07 - Structure/MOC-Plugin-Ecosystem.md")
   read_file(path="07 - Structure/MOC-Architecture-Patterns.md")
   read_file(path="README.md")
   ```
7. Initial commit checkpoint:
   ```bash
   cd "${HOME}/repository/git/ai-matrix-trends"
   git add -A
   git commit -m "Daily scan: pre-scan state checkpoint" || echo "Nothing to commit"
   git push
   ```

---

## Parallel Research Streams

Launch 4 parallel research streams using `delegate_task`.

**Key:** Each stream writes a **manifest** file after creating notes. The merge step reads all manifests to cross-link.

**Timestamp allocation strategy:**
- Stream A: use minutes 00, 01, 02, 03, 04
- Stream B: use minutes 10, 11, 12, 13, 14
- Stream C: use minutes 20, 21, 22
- Stream D: use minutes 30, 31, 32

This prevents collisions between parallel streams.

**Research method for each stream:**
1. Use `web_search(query)` to find trending tools (e.g., "trending AI coding agents 2026", "best Claude Code plugins")
2. Use `web_extract([urls])` to get details from specific pages
3. Synthesize findings into atomic notes
4. Write notes using the appropriate template
5. Write manifest file

**Important for sub-agents:**
- You are a sub-agent. Load skills independently: `skill_view(name="obsidian")`
- Use `terminal(command="...")` for all git operations (commit, push, etc.)
- Use `write_file(path="...", content="...")` to create notes and manifests
- Use `read_file(path="...")` to read templates before writing

### Stream A: Agent Profiles
```
Goal: Find 3-5 trending AI coding agents.
Focus areas:
- Claude Code, OpenCode, Hermes, Codex, Cursor, Cline, Aider, Windsurf, Pi
- New releases, GitHub star growth, HN/Reddit/Twitter mentions
- Compare features, pricing, architecture

Before writing:
- Load skill: skill_view(name="obsidian")
- Read template: read_file(path=".obsidian/templates/agent-profile.md")

Research steps:
1. web_search("trending AI coding agents 2026")
2. web_search("Claude Code vs Codex vs Cursor comparison")
3. web_search("AI coding agent GitHub stars growth")
4. web_extract relevant URLs for details

Write notes to: 03 - Agents/

RULES:
- Use UNIQUE timestamps: 202609202000, 202609202001, 202609202002, etc.
- Every note must link to at least 2 other notes in the SAME folder
- **CRITICAL: The `links:` frontmatter field MUST contain at least 2 working wikilinks**
- **Sub-agents: Do NOT write links like `[[Claude Code]]` in the frontmatter — write `[[202609202000 - Claude Code]]` (the actual filename)**
- Example frontmatter:
  ```
  ---
  id: 202609202000
  created: 2026-09-20T20:00:00+02:00
  tags:
    - agent
    - cli
  links:
    - "[[202609202000 - Claude Code]]"
    - "[[202609202000 - Aider]]"
  ---
  ```
- Do NOT link to notes in other folders yet (cross-linking happens in merge)
- After writing notes, create manifest using write_file:
  write_file("08 - Projects/scan-manifests/stream-a-UNIQUE.json", '[{"file": "03 - Agents/YYYYMMDDHHMM - Name.md", "title": "Name", "type": "agent", "tags": ["cli", "tool"]}, ...]')
- Use terminal for git: terminal(command="cd ${HOME}/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan: agent profiles' && git push")
```

### Stream B: Plugin Ecosystem
```
Goal: Find 3-5 trending plugins/extensions.
Focus areas:
- Hermes plugins (jev, mcp, skills, kanban, curator)
- Claude Code extensions (MCP servers, skills)
- OpenCode/Codex integrations
- Cross-agent tools (Browser Use, Firecrawl, FAL)

Before writing:
- Load skill: skill_view(name="obsidian")
- Read template: read_file(path=".obsidian/templates/plugin-profile.md")

Research steps:
1. web_search("best Claude Code MCP servers 2026")
2. web_search("Hermes AI agent plugins")
3. web_search("OpenCode plugins and extensions")
4. web_search("AI coding agent browser automation tools")
5. web_extract relevant URLs for details

Write notes to: 04 - Plugins/

RULES:
- Use UNIQUE timestamps: 202609202010, 202609202011, 202609202012, etc.
- Every note must link to at least 2 MOCs: [[MOC-Plugin-Ecosystem]] and [[MOC-Trending-Agents]]
- Do NOT link to specific agent notes yet (cross-linking happens in merge)
- After writing notes, create manifest using write_file:
  write_file("08 - Projects/scan-manifests/stream-b-UNIQUE.json", '[{"file": "04 - Plugins/YYYYMMDDHHMM - Name.md", "title": "Name", "type": "plugin", "agents": ["Claude Code"]}, ...]')
- Use terminal for git: terminal(command="cd ${HOME}/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan: plugin ecosystem' && git push")
```

### Stream C: Architecture Patterns
```
Goal: Find 2-3 emerging architecture patterns.
Focus areas:
- MCP Protocol developments
- Multi-agent orchestration patterns
- Context engineering (RAG, summarization, curation)
- Tool-calling patterns and guardrails

Before writing:
- Load skill: skill_view(name="obsidian")
- Read template: read_file(path=".obsidian/templates/architecture-pattern.md")

Research steps:
1. web_search("MCP protocol architecture patterns 2026")
2. web_search("multi-agent AI orchestration patterns")
3. web_search("context engineering for long-horizon agents")
4. web_search("AI agent guardrails and safety patterns")
5. web_extract relevant URLs for details

Write notes to: 05 - Architecture/

RULES:
- Use UNIQUE timestamps: 202609202000, 202609202001, 202609202002, etc.
- Every note must link to at least 2 other notes in the SAME folder
- **CRITICAL: The `links:` frontmatter field MUST contain at least 2 working wikilinks**
- **Sub-agents: Do NOT write links like `[[Claude Code]]` in the frontmatter — write `[[202609202000 - Claude Code]]` (the actual filename)**
- Example frontmatter:
  ```
  ---
  id: 202609202000
  created: 2026-09-20T20:00:00+02:00
  tags:
    - agent
    - cli
  links:
    - "[[202609202000 - Claude Code]]"
    - "[[202609202000 - Aider]]"
  ---
  ```
- Do NOT link to notes in other folders yet (cross-linking happens in merge)
- After writing notes, create manifest using write_file:
  write_file("08 - Projects/scan-manifests/stream-c-UNIQUE.json", '[{"file": "05 - Architecture/YYYYMMDDHHMM - Name.md", "title": "Name", "type": "architecture", "examples": ["Claude Code"]}, ...]')
- Use terminal for git: terminal(command="cd ${HOME}/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan: architecture patterns' && git push")
```

### Stream D: Use Cases
```
Goal: Find 2-3 real-world use cases or workflows.
Focus areas:
- Agent + plugin combinations
- Config snippets and setup patterns
- Integration tutorials
- Workflow automation examples

Before writing:
- Load skill: skill_view(name="obsidian")
- Read template: read_file(path=".obsidian/templates/atomic-note.md")

Research steps:
1. web_search("Claude Code hooks CI/CD automation")
2. web_search("AI coding agent team workflow standardization")
3. web_search("multi-server MCP orchestration workflows")
4. web_search("AI agent plugin combinations use cases")
5. web_extract relevant URLs for details

Write notes to: 06 - Use Cases/

RULES:
- Use UNIQUE timestamps: 202609202030, 202609202031, 202609202032, etc.
- Every note must link to at least 2 MOCs: [[MOC-Plugin-Ecosystem]] and [[MOC-Architecture-Patterns]]
- Do NOT link to specific notes yet (cross-linking happens in merge)
- After writing notes, create manifest using write_file:
  write_file("08 - Projects/scan-manifests/stream-d-UNIQUE.json", '[{"file": "06 - Use Cases/YYYYMMDDHHMM - Name.md", "title": "Name", "type": "workflow", "agents": ["Claude Code"], "plugins": ["Firecrawl"]}, ...]')
- Use terminal for git: terminal(command="cd ${HOME}/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan: use cases' && git push")
```

---

## Post-Scan Merge (CRITICAL — after all streams complete)

**This step is mandatory.** Do not skip. The vault is only complete when cross-links exist.

### Step 1: Read All Manifests

```bash
search_files(pattern="stream-*.json", target="files", path="08 - Projects/scan-manifests")
```

Read each manifest file to understand what was created:
- `stream-a-*.json` — agents
- `stream-b-*.json` — plugins (with `agents` field showing compatibility)
- `stream-c-*.json` — architecture patterns (with `examples` field)
- `stream-d-*.json` — use cases (with `agents` and `plugins` fields)

### Step 2: Fix Orphan Wikilinks and Frontmatter Links

For each folder (03 - Agents, 04 - Plugins, 05 - Architecture, 06 - Use Cases):

1. Find all wikilinks: `search_files(pattern="\\[\\[.*\\]\\]", target="content", path="03 - Agents", file_glob="*.md")`

2. For each `[[link_text]]` found, check if target file exists:
   - Walk all folders and compare link_text against filenames
   - Match rules: `[[Claude Code]]` matches `202609202000 - Claude Code.md`
   - Match rules: `[[202609202000 - Claude Code]]` matches exactly

3. If NO match found, find the best replacement:
   - Search for partial match: if link is `[[opencode-tavily]]`, look for files containing "opencode" or "tavily"
   - Search for related terms: if link is `[[VS Code]]`, link to an existing editor note like `[[202609202000 - Cursor]]`
   - If no good match exists, link to the most relevant MOC

4. Apply the fix using `patch()`:
   ```
   patch(path="04 - Plugins/202609202000 - Firecrawl MCP Server.md",
         old_string="[[opencode-tavily]]",
         new_string="[[202609202000 - OpenCode Firecrawl]]")
   ```

5. **Verify frontmatter links:** For every note, ensure the `links:` field exists and has at least 2 working wikilinks. If missing, add them using `patch()`:
   ```
   patch(path="03 - Agents/202609202000 - Devin.md",
         old_string="---\nid: 202609202000\ncreated: ...",
         new_string="---\nid: 202609202000\ncreated: ...\nlinks:\n  - \"[[202609202000 - Claude Code]]\"\n  - \"[[202609200758 - OpenCode]]\"\n---")
   ```

6. Repeat until zero orphans remain.

**Important:** The sub-agents write notes with short-name wikilinks like `[[Claude Code]]` but files are named `202609202000 - Claude Code.md`. Your job is to resolve these to the actual filename.

**Common wikilink patterns to resolve:**

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

### Step 3: Add Cross-Stream Links Using Manifests

Use the manifest data to add intelligent cross-links:

**Agents → Plugins:** For each agent, check which plugins list it in their `agents` field. Add those plugin links to the agent note.

**Plugins → Agents:** For each plugin, add links to the agents it supports (from manifest `agents` field).

**Architecture → Agents:** For each pattern, add links to agents in its `examples` field.

**Use Cases → Agents/Plugins:** For each use case, add links to agents and plugins listed in its manifest.

**How to update links in existing notes:**
1. `read_file(path="03 - Agents/202609202000 - Claude Code.md")`
2. Use `patch()` to add new links to the `links:` frontmatter and `## Related` section:
   ```
   patch(path="03 - Agents/202609202000 - Claude Code.md",
         old_string="links:\n  - [[202609202000 - Codex]]\n  - [[202609202000 - Cline]]",
         new_string="links:\n  - [[202609202000 - Codex]]\n  - [[202609202000 - Cline]]\n  - [[202609202010 - Browser Use MCP]]")
   ```

### Step 4: Update MOCs and Master Index with New Notes

Open each MOC file and add new notes from manifests to the appropriate cluster:
- `07 - Structure/MOC-Trending-Agents.md` — add new agents from stream-a manifest
- `07 - Structure/MOC-Plugin-Ecosystem.md` — add new plugins from stream-b manifest
- `07 - Structure/MOC-Architecture-Patterns.md` — add new patterns from stream-c manifest

How:
1. `read_file(path="07 - Structure/MOC-Trending-Agents.md")`
2. Use `patch()` to add new entries under `## Key Notes` or `## Clusters`

Format:
```markdown
- [[YYYYMMDDHHMM - Note Title]] — [one-line summary from manifest]
```

**For Architecture Patterns:**
- Also update the AI Architecture Master Index at `05 - Architecture/00 - AI Architecture Master Index.md`
- Add new patterns to the appropriate section (Core, Emerging, Production)
- Update the comparison table if adoption levels changed

**For Plugins:**
- Also update the Plugin Master Index at `04 - Plugins/00 - Plugin Master Index.md`
- Categorize new plugins as Trending/Stable/Emerging
- Add to the By Agent Ecosystem section
- Link to supported agents

### Step 5: Update README (DEDUPLICATE AND CLEAN)

**CRITICAL: README LINK FORMAT FOR GITHUB**
GitHub does NOT render `[[wikilinks]]` as clickable. Every link MUST use: `[Display Text](./path%20with%20spaces/file.md)`

**Examples:**
- ✅ `[Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)`
- ❌ `[[Claude Code]]`

**Steps:**
1. `read_file(path="README.md")` to see current content
2. Convert every `[[...]]` to `[text](./path.md)` format
3. Verify target exists: `search_files(pattern="filename.md", target="files", path=".")`
4. Remove duplicate entries (old non-timestamped versions)
5. **Update Trend Radar (CRITICAL):**
   Analyze all new findings and update the Trend Radar section in README.md AND create atomic notes in the appropriate folders:

   **Heating Up 🔥** (`09 - Trend Radar/Heating Up/`) — Recent (last 30 days), rapid growth signals:
   - New tools/plugins with rapid GitHub star growth (>5k stars/week)
   - New architecture patterns gaining adoption (MCP servers, multi-agent orchestration)
   - Community buzz (HN front page, Reddit r/LocalLMAI top posts)
   - New releases from major players (Claude Code features, OpenAI Codex updates)

   **Stable 📈** (`09 - Trend Radar/Stable/`) — Established patterns, steady adoption:
   - Tool-calling as standard interface (all agents now do this)
   - RAG + context compression (standard practice)
   - IDE integrations (VS Code, JetBrains, Zed)
   - MCP as universal plugin protocol
   - Containerized agent sandboxes (Docker profiles)

   **Emerging 🌱** (`09 - Trend Radar/Emerging/`) — Early signals, watch list:
   - Agent-to-agent communication (A2A, ACP protocols)
   - Verifiable execution (cryptographic proof of agent actions)
   - Federated agent networks
   - Personal agent memory systems (cross-session memory)
   - Interactive UI protocols (MCP Apps)
   - New architecture patterns from Stream C analysis

   **How to update:**
   1. Read current Trend Radar from README.md
   2. Analyze findings from all 4 streams
   3. Move items between categories based on new evidence
   4. Add new items with evidence from research
   5. Remove outdated items
   6. Create atomic notes in the appropriate Trend Radar folder for each new trend signal:
      - Use `write_file(path="09 - Trend Radar/Heating Up/YYYYMMDDHHMM - Trend Name.md", content=...)`
      - Include frontmatter with id, created, tags, links
      - Link to related notes in the vault
   7. Write updated Trend Radar using `patch()` on README.md

6. **Update `Last refreshed: YYYY-MM-DD`** at the bottom
6. `write_file(path="README.md", content="...")` with complete updated content


   **Goal:** Zero `[[wikilinks]]` in README. All links are clickable Markdown. No orphans.

### Step 6: Verify All Links (NOTES + README)

Every note AND every link in README/MOCs must have at least 2 working outbound links.

```bash
# Count links per file (should be >= 2)
grep -c "\\[\\[" "03 - Agents/"*.md
grep -c "\\[\\[" "04 - Plugins/"*.md
grep -c "\\[\\[" "05 - Architecture/"*.md
grep -c "\\[\\[" "06 - Use Cases/"*.md
```

**Also verify README links:**
1. `read_file(path="README.md")`
2. Extract all `[text](url)` and `[[wikilinks]]`
3. For each, check if target file exists with `search_files`
4. If any link is broken, fix it now using `patch()` on README.md

If any note has fewer than 2 links, add more.

### Step 7: Final Commit and Push

Use `terminal` for git operations:
```
terminal(command="cd ${HOME}/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan: cross-links, MOCs, README update' && git push")
```

### Step 8: Cleanup

Remove old manifest files from previous runs (keep current):
```
terminal(command="find '${HOME}/repository/git/ai-matrix-trends/08 - Projects/scan-manifests' -name '*.json' ! -name '*$(date +%Y%m%d)*' -delete")
```

### Step 9: Validate Frontmatter

Verify every note has complete frontmatter with working links:

```bash
# Check each note
read_file(path="03 - Agents/<note>.md", limit=15)
```

**Verify all fields:**
- `id:` — matches filename timestamp
- `created:` — ISO 8601 date
- `tags:` — at least 1 tag
- `links:` — **at least 2 working wikilinks**

**Fix missing links field:**
```
patch(path="...", 
      old_string="---\nid: ...\ncreated: ...\ntags:\n  - ...",
      new_string="---\nid: ...\ncreated: ...\ntags:\n  - ...\nlinks:\n  - \"[[...]]\"\n  - \"[[...]]\"")
```

Verify: `id`, `created`, `tags`, `links` all present and populated. If missing, add them via `patch()`.

---

## Rules

- One idea per note. Split compound topics.
- Own words — synthesize, never copy-paste. Use blockquotes with attribution for sources.
- **Unique timestamp prefix per filename:** `YYYYMMDDHHMM - Title.md` — never reuse the same timestamp for multiple files.
- Frontmatter must include: `id`, `created`, `tags`, `links`
- **Minimum 2 outbound links per note** — and they must point to EXISTING files
- Never delete existing content — split, merge, or add `replaced-by` frontmatter
- If a note already exists for a topic, UPDATE it rather than creating duplicate
- **Cross-stream linking is mandatory** — agents link to plugins, patterns link to agents

---

*Vault path: ${HOME}/repository/git/ai-matrix-trends*
*Agent profile: ai-matrix-trends*
