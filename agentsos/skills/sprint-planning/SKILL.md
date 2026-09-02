# SKILL.md - sprint-planning

## Metadados

- **Name**: sprint-planning
- **Version**: 1.0.0
- **Description**: Executa sprint planning session: seleciona stories, estima, cria sprint backlog e capacity plan.
- **Owner**: pm
- **Status**: stable

## Inputs

- `prd_stories` — User stories do PRD com points e priority
- `team_capacity` — Capacity do time (roles, horas, dias)
- `velocity_history` — Velocity médio dos últimos 3 sprints (opcional)
- `dependencies` — Dependências externas conhecidas
- `risks` — Riscos do sprint

## Outputs

- `sprint_plan` — Sprint Plan preenchido (template: `agentsos/templates/sprint/sprint-plan-template.md`)
- `sprint_report` — Relatório com capacity analysis, risks, commitments

## Dependencies

- `prd-writing` — Stories devem estar no PRD
- `story-slicing` — Stories podem ser sliced durante planning

## Tools

- `filesystem.read` — Ler templates e PRD
- `filesystem.write` — Escrever sprint plan
- `terminal` — Velocity analysis (se disponível)

## Purpose

Planejar sprint com capacity real, velocity realista, e commits claros — evitando overcommit.

## When to Use

- Início de cada sprint
- Após PRD com stories estimadas
- Para sprints de 1-2 semanas

## When NOT to Use

- Quick path
- Kanban (continuous delivery)
- When velocity history unavailable (primeiro sprint)

## Procedure

1. **Ler Inputs**: PRD stories, team capacity, velocity history, dependencies, risks.
2. **Validar Template**: Ler `agentsos/templates/sprint/sprint-plan-template.md`.
3. **Analisar Capacity**:
   - Calcular total hours disponíveis
   - Subtrair holidays, meetings recorrentes
   - Aplicar buffer 20% para unexpected
   - Converter para story points usando velocity médio
4. **Selecionar Stories**:
   - Priorizar por MoSCoW (MUST primeiro)
   - Selecionar até capacity disponível
   - Verificar dependencies não bloqueiam
5. **Descompor em Tasks**: Para cada story, criar tasks com owners e estimates.
6. **Definir Sprint Goal**: 1 frase clara do que o sprint entrega.
7. **Produzir Report**: `sprint_report` com:
   - `status`: `committed` | `over_capacity` | `under_capacity`
   - `capacity_analysis`: Hours vs estimated
   - `risks_identified`: Impacto no sprint
   - `deferred_stories`: Stories que não cabem

## Validation

- Verificar se total points ≤ velocity médio × 1.2 (buffer)
- Confirmar se todas stories HAVE acceptance criteria
- Confirmar se tasks têm owners asignados
- Cross-check com `memory/knowledge` — velocity realista baseado em histórico

## Failure Modes

- **Overcommit**: More stories than capacity; mitigação: velocity buffering
- **Undercommit**: Sprint com folga demais; mitigação: pull from backlog
- **Blocked stories**: Dependencies não resolvidas; mitigação: verify before commitment

## Examples

### Exemplo 1: Planning para sprint 5

```
Input: prd_stories=[US-001(5), US-002(8), US-003(3), US-004(5)], velocity=18, capacity=240h
Output: sprint_plan={goal: "Complete payment flow", committed: [US-001, US-003, US-002], points: 16, buffer: 20%}
```

## Known Limitations

- Requer velocity history para estimativas realistas
- Sprint de 2 semanas é sweet spot — 1 semana pode ser apertado

## Improvement Criteria

- **Nova skill**: Quando sprint consistently over/under committed em 3+ sprints
- **Promoção para rule**: Quando sprint planning obrigatório para todos os times

## Changelog

- **1.0.0**: Versão inicial