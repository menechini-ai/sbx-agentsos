# SKILL.md - qa-gate

## Metadados

- **Name**: qa-gate
- **Version**: 1.0.0
- **Description**: Executa QA gate: valida se build atende PRD/spec e está pronto para deploy.
- **Owner**: qa
- **Status**: stable

## Inputs

- `story` — User story com acceptance criteria
- `implementation` — Output de `agentos-build` (changes, tests)
- `test_plan` — Test plan (se existe)

## Outputs

- `qa_report` — Relatório com test results, bugs found, approval/rejection
- `gate_status` — `passed` | `failed` | `conditional`

## Dependencies

- `agentos-build` — Implementation deve existir
- `test-planning` — Test plan (se existe)

## Tools

- `terminal` — Test runners, linters
- `filesystem.read` — Ler implementation
- `github.read` — PR review

## Purpose

Garantir que implementation atende acceptance criteria, não tem bugs críticos, e está seguro para deploy.

## When to Use

- Após `agentos-build` (antes de merge/deploy)
- Antes de deploy em produção
- Para release candidates

## When NOT to Use

- Quick path sem production deploy
- Para infra provisioning (usar SRE validation)

## Procedure

1. **Ler Story + Implementation**: Carregar acceptance criteria e changes.
2. **Validar Acceptance Criteria**: Checklist item por item.
3. **Rodar Testes**: Unit, integration, e2e (se existem).
4. **Revisar Code**: Security review, performance review.
5. **Testar Manualmente**: Se UI, testar fluxo completo.
6. **Checar Metrics**: Datadog monitors (se deploy existente).
7. **Decidir**:
   - `passed`: Todos criteria atendidos, sem bugs críticos
   - `failed`: Bugs críticos ou criteria não atendidos
   - `conditional`: Issues menores que podem ser fixados after merge
8. **Produzir Report**: `qa_report` com:
   - `gate_status`: passed/failed/conditional
   - `criteria_results`: Checklist com pass/fail por criterion
   - `bugs_found`: Lista de bugs com severity
   - `test_coverage`: Unit/integration/e2e coverage
   - `risks`: Known limitations
   - `handoff`: Para `retrospective` (se passed) ou `agentos-build` (se failed)

## Validation

- Verificar se todos acceptance criteria passam
- Confirmar que testes rodam sem erros
- Confirmar que não há bugs de severity critical/high

## Failure Modes

- **False positive**: Tests passam mas app quebra; mitigação: e2e tests
- **Flaky tests**: Tests intermitentes; mitigação: retry logic
- **Scope creep**: QA testa além da story; mitigação: stick to acceptance criteria

## Examples

### Exemplo 1: QA gate para payment feature

```
Input: story={criteria: ["POST /payments returns 201", "Invalid input returns 400"]},
  implementation={tests: {unit: 15, integration: 3, e2e: 2}}
Output: qa_report={gate_status: "passed", criteria_results: [{criterion: "POST /payments", status: "pass"}, {criterion: "Invalid input", status: "pass"}], bugs_found: []}
```

## Known Limitations

- Requer QA com conhecimento do domain
- QA gate não substitui monitoring em produção

## Improvement Criteria

- **Nova skill**: Quando bugs passam consistently por QA gate
- **Promoção para rule**: Quando QA gate obrigatório para todos os deploys

## Changelog

- **1.0.0**: Versão inicial