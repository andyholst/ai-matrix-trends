---
id: 202609202032
created: 2026-09-20T20:32:00+02:00
tags:
  - trend
  - tool
aliases:
links:
  - "[[MOC-Plugin-Ecosystem]]"
  - "[[MOC-Architecture-Patterns]]"
  - "[[202609202000 - Claude Code]]"
  - "[[202609202508 - Hermes Plugin System]]"
---

# Custom Skills and Slash Commands as Team Workflow Accelerators

## Core Idea
Custom skills — portable markdown files following the standard `SKILL.md` format — let teams encode recurring workflows as slash commands that any developer or agent can invoke with a shortcut, turning idiosyncratic tribal knowledge into standardized, reusable, version-controlled automation.

## Details
Most AI coding agents support custom skills or commands: Claude Code uses skills, Cursor uses rules, GitHub Copilot uses instructions. In Claude Code, a skill is a directory containing a `SKILL.md` file plus any supporting files (images, PDFs, scripts). A slash command like `/commit` can prompt for a GitHub issue number, format the commit message with a `Closes #123` trailer, and ask whether to push. A `/jira` skill can walk through the custom fields a client requires, asking the developer questions along the way instead of forcing them to remember every field. A `/show-notes` skill can generate podcast show notes following an exact format. These skills live in version control alongside the codebase, so they evolve with the team's understanding.

The portability is the key differentiator: skills are just markdown, so the same skill works across Claude Code, Cursor, and other agents that follow the standard format. Anthropic even provides a skill-creator skill that helps teams build, improve, and verify new skills. Teams that invest in a shared skill library effectively build an internal automation layer — every developer's agent gains the same capabilities, onboarding new engineers becomes a matter of pointing them at the skill directory, and best practices propagate automatically as skills are refined.

## Implications
Custom skills shift workflow automation from ad-hoc prompts to standardized, team-owned tools. The cost of encoding a recurring workflow is low — a markdown file — but the payoff is consistency: every commit follows the same format, every Jira ticket has the required fields, every podcast episode has show notes in the same style. This also creates a continuous improvement loop: teams discover edge cases, update the skill, and every developer's agent immediately benefits.

## Related
- [[MOC-Plugin-Ecosystem]]
- [[MOC-Architecture-Patterns]]

## Sources
- https://www.danclarke.com/the-many-use-cases-of-ai-coding-agents/
- https://medium.com/nick-tune-tech-strategy-blog/coding-agent-development-workflows-af52e6f912aa
- https://timdeschryver.dev/blog/keep-agentic-ai-simple-a-practical-workflow-for-software-development
- https://www.ibm.com/think/insights/standardize-ai-code-generation-across-your-development-team
