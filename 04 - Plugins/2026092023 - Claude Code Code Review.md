---
id: 2026092023
created: 2026-09-20T23:00:00+02:00
tags:
  - plugin
  - claude-code
agents:
  - claude-code
  - opencode
  - cursor
  - codex
  - windsurf
  - aider
  - gemini-cli
  - github-copilot
  - kilo-code
  - roocode
  - jetbrains-junie
  - cline
  - hermes
---



# Claude Code Code Review

## Overview
The Code Review plugin is an official Claude Code extension that automates pull request review using multiple specialized agents running in parallel. It uses confidence-based scoring to filter false positives, ensuring only high-quality, actionable feedback is posted. Created by Boris Cherny at Anthropic, it is one of the most popular Claude Code plugins with 438,525+ installs on the Claude plugins marketplace.

## Key Features
- **Multi-agent architecture:** 4 parallel agents review from different perspectives
- **Confidence scoring:** Each issue scored 0-100; only issues ≥80 confidence are reported
- **CLAUDE.md compliance:** Agents check changes against repository guidelines
- **Bug detection:** Dedicated agent scans for obvious bugs in changes
- **Git history analysis:** Agent uses git blame and history for context
- **PR comment posting:** Optionally post reviews as GitHub PR comments
- **Smart skipping:** Automatically skips closed, draft, trivial, or already-reviewed PRs

## Commands
```
/code-review          # Run review (outputs to terminal)
/code-review --comment  # Post review as PR comment
```

## Installation
```bash
# Included with Claude Code - command is automatically available
# Or install from marketplace:
/plugin install code-review@claude-plugins-official
```

## How It Works
1. Checks if review is needed (skips closed, draft, trivial, or already-reviewed PRs)
2. Gathers relevant CLAUDE.md guideline files from the repository
3. Summarizes the pull request changes
4. Launches 4 parallel    - **Agents #1 & #2:** Audit for CLAUDE.md compliance
   - **Agent #3:** Scan for obvious bugs in changes
   - **Agent #4:** Analyze git blame/history for context-based issues
5. Scores each issue 0-100 for confidence level
6. Filters out issues below 80 confidence threshold
7. Outputs review (to terminal or as PR comment)

## Use Cases
- Automated PR review for teams using Claude Code
- Enforcing CLAUDE.md guidelines across contributions
- Catching bugs before human review
- Reducing PR review turnaround time

## Compatibility
- **Agent:** Claude Code
- **Requirements:** Git repository, GitHub CLI (`gh`) installed and authenticated
- **Optional:** CLAUDE.md files for guideline checking

## Related
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md)
- [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md)
- [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)

## Sources
- [Claude Code Plugins](https://github.com/anthropics/claude-code/blob/main/plugins/code-review/README.md)
- [Claude Code Plugin Marketplace](https://claude.com/plugins/code-review)
