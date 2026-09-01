# SKILL.md - coding

## Metadados

- **Name**: coding
- **Version**: 1.0.0
- **Description**: Skill de desenvolvimento — implementação de código, reviews, debugging e testes conforme contratos.
- **Owner**: developer
- **Status**: stable

## Inputs

- `task_id` — ID da tarefa referenciando o contrato INPUT em `contracts/input/`
- `objective` — Descrição da implementação requerida
- `context` — Contexto adicional (repository, branch, constraints)

## Outputs

- `implementation_report` — Relatório estruturado com changes, validation e risks

## Dependencies

- `github` — Acesso ao repository, issues, PRs
- `filesystem` — Leitura/escrita de arquivos source e tests

## Tools

- `github.read` — Ler código fonte, issues, PRs, commits
- `github.write` — Criar branches, commits, PRs, issues
- `filesystem.read` — Ler arquivos source, tests, configs
- `filesystem.write` — Escrever código source, tests, configs
- `terminal` — Executar comandos de build, test, lint quando necessário

## Purpose

Implementar features, corrigir bugs, refatorar código ou adicionar testes conforme contrato INPUT recebido, produzindo um `implementation_report` estruturado que possa ser:
- Validado através dos contratos OUTPUT
- Promovido para knowledge no ai-memory
- Servir de base para future skills ou rules

## When to Use

- Quando receber um task envelope INPUT com objective de implementação
- Quando necessário implementar uma feature baseada em requisitos claros
- Para debugging de código existente quando o problema está bem definido
- Para adicionar testes quando a implementação requer cobertura

## When NOT to Use

- Quando a task requer pesquisa extensa antes da implementação (usar `research` skill primeiro)
- Quando o problema não está bem definido (usar `debugging` skill ou clarification)
- Quando a mudança requer aprovação de governança (verificar `GOVERNANCE.md` §01 matriz de autorização)
- Quando a task envolve configurações de MCP que não estão no escopo L2 (needs L1 approval)

## Procedure

1. **Ler task envelope**: Consultar `contracts/input/task-envelope.md` para entender:
   - Objective preciso
   - Constraints e boundaries
   - Skills e tools autorizadas (matriz ✅⚠️🔐 de GOVERNANCE.md)
   - Memory que pode ser consultada
2. **Explorar código**: Utilizar `github.read` e `filesystem.read` para entender:
   - Estrutura do repository
   - Código existente relacionado
   - Patterns e conventions do projeto
3. **Implementar**: Escrever código conforme constraints, following project conventions
4. **Escrever tests**: Implementar testes que validam a implementação
5. **Validar**: Cross-check com:
   - Conformance a GOVERNANCE.md authority limits
   - Existing tests não quebrados
   - Code conventions do projeto
6. **Produzir report**: Gerar `implementation_report` com:
   - `status`: completed/partial/blocked
   - `changes`: files modificados + descrição succinta
   - `validation`: status dos testes (passed/failed/total)
   - `risks`: risks identificados, assumptions feitas
   - `memory_candidates`: aprendizados para promover
   - `improvement_candidates`: skills/patterns a propor

## Validation

- Verificar se todas as constraints do task envelope foram respeitadas
- Confirmar que changes não violam authority limits de GOVERNANCE.md §01
- Confirmar que tests passam no número especificado (ou documentar failures)
- Cross-check com `ai-memory` — promover learning se aplicável

## Failure Modes

- **Constraint violation**: Code written outside boundaries autorizadas; recomenda-se revisar constraints e refatorar
- **Test failures**: Tests falhando; recomenda-se debugging e ajuste de implementation
- **Authority overreach**: Implementation tentando modificar GOVERNANCE.md ou hierarquia; recomenda-se propoer mudança via `proposals/`

## Examples

### Exemplo 1: Implementar Feature

```
Input: task_id="TASK-2026-0001", objective="Implementar autenticação", 
  constraints=["Não alterar arquitetura global"]
Output: implementation_report contendo:
  - status: completed
  - changes: [src/auth/login.ts, tests/auth/login.test.ts]
  - validation: tests status: passed, total: 42
  - risks: ["JWT expiration ainda usa configuração padrão"]
  - memory_candidates: [type: learning, description: "Projeto utiliza refresh token de 7 dias"]
  - improvement_candidates: [type: skill, name: "auth-testing", reason: "Padrão repetido em 4 tarefas"]
```

### Exemplo 2: Bug Fix

```
Input: task_id="TASK-2026-0002", objective="Corrigir memory leak", 
  constraints=["Não alterar estrutura de memória"]
Output: implementation_report contendo:
  - status: completed
  - changes: [src/memory/cleanup.ts]
  - validation: tests status: passed, total: 15
  - risks: baixo
  - memory_candidates: [type: learning, description: "Pattern de leak detectado; promover para rule"]
```

## Known Limitations

- Dependente de specifications claras no task envelope
- Pode não cobrir edge cases se constraints forem muito restritivas
- Requires acesso a github e filesystem (L2 tools)

## Improvement Criteria

- **Nova skill proposta**: Quando pattern repetido em 4+ tasks (GOVERNANCE.md §02.4)
- **Promoção para rule**: Quando bug/pattern sistêmico impacta múltiplas tasks
- **Memory promotion**: Quando aprendizado relevante para arquitetura ou padrões de código

## Changelog

- **1.0.0**: Versão inicial