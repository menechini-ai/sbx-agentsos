# SKILL.md - retrospective

## Metadados

- **Name**: retrospective
- **Version**: 1.0.0
- **Description**: Executa sprint retrospective: analisa resultados, identifica aprendizados, cria action items.
- **Owner**: ceo
- **Status**: stable

## Inputs

- `sprint_metrics` — Velocity, bugs, incidents, deploy count
- `sprint_outcome` — Stories done/blocked/carried over
- `team_feedback` — Feedback do time (匿名 opcional)

## Outputs

- `retrospective` — Retro preenchido (template: `agentsos/templates/retrospective/retrospective-template.md`)
- `action_items` — Lista de ações com owners e due dates
- `memory_candidates` — Learnings para `memory/knowledge`

## Dependencies

- `sprint-planning` — Sprint plan deve existir
- `qa-gate` — Test results do sprint

## Tools

- `filesystem.read` — Ler template e sprint data
- `filesystem.write` — Escrever retrospective
- `memory/knowledge.write` — Persistir learnings

## Purpose

Inspecionar o que funcionou, o que não funcionou, e criar ações concretas para melhoria contínua.

## When to Use

- Fim de cada sprint (Standard/Full)
- Após milestone ou release
- Após incidente significativo

## When NOT to Use

- Quick path (sem sprint)
- Kanban (pode ser ad-hoc)

## Procedure

1. **Collect Data**: Ler sprint metrics, outcome, team feedback.
2. **Validar Template**: Ler `agentsos/templates/retrospective/retrospective-template.md`.
3. **Discuss** (facilitated by CEO):
   - **What went well**: Celebrar successes
   - **What didn't go well**: Root cause analysis (5 Whys)
   - **Action items**: Máximo 3, específicos, mensuráveis
4. **Identify Learnings**: Classificar como `process`, `tool`, `technical`, `team`.
5. **Create Memory Candidates**: Para learnings que devem ser promovidos.
6. **Produzir Report**: `retrospective` com:
   - `what_well`: Lista de successes
   - `what_didnt_well`: Lista de issues com root cause
   - `action_items`: Actions com owners e due dates
   - `memory_candidates`: Para `memory/knowledge` pipeline
   - `mood`: Team health scores

## Validation

- Verificar se action items são específicos e mensuráveis
- Confirmar que memory candidates têm tipo e descrição
- Confirmar que root causes são identificados (não apenas symptoms)

## Failure Modes

- **Blame game**: Focar em pessoas em vez de processos; mitigação: safe space, anonymous feedback
- **No action items**: Retro sem follow-through; mitigação: máximo 3 actions com owners
- **Repeating issues**: Mesmos problemas em múltiplos sprints; mitigação: track action item completion

## Examples

### Exemplo 1: Retrospective sprint 5

```
Input: sprint_metrics={velocity: 18, bugs: 2, incidents: 0}, sprint_outcome={done: 5, carried: 1}
Output: retrospective={what_well: ["New payment flow shipped on time"], what_didnt_well: ["API latency spike during deploy"], action_items: [{action: "Add canary deploy for payment service", owner: "SRE", due: "next sprint"}]}
```

## Known Limitations

- Requer facilitador neutro (CEO ideal)
- Retrospective quality depende de psychological safety

## Improvement Criteria

- **Nova skill**: Quando retro consistently geram sem action items
- **Promoção para rule**: Quando retro obrigatório para todos os sprints

## Changelog

- **1.0.0**: Versão inicial