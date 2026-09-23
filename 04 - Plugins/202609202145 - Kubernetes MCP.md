---
id: 202609202145
created: 2026-09-20T21:45:00+02:00
tags:
  - plugin
  - mcp
agents:
  - claude-code
  - opencode
  - cursor
  - codex
  - windsurf
  - aider
  - gemini-cli
  - github-copilot
  - kilo-code
  - roocode
  - jetbrains-junie
  - cline
  - hermes
---

# Kubernetes MCP

## Overview
Kubernetes MCP is a community-maintained Model Context Protocol server that gives AI coding agents access to Kubernetes clusters. Agents can run kubectl commands, inspect pods and deployments, debug services, and reason about cluster state — all through natural language. Supports both stdio and HTTP transports. Ideal for platform engineers and SREs who want their AI assistant to help with cluster operations.

## Installation
```bash
# Claude Code
claude mcp add kubernetes -- npx -y @kubernetes/mcp-server

# Or via Helm
helm install kubernetes-mcp kubernetes/mcp-server
```

## Configuration
```yaml
mcpServers:
  kubernetes:
    command: npx
    args: ["-y", "@kubernetes/mcp-server"]
    env:
      KUBECONFIG: ~/.kube/config
    # Or remote HTTP:
    # type: http
    # url: https://mcp.kubernetes.example.com/mcp
    # headers:
    #   Authorization: Bearer ${K8S_TOKEN}
```

## Use Cases
- Debugging pod crashes and resource issues
- Inspecting deployment status and rollout history
- Querying service endpoints and ingress rules
- Reasoning about cluster capacity and scaling

## Compatibility
- **Agent:** [202609202000 - Claude Code](../03%20-%20Agents/202609202000%20-%20Claude%20Code.md), [202609202000 - Cursor](../03%20-%20Agents/202609202000%20-%20Cursor.md), [202609202000 - Codex](../03%20-%20Agents/202609202000%20-%20Codex.md)
- **Versions:** MCP spec 2025-03-26+

## Related Plugins
- [2026092020 - GitHub MCP Server](2026092020%20-%20GitHub%20MCP%20Server.md)
- [202609202000 - Browser Use MCP](202609202000%20-%20Browser%20Use%20MCP.md)

## Sources
- [GitHub](https://github.com/Flux159/mcp-server-kubernetes)
- [Docs](https://kubernetes.io/docs/reference/)
