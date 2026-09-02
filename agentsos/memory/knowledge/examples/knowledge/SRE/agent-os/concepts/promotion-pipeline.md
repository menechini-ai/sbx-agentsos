---
id: agent-os.concept.promotion-pipeline
title: Promotion Pipeline (Memory→Skill→Rule→Agent)
type: concept
domain: agent-os
tags:
  - promotion
  - pipeline
  - memory
  - skill
  - rule
  - agent
aliases:
  - pipeline de promoção
  - memory skill rule agent
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
  - [[portable-context]]
quality_score: 90
---

# Promotion Pipeline (Memory→Skill→Rule→Agent)

## Overview

Pipeline de promoção de aprendizados: raw learning → candidate → concept/pattern note → rule → agent update.

## Purpose

Transformar aprendizados de sessões em conhecimento persistente e acionável.

## Content

### Pipeline

```
Raw learning (session)
  → agentsos/memory/candidates/{slug}.md
  → Reviewed + promoted to:
     - concept note → memory/knowledge/.../concepts/
     - pattern note → memory/knowledge/.../patterns/
     - runbook → memory/knowledge/.../runbooks/
  → Eventually → rule (guardrails) or agent update
```

### Gate de Risco

| Destino | Risk Level | Aprovação |
|---------|-----------|-----------|
| concept note | LOW | Auto |
| pattern note | MEDIUM | Superior |
| rule update | HIGH | CEO + humano |
| agent update | HIGH | CEO + humano |

### Tipos de Nota

| Tipo | Quando | Exemplo |
|------|--------|---------|
| **concept** | Definição, ideia | "O que é delivery loop" |
| **pattern** | Problema resolvido | "Como fazer rollup em AKS" |
| **runbook** | Procedimento operacional | "Como criar pipeline YAML" |
| **architecture** | Design de sistema | "Arquitetura multi-cluster AKS" |

## Usage

```
Developer aprende padrão de leak:
→ Cria candidate: memory/candidates/memory-leak-pattern.md
→ Review: MEDIUM risk, superior aprova
→ Promote: memory/knowledge/.../patterns/memory-leak-pattern.md
→ Eventually: vira rule em guardrails
```

## Relationships
- [[agent-os-architecture]] - Estrutura do sistema
- [[portable-context]] - Contexto entre sessões

## Notes

- Candidates ficam em memory/candidates/ até review
- Só são promovidos após aprovação do risk level
- Knowledge notes seguem schema do skill-kwonledge

## References

- `agentsos/memory/candidates/` - Learning candidates
- `agentsos/memory/knowledge/` - Knowledge base
- `skills/knowledge-manager/SKILL.md` - Gestão de knowledge
