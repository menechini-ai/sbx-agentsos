# SKILL.md - research

## Metadados

- **Name**: research
- **Version**: 1.0.0
- **Description**: Skill de pesquisa e análise — coleta, síntese e análise de informações de fontes externas.
- **Owner**: researcher
- **Status**: stable

## Inputs

- `api_spec` — Especificação da API ou domínio a ser pesquisado (opcional)
- `endpoint` — Endpoint ou pergunta específica a ser respondida (opcional)

## Outputs

- `test_report` — Relatório estruturado com findings, sources e recomendações

## Dependencies

- `http-client` — Para requisições a fontes externas
- `filesystem` — Para leitura de documentos locais

## Tools

- `filesystem.read` — Ler documentos, artigos, papers
- `filesystem.write` — Escrever findings, summaries
- `github.read` — Issues, discussions, code review como fonte de informação
- `github.write` — Comentar, documentar findings

## Purpose

Realizar pesquisa aprofundada sobre um domínio, tópico ou questão específica, produzindo um relatório estruturado que possa ser:
- Reutilizado por outros agents
- Promovido para conhecimento persistente no ai-memory
- Utilizado como base para skills ou rules

## When to Use

- Quando necessário coletar informações de múltiplas fontes
- Antes de implementar uma feature onde há falta de conhecimento sobre o domínio
- Para síntese de conhecimento existente antes de criar novo
- Para apoiar decisões de arquitetura ou design

## When NOT to Use

- Quando a informação já está disponível no `ai-memory` (consultar antes)
- Quando a tarefa requer implementação de código (usar `coding` skill)
- Quando a tarefa requer testes (usar `testing` skill)
- Quando a decisão precisa ser tomada imediatamente sem pesquisa (usar expertise existente)

## Procedure

1. **Coletar fontes**: Identificar e ler documentos, artigos, issues, código relevante
2. **Analisar padrões**: Identificar tendências, conflitos, lacunas no conhecimento
3. **Sintetizar findings**: Estruturar o relatório com:
   - Contexto/research question
   - Sources consultadas (com citations)
   - Findings principais
   - Lacunas identificadas
   - Recomendações
4. **Validar**: Cross-check com `ai-memory` — verificar se informação já foi aprendida/promovida anteriormente
5. **Entregar**: Produzir `test_report` output estruturado

## Validation

- Verificar se todas as sources foram citadas no `test_report`
- Cross-check com `ai-memory` — confirmar que informação não está já registrada
- Confirmar que o relatório responde à pergunta/necessidade original

## Failure Modes

- **Sources incompletas**: Apenas uma fonte consultada; recomenda-se consultar mais fontes antes de entregar
- **Hallucination**: Findings baseados em suposições não-verificadas; recomenda-se validação cruzada
- **Lacunas não identificadas**: Recommendations baseadas em conhecimento incompleto; recomenda-se identificar lacunas explicitamente

## Examples

### Exemplo 1: Pesquisa de API

```
Input: endpoint="authentication flow"
Output: test_report contendo:
  - Sources: OAuth 2.0 spec, Django auth docs, Flask security guide
  - Findings: JWT flow, token refresh, scope strategies
  - Recommendations: Use refresh tokens de 7 dias, implementar rotation
```

### Exemplo 2: Análise de Padrão

```
Input: repeated_task="test API authentication"
Output: test_report contendo:
  - Sources: 4 task histories, ai-memory sessions
  - Findings: Pattern detected em 4/4 tasks; common failure em token expiration
  - Recommendation: Consider creating "auth-testing" skill
```

## Known Limitations

- Dependente da disponibilidade e qualidade das fontes externas
- Pode não cobrir domínios extremamente novos ou nichos sem documentação existente
- síntese pode perder nuances de fontes complexas

## Improvement Criteria

- **Nova skill proposta**: Quando pattern detectado em 4+ tasks (como definido em GOVERNANCE.md §02.4)
- **Promoção para rule**: Quando padrão sistêmico identificado impactando múltiplos domains
- **Memory promotion**: Quando aprendizado relevante para arquitetura do projeto

## Changelog

- **1.0.0**: Versão inicial