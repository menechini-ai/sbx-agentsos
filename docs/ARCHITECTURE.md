# Arquitetura do Agent OS

## Visão Geral

O Agent OS é uma arquitetura modular para agentes de IA com governança formal, memória persistente e habilidades reutilizáveis.

## Camadas da Arquitetura

```
┌───────────────────────────────────────┐
│              GOVERNANCE               │
│  L0: Regras constitucionais, limites  │
└───────────────────┬───────────────────┘
                    ▼
┌───────────────────────────────────────┐
│                 CEO                   │
│  L1: Orquestração, delegação          │
└───────────────────┬───────────────────┘
                    ▼
┌───────────────────────────────────────┐
│         Department Agents             │
│  L2: Developer, QA, Security, Research│
└───────────────────┬───────────────────┘
                    ▼
┌───────────────────────────────────────┐
│         Specialist Agents             │
│  L3: Expertise específica             │
└───────────────────┬───────────────────┘
                    ▼
┌───────────────────────────────────────┐
│             Subagents                 │
│  L4: Execução de tarefas específicas  │
└───────────────────┬───────────────────┘
                    ▼
┌───────────────────────────────────────┐
│            Tools / MCP                │
│  L5: GitHub, Filesystem, Database...  │
└───────────────────────────────────────┘
```

## Princípios Fundamentais

1. **Separação de Responsabilidades**
   - GOVERNANCE.md: "QUEM SOU E QUAIS SÃO MEUS LIMITES"
   - AGENTS.md: "QUEM SOU E COMO DEVO ME COMPORTAR"
   - SKILL.md: "COMO EXECUTO UMA TAREFA"
   - ai-memory: "O QUE EU APRENDI"

2. **Hierarquia Estrita**: Nível inferior NÃO pode sobrescrever regras de nível superior

3. **Memória Única**: ai-memory como fonte de verdade (wiki markdown + SQLite)

4. **Contratos Estruturados**: INPUT/OUTPUT envelopes para toda comunicação

5. **Pipeline Controlado**: Memory → Skill → Rule → Agent com gates de risco

## Fluxo de Trabalho

```
TAREFA → CEO → Department Agent → Specialist → Subagent → Tools
   ↓
CONTRATO INPUT (task-envelope.json)
   ↓
EXECUÇÃO (EXECUTION-FIRST POLICY)
   ↓
VALIDAÇÃO
   ↓
CONTRATO OUTPUT (result-envelope.json)
   ↓
HANDOFF (se necessário)
   ↓
REVIEW/LEARNING
   ↓
PROMOÇÃO (se aplicável)
```

## Diretórios Principais

| Diretório | Propósito |
|-----------|-----------|
| `agents/` | Definições de agentes por nível |
| `skills/` | Skills globais reutilizáveis |
| `memory/` | Políticas, decisões, learnings, candidates |
| `contracts/` | Envelopes INPUT/OUTPUT |
| `guardrails/` | Regras de autoridade, scope, tools, risk |
| `mcp/` | Model Context Protocol servers & policies |
| `workflows/` | Delegation, handoff, review, improvement |
| `templates/` | Templates para agents, skills, tasks, etc. |
| `proposals/` | Propostas de skills, agents, rules, architecture |
| `tests/` | Testes de conformidade |