# AI Matrix Trends — Daily Scan Instructions

This file is the daily scan workflow for the AI Matrix Trends vault.
The cron job reads AGENTS.md first for context, then this file for instructions.

**Important:** After each major step, run `git add -A && git commit -m "..." && git push` to persist progress. If the Hermes agent fails mid-scan, completed work is already on remote.

---

## Pre-Scan Setup

1. Read `AGENTS.md` in the vault root for vault structure, templates, and rules.
2. Check existing vault state:
   ```bash
   search_files(pattern="*.md", target="files", path="03 - Agents")
   search_files(pattern="*.md", target="files", path="04 - Plugins")
   search_files(pattern="*.md", target="files", path="05 - Architecture")
   search_files(pattern="*.md", target="files", path="06 - Use Cases")
   ```
3. **Read existing MOCs and README** to understand current vault state:
   ```bash
   read_file(path="07 - Structure/MOC-Trending-Agents.md")
   read_file(path="07 - Structure/MOC-Plugin-Ecosystem.md")
   read_file(path="07 - Structure/MOC-Architecture-Patterns.md")
   read_file(path="README.md")
   ```
4. Initial commit checkpoint:
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

### Stream A: Agent Profiles
```
Goal: Find 3-5 trending AI coding agents.
Focus areas:
- Claude Code, OpenCode, Hermes, Codex, Cursor, Cline, Aider, Windsurf, Pi
- New releases, GitHub star growth, HN/Reddit/Twitter mentions
- Compare features, pricing, architecture

Write notes to: 03 - Agents/ (use agent-profile template from AGENTS.md)

RULES:
- Use UNIQUE timestamps per note (increment: 2000, 2001, 2002...)
- Every note must link to at least 2 other notes in the SAME folder
- Do NOT link to notes in other folders yet (cross-linking happens in merge)
- After writing notes, create manifest: write_file("08 - Projects/scan-manifests/stream-a-$(date +%Y%m%d%H%M).json", ...)
- Manifest format: JSON array of {"file": "...", "title": "...", "type": "agent", "tags": [...]}

After manifest: cd "${HOME}/repository/git/ai-matrix-trends" && git add -A && git commit -m "Daily scan: agent profiles $(date +%Y-%m-%d)" && git push
```

### Stream B: Plugin Ecosystem
```
Goal: Find 3-5 trending plugins/extensions.
Focus areas:
- Hermes plugins (jev, mcp, skills, kanban, curator)
- Claude Code extensions (MCP servers, skills)
- OpenCode/Codex integrations
- Cross-agent tools (Browser Use, Firecrawl, FAL)

Write notes to: 04 - Plugins/ (use plugin-profile template from AGENTS.md)

RULES:
- Use UNIQUE timestamps per note (increment: 2000, 2001, 2002...)
- Every note must link to at least 2 MOCs: [[MOC-Plugin-Ecosystem]] and [[MOC-Trending-Agents]]
- Do NOT link to specific agent notes yet (cross-linking happens in merge)
- After writing notes, create manifest: write_file("08 - Projects/scan-manifests/stream-b-$(date +%Y%m%d%H%M).json", ...)
- Manifest format: JSON array of {"file": "...", "title": "...", "type": "plugin", "agents": ["Claude Code"]}

After manifest: cd "${HOME}/repository/git/ai-matrix-trends" && git add -A && git commit -m "Daily scan: plugin ecosystem $(date +%Y-%m-%d)" && git push
```

### Stream C: Architecture Patterns
```
Goal: Find 2-3 emerging architecture patterns.
Focus areas:
- MCP Protocol developments
- Multi-agent orchestration patterns
- Context engineering (RAG, summarization, curation)
- Tool-calling patterns and guardrails

Write notes to: 05 - Architecture/ (use architecture-pattern template from AGENTS.md)

RULES:
- Use UNIQUE timestamps per note (increment: 2000, 2001, 2002...)
- Every note must link to at least 2 other notes in the SAME folder
- Do NOT link to notes in other folders yet (cross-linking happens in merge)
- After writing notes, create manifest: write_file("08 - Projects/scan-manifests/stream-c-$(date +%Y%m%d%H%M).json", ...)
- Manifest format: JSON array of {"file": "...", "title": "...", "type": "architecture", "examples": ["Claude Code"]}

After manifest: cd "${HOME}/repository/git/ai-matrix-trends" && git add -A && git commit -m "Daily scan: architecture patterns $(date +%Y-%m-%d)" && git push
```

### Stream D: Use Cases
```
Goal: Find 2-3 real-world use cases or workflows.
Focus areas:
- Agent + plugin combinations
- Config snippets and setup patterns
- Integration tutorials
- Workflow automation examples

Write notes to: 06 - Use Cases/ (use atomic-note template from AGENTS.md)

RULES:
- Use UNIQUE timestamps per note (increment: 2000, 2001, 2002...)
- Every note must link to at least 2 MOCs: [[MOC-Plugin-Ecosystem]] and [[MOC-Architecture-Patterns]]
- Do NOT link to specific notes yet (cross-linking happens in merge)
- After writing notes, create manifest: write_file("08 - Projects/scan-manifests/stream-d-$(date +%Y%m%d%H%M).json", ...)
- Manifest format: JSON array of {"file": "...", "title": "...", "type": "workflow", "agents": ["Claude Code"], "plugins": ["Firecrawl"]}

After manifest: cd "${HOME}/repository/git/ai-matrix-trends" && git add -A && git commit -m "Daily scan: use cases $(date +%Y-%m-%d)" && git push
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

Search for broken links and fix them:
```bash
search_files(pattern="\\[\\[.*\\]\\]", target="content", path="03 - Agents", file_glob="*.md")
search_files(pattern="\\[\\[.*\\]\\]", target="content", path="04 - Plugins", file_glob="*.md")
search_files(pattern="\\[\\[.*\\]\\]", target="content", path="05 - Architecture", file_glob="*.md")
search_files(pattern="\\[\\[.*\\]\\]", target="content", path="06 - Use Cases", file_glob="*.md")
```

For each `[[link]]` found, check if the target file exists. If not:
- Search for the correct filename: `search_files(pattern="*link*", target="files", path=".")`
- Update the wikilink to match the actual filename

### Step 3: Add Cross-Stream Links Using Manifests

Use the manifest data to add intelligent cross-links:

**Agents → Plugins:** For each agent, check which plugins list it in their `agents` field. Add those plugin links to the agent note.

**Plugins → Agents:** For each plugin, add links to the agents it supports (from manifest `agents` field).

**Architecture → Agents:** For each pattern, add links to agents in its `examples` field.

**Use Cases → Agents/Plugins:** For each use case, add links to agents and plugins listed in its manifest.

**Use read_file() + patch() to update existing notes with new links.**

### Step 4: Update MOCs with New Notes

Open each MOC file and add new notes from manifests to the appropriate cluster:
- `07 - Structure/MOC-Trending-Agents.md` — add new agents from stream-a manifest
- `07 - Structure/MOC-Plugin-Ecosystem.md` — add new plugins from stream-b manifest
- `07 - Structure/MOC-Architecture-Patterns.md` — add new patterns from stream-c manifest

Format:
```markdown
- [[YYYYMMDDHHMM - Note Title]] — [one-line summary from manifest]
```

### Step 5: Update README

1. Update **Trending Agents** table — add new agents from stream-a manifest with stars/description
2. Update **Top Plugins & Extensions** — add new plugins from stream-b manifest
3. Update **Architecture Patterns** — add new patterns from stream-c manifest
4. Update **Configuration Snippets** — add new use case links from stream-d manifest
5. Update **Trend Radar** — move items between heating/stable/emerging as needed
6. Update `Last refreshed: YYYY-MM-DD` at the bottom

### Step 6: Verify Minimum Link Count

Every note must have at least 2 working outbound links. Run:
```bash
grep -c "\\[\\[" "03 - Agents/"*.md
grep -c "\\[\\[" "04 - Plugins/"*.md
grep -c "\\[\\[" "05 - Architecture/"*.md
grep -c "\\[\\[" "06 - Use Cases/"*.md
```

If any note has fewer than 2 links, add more.

### Step 7: Final Commit and Push

```bash
cd "${HOME}/repository/git/ai-matrix-trends"
git add -A
git commit -m "Daily scan: cross-links, MOCs, README update $(date +%Y-%m-%d)" || echo "Nothing to commit"
git push
```

### Step 8: Cleanup

Remove old manifest files from previous runs (keep current):
```bash
# Remove manifests older than today
find "08 - Projects/scan-manifests" -name "*.json" ! -name "*$(date +%Y%m%d)*" -delete
```

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
