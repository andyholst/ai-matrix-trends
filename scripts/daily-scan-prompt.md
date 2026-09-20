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
- **ONLY put links in `## Related` section at bottom of note using short names like `[[Claude Code]]`**
- The merge step will resolve short names to actual filenames

### Stream A: Agents (minutes 10-14)
```
Goal: 3-5 new agents | Folder: 03 - Agents/
Timestamps: 2026092010, 2026092011, 2026092012, etc.

Frontmatter (NO links field):
---
id: 2026092010
created: 2026-09-20T10:00:00+02:00
tags:
  - agent
  - cli
---

Body ## Related: [[Name 1]], [[Name 2]] (short names only)
Manifest: 08 - Projects/scan-manifests/stream-a-UNIQUE.json
Git: commit + push
```

### Stream B: Plugins (minutes 20-24)
```
Goal: 3-5 new plugins | Folder: 04 - Plugins/
Timestamps: 2026092020, 2026092021, etc.

Frontmatter (NO links field):
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

Frontmatter (NO links field):
---
id: 2026092030
created: 2026-09-20T30:00:00+02:00
tags:
  - architecture
  - mcp
---

Body ## Related: [[Pattern 1]], [[Pattern 2]]
Manifest: 08 - Projects/scan-manifests/stream-c-UNIQUE.json
Git: commit + push
```

### Stream D: Use Cases (minutes 40-42)
```
Goal: 2-3 new use cases | Folder: 06 - Use Cases/
Timestamps: 2026092040, 2026092041, etc.

Frontmatter (NO links field):
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

## Post-Scan Merge (MANDATORY — after all streams complete)

### Step 1: Read Manifests
```
search_files(pattern="stream-*.json", target="files", path="08 - Projects/scan-manifests")
```

### Step 2: Add Frontmatter Links to ALL New Notes

**Use execute_code to resolve links from actual files:**

```python
import os, re

# Build file map
file_map = {}
for root, dirs, files in os.walk('${HOME}/repository/git/ai-matrix-trends'):
    if '/.git' in root: continue
    for f in files:
        if f.endswith('.md'):
            fname = f.replace('.md', '')
            file_map[fname.lower()] = fname
            if ' - ' in fname:
                no_ts = fname.split(' - ', 1)[1].lower().replace(' ', '-')
                file_map[no_ts] = fname

# Manual mappings
file_map.update({
    'cursor': '202609202000 - Cursor',
    'windsurf': '202609200800 - Windsurf',
    'opencode': '202609200758 - OpenCode',
    'hermes': '202609200759 - Hermes Agent',
    'hermes-agent': '202609200759 - Hermes Agent',
    'claude-code': '202609202000 - Claude Code',
    'codex': '202609202000 - Codex',
    'openai-codex': '202609202000 - Codex',
    'mcp-proxy-aggregator-pattern': '202609202000 - MCP Proxy Aggregator Pattern',
    'context-engineering-long-horizon-agents': '202609202001 - Context Engineering for Long-Horizon Agents',
    'multi-agent-orchestration-patterns': '202609202002 - Multi-Agent Orchestration with Guardrail Layering',
    'chrome-devtools-mcp': '202609202011 - Chrome DevTools MCP',
    'mcp-server-ecosystem-explosion': '202609200100 - MCP Server Ecosystem Explosion',
    'hermes-jev': '202609202000 - Jev Agent Router',
})

# For each new note:
# 1. Read note
# 2. Find ## Related section
# 3. Extract short names
# 4. Resolve against file_map
# 5. Add links: field to frontmatter
# 6. Also fix all body wikilinks
```

### Step 3: Update MOCs + Master Indexes
- `07 - Structure/MOC-Trending-Agents.md`
- `07 - Structure/MOC-Plugin-Ecosystem.md`
- `07 - Structure/MOC-Architecture-Patterns.md`
- `05 - Architecture/00 - AI Architecture Master Index.md`
- `04 - Plugins/00 - Plugin Master Index.md`

### Step 4: Update README
- Convert ALL `[[wikilinks]]` to `[text](./path.md)` Markdown
- Update Trend Radar
- Create atomic notes in `09 - Trend Radar/`
- Update date

### Step 5: Final Commit
```
terminal(command="cd ${HOME}/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan: cross-links, MOCs, README' && git push")
```

### Step 6: Cleanup + Validate
Remove old manifests. Verify 5 random notes have complete frontmatter.

---

## Rules

- Sub-agents: NEVER write `links:` in frontmatter
- Merge step: ALWAYS uses Python to resolve links from actual folder contents
- Every note MUST end with 2+ working frontmatter wikilinks
- Zero orphans in body text

*Vault path: ${HOME}/repository/git/ai-matrix-trends*
*Agent profile: ai-matrix-trends*
