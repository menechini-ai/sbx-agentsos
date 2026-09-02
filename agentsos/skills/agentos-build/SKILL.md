# SKILL.md - agentos-build

## Metadados

- **Name**: agentos-build
- **Version**: 1.0.0
- **Description**: Implementa código/infra baseado em tech spec e stories aprovadas.
- **Owner**: developer
- **Status**: stable

## Inputs

- `story` — User story com acceptance criteria
- `tech_spec` — Tech spec com API contract, data model, stack
- `codebase` — Código existente no repo

## Outputs

- `implementation_report` — Relatório com changes, tests, validation

## Dependencies

- `tech-spec` — Tech spec aprovado
- `sprint-planning` — Story atribuída no sprint

## Tools

- `filesystem.read/write` — Código fonte e configs
- `github.read/write` — Branches, commits, PRs
- `terminal` — Build, test, lint commands

## Purpose

Implementar feature/bugfix seguindo tech spec, escrevendo código limpo, testado e documentado.

## When to Use

- Fase Build (todos os paths)
- Story atribuída no sprint plan
- Quick path (direto)

## When NOT to Use

- Antes de tech spec/prd existirem
- Para infra provisioning (usar `resource-provisioning`)
- Para deploy em prod sem QA gate

## Procedure

1. **Ler Story + Tech Spec**: Carregar acceptance criteria e API contract.
2. **Criar Branch**: `feature/US-XXX-description` a partir de `main`.
3. **Implementar**: Seguir tech spec, escrever código modular e testável.
4. **Escrever Tests**: Unit tests (>80% coverage), integration tests.
5. **Rodar Quality Gate**: `npm run quality` ou equivalente.
6. **Commit**: Conventional commits (`feat:`, `fix:`, `refactor:`).
7. **Criar PR**: Link para story, descrição com changes.
8. **Produzir Report**: `implementation_report` com:
   - `status`: `completed` | `partial` | `blocked`
   - `changes`: Files modificados + descrição
   - `tests`: Unit/integration test results
   - `risks`: Known limitations
   - `handoff`: Para QA (`qa-gate`)

## Validation

- Verificar se acceptance criteria da story são atendidos
- Confirmar que tests passam
- Confirmar que lint/format passam
- Cross-check com tech spec — implementation matches spec

## Failure Modes

- **Spec drift**: Implementation diverge from tech spec; mitigação: review tech spec regularly
- **Missing tests**: Code without tests; mitigação: TDD approach
- **Scope creep**: Implementing beyond story; mitigação: stick to acceptance criteria

## Examples

### Exemplo 1: Implement payment endpoint

```
Input: story={id: "US-001", criteria: ["POST /payments returns 201", "Invalid input returns 400"]},
  tech_spec={endpoint: "POST /payments", schema: {amount: number, currency: string}}
Output: implementation_report={status: "completed", changes: ["src/payments/handler.ts", "tests/payments.test.ts"], tests: {unit: 15, integration: 3}}
```

## Known Limitations

- Requer tech spec detalhado para implementação eficiente
- Não cobre infra provisioning (usar SRE skills)

## Improvement Criteria

- **Nova skill**: Quando padrão de implementação se repete em 4+ stories
- **Promoção para rule**: Quando coding standard se torna obrigatório

## Changelog

- **1.0.0**: Versão inicial