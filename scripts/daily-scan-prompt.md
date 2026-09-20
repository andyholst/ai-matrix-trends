# AI Matrix Trends — Daily Scan Instructions

This file is the daily scan workflow for the AI Matrix Trends vault.
The cron job reads AGENTS.md first for context, then this file for instructions.

---

## Pre-Scan Setup

1. **Load required skills:** `skill_view(name="obsidian")`
2. **Research tools:** `web_search(query)`, `web_extract([urls])`
3. Read `AGENTS.md` for vault structure, templates, and rules
4. Read note templates:
   - `read_file(path=".obsidian/templates/agent-profile.md")`
   - `read_file(path=".obsidian/templates/plugin-profile.md")`
   - `read_file(path=".obsidian/templates/architecture-pattern.md")`
   - `read_file(path=".obsidian/templates/atomic-note.md")`
5. Check existing vault state: `search_files` on all folders
6. Read existing MOCs and README
7. Initial commit checkpoint

---

## Parallel Research Streams

Launch 4 parallel streams via `delegate_task`.

**Important for sub-agents:**
- You are a sub-agent. Load skills independently: `skill_view(name="obsidian")`
- Use `terminal(command="...")` for all git operations
- Use `write_file(path="...", content="...")` to create notes and manifests
- Use `read_file(path="...")` to read templates before writing
- **FRONTMATTER MUST INCLUDE `links:` WITH AT LEAST 2 WIKILINKS**

### Stream A: Agent Profiles
```
Goal: Find 3-5 trending AI coding agents.
Timestamps: use minutes 10, 11, 12, 13, 14 (e.g., 2026092010, 2026092011)

Before writing:
- Load skill: skill_view(name="obsidian")
- Read template: read_file(path=".obsidian/templates/agent-profile.md")

Research:
1. web_search("trending AI coding agents 2026")
2. web_search("Claude Code vs Codex vs Cursor comparison")
3. web_extract relevant URLs

Write to: 03 - Agents/

MANDATORY FRONTMATTER TEMPLATE:
---
id: 2026092010
created: 2026-09-20T10:00:00+02:00
tags:
  - agent
  - cli
links:
  - "[[2026092011 - Agent Name 2]]"
  - "[[2026092012 - Agent Name 3]]"
---

RULES:
- Every note MUST have links field with 2+ wikilinks in frontmatter
- Wikilink format: [[YYYYMMDDHHMM - Exact Title.md]] (the actual filename)
- Do NOT write [[Claude Code]] — write [[2026092010 - Claude Code]] (actual filename)
- Link to notes in the SAME folder (other agents)
- After writing: create manifest at 08 - Projects/scan-manifests/stream-a-UNIQUE.json
  Format: [{"file": "03 - Agents/2026092010 - Name.md", "title": "Name", "type": "agent", "tags": [...]}]
- Git: terminal(command="cd ${HOME}/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan: agent profiles' && git push")
```

### Stream B: Plugin Ecosystem
```
Goal: Find 3-5 trending plugins/extensions.
Timestamps: use minutes 20, 21, 22, 23, 24 (e.g., 2026092020, 2026092021)

Before writing:
- Load skill: skill_view(name="obsidian")
- Read template: read_file(path=".obsidian/templates/plugin-profile.md")

Research:
1. web_search("best Claude Code MCP servers 2026")
2. web_search("OpenCode plugins and extensions")
3. web_search("AI coding agent browser automation tools")
4. web_extract relevant URLs

Write to: 04 - Plugins/

MANDATORY FRONTMATTER TEMPLATE:
---
id: 2026092020
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - mcp
links:
  - "[[MOC-Plugin-Ecosystem]]"
  - "[[MOC-Trending-Agents]]"
---

RULES:
- Every note MUST have links field with 2+ wikilinks in frontmatter
- Link to MOC-Plugin-Ecosystem and MOC-Trending-Agents
- Do NOT link to specific agent notes yet (cross-linking in merge)
- After writing: create manifest at 08 - Projects/scan-manifests/stream-b-UNIQUE.json
  Format: [{"file": "04 - Plugins/2026092020 - Name.md", "title": "Name", "type": "plugin", "agents": ["Claude Code"]}]
- Git: terminal(command="cd ${HOME}/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan: plugin ecosystem' && git push")
```

### Stream C: Architecture Patterns
```
Goal: Find 2-3 emerging architecture patterns.
Timestamps: use minutes 30, 31, 32 (e.g., 2026092030, 2026092031)

Before writing:
- Load skill: skill_view(name="obsidian")
- Read template: read_file(path=".obsidian/templates/architecture-pattern.md")

Research:
1. web_search("MCP protocol architecture patterns 2026")
2. web_search("multi-agent AI orchestration patterns")
3. web_search("context engineering for long-horizon agents")
4. web_extract relevant URLs

Write to: 05 - Architecture/

MANDATORY FRONTMATTER TEMPLATE:
---
id: 2026092030
created: 2026-09-20T30:00:00+02:00
tags:
  - architecture
  - mcp
links:
  - "[[2026092031 - Pattern Name 2]]"
  - "[[2026092032 - Pattern Name 3]]"
---

RULES:
- Every note MUST have links field with 2+ wikilinks in frontmatter
- Wikilink format: [[YYYYMMDDHHMM - Exact Title.md]] (the actual filename)
- Link to notes in the SAME folder (other patterns)
- After writing: create manifest at 08 - Projects/scan-manifests/stream-c-UNIQUE.json
  Format: [{"file": "05 - Architecture/2026092030 - Name.md", "title": "Name", "type": "architecture", "examples": ["Claude Code"]}]
- Git: terminal(command="cd ${HOME}/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan: architecture patterns' && git push")
```

### Stream D: Use Cases
```
Goal: Find 2-3 real-world use cases or workflows.
Timestamps: use minutes 40, 41, 42 (e.g., 2026092040, 2026092041)

Before writing:
- Load skill: skill_view(name="obsidian")
- Read template: read_file(path=".obsidian/templates/atomic-note.md")

Research:
1. web_search("Claude Code hooks CI/CD automation")
2. web_search("multi-server MCP orchestration workflows")
3. web_search("AI agent plugin combinations use cases")
4. web_extract relevant URLs

Write to: 06 - Use Cases/

MANDATORY FRONTMATTER TEMPLATE:
---
id: 2026092040
created: 2026-09-20T40:00:00+02:00
tags:
  - workflow
  - config
links:
  - "[[MOC-Plugin-Ecosystem]]"
  - "[[MOC-Architecture-Patterns]]"
---

RULES:
- Every note MUST have links field with 2+ wikilinks in frontmatter
- Link to MOC-Plugin-Ecosystem and MOC-Architecture-Patterns
- Do NOT link to specific notes yet (cross-linking in merge)
- After writing: create manifest at 08 - Projects/scan-manifests/stream-d-UNIQUE.json
  Format: [{"file": "06 - Use Cases/2026092040 - Name.md", "title": "Name", "type": "workflow", "agents": ["Claude Code"], "plugins": ["Firecrawl"]}]
- Git: terminal(command="cd ${HOME}/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan: use cases' && git push")
```

---

## Post-Scan Merge (MANDATORY — after all streams complete)

### Step 1: Read All Manifests
```
search_files(pattern="stream-*.json", target="files", path="08 - Projects/scan-manifests")
```
Read each manifest to understand what was created.

### Step 2: Fix Orphan Wikilinks AND Frontmatter Links

**For each folder (03 - Agents, 04 - Plugins, 05 - Architecture, 06 - Use Cases):**

1. Extract all wikilinks: `search_files(pattern="\\[\\[.*\\]\\]", target="content", path="<folder>", file_glob="*.md")`

2. For each `[[link_text]]` found, check if target file exists by walking all folders

3. If NO match found, find the best replacement using partial matching

4. Apply fix: `patch(path="<file>", old_string="[[<link>]]", new_string="[[<actual filename>]]")`

5. **CHECK FRONTMATTER:** For every note, verify the `links:` field exists and has 2+ wikilinks:
   - Read note: `read_file(path="<note>", limit=15)`
   - Check for `links:` field
   - If missing or empty, ADD IT using patch():
   ```
   patch(path="<note>",
         old_string="---\nid: ...\ncreated: ...\ntags:\n  - ...",
         new_string="---\nid: ...\ncreated: ...\ntags:\n  - ...\nlinks:\n  - \"[[<actual filename 1>]]\"\n  - \"[[<actual filename 2>]]\"\n---")
   ```

6. Repeat until zero orphans AND all frontmatter has 2+ links.

**Important:** Sub-agents write short-name wikilinks like `[[Claude Code]]` but files are named `2026092010 - Claude Code.md`. Resolve to actual filename.

**Common patterns:**
- `[[Claude Code]]` → `[[2026092010 - Claude Code]]`
- `[[OpenCode]]` → `[[2026092011 - OpenCode]]`
- `[[opencode-tavily]]` → `[[2026092020 - OpenCode Firecrawl]]`

### Step 3: Add Cross-Stream Links
Use manifest data to add intelligent cross-links:
- Agents → Plugins (from plugin manifest `agents` field)
- Plugins → Agents (same)
- Architecture → Agents (from pattern manifest `examples` field)
- Use Cases → Agents + Plugins (from use case manifest)

### Step 4: Update MOCs and Master Indexes
- Update MOC-Trending-Agents.md
- Update MOC-Plugin-Ecosystem.md
- Update MOC-Architecture-Patterns.md
- Update AI Architecture Master Index (05 - Architecture/00 - AI Architecture Master Index.md)
- Update Plugin Master Index (04 - Plugins/00 - Plugin Master Index.md)

### Step 5: Update README
- Convert all `[[wikilinks]]` to `[text](./path.md)` Markdown links
- Remove duplicates
- Update Trend Radar tables
- Create atomic notes in 09 - Trend Radar/ folders for new trends
- Update date

### Step 6: Verify All Links
- Count wikilinks per note (all must have ≥2)
- Check README links are valid
- Fix any remaining orphans

### Step 7: Final Commit
```
terminal(command="cd ${HOME}/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan: cross-links, MOCs, README' && git push")
```

### Step 8: Cleanup
Remove old manifest files, keep current day.

### Step 9: Validate Frontmatter
Spot-check 3-5 notes: verify `id`, `created`, `tags`, `links` all present and populated.

---

## Rules
- One idea per note
- Own words, never copy-paste
- Unique timestamps per filename
- Frontmatter must include: `id`, `created`, `tags`, `links`
- Minimum 2 outbound links per note
- Cross-stream linking is mandatory

*Vault path: ${HOME}/repository/git/ai-matrix-trends*
*Agent profile: ai-matrix-trends*
