---
id: 202609202052
created: 2026-09-20T20:52:00+02:00
tags:
  - workflow
  - config
links:
  - "[Multi-Agent Team Orchestration for Parallel Development](./06%20-%20Use%20Cases/2026092040%20-%20Multi-Agent%20Team%20Orchestration%20for%20Parallel%20Development.md)"
  - "[Git Worktree Isolation for Parallel AI Agents](./06%20-%20Use%20Cases/2026092041%20-%20Git%20Worktree%20Isolation%20for%20Parallel%20AI%20Agents.md)"
---

# Background Cloud Agents for Asynchronous Development

## Overview
Background cloud agents clone a repository into an isolated cloud environment, work on a task autonomously (writing code, running tests, fixing failures), and deliver a pull request when finished. Developers assign a task and context-switch to other work while the agent executes. This pattern turns coding agents from interactive pair programmers into asynchronous team members that expand effective team capacity without requiring synchronous attention.

## Setup
```bash
# GitHub Copilot coding agent — enabled in repo settings
# Repository Settings → Code and automation → Copilot → Coding agent

# OpenAI Codex cloud delegation
codex delegate "Refactor the payment module for the new API" --repo owner/repo

# Devin (Cognition) — assign via web UI or CLI
devin assign "Implement OAuth2 flow for the auth service" --repo owner/repo
```

## Workflow
1. **Assign task with context** — Provide the agent with a clear description, relevant files, and acceptance criteria. Load spec or plan documents so the agent knows the exact sequence of tasks.
2. **Agent clones and explores** — The agent clones the repo into a sandboxed cloud VM, reads the codebase, and formulates an implementation plan.
3. **Autonomous execution loop** — The agent writes code, runs tests, debugs failures, and iterates until tests pass. It can run linters, type checkers, and integration tests in the cloud environment.
4. **PR delivery** — When tests pass, the agent opens a pull request with a summary of changes, test results, and any decisions made during implementation.
5. **Human review and merge** — A developer reviews the PR, requests changes if needed, and merges. The agent can iterate on review feedback.

## Benefits
- Developer context-switches to other work while agent executes
- Cloud environment has full compute resources for test suites
- Isolated sandbox prevents local environment contamination
- Scales team capacity without synchronous coordination overhead

## Related Use Cases
- [[2026092040 - Multi-Agent Team Orchestration for Parallel Development]]
- [[2026092041 - Git Worktree Isolation for Parallel AI Agents]]

## Sources
- [Best AI Coding Agents in 2026, Ranked — MightyBot](https://mightybot.ai/blog/coding-ai-agents-for-accelerating-engineering-workflows/)
- [My LLM coding workflow going into 2026 — Addy Osmani](https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e)
- [AI Coding Agents in 2026: How Developers Are Changing the Way They Code](https://ai.plainenglish.io/ai-coding-agents-in-2026-how-developers-are-changing-the-way-they-code-88c2dbd237ab)
