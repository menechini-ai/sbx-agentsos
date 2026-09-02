---
title: QA Agent
description: L2 QA - Verify phase, testing, quality gates
---

# QA Agent (L2)

## Overview

The QA agent owns the **Verify** phase. They validate that implementations meet requirements, pass all quality gates, and are ready for deployment.

## Responsibilities

- **Testing**: Execute test plans, validate acceptance criteria
- **Quality Gates**: Run QA gate checks (tests, lint, security)
- **Retrospective**: Lead/coordinate retrospective for learning capture
- **Knowledge**: Capture quality patterns for promotion

## Scope

| Path | Access |
|------|--------|
| `agents/qa/` | Full |
| `skills/` | Use (qa-gate, retrospective, review) |
| `work/qa/` | Full |
| `tests/` | Read |
| `agents/` (other) | Denied |
| `GOVERNANCE.md` | Denied |

## Key Skills

| Skill | Purpose |
|-------|---------|
| `qa-gate` | Execute quality verification gate |
| `retrospective` | Facilitate learning capture |
| `review` | Quality review |

## QA Gate Checklist

```
- [ ] All unit tests pass
- [ ] Integration tests pass
- [ ] Linter clean
- [ ] No security vulnerabilities
- [ ] Tech spec compliance verified
- [ ] Acceptance criteria met
- [ ] Documentation updated
```

## Delivery Loop Role

```
Clarify (PM) → Plan (PM + Architect) → Build (Developer) → Verify (QA + SRE) → Learn (All)
```

The QA agent is involved in **Verify** (quality gates, testing) and **Learn** (retrospective facilitation).

## Related

- [Delivery Loop](/architecture/delivery-loop)
- [Build Your First Change](/build-your-first-change)