---
title: Sprint Template
description: Sprint Planning template for Agent OS
---

# Sprint Template

## Purpose

Sprint planning organizes committed work with capacity planning and risk assessment.

## Template

```markdown
# Sprint [Number] Plan

## Metadata
- **Sprint**: [Number] (e.g., Sprint 5)
- **Dates**: YYYY-MM-DD to YYYY-MM-DD
- **Goal**: [One sentence sprint goal]
- **PM**: [PM Name]
- **Architect**: [Architect Name]

## Capacity Planning

| Team Member | Role | Available Days | Points/Day | Total Points |
|-------------|------|----------------|------------|--------------|
| [Name] | Developer | 8 | 1 | 8 |
| [Name] | Developer | 8 | 1 | 8 |
| **Total** | | | | **16** |

## Committed Stories

| ID | Title | Points | Assignee | Status |
|----|-------|--------|----------|--------|
| STORY-001 | [Title] | 5 | [Name] | Planned |
| STORY-002 | [Title] | 3 | [Name] | Planned |
| STORY-003 | [Title] | 8 | [Name] | Planned |
| **Total** | | **16** | | |

## Velocity

| Sprint | Committed | Completed | Velocity |
|--------|-----------|-----------|----------|
| Sprint N-2 | 13 | 11 | 11 |
| Sprint N-1 | 15 | 15 | 15 |
| **Sprint N** | **16** | — | **—** |
| **Average** | | | **13** |

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | Medium | High | [Mitigation] |
| [Risk 2] | Low | Medium | [Mitigation] |

## Definition of Done

- [ ] Code implemented
- [ ] Unit tests pass (>80% coverage)
- [ ] Integration tests pass
- [ ] Code review approved
- [ ] Documentation updated
- [ ] QA gate passes
- [ ] Deployed to staging

## Retrospective Date
YYYY-MM-DD
```

## Usage

Used with `sprint-planning` skill by PM agent.

## Related

- [Stories Template](/templates/stories)
- [PRD Template](/templates/prd)
- [Retrospective Template](/templates/retrospective)