# SKILL.md - review

## Metadados

- **Name**: review
- **Version**: 1.0.0
- **Description**: Code review estruturado com checklist de qualidade, security e performance.
- **Owner**: developer
- **Status**: stable

## Inputs

- `pr` — Pull request com changes
- `tech_spec` — Tech spec para referência
- `story` — Story context

## Outputs

- `review_report` — Relatório com findings, approval/rejection
- `review_status` — `approved` | `changes_requested` | `comment`

## Dependencies

- `agentos-build` — PR deve existir

## Tools

- `github.read` — Ler PR diff
- `github.write` — Comentar, approve/request changes
- `filesystem.read` — Ler código completo

## Purpose

Revisar PR de forma estruturada, garantindo qualidade, security e adherence ao tech spec.

## When to Use

- Após `agentos-build` cria PR
- Antes de merge
- Para PRs grandes ou complexos

## When NOT to Use

- Quick path sem PR (commit direto)
- Para docs only changes

## Procedure

1. **Ler PR**: Ler diff, description, linked story.
2. **Checklist de Review**:
   - **Correctness**: Implementation matches acceptance criteria?
   - **Code Quality**: Naming, complexity, DRY, YAGNI?
   - **Tests**: Adequate coverage, edge cases covered?
   - **Security**: Input validation, auth, secrets handling?
   - **Performance**: No N+1 queries, proper indexing, caching?
   - **Maintainability**: Readable, documented, follows conventions?
3. **Comentar**: Adicionar inline comments para issues.
4. **Decidir**:
   - `approved`: Ready to merge
   - `changes_requested`: Issues significant precisam de fix
   - `comment`: Suggestions opcionais
5. **Produzir Report**: `review_report` com:
   - `review_status`: approved/changes_requested/comment
   - `findings`: Lista com severity, location, description
   - `suggestions`: Melhorias opcionais
   - `risks`: Known limitations do PR

## Validation

- Verificar se todos findings têm severity e location
- Confirmar que critical findings bloqueiam merge
- Cross-check com tech spec — implementation matches

## Failure Modes

- **Rubber stamping**: Approve without reading; mitigação: checklist obrigatório
- **Nitpicking**: Focar em style em vez de substance; mitigação: severity levels
- **Missed bugs**: Review não pega bugs; mitigação: pair review para changes críticos

## Examples

### Exemplo 1: Review para payment handler

```
Input: pr={files: ["src/payments/handler.ts", "tests/payments.test.ts"], additions: 150}
Output: review_report={review_status: "approved", findings: [{severity: "low", location: "handler.ts:42", description: "Consider using logger instead of console.log"}]}
```

## Known Limitations

- Requer reviewer com knowledge do domain
- Não substitui QA testing

## Improvement Criteria

- **Nova skill**: Quando review consistently miss bugs em 3+ PRs
- **Promoção para rule**: Quando review obrigatório para todos os PRs

## Changelog

- **1.0.0**: Versão inicial