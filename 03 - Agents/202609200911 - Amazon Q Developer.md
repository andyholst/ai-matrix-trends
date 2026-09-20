---
id: 202609200911
created: 2026-09-20T09:11:00+02:00
tags:
  - agent
  - aws
  - enterprise
  - ide-plugin
links:
  - "[[202609202003 - AWS Kiro]]"
  - "[[202609202001 - GitHub Copilot Agent]]"
---

# Amazon Q Developer

## Overview
Amazon Q Developer is AWS's generative AI-powered coding assistant that provides agentic coding capabilities across IDE plugins (VS Code, JetBrains, Visual Studio, Eclipse) and the command line. It autonomously implements features, documents code, tests, reviews, refactors, and performs software upgrades. Note: AWS announced end of support for Q Developer IDE plugins on April 30, 2027, with capabilities migrating to AWS Kiro.

## Installation
```bash
# VS Code extension
code --install-extension AmazonWebServices.amazon-q-vscode

# JetBrains plugin
# Install from JetBrains Marketplace: Amazon Q

# CLI installation
npm install -g @aws-amplify/q-developer-cli
# or download from https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html
```

## Core Capabilities
- Agentic coding: autonomous feature implementation, testing, review, refactoring
- Code transformation for .NET, mainframe, and VMware workloads
- Integration with AWS services and infrastructure
- Multi-IDE support: VS Code, JetBrains, Visual Studio, Eclipse
- CLI for terminal-based workflows
- Free tier available with AWS account

## Configuration
```json
// .aws/q-developer/config.json
{
  "model": "claude-sonnet-4",
  "region": "us-east-1",
  "agentMode": "autonomous",
  "permissions": {
    "shell": "ask",
    "fileWrite": "ask",
    "network": "restricted"
  }
}
```

## Key Plugins/Extensions
- VS Code extension (Amazon Q Developer)
- JetBrains plugin (IntelliJ, PyCharm, WebStorm)
- Visual Studio extension
- Eclipse plugin
- AWS Toolkit integration

## Strengths
- Deep AWS ecosystem integration
- Multi-IDE coverage including enterprise IDEs (Visual Studio, Eclipse)
- Code transformation capabilities for legacy workloads
- Free tier lowers barrier to entry
- Agentic capabilities across full SDLC

## Weaknesses
- IDE plugin support ending April 2027 (migrating to Kiro)
- Less mature agentic workflow compared to Claude Code or Codex
- AWS-centric — less useful for non-AWS environments
- Smaller community and plugin ecosystem

## Use Cases
- AWS-centric development teams
- Enterprise developers needing IDE-integrated AI
- Legacy code transformation (.NET, mainframe)
- Teams already invested in AWS ecosystem

## Related Agents
- [[202609202003 - AWS Kiro]]
- [[202609202001 - GitHub Copilot Agent]]

## Sources
- [Official Site](https://aws.amazon.com/q/developer/)
- [Agentic Coding Experience](https://aws.amazon.com/q/developer/build/)
- [End of Support Announcement](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/)
