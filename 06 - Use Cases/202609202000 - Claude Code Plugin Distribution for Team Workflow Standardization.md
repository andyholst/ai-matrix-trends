---
id: 202609202000
created: 2026-09-20T20:00:00+02:00
tags:
  - workflow
  - config
  - agent
links:
  - [[202609202000 - Claude Code]]
  - [[202609202002 - Multi-Server MCP Orchestration for Cross-Tool Workflows]]
---

# Claude Code Plugin Distribution for Team Workflow Standardization

## Core Idea
Packaging skills, hooks, MCP server configs, sub-agents, and slash commands into a versioned plugin that installs with a single command, turning one engineer's Claude Code setup into a shareable org-wide standard.

## Details
A Claude Code plugin is a directory containing a `.claude-plugin/plugin.json` manifest plus any combination of harness components: `skills/`, `hooks/hooks.json`, `.mcp.json`, `agents/`, `commands/`, `.lsp.json`, `monitors/monitors.json`, and `settings.json`. The manifest's `name` field becomes the namespace prefix for every skill, so a `hello` skill inside a plugin named `my-first-plugin` is invoked as `/my-first-plugin:hello`. This namespacing is mandatory and prevents collisions when multiple plugins define skills with the same name.

The pattern solves what Anthropic calls "tribal knowledge" in team environments: one engineer discovers a useful hook, another builds an MCP server for internal docs, a third writes a slash command for deploys. Without packaging, new hires inherit a blank `.claude/` folder. With a plugin, `claude plugin install` distributes the entire harness — versioned, namespaced, and updatable when the maintainer bumps the version.

A reference implementation is Cole Medin's `helpline` repo, which ships a stop hook that proposes CLAUDE.md updates, an `explorer` sub-agent for read-only codebase mapping, and a `scoped-tests` skill — all under 200 lines of config.

### Step-by-Step: Building Your First Plugin

1. **Create the plugin directory** with a `.claude-plugin/` subdirectory containing `plugin.json`:
   ```json
   {
     "name": "my-first-plugin",
     "description": "A greeting plugin to learn the basics",
     "version": "1.0.0",
     "author": { "name": "Your Name" }
   }
   ```

2. **Add a skill** by creating `skills/hello/SKILL.md`:
   ```markdown
   ---
   description: Greet the user with a friendly message
   disable-model-invocation: true
   ---
   Greet the user warmly and ask how you can help them today.
   ```

3. **Test locally** with the `--plugin-dir` flag:
   ```bash
   claude --plugin-dir ./my-first-plugin
   ```
   Then invoke `/my-first-plugin:hello` inside the session.

4. **Convert existing `.claude/` configs** into plugin components by moving skills, hooks, and agents into the plugin directory structure. Project and user `.claude/agents/` definitions override same-named plugin agents, so remove originals after migrating.

5. **Distribute** via a marketplace. Users add it with:
   ```
   /plugin marketplace add your-org/your-repo
   ```
   Then install with:
   ```bash
   claude plugin install your-plugin@your-marketplace
   ```

### Key Pitfalls
- Only `plugin.json` goes inside `.claude-plugin/`. Everything else (skills, hooks, MCP configs) lives at the plugin root.
- Hardcoded paths like `/Users/you/repos/...` work for one person and break for the team. Use `${CLAUDE_PLUGIN_ROOT}` or relative paths.
- The `version` field is optional but load-bearing. Set it explicitly; otherwise the commit SHA becomes the version and every push counts as a release.

## Implications
Plugins transform Claude Code from a personal tool into a platform. A team can standardize on a single `/deploy` skill, a shared set of MCP servers, and organization-wide hooks that enforce code quality — all maintained by one engineer and consumed by everyone. The tribal-knowledge problem that plagues AI-assisted teams (screenshots in Slack threads, incomplete README instructions) is solved by a single install command that delivers the entire workflow.

## Related
- [[202609202000 - Claude Code]]
- [[202609202002 - Multi-Server MCP Orchestration for Cross-Tool Workflows]]

## Sources
- https://code.claude.com/docs/en/plugins
- https://claudefa.st/blog/tools/mcp-extensions/plugins-distribution
