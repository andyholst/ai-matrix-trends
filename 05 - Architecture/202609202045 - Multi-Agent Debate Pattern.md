---
id: 202609202045
created: 2026-09-20T20:45:00+02:00
tags:
  - architecture
  - mcp
links:
  - "[Multi-Agent Orchestration with Guardrail Layering](./05%20-%20Architecture/202609202002%20-%20Multi-Agent%20Orchestration%20with%20Guardrail%20Layering.md)"
  - "[Agent Teams Pattern](./09%20-%20Trend%20Radar/Emerging/2026092031%20-%20Agent%20Teams%20Pattern.md)"
---

# Multi-Agent Debate Pattern

## Core Idea
Multiple agents participate in a shared conversation, contributing perspectives, challenging each other's positions, and refining conclusions across structured rounds — with a synthesizer or judge agent drawing the final conclusion.

## How It Works
```
Generator Agent → produces initial output
      ↓
Checker Agent → critiques against rubric
      ↓
Generator revises → Checker validates
      ↓ (repeat until approved or budget exhausted)
Synthesizer Agent → merges perspectives into final output
```

Two primary variants exist:

1. **Maker-Checker Loop:** A cheap fast model generates output; a capable model validates against a rubric. The generator revises until the checker approves or the step budget is exhausted. Cuts cost 40-60% versus running both on capable models.

2. **Multi-Perspective Debate:** Two or more agents argue different positions (advocate, skeptic, synthesizer). Research shows debate reduces hallucinations compared to single-model queries because agents catch each other's mistakes. Microsoft recommends limiting group chat to three or fewer agents to prevent convergence failures.

The pattern is competitive rather than collaborative — agents are in tension, not agreement. A separate judge or synthesizer agent draws the conclusion from the debate transcript.

## When to Use
- High-stakes decisions where considering counter-positions matters (compliance review, safety-critical evaluation)
- Quality assurance with structured review rubrics
- Research synthesis where multiple expert perspectives reduce hallucination
- Code review requiring security, style, and performance perspectives

## Tradeoffs
- **Pros:** Reduces hallucinations 30-50% on structured tasks; catches single-model blind spots; maker-checker variant is cost-efficient
- **Cons:** Conversation loops without convergence; sycophancy cascading (agents agree with majority even when wrong); 15 LLM calls per task for 5 rounds with 3 agents; judge bias toward verbose arguments

## Examples
- Compliance review requiring legal, security, and business perspectives
- Code generation review with security, style, and performance critics
- Strategic recommendation with advocate, skeptic, and synthesizer roles

## Related Patterns
- [202609202002 - Multi-Agent Orchestration with Guardrail Layering](./05%20-%20Architecture/202609202002%20-%20Multi-Agent%20Orchestration%20with%20Guardrail%20Layering.md) — guardrails at execution points
- [2026092031 - Agent Teams Pattern](./09%20-%20Trend%20Radar/Emerging/2026092031%20-%20Agent%20Teams%20Pattern.md) — collaborative team alternative
- [202609202020 - Orchestrator-Worker Delegation Pattern](./05%20-%20Architecture/202609202020%20-%20Orchestrator-Worker%20Delegation%20Pattern.md) — hierarchical alternative

## Sources
- https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production
- https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
