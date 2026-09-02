---
title: Governance
description: Agent OS Governance - L0-L5 hierarchy, risk levels, and authorization matrix
---

# Governance

Agent OS uses a constitutional governance model with L0-L5 hierarchy and zero-trust authorization.

## L0-L5 Hierarchy

```
L0 — GOVERNANCE.md (Constitutional)
    ↓
L1 — CEO / Principal (Orchestration)
    ↓
L2 — Department Agents (PM, Architect, Developer, QA, SRE, Researcher)
    ↓
L3 — Specialist Agents (Azure DevOps, Cloud, AKS, Datadog)
    ↓
L4 — Subagents (Task-scoped)
    ↓
L5 — Tools (az, kubectl, helm, datadog API, github, filesystem)
```

## Fundamental Rule

> **Lower level CANNOT override higher level.**

## Risk Levels

| Level | Description | Approval |
|-------|-------------|----------|
| **LOW** | Code, tests, docs, examples | Auto (agent decides) |
| **MEDIUM** | Dependencies, config, skills, guardrails | Superior review |
| **HIGH** | AGENTS.md, GOVERNANCE.md, guardrails, MCP, agent creation | CEO + Human |

## Authorization Matrix (Symbols)

| Symbol | Meaning |
|--------|---------|
| ✅ | Allowed (auto) |
| ⚠️ | Needs superior approval |
| 🔐 | Needs CEO + Human approval |
| ❌ | Denied permanently |

## Department Agent Matrix (L2)

| Action | PM | Architect | Dev | QA | SRE | Researcher |
|--------|-----|-----------|-----|-----|-----|------------|
| Create Brief/PRD | ✅ | ⚠️ | ❌ | ❌ | ❌ | ⚠️ |
| Approve Tech Spec | ⚠️ | ✅ | ⚠️ | ❌ | ⚠️ | ❌ |
| Write Code | ❌ | ❌ | ✅ | ⚠️ | ❌ | ❌ |
| QA Gate | ❌ | ❌ | ⚠️ | ✅ | ⚠️ | ❌ |
| Provision Infra | ❌ | ⚠️ | ❌ | ❌ | ✅ | ❌ |
| Approve Prod Deploy | ❌ | ⚠️ | ❌ | ❌ | ⚠️ | ❌ |
| Create Datadog Monitor | ❌ | ❌ | ❌ | ⚠️ | ✅ | ❌ |
| Activate LOW Skill | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Propose Skill/Agent | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Azure Specialist Matrix (L3)

| Action | Azure DevOps | Azure Cloud | Azure AKS | Datadog |
|--------|-------------|-------------|-----------|---------|
| Pipeline YAML | ✅ | ❌ | ❌ | ❌ |
| Provision Azure (non-prod) | ❌ | ✅ | ❌ | ❌ |
| Provision Azure (prod) | ❌ | ⚠️ | ❌ | ❌ |
| AKS Setup (non-prod) | ❌ | ❌ | ✅ | ❌ |
| AKS Upgrade (prod) | ❌ | ❌ | 🔐 | ❌ |
| Rollout Workloads | ❌ | ❌ | ✅ | ❌ |
| Datadog Monitors | ❌ | ❌ | ❌ | ✅ |
| SLO/SLI | ❌ | ❌ | ⚠️ | ✅ |

## Guardrails

Global guardrails in `agentsos/guardrails/global/`:
- `scope.md` - Path access per level
- `tools.md` - Tool usage per level
- `authority.md` - Decision authority
- `change-risk-levels.md` - Risk classification

## Proposals

Changes requiring MEDIUM/HIGH approval go to `proposals/`:
- `proposals/skills/` - New skills
- `proposals/agents/` - New agents
- `proposals/rules/` - Guardrail changes
- `proposals/architecture/` - Architecture changes

## Memory System

Knowledge base at `agentsos/memory/knowledge/` (skill-kwonledge, Obsidian-style) with:
- Categories: IaC, DevOps, AI, SRE
- Types: concepts, guides, references, examples
- Promotion pipeline: candidate → knowledge → rule

## Related

- [Architecture Overview](/architecture/overview)
- [Delivery Loop](/architecture/delivery-loop)
- [CEO Agent](/agents/ceo)