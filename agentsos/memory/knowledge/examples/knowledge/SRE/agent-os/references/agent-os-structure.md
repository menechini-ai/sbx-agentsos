---
id: agent-os.reference.structure
title: Agent OS Project Structure
type: reference
domain: agent-os
tags:
  - structure
  - folders
  - organization
aliases:
  - estrutura do projeto
  - diretórios agent os
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

# Agent OS Project Structure

## Overview

Referência completa da estrutura de diretórios do Agent OS.

## Purpose

Orientar navegação e organização do projeto.

## Content

### Estrutura Principal

```
sbx-agents-os/
├── docs/
│   ├── GOVERNANCE.md        # L0 constitucional
│   ├── ARCHITECTURE.md      # Arquitetura completa
│   └── plan/                # Planning paths
├── agentsos/
│   ├── agents/              # Definições de agentes
│   │   ├── ceo/AGENTS.md    # L1 CEO
│   │   ├── pm/AGENTS.md     # L2 PM
│   │   ├── architect/AGENTS.md # L2 Architect
│   │   ├── developer/AGENTS.md # L2 Developer
│   │   ├── qa/AGENTS.md     # L2 QA
│   │   ├── researcher/AGENTS.md # L2 Researcher
│   │   ├── sre/AGENTS.md    # L2 SRE
│   │   └── sre/             # L3 specialists
│   │       ├── azure-devops/
│   │       ├── azure-cloud/
│   │       ├── azure-aks/
│   │       └── datadog/
│   ├── skills/              # Habilidades reutilizáveis
│   │   ├── brainstorming/
│   │   ├── brief-creation/
│   │   ├── prd-writing/
│   │   ├── tech-spec/
│   │   ├── adr-writing/
│   │   ├── sprint-planning/
│   │   ├── agentos-build/
│   │   ├── dev-story/
│   │   ├── qa-gate/
│   │   ├── review/
│   │   ├── retrospective/
│   │   ├── agentos-help/
│   │   ├── pipeline-yaml/
│   │   ├── resource-provisioning/
│   │   ├── cluster-setup/
│   │   ├── rollout-strategies/
│   │   ├── monitor-setup/
│   │   ├── integration-setup/
│   │   ├── coding/
│   │   ├── research/
│   │   ├── documentation/
│   │   └── session-handoff/
│   ├── templates/           # Templates de artefatos
│   ├── guardrails/          # Restrições por agente
│   ├── memory/              # Sistema de memória
│   │   ├── knowledge/       # Skill-kwonledge (Obsidian KB)
│   │   ├── sessions/        # Logs de sessão
│   │   ├── candidates/      # Learning candidates
│   │   └── portable-context.md
│   ├── contracts/           # Contratos INPUT/OUTPUT
│   ├── tests/               # Validação automática
│   └── benchmarks/          # Benchmarks de governança
├── website/                 # Docs site (Astro+Starlight)
├── web-bundles/             # Prompts para Gemini/GPT
├── tools/                   # CLI e validadores
└── package.json             # npm package
```

### Convencções de Naming

| Tipo | Convencão | Exemplo |
|------|-----------|---------|
| Agentes | lowercase, kebab-case | `azure-devops` |
| Skills | lowercase, kebab-case | `pipeline-yaml` |
| Templates | lowercase, kebab-case | `brief-template.md` |
| Knowledge | Obsidian slug | `agent-os-architecture.md` |

## Usage

```
Encontrar skill de pipeline:
→ agentsos/skills/pipeline-yaml/SKILL.md

Encontrar agente SRE:
→ agentsos/agents/sre/AGENTS.md

Encontrar knowledge de governance:
→ agentsos/memory/knowledge/.../concepts/agent-os-governance.md
```

## Relationships
- [[agent-os-architecture]] - Arquitetura do sistema

## Notes

- `docs/` contém documentação de governança
- `agentsos/` contém todo o sistema de agentes
- `memory/knowledge/` é a base de conhecimento (Obsidian-style)

## References

- `docs/ARCHITECTURE.md` - Arquitetura detalhada
- `docs/GOVERNANCE.md` - Constituição
