# AI Matrix Trends — Daily Scan Instructions

**CRITICAL: Sub-agents NEVER delete files. NEVER add links to frontmatter. Use ONLY short names in ## Related.**

---

## Pre-Scan Setup

`skill_view(name="obsidian")`
Read templates, MOCs, README

---

## Parallel Research Streams

### Stream A: Agents
```
Goal: 5 agents | 03 - Agents/ | Timestamps: 10-14
Frontmatter: id, created, tags (NO links field)
Body: ## Related with [[Short Names]]
Manifest: stream-a-UNIQUE.json
```

### Stream B: Plugins
```
Goal: 10 plugins | 04 - Plugins/ | Timestamps: 20-29
Frontmatter: id, created, tags (NO links field)
Body: ## Related with [[Short Names]]
Manifest: stream-b-UNIQUE.json
```

### Stream C: Architecture
```
Goal: 3 patterns | 05 - Architecture/ | Timestamps: 30-32
Frontmatter: id, created, tags (NO links field)
Manifest: stream-c-UNIQUE.json
```

### Stream D: Use Cases
```
Goal: 3 use cases | 06 - Use Cases/ | Timestamps: 40-42
Frontmatter: id, created, tags (NO links field)
Manifest: stream-d-UNIQUE.json
```

---

## Post-Scan Merge (MANDATORY ORDER)

1. `cd ~/repository/git/ai-matrix-trends && python3 scripts/fix_all_links.py`
2. `cd ~/repository/git/ai-matrix-trends && python3 scripts/aggregate-trends.py`
3. **Agent updates README** with Trend Radar top 5
4. `cd ~/repository/git/ai-matrix-trends && python3 scripts/verify-vault.py`
5. `cd ~/repository/git/ai-matrix-trends && git add -A && git commit -m 'Daily scan' && git push`
