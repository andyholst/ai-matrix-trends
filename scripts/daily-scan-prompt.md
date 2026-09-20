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
3. Initial commit checkpoint:
   ```bash
   cd "${HOME}/repository/git/ai-matrix-trends"
   git add -A
   git commit -m "Daily scan: pre-scan state checkpoint" || echo "Nothing to commit"
   git push
   ```

---

## Parallel Research Streams

Launch 4 parallel research streams using `delegate_task`:

### Stream A: Agent Profiles
```
Goal: Find 3-5 trending AI coding agents.
Focus areas:
- Claude Code, OpenCode, Hermes, Codex, Cursor, Cline, Aider, Windsurf, Pi
- New releases, GitHub star growth, HN/Reddit/Twitter mentions
- Compare features, pricing, architecture

Write notes to: 03 - Agents/ (use agent-profile template from AGENTS.md)

After writing: cd "${HOME}/repository/git/ai-matrix-trends" && git add -A && git commit -m "Daily scan: agent profiles $(date +%Y-%m-%d)" && git push
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

After writing: cd "${HOME}/repository/git/ai-matrix-trends" && git add -A && git commit -m "Daily scan: plugin ecosystem $(date +%Y-%m-%d)" && git push
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

After writing: cd "${HOME}/repository/git/ai-matrix-trends" && git add -A && git commit -m "Daily scan: architecture patterns $(date +%Y-%m-%d)" && git push
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

After writing: cd "${HOME}/repository/git/ai-matrix-trends" && git add -A && git commit -m "Daily scan: use cases $(date +%Y-%m-%d)" && git push
```

---

## Post-Scan Merge (after all streams complete)

1. **Deduplicate** — merge notes on the same topic; prefer updating existing notes over creating duplicates.
2. **Cross-link** — every note must link to at least 2 existing notes via `[[wikilinks]]`.
3. **Update MOCs** — add new notes to relevant Maps of Content in `07 - Structure/`.
4. **Update README** — refresh trend tables, radar, and wikilinks in `README.md`.
5. **Final commit and push:**
   ```bash
   cd "${HOME}/repository/git/ai-matrix-trends"
   git add -A
   git commit -m "Daily scan: merge, MOCs, README update $(date +%Y-%m-%d)" || echo "Nothing to commit"
   git push
   ```

---

## Rules

- One idea per note. Split compound topics.
- Own words — synthesize, never copy-paste. Use blockquotes with attribution for sources.
- Timestamp prefix filenames: `YYYYMMDDHHMM - Title.md`
- Frontmatter must include: `id`, `created`, `tags`, `links`
- Minimum 2 outbound links per note
- Never delete existing content — split, merge, or add `replaced-by` frontmatter
- If a note already exists for a topic, UPDATE it rather than creating duplicate

---

*Vault path: ${HOME}/repository/git/ai-matrix-trends*
*Agent profile: ai-matrix-trends*
