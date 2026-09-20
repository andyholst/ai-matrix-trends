# AI Matrix Trends — Daily Scan Instructions

**CRITICAL: The daily scan runs in 4 separate cron jobs (stages). Each stage runs after the previous one completes.**

---

## Stage 1: Research (20:00) — `stage-1-research.sh`

Launches 4 parallel research sub-agents via `delegate_task`.

**SUB-AGENTS: ALWAYS USE FULL FILENAMES FOR WIKILINKS.**
- ✅ Correct: `[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)`
- ❌ Wrong: `[202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)`

### Stream A: Agents (Goal: 5 new agents)
Research trending AI coding agents.

### Stream B: Plugins (Goal: 50+ plugins for ALL major agents)
CRITICAL: Research plugins/extensions for EACH of these 50+ major agents:
- Claude Code, OpenCode, Cursor, Codex, Windsurf, Aider, Gemini CLI
- GitHub Copilot, Kilo Code, RooCode, JetBrains Junie, Hermes Agent

For EACH agent, search:
- web_search("best [agent name] plugins 2026")
- web_search("[agent name] MCP servers 2026")
- web_search("[agent name] extensions 2026")

Each plugin note MUST have:
```
## Compatibility
**Agent:** [202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md), [202609200759 - Hermes Agent](./03%20-%20Agents/202609200759%20-%20Hermes%20Agent.md)
agents: [claude-code, hermes, opencode]
```

### Stream C: Architecture (Goal: 3 patterns)
### Stream D: Use Cases (Goal: 3 use cases)

---

## Stage 2: Link Resolution (20:30) — `stage-2-links.sh`

1. `python3 scripts/resolve_wikilinks.py`
2. `python3 scripts/fix_all_links.py`
3. `python3 scripts/verify-vault.py`

---

## Stage 3: Scoring (20:45) — `stage-3-scoring.sh`

4. `python3 scripts/aggregate-trends.py`
5. `python3 scripts/collect_agent_plugins.py`

---

## Stage 4: Indexes & Commit (21:00) — `stage-4-indexes.py`

6. `python3 scripts/update-mocs.py`
7. `python3 scripts/update-plugin-master-index.py`
8. `python3 scripts/update-agent-master-index.py`
9. `python3 scripts/update_readme.py`
10. `python3 scripts/fix-master-index-links.py`
11. `python3 scripts/ci/fix-links-relative.py` (safety net: rewrite vault-root-style links to file-relative)
12. `python3 scripts/verify-vault.py`
13. `git add -A && git commit -m 'Daily scan' && git push`

**NEVER skip any script. NEVER change the order. NEVER delete files.**

**Link rules (CRITICAL):** All links are standard Markdown `[title](path)` — never
`[[wikilinks]]`. Paths are FILE-RELATIVE (same as GitHub): from a note in a
subfolder, use `../03%20-%20Agents/...` to reach another folder. See
"Link Verification" in AGENTS.md.
