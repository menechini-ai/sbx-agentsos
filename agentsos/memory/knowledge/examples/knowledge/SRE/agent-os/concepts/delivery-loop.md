---
id: agent-os.concept.delivery-loop
title: Delivery Loop (BMAD)
type: concept
domain: agent-os
tags:
  - delivery-loop
  - clarify
  - plan
  - build
  - verify
  - learn
aliases:
  - loop de delivery
status: active
version: "1.0.0"
created: 2026-09-02
updated: 2026-09-02
confidence: high
source: internal
inputs: []
outputs: []
dependencies:
  - [[agent-os-architecture]]
quality_score: 90
---

# Delivery Loop (BMAD)

## Overview

Pipeline de delivery inspirado em BMAD: um único caminho de delivery que todos seguem, adaptado por complexidade.

## Purpose

Fornecer estrutura consistente para todas as mudanças, desde hotfixes rápidos até features completas.

## Content

### Cinco Fases

| Fase | Agentes | Output |
|------|---------|--------|
| **Clarify** | PM | Brief/requirements |
| **Plan** | Architect, PM | Tech spec, stories, sprint |
| **Build** | Developer | Code implementation |
| **Verify** | QA, SRE | Tests, deployment |
| **Learn** | All | Retrospective, learnings |

### Três Caminhos de Planning

| Path | When | Ceremony |
|------|------|----------|
| **Quick** | Bug fixes, hotfixes, small | Minimal |
| **Standard** | Features, normal changes | Moderate |
| **Full** | Major changes, architecture | High |

### Workflow

```
Clarify → Plan → Build → Verify → Learn
  PM      Arch    Dev     QA/SRE    All
           │
            ├─ Quick: Minimal planning
            ├─ Standard: Stories + sprint
            └─ Full: PRD + architecture + sprint
```

## Usage

```
Nova feature request:
→ Clarify: PM cria brief
→ Plan: Architect cria tech spec, PM cria stories
→ Build: Developer implementa
→ Verify: QA testa, SRE valida deployment
→ Learn: Retrospective captura learnings
```

## Relationships

- [[agent-os-architecture]] - Estrutura do sistema
- [[agent-os-governance]] - Regras de governança

## Notes

- Cada fase tem gate de aprovação
- Learnings são promovidos para memory/knowledge/
- Session handoff preserva contexto entre fases

## References

- `docs/ARCHITECTURE.md` - Detalhes do delivery loop
- `docs/plan/choose-a-planning-path.md` - Guia de paths