# Learning Entry

## Formato Padrão

```
learning_id: LEARN-2026-0001
task_id: TASK-2026-0001
agent: developer
date: 2026-09-01
type: learning
status: ephemeral

content:
  - "Projeto utiliza refresh token de 7 dias"
  - "Pattern de memory leak detectado em src/memory/cleanup.ts"

context:
  task: "Implementar autenticação"
  repository: "project"
  branch: "feature/auth"

promotion_candidate:
  type: skill  # ou rule, ou agent
  description: "Padrão de refresh token repetido em 4 tarefas"
  occurrences: 4
  confidence: 0.87
```

## Uso

- Aprendidos são registrados em `memory/learnings/` quando:
  - O agente observa algo novo durante a execução
  - O aprendizado ainda não passou pelo pipeline de promoção
  - O pattern ainda não atingiu threshold de repetição (min 3 ocorrências)

## Validação

- Cada learning deve ter um `learning_id` único
- Deve ter referência a `task_id` para rastreabilidade
- Deve ter `agent` e `date` para accountability
- Deve ter `promotion_candidate` se for candidato a promoção futura