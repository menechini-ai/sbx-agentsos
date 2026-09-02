# SKILL.md - dev-story

## Metadados

- **Name**: dev-story
- **Version**: 1.0.0
- **Description**: Descompõe user story em tasks técnicas detalhadas com estimates e dependencies.
- **Owner**: developer
- **Status**: stable

## Inputs

- `story` — User story com acceptance criteria
- `tech_spec` — Tech spec com data model, API contract
- `codebase` — Código existente

## Outputs

- `tasks_breakdown` — Lista de tasks com owner, estimate, dependencies
- `story_report` — Relatório com estimativas, risks, dependencies

## Dependencies

- `tech-spec` — Tech spec deve existir
- `prd-writing` — Stories do PRD

## Tools

- `filesystem.read` — Ler tech spec e código
- `terminal` — Code analysis tools

## Purpose

Quebrar story em tasks granulares para implementação eficiente e estimation precisa.

## When to Use

- Antes de `agentos-build` (para stories complexas)
- Durante sprint planning (para estimation)
- Quando story tem múltiplos componentes

## When NOT to Use

- Quick path (story já é task)
- Stories simples (< 2 points)

## Procedure

1. **Ler Story + Tech Spec**: Entender acceptance criteria e componentes.
2. **Identificar Componentes**: API, database, frontend, tests, docs, infra.
3. **Quebrar em Tasks**: Cada componente vira task com:
   - Description clara
   - Owner (Dev, QA, SRE)
   - Estimate (hours)
   - Dependencies
   - Definition of done
4. **Sequenciar**: Ordenar por dependencies (blockers primeiro).
5. **Estimar Total**: Somar hours, comparar com story points.
6. **Produzir Report**: `story_report` com:
   - `total_hours`: Soma de estimates
   - `risks`: Complexidade subestimada, dependencies
   - `handoff`: Para `agentos-build` (implementation)

## Validation

- Verificar se tasks cobrem todos acceptance criteria
- Confirmar que estimates são realistas (base histórico)
- Confirmar que dependencies estão mapeadas

## Failure Modes

- **Over-decomposition**: Tasks micro-demas; mitigação: agrupar relacionadas
- **Under-estimation**: Tasks parecem simples mas são complexas; mitigação: spike para unknowns
- **Missing tasks**: Componentes esquecidos; mitigação: checklist de review

## Examples

### Exemplo 1: Descompor story de pagamento

```
Input: story={id: "US-001", criteria: ["POST /payments", "Stripe integration"]}
Output: tasks_breakdown=[
  {task: "Create payment handler", owner: "dev", estimate: 4h, deps: []},
  {task: "Stripe SDK integration", owner: "dev", estimate: 3h, deps: []},
  {task: "Database schema migration", owner: "dev", estimate: 2h, deps: []},
  {task: "Unit tests", owner: "dev", estimate: 2h, deps: ["handler"]},
  {task: "Integration tests", owner: "qa", estimate: 2h, deps: ["handler", "stripe"]},
  {task: "API docs update", owner: "dev", estimate: 1h, deps: ["handler"]}
]
```

## Known Limitations

- Requer dev knowledge do codebase
- Estimates melhoram com histórico de velocity

## Improvement Criteria

- **Nova skill**: Quando stories consistentlyVoltam com tasks faltantes
- **Promoção para rule**: Quando task breakdown obrigatório para stories > 3 points

## Changelog

- **1.0.0**: Versão inicial