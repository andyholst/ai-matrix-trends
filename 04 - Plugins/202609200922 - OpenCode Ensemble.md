---
id: 202609200922
created: 2026-09-20T09:22:00+02:00
tags:
  - plugin
  - opencode
  - multi-agent
agents:
  - opencode
---

# OpenCode Ensemble

## Overview
OpenCode Ensemble is a multi-agent orchestration plugin that enables parallel agent teams with messaging, shared tasks, and coordinated execution. Each team member runs in their own session with isolated context, communicating through a shared message bus. The plugin provides compaction safety (team context is preserved when sessions get long), team-aware shell environment variables, graceful shutdown, and plan approval mode. With 218 GitHub stars and 835 tests, it is one of the most robust multi-agent plugins in the OpenCode ecosystem.

## Installation
```bash
# Add to OpenCode config
# ~/.config/opencode/config.json

{
  "plugin": ["opencode-ensemble"]
}
```

## Configuration
```json
{
  "plugin": ["opencode-ensemble"],
  "ensemble": {
    "maxTeammates": 4,
    "compactionSafety": true,
    "planApprovalMode": true,
    "gracefulShutdown": true,
    "teamShellEnv": true
  }
}
```

## Use Cases
- Parallel feature development with multiple agents
- Code review teams with specialized roles
- Research and implementation pipelines
- Multi-perspective problem solving
- Coordinated refactoring across large codebases

## Compatibility
- **Agent:** [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md)
- **Versions:** OpenCode 2.x+, Node.js 24+

## Related Plugins
- [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md) — all-in-one agent harness
- [202609200758 - OpenCode](../03%20-%20Agents/202609200758%20-%20OpenCode.md) — persistent memory across sessions
- [202609202000 - Jev Agent Router](202609202000%20-%20Jev%20Agent%20Router.md) — agent routing and orchestration

## Sources
- [GitHub](https://github.com/hueyexe/opencode-ensemble)
- [Awesome OpenCode](https://github.com/awesome-opencode/awesome-opencode)
- [OpenCode Ecosystem](https://opencode.ai/docs/ecosystem/)

## Related
- [MOC-Plugin-Ecosystem](../07%20-%20Structure/MOC-Plugin-Ecosystem.md)
- [MOC-Trending-Agents](../07%20-%20Structure/MOC-Trending-Agents.md)
