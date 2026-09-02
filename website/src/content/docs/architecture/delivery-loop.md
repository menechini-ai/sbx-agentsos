---
title: Delivery Loop
description: The Agent OS delivery loop for Agent OS
---

# Delivery Loop

Agent OS uses the **Agent OS Delivery Loop** for all software delivery work.

## The Loop

```
Clarify → Plan → Build → Verify → Learn
   ↑                                        │
   └────────────────────────────────────────┘
```

## Fase Details

| Fase | Owner | Skills | Artifacts | Exit Criteria |
|------|-------|--------|-----------|---------------|
| **Clarify** | PM | `brainstorming`, `brief-creation` | Brief | Stakeholders aligned |
| **Plan** | PM + Architect | `prd-writing`, `tech-spec`, `adr-writing`, `sprint-planning` | PRD, Tech Spec, ADRs, Stories, Sprint Plan | CEO approval (if HIGH risk) |
| **Build** | Developer + SRE | `agentos-build`, `dev-story`, `pipeline-yaml`, `cluster-setup` | Code, Tests, Infrastructure | Tests pass, QA gate |
| **Verify** | QA + SRE | `qa-gate`, `test-planning`, `monitor-setup` | Test Report, Monitor Status | All gates green |
| **Learn** | CEO + All | `retrospective` | Retrospective, Action Items | Actions committed |

## Planning Paths

| Path | Trigger | Fases | Artifacts | Time |
|------|---------|-------|-----------|------|
| **Quick** | Clear, <2h, LOW risk | → Build | None | <2h |
| **Standard** | Feature, 2-8h, MEDIUM risk | Brief→PRD→Arch→Stories | Brief, PRD, Tech Spec, Stories, Sprint Plan | 2-8h |
| **Full** | Complex, >8h, HIGH risk | Research→Brief→PRD→Arch→Full Stories | Research, Brief, PRD, Tech Spec, ADRs, Stories, Multi-sprint Plan | >8h |

## Loop Rules

1. **Right-Sized**: Choose path based on clarity, scope, and risk
2. **Durable Context**: Brief, PRD, Tech Spec, ADRs are source of truth — don't re-explain
3. **Specialized Perspectives**: Each phase uses appropriate expertise
4. **One Delivery Path**: Clarify→Plan→Build→Verify→Learn is the only path — don't skip phases in Standard/Full
5. **Learn→Plan Feedback**: Retrospective generates action items and memory candidates
6. **Existing Codebase**: Run `workflows/existing-codebase/` before entering loop

## Artifacts Flow

```
Brief (PM)
  ↓
PRD (PM)
  ↓
Tech Spec + ADRs (Architect)
  ↓
Stories + Sprint Plan (PM + Dev)
  ↓
Code + Tests (Developer)
  ↓
Infrastructure (SRE)
  ↓
Test Report (QA)
  ↓
Monitor Status (SRE + Datadog)
  ↓
Retrospective (All)
```

## Memory Integration

Each phase generates **memory candidates** for `memory/knowledge`:

| Phase | Candidates |
|-------|------------|
| Clarify | Brainstorm patterns, assumption validation |
| Plan | Tech decisions, PRD patterns, estimation accuracy |
| Build | Code patterns, testing strategies, deployment issues |
| Verify | QA findings, performance patterns, security issues |
| Learn | Process improvements, team dynamics, tool effectiveness |

## Existing Codebase

For inherited codebases, run `workflows/existing-codebase/` first:

1. **Scan Repo** — Identify tech stack, patterns
2. **Establish Context** — Generate `docs/architecture-existing.md`
3. **Enter Loop** — Choose planning path based on complexity

## Related

- [Choose a Planning Path](/choose-a-planning-path)
- [Build Your First Change](/build-your-first-change)
- [Templates](/templates/brief)