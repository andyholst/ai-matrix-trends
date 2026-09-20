---
id: 202609200940
created: 2026-09-20T09:40:00+02:00
tags:
  - workflow
links:
  - "[[202609202001 - Claude Code Hooks for CI-CD Automation]]"
  - "[[202609202030 - CI/CD Pipeline Automation with Claude Code Hooks and GitHub Actions]]"
  - "[[MOC-Plugin-Ecosystem]]"
  - "[[MOC-Architecture-Patterns]]"
---

# Claude Code Hooks for CI-CD Automation

## Core Idea
Claude Code hooks — user-defined commands, prompts, or agents that execute automatically at 12 lifecycle events — transform quality guidelines from documentation into enforced rules that run every time Claude touches a codebase.

## Details
Released in early 2026, Claude Code hooks fire at lifecycle points including PreToolUse (can approve or deny actions), PostToolUse (run checks after changes), and Stop (final validation). Three handler types cover different verification needs: Command hooks run shell scripts for formatting and linting; Prompt hooks delegate security classification to the LLM for semantic review; Agent hooks spawn subagents with Read/Grep/Glob access for cross-file verification. PreToolUse is the most powerful event because it can block actions entirely — making it the enforcement mechanism for security policies, file protection, and mandatory review gates.

Production patterns include auto-formatting on every edit, protecting critical files (middleware, API routes, .env) from modification, blocking production dependency installs without review, running TypeScript type checks after edits, and prompt-based security reviews that deny edits touching auth, payments, or secrets. Hooks integrate with GitHub Actions and GitLab CI, running quality gates (Snyk, SonarQube, GitGuardian) on AI-generated code before merge. The pattern converts manual review steps into automated gates, freeing human reviewers for decisions that require judgment.

## Implications
Hooks close the loop between CLAUDE.md (defining standards) and thread-based engineering (governance framework). Teams can enforce formatting, security, and architectural rules without relying on developer discipline. The approach scales: start with zero-risk formatting hooks, add file protection, then layer in semantic security review. This shifts CI/CD from reactive failure detection to proactive quality enforcement at the moment code is written.

## Related
- [[202609202001 - Claude Code Hooks for CI-CD Automation]]
- [[202609202030 - CI/CD Pipeline Automation with Claude Code Hooks and GitHub Actions]]
- [[202609202005 - Auto-Commit Checkpoint Workflow with Stop Hooks and Git]]

## Sources
- https://www.pixelmojo.io/blogs/claude-code-hooks-production-quality-ci-cd-patterns
- https://academy.claude.com/courses/ai-native-sdlc-playbook/ci-cd-integration-and-deployment
- https://code.claude.com/docs/en/hooks
