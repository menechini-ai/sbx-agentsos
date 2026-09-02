# Skill Kwonledge

Knowledge base repository with Obsidian-style skills and documentation, including best practices from official documentation.

## Project Structure

```
skill-kwonledge/
├── skills/
│   ├── knowledge-manager/   # Create full category structures
│   │   ├── SKILL.md
│   │   ├── evals/
│   │   └── scripts          # deduplicate.py, update_schema.py
│   └── knowledge-create/     # Create validated individual notes
│       ├── SKILL.md
│       ├── evals/
│       ├── templates/       # concept, pattern, runbook, architecture
│       ├── validators/       # JSON Schema
│       └── hooks/           # Post-creation actions
├── examples/
│   └── knowledge/
│       ├── IaC/           # terraform, terragrunt, ansible
│       ├── DevOps/         # kubernetes, argocd
│       ├── AI/             # deepagents, langchain-ai
│       └── patterns/       # cross-category patterns
├── AGENTS.md
├── .gitignore
└── README.md
```

## Skills Overview

| Skill | Use Case | Output |
|-------|----------|--------|
| **knowledge-manager** | "add kubernetes" or "add IaC/ansible" | Full folder structure |
| **knowledge-create** | "create pattern for X" | Single validated note |

### When to Use Each

**knowledge-manager** - Create complete category structure:
- "add [topic]" → e.g., `examples/knowledge/ansible/`
- "add [category]/[topic]" → e.g., `examples/knowledge/ansible/` (with IaC category)
- "find duplicates" → deduplication check
- "clean up" → optimize cross-links

**Supported Categories:**
| Category | Topics |
|----------|-------|
| IaC | terraform, terragrunt, ansible, puppet, chef |
| DevOps | kubernetes, argocd, docker, helm |
| AI | deepagents, langchain, langgraph |

**knowledge-create** - Create validated individual notes:
- "create runbook for incident response"
- "document pattern for blue-green deployment"
- "capture architecture for e-commerce"

## Quick Start

### Add New Knowledge (with Category)

```bash
# Use knowledge-manager skill with category
"add IaC/ansible"        → examples/knowledge/IaC/ansible/
"add DevOps/kubernetes" → examples/knowledge/DevOps/kubernetes/
"add AI/langchain"       → examples/knowledge/AI/langchain-ai/
```

### Create Individual Note (Validated)

```bash
# Use knowledge-create skill
"create pattern for DRY configs in Terragrunt"
→ Creates examples/knowledge/patterns/terragrunt-dry-configs.md
```

## Knowledge Note Structure

### Folder Organization

```
examples/knowledge/<category>/<topic>/
├── concepts/       # Explanatory content
├── guides/         # How-to content
├── references/     # Quick references/commands
├── examples/       # Code examples from official docs
└── INDEX.md        # Topic index
```

### Note Types (knowledge-create)

| Type | Template | Purpose |
|------|----------|---------|
| concept | concept.md | Definitions, ideas |
| pattern | pattern.md | Solved problems |
| runbook | runbook.md | Procedures |
| architecture | architecture.md | System designs |

## Schema

All notes follow a formal schema:

```yaml
---
id: kubernetes.pods
title: Kubernetes Pods
type: concept
category: kubernetes
domain: kubernetes
tags:
  - containers
  - pods
summary: Brief 1-2 sentence summary
related:
  - [[kubernetes.architecture]]
  - [[kubernetes.services]]
source: https://kubernetes.io/docs/
status: active
version: "1.0.0"
created: 2026-04-27
updated: 2026-04-28
confidence: high
quality_score: 85
---
```

## Available Knowledge

| Topic | Notes | Best Practices |
|-------|-------|----------------|
| Kubernetes | 8 | ✅ Config good practices |
| Terraform | 4 | ✅ Collaborative IaC |
| Terragrunt | 3 | ✅ DRY configs |
| Ansible | 3 | ✅ Best practices |
| ArgoCD | 4 | ✅ GitOps practices |
| Deep Agents | 4 | - |
| LangChain | 4 | - |
| Patterns | 2 | ✅ ClawTeam, Terragrunt DRY |

### Topics Details

**IaC** (Infrastructure as Code) - `examples/knowledge/IaC/`
- Terraform: architecture, basics, commands, ec2-example
- Terragrunt: overview, commands, vpc-example, getting-started
- Ansible: overview, directory-layout, commands

**DevOps** - `examples/knowledge/DevOps/`
- Kubernetes: architecture, pods, deployments, services, ingress, helm, configmaps-secrets
- ArgoCD: architecture, basics, commands

**AI** - `examples/knowledge/AI/`
- Deep Agents: architecture, basics, commands, quickstart
- LangChain: fundamentals, getting-started, components, lcel-example

**Patterns** - `examples/knowledge/patterns/`
- clawteam (Agent Swarm Intelligence)
- terragrunt-dry-configs

## Best Practices Sources

- [Kubernetes Configuration Good Practices](https://kubernetes.io/blog/2025/11/25/configuration-good-practices/)
- [Terraform Recommended Practices](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices)
- [ArgoCD Best Practices](https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/)
- [Terragrunt Documentation](https://docs.terragrunt.com/)

## Scripts

### Deduplication Check

```bash
python3 skills/knowledge-manager/scripts/deduplicate.py examples/knowledge/
```

### Schema Update

```bash
python3 skills/knowledge-manager/scripts/update_schema.py
```

## Contributing

1. Use `knowledge-manager` for full categories
2. Use `knowledge-create` for validated individual notes
3. Follow schema and templates
4. Reference official documentation

## Related

- See `AGENTS.md` for detailed agent instructions
- Skill framework: `~/.config/opencode/skills/skill-creator/`
