---
id: 202609200931
created: 2026-09-20T09:31:00+02:00
tags:
  - architecture
links:
  - "[[202609202020 - Orchestrator-Worker Delegation Pattern]]"
  - "[[202609202024 - Orchestrator Worker Multi-Agent Delegation]]"
  - "[[202609202002 - Multi-Agent Orchestration with Guardrail Layering]]"
---

# Adaptive Planning (Magentic) Orchestration Pattern

## Core Idea
A manager agent dynamically builds, refines, and executes a task plan by consulting specialist agents — the plan itself is discovered through collaboration rather than being predefined, enabling real-time pivoting when new information emerges.

## How It Works
```
┌──────────────────────────────────────────────────────┐
│                  Manager Agent                        │
│  1. Receives goal                                    │
│  2. Builds initial task plan (task ledger)           │
│  3. Assigns tasks to specialists                     │
│  4. Monitors progress, reorders/replans as needed    │
│  5. Checks goal satisfaction; iterates if not met   │
└──────────┬───────────┬───────────┬───────────────────┘
           │           │           │
     ┌─────▼─────┐ ┌──▼──────┐ ┌─▼──────────┐
     │Diagnostic │ │Infra    │ │Remediation │
     │Agent      │ │Agent    │ │Agent       │
     └───────────┘ └─────────┘ └────────────┘
```

1. **Plan construction**: The manager creates an initial task ledger — a structured plan of subtasks with dependencies.
2. **Dynamic delegation**: Tasks are assigned to specialist agents based on their capabilities.
3. **Adaptive replanning**: As specialists report back, the manager reorders, adds, or removes tasks. If diagnostics reveal the root cause is different from what was assumed, the entire plan pivots.
4. **Goal-continuous verification**: After each round, the manager checks whether the original goal is satisfied. If not, it iterates.
5. **Convergence**: The loop continues until the goal is met or a termination condition is hit.

## When to Use
- Open-ended problems with no predetermined solution path
- Incident response where remediation steps emerge from diagnosis
- Complex migrations where scope changes during execution
- SRE workflows: diagnose → hypothesize → test → remediate → verify
- Any domain where the right specialist is not known upfront

## Tradeoffs
- **Pros:**
  - Handles ambiguity and changing requirements gracefully
  - No need to predefine the full task decomposition
  - Can pivot in real time when new information emerges
  - Works well with heterogeneous specialist agents
- **Cons:**
  - Slow to converge — may iterate many times before reaching a solution
  - Stalls on ambiguous goals where the manager cannot determine next steps
  - Higher token cost due to multiple manager-specialist round trips
  - Risk of infinite loops if termination conditions are poorly defined
  - Manager agent becomes a bottleneck and single point of failure

## Examples
- Microsoft Azure's Magenta orchestration pattern for SRE incident response
- Salesforce Agentforce 2.0's Atlas Reasoning Engine (adaptive variant of orchestrator-worker)
- Complex codebase migration where the plan evolves as the agent discovers dependencies

## Related Patterns
- [[202609202020 - Orchestrator-Worker Delegation Pattern]] — static plan known upfront; adaptive planning discovers the plan
- [[202609202024 - Orchestrator Worker Multi-Agent Delegation]] — similar but with fixed decomposition
- [[202609202002 - Multi-Agent Orchestration with Guardrail Layering]] — guardrails can be layered on top of adaptive planning

## Sources
- Microsoft Azure Architecture Center: "AI Agent Orchestration Patterns" — Magentic orchestration (https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- Beam AI: "6 Multi-Agent Orchestration Patterns for Production (2026)" — Adaptive planning (https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production)
