# Memory System — Agent OS

## Overview

O sistema de memória do Agent OS é composto por três camadas:

1. **Knowledge Base** (`memory/knowledge/`) — Skill-kwonledge clone com notas Obsidian-style
2. **Session Logs** (`memory/sessions/`) — Logs simples de sessões por data
3. **Learning Candidates** (`memory/candidates/`) — Aprendizados aguardando review

## Architecture

```
agentsos/memory/
├── knowledge/                    # Base de conhecimento (Obsidian-style)
│   ├── examples/knowledge/       # Notas organizadas por categoria
│   │   ├── IaC/                  # Infrastructure as Code
│   │   ├── DevOps/               # Kubernetes, ArgoCD, etc.
│   │   ├── AI/                   # LangChain, DeepAgents
│   │   ├── SRE/                  # Agent OS e SRE
│   │   │   └── agent-os/         # Arquitetura, governança, delivery loop
│   │   └── patterns/             # Patterns cross-category
│   ├── skills/                   # knowledge-manager + knowledge-create
│   └── scripts/                  # dedup, validation
├── sessions/                     # Logs de sessão (flat, por data)
│   ├── session-template.md       # Template
│   └── YYYY-MM-DD-agent.md       # Logs reais
├── candidates/                   # Learning candidates
│   ├── candidate-template.md     # Template
│   └── {slug}.md                 # Candidates reais
├── portable-context.md           # Formato de export/import
└── README.md                     # Este arquivo
```

## Promotion Pipeline

```
Raw learning (session)
  → memory/candidates/{slug}.md
  → Reviewed + promoted to:
     - concept note → memory/knowledge/.../concepts/
     - pattern note → memory/knowledge/.../patterns/
     - runbook → memory/knowledge/.../runbooks/
  → Eventually → rule (guardrails) or agent update
```

## Gate de Risco

| Destino | Risk Level | Aprovação |
|---------|-----------|-----------|
| concept note | LOW | Auto |
| pattern note | MEDIUM | Superior |
| rule update | HIGH | CEO + humano |
| agent update | HIGH | CEO + humano |

## Knowledge Schema

Todas as notas seguem o schema do skill-kwonledge:

```yaml
---
id: domain.type.slug
title: Human-readable title
type: concept | pattern | runbook | architecture
domain: agent-os | kubernetes | terraform | etc.
tags:
  - tag1
  - tag2
status: active
version: "1.0.0"
created: YYYY-MM-DD
updated: YYYY-MM-DD
confidence: high | medium | low
source: internal | docs | external
quality_score: 0-100
---
```

## Usage

### Consultar Knowledge

```bash
# Listar notas de agent-os
ls memory/knowledge/examples/knowledge/SRE/agent-os/

# Buscar por tag
grep -r "tags:" memory/knowledge/ | grep "governance"

# Ler nota específica
cat memory/knowledge/examples/knowledge/SRE/agent-os/concepts/agent-os-governance.md
```

### Criar Nova Nota

```bash
# Usar knowledge-create skill
→ "create pattern for AKS blue-green deployment"
→ Creates: memory/knowledge/.../patterns/aks-blue-green.md
```

### Promover Learning

```bash
# 1. Criar candidate
cp candidates/candidate-template.md candidates/my-learning.md
# 2. Editar com aprendizado
# 3. Review (MEDIUM risk → superior aprova)
# 4. Promover para knowledge note
```

## Integration

- **Agentes**: Referenciam `memory/knowledge/` via guardrails (somente leitura)
- **Skills**: session-handoff exporta/importa de `memory/sessions/`
- **Portable Context**: Formato YAML em `memory/portable-context.md`
- **Validation**: `validate.py` verifica integridade da knowledge base
