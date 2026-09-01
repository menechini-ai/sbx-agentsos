# Workflow: Review

## Propósito

Definir o fluxo de revisão pós-tarefa (POST-TASK REVIEW), garantindo que aprendizados sejam registrados e candidatos a skills/rules sejam propostos adequadamente.

## Quando Revisão

1. **Após conclusão de tarefa**: Quando task status = completed
2. **Após interrupção segura**: Quando task bloqueada mas trabalho pode ser resumido
3. **Detecção de patterns**: Agente observa padrões repetidos durante execução

## Passos

1. **Review Pós-Tarefa**
   - `what_worked`: O que resolveu 80%+ da tarefa
   - `what_failed`: O que não funcionou ou obstacles encontrados
   - `repeated_pattern`: Padrões detectados (true/false, occurrences se sim)
   - `improvement`: Tipo de melhoria proposta (skill/agent/rule/workflow/doc) + proposal + confidence score (0-1)

2. **Registro de Aprendizados**
   - Learning entry criado em `memory/learnings/` se ainda não passou pelo pipeline
   - Candidate criado em `memory/candidates/` se atingiu threshold de repetição (min 3 ocorrências)

3. **Proposta de Melhoria**
   - Se `improvement.type` = skill: criado em `proposals/skills/`
   - Se `improvement.type` = agent: criado em `proposals/agents/`
   - Se `improvement.type` = rule: criado em `proposals/rules/`
   - Se `improvement.type` = workflow/doc: criado em `proposals/workflow/` ou `proposals/architecture/`

4. **Pipeline de Promoção**
   - Candidate → Risk Analysis → Review → Test → Approve → Deploy (se aplicável)
   - Segue políticas de risco LOW/MEDIUM/HIGH de GOVERNANCE.md §02.4

## Exemplos

### Review Pós-Tarefa

```json
{
  "task_id": "TASK-2026-0001",
  "what_worked": ["Skill X resolveu 80% da tarefa"],
  "what_failed": ["Não havia skill para testes de integração"],
  "repeated_pattern": {"detected": true, "occurrences": 5},
  "improvement": {
    "type": "new_skill",
    "proposal": "integration-testing",
    "confidence": 0.87
  }
}
```

### Fluxo Resultante

1. Review registrado em `memory/learnings/` ou `memory/candidates/`
2. Candidate detectado: pattern em 5 tasks → skill candidate
3. Proposta criada em `proposals/skills/integration-testing/`
4. Review por L1 CEO → approval → pipeline Memory→Skill→Rule
5. Se aprovado: `skills/integration-testing/SKILL.md` criado e ativado