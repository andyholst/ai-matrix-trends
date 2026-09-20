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
- Use UNIQUE timestamps: 202609202020, 202609202021, 202609202022, etc.
- Every note must link to at least 2 other notes in the SAME folder
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

### Step 2: Fix Orphan Wikilinks

Search for broken links in each folder and fix them. For each folder:
1. Use `search_files(pattern="\\[\\[.*\\]\\]", target="content", path="03 - Agents", file_glob="*.md")` to find all wikilinks
2. For each `[[link]]` found, check if the target file exists:
   - If `link` contains a filename like `202609202000 - Claude Code`, search: `search_files(pattern="202609202000 - Claude Code.md", target="files", path=".")`
   - If the file does NOT exist, search for a match: `search_files(pattern="*Claude Code*", target="files", path="03 - Agents")`
   - Update the wikilink to match the actual filename using `patch()` on the source file
3. Repeat for all folders: `03 - Agents`, `04 - Plugins`, `05 - Architecture`, `06 - Use Cases`

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

### Step 4: Update MOCs with New Notes

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
5. Update tables from manifests, update trend radar, update date
6. `write_file(path="README.md", content="...")` with complete updated content

**Goal:** Zero `[[wikilinks]]` in README. All links are clickable Markdown.
5. **Update tables:**
   - Trending Agents — from stream-a manifest, remove old duplicates
   - Top Plugins — from stream-b manifest, remove old duplicates
   - Architecture Patterns — from stream-c manifest, remove old duplicates
   - Configuration Snippets — from stream-d manifest, only link to existing files
6. **Update Trend Radar** — move items as needed
7. **Update `Last refreshed: YYYY-MM-DD`** at the bottom
8. **Write the updated README** using `write_file(path="README.md", content="...")` or `patch()` for targeted edits

**Goal:** Every link in README must be a working Markdown link. No orphans, no `[[wikilinks]]`.

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

Spot-check 2-3 notes to verify frontmatter is complete:
```
read_file(path="03 - Agents/<newest-note>.md", limit=15)
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
