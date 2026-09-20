---
id: 2026092041
created: 2026-09-20T41:00:00+02:00
tags:
  - workflow
  - config
links:
  - "[[202609202000 - Claude Code Plugin Distribution for Team Workflow Standardization]]"
  - "[[202609202001 - Claude Code Hooks for CI-CD Automation]]"
---

# Git Worktree Isolation for Parallel AI Agents

## Overview

When multiple AI coding agents work on the same repository, they create silent file overwrites, stale context, and git lock contention. Git worktrees solve this by giving each agent its own checked-out working directory and branch while sharing a single `.git` object store. This has become the dominant isolation primitive for parallel AI agent development — lightweight, native to git, and requiring no infrastructure beyond the repository itself.

## Setup

```bash
# Create a worktree for an agent
git worktree add ../feature-auth -b agent/feature-auth

# Run an agent in that worktree
cd ../feature-auth
claude --prompt "Implement the authentication module per SPEC.md"

# Clean up when done
git worktree remove ../feature-auth
```

## Configuration

```toml
# ~/.agent-worktree/config.toml (for agent-worktree tool)
[general]
merge_strategy = "merge"   # squash | merge
sync_strategy = "merge"    # rebase | merge
copy_files = [".env", ".env.*"]
submodules = true
submodule_jobs = 8

[hooks]
post_create = ["pnpm install"]
pre_merge = ["pnpm test", "pnpm lint"]
post_merge = []
```

## Workflow

1. **Decompose** — Break work into independent tasks with no file-level dependencies between agents.
2. **Create worktrees** — Each agent gets its own worktree: `git worktree add ../agent-a -b agent/a`.
3. **Run agents in parallel** — Launch each agent in its own worktree directory. Agents never share a working directory, so no file conflicts.
4. **Verify** — Run tests and lint in each worktree before merging.
5. **Merge or discard** — Successful worktrees merge back to main; failed experiments are removed with `git worktree remove`.

## Results

- Eliminates file-level conflicts and context contamination between parallel agents
- Enables 3x+ throughput on independent tasks (one agent per worktree)
- Failed experiments are cheap to discard — just remove the worktree
- Works in monorepos: different services can be worked on in separate trees simultaneously
- Experimentation rate increases ~7x (from 1-2 experiments/month to 10-15) because cleanup is trivial

## Related

- [[MOC-Architecture-Patterns]]
- [[MOC-Trending-Agents]]

## Sources

- [agent-worktree — Git worktree workflow tool for AI coding agents](https://github.com/nekocode/agent-worktree)
- [Git Worktrees for Parallel Development: 3x Throughput with AI Agents](https://understandingdata.com/posts/git-worktrees-parallel-dev/)
- [How we're shipping faster with Claude Code and Git Worktrees — Incident.io](https://incident.io/blog/shipping-faster-with-claude-code-and-git-worktrees)
