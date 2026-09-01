# Test: Contract Envelopes

## Teste: validação de envelopes INPUT/OUTPUT

### Teste: task-envelope.json

1. Verificar se todos os campos obrigatórios presentes:
   - `task.id`, `task.parent_id`
   - `task.sender.agent`, `task.sender.level`
   - `task.receiver.agent`, `task.receiver.level`
   - `task.objective.primary`
   - `task.context.repository`, `task.context.branch`
   - `task.constraints` list
   - `task.resources.skills` list
   - `task.resources.tools` list
   - `task.memory.read` list
   - `task.expected_output.type`, `task.expected_output.required` list
   - `task.deadline.priority`

2. Validar tipos de dados:
   - levels são números inteiros (1, 2, 3, 4, 5)
   - skills e tools são arrays de strings
   - expected_output.required é array de strings

3. Testes de consistência:
   - `sender.level` < `receiver.level` hierarquia esperada
   - skills e tools dentro dos limites da matriz ✅⚠️🔐 de GOVERNANCE.md §01

### Teste: result-envelope.json

1. Verificar se todos os campos obrigatórios presentes:
   - `result.task_id`
   - `result.status`
   - `result.summary` list
   - `result.changes.files` list
   - `result.validation.tests.status`, `result.validation.tests.total`
   - `result.risks` list
   - `result.assumptions` list
   - `result.memory_candidates` list
   - `result.improvement_candidates` list
   - `result.handoff.next_agent`, `result.handoff.required`

2. Validar tipos de dados:
   - `task_id` é string
   - `status` é string (completed/partial/blocked/failed)
   - `summary` é array de strings
   - `changes.files` é array de strings
   - `validation.tests.status` é string
   - `validation.tests.total` é número inteiro
   - `risks` é array de strings
   - `assumptions` é array de strings
   - `memory_candidates` é array de objects com `type`, `description`
   - `improvement_candidates` é array de objects com `type`, `name`, `reason`
   - `handoff.next_agent` é string
   - `handoff.required` é boolean

3. Testes de consistência:
   - `task_id` corresponde ao task envelope original
   - `memory_candidates` e `improvement_candidates` seguem formato padr