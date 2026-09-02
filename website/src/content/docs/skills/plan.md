---
title: Plan Skills
description: Skills for the Plan phase - tech-spec, adr-writing, sprint-planning
---

# Plan Skills

Skills used during the **Plan** phase by the Architect and PM agents.

## tech-spec

**Purpose**: Write technical specifications with architecture, data model, API design, and infrastructure.

**Triggers**: "Write tech spec for...", "Technical design...", "Architecture document..."

**Output**: `tech-spec.md` with:
- Architecture overview
- Data model / schema
- API endpoints
- Infrastructure requirements
- Security considerations
- Non-functional requirements

## adr-writing

**Purpose**: Record Architecture Decision Records for significant technical choices.

**Triggers**: "Record ADR for...", "Document decision...", "Why did we choose..."

**Output**: ADR in `docs/architecture/adr-XXX.md`:
- Status (Accepted/Rejected/Superseded)
- Context
- Decision
- Consequences

## sprint-planning

**Purpose**: Plan sprints with story estimation, capacity planning, and commitment.

**Triggers**: "Plan sprint...", "Estimate stories...", "Sprint planning..."

**Output**: `sprint.md` with:
- Sprint goal
- Committed stories with points
- Capacity calculation
- Risk assessment

## Usage

```
Architect: "Use tech-spec for the payment service"
→ Creates tech-spec.md

Architect: "Use adr-writing for choosing PostgreSQL over MongoDB"
→ Creates ADR-001

PM: "Use sprint-planning for Sprint 5"
→ Creates sprint.md
```

## Related

- [Architect Agent](/agents/architect)
- [PM Agent](/agents/pm)
- [Delivery Loop](/architecture/delivery-loop)
- [Build Skills](/skills/build)