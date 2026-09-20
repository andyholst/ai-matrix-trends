---
id: 202609202000
created: 2026-09-20T20:00:00+02:00
tags:
  - plugin
  - tool
  - mcp

---

# Jev Agent Router

## Overview
Jev is a System One decision model from TypeSafe AI that returns typed decisions with calibrated probabilities instead of generating text. The Jev Agent Router is a Hermes plugin that integrates Jev's context engine into Hermes Agent, providing a skill plus a stdio MCP server (`agent_route`) for intelligent context management. Jev selects what to keep rather than summarizing, cutting roughly 75% of context usage while preserving every user and agent message verbatim — only old tool outputs are candidates for pruning. Beyond the Hermes integration, Jev itself is a cross-agent decision layer usable via LangChain middleware for model routing, auto-mode guardrails, tool-call validation, and jailbreak screening. TypeSafe claims 40-200x faster inference than frontier LLMs at $0.042 per 1M input tokens with free output, and Jev's typed outputs mathematically cannot hallucinate or produce type errors.

## Installation
```bash
# Clone the plugin from the Hermes plugin catalog
hermes plugins install jev-agent-router

# Or install directly from source
git clone https://github.com/NousResearch/hermes-agent ~/.hermes/plugins/jev-agent-router
```

Requires `uv` on PATH. The plugin registers as a skill plus a stdio MCP server started with `uv run` from the checkout directory.

For LangChain integration (cross-agent):
```bash
pip install langchain-typesafe
```

## Configuration
```yaml
# In your Hermes config.yaml, the MCP server is auto-discovered.
# No additional configuration needed beyond installing the plugin.
```

For LangChain model routing:
```python
from langchain_typesafe.experimental.middleware import (
    ModelChoice,
    ModelRouterMiddleware,
)

router = ModelRouterMiddleware(
    choices={
        "fast": ModelChoice(model="openai:luna", criteria="Direct lookups and localized changes."),
        "powerful": ModelChoice(model="openai:sol", criteria="Architecture and high-stakes decisions."),
    },
    instructions="Choose the least costly model that can complete the task.",
)
```

## Use Cases
- Long-running agent sessions where context window saturation is a problem
- Model routing — pick the cheapest model that can handle a task
- Tool-call validation — guaranteed-valid tool selection with confidence scoring
- Jailbreak and prompt-injection screening at 40-200x faster than a second LLM pass
- Auto-mode guardrails — let Jev decide whether a tool call is safe to auto-execute
- Multi-step coding tasks that accumulate large tool outputs

## Compatibility
**Agent:** [202609200759 - Hermes Agent](./03%20-%20Agents/202609200759%20-%20Hermes%20Agent.md), [202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md) (via LangChain), any LangChain-compatible agent
**Versions:** Hermes Agent 1.0+
**Dependencies:** uv, Python 3.10+, TypeSafe API key (for LangChain integration)

## Related Plugins
- [202609202000 - Browser Use MCP](./04%20-%20Plugins/202609202000%20-%20Browser%20Use%20MCP.md) — Validate browser tool calls with Jev before execution
- [202609200805 - Hermes Kanban Dashboard](./04%20-%20Plugins/202609200805%20-%20Hermes%20Kanban%20Dashboard.md) — Route Kanban worker tasks through Jev for cost optimization
- [202609200806 - Hermes Curator](./04%20-%20Plugins/202609200806%20-%20Hermes%20Curator.md) — Use Jev to decide which skills to prune or consolidate

## Sources
- [TypeSafe AI: Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
- [LangChain: Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)
- [DataCamp: Jev System One Model Explained](https://www.datacamp.com/blog/system-one-models-jev)
- [Reddit: Jev Context Engine Integration](https://www.reddit.com/r/hermesagent/comments/1wkpl3q/integrated_the_jev_context_engine_into_hermes/)

## Related
- [MOC-Plugin-Ecosystem](./07%20-%20Structure/MOC-Plugin-Ecosystem.md)
- [MOC-Trending-Agents](./07%20-%20Structure/MOC-Trending-Agents.md)
