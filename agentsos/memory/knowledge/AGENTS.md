# AGENTS.md - Skill Kwonledge

## Project Overview

This is a **knowledge base repository** containing Obsidian-style knowledge notes and skills for managing them.

## Repository Structure

```
skill-kwonledge/
├── skills/
│   ├── knowledge-manager/   # Create full category structures
│   │   ├── SKILL.md
│   │   ├── evals/
│   │   ├── scripts          # deduplicate.py, update_schema.py
│   │   └── resources/
│   └── knowledge-create/     # Create validated individual notes
│       ├── SKILL.md
│       ├── evals/
│       ├── templates/       # concept, pattern, runbook, architecture
│       ├── validators/     # JSON Schema
│       └── hooks/          # Post-creation actions
├── examples/
│   └── knowledge/
│       ├── IaC/           # terraform, terragrunt, ansible
│       ├── DevOps/         # kubernetes, argocd
│       ├── AI/             # deepagents, langchain-ai
│       └── patterns/      # cross-category patterns
├── AGENTS.md
├── .gitignore
└── README.md
```

---

## Topics by Category

### IaC (Infrastructure as Code)
- **Terraform**: `examples/knowledge/IaC/terraform/`
- **Terragrunt**: `examples/knowledge/IaC/terragrunt/`
- **Ansible**: `examples/knowledge/IaC/ansible/`

### DevOps
- **Kubernetes**: `examples/knowledge/DevOps/kubernetes/`
- **ArgoCD**: `examples/knowledge/DevOps/argocd/`

### AI
- **Deep Agents**: `examples/knowledge/AI/deepagents/`
- **LangChain**: `examples/knowledge/AI/langchain-ai/`

### Patterns (cross-category)
- `examples/knowledge/patterns/`

---

## Skills Overview

### knowledge-manager

Create full category structures.

**Trigger Phrases:**
- "add [topic]" → e.g., "add kubernetes", "add ansible"
- "add [category]/[topic]" → e.g., "add IaC/ansible", "add DevOps/kubernetes"
- "document [subject]"
- "create knowledge"

**Category Format:**
| Request | Category | Topic |
|---------|---------|-------|
| "add IaC/ansible" | IaC | ansible |
| "add DevOps/kubernetes" | DevOps | kubernetes |
| "add AI/langchain" | AI | langchain |

**Refactor Mode:**
- "find duplicates"
- "clean up"
- "deduplicate"

**Output:** Full folder structure with concepts/, guides/, references/, examples/

### knowledge-create

Create validated individual notes with templates.

**Trigger Phrases:**
- "create pattern for [topic]"
- "create runbook for [topic]"
- "create concept about [topic]"
- "document [subject] with pattern"

**Output:** Single .md file with:
- Valid frontmatter
- Template applied (concept/pattern/runbook/architecture)
- Related links

---

## When to Use Each Skill

| Use Case | Skill |
|----------|-------|
| "add kubernetes" | knowledge-manager |
| "create pattern for DRY configs" | knowledge-create |
| "find duplicates" | knowledge-manager |
| "create runbook for incident response" | knowledge-create |

---

## Primary Skill: knowledge-manager

This is the main skill for knowledge management in this repo.

### Trigger Phrases

**CREATE Mode:**
- "add [topic]" - e.g., "add ansible"
- "add [category]/[topic]" - e.g., "add IaC/ansible"
- "document [subject]"
- "research [topic]"
- "learn about"

**REFACTOR Mode:**
- "find duplicates"
- "merge notes"
- "clean up"
- "deduplicate"

### Usage

```bash
# With category:
"add IaC/ansible" → examples/knowledge/IaC/ansible/
"add DevOps/kubernetes" → examples/knowledge/DevOps/kubernetes/
"add AI/langchain" → examples/knowledge/AI/langchain-ai/

# Without category (creates in root):
"add ansible" → examples/knowledge/ansible/ (if no category)

# Patterns (cross-category):
"create pattern for DRY" → examples/knowledge/patterns/terragrunt-dry-configs.md
```

---

## Scripts

### Deduplicate Check

```bash
python3 skills/knowledge-manager/scripts/deduplicate.py examples/knowledge/
```

### Update Schema

```bash
python3 skills/knowledge-manager/scripts/update_schema.py
```

---

## Knowledge Note Schema

All notes follow a formal schema:

```yaml
---
id: kubernetes.pods
title: Kubernetes Pods
type: concept
category: kubernetes
tags:
  - containers
  - pods
aliases:
  - k8s pods
status: active
version: "1.0.0"
created: 2026-04-27
updated: 2026-04-28
confidence: high
source: docs
inputs: []
outputs: []
dependencies: []
quality_score: 85
---
```

### Schema Fields

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `id` | Text | Yes | Unique ID (e.g., `kubernetes.pods`) |
| `title` | Text | Yes | Human-readable title |
| `type` | Text | Yes | concept/guide/reference/example |
| `category` | Text | Yes | Knowledge category |
| `tags` | List | Yes | Topics for filtering |
| `aliases` | List | No | Alternative names |
| `status` | Text | Yes | active/draft/done |
| `version` | Text | Yes | Semantic version |
| `created` | Date | Yes | Creation date |
| `updated` | Date | Yes | Last update |
| `confidence` | Text | Yes | high/medium/low |
| `source` | Text | Yes | docs/internal/external |
| `inputs` | List | No | Expected inputs |
| `outputs` | List | No | Expected outputs |
| `dependencies` | List | No | Related notes |
| `quality_score` | Number | No | Quality (0-100) |

---

## Skill Anatomy Reference

For creating new skills in this repo, follow this pattern based on `skill-creator` framework:

### Basic Structure

```
skills/<skill-name>/
├── SKILL.md              # Main skill file (REQUIRED)
├── evals/
│   └── evals.json       # Test cases
���── resources/
    ├── template.md     # Output template
    └── quality_rules.md # Quality standards
```

### SKILL.md Required Elements

```yaml
---
name: <skill-name>
description: <detailed "pushy" description with triggers>
triggers: ["phrase1", "phrase2", "phrase3"]
tools: [filesystem, read, write]
category: <domain>
---

# <Skill Name>

## Purpose
<One sentence on what this skill does>

## When to use
- Trigger when user says X
- Trigger when user wants Y
- Also trigger when Z

## Instructions

### Step 1: <Action>
<Detailed instructions>

## Output Format
<Expected output structure>

## Examples
**Example 1:**
Input: <user prompt>
Output: <expected result>
```

---

## Available Knowledge Topics

| Topic | Notes | Best Practices |
|-------|-------|--------------|
| Kubernetes | 8 | ✅ Config good practices |
| Terraform | 4 | ✅ Collaborative IaC |
| Terragrunt | 3 | ✅ DRY configs |
| Ansible | 3 | ✅ Best practices |
| ArgoCD | 4 | ✅ GitOps practices |
| Deep Agents | 4 | - |
| LangChain | 4 | - |

### Best Practices Sources

- **Kubernetes**: [Configuration Good Practices](https://kubernetes.io/blog/2025/11/25/configuration-good-practices/)
- **Terraform**: [Recommended Practices](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices)
- **ArgoCD**: [Best Practices](https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/)

---

## Tips for Agents

### Creating New Knowledge
1. Use `knowledge-manager` skill
2. Request format: "add [topic name]"
3. Creates folder structure automatically with examples from official docs
4. Example: `add docker` → creates `knowledge/docker/`

### Writing Notes
- Use wiki-style links: `[[topic-name]]`
- Group notes by type: `concepts/`, `guides/`, `references/`, `examples/`
- Include practical examples in Usage sections
- Update `INDEX.md` after adding new notes
- NEVER leave empty sections in notes
- Use official documentation for examples

### Conventions
- Category folder = topic name (lowercase, hyphen-separated)
- File path: `knowledge/<category>/<type>/<slug>.md`
- Frontmatter fields: All schema fields required
- Date format: YYYY-MM-DD

---

## Adding New Topics

1. Use the `knowledge-manager` skill
2. Request: "add [topic name]"
3. Skill creates folder structure automatically
4. Use official docs for examples

Example flows:

```bash
# Add new topic
"add docker"
→ Creates knowledge/docker/ with concepts/, guides/, references/, examples/, INDEX.md

# Document with best practices
"document Terraform with best practices"
→ Creates knowledge/terraform/ with collaborative IaC workflow

# Find duplicates
"check for duplicates"
→ Runs deduplicate.py script
```

---

## Skill Creation Best Practices

Based on the `skill-creator` framework:

### Trigger Pattern

```yaml
triggers: [
  "add note",
  "document this",
  "create knowledge",
  "research",
  "learn about"
]
```

### Testing Skills

Create `evals/evals.json` with realistic test cases:

```json
{
  "skill_name": "example-skill",
  "description": "What this skill does",
  "evals": [
    {
      "id": 1,
      "prompt": "User task prompt",
      "expected_output": "Description of expected result",
      "files": [],
      "assertions": []
    }
  ]
}
```

### Output Quality Checklist

- [ ] Frontmatter complete (all schema fields)
- [ ] All 7 sections present (Overview, Purpose, Content, Usage, Relationships, Notes, References)
- [ ] No empty sections
- [ ] At least one [[link]] in Relationships
- [ ] Practical examples in Usage section
- [ ] INDEX.md updated for category
- [ ] Best practices from official docs

---

## Related Files

- See `skill-creator` in `~/.config/opencode/skills/skill-creator/` for full skill creation guide
- See `README.md` for project overview
- Skill path: `~/.config/opencode/skills/skill-creator/`

---

## Quick Reference

| Task | Command |
|-----|---------|
| Add knowledge | "add [topic]" |
| Document subject | "document [subject]" |
| Find duplicates | "find duplicates" |
| Check with docs | "use official documentation" |

---

*Last updated: 2026-04-28*