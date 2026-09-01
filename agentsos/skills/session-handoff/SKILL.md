# SKILL.md - session-handoff

## Metadados

- **Name**: session-handoff
- **Version**: 1.0.0
- **Description**: Skill de handoff entre sessões/agentes — transferência de conhecimento, artefatos e estado pendente.
- **Owner**: ceo
- **Status**: stable

## Inputs

- `from_agent` — Agente origem do handoff (ex: developer, researcher, qa)
- `task_id` — ID da tarefa sendo transferida
- `completed` — Lista de itens já concluídos
- `pending` — Lista de itens pendentes
- `artifacts` — Caminhos/artefatos a transferir
- `risks` — Riscos identificados que o próximo agente deve observar
- `instructions` — Instruções específicas para o próximo agente

## Outputs

- `handoff_report` — Relatório estruturado entregue ao agente/próxima sessão

## Dependencies

- `filesystem` — Para leitura/escrita de artefatos durante handoff
- `ai-memory` — Para persistência do estado do handoff e recuperação entre sessões

## Tools

- `filesystem.read` — Ler artefatos, docs, code a ser transferido
- `filesystem.write` — Escrever estado de handoff, persister artefatos
- `ai-memory.read` — Recuperar estado de handoffs anteriores, learning do ai-memory
- `ai-memory.write` — Persistir estado atual de handoff para recuperação futura

## Purpose

Garantir continuidade entre sessões e transferência adequada de conhecimento, estado e responsabilidade entre agentes ou sessões de trabalho, produzindo um `handoff_report` estruturado que possa ser:
- Consumido pelo agente/próxima sessão receptor
- Persistido no `ai-memory` para recuperação futura
- Utilizado como base para `improvement_candidates` e promoção de skills

## When to Use

- Ao encerrar uma sessão de trabalho antes de completar todas as tarefas
- Ao transferir responsabilidade entre agents (ex: developer → qa, qa → security)
- Ao finalizar um trabalho periodicamente e garantir que conhecimento não se perca
- Ao mover de um contexto de agente para outro mantendo continuidade

## When NOT to Use

- Quando todas as tarefas estão completas e não há nada a transferir (encerre simplesmente a sessão)
- Quando o handoff seria para um agente que não tem autoridade sobre os artefatos (verificar matriz ✅⚠️🔐 de GOVERNANCE.md)
- Quando o conhecimento já está adequadamente no `ai-memory` como learning promovido (verificar pipeline Memory→Skill→Rule)

## Procedure

1. **Coletar estado**: Reunir o que foi concluído, o que está pendente, os artefatos e riscos
2. **Persistir no ai-memory**: Salvar estado de handoff para recuperação futura (sessions/, decisions/)
3. **Entregar report**: Produzir `handoff_report` com:
   - `from_agent`: quem estáhando
   - `task_id`: tarefa referência
   - `completed`: itens já feitos
   - `pending`: itens que seguem em frente
   - `artifacts`: what was produced, where
   - `risks`: what the next agent/should be aware of
   - `instructions`: specific guidance for the receiver
4. **Entregar**: Passar o `handoff_report` para o próximo agente/sessão

## Validation

- Verificar se todos os `completed` items foram realmente entregues/no estado correto
- Confirmar que `artifacts` existem e estão acessíveis
- Confirmar que `risks` são reais e documentados (não inventados)
- Cross-check com `ai-memory` — confirmar que estado não contradiz learning promovidos anteriormente

## Failure Modes

- **Incomplete state**: `completed` ou `pending` não refletem realidade; recomenda-se auditoria do estado antes do handoff
- **Artefatos perdidos**: `artifacts` não existem ou estão em path incorreto; recomenda-se verificar filesystem e/github
- **Riscos inventados**: `risks` que não são reais; recomenda-se basar em observações reais da task
- **Authority mismatch**: Handoff para agente sem autorização sobre os artefatos; recomendar verificar matriz ✅⚠️🔐 de GOVERNANCE.md

## Examples

### Exemplo 1: Handoff developer → qa

```
Input: from_agent="developer", task_id="TASK-2026-0001", 
  completed=["authentication implementation"],
  pending=["integration tests"],
  artifacts=["src/auth/", "tests/auth/"],
  risks=["token expiration configuration"],
  instructions=["Validate authentication flow"]

Output: handoff_report contendo:
  - from_agent: developer
  - task_id: TASK-2026-0001
  - completed: authentication implementation
  - pending: integration tests
  - artifacts: src/auth/, tests/auth/
  - risks: token expiration configuration
  - instructions: Validate authentication flow
```

### Exemplo 2: Handoff qa → security

```
Input: from_agent="qa", task_id="TASK-2026-0001",
  completed=["test_report with 42 passed tests"],
  pending=[],
  artifacts=["tests/auth/report.json"],
  risks=["JWT expiration configuration"],
  instructions=["Review token expiration security"]

Output: handoff_report contendo:
  - from_agent: qa
  - task_id: TASK-2026-0001
  - completed: test_report with 42 passed tests
  - pending: (none)
  - artifacts: tests/auth/report.json
  - risks: JWT expiration configuration
  - instructions: Review token expiration security
```

## Known Limitations

- Dependente de estado accuratemente rastreado durante a task
- Pode não cobrir todos os tipos de transferência (ex: transferência entre diferentes projects)
- Requires acesso a filesystem e ai-memory (L0-L2 tools)

## Improvement Criteria

- **Padrão de handoff aprimorado**: Quando handoff detectado como incompleto ou confuso em 3+ occasions (GOVERNANCE.md §02.4)
- **Automação de estado**: Quando tracking state manual se mostra propenso a erros; recomenda-se automação via scripts ou tools
- **Memory promotion**: Quando patterns de handoff aprendidos são relevantes para políticas do projeto

## Changelog

- **1.0.0**: Versão inicial