---
title: Skills Overview
description: All available skills in Agent OS - organized by delivery phase
---

# Skills Overview

Agent OS skills are lean (~60 lines each) and follow the SKILL.md format with structured frontmatter. They map to the delivery loop phases.

## Skills by Phase

### Clarify Phase (PM)

| Skill | Purpose |
|-------|---------|
| `brainstorming` | Explore intent, requirements, design |
| `brief-creation` | Create structured briefs |
| `prd-writing` | Write Product Requirements Documents |

### Plan Phase (Architect + PM)

| Skill | Purpose |
|-------|---------|
| `tech-spec` | Write technical specifications |
| `adr-writing` | Record Architecture Decision Records |
| `sprint-planning` | Plan sprints with capacity |

### Build Phase (Developer)

| Skill | Purpose |
|-------|---------|
| `coding` | Implementation workflow |
| `dev-story` | Implement a user story |
| `agentos-build` | Build orchestration |

### Verify Phase (QA + SRE)

| Skill | Purpose |
|-------|---------|
| `qa-gate` | Quality verification gate |
| `review` | Code/technical review |

### Learn Phase (All)

| Skill | Purpose |
|-------|---------|
| `retrospective` | Learning capture and improvement |

### Cross-Cutting Skills

| Skill | Purpose |
|-------|---------|
| `session-handoff` | Context preservation between sessions |
| `research` | Technical research |
| `documentation` | Documentation writing |
| `agentos-help` | System guidance |

### Azure/SRE Skills

| Skill | Purpose |
|-------|---------|
| `pipeline-yaml` | Azure DevOps pipeline creation |
| `resource-provisioning` | Azure resource provisioning |
| `cluster-setup` | AKS cluster management |
| `rollout-strategies` | Deployment strategies (rolling, canary, blue-green) |
| `monitor-setup` | Datadog monitor configuration |
| `integration-setup` | Azure+Datadog integration |

## Skill Format

All skills follow this structure:

```yaml
---
name: skill-name
description: One-line purpose
triggers: ["trigger phrases"]
tools: [list, of, tools]
---
```

## Usage

```
→ "Use [skill-name] to [task]"
→ Skill loads instructions and guides execution
```

## Related

- [Clarify Skills](/skills/clarify)
- [Plan Skills](/skills/plan)
- [Build Skills](/skills/build)
- [Verify Skills](/skills/verify)
- [Azure Skills](/skills/azure)