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
Goal: 3-5 new agents | Folder: 03 - Agents/
Timestamps: 2026092010, 2026092011, etc.
Frontmatter (NO links):
---
id: 2026092010
created: 2026-09-20T10:00:00+02:00
tags:
  - agent
  - cli
---
Body ## Related: [[Claude Code]], [[Aider]] (short names)
Manifest: 08 - Projects/scan-manifests/stream-a-UNIQUE.json
Git: commit + push
```

### Stream B: Plugins (minutes 20-24)
```
Goal: 3-5 new plugins | Folder: 04 - Plugins/
Timestamps: 2026092020, 2026092021, etc.
Frontmatter (NO links):
---
id: 2026092020
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - mcp
---
Body ## Related: [[MOC-Plugin-Ecosystem]], [[MOC-Trending-Agents]]
Manifest: 08 - Projects/scan-manifests/stream-b-UNIQUE.json
Git: commit + push
```

### Stream C: Architecture (minutes 30-32)
```
Goal: 2-3 new patterns | Folder: 05 - Architecture/
Timestamps: 2026092030, 2026092031, etc.
Frontmatter (NO links):
---
id: 2026092030
created: 2026-09-20T30:00:00+02:00
tags:
  - architecture
  - mcp
---
Body ## Related: [[MCP Protocol]], [[Claude Code]]
Manifest: 08 - Projects/scan-manifests/stream-c-UNIQUE.json
Git: commit + push
```

### Stream D: Use Cases (minutes 40-42)
```
Goal: 2-3 new use cases | Folder: 06 - Use Cases/
Timestamps: 2026092040, 2026092041, etc.
Frontmatter (NO links):
---
id: 2026092040
created: 2026-09-20T40:00:00+02:00
tags:
  - workflow
  - config
---
Body ## Related: [[MOC-Plugin-Ecosystem]], [[MOC-Architecture-Patterns]]
Manifest: 08 - Projects/scan-manifests/stream-d-UNIQUE.json
Git: commit + push
```

---

## Post-Scan Merge (MANDATORY — RUN IN ORDER)

### Step 1: Run Link Fixer
```bash
cd ~/repository/git/ai-matrix-trends && python3 scripts/fix-links.py
```

### Step 2: Update MOCs
```bash
cd ~/repository/git/ai-matrix-trends && python3 scripts/update-mocs.py
```

### Step 3: Agent Updates README with Meaningful Content

**After the scripts run, YOU must update README.md with meaningful content:**

1. Read each new note created by the streams
2. Extract key information (trending status, category, importance)
3. Update README Trend Radar tables with new findings:
   - Add to Heating Up 🔥 for rapid growth/new tools
   - Add to Stable 📈 for established patterns
   - Add to Emerging 🌱 for early signals
4. Update the Trend Radar description to reflect current state
5. Update the `Last refreshed: YYYY-MM-DD` date
6. Format all links as Markdown: `[text](./path.md)`

### Step 4: Verify Vault
```bash
cd ~/repository/git/ai-matrix-trends && python3 scripts/verify-vault.py
```

### Step 5: Agent Verification of README

**YOU must verify README looks correct:**
1. Read README.md
2. Check Trend Radar tables have correct entries from Step 3
3. Check all Markdown links resolve (decode %20 before checking)
4. Verify no duplicate entries
5. Verify formatting is clean and consistent
6. Fix any issues found

### Step 6: Commit and Push
```bash
cd ~/repository/git/ai-matrix-trends && git add -A && git commit -m "Daily scan: cross-links, MOCs, README" && git push
```

---

## Rules

- Sub-agents: NEVER write `links:` in frontmatter
- Merge step: ALWAYS runs Python scripts in order FIRST
- Main agent: ALWAYS updates README with meaningful content AFTER scripts
- Main agent: ALWAYS verifies README looks correct after updating
- Every note MUST end with 2+ working frontmatter wikilinks
- Zero orphans in body text

*Vault path: ${HOME}/repository/git/ai-matrix-trends*
*Agent profile: ai-matrix-trends*
