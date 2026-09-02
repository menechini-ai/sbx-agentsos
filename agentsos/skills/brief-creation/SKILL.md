# SKILL.md - brief-creation

## Metadados

- **Name**: brief-creation
- **Version**: 1.0.0
- **Description**: Cria Product Brief a partir de ideia vaga ou task envelope, usando template padrão.
- **Owner**: pm
- **Status**: stable

## Inputs

- `topic` — Ideia, problema ou opportunity statement
- `stakeholders` — Lista de stakeholders conhecidos
- `constraints` — Constraints conhecidos (timeline, budget, tech, compliance)
- `context` — Contexto adicional (market data, user feedback, tech debt)

## Outputs

- `brief` — Product Brief preenchido (template: `agentsos/templates/brief/product-brief-template.md`)
- `brief_report` — Relatório com gaps identificados, next steps

## Dependencies

- `brainstorming` — Para explorar ideia antes (opcional)
- `research` — Para validar assumptions (opcional)

## Tools

- `filesystem.read` — Ler template
- `filesystem.write` — Escrever brief
- `github.read` — Ver issues/PRs relacionados

## Purpose

Transformar vaga noção em Brief estruturado com objective, scope, constraints, success criteria — entrada para PRD writing.

## When to Use

- Fase Clarify (Standard/Full path)
- Quando task envelope tem objective vago
- Antes de `prd-writing` skill

## When NOT to Use

- Quick path (→ Build direto)
- Quando Brief já existe e está aprovado
- Para tarefas puramente técnicas sem product scope

## Procedure

1. **Ler Inputs**: Coletar topic, stakeholders, constraints, context do task envelope ou conversa.
2. **Validar Template**: Ler `agentsos/templates/brief/product-brief-template.md`.
3. **Preencher Brief**:
   - **Objective**: 1-2 frases, outcome mensurável
   - **Stakeholders**: Mapear RACI
   - **Scope**: In/Out explícito
   - **Constraints**: Timeline, budget, tech, compliance
   - **Success Criteria**: 3-5 métricas mensuráveis (não vanity metrics)
4. **Identificar Gaps**: Marcar seções incompletas com `[TBD]` e next steps.
5. **Produzir Report**: `brief_report` com:
   - `status`: `complete` | `partial` (tem TBDs)
   - `gaps`: Lista de TBDs com owner e due date
   - `next_steps`: Ex: "Validate constraints with SRE", "Research competitors"
   - `handoff`: Para `prd-writing` se complete, ou `research` se gaps críticos

## Validation

- Verificar se Objective é SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- Confirmar se Success Criteria são mensuráveis (não "better UX")
- Confirmar se Scope In/Out é mutuamente exclusivo e coletivamente exaustivo
- Cross-check com `memory/knowledge` — evitar duplicar briefs existentes

## Failure Modes

- **Brief vago**: Objective não mensurável; mitigação: template exige métricas
- **Stakeholders missing**: Aprovação atrasada; mitigação: RACI obrigatório
- **Constraints não realistas**: Timeline impossível; mitigação: validar com Dev/SRE antes de aprovar

## Examples

### Exemplo 1: Feature de onboarding

```
Input: topic="Improve user onboarding", stakeholders=["PM", "UX", "Dev"], constraints=["2 sprints", "no DB migration"]
Output: brief contendo:
  - objective: "Reduce time-to-first-value from 15min to 5min for new users"
  - success_criteria: ["TTV p50 < 5min", "Activation rate +20%", "Support tickets -30%"]
  - gaps: ["UX mockups needed", "SRE: infra for feature flags"]
  - next_steps: ["UX: mockups by Friday", "Dev: spike feature flags"]
```

## Known Limitations

- Requer PM com product sense
- Não substitui discovery contínuo com usuários
- Brief é living document — atualizar conforme learnings

## Improvement Criteria

- **Nova skill**: Quando briefs consistentemente incompletos em 3+ casos
- **Promoção para rule**: Quando brief template se torna obrigatório para todas features

## Changelog

- **1.0.0**: Versão inicial