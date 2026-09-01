# Candidate Entry

## Formato Padrão

```
candidate_id: CAND-2026-0001
task_id: TASK-2026-0001
agent: developer
date: 2026-09-01
type: skill  # ou rule, ou agent
status: awaiting_review

description:
  - "Projeto utiliza refresh token de 7 dias"
  - "Padrão repetido em 4 tarefas"

pattern_detection:
  occurrences: 4
  tasks:
    - TASK-2026-0001
    - TASK-2026-0002
    - TASK-2026-0003
    - TASK-2026-0004

confidence: 0.87

risk_level: LOW  # LOW, MEDIUM, HIGH

review:
  required: true
  reviewer: ceo
  status: pending
```

## Uso

- Candidatos são registrados em `memory/candidates/` quando:
  - O pattern detection identifica repetição suficiente
  - O aprendizado ainda está aguardando review antes de ser promovido
  - O agente não pode auto-promover (governança controlada)

## Tipos de Candidatos

### Skill Candidate
- Trigger: pattern detectado em 4+ tasks
- Path: `memory/candidates/skills/<skill-name>/`
- Exemplo: `memory/candidates/skills/auth-testing/`

### Rule Candidate
- Trigger: impacto sistêmico identificado, falha repetida
- Path: `memory/candidates/rules/<rule-name>/`
- Exemplo: `memory/candidates/rules/dependency-declaration/`

### Agent Candidate
- Trigger: 20+ tasks no mesmo domínio, sobrecarga do agent existente
- Path: `memory/candidates/agents/<agent-name>/`
- Exemplo: `memory/candidates/agents/database-specialist/`

## Validação

- Cada candidate deve ter um `candidate_id` único
- Deve ter `task_id` e `agent` para rastreabilidade
- Deve ter `pattern_detection` com occurrences e tasks
- Deve ter `risk_level` para determinar o fluxo de aprovação
- Deve ter `review` com reviewer e status