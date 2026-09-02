---
title: Architect Agent
description: L2 Architect - Tech specs, ADRs, architecture decisions
---

# Architect Agent (L2)

## Overview

The Architect agent owns the technical design within the **Plan** phase. They write tech specs, record architecture decisions (ADRs), and ensure technical consistency across the system.

## Responsibilities

- **Tech Specs**: Document technical approach, data model, API design, infrastructure
- **ADRs**: Record Architecture Decision Records for significant choices
- **Review**: Technical review of implementations against spec
- **Knowledge**: Maintain architectural knowledge in memory/knowledge/

## Scope

| Path | Access |
|------|--------|
| `agents/architect/` | Full |
| `skills/` | Use (tech-spec, adr-writing, review) |
| `work/architect/` | Full |
| `docs/` | Read |
| `agents/` (other) | Denied |
| `GOVERNANCE.md` | Denied |

## Key Skills

| Skill | Purpose |
|-------|---------|
| `tech-spec` | Write technical specifications |
| `adr-writing` | Record architecture decisions |
| `review` | Technical review of implementations |
| `brainstorming` | Design exploration and trade-offs |

## ADR Template

Every significant architectural decision gets an ADR:

```
# ADR-001: [Decision Title]
- Status: Accepted/Rejected/Superseded
- Context: Why this decision was needed
- Decision: What was decided
- Consequences: What follows from the decision
```

## Delivery Loop Role

```
Clarify (PM) → Plan (PM + Architect) → Build (Developer) → Verify (QA + SRE) → Learn (All)
```

The Architect is involved in **Plan** (tech spec, ADRs) and **Verify** (technical review). They work closely with the Developer during Build for guidance.

## Related

- [Delivery Loop](/architecture/delivery-loop)
- [Architecture Overview](/architecture/overview)