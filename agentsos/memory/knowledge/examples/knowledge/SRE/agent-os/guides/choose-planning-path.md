---
id: agent-os.guide.choose-planning-path
title: Choose a Planning Path
type: guide
domain: agent-os
tags:
  - planning
  - paths
  - quick
  - standard
  - full
aliases:
  - escolher path
  - caminhos de planning
status: active
version: "1.0.0"
created: 2026-09-02
updated: 2026-09-02
confidence: high
source: internal
inputs: []
outputs: []
dependencies:
  - [[delivery-loop]]
quality_score: 85
---

# Choose a Planning Path

## Overview

Guia para escolher entre Quick, Standard e Full planning paths.

## Purpose

Orientar a escolha do nível de ceremony baseado na complexidade da mudança.

## Content

### Três Paths

| Path | Ceremony | Quando |
|------|----------|--------|
| **Quick** | Mínimo | Bug fixes, hotfixes, < 1 dia |
| **Standard** | Moderado | Features, mudanças normais |
| **Full** | Alto | Mudanças grandes, arquitetura |

### Quick Path

```
Clarify (5 min) → Build → Verify → Learn
- Sem PRD
- Sem tech spec formal
- Stories opcionais
- Ideal para: bug fixes, typo fixes, config changes
```

### Standard Path

```
Clarify → Plan → Build → Verify → Learn
- Brief (PM)
- Stories + Sprint (PM)
- Tech Spec (Architect)
- Ideal para: features, improvements, refactors
```

### Full Path

```
Clarify → Plan → Build → Verify → Learn
- PRD completo (PM)
- Tech Spec + ADRs (Architect)
- Stories + Sprint (PM)
- Ideal para: novas arquiteturas, mudanças de sistema
```

### Critérios de Escolha

| Fator | Quick | Standard | Full |
|-------|-------|----------|------|
| Complexidade | Baixa | Média | Alta |
| Risco | LOW | MEDIUM | HIGH |
| Duração | < 1 dia | 1-5 dias | > 5 dias |
| Impacto | Local | Módulo | Sistema |

## Usage

```
Bug fix em pipeline:
→ Quick path
→ Clarify: "Fix timeout in YAML"
→ Build: Fix code
→ Verify: Test passes
→ Done
```

## Relationships
- [[delivery-loop]] - Pipeline completo
- [[build-first-change]] - Tutorial

## Notes

- Path pode escalar mid-task se complexidade aumentar
- Nunca downgradar de Full para Quick
- Gate de aprovação em cada fase

## References

- `docs/plan/choose-a-planning-path.md` - Guia completo
