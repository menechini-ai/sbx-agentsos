---
title: PRD Template
description: Product Requirements Document template for Agent OS
---

# PRD Template

## Purpose

The Product Requirements Document (PRD) defines feature requirements with acceptance criteria, user stories, and non-functional requirements.

## Template

```markdown
# PRD: [Feature Name]

## Overview
- **Feature**: [Name]
- **Status**: Draft/In Review/Approved
- **Owner**: [PM Name]
- **Created**: YYYY-MM-DD
- **Updated**: YYYY-MM-DD

## Objective
[Brief description of what this feature achieves]

## User Stories

### MUST
- [ ] As a [user], I want [feature] so that [benefit]
  - **Acceptance Criteria**:
    - [ ] Given [context] when [action] then [result]
    - [ ] Given [context] when [action] then [result]

### SHOULD
- [ ] As a [user], I want [feature] so that [benefit]
  - **Acceptance Criteria**:
    - [ ] Given [context] when [action] then [result]

### COULD
- [ ] As a [user], I want [feature] so that [benefit]
  - **Acceptance Criteria**:
    - [ ] Given [context] when [action] then [result]

## Non-Functional Requirements

| Requirement | Target |
|-------------|--------|
| Performance | < 200ms response time |
| Availability | 99.9% uptime |
| Security | OAuth 2.0, HTTPS only |
| Scalability | Support 10k concurrent users |

## Dependencies

- [Dependency 1]
- [Dependency 2]

## Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk] | High | [Mitigation] |

## Out of Scope

- [Item 1]
- [Item 2]
```

## Usage

Use with `prd-writing` skill by PM agent.

## Related

- [Brief Template](/templates/brief)
- [Stories Template](/templates/stories)
- [Sprint Template](/templates/sprint)