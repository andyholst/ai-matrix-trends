---
id: 202609202005
created: 2026-09-20T20:05:00+02:00
tags:

  - agent
aliases:
  - Junie
  - JetBrains Junie
  - JetBrains AI Agent
links:
  - "[Claude Code](202609202000%20-%20Claude%20Code.md)"
  - "[Codex](202609202000%20-%20Codex.md)"
  - "[Cursor](202609202000%20-%20Cursor.md)"
---

# JetBrains Junie

## Overview
JetBrains Junie is JetBrains' AI coding agent, integrated directly into IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs. It represents JetBrains' answer to the agentic coding trend, offering native IDE integration with multi-file editing, code generation, and refactoring capabilities. As of 2026, JetBrains AI (including Junie) is used by approximately 9% of professional developers worldwide.

## Installation
```bash
# JetBrains IDE plugin marketplace
# Settings → Plugins → Search "Junie" or "JetBrains AI"
# Or bundled with JetBrains AI subscription
```

## Core Capabilities
- Native JetBrains IDE integration
- Multi-file code generation and refactoring
- Context-aware suggestions using IDE's code intelligence
- Support for multiple LLM providers
- Integration with JetBrains AI Assistant

## Configuration
```yaml
# Settings → Tools → JetBrains AI
{
  "provider": "anthropic",
  "model": "claude-sonnet-4-20250514",
  "autoComplete": true,
  "agentMode": "chat",
  "contextScope": "project"
}
```

## Key Plugins/Extensions
- [202609202000 - Claude Code](202609202000%20-%20Claude%20Code.md) (terminal-native alternative)
- [202609202000 - Cursor](202609202000%20-%20Cursor.md) (IDE-based alternative)
- [202609202010 - Playwright MCP](../04%20-%20Plugins/202609202010%20-%20Playwright%20MCP.md) (browser automation)

## Strengths
- Deepest JetBrains IDE integration available
- Leverages IDE's code intelligence for better context
- Multi-provider support
- Familiar workflow for JetBrains users
- Enterprise-friendly (JetBrains licenses)

## Weaknesses
- JetBrains IDEs only (no VS Code or terminal)
- Lower adoption than Claude Code or Copilot
- Newer agent with less mature agentic loop
- Requires JetBrains subscription for full features

## Use Cases
- Teams standardized on JetBrains IDEs
- Developers wanting native IDE agent experience
- Enterprise environments with JetBrains licenses
- Projects leveraging JetBrains code intelligence

## Related Agents
- [202609202000 - Claude Code](202609202000%20-%20Claude%20Code.md)
- [202609202000 - Codex](202609202000%20-%20Codex.md)
- [202609202000 - Cursor](202609202000%20-%20Cursor.md)

## Sources
- [Official Docs](https://www.jetbrains.com/ai/)
- [JetBrains Blog](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/)
- [Faros AI Blog](https://www.faros.ai/blog/best-ai-coding-agents-2026)
