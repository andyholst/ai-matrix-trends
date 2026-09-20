# AI Matrix Trends — Daily Scan Instructions

## Pre-Scan Setup

1. `skill_view(name="obsidian")`
2. Read all 4 templates from `.obsidian/templates/`
3. Read existing MOCs and README
4. Initial commit checkpoint

---

## Parallel Research Streams

Launch 4 streams via `delegate_task`.

**SUB-AGENTS: DO NOT ADD `links:` TO FRONTMATTER. Only use `## Related` section at bottom.**

### Stream A: Agents (minutes 10-14)
```
Goal: Find 5 NEW trending AI coding agents (not already in vault).
Folder: 03 - Agents/
Timestamps: 2026092010-2026092014

SEARCH QUERIES (run ALL):
1. web_search("trending AI coding agents 2026 new releases")
2. web_search("best new AI code assistant tools github stars")
3. web_search("Claude Code alternatives 2026")
4. web_search("new open source coding agent github")
5. web_search("AI pair programming tools new 2026")

EXTRACT: Name, GitHub stars, description, supported models, key features.
ONLY include agents with 1000+ stars or significant community buzz.
Do NOT include agents already in the vault.

Frontmatter (NO links):
---
id: 2026092010
created: 2026-09-20T10:00:00+02:00
tags:
  - agent
  - cli
---

Body ## Related: [[Agent 1]], [[Agent 2]] (short names)
Manifest: 08 - Projects/scan-manifests/stream-a-UNIQUE.json
Git: commit + push
```

### Stream B: Plugins (minutes 20-24)
```
Goal: Find 10 NEW plugins/extensions for EACH major agent (Claude Code, OpenCode, Hermes, Cursor, Codex).
Folder: 04 - Plugins/
Timestamps: 2026092020-2026092029

SEARCH QUERIES (run ALL):
1. web_search("best Claude Code MCP servers 2026")
2. web_search("Claude Code extensions plugins new")
3. web_search("OpenCode plugins ecosystem new")
4. web_search("Hermes AI agent plugins new")
5. web_search("Cursor IDE extensions AI coding")
6. web_search("Codex OpenAI plugins integrations")
7. web_search("MCP servers trending 2026")
8. web_search("AI coding agent browser automation tools")
9. web_search("Claude Code hooks CI/CD tools")
10. web_search("new AI developer tools september 2026")

EXTRACT: Name, supported agents, description, stars/installs, key features.
Include ONLY plugins not already in vault.
Aim for 10+ new plugins.

Frontmatter (NO links):
---
id: 2026092020
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - mcp
---

Body ## Related: [[Plugin 1]], [[Plugin 2]] (short names)
Manifest: 08 - Projects/scan-manifests/stream-b-UNIQUE.json
Git: commit + push
```

### Stream C: Architecture (minutes 30-32)
```
Goal: Find 3 NEW emerging architecture patterns.
Folder: 05 - Architecture/
Timestamps: 2026092030-2026092032

SEARCH QUERIES:
1. web_search("MCP protocol new patterns 2026")
2. web_search("multi-agent AI orchestration architecture")
3. web_search("context engineering long-horizon agents new")
4. web_search("AI agent safety guardrails patterns")

EXTRACT: Pattern name, description, adoption level, tradeoffs.

Frontmatter (NO links):
---
id: 2026092030
created: 2026-09-20T30:00:00+02:00
tags:
  - architecture
  - mcp
---

Body ## Related: [[Pattern 1]], [[Pattern 2]] (short names)
Manifest: 08 - Projects/scan-manifests/stream-c-UNIQUE.json
Git: commit + push
```

### Stream D: Use Cases (minutes 40-42)
```
Goal: Find 3 NEW real-world use cases.
Folder: 06 - Use Cases/
Timestamps: 2026092040-2026092042

SEARCH QUERIES:
1. web_search("Claude Code hooks CI/CD automation examples")
2. web_search("multi-server MCP orchestration enterprise workflows")
3. web_search("AI agent plugin combinations use cases 2026")

EXTRACT: Use case description, agents/plugins involved, benefits.

Frontmatter (NO links):
---
id: 2026092040
created: 2026-09-20T40:00:00+02:00
tags:
  - workflow
  - config
---

Body ## Related: [[Use Case 1]], [[Use Case 2]] (short names)
Manifest: 08 - Projects/scan-manifests/stream-d-UNIQUE.json
Git: commit + push
```

---

## Post-Scan Merge (MANDATORY — RUN IN ORDER)

### Step 1: Run Meta Tag Fixer
```bash
cd ~/repository/git/ai-matrix-trends && python3 scripts/fix_meta_tags.py
```

### Step 2: Run Link Fixer
```bash
cd ~/repository/git/ai-matrix-trends && python3 scripts/fix-links.py
```

### Step 3: Update MOCs
```bash
cd ~/repository/git/ai-matrix-trends && python3 scripts/update-mocs.py
```

### Step 4: Aggregate Trends
```bash
cd ~/repository/git/ai-matrix-trends && python3 scripts/aggregate-trends.py
```

### Step 5: Agent Updates README

**After scripts run, YOU must update README.md:**

1. Read new notes from all streams
2. Read trend-data.json for scored trends
3. Update Trend Radar tables:
   - **Heating Up 🔥**: Top 5 highest scored items (score >= 50)
   - **Stable 📈**: Next 5 items (score 20-49)
   - **Emerging 🌱**: Items with score < 20 but showing growth signals
4. Update agent/plugin/pattern tables with new entries
5. Format all links as: `[text](./path.md)`
6. Update `Last refreshed: YYYY-MM-DD`

### Step 6: Verify Vault
```bash
cd ~/repository/git/ai-matrix-trends && python3 scripts/verify-vault.py
```

### Step 7: Agent Verification of README
**YOU must verify:**
1. Trend Radar has correct top 5 entries per category
2. All Markdown links resolve
3. No duplicates
4. Scoring is reflected in descriptions
5. Proper formatting

### Step 8: Commit and Push
```bash
cd ~/repository/git/ai-matrix-trends && git add -A && git commit -m "Daily scan: fix links, update MOCs, README" && git push
```

---

## Rules

- Sub-agents: NEVER write `links:` in frontmatter
- Sub-agents: Run ALL search queries, get MAXIMUM results
- Merge step: ALWAYS runs scripts in order
- Main agent: ALWAYS updates README with scored trend data
- Every note MUST end with 2+ working frontmatter wikilinks
- Zero orphans in body text

*Vault path: ${HOME}/repository/git/ai-matrix-trends*
*Agent profile: ai-matrix-trends*
