# AI Matrix Trends — Agent Operating Manual

## Purpose

This is an Obsidian vault for **AI Matrix Trends**, a knowledge system tracking trends, signals, and analysis in the AI/ML ecosystem. The agent (Hermes) operates within this vault using the **Zettelkasten method** — every insight is an atomic note, richly linked, progressively refined into higher-order structure.

## Vault Philosophy

1. **One idea per note.** Every note captures a single concept, signal, trend, or data point. Splitting is always better than combining.
2. **Own words.** Notes are written in the agent's own synthesis — never raw copy-paste. If a source must be preserved, embed it as a blockquote with attribution.
3. **Dense linking.** Every note should link to at least 2–3 related notes. The web of links is the value.
4. **Progressive refinement.** Notes are living — they get revisited, restructured, expanded. This is expected and encouraged.
5. **Evergreen over ephemeral.** Permanent notes aim to be timeless; time-sensitive material lives in the inbox/fleeting layer with a clear expiry path.

---

## Vault Structure

```
ai-matrix-trends/
├── .obsidian/              # Obsidian vault config (do NOT edit manually)
├── 00 - Inbox/             # Raw, unprocessed observations (triage daily)
├── 01 - Fleeting/          # Quick thoughts, reminders, half-baked ideas
├── 02 - Literature/        # Source-derived notes (papers, articles, talks)
├── 03 - Permanent/         # Processed atomic evergreen notes (the core)
├── 04 - Structure/         # Maps of Content (MOCs), indexes, dashboards
├── 05 - Projects/          # Active project-specific notes
├── 99 - Attachments/       # Images, PDFs, exported files
├── AGENTS.md               # This file
└── LICENSE
```

### Folder Roles

| Folder | Purpose | Retention |
|--------|---------|-----------|
| `00 - Inbox` | Drop zone for new signals. Agent triages here first. | Processed into Permanent/Fleeting within a session |
| `01 - Fleeting` | Quick capture, reminders, half-formed ideas. | Either promoted to Permanent or archived |
| `02 - Literature` | Notes tied to a specific source (paper, blog, talk). | Source + own synthesis, permanently kept |
| `03 - Permanent` | The vault's core. Atomic, evergreen, self-contained notes. | Kept indefinitely, continuously refined |
| `04 - Structure` | Maps of Content that organize Permanent notes into themes. | Updated as the vault grows |
| `05 - Projects` | Time-bound work (e.g., "analyze Q3 model releases"). | Archived or deleted after project closes |
| `99 - Attachments` | Binary assets, images, PDFs. | Linked from notes, kept as needed |

---

## Note Naming Convention

Atomic notes use a **timestamp prefix** for sortability and uniqueness:

```
YYYYMMDDHHMM - Descriptive title in sentence case.md
```

Examples:
- `202609201430 - Mixture of Experts architecture variants.md`
- `202609201445 - Llama 4 benchmark results vs GPT-5.md`
- `202609201500 - Anthropic constitutional AI method evolution.md`

**Why timestamp + sentence case?** Timestamps give chronological context and prevent filename collisions. Sentence case titles are readable and wiki-link friendly.

---

## Atomic Note Template

Every permanent note follows this structure:

```markdown
---
id: 202609201430
created: 2026-09-20T14:30:00+02:00
tags:
  - trend
  - architecture
aliases:
  - MoE variants
links:
  - "[[202609201400 - Mixture of Experts foundational paper]]"
  - "[[202609201415 - Sparse vs dense model tradeoffs]]"
---

# Mixture of Experts Architecture Variants

## Core Idea
[One sentence capturing the single idea]

## Details
[2–4 paragraphs: what it is, why it matters, key differentiators]

## Implications
[So what? What does this enable or change?]

## Related
- [[202609201400 - Mixture of Experts foundational paper]]
- [[202609201415 - Sparse vs dense model tradeoffs]]

## Sources
- [Source Name](url) (if applicable)
```

### Field Definitions

| Field | Purpose |
|-------|---------|
| `id` | Timestamp ID matching filename |
| `created` | ISO 8601 creation date |
| `tags` | Flat tag list — no hierarchy. Use kebab-case |
| `aliases` | Alternative titles Obsidian can match via `[[wikilinks]]` |
| `links` | Explicit list of strongly related permanent notes |
| `Core Idea` | The one-liner — if you can only read one sentence |
| `Details` | The meat — own words, blockquotes for source material |
| `Implications` | Forward-looking — why this matters |
| `Related` | Wikilinks to other permanent notes |
| `Sources` | Attribution when synthesizing external content |

---

## Tag Taxonomy (controlled vocabulary)

Use these tags consistently. Add new ones only when a theme recurs.

### Type Tags
- `trend` — a directional shift in the AI landscape
- `signal` — a data point that may indicate a trend
- `tool` — a software, library, or platform
- `paper` — academic research output
- `model` — a specific ML model
- `method` — a technique, algorithm, or approach
- `company` — organization-specific activity
- `person` — notable individual
- `event` — conference, announcement, milestone

### Status Tags
- `seedling` — new, underdeveloped note (fleeting → permanent transition)
- `evergreen` — mature, reviewed, stable
- `refactoring` — currently being restructured
- `deprecated` — superseded or no longer relevant (keep for traceability)

### Domain Tags
- `architecture` — model architecture topics
- `training` — training methods, data, compute
- `inference` — deployment, optimization, serving
- `alignment` — safety, RLHF, constitutional AI
- `multimodal` — vision, audio, video models
- `agentic` — AI agents, tool use, planning
- `regulation` — policy, governance, compliance
- `benchmark` — evaluation, leaderboards, metrics

---

## Map of Content (MOC) Rules

Structure notes in `04 - Structure/` organize permanent notes into thematic clusters.

### MOC Template

```markdown
---
tags:
  - moc
---

# MOC: [Theme Name]

## Overview
[2 sentences on what this map covers]

## Key Notes
- [[YYYYMMDDHHMM - Note title]] — [one-line summary]
- [[YYYYMMDDHHMM - Note title]] — [one-line summary]

## Clusters
### Sub-theme A
- [[note-link-1]]
- [[note-link-2]]

### Sub-theme B
- [[note-link-3]]

## Open Questions
- What is the relationship between X and Y?

## Related MOCs
- [[MOC: Related theme]]
```

### MOC Maintenance

- Create a new MOC when a theme has **5+** related permanent notes
- MOCs should be updated when a new note joins their cluster
- Each permanent note should link to at least one MOC
- MOCs link to each other where themes intersect

---

## Agent Workflow

### When Adding New Knowledge

1. **Ingest** → Drop raw observation into `00 - Inbox/` with a timestamp-prefixed filename
2. **Triagate** → Determine if this is fleeting, literature, or permanent material
3. **Atomize** → Split compound ideas into separate notes (one idea each)
4. **Link** → Every new note must link to at least 2 existing notes (or note why it's an orphan)
5. **Tag** → Apply controlled vocabulary tags
6. **MOC update** → Add to relevant Map of Content if the theme exists; create new MOC if threshold reached
7. **Refactor** → After batch ingestion, revisit earlier notes to strengthen links, merge duplicates, or split oversized notes

### Refactoring Rules

Refactoring is expected. When restructuring:

- **Never delete content** — split into new notes or move to `01 - Fleeting/` if it loses relevance
- **Preserve wikilinks** — if a filename changes, update all `[[links]]` across the vault
- **Update MOCs** — rename or re-point any MOC references to moved notes
- **Leave traces** — if a note is superseded, add a `replaced-by: [[new-note]]` frontmatter field

### When to Create vs Link

| Situation | Action |
|-----------|--------|
| New concept, no existing note | Create new atomic note |
| Related to 1–2 existing notes | Link to them |
| Related to 5+ notes | Create/update a MOC |
| Repeats existing note | Merge — add new info to existing, delete duplicate |
| Part of a larger trend | Link to the trend note + add trend as tag |
| A correction to existing note | Edit the note, add update timestamp in frontmatter |

---

## Obsidian Configuration

The `.obsidian/` directory should contain:

```json
// .obsidian/app.json
{
  "alwaysUpdateLinks": true,
  "newLinkMode": "relative",
  "useMarkdownLinks": false,
  "attachmentFolderPath": "99 - Attachments",
  "newFileLocation": "folder",
  "newFileFolderPath": "00 - Inbox"
}
```

```json
// .obsidian/templates/core.json
{
  "templateFolderPath": ".obsidian/templates"
}
```

---

## Output Expectations

When the agent produces work in this vault:

1. **All notes are atomic** — no note exceeds what one idea needs
2. **Every note is linked** — minimum 2 outbound links for permanent notes
3. **Frontmatter is complete** — id, created, tags, links all populated
4. **Sources are attributed** — blockquotes + links for any external material
5. **MOCs are current** — no orphan notes in clusters of 5+
6. **Timestamps are accurate** — creation dates reflect when the note was written, not the source date

The vault is a living system. Small, frequent, well-linked notes beat large, infrequent ones. Refactoring is growth.
