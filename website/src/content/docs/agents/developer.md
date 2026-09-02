---
title: Developer Agent
description: L2 Developer - Build phase, coding, testing, implementation
---

# Developer Agent (L2)

## Overview

The Developer agent executes the **Build** phase of the delivery loop. They implement code, write tests, perform code review, and deliver working software.

## Responsibilities

- **Coding**: Implement features according to tech spec
- **Testing**: Write unit tests, integration tests
- **Code Review**: Review subagent work (L4)
- **Knowledge**: Capture patterns for promotion to memory/knowledge/

## Scope

| Path | Access |
|------|--------|
| `agents/developer/` | Full |
| `skills/` | Use (coding, dev-story, review) |
| `work/developer/` | Full |
| `src/` | Read/Write |
| `tests/` | Read/Write |
| `agents/` (other) | Denied |
| `GOVERNANCE.md` | Denied |

## Key Skills

| Skill | Purpose |
|-------|---------|
| `coding` | Implementation workflow |
| `dev-story` | Implement a user story |
| `review` | Code review |
| `research` | Technical research |

## Build Process

1. Receive story from PM
2. Review tech spec from Architect
3. Implement in `src/`
4. Write tests in `tests/`
5. Self-review
6. Report to QA for verification

## Quality Gates

- All tests pass
- Linter clean
- Tech spec compliance
- No security vulnerabilities

## Delivery Loop Role

```
Clarify (PM) → Plan (PM + Architect) → Build (Developer) → Verify (QA + SRE) → Learn (All)
```

The Developer executes the **Build** phase. They receive stories and tech specs, implement code, write tests, and hand off to QA/SRE for verification.

## Related

- [Build Your First Change](/build-your-first-change)
- [Delivery Loop](/architecture/delivery-loop)