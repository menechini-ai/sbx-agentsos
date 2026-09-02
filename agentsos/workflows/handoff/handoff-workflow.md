# Workflow: Handoff

## Propósito

Definir o fluxo de handoff entre agentes/sessões, garantindo continuidade de conhecimento, artefatos e estado pendente.

## Quando Hacer Handoff

1. **Encerramento de sessão**: Ao finalizar trabalho antes de completar todas as tarefas
2. **Transferência entre agents**: Developer → QA, QA → Security, etc.
3. **Fim de dia/período**: Garantir que conhecimento não se perca
4. **Mudança de contexto**: Agente precisa focar em tarefa diferente

## Passos

1. **Coletar estado**: Reunir o que foi concluído, o que está pendente
2. **Persistir no memory/knowledge**: Salvar estado em `memory/sessions/` para recuperação futura
3. **Produzir handoff_report**: Estruturado com completed/pending/artifacts/risks/instructions
4. **Entregar ao receptor**: Passar o handoff_report para o próximo agente/sessão
5. **Recuperar (futuro)**: Ao iniciar nova sessão, recuperar handoff anterior via memory/knowledge retrieval

## Estrutura do Handoff Report

```json
{
  "from_agent": "developer",
  "from_level": 2,
  "task_id": "TASK-2026-0001",
  "completed": ["authentication implementation"],
  "pending": ["integration tests"],
  "artifacts": ["src/auth/", "tests/auth/"],
  "risks": ["token expiration configuration"],
  "instructions": ["Validate authentication flow"],
  "expected": ["test_report"],
  "handoff_id": "HANDOFF-2026-0001",
  "date": "2026-09-01"
}
```

## Validação

- Verificar se todos `completed` items foram realmente entregues/no estado correto
- Confirmar que `artifacts` existem e estão acessíveis
- Confirmar que `risks` são reais e documentados (não inventados)
- Cross-check com `memory/knowledge` — confirmar que estado não contradiz learning promovidos anteriormente

## Exemplos

### Handoff Developer → QA

```json
{
  "from_agent": "developer",
  "from_level": 2,
  "task_id": "TASK-2026-0001",
  "completed": ["authentication implementation"],
  "pending": ["integration tests"],
  "artifacts": ["src/auth/", "tests/auth/"],
  "risks": ["token expiration configuration"],
  "instructions": ["Validate authentication flow"],
  "expected": ["test_report"],
  "handoff_id": "HANDOFF-2026-0001",
  "date": "2026-09-01"
}
```

### Handoff QA → Security

```json
{
  "from_agent": "qa",
  "from_level": 3,
  "task_id": "TASK-2026-0001",
  "completed": ["test_report with 42 passed tests"],
  "pending": [],
  "artifacts": ["tests/auth/report.json"],
  "risks": ["JWT expiration configuration"],
  "instructions": ["Review token expiration security"],
  "expected": ["security review"],
  "handoff_id": "HANDOFF-2026-0002",
  "date": "2026-09-01"
}
```