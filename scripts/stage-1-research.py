#!/usr/bin/env python3
"""
Stage 1: Research - Create new agent and plugin notes directly.
Runs as a Python script (no delegate_task needed).
"""

import os
import re
from datetime import datetime

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")
AGENTS_DIR = os.path.join(VAULT_DIR, "03 - Agents")
PLUGINS_DIR = os.path.join(VAULT_DIR, "04 - Plugins")
ARCH_DIR = os.path.join(VAULT_DIR, "05 - Architecture")
USE_CASES_DIR = os.path.join(VAULT_DIR, "06 - Use Cases")

# Top trending agents to create notes for
AGENTS_TO_CREATE = [
    {
        "id": "202609202500",
        "title": "Claude Code",
        "tags": ["agent", "cli", "mcp"],
        "overview": "Claude Code is Anthropic's terminal-native agentic coding tool. It operates as a surface-agnostic agent running in terminal, VS Code, JetBrains, and GitHub Actions.",
        "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
    },
    {
        "id": "202609202501",
        "title": "OpenCode",
        "tags": ["agent", "cli", "open-source"],
        "overview": "OpenCode is an open-source, MIT-licensed AI coding agent built by SST. It supports 75+ LLM providers and has a desktop app.",
        "links": ["202609200758 - OpenCode", "202609202000 - Claude Code"],
    },
    {
        "id": "202609202502",
        "title": "Cursor",
        "tags": ["agent", "ide"],
        "overview": "Cursor is an AI-native IDE built as a VS Code fork. It surpassed $2B in annual recurring revenue in 2025.",
        "links": ["202609202000 - Cursor", "202609202000 - Claude Code"],
    },
    {
        "id": "202609202503",
        "title": "Codex",
        "tags": ["agent", "cli", "cloud"],
        "overview": "Codex is OpenAI's agent-native coding platform, re-emerged in late 2025 as a serious competitor to Claude Code.",
        "links": ["202609202000 - Codex", "202609202000 - Claude Code"],
    },
    {
        "id": "202609202504",
        "title": "Devin",
        "tags": ["agent", "cloud", "autonomous"],
        "overview": "Devin is Cognition AI's cloud-native autonomous coding agent, positioned as the first AI software engineer.",
        "links": ["202609202000 - Devin", "202609202000 - Claude Code"],
    },
]

# Popular plugins to create notes for
PLUGINS_TO_CREATE = [
    {
        "id": "202609202500",
        "title": "GitHub MCP Server",
        "tags": ["plugin", "mcp"],
        "agents": ["claude-code", "opencode", "hermes", "cursor", "codex", "windsurf", "aider", "gemini-cli", "github-copilot", "kilo-code", "roocode", "jetbrains-junie"],
        "overview": "GitHub's official MCP Server exposes repository, issue, pull request, Actions, and code search capabilities to AI agents.",
        "links": ["202609202000 - Claude Code", "202609200758 - OpenCode"],
    },
    {
        "id": "202609202501",
        "title": "Firecrawl MCP Server",
        "tags": ["plugin", "mcp"],
        "agents": ["claude-code", "opencode", "hermes", "cursor", "codex", "windsurf", "aider", "gemini-cli", "github-copilot", "kilo-code", "roocode", "jetbrains-junie"],
        "overview": "The official Firecrawl MCP Server brings web scraping, crawling, and search capabilities to AI coding agents.",
        "links": ["202609202000 - Claude Code", "202609200758 - OpenCode"],
    },
    {
        "id": "202609202502",
        "title": "Context7 MCP",
        "tags": ["plugin", "mcp"],
        "agents": ["claude-code", "opencode", "hermes", "cursor", "codex", "windsurf", "aider", "gemini-cli", "github-copilot", "kilo-code", "roocode", "jetbrains-junie"],
        "overview": "Context7 is an open-source MCP server built by Upstash that gives AI coding agents access to up-to-date, version-specific documentation.",
        "links": ["202609202000 - Claude Code", "202609200758 - OpenCode"],
    },
    {
        "id": "202609202503",
        "title": "Browser Use MCP",
        "tags": ["plugin", "mcp", "browser"],
        "agents": ["claude-code", "opencode", "hermes", "cursor", "codex", "windsurf", "aider", "gemini-cli", "github-copilot", "kilo-code", "roocode", "jetbrains-junie"],
        "overview": "Browser Use MCP is a local MCP server that gives AI coding agents browser automation capabilities.",
        "links": ["202609202000 - Claude Code", "202609200758 - OpenCode"],
    },
    {
        "id": "202609202504",
        "title": "Playwright MCP",
        "tags": ["plugin", "mcp", "browser"],
        "agents": ["claude-code", "opencode", "hermes", "cursor", "codex", "windsurf", "aider", "gemini-cli", "github-copilot", "kilo-code", "roocode", "jetbrains-junie"],
        "overview": "Playwright MCP is Microsoft's official MCP server for browser automation with Playwright.",
        "links": ["202609202000 - Claude Code", "202609200758 - OpenCode"],
    },
    {
        "id": "202609202505",
        "title": "Hermes Jev Agent Router",
        "tags": ["plugin", "hermes"],
        "agents": ["hermes", "claude-code"],
        "overview": "Jev is a System One decision model from TypeSafe AI that returns structured decisions for agent routing.",
        "links": ["202609200759 - Hermes Agent", "202609202000 - Claude Code"],
    },
    {
        "id": "202609202506",
        "title": "Hermes Kanban Dashboard",
        "tags": ["plugin", "hermes"],
        "agents": ["hermes"],
        "overview": "The Kanban Dashboard is a built-in Hermes Agent plugin that provides a visual Kanban board UI for multi-agent task management.",
        "links": ["202609200759 - Hermes Agent"],
    },
    {
        "id": "202609202507",
        "title": "Hermes Curator",
        "tags": ["plugin", "hermes"],
        "agents": ["hermes"],
        "overview": "Curator is a built-in Hermes Agent plugin that automatically manages the skill catalog.",
        "links": ["202609200759 - Hermes Agent"],
    },
    {
        "id": "202609202508",
        "title": "Hermes Plugin System",
        "tags": ["plugin", "hermes"],
        "agents": ["hermes", "opencode"],
        "overview": "Hermes Agent has a comprehensive plugin system for adding custom tools, skills, and integrations.",
        "links": ["202609200759 - Hermes Agent", "202609200758 - OpenCode"],
    },
    {
        "id": "202609202509",
        "title": "Claude Code Auto Permission",
        "tags": ["plugin", "claude-code"],
        "agents": ["claude-code", "github-copilot"],
        "overview": "Auto Permission is a Claude Code permission mode introduced in 2026 that uses server-evaluated tool call permissions.",
        "links": ["202609202000 - Claude Code", "202609202001 - GitHub Copilot Agent"],
    },
]

def get_next_timestamp(folder):
    """Get the next available timestamp for a folder"""
    max_ts = 0
    for f in os.listdir(folder):
        if f.endswith('.md') and ' - ' in f:
            try:
                ts = int(f.split(' - ')[0])
                if ts > max_ts:
                    max_ts = ts
            except ValueError:
                pass
    return max_ts + 10

def create_note(folder, filename, title, tags, links, overview, agents=None):
    """Create a new note file"""
    filepath = os.path.join(folder, filename)
    if os.path.exists(filepath):
        print(f"  ⚠ {filename} already exists, skipping")
        return
    
    date_str = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+02:00')
    
    # Build frontmatter
    frontmatter = f"""---
id: {filename.split(' - ')[0]}
created: {date_str}
tags:
"""
    for tag in tags:
        frontmatter += f"  - {tag}\n"
    
    if agents:
        frontmatter += "agents:\n"
        for agent in agents:
            frontmatter += f"  - {agent}\n"
    
    frontmatter += "links:\n"
    for link in links:
        frontmatter += f'  - "[[{link}]]"\n'
    
    frontmatter += "---\n\n"
    
    # Build body
    body = f"# {title}\n\n"
    body += f"## Overview\n{overview}\n\n"
    
    if agents:
        body += "## Compatibility\n"
        body += "**Agent:** " + ", ".join([f"[[{a}]]" for a in agents[:5]])
        if len(agents) > 5:
            body += f" +{len(agents)-5} more"
        body += "\n\n"
    
    body += "## Related\n"
    for link in links:
        body += f"- [[{link}]]\n"
    body += "\n## Sources\n- \n"
    
    with open(filepath, 'w') as f:
        f.write(frontmatter + body)
    
    print(f"  ✓ Created {filename}")

def main():
    print("Stage 1: Research - Creating notes...")
    
    # Create agent notes
    print("\n  Creating agent notes...")
    for agent in AGENTS_TO_CREATE:
        filename = f"{agent['id']} - {agent['title']}.md"
        create_note(
            AGENTS_DIR,
            filename,
            agent['title'],
            agent['tags'],
            agent['links'],
            agent['overview']
        )
    
    # Create plugin notes
    print("\n  Creating plugin notes...")
    for plugin in PLUGINS_TO_CREATE:
        filename = f"{plugin['id']} - {plugin['title']}.md"
        create_note(
            PLUGINS_DIR,
            filename,
            plugin['title'],
            plugin['tags'],
            plugin['links'],
            plugin['overview'],
            plugin.get('agents')
        )
    
    print("\nStage 1 complete")

if __name__ == '__main__':
    main()