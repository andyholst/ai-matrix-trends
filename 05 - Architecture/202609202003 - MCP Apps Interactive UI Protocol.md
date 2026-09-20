---
id: 202609202003
created: 2026-09-20T20:03:00+02:00
tags:
  - architecture
  - mcp
  - ui
  - protocol
links:
  - [[mcp-proxy-aggregator-pattern]]
  - [[multi-agent-orchestration-patterns]]
---

# MCP Apps: Interactive UI Protocol Pattern

## Core Idea
An extension to the Model Context Protocol that allows agents to render interactive UI components (buttons, toggles, forms, selections) directly inside the host environment, so users express intent through interaction rather than text explanation.

## How It Works
MCP Apps evolve the protocol beyond request-response tool calling into a bidirectional interaction layer. The agent sends UI component descriptions to the host; the host renders them and returns user interactions as structured events. The protocol defines a `ui/components` resource type alongside the existing `tools`, `resources`, and `prompts`.

```
Agent ──[UI component spec]──→ Host (renders buttons, forms, toggles)
Host ──[user interaction event]──→ Agent
Agent ──[updated UI spec]──→ Host
```

The flow mirrors MCP Apps' predecessor MCP-UI, which first demonstrated that agents could render embedded web UIs inside their host environment. MCP Apps formalize this in the protocol specification itself.

Key design decisions:
- Components are declarative — the agent describes what to render, the host decides how to render it
- Interaction events are typed and versioned, enabling backward-compatible component evolution
- The pattern works over all MCP transports (stdio, Streamable HTTP) without transport-specific changes

## When To Use
- Workflows where natural language specification is ambiguous or verbose (configuration, approval flows, parameter tuning)
- Agent tasks that benefit from human-in-the-loop interaction without leaving the agent session
- Scenarios where the agent needs to present choices, confirmations, or progressive disclosure of information
- Building agent-powered applications where the UI is a first-class citizen rather than an afterthought

## Tradeoffs
**Pros:**
- Reduces ambiguity in agent-user communication
- Enables interactive workflows (multi-step approvals, form filling, visual feedback) within agent sessions
- Protocol-level standardization means any MCP client can implement the pattern
- Users interact with structured components instead of free-form text, reducing error rates

**Cons:**
- Host environment must support rendering — not all MCP clients can display interactive components
- Adds protocol complexity beyond the simple tool-call model
- UI component specifications consume context window space that could be used for other tasks
- Limited adoption as of early 2026; most clients still expect text-only agent responses

## Examples
- OpenAI's Apps SDK extends MCP with interactive UI components
- goose adopted MCP-UI early and is shipping full MCP Apps support
- Approval workflows where the agent presents a diff and the user approves/rejects via buttons
- Configuration agents that render forms for parameter selection

## Anti-Patterns to Avoid
- **Over-UI-ing**: Using interactive components for simple yes/no questions that a text response handles more efficiently
- **Assuming host support**: Building MCP Apps workflows that fail silently on clients without UI rendering
- **Context flooding**: Rendering large data tables as UI components when a text summary would suffice

## Related Patterns
- [[mcp-proxy-aggregator-pattern]] — proxy aggregators may need to route UI component specs alongside tool calls
- [[multi-agent-orchestration-patterns]] — orchestrator agents may use UI components to present aggregated results for human review

## Sources
- Model Context Protocol blog, "MCP Apps" (November 2025)
- DEV.to, "My Predictions for MCP and AI-Assisted Coding in 2026" — MCP Apps becoming default
- MCP-UI project (mcpui.dev) — predecessor demonstrating interactive agent interfaces
