---
id: 2026092031
created: 2026-09-20T31:00:00+02:00
tags:
  - architecture
  - multi-agent
  - event-driven
links:
  - "[Fan-Out Fan-In Parallel Agent Pattern](./05%20-%20Architecture/202609200932%20-%20Fan-Out%20Fan-In%20Parallel%20Agent%20Pattern.md)"
  - "[Orchestrator-Worker Delegation Pattern](./05%20-%20Architecture/202609202020%20-%20Orchestrator-Worker%20Delegation%20Pattern.md)"
  - "[Bidirectional MCP Agent Pattern](./05%20-%20Architecture/2026092030%20-%20Bidirectional%20MCP%20Agent%20Pattern.md)"
---

# Event-Driven Agent Concurrency Pattern

## Core Idea
Agents publish typed events to named topics on an async event bus and subscribe to the topics they care about — instead of Agent A calling Agent B and waiting for a return value. Agents that don't depend on each other's output run concurrently rather than blocking in a call chain.

## How It Works
```
┌─────────────┐    publish     ┌───────────────────────────┐
│  Sensor     │───────────────►│  Event Bus (async)        │
│  Agent      │  CLINICAL.     │                           │
│             │  ANOMALY_      │  ┌─────────────────────┐  │
│  (polls     │  DETECTED      │  │ Topic: CLINICAL.    │  │
│   every     │                │  │ ANOMALY_DETECTED    │  │
│   few sec)  │                │  └──────────┬──────────┘  │
└─────────────┘                │             │             │
                               │             ▼             │
                               │  ┌─────────────────────┐  │
                               │  │ Compliance Agent    │  │
                               │  │ (subscribed to      │  │
                               │  │  ANOMALY_DETECTED)  │  │
                               │  └──────────┬──────────┘  │
                               │             │             │
                               │             ▼             │
                               │  ┌─────────────────────┐  │
                               │  │ publish: COMPLIANCE_│  │
                               │  │ REPORT_READY        │  │
                               │  └──────────┬──────────┘  │
                               │             │             │
                               │             ▼             │
                               │  ┌─────────────────────┐  │
                               │  │ Messaging Agent     │  │
                               │  │ Dispatch Agent      │  │
                               │  │ (both subscribed   │  │
                               │  │  to REPORT_READY)   │  │
                               │  └─────────────────────┘  │
                               └───────────────────────────┘
```

1. **Typed events**: Agents publish strongly-typed events to named topics (e.g., `CLINICAL.ANOMALY_DETECTED`, `CLINICAL.COMPLIANCE_REPORT_READY`).
2. **Subscription model**: Each agent subscribes to the topics it cares about and is woken when a matching event fires — not by a direct call from whoever ran before it.
3. **Independent concurrency**: Agents that don't depend on each other's output run at the same moment, because neither is blocking on the other's return.
4. **Different tempos**: Agents operating on different timescales (one polling every few seconds, one making a network call, one firing once at the end) coexist without bottlenecking each other.

## When to Use
- Multi-agent systems where agents operate on genuinely different tempos
- Scenarios where multiple agents need to react to the same signal
- Replacing linear call chains that fall apart under real-time constraints
- Systems where total latency must not be additive across agents

## Tradeoffs
- **Pros:**
  - Total latency is not additive — concurrent agents run in parallel
  - Agents are decoupled — no direct dependencies between them
  - Natural fit for agents operating at different polling/execution frequencies
  - Scales well — adding a new subscriber doesn't affect publishers
- **Cons:**
  - Debugging is harder — no single call stack to trace
  - Event ordering and delivery guarantees must be handled explicitly
  - Risk of event storms if topics are too broadly subscribed
  - Requires infrastructure (message broker, queue management)

## Examples
- A fall-risk detection system: sensor-monitoring agent publishes `CLINICAL.ANOMALY_DETECTED`, compliance agent cross-references drug-interaction DB and publishes `CLINICAL.COMPLIANCE_REPORT_READY`, messaging and dispatch agents act on that event — all in parallel, not in a chain
- CI/CD pipelines where a build-failure event triggers parallel agents for logging, notification, and rollback
- Multi-agent code review where a "PR opened" event triggers security, style, and performance agents simultaneously

## Anti-Patterns to Avoid
- **Call chain disguised as multi-agent**: If Agent A must wait for Agent B before doing anything, it's a single-threaded system wearing a multi-agent label
- **Polling instead of subscribing**: Agents polling a shared state rather than reacting to events adds latency and waste
- **Unbounded event payloads**: Publishing large data blobs instead of references defeats the decoupling benefit

## Related Patterns
- [[202609200932 - Fan-Out Fan-In Parallel Agent Pattern]] — fan-out is about parallel execution with aggregation; event-driven is about async coordination without a central aggregator
- [[202609202020 - Orchestrator-Worker Delegation Pattern]] — orchestrator-worker uses direct delegation; event-driven uses indirect pub/sub
- [[2026092030 - Bidirectional MCP Agent Pattern]] — bidirectional MCP can expose an event-driven agent's tools to external callers

## Sources
- Google Developers Blog: "4 engineering patterns behind the strongest AI Agents Challenge submissions" (Sept 2026) — https://developers.googleblog.com/4-engineering-patterns-behind-the-strongest-ai-agents-challenge-submissions/
