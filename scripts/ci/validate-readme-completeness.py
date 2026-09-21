#!/usr/bin/env python3
"""
validate-readme-completeness.py - Validate README.md contains all required sections
and that they match the actual vault data.
Stage 10 of CI pipeline.

Checks:
1. README has ## 🛠️ Agent Tools & CLIs section
2. All agents from 03 - Agents/ are listed in the README section
3. All agents in the README section exist as files
4. Agent Master Index exists and lists all agents
5. Plugin Master Index exists and lists all plugins
6. README "Plugins by Agent" section exists
"""

import os
import re
import sys
import json

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
README_FILE = os.path.join(VAULT_DIR, 'README.md')
DATA_FILE = os.path.join(VAULT_DIR, '08 - Projects', 'trend-data.json')
AGENTS_DIR = os.path.join(VAULT_DIR, '03 - Agents')
PLUGINS_DIR = os.path.join(VAULT_DIR, '04 - Plugins')
AGENTS_INDEX = os.path.join(AGENTS_DIR, '00 - Agent Master Index.md')
PLUGINS_INDEX = os.path.join(PLUGINS_DIR, '00 - Plugin Master Index.md')


def load_trend_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {'items': {}}


def extract_section(content, section_header):
    """Extract a ## section from markdown content"""
    pattern = re.escape(section_header) + r'\n(.*?)(?=\n## |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1) if match else None


def extract_link_targets(section_content):
    """Extract all link targets (paths) from a section"""
    if not section_content:
        return set()
    targets = set()
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', section_content):
        path = match.group(2)
        if path.startswith('http'):
            continue
        # Normalize: decode %20, strip ./
        clean = path.replace('%20', ' ').replace('./', '').replace('../', '')
        targets.add(clean.lower())
        # Also add just the filename
        fname = os.path.basename(clean)
        if fname.endswith('.md'):
            fname = fname[:-3]
        targets.add(fname.lower())
    return targets


def get_folder_note_files(folder_path):
    """Get all note filenames in a folder (excluding 00 - indexes)"""
    notes = set()
    if not os.path.exists(folder_path):
        return notes
    for f in os.listdir(folder_path):
        if f.endswith('.md') and not f.startswith('00 -'):
            notes.add(f[:-3].lower())  # strip .md
    return notes


def main():
    print("STAGE 10: README Completeness Validation")
    print("=" * 60)

    errors = []

    # Check README exists
    if not os.path.exists(README_FILE):
        errors.append("README.md not found")
        print(f"\n{'=' * 60}")
        print(f"✗ FAIL: {errors[0]}")
        sys.exit(1)

    with open(README_FILE) as f:
        readme_content = f.read()

    # === Check 1: Agent Tools & CLIs section exists ===
    print("\n  Checking: Agent Tools & CLIs section exists...")
    agent_tools_section = extract_section(readme_content, '## 🛠️ Agent Tools & CLIs')
    if not agent_tools_section:
        errors.append("README missing '## 🛠️ Agent Tools & CLIs' section")
        print("    ✗ Section not found")
    else:
        print("    ✓ Section found")

    # === Check 2: All agent files are in README ===
    print("\n  Checking: All agent files listed in README...")
    agent_files = get_folder_note_files(AGENTS_DIR)
    readme_agent_targets = extract_link_targets(agent_tools_section) if agent_tools_section else set()
    missing_from_readme = agent_files - readme_agent_targets
    if missing_from_readme:
        errors.append(f"Agent files missing from README: {missing_from_readme}")
        print(f"    ✗ Missing: {missing_from_readme}")
    else:
        print(f"    ✓ All {len(agent_files)} agent files listed")

    # === Check 3: All README agent links resolve to files ===
    print("\n  Checking: All README agent links resolve...")
    if agent_tools_section:
        for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', agent_tools_section):
            path = match.group(2).replace('%20', ' ')
            if path.startswith('http'):
                continue
            full_path = os.path.join(VAULT_DIR, path)
            if not os.path.isfile(full_path):
                errors.append(f"README agent link broken: {path}")
                print(f"    ✗ Broken: {path}")

    # === Check 4: Agent Master Index exists and is complete ===
    print("\n  Checking: Agent Master Index completeness...")
    if not os.path.exists(AGENTS_INDEX):
        errors.append("Agent Master Index not found")
        print("    ✗ Not found")
    else:
        with open(AGENTS_INDEX) as f:
            index_content = f.read()
        index_targets = extract_link_targets(index_content)
        missing_from_index = agent_files - index_targets
        if missing_from_index:
            errors.append(f"Agent files missing from Agent Master Index: {missing_from_index}")
            print(f"    ✗ Missing: {missing_from_index}")
        else:
            print(f"    ✓ All {len(agent_files)} agents indexed")

    # === Check 5: Plugin Master Index exists and is complete ===
    print("\n  Checking: Plugin Master Index completeness...")
    plugin_files = get_folder_note_files(PLUGINS_DIR)
    if not os.path.exists(PLUGINS_INDEX):
        errors.append("Plugin Master Index not found")
        print("    ✗ Not found")
    else:
        with open(PLUGINS_INDEX) as f:
            plugin_index_content = f.read()
        index_plugin_targets = extract_link_targets(plugin_index_content)
        missing_plugins = plugin_files - index_plugin_targets
        if missing_plugins:
            errors.append(f"Plugin files missing from Plugin Master Index: {missing_plugins}")
            print(f"    ✗ Missing: {missing_plugins}")
        else:
            print(f"    ✓ All {len(plugin_files)} plugins indexed")

    # === Check 6: Plugins by Agent section exists ===
    print("\n  Checking: Plugins by Agent section exists...")
    plugins_by_agent = extract_section(readme_content, '## 🔌 Plugins by Agent')
    if not plugins_by_agent:
        errors.append("README missing '## 🔌 Plugins by Agent' section")
        print("    ✗ Section not found")
    else:
        print("    ✓ Section found")

    # === Summary ===
    print(f"\n{'=' * 60}")
    if errors:
        print(f"✗ FAIL: {len(errors)} issues detected")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("✓ README is complete and consistent with vault data")
        sys.exit(0)


if __name__ == '__main__':
    main()
