---
title: PM Agent
description: L2 Product Manager - Clarify & Plan phases, briefs, PRDs
---

# PM Agent (L2)

## Overview

The Product Manager (PM) agent handles the **Clarify** and **Plan** phases of the delivery loop. They create briefs, write PRDs, create user stories, and plan sprints.

## Responsibilities

- **Brief Creation**: Define objectives, constraints, and success criteria
- **PRD Writing**: Document feature requirements with acceptance criteria
- **Story Creation**: Break work into implementable user stories
- **Sprint Planning**: Organize work into sprints with capacity planning

## Scope

| Path | Access |
|------|--------|
| `agents/pm/` | Full |
| `skills/` | Use (brief-creation, prd-writing, sprint-planning) |
| `work/pm/` | Full |
| `memory/knowledge/` | Read via retrieval |
| `agents/` (other) | Denied |
| `GOVERNANCE.md` | Denied |

## Key Skills

| Skill | Purpose |
|-------|---------|
| `brief-creation` | Create structured briefs (Objective/Constraints/Success) |
| `prd-writing` | Write Product Requirements Documents |
| `sprint-planning` | Plan sprints with stories and capacity |
| `agentos-help` | System guidance |

## Output Templates

- [Brief Template](/templates/brief)
- [PRD Template](/templates/prd)
- [Stories Template](/templates/stories)
- [Sprint Template](/templates/sprint)

## Delivery Loop Role

```
Clarify (PM) → Plan (PM + Architect) → Build (Developer) → Verify (QA + SRE) → Learn (All)
```

The PM is involved in **Clarify** (brief) and **Plan** (PRD, stories, sprint) phases. They coordinate with the Architect for tech specs and with all implementers for planning accuracy.

## Related

- [Delivery Loop](/architecture/delivery-loop)
- [Build Your First Change](/build-your-first-change)