# SKILL.md - tech-spec

## Metadados

- **Name**: tech-spec
- **Version**: 1.0.0
- **Description**: Escreve Technical Specification baseado em PRD aprovado, incluindo stack, data model, API, infra.
- **Owner**: architect
- **Status**: stable

## Inputs

- `prd` — PRD aprovado (output de `prd-writing`)
- `codebase_context` — Output de `existing-codebase-analysis` (se codebase existente)
- `constraints` — Tech constraints conhecidos

## Outputs

- `tech_spec` — Tech Spec preenchido (template: `agentsos/templates/architecture/tech-spec-template.md`)
- `tech_spec_report` — Relatório com decisions pendentes, risks, dependencies

## Dependencies

- `prd-writing` — PRD deve existir e estar aprovado
- `existing-codebase-analysis` — Para codebases existentes (opcional)

## Tools

- `filesystem.read` — Ler template, PRD, código existente
- `filesystem.write` — Escrever tech spec
- `github.read` — Analisar arquitetura existente

## Purpose

Traduzir requirements de produto em especificação técnica com stack, data model, API, infra Azure, security, observability.

## When to Use

- Fase Plan (Standard/Full path)
- Após PRD aprovado
- Antes de `adr-writing` e `story-slicing`
- Para migrar codebases existentes (com `existing-codebase-analysis`)

## When NOT to Use

- Quick path
- Quando tech spec já existe e está atualizado
- Para bugs simples (task envelope direto)

## Procedure

1. **Ler PRD**: Carregar PRD + codebase context.
2. **Validar Template**: Ler `agentsos/templates/architecture/tech-spec-template.md`.
3. **Escrever Tech Spec**:
   - **Overview**: Contexto e relation ao PRD
   - **Architecture Diagram**: Mermaid diagram de componentes
   - **Technology Stack**: Tabela com choices e justificativas
   - **Data Model**: Entities, migrations, indexes
   - **API Contract**: Endpoints, request/response, auth
   - **Infrastructure**: Azure resources, networking, IaC
   - **Security**: Auth, authz, secrets, compliance
   - **Observability**: Datadog metrics, logs, traces, SLOs
   - **Deployment**: Strategy (rolling/canary/blue-green), environments
   - **Risks**: Risk register com mitigations
4. **Identificar ADRs**: Marcas decisões não triviais para `adr-writing` skill.
5. **Produzir Report**: `tech_spec_report` com:
   - `status`: `complete` | `needs_review` | `needs_adr`
   - `decisions_pending`: Lista para `adr-writing`
   - `risks_identified`: Risk register
   - `dependencies`: Infra/outros times
   - `handoff`: Para `adr-writing` + `dev-story`

## Validation

- Verificar se diagrama cobre todos os componentes do PRD
- Confirmar se stack choices têm justificativa
- Confirmar se API contract é consistente com PRD features
- Cross-check com guardrails (scope/tools) — infra não viola policies

## Failure Modes

- **Over-engineering**: Solução complexa demais; mitigação: YAGNI, MVP first
- **Under-specification**: Detalhes faltando; mitigação: checklist de seções obrigatórias
- **Stack lock-in**: Choice inflexível; mitigação: documentar trade-offs em ADR

## Examples

### Exemplo 1: Tech spec para payment feature

```
Input: prd={features: [guest_checkout, saved_payment]}, codebase={stack: "Node.js + PostgreSQL + Redis"}
Output: tech_spec contendo:
  - architecture: API Gateway → Payment Service → Stripe API → Database
  - stack: {payment: "Stripe (Why: docs, PCI compliance)", cache: "Redis (existing)"}
  - data_model: payment_methods table, transactions table
  - api: POST /payments, GET /payments/{id}, POST /payment-methods
  - infra: AKS cluster, PostgreSQL Flexible Server, Key Vault
  - observability: Datadog APM + Stripe webhook logs
  - risks: [PCI scope for guest checkout]
```

## Known Limitations

- Requer Arquiteto com visão full-stack
- Tech spec é living document — atualizar durante implementação
- Não substitui spike técnico para decisões complexas

## Improvement Criteria

- **Nova skill**: Quando tech specs consistently deixam gaps críticos em 3+ casos
- **Promoção para rule**: Quando tech spec template se torna obrigatório

## Changelog

- **1.0.0**: Versão inicial