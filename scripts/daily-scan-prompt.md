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

**IMPORTANT FOR SUB-AGENTS:**
- You are a sub-agent. Load skills independently: `skill_view(name="obsidian")`
- Use `terminal(command="...")` for all git operations
- Use `write_file(path="...", content="...")` to create notes and manifests
- Use `read_file(path="...")` to read templates before writing
- **DO NOT PUT LINKS IN FRONTMATTER** — leave `links:` empty or omit it entirely
- The merge step will populate frontmatter links from actual folder contents
- **ONLY put links in the `## Related` section at the bottom of the note**

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

FRONTMATTER TEMPLATE (NO LINKS):
---
id: 2026092010
created: 2026-09-20T10:00:00+02:00
tags:
  - agent
  - cli
---

RULES:
- DO NOT add links: field to frontmatter
- Put all links in the ## Related section at the bottom
- Use short names in ## Related: [[Claude Code]], [[Aider]], etc.
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

FRONTMATTER TEMPLATE (NO LINKS):
---
id: 2026092020
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - mcp
---

RULES:
- DO NOT add links: field to frontmatter
- Put all links in the ## Related section at the bottom
- Link to MOCs in ## Related: [[MOC-Plugin-Ecosystem]], [[MOC-Trending-Agents]]
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

FRONTMATTER TEMPLATE (NO LINKS):
---
id: 2026092030
created: 2026-09-20T30:00:00+02:00
tags:
  - architecture
  - mcp
---

RULES:
- DO NOT add links: field to frontmatter
- Put all links in the ## Related section at the bottom
- Use short names: [[Claude Code]], [[MCP Protocol]], etc.
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

FRONTMATTER TEMPLATE (NO LINKS):
---
id: 2026092040
created: 2026-09-20T40:00:00+02:00
tags:
  - workflow
  - config
---

RULES:
- DO NOT add links: field to frontmatter
- Put all links in the ## Related section at the bottom
- Link to MOCs: [[MOC-Plugin-Ecosystem]], [[MOC-Architecture-Patterns]]
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

### Step 2: Build Link Map from Actual Files

**Create a complete file map of the vault:**

```python
# Pseudocode — execute via execute_code or logic in your response:
file_map = {}
for root, dirs, files in os.walk('${HOME}/repository/git/ai-matrix-trends'):
    if '/.git' in root: continue
    for f in files:
        if f.endswith('.md'):
            fname = f.replace('.md', '')
            file_map[fname.lower()] = os.path.join(root, f)
```

**Then for each new note from manifests:**
1. Read note content
2. Find all `[[short name]]` links in body
3. Match each short name against file_map
4. Build proper links using actual filenames
5. Add `links:` field to frontmatter with 2+ actual filename wikilinks

### Step 3: Add Frontmatter Links to New Notes

For EVERY note created by sub-agents:

1. Read the note
2. Find the `## Related` section
3. Extract short names from `[[...]]` links
4. Search all folders for matching filenames
5. Add a `links:` field to frontmatter:

```
patch(path="<note>",
      old_string="---\nid: ...\ncreated: ...\ntags:\n  - ...",
      new_string="---\nid: ...\ncreated: ...\ntags:\n  - ...\nlinks:\n  - \"[[YYYYMMDDHHMM - Actual Title]]\"\n  - \"[[YYYYMMDDHHMM - Actual Title 2]]\"\n---")
```

**Critical:** The links field MUST contain at least 2 wikilinks pointing to EXISTING files.

### Step 4: Fix Orphan Wikilinks

For EVERY note in all folders:
1. Find all `[[link_text]]` in body
2. Check if target exists in file_map
3. If not, find closest match and fix with `patch()`

### Step 5: Add Cross-Stream Links

Using manifest data:
- Agents → Plugins (from plugin manifest `agents` field)
- Plugins → Agents (same)
- Architecture → Agents (from pattern manifest `examples` field)
- Use Cases → Agents + Plugins (from use case manifest)

### Step 6: Update MOCs and Master Indexes
- Update MOC-Trending-Agents.md
- Update MOC-Plugin-Ecosystem.md
- Update MOC-Architecture-Patterns.md
- Update AI Architecture Master Index (05 - Architecture/00 - AI Architecture Master Index.md)
- Update Plugin Master Index (04 - Plugins/00 - Plugin Master Index.md)

### Step 7: Update README
- Convert all `[[wikilinks]]` to `[text](./path.md)` Markdown links
- Remove duplicates
- Update Trend Radar tables
- Create atomic notes in 09 - Trend Radar/ folders for new trends
- Update date

### Step 8: Verify All Links
- Count wikilinks per note (all must have ≥2)
- Check README links are valid
- Fix any remaining orphans

### Step 9: Final Commit
```
terminal(command="cd ${HOME}/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan: cross-links, MOCs, README' && git push")
```

### Step 10: Cleanup
Remove old manifest files, keep current day.

### Step 11: Validate Frontmatter
Spot-check 5 notes: verify `id`, `created`, `tags`, `links` all present and populated.

---

## Rules
- One idea per note
- Own words, never copy-paste
- Unique timestamps per filename
- Sub-agents: DO NOT put links in frontmatter — use ## Related section
- Merge step: ADD frontmatter links from actual folder contents
- Minimum 2 outbound links per note
- Cross-stream linking is mandatory

*Vault path: ${HOME}/repository/git/ai-matrix-trends*
*Agent profile: ai-matrix-trends*
