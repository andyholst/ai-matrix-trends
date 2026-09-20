---
id: 202609200103
created: 2026-09-20T10:03:00+02:00
tags:
  - trend
  - stable
  - infrastructure
  - docker
aliases:
  - Containerized Agent Sandboxes
links:
  - "[[202609202000 - Claude Code]]"
  - "[[202609202000 - Codex]]"
---

# Containerized Agent Sandboxes

## Core Idea
AI agents increasingly run inside Docker containers for isolation, reproducibility, and security — especially in enterprise deployments.

## Details
- **Hermes Docker profile**: `terminal.backend: docker` with `nikolaik/python-nodejs` image
- **Codex**: Cloud-native sandboxed execution by default
- **MCP servers**: Many run as isolated containers (Docker MCP Toolkit)
- **Security**: Containers limit blast radius of agent actions

## Why It's Stable
Multiple major players have settled on containerization as the deployment pattern. The tooling (Docker, Podman) is mature.

## Related Patterns
- [[202609202004 - Layered Protocol Stack MCP A2A Streamable HTTP]] — MCP servers in containers
- [[202609202000 - MCP Proxy Aggregator Pattern]] — Containerized MCP routing

## Sources
- [Docker MCP Toolkit](https://www.docker.com/blog/introducing-docker-mcp-toolkit/)
- [Hermes Docker Profile](https://hermes-agent.nousresearch.com/docs)
