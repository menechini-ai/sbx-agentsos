---
id: agent-os.guide.build-first-change
title: Build Your First Change
type: guide
domain: agent-os
tags:
  - tutorial
  - getting-started
  - quick-start
aliases:
  - primeira mudança
  - getting started agent os
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
  - [[agent-os-architecture]]
quality_score: 85
---

# Build Your First Change

## Overview

Guia passo a passo para implementar sua primeira mudança no Agent OS.

## Purpose

Orientar novos usuários através do delivery loop completo.

## Content

### Pré-requisitos

1. Agent OS instalado (`npx agent-os install`)
2. Git configurado
3. Conhecimento básico de Markdown

### Passo 1: Clarify (PM)

```
→ Use skill: brainstorming
→ Defina o que precisa ser feito
→ Output: brief.md
```

### Passo 2: Plan (Architect + PM)

```
→ Architect: tech spec
→ PM: stories.md + sprint.md
→ Choose path: Quick/Standard/Full
```

### Passo 3: Build (Developer)

```
→ Use skill: dev-story
→ Implemente código
→ Output: código + testes
```

### Passo 4: Verify (QA + SRE)

```
→ QA: qa-gate (testes)
→ SRE: validação deployment
→ Output: relatório de verificação
```

### Passo 5: Learn (All)

```
→ retrospective
→ Capture learnings
→ Promote to memory/knowledge/
```

## Usage

```
Bug fix rápido:
→ Quick path (mínimo ceremony)
→ Clarify: "Corrigir bug X"
→ Build: Fix + teste
→ Verify: QA valida
→ Learn: Learning promovido
```

## Relationships
- [[delivery-loop]] - Pipeline completo
- [[choose-planning-path]] - Paths de planning
- [[agent-os-architecture]] - Estrutura do sistema

## Notes

- Quick path para bug fixes
- Standard path para features
- Full path para mudanças arquiteturais

## References

- `docs/plan/choose-a-planning-path.md` - Guia de paths
- `docs/ARCHITECTURE.md` - Arquitetura completa
