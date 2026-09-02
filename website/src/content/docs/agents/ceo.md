---
title: CEO Agent
description: L1 Orchestrator - delegation, coordination, business decisions
---

# CEO Agent (L1)

## Overview

The CEO agent is the L1 orchestrator responsible for high-level coordination, delegation to L2 department agents, and business decisions. It operates above the department level with broad scope.

## Responsibilities

- **Delegation**: Assign tasks to appropriate L2 agents (PM, Architect, Developer, QA, SRE, Researcher)
- **Coordination**: Manage cross-department initiatives and dependencies
- **Decision Making**: Approve MEDIUM/HIGH risk proposals, resolve conflicts
- **Governance**: Work with L0 GOVERNANCE.md for constitutional changes

## Scope

| Path | Access |
|------|--------|
| `agents/` | All departments |
| `skills/` | All skills |
| `work/` | All production |
| `memory/knowledge/` | Read via retrieval |
| `GOVERNANCE.md` | Propose changes (requires human approval) |
| `guardrails/` | Propose changes (requires human approval) |

## Tools

- `filesystem.read` - Full filesystem read
- `filesystem.write` - Write except security paths
- `github.read` / `github.write` - Issues, PRs, branches
- `terminal` - Coordination commands

## Risk Level

| Action | Risk | Approval |
|--------|------|----------|
| Modify GOVERNANCE.md | HIGH | Human |
| Modify guardrails | HIGH | Human |
| Approve MEDIUM risk | MEDIUM | CEO (self) |
| Delegate to L2 | LOW | Auto |

## Delegation Flow

```
User Request
    │
    ▼
CEO (L1) - Clarify & Delegate
    │
    ├─► PM (L2) - Clarify/Plan
    ├─► Architect (L2) - Tech Spec
    ├─► Developer (L2) - Build
    ├─► QA (L2) - Verify
    ├─► SRE (L2) - Infra/Platform
    └─► Researcher (L2) - Research
```

## Key Skills

- `session-handoff` - Preserve context across sessions
- `research` - Market/competitive analysis
- `agentos-help` - System guidance

## Related

- [Architecture Overview](/architecture/overview)
- [Delivery Loop](/architecture/delivery-loop)
- [Governance](/architecture/governance)