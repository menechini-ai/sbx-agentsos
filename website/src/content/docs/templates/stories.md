---
title: Stories Template
description: User Stories template for sprint planning
---

# Stories Template

## Purpose

User stories break down features into implementable units with clear acceptance criteria.

## Template

```markdown
# Sprint [N] Stories

## Sprint Goal
[One sentence describing what this sprint delivers]

## Stories

### Story 1: [Title]
- **ID**: STORY-001
- **Points**: 5
- **Assignee**: [Developer Name]
- **Type**: Feature/Bug/Tech Debt/Research

**As a** [user]
**I want** [feature]
**So that** [benefit]

**Acceptance Criteria**:
- [ ] Given [context] when [action] then [result]
- [ ] Given [context] when [action] then [result]

**Technical Notes**:
- [Reference to tech spec section]
- [Any constraints]

**Dependencies**:
- [Story ID or external dependency]

---

### Story 2: [Title]
[Repeat structure]

## Capacity

| Role | Available Points |
|------|------------------|
| Developer 1 | 8 |
| Developer 2 | 8 |
| **Total** | **16** |

## Committed Points
**Total**: [N] / [Capacity] points

## Risks
| Story | Risk | Mitigation |
|-------|------|------------|
| STORY-001 | [Risk] | [Mitigation] |
```

## Usage

Used with `sprint-planning` skill by PM agent.

## Related

- [Sprint Template](/templates/sprint)
- [PRD Template](/templates/prd)
- [Delivery Loop](/architecture/delivery-loop)