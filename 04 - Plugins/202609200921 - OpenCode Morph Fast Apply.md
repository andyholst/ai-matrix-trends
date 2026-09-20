---
id: 202609200921
created: 2026-09-20T09:21:00+02:00
tags:
  - plugin
  - opencode
  - code-editing
links:
  - "[[MOC-Plugin-Ecosystem]]"
  - "[[MOC-Trending-Agents]]"
  - "[[202609200758 - OpenCode]]"
---

# OpenCode Morph Fast Apply

## Overview
OpenCode Morph Fast Apply is a plugin that integrates the Morph Fast Apply API into OpenCode, enabling 10x faster code editing with lazy edit markers. Instead of sending full file diffs, it sends concise edit instructions that the Morph engine applies at 10,500+ tokens/sec. The plugin requires no MCP server and works as a pure OpenCode plugin. It has 171 GitHub stars and is actively maintained.

## Installation
```bash
# Add to OpenCode config
# ~/.config/opencode/config.json

{
  "plugin": ["opencode-morph-fast-apply"]
}
```

## Configuration
```json
{
  "plugin": ["opencode-morph-fast-apply"],
  "morph": {
    "apiKey": "your-morph-api-key",
    "model": "morph-fast-apply",
    "lazyMarkers": true,
    "fallbackToStandardEdit": true
  }
}
```

## Use Cases
- High-speed code edits in large files
- Reducing token consumption by 72% for edit instructions
- Batch code transformations across multiple files
- Real-time collaborative editing with minimal latency
- Fallback to standard edit when Morph is unavailable

## Compatibility
- **Agent:** [[202609200758 - OpenCode]]
- **Versions:** OpenCode 2.x+

## Related Plugins
- [[202609200758 - OpenCode]] — all-in-one agent harness
- [[202609200758 - OpenCode]] — context optimization

## Sources
- [GitHub](https://github.com/JRedeker/opencode-morph-fast-apply)
- [Awesome OpenCode](https://github.com/awesome-opencode/awesome-opencode)
- [OpenCode Ecosystem](https://opencode.ai/docs/ecosystem/)
