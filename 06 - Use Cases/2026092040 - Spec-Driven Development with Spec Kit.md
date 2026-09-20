---
id: 2026092040
created: 2026-09-20T40:00:00+02:00
tags:
  - workflow
  - config
links:
  - "[Claude Code Plugin Distribution for Team Workflow Standardization](./06%20-%20Use%20Cases/202609202000%20-%20Claude%20Code%20Plugin%20Distribution%20for%20Team%20Workflow%20Standardization.md)"
  - "[Claude Code Hooks for CI-CD Automation](./06%20-%20Use%20Cases/202609202001%20-%20Claude%20Code%20Hooks%20for%20CI-CD%20Automation.md)"
---

# Spec-Driven Development with Spec Kit

## Overview

Spec-Driven Development (SDD) inverts the traditional code-first workflow: the specification becomes the source of truth, and code is treated as a generated, verifiable artifact. In 2026 this discipline went mainstream because AI agents are excellent at writing code but poor at guessing intent. GitHub's open-source Spec Kit provides a structured four-phase process (Specify → Plan → Tasks → Implement) that makes the spec the center of the engineering workflow, with explicit human validation gates between each phase.

## Setup

```bash
# Install Spec Kit (requires Node.js 18+)
npm install -g @github/spec-kit

# Or use with npx in a project directory
npx @github/spec-kit init
```

## Configuration

```yaml
# .github/spec-kit/config.yaml
agent: claude-code          # or copilot, gemini-cli
phases:
  - specify       # high-level description → detailed spec
  - plan          # stack + architecture → technical plan
  - tasks         # plan → small, reviewable task list
  - implement     # tasks → code, one at a time
validation_gates:
  - human_review_after_specify
  - human_review_after_plan
  - human_review_after_tasks
```

## Workflow

1. **Specify** — Provide a high-level description of what you're building and why. The coding agent generates a detailed specification covering user journeys, success criteria, and constraints. Review and refine before proceeding.
2. **Plan** — Supply your desired stack, architecture, and constraints. The agent generates a technical plan integrating your internal docs and patterns. Request multiple plan variations to compare approaches.
3. **Tasks** — The agent breaks the plan into small, reviewable chunks — each implementable and testable in isolation (e.g., "create a user registration endpoint that validates email format" rather than "build authentication").
4. **Implement** — The coding agent tackles tasks one by one or in parallel where independent. You review focused changes that solve specific problems, not thousand-line code dumps.

## Results

- Catches requirement misunderstandings before any code is written
- Enables parallel agent execution — different agents implement different spec sections simultaneously
- Changing course is cheap: update the spec, regenerate the plan, let the agent handle the rest
- The spec serves as living documentation that evolves with the project

## Related

- [MOC-Architecture-Patterns](./07%20-%20Structure/MOC-Architecture-Patterns.md)
- [MOC-Trending-Agents](./07%20-%20Structure/MOC-Trending-Agents.md)

## Sources

- [GitHub Spec Kit announcement](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)
- [Spec-Driven Development: From Code to Contract (arXiv:2602.00180)](https://arxiv.org/abs/2602.00180)
- [Addy Osmani — How to write a good spec for AI agents](https://addyosmani.com/blog/good-spec/)
