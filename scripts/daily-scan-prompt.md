# AI Matrix Trends — Daily Scan Instructions

## Pre-Scan Setup

1. `skill_view(name="obsidian")`
2. Read all 4 templates from `.obsidian/templates/`
3. Read existing MOCs and README
4. Initial commit checkpoint

---

## Parallel Research Streams

Launch 4 streams via `delegate_task`.

**CRITICAL RULE FOR SUB-AGENTS:**
- **DO NOT add `links:` field to frontmatter**
- **ONLY put links in `## Related` section at bottom using short names like `[[Claude Code]]`**
- The merge step will resolve short names to actual filenames

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

## Post-Scan Merge (MANDATORY)

### Step 1: Read Manifests
`search_files(pattern="stream-*.json", target="files", path="08 - Projects/scan-manifests")`

### Step 2: Add Frontmatter Links to ALL New Notes

**Use execute_code to resolve links from actual files:**

```python
import os, re

# Build title -> filename map
title_map = {}
for root, dirs, files in os.walk('${HOME}/repository/git/ai-matrix-trends'):
    if '/.git' in root: continue
    for f in files:
        if f.endswith('.md'):
            fname = f.replace('.md', '')
            if ' - ' in fname:
                title = fname.split(' - ', 1)[1]
                title_map[title.lower().replace(' ', '-').replace("'", "")] = fname

# Add MOCs
title_map['moc-trending-agents'] = 'MOC-Trending-Agents'
title_map['moc-plugin-ecosystem'] = 'MOC-Plugin-Ecosystem'
title_map['moc-architecture-patterns'] = 'MOC-Architecture-Patterns'

# Add short names
title_map['claude-code'] = '202609202000 - Claude Code'
title_map['codex'] = '202609202000 - Codex'
title_map['cursor'] = '202609202000 - Cursor'
title_map['opencode'] = '202609200758 - OpenCode'
title_map['hermes'] = '202609200759 - Hermes Agent'

# For each new note:
# 1. Read note, find ## Related section
# 2. Extract short names from [[...]]
# 3. Resolve against title_map
# 4. Add links: field to frontmatter with 2+ actual filename wikilinks
# 5. Fix body wikilinks the same way
```

**Then use patch() to add frontmatter links to EVERY new note.**

### Step 3: Fix Orphan Wikilinks
For EVERY note in ALL folders, check all `[[...]]` resolve to existing files. Fix with `patch()`.

### Step 4: Add Cross-Stream Links
From manifests:
- Agents → Plugins (from plugin `agents` field)
- Plugins → Agents (same)
- Architecture → Agents (from pattern `examples` field)

### Step 5: Update MOCs + Master Indexes
- MOC-Trending-Agents.md
- MOC-Plugin-Ecosystem.md
- MOC-Architecture-Patterns.md
- 05 - Architecture/00 - AI Architecture Master Index.md
- 04 - Plugins/00 - Plugin Master Index.md

### Step 6: Update README
- Convert ALL `[[wikilinks]]` to `[text](./path.md)` Markdown
- Update Trend Radar
- Create atomic notes in 09 - Trend Radar/ folders
- Update date

### Step 7: Final Commit
`terminal(command="cd ${HOME}/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan: cross-links, MOCs, README' && git push")`

### Step 8: Cleanup + Validate
Remove old manifests. Verify 5 random notes.

---

## Rules
- Sub-agents: NEVER write `links:` in frontmatter
- Merge step: ALWAYS uses Python to resolve links from actual folder contents
- Every note MUST end with 2+ working frontmatter wikilinks
- Zero orphans in body text

*Vault path: ${HOME}/repository/git/ai-matrix-trends*
