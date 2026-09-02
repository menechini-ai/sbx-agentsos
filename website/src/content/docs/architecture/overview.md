---
title: Architecture Overview
description: Agent OS architecture with L0-L5 governance
---

# Architecture Overview

Agent OS is a modular AI-agent architecture with formal governance, persistent memory, and reusable skills.

## Key Differentiator

**Constitutional Governance** (L0-L5) combined with **Agent OS Delivery Loop** (Clarify→Plan→Build→Verify→Learn).

## Architecture Layers

```
L0 GOVERNANCE (docs/GOVERNANCE.md)
 └─ L1 CEO (ceo/)
     ├─ L2 PM (pm/)
     ├─ L2 Architect (architect/)
     ├─ L2 Developer (developer/)
     ├─ L2 QA (qa/)
     ├─ L2 Researcher (researcher/)
     └─ L2 SRE (sre/)
         ├─ L3 Azure DevOps
         ├─ L3 Azure Cloud
         ├─ L3 Azure AKS
         └─ L3 Datadog
             └─ L4 Subagents (on-demand)
                 └─ L5 Tools (az, kubectl, helm, datadog API)
```

## Layer Responsibilities

### L0 — Governance (Constitutional)
- Defines hierarchy and authority matrix
- Zero-trust: lower levels cannot override higher
- Risk levels: LOW (auto) → MEDIUM (review) → HIGH (CEO + human)

### L1 — CEO / Principal
- Orchestration and delegation
- Approval for MEDIUM/HIGH risk changes
- Cross-department coordination

### L2 — Department Agents
- **PM**: Product management, briefs, PRDs, sprint planning
- **Architect**: Tech specs, ADRs, stack decisions
- **Developer**: Code implementation, testing
- **QA**: Quality assurance, test plans, QA gates
- **Researcher**: Research, analysis, synthesis
- **SRE**: Infrastructure, reliability, observability

### L3 — Specialist Agents
- **Azure DevOps**: Pipelines YAML, repos, boards
- **Azure Cloud**: Resources, networking, IaC (Bicep/Terraform)
- **Azure AKS**: Clusters, node pools, rollouts
- **Datadog**: Monitoring, tracing, logs, SLOs

### L4 — Subagents
- On-demand execution for specific tasks
- Spawned by L3 when complexity exceeds batch size

### L5 — Tools / MCP
- Azure CLI, kubectl, helm, Datadog API
- GitHub, filesystem, terminal
- Authorized via MCP policies

## Separation Principle

```
GOVERNANCE.md  → "WHO I AM AND WHAT ARE MY LIMITS"
AGENTS.md      → "WHO I AM AND HOW I BEHAVE"
SKILL.md       → "HOW I EXECUTE A TASK"
memory/knowledge      → "WHAT I LEARNED"
work/          → "WHAT I'M PRODUCING"
docs/          → "HOW THE SYSTEM WORKS"
```

## Single Source of Truth

- **memory/knowledge**: External wiki (Markdown + SQLite)
- **No duplication**: Don't create parallel memory systems
- **Structured contracts**: INPUT/OUTPUT envelopes for communication

## Related

- [Delivery Loop](/architecture/delivery-loop)
- [Governance](/architecture/governance)
- [Agents](/agents/ceo)