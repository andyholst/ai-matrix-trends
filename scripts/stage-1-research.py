#!/usr/bin/env python3
"""
Stage 1: Research - Create new agent and plugin notes directly.
Runs as a Python script (no delegate_task needed).
Prevents duplicates by checking ALL vault folders for existing titles.

This is the daily entry point. Add new agents/plugins here to ensure
they are created on the next run (or recreated if deleted).
"""

import os
import re
from datetime import datetime

VAULT_DIR = os.path.expanduser("~/repository/git/ai-matrix-trends")
AGENTS_DIR = os.path.join(VAULT_DIR, "03 - Agents")
PLUGINS_DIR = os.path.join(VAULT_DIR, "04 - Plugins")
ARCH_DIR = os.path.join(VAULT_DIR, "05 - Architecture")
USE_CASES_DIR = os.path.join(VAULT_DIR, "06 - Use Cases")

def get_all_existing_titles():
    """Get ALL note titles across ALL vault folders (prevents cross-folder duplicates)"""
    titles = set()
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root or '/__pycache__' in root:
            continue
        for f in files:
            if f.endswith('.md') and ' - ' in f and not f.startswith('00 -'):
                title = f.split(' - ', 1)[1].replace('.md', '').lower()
                titles.add(title)
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
    """Create a new note file (skips if title exists ANYWHERE in vault)"""
    existing = get_all_existing_titles()
    
    # Check if a note with this title already exists ANYWHERE
    if title.lower() in existing:
        print(f"  ⚠ {title} already exists (somewhere in vault), skipping")
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
    
    # ============================================================
    # AGENTS — Add new agents here to ensure daily coverage
    # ============================================================
    print("\n  Creating agent notes...")
    agents_to_create = [
        # --- Core agents (original) ---
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
        # --- Extended agents (2026 landscape) ---
        {
            "title": "Factory Code",
            "tags": ["agent", "cloud", "enterprise"],
            "overview": "Factory Code is an enterprise-grade autonomous coding agent that builds, tests, and deploys code autonomously.",
            "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
        },
        {
            "title": "Sweep AI",
            "tags": ["agent", "github", "autonomous"],
            "overview": "Sweep AI is a GitHub-integrated AI agent that autonomously creates pull requests from issue descriptions.",
            "links": ["202609202001 - GitHub Copilot Agent", "202609202000 - Claude Code"],
        },
        {
            "title": "Greptile",
            "tags": ["agent", "code-intelligence", "enterprise"],
            "overview": "Greptile is an AI agent that understands entire codebases and provides context-aware code search and generation.",
            "links": ["202609202000 - Cursor", "202609200911 - Amazon Q Developer"],
        },
        {
            "title": "OpenHands",
            "tags": ["agent", "open-source", "autonomous"],
            "overview": "OpenHands (formerly OpenDevin) is an open-source autonomous AI software engineer built for full-stack development.",
            "links": ["202609202000 - Devin", "202609202000 - Claude Code"],
        },
        {
            "title": "Continue.dev",
            "tags": ["agent", "ide", "open-source"],
            "overview": "Continue.dev is an open-source AI code assistant that integrates with VS Code and JetBrains IDEs.",
            "links": ["202609202000 - Cursor", "202609202001 - GitHub Copilot Agent"],
        },
        {
            "title": "Sourcegraph Cody",
            "tags": ["agent", "code-intelligence", "enterprise"],
            "overview": "Cody is Sourcegraph's AI coding agent that leverages the Sourcegraph code graph for deep codebase understanding.",
            "links": ["202609202000 - Cursor", "202609202001 - GitHub Copilot Agent"],
        },
        {
            "title": "Tabnine",
            "tags": ["agent", "code-completion", "enterprise"],
            "overview": "Tabnine is an AI-powered code completion agent that learns from your codebase and provides context-aware suggestions.",
            "links": ["202609202001 - GitHub Copilot Agent", "202609202000 - Cursor"],
        },
        {
            "title": "Mintlify",
            "tags": ["agent", "documentation", "autonomous"],
            "overview": "Mintlify is an AI agent that automatically generates and maintains documentation from code changes.",
            "links": ["202609202000 - Claude Code", "202609200758 - OpenCode"],
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
    
    # ============================================================
    # PLUGINS / MCP SERVERS — Add new plugins here
    # ============================================================
    print("\n  Creating plugin notes...")
    plugins_to_create = [
        # --- Original plugins ---
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
        # --- Extended MCP servers (2026 landscape) ---
        {
            "title": "Slack MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "hermes", "opencode"],
            "overview": "Slack MCP server provides AI agents with access to Slack channels, messages, and user management.",
            "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
        },
        {
            "title": "Atlassian Jira MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "hermes", "opencode", "cursor"],
            "overview": "Atlassian Jira MCP server enables AI agents to create, update, and search Jira issues and projects.",
            "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
        },
        {
            "title": "Airtable MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "hermes", "opencode"],
            "overview": "Airtable MCP server provides AI agents with read/write access to Airtable bases and tables.",
            "links": ["202609202000 - Claude Code", "202609200758 - OpenCode"],
        },
        {
            "title": "GitLab MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "hermes", "opencode", "cursor"],
            "overview": "GitLab MCP server enables AI agents to interact with GitLab repositories, merge requests, and CI/CD pipelines.",
            "links": ["202609202000 - Claude Code", "202609200758 - OpenCode"],
        },
        {
            "title": "Docker MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "hermes", "opencode"],
            "overview": "Docker MCP server provides AI agents with container management, image building, and deployment capabilities.",
            "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
        },
        {
            "title": "Google Workspace MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "hermes", "opencode", "cursor"],
            "overview": "Google Workspace MCP server gives AI agents access to Gmail, Calendar, Drive, and Google Sheets.",
            "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
        },
        {
            "title": "Pinecone MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "hermes", "opencode"],
            "overview": "Pinecone MCP server enables AI agents to query and manage Pinecone vector databases for RAG applications.",
            "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
        },
        {
            "title": "Weaviate MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "hermes", "opencode"],
            "overview": "Weaviate MCP server provides AI agents with vector search and knowledge graph capabilities via Weaviate.",
            "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
        },
        {
            "title": "Neo4j MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "hermes", "opencode"],
            "overview": "Neo4j MCP server enables AI agents to query and manage Neo4j graph databases for relationship analysis.",
            "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
        },
        {
            "title": "Snowflake MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "hermes", "opencode"],
            "overview": "Snowflake MCP server provides AI agents with SQL query capabilities and data warehouse access via Snowflake.",
            "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
        },
        {
            "title": "BigQuery MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "hermes", "opencode"],
            "overview": "BigQuery MCP server enables AI agents to query Google BigQuery datasets and manage data pipelines.",
            "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
        },
        {
            "title": "Asana MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "hermes", "opencode"],
            "overview": "Asana MCP server provides AI agents with project management capabilities via the Asana API.",
            "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
        },
        {
            "title": "Monday.com MCP",
            "tags": ["plugin", "mcp"],
            "agents": ["claude-code", "hermes", "opencode"],
            "overview": "Monday.com MCP server enables AI agents to manage boards, items, and workflows on the Monday.com platform.",
            "links": ["202609202000 - Claude Code", "202609200759 - Hermes Agent"],
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
    
    # ============================================================
    # ARCHITECTURE PATTERNS — Add new patterns here
    # ============================================================
    print("\n  Creating architecture pattern notes...")
    arch_to_create = [
        {
            "title": "ReAct Reasoning and Acting",
            "tags": ["architecture", "reasoning"],
            "overview": "ReAct interleaves reasoning traces and actions, allowing agents to perform dynamic reasoning while interacting with external environments.",
            "links": ["202609202001 - Context Engineering for Long-Horizon Agents", "202609200931 - Adaptive Planning Magentic Orchestration Pattern"],
        },
        {
            "title": "Reflexion",
            "tags": ["architecture", "self-improving"],
            "overview": "Reflexion is a framework where agents reflect on task feedback verbally, maintaining reflective memories to improve subsequent performances.",
            "links": ["202609202001 - Context Engineering for Long-Horizon Agents", "202609200931 - Adaptive Planning Magentic Orchestration Pattern"],
        },
        {
            "title": "Tree of Thought",
            "tags": ["architecture", "reasoning"],
            "overview": "Tree of Thought generalizes chain-of-thought by exploring multiple reasoning paths, using tree search strategies to find optimal solutions.",
            "links": ["202609202001 - Context Engineering for Long-Horizon Agents", "202609200932 - Fan-Out Fan-In Parallel Agent Pattern"],
        },
        {
            "title": "Graph of Thought",
            "tags": ["architecture", "reasoning"],
            "overview": "Graph of Thought extends Tree of Thought by allowing arbitrary graph structures of reasoning, enabling more flexible problem-solving.",
            "links": ["202609202001 - Context Engineering for Long-Horizon Agents", "202609200932 - Fan-Out Fan-In Parallel Agent Pattern"],
        },
        {
            "title": "Mixture of Experts for Agents",
            "tags": ["architecture", "modeling"],
            "overview": "Mixture of Experts routes tasks to specialized sub-models or agents, each expert in a specific domain or task type.",
            "links": ["2026092032 - Tiered Routing Model Cascade Pattern", "202609202002 - Multi-Agent Orchestration with Guardrail Layering"],
        },
        {
            "title": "Speculative Decoding",
            "tags": ["architecture", "optimization"],
            "overview": "Speculative Decoding uses a smaller draft model to generate tokens in parallel, then verifies them with the main model for faster inference.",
            "links": ["2026092032 - Tiered Routing Model Cascade Pattern", "202609202020 - Orchestrator-Worker Delegation Pattern"],
        },
        {
            "title": "Guardrails and Safety Layers",
            "tags": ["architecture", "safety"],
            "overview": "Guardrails enforce boundaries on agent actions through validation layers, preventing unauthorized or unsafe operations.",
            "links": ["202609202002 - Multi-Agent Orchestration with Guardrail Layering", "202609202003 - MCP Apps Interactive UI Protocol"],
        },
        {
            "title": "Prompt Caching and KV Cache",
            "tags": ["architecture", "optimization"],
            "overview": "Prompt Caching stores key-value pairs from previous computations to avoid redundant processing, reducing latency and cost.",
            "links": ["202609202021 - Context Compaction and Structured Note-Taking", "2026092032 - Tiered Routing Model Cascade Pattern"],
        },
    ]
    
    for pattern in arch_to_create:
        create_note(
            ARCH_DIR,
            pattern['title'],
            pattern['tags'],
            pattern['links'],
            pattern['overview']
        )
    
    print("\nStage 1 complete")

if __name__ == '__main__':
    main()
