---
id: agent-os.concept.portable-context
title: Portable Context
type: concept
domain: agent-os
tags:
  - portable-context
  - handoff
  - session
  - export
  - import
aliases:
  - contexto portátil
  - handoff context
status: active
version: "1.0.0"
created: 2026-09-02
updated: 2026-09-02
confidence: high
source: internal
inputs: []
outputs: []
dependencies:
  - [[session-handoff-runbook]]
quality_score: 85
---

# Portable Context

## Overview

Formato de exportação/importação de contexto entre sessões de agentes, preservando estado, decisões e pending tasks.

## Purpose

Permitir continuidade entre sessões sem depender de contexto de conversa.

## Content

### Estrutura do Export

```yaml
export:
  version: "1.0"
  timestamp: "2026-09-02T10:00:00Z"
  session:
    agent: developer
    task: "Implementar feature X"
    status: in_progress
  context:
    current_file: src/feature.ts
    decisions: [...]
    pending: [...]
    artifacts: [...]
  memory:
    candidates: [...]
    learnings: [...]
```

### Local de Armazenamento

- **Export/Import**: `agentsos/memory/portable-context.md`
- **Session logs**: `agentsos/memory/sessions/`
- **Knowledge**: `agentsos/memory/knowledge/`

## Usage

```
Sessão termina:
→ Agent exporta contexto para memory/portable-context.md
→ Próxima sessão importa contexto automaticamente
→ Continuidade preservada sem contexto de conversa
```

## Relationships
- [[session-handoff-runbook]] - Procedimento de handoff
- [[agent-os-architecture]] - Estrutura do sistema

## Notes

- Formato YAML para parse fácil
- Inclui apenas dados necessários (não full context)
- Compatível comtodos os agentes L2/L3

## References

- `agentsos/memory/portable-context.md` - Formato completo
- `agentsos/skills/session-handoff/SKILL.md` - Skill de handoff
