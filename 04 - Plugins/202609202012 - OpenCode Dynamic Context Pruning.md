---
id: 202609202012
created: 2026-09-20T20:12:00+02:00
tags:
  - plugin
  - opencode
  - context-management
links:
  - [[202609202000 - Jev Agent Router]]
  - [[202609202000 - OpenCode Supermemory]]
---

# OpenCode Dynamic Context Pruning

## Overview
OpenCode Dynamic Context Pruning (DCP) is a plugin that intelligently manages conversation context to optimize token usage. It prunes obsolete tool outputs from conversation history while preserving user and agent messages verbatim. In testing, it reduces token consumption by 60-90% in long sessions with minimal impact on cache hit rates (85% vs 90% without). It is licensed under AGPL-3.0 and has 4.2k GitHub stars.

## Installation
```bash
# Add to OpenCode config
# ~/.config/opencode/config.json
{
  "plugin": ["opencode-dynamic-context-pruning"]
}
```

## Configuration
```json
{
  "plugin": ["opencode-dynamic-context-pruning"],
  "dcp": {
    "protectedFilePatterns": ["*.env*", "*.secret*"],
    "pruneThreshold": 0.8,
    "keepLastNToolOutputs": 5
  }
}
```

## Use Cases
- Long-running coding sessions that approach context limits
- Reducing API costs by minimizing token usage
- Maintaining conversation quality by removing stale tool outputs
- Preventing hallucinations from outdated context

## Compatibility
- **Agent:** [[OpenCode]]
- **Versions:** OpenCode 2.x+

## Related Plugins
- [[202609202000 - Jev Agent Router]] — alternative context management approach
- [[202609202000 - OpenCode Supermemory]] — persistent memory across sessions

## Sources
- [GitHub](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning)
- [OpenCode Ecosystem](https://opencode.ai/docs/ecosystem/)
