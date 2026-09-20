---
id: 202609202051
created: 2026-09-20T20:51:00+02:00
tags:
  - workflow
  - config
links:
  - "[[202609202030 - CI-CD Pipeline Automation with Claude Code Hooks and GitHub Actions]]"
  - "[[2026092040 - Spec-Driven Development with Spec Kit]]"
---

# Spec-Driven CI/CD Verification Gates for Agent-Generated Code

## Overview
Traditional CI/CD pipelines validate syntax, types, and test results — but AI-generated code can pass all checks while silently violating the specification. Spec-driven verification adds a living spec layer to the pipeline and a Verifier gate that blocks merges when agent output drifts from the agreed contract. This catches the failure modes unique to AI agents: spec drift, hallucinated dependencies, and code that passes tests while violating behavioral contracts.

## Setup
```bash
# Install Auggie CLI (Intent's CI bridge)
npm install -g @augmentcode/auggie

# Authenticate locally
auggie login
auggie token print  # save as AUGMENT_SESSION_AUTH secret

# Add to GitHub Actions workflow
# .github/workflows/agent-verification.yaml
```

## Workflow
1. **Define living specs** — Write specs in `specs/` directory describing API contracts, validation rules, and behavioral expectations. These serve as the shared source of truth for both agents and CI.
2. **Agent generates PR** — An AI coding agent implements a feature and opens a pull request with code and tests.
3. **CI runs Verifier gate** — The pipeline runs `auggie --print "Review the changes in this PR for spec compliance"` which checks the diff against the living spec, not just test results.
4. **Block or allow merge** — If the Verifier finds spec drift (e.g., an endpoint no longer enforces the validation contract), the PR is blocked with actionable feedback. If it passes, the PR proceeds to human review.
5. **Feed failures back to agent** — Verifier feedback is piped back to the agent for automated remediation, creating a self-healing loop.

## Benefits
- Catches spec drift that traditional CI misses
- Prevents hallucinated dependencies from reaching production
- Creates audit trail of spec compliance decisions
- Enables self-healing agent loops with automated remediation

## Related Use Cases
- [[202609202030 - CI-CD Pipeline Automation with Claude Code Hooks and GitHub Actions]]
- [[2026092040 - Spec-Driven Development with Spec Kit]]

## Sources
- [CI/CD for AI Agents: How to Integrate Agent Orchestration into Your Pipeline — Augment Code](https://www.augmentcode.com/guides/cicd-ai-agents-pipeline-integration)
- [Continuous integration and continuous delivery for agentic AI — Red Hat](https://developers.redhat.com/articles/2026/05/18/ci-cd-delivery-agentic-ai)
