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

### Stream A: Agents (Goal: 5 new agents)
Research trending AI coding agents. Search GitHub, Hacker News, Reddit for new releases.

### Stream B: Plugins (Goal: 50+ plugins for ALL major agents)
CRITICAL: Research plugins/extensions for EACH of these 50+ major agents:
- Claude Code, OpenCode, Cursor, Codex, Windsurf, Aider, Gemini CLI
- GitHub Copilot, Kilo Code, RooCode, JetBrains Junie, Hermes Agent
- And any other trending agents found in Stream A

For EACH agent, search:
- web_search("best [agent name] plugins 2026")
- web_search("[agent name] MCP servers 2026")
- web_search("[agent name] extensions 2026")

Each plugin note MUST have:
```
## Compatibility
**Agent:** [[202609202000 - Claude Code]], [[202609200759 - Hermes Agent]]
agents: [claude-code, hermes, opencode]
```

### Stream C: Architecture (Goal: 3 patterns)
Research emerging architecture patterns.

### Stream D: Use Cases (Goal: 3 use cases)
Research real-world workflows.

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
9. `cd ~/repository/git/ai-matrix-trends && python3 scripts/update-agent-master-index.py`
10. `cd ~/repository/git/ai-matrix-trends && python3 scripts/fix-master-index-links.py`
11. `cd ~/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan' && git push`
