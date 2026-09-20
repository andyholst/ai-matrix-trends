---
id: 202609202001
created: 2026-09-20T20:00:00+02:00
tags:
  - workflow
  - config
  - cli
links:
  - "[Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)"
  - "[Multi-Server MCP Orchestration for Cross-Tool Workflows](./06%20-%20Use%20Cases/202609202002%20-%20Multi-Server%20MCP%20Orchestration%20for%20Cross-Tool%20Workflows.md)"
---

# Claude Code Hooks for CI/CD Automation

## Core Idea
Event-driven shell commands that fire at 12 lifecycle points in Claude Code, enabling deterministic enforcement of code quality, branch protection, and formatting policies without relying on the LLM's judgment.

## Details
Claude Code hooks execute shell commands at defined lifecycle events. The two most powerful are `PreToolUse` (fires before a tool call executes and can block it) and `PostToolUse` (fires after a tool call succeeds for checks and formatting). Hooks receive tool input as JSON on stdin and communicate decisions via exit codes and JSON on stdout.

### Hook Lifecycle Events

| Event | When It Fires | Use Case |
|-------|--------------|----------|
| `PreToolUse` | Before a tool call executes | Block dangerous commands, enforce branch protection |
| `PostToolUse` | After a tool call succeeds | Auto-format, lint, audit logging |
| `Notification` | When Claude sends a notification | Desktop alerts when human input needed |
| `Stop` | When Claude finishes responding | Validate final output, trigger CI |
| `SessionStart` | When a session begins or resumes | Load project context, verify environment |
| `SubagentStop` | When a subagent finishes | Aggregate results, update tracking |
| `PreCompact` | Before context compaction | Save session state, flush logs |

### Auto-Format on Write (PostToolUse)

The most common hook pattern. Runs a formatter on every file Claude edits:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/format-file.sh",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

The script itself:

```bash
#!/usr/bin/env bash
set -euo pipefail
file_path="$(jq -r '.tool_input.file_path // empty')"
[ -z "$file_path" ] && exit 0
[ -f "$file_path" ] || exit 0
case "$file_path" in
  *.py)        ruff format "$file_path" >&2 ;;
  *.ts|*.tsx|*.js|*.jsx|*.json|*.css|*.md)
               npx --no-install prettier --write "$file_path" >&2 ;;
  *.go)        gofmt -w "$file_path" >&2 ;;
  *)           exit 0 ;;
esac
exit 0
```

### Branch Protection (PreToolUse)

Block direct commits to main and force feature-branch workflow:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "./scripts/claude-branch-protection.sh"
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
COMMAND=$(echo "$CLAUDE_TOOL_INPUT" | jq -r '.command')
if echo "$COMMAND" | grep -q -E 'git\s+(commit|push.*\smain|push.*origin\s+main)'; then
  cat <<'EOF'
{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "Direct commits to main prohibited. Use feature branches: git checkout -b feat/name && gh pr create"}}
EOF
  exit 0
fi
echo '{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "allow"}}'
```

### Audit Logging (PostToolUse)

Record every tool call for compliance and debugging:

```bash
#!/usr/bin/env bash
set -euo pipefail
log_dir="${CLAUDE_PROJECT_DIR}/.claude/audit"
mkdir -p "$log_dir"
jq -c '{ ts: now | todateiso8601, session: .session_id, tool: .tool_name, input: .tool_input }' >> "$log_dir/tool-calls.jsonl"
exit 0
```

### CI/CD Integration Pattern

The production pattern chains hooks with CI:
1. Developer works with Claude Code locally; hooks enforce formatting and branch policy.
2. On PR creation, GitHub Actions triggers Claude Code in CI mode (`-p` flag).
3. CI hooks run quality gates: lint, type check, security scan (Snyk), test suite.
4. Results post as PR comments via GitHub API.
5. Merge is blocked until all gates pass.

This ensures AI-generated code meets the same standards as human-written code before entering the main branch.

## Implications
Hooks make Claude Code deterministic where the LLM alone is probabilistic. Instead of hoping the AI remembers to format code or avoids dangerous commands, hooks enforce those policies at the system level. This shifts the trust boundary from "trust the model" to "trust the hook script" — a much easier audit surface. Teams can enforce organizational policies (no direct prod DB access, no edits to `.env` files, mandatory test runs before push) without relying on prompt engineering or system-prompt reminders that the model may ignore.

## Related
- [202609202000 - Claude Code](./03%20-%20Agents/202609202000%20-%20Claude%20Code.md)
- [202609202002 - Multi-Server MCP Orchestration for Cross-Tool Workflows](./06%20-%20Use%20Cases/202609202002%20-%20Multi-Server%20MCP%20Orchestration%20for%20Cross-Tool%20Workflows.md)

## Sources
- https://code.claude.com/docs/en/hooks-guide
- https://www.pixelmojo.io/blogs/claude-code-hooks-production-quality-ci-cd-patterns
- https://cameronwestland.com/building-my-first-claude-code-hooks-automating-the-workflow-i-actually-want/
