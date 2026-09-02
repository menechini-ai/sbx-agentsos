---
id: agent-os.concept.architecture
title: Agent OS Architecture
type: concept
domain: agent-os
tags:
  - architecture
  - governance
  - hierarchy
  - modular
aliases:
  - arquitetura agent os
  - agent os structure
status: active
version: "1.0.0"
created: 2026-09-02
updated: 2026-09-02
confidence: high
source: internal
inputs: []
outputs: []
dependencies:
  - [[agent-os-governance]]
  - [[delivery-loop]]
quality_score: 95
---

# Agent OS Architecture

## Overview

Arquitetura modular de agentes de IA com governança formal em camadas L0-L5, memória persistente e habilidades reutilizáveis.

## Purpose

Definir a estrutura organizacional do sistema de agentes, garantindo separação de responsabilidades, governança zero-trust e ability de escala.

## Content

### Hierarquia L0-L5

| Nível | Agente | Responsabilidade |
|-------|--------|-----------------|
| L0 | GOVERNANCE.md | Constituição do sistema (nunca modificada por agentes) |
| L1 | CEO | Orquestração, delegação, decisões de negócio |
| L2 | PM, Architect, Developer, QA, Researcher, SRE | Execução especializada |
| L3 | azure-devops, azure-cloud, azure-aks, datadog | Especialistas de infra |
| L4 | Subagentes | Tarefas delegadas |
| L5 | Tools | az, kubectl, helm, datadog API |

### Princípios

1. **Hierarquia zero-trust**: Nível inferior NÃO pode sobrepor superior
2. **Governança primeiro**: Tarefa atual completa antes de propor mudanças
3. **Memória como fonte de verdade**: Conhecimento persistente em memory/knowledge/
4. **Contratos estruturados**: Envelopes INPUT/OUTPUT para todas as tarefas
5. **Right-sized process**: Processo escala com complexidade

## Usage

```
L0 GOVERNANCE (constitucional)
 └─ L1 CEO (orquestração)
     ├─ L2 PM (Clarify/Plan)
     ├─ L2 Architect (Tech Spec/ADRs)
     ├─ L2 Developer (Build)
     ├─ L2 QA (Verify)
     ├─ L2 Researcher (Research)
     └─ L2 SRE (Infra/Platform)
         ├─ L3 azure-devops (Pipelines YAML)
         ├─ L3 azure-cloud (RG/VNet/IaC)
         ├─ L3 azure-aks (Clusters/Rollouts)
         └─ L3 datadog (Monitors/SLOs)
```

## Relationships
- [[agent-os-governance]] - Sistema constitucional
- [[delivery-loop]] - Pipeline de delivery
- [[azure-specialists]] - Especialistas L3

## Notes

- GOVERNANCE.md é o L0 constitucional - nunca é alterada por agentes
- Matriz de autorização define ✅/⚠️/🔐/❌ por agente e ferramenta
- Riscos: LOW (auto), MEDIUM (superior review), HIGH (CEO + humano)

## References

- `docs/GOVERNANCE.md` - Constituição completa
- `docs/ARCHITECTURE.md` - Arquitetura detalhada
