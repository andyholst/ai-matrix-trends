#!/usr/bin/env python3
"""
validate-tags.py - Validate tag usage and structure.
Stage 4 of CI pipeline.
"""

import os
import re
import sys

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Valid tags
VALID_TAGS = {
    'agent', 'plugin', 'tool', 'mcp', 'architecture', 'cli', 'tui', 'gateway',
    'config', 'workflow', 'trend', 'signal', 'paper', 'model', 'method',
    'company', 'person', 'event', 'seedling', 'evergreen', 'refactoring', 'deprecated',
    'moc', 'index', 'ai-tools', 'open-source', 'cloud', 'autonomous', 'ide',
    'multi-agent', 'enterprise', 'browser-automation', 'debugging', 'claude-code',
    'hermes', 'opencode', 'codex', 'cursor', 'context-management', 'all-in-one',
    'rag', 'semantic-search', 'token-optimization', 'skills', 'integrations',
    'codebase-intelligence', 'ui', 'protocol', 'a2a', 'transport', 'acp',
    'portability', 'cost-optimization', 'model-routing', 'sub-agent', 'orchestration',
    'delegation', 'agent-teams', 'parallel-execution', 'context-engineering',
    'compaction', 'memory', 'long-horizon', 'hooks', 'git', 'docs', 'code-review',
    'qa', 'automation', 'documentation', 'heating-up', 'stable', 'emerging',
    'tool-calling', 'infrastructure', 'docker', 'personalization', 'rust',
    'spec-driven', 'decision-model', 'composite', 'app-builder', 'no-code',
    'collaboration', 'workspace', 'visual', 'jetbrains', 'preview',
    'personal-assistant', 'code-intelligence', 'ide-plugin', 'aws',
    'google', 'gemini', 'rebrand', 'self-improving', 'messaging',
    'multi-model', 'code-editing', 'event-driven', 'MCP', 'placeholder',
}

# Files to skip
SKIP_FILES = {
    'AGENTS.md',
    '.obsidian/templates/moc.md',
    '.obsidian/templates/agent-profile.md',
    '.obsidian/templates/plugin-profile.md',
    '.obsidian/templates/architecture-pattern.md',
    'scripts/daily-scan-prompt.md',
}

def extract_tags(fm):
    """Extract tags from frontmatter by parsing line by line"""
    tags = []
    lines = fm.split('\n')
    in_tags = False
    
    for line in lines:
        stripped = line.strip()
        
        if stripped == 'tags:':
            in_tags = True
            continue
        
        if in_tags:
            # Check if this is a tag line
            if stripped.startswith('- '):
                tag = stripped[2:].strip()
                # Remove surrounding quotes if present
                if tag.startswith('"') and tag.endswith('"'):
                    tag = tag[1:-1]
                # Skip wikilinks in tags
                if tag.startswith('[[') and tag.endswith(']]'):
                    continue
                # Skip MOC references
                if 'moc' in tag.lower():
                    continue
                # Skip if it looks like a field name
                if tag.endswith(':'):
                    continue
                if tag:
                    tags.append(tag)
            elif stripped == '':
                # Empty line, might be end of tags
                continue
            else:
                # Non-tag line, end of tags section
                in_tags = False
    
    return tags

def validate_file(filepath):
    """Validate tags of a single file"""
    errors = []
    
    if any(skip in filepath for skip in SKIP_FILES):
        return errors
    
    # Skip index files
    if '00 -' in filepath or 'Master Index' in filepath:
        return errors
    
    # Skip MOC files
    if 'MOC-' in filepath:
        return errors
    
    with open(filepath) as f:
        content = f.read()
    
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return errors
    
    fm = fm_match.group(1)
    
    tags = extract_tags(fm)
    
    if not tags:
        errors.append("  Missing or empty tags field")
        return errors
    
    for tag in tags:
        if tag not in VALID_TAGS:
            errors.append(f"  Invalid tag: {tag}")
    
    return errors

def main():
    print("STAGE 4: Tag Validation")
    print("=" * 60)
    
    total_errors = 0
    files_with_errors = 0
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if '/.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                errors = validate_file(filepath)
                if errors:
                    files_with_errors += 1
                    total_errors += len(errors)
                    rel_path = os.path.relpath(filepath, VAULT_DIR)
                    print(f"\n{rel_path}:")
                    for error in errors:
                        print(error)
    
    print(f"\n{'=' * 60}")
    print(f"Files with errors: {files_with_errors}")
    print(f"Total errors: {total_errors}")
    
    if total_errors > 0:
        sys.exit(1)
    else:
        print("✓ All tags valid")
        sys.exit(0)

if __name__ == '__main__':
    os.chdir(VAULT_DIR)
    main()