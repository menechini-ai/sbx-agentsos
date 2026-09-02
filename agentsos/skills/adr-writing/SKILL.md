# SKILL.md - adr-writing

## Metadados

- **Name**: adr-writing
- **Version**: 1.0.0
- **Description**: Escreve Architecture Decision Records (ADRs) para decisões técnicas não triviais.
- **Owner**: architect
- **Status**: stable

## Inputs

- `decision` — Decisão a documentar
- `alternatives` — Alternativas consideradas (opcional, default: pesquisar)
- `context` — Contexto técnico/organizacional
- `related_prd` — PRD relacionado (opcional)

## Outputs

- `adr` — ADR preenchido (template: `agentsos/templates/architecture/adr-template.md`)
- `adr_id` — ID único do ADR (ex: ADR-0001)

## Dependencies

- `tech-spec` — Para decisões identificadas durante tech spec
- `research` — Para avaliar alternativas

## Tools

- `filesystem.read` — Ler template e ADRs existentes
- `filesystem.write` — Escrever ADR
- `github.read` — Pesquisar decisões anteriores

## Purpose

Documentar decisões arquiteturais com contexto, rationale, consequências — preservando "durable context" para decisões futuras.

## When to Use

- Após `tech-spec` identificar decisões não triviais
- Quando múltiplas alternativas existem
- Quando decisão impacta segurança, performance ou manutenibilidade
- Para decisões reversíveis importantes

## When NOT to Use

- Decisões triviais (ex: usar ESLint)
- Decisões já documentadas em ADRs existentes
- Quick path

## Procedure

1. **Pesquisar ADRs existentes**: Verificar se decisão similar já foi tomada.
2. **Identificar Alternatives**: Listar 2-4 alternativas com pros/cons.
3. **Escrever ADR**:
   - **Context**: Problema e contexto
   - **Decision**: Decisão tomada
   - **Consequences**: Positivas, negativas, riscos
   - **Alternatives Considered**: Tabela comparativa
   - **Implementation Notes**: Como implementar
   - **Related**: Links para PRD, tech spec, outros ADRs
4. **Propose Review**: ADR é Proposed → Aguarda review → Accepted/Rejected
5. **Persistir**: Salvar em `agentsos/templates/architecture/` ou em docs do projeto

## Validation

- Verificar se todas as alternativas têm pros/cons documentadas
- Confirmar que decision é inequívoca
- Cross-check com `memory/knowledge` — evitar contradizer decisões anteriores

## Failure Modes

- **ADR overkill**: Documentar decisões triviais; mitigação: threshold "impacta 2+ systems"
- **Stale ADR**: Decisão muda mas ADR não é atualizado; mitigação: status Superseded
- **No rationale**: Decisão sem justification; mitigação: template exige "Why"

## Examples

### Exemplo 1: Use PostgreSQL over MongoDB

```
Input: decision="Use PostgreSQL for new microservice", alternatives=["MongoDB", "DynamoDB"]
Output: adr={id: "ADR-0001", status: "Accepted",
  context: "Microservice needs relational data + ACID transactions",
  decision: "PostgreSQL",
  pros: [existing infra, SQL expertise, ACID], cons: [schema migrations]
  alternatives: [{mongo: "schema flexibility but no ACID"}, {dynamo: "scalable but vendor lock"}]
  }
```

## Known Limitations

- Requer Arquiteto com visão de trade-offs
- ADRs são reversíveis — usar status "Superseded" quando mudam

## Improvement Criteria

- **Nova skill**: Quando decisões são re-feitas por não terem sido documentadas
- **Promoção para rule**: Quando ADR obrigatório para decisões de stack

## Changelog

- **1.0.0**: Versão inicial