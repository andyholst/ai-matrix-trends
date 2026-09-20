#!/usr/bin/env python3
"""
Stage 1: Research - Create new agent and plugin notes directly.
Runs as a Python script (no delegate_task needed).
Prevents duplicates by checking existing titles.
"""

import os
import re
from datetime import datetime

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")
AGENTS_DIR = os.path.join(VAULT_DIR, "03 - Agents")
PLUGINS_DIR = os.path.join(VAULT_DIR, "04 - Plugins")
ARCH_DIR = os.path.join(VAULT_DIR, "05 - Architecture")
USE_CASES_DIR = os.path.join(VAULT_DIR, "06 - Use Cases")

def get_existing_titles(folder):
    """Get all existing note titles in a folder"""
    titles = set()
    if not os.path.exists(folder):
        return titles
    for f in os.listdir(folder):
        if f.endswith('.md') and ' - ' in f:
            # Extract title after timestamp
            title = f.split(' - ', 1)[1].replace('.md', '').lower()
            titles.add(title)
            # Also add the full filename without timestamp
            titles.add(f.replace('.md', '').lower())
    return titles

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

def create_note(folder, title, tags, links, overview, agents=None):
    """Create a new note file (skips if title already exists)"""
    existing = get_existing_titles(folder)
    
    # Check if a note with this title already exists
    if title.lower() in existing:
        print(f"  ⚠ {title} already exists, skipping")
        return
    
    # Generate new timestamp
    ts = get_next_timestamp(folder)
    filename = f"{ts} - {title}.md"
    filepath = os.path.join(folder, filename)
    
    date_str = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+02:00')
    
    # Build frontmatter
    frontmatter = f"""---
id: {ts}
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
    agents_to_create = [
        {
            "title": "Claude Code",
            "tags": ["agent", "cli", "mcp"],
            "overview": "Claude Code is Anthropic's terminal-native agentic coding tool.",
            "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
        },
        {
            "title": "OpenCode",
            "tags": ["agent", "cli", "open-source"],
            "overview": "OpenCode is an open-source, MIT-licensed AI coding agent.",
            "links": ["202609200758 - OpenCode", "202609202000 - Claude Code"],
        },
        {
            "title": "Cursor",
            "tags": ["agent", "ide"],
            "overview": "Cursor is an AI-native IDE built as a VS Code fork.",
            "links": ["202609202000 - Cursor", "202609202000 - Claude Code"],
        },
        {
            "title": "Codex",
            "tags": ["agent", "cli", "cloud"],
            "overview": "Codex is OpenAI's agent-native coding platform.",
            "links": ["202609202000 - Codex", "202609202000 - Claude Code"],
        },
        {
            "title": "Devin",
            "tags": ["agent", "cloud", "autonomous"],
            "overview": "Devin is Cognition AI's cloud-native autonomous coding agent.",
            "links": ["202609202000 - Devin", "202609202000 - Claude Code"],
        },
    ]
    
    for agent in agents_to_create:
        create_note(
            AGENTS_DIR,
            agent['title'],
            agent['tags'],
            agent['links'],
            agent['overview']
        )
    
    # Create plugin notes
    print("\n  Creating plugin notes...")
    plugins_to_create = [
        {
            "title": "GitHub MCP Server",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "opencode", "hermes", "cursor", "codex", "windsurf", "aider", "gemini-cli", "github-copilot", "kilo-code", "roocode", "jetbrains-junie"],
            "overview": "GitHub's official MCP Server exposes repository, issue, pull request, Actions, and code search capabilities.",
            "links": ["202609202000 - Claude Code", "202609200758 - OpenCode"],
        },
        {
            "title": "Firecrawl MCP Server",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "opencode", "hermes", "cursor", "codex", "windsurf", "aider", "gemini-cli", "github-copilot", "kilo-code", "roocode", "jetbrains-junie"],
            "overview": "The official Firecrawl MCP Server brings web scraping, crawling, and search capabilities.",
            "links": ["202609202000 - Claude Code", "202609200758 - OpenCode"],
        },
        {
            "title": "Context7 MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "opencode", "hermes", "cursor", "codex", "windsurf", "aider", "gemini-cli", "github-copilot", "kilo-code", "roocode", "jetbrains-junie"],
            "overview": "Context7 is an open-source MCP server built by Upstash for up-to-date documentation.",
            "links": ["202609202000 - Claude Code", "202609200758 - OpenCode"],
        },
        {
            "title": "Browser Use MCP",
            "tags": ["plugin", "mcp", "browser"],
            "agents": ["claude-code", "opencode", "hermes", "cursor", "codex", "windsurf", "aider", "gemini-cli", "github-copilot", "kilo-code", "roocode", "jetbrains-junie"],
            "overview": "Browser Use MCP is a local MCP server for browser automation.",
            "links": ["202609202000 - Claude Code", "202609200758 - OpenCode"],
        },
        {
            "title": "Playwright MCP",
            "tags": ["plugin", "mcp", "browser"],
            "agents": ["claude-code", "opencode", "hermes", "cursor", "codex", "windsurf", "aider", "gemini-cli", "github-copilot", "kilo-code", "roocode", "jetbrains-junie"],
            "overview": "Playwright MCP is Microsoft's official MCP server for browser automation.",
            "links": ["202609202000 - Claude Code", "202609200758 - OpenCode"],
        },
        {
            "title": "Hermes Jev Agent Router",
            "tags": ["plugin", "hermes"],
            "agents": ["hermes", "claude-code"],
            "overview": "Jev is a System One decision model from TypeSafe AI for agent routing.",
            "links": ["202609200759 - Hermes Agent", "202609202000 - Claude Code"],
        },
        {
            "title": "Hermes Kanban Dashboard",
            "tags": ["plugin", "hermes"],
            "agents": ["hermes"],
            "overview": "The Kanban Dashboard is a built-in Hermes Agent plugin for multi-agent task management.",
            "links": ["202609200759 - Hermes Agent"],
        },
        {
            "title": "Hermes Curator",
            "tags": ["plugin", "hermes"],
            "agents": ["hermes"],
            "overview": "Curator is a built-in Hermes Agent plugin that manages the skill catalog.",
            "links": ["202609200759 - Hermes Agent"],
        },
        {
            "title": "Hermes Plugin System",
            "tags": ["plugin", "hermes"],
            "agents": ["hermes", "opencode"],
            "overview": "Hermes Agent has a comprehensive plugin system for custom tools and skills.",
            "links": ["202609200759 - Hermes Agent", "202609200758 - OpenCode"],
        },
        {
            "title": "Claude Code Auto Permission",
            "tags": ["plugin", "claude-code"],
            "agents": ["claude-code", "github-copilot"],
            "overview": "Auto Permission is a Claude Code permission mode with server-evaluated tool call permissions.",
            "links": ["202609202000 - Claude Code", "202609202001 - GitHub Copilot Agent"],
        },
    ]
    
    for plugin in plugins_to_create:
        create_note(
            PLUGINS_DIR,
            plugin['title'],
            plugin['tags'],
            plugin['links'],
            plugin['overview'],
            plugin.get('agents')
        )
    
    print("\nStage 1 complete")

if __name__ == '__main__':
    main()