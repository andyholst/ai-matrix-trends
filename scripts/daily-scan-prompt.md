# AI Matrix Trends — Daily Scan Instructions

**CRITICAL: Run scripts IN ORDER. NEVER delete files. Sub-agents: USE FULL FILENAMES for all wikilinks.**

---

## Pre-Scan Setup

`skill_view(name="obsidian")`
Read templates, MOCs, README

**CRITICAL: Before writing ANY note, list existing files to avoid timestamp collisions:**
```
search_files(pattern="*", target="files", path="03 - Agents")
search_files(pattern="*", target="files", path="04 - Plugins")
search_files(pattern="*", target="files", path="05 - Architecture")
search_files(pattern="*", target="files", path="06 - Use Cases")
```
Use the HIGHEST existing timestamp + 10 to avoid collisions.

---

## Parallel Research Streams

Launch 4 streams via `delegate_task`.

**SUB-AGENTS: ALWAYS USE FULL FILENAMES FOR WIKILINKS.**
- ✅ Correct: `[[202609202000 - Claude Code]]`
- ❌ Wrong: `[[Claude Code]]`
- NEVER use short names. The merge step is eliminated — agents must link correctly from the start.

**SUB-AGENTS: CHECK FOR EXISTING FILES BEFORE WRITING.**
If a note already exists for a topic, UPDATE it instead of creating a duplicate.

### Stream A: Agents
```
Goal: 5 agents | 03 - Agents/ | Timestamps: USE search_files to find max existing + 10
Frontmatter: id, created, tags, links (2+ full filename links)
Body: ## Related with [[FULL Filename]]
```

### Stream B: Plugins
```
Goal: 10+ plugins | 04 - Plugins/ | Timestamps: USE search_files to find max existing + 10
Frontmatter: id, created, tags, links (2+ full filename links)
Body: ## Related with [[FULL Filename]]
```

### Stream C: Architecture
```
Goal: 3 patterns | 05 - Architecture/ | Timestamps: USE search_files to find max existing + 10
Frontmatter: id, created, tags, links (2+ full filename links)
```

### Stream D: Use Cases
```
Goal: 3 use cases | 06 - Use Cases/ | Timestamps: USE search_files to find max existing + 10
Frontmatter: id, created, tags, links (2+ full filename links)
```

---

## Post-Scan Merge (MANDATORY ORDER)

1. `cd ~/repository/git/ai-matrix-trends && python3 scripts/resolve_wikilinks.py`
2. `cd ~/repository/git/ai-matrix-trends && python3 scripts/fix_all_links.py`
3. `cd ~/repository/git/ai-matrix-trends && python3 scripts/aggregate-trends.py`
4. `cd ~/repository/git/ai-matrix-trends && python3 scripts/collect_agent_plugins.py`
5. `cd ~/repository/git/ai-matrix-trends && python3 scripts/update_readme.py`
6. `cd ~/repository/git/ai-matrix-trends && python3 scripts/verify-vault.py`
7. `cd ~/repository/git/ai-matrix-trends && python3 scripts/update-mocs.py`
8. `cd ~/repository/git/ai-matrix-trends && python3 scripts/update-plugin-master-index.py`
9. `cd ~/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan' && git push`
