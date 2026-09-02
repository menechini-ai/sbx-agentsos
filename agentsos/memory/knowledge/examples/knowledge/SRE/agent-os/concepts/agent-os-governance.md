---
id: agent-os.concept.governance
title: Agent OS Governance System
type: concept
domain: agent-os
tags:
  - governance
  - constitution
  - risk-levels
  - authorization
aliases:
  - governança agent os
  - sistema constitucional
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
quality_score: 95
---

# Agent OS Governance System

## Overview

Sistema constitucional que define limites, hierarquia e políticas para todos os agentes do sistema.

## Purpose

Garantir que nenhum agente ultrapasse seus limites autorizados, mantendo integridade do sistema e alinhamento com decisões de negócio.

## Content

### Níveis de Risco

| Nível | Aprovação | Exemplo |
|-------|-----------|---------|
| LOW | Auto (agente decide) | Criar documento, escrever código |
| MEDIUM | Superior direto revisa | Modificar guardrails, criar skill |
| HIGH | CEO + humano | Alterar GOVERNANCE.md, criar agente |

### Símbolos da Matriz

- ✅ Permitido (auto)
- ⚠️ Precisa aprovação do superior
- 🔐 Precisa CEO + humano
- ❌ Negado permanentemente

### Guardrails Ativos

- `scope.md` - Caminhos permitidos/denegados por agente
- `tools.md` - Ferramentas permitidas por agente
- `authority.md` - Matriz de autorização por agente
- `change-risk-levels.md` - Mapeamento de risco por tipo de mudança

## Usage

```
Agent quer modificar GOVERNANCE.md?
→ Verificar authority.md: 🔐 para todos
→ Requer CEO + aprovação humana
→ Risco: HIGH
```

## Relationships
- [[agent-os-architecture]] - Estrutura do sistema
- [[azure-specialists]] - Guardrails Azure específicos

## Notes

- GOVERNANCE.md é o L0 - constitucional, nunca modificada por agentes
- Guardrails ficam em `agentsos/guardrails/global/`
- Validação automática via `validate.py`

## References

- `docs/GOVERNANCE.md` - Constituição completa
- `agentsos/guardrails/global/` - Guardrails ativos
