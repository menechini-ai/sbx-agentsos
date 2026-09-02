# SKILL.md - prd-writing

## Metadados

- **Name**: prd-writing
- **Version**: 1.0.0
- **Description**: Escreve Product Requirements Document (PRD) baseado em Brief aprovado.
- **Owner**: pm
- **Status**: stable

## Inputs

- `brief` — Brief aprovado (output de `brief-creation`)
- `research_findings` — Output de `research` skill (opcional)
- `stakeholder_feedback` — Feedback de stakeholders sobre Brief

## Outputs

- `prd` — PRD preenchido (template: `agentsos/templates/prd/prd-template.md`)
- `prd_report` — Relatório com open questions, dependencies, next steps

## Dependencies

- `brief-creation` — Brief deve existir e estar aprovado
- `research` — Para validar assumptions (opcional)

## Tools

- `filesystem.read` — Ler template e brief
- `filesystem.write` — Escrever PRD
- `github.read` — Ver issues/PRs relacionados

## Purpose

Expandir Brief em PRD detalhado com features, user stories, NFRs, release criteria — base para Tech Spec e Sprint Planning.

## When to Use

- Fase Plan (Standard/Full path)
- Após Brief aprovado por stakeholders
- Antes de `tech-spec` (Arquiteto) e `story-slicing`

## When NOT to Use

- Quick path
- Quando PRD já existe e está atualizado
- Para bugs/tech debt (usar task envelope direto)

## Procedure

1. **Ler Brief**: Carregar brief aprovado + research findings.
2. **Validar Template**: Ler `agentsos/templates/prd/prd-template.md`.
3. **Escrever PRD**:
   - **Vision**: Problem statement, solution summary, value prop
   - **Features**: Lista com user stories, acceptance criteria, priority (MoSCoW)
   - **User Stories**: Backlog priorizado com points, dependencies, sprint target
   - **NFRs**: Performance, availability, security, scalability, compliance — com targets mensuráveis
   - **UI/UX**: Links para designs, accessibility, responsive
   - **Data & Analytics**: Events, dashboards, privacy
   - **Release Criteria**: Checklist objetivo
   - **Open Questions**: Rastreadas com owner/due date
4. **Review Interno**: PM self-review contra checklist.
5. **Produzir Report**: `prd_report` com:
   - `status`: `complete` | `needs_review`
   - `open_questions`: Lista com owner
   - `dependencies`: Technical dependencies identificadas
   - `handoff`: Para Arquiteto (`tech-spec`) + Dev (estimation)

## Validation

- Verificar se todas features têm acceptance criteria testáveis
- Confirmar se NFRs têm targets mensuráveis (não "fast", usar "< 200ms p99")
- Confirmar se user stories seguem INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- Cross-check com `memory/knowledge` — evitar re-escrever PRDs para mesmo domain

## Failure Modes

- **PRD over-specified**: Solutioning em vez de requirements; mitigação: foco no "what/why", não "how"
- **Scope creep**: Features `COULD`/`WON'T` não claras; mitigação: MoSCoW rigoroso
- **Stakeholder misalignment**: Aprovação sem review; mitigação: review meeting obrigatório

## Examples

### Exemplo 1: PRD para checkout redesign

```
Input: brief={objective: "Reduce checkout abandonment from 40% to 20%"}, research={competitors: ["Stripe", "Shopify"]}
Output: prd contendo:
  - features: [Guest checkout (MUST), Saved payment (SHOULD), Apple Pay (COULD)]
  - nfrs: {latency: "< 500ms p99", availability: "99.95%"}
  - release_criteria: ["A/B test shows -20% abandonment", "No regression in conversion"]
  - open_questions: ["Legal: PCI scope for guest?", "Design: mobile vs desktop?"]
  - handoff: Arquiteto para tech-spec (payment gateway integration)
```

## Known Limitations

- Requer PM experiente em product discovery
- PRD é living document — atualizar durante sprints
- Não substitui conversation contínua com dev/design

## Improvement Criteria

- **Nova skill**: Quando PRDs consistentemente voltam com muitos changes em 3+ casos
- **Promoção para rule**: Quando PRD template se torna obrigatório para todas features Standard/Full

## Changelog

- **1.0.0**: Versão inicial