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
│  L2: PM, Architect, Dev, QA, SRE,    │
│       Researcher                      │
└───────────────────┬───────────────────┘
                    ▼
┌───────────────────────────────────────┐
│         Specialist Agents             │
│  L3: Azure DevOps, Azure Cloud,       │
│       Azure AKS, Datadog, etc.        │
└───────────────────┬───────────────────┘
                    ▼
┌───────────────────────────────────────┐
│             Subagents                 │
│  L4: Execução de tarefas específicas  │
└───────────────────┬───────────────────┘
                    ▼
┌───────────────────────────────────────┐
│            Tools / MCP                │
│  L5: az cli, kubectl, helm,          │
│      datadog API, GitHub, Filesystem  │
└───────────────────┬───────────────────┘
```

## Princípios Fundamentais

1. **Separação de Responsabilidades**
   - GOVERNANCE.md: "QUEM SOU E QUAIS SÃO MEUS LIMITES"
   - AGENTS.md: "QUEM SOU E COMO DEVO ME COMPORTAR"
   - SKILL.md: "COMO EXECUTO UMA TAREFA"
   - memory/knowledge: "O QUE EU APRENDI"

2. **Hierarquia Estrita**: Nível inferior NÃO pode sobrescrever regras de nível superior

3. **Memória Única**: memory/knowledge como fonte de verdade (wiki markdown + SQLite)

4. **Contratos Estruturados**: INPUT/OUTPUT envelopes para toda comunicação

5. **Pipeline Controlado**: Memory → Skill → Rule → Agent com gates de risco

6. **Right-Sized Process** (BMAD): Processo dimensionado à complexidade da tarefa

7. **Durable Context**: Decisões de produto/técnicas carregadas adiante

8. **Specialized Perspectives**: PM, Architect, Dev, QA, SRE on-demand

## Delivery Loop (BMAD)

```
Clarify → Plan → Build → Verify → Learn
   ↑                                        │
   └────────────────────────────────────────┘
   (Learn alimenta próximo Clarify/Plan)
```

### Planning Paths (Right-Sized)

| Path | Trigger | Fases | Artefatos | Tempo Típico |
|------|---------|-------|-----------|--------------|
| **Quick** | Requisitos claros, <2h | → Build | Nenhum | < 2h |
| **Standard** | Feature média, 2-8h | Brief → PRD → Arch → Stories | Brief, PRD, Tech Spec, Stories, Sprint Plan | 2-8h |
| **Full** | Complexo, >8h, alta incerteza | Research → Brief → PRD → Arch → Full Stories | Research, Brief, PRD, Tech Spec, ADRs, Stories, Multi-sprint Plan | > 8h |

**Referência**: `docs/plan/choose-a-planning-path.md` para detalhes completos.

### Fase Details

| Fase | Owner | Skills | Artefatos | Exit Criteria |
|------|-------|--------|-----------|---------------|
| **Clarify** | PM | `brainstorming`, `brief-creation` | Brief | Stakeholders aligned |
| **Plan** | PM + Arquiteto | `prd-writing`, `tech-spec`, `adr-writing`, `sprint-planning` | PRD, Tech Spec, ADRs, Stories, Sprint Plan | CEO approval (se HIGH risk) |
| **Build** | Dev + SRE | `agentos-build`, `dev-story`, `pipeline-yaml`, `cluster-setup` | Code, Tests, Infra | Tests pass, QA gate |
| **Verify** | QA + SRE | `qa-gate`, `test-planning`, `monitor-setup` | Test Report, Monitor Status | All gates green |
| **Learn** | CEO + All | `retrospective` | Retrospective, Action Items | Actions committed |

## Fluxo de Trabalho (Legacy - para compatibilidade)

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
| `workflows/` | Clarify, Plan, Build, Verify, Learn, existing-codebase |
| `templates/` | Brief, PRD, Arch, Stories, Sprint, Retrospective |
| `proposals/` | Propostas de skills, agents, rules, architecture |
| `tests/` | Testes de conformidade |

## Workflows

| Workflow | Propósito |
|----------|-----------|
| `workflows/clarify/` | Brainstorming, brief creation |
| `workflows/plan/` | PRD, Tech Spec, ADR, Sprint Planning |
| `workflows/build/` | Implementation, infra provisioning |
| `workflows/verify/` | QA gates, testing, monitoring |
| `workflows/learn/` | Retrospective, improvement |
| `workflows/existing-codebase/` | Scan repo, establish context, enter loop |