# Workflow: Delegation

## Propósito

Definir o fluxo de delegação de tarefas do CEO → Agents → Subagents, garantindo que cada nível tenha autoridade adequada e os contratos INPUT/OUTPUT são respeitados.

## Passos

1. **CEO cria tarefa**
   - Task envelope criado em `contracts/input/task-envelope.json`
   - Nível da tarefa definido (L1, L2, L3 ou L4)
   - Constraints, skills e tools autorizadas definidas

2. **CEO delega**
   - Tarefa enviada ao agente receptor
   - Agent nível verificado contra matriz ✅⚠️🔐 de GOVERNANCE.md §01
   - Autorização conferida

3. **Agent executa**
   - Agent começa EXECUTION imediatamente (EXECUTION-FIRST POLICY)
   - Durante execução, pode OBSERVE patterns, gaps, failures
   - Registro de aprendizados em `memory/learnings/` ou candidates em `memory/candidates/`

4. **Agent valida**
   - OUTPUT envelope criado em `contracts/output/result-envelope.json`
   - Validação de: conformidade a constraints, results esperados, risks identificados

5. **Handoff**
   - Se necessário, handoff criado para próximo agente/sessão
   - `handoff_report` estruturado com completed/pending/artifacts/risks/instructions

## Riscos e Guardrails

- **Authority violation**: Agent tenta agir fora de seu nível — guardrails impedem
- **Scope violation**: Agent tenta modificar paths não autorizadas — guardrails impedem
- **Governance violation**: Agent tenta modificar GOVERNANCE.md, hierarquia — 🔐 requiere aprovação

## Exemplos

### Delegação CEO → Developer

```json
{
  "task": {
    "id": "TASK-2026-0001",
    "sender": {"agent": "ceo", "level": 1},
    "receiver": {"agent": "developer", "level": 2},
    "objective": {"primary": "Implementar autenticação"},
    "constraints": ["Não alterar arquitetura global"],
    "resources": {
      "skills": ["authentication", "testing"],
      "tools": ["github", "filesystem"]
    },
    "memory": {"read": ["decisions/authentication.md"]},
    "expected_output": {"type": "implementation_report", "required": ["status", "changes", "tests", "risks"]}
  }
}
```

### Delegação Developer → QA (Handoff)

```json
{
  "handoff": {
    "from": {"agent": "developer", "level": 2},
    "to": {"agent": "qa", "level": 3},
    "task_id": "TASK-2026-0001",
    "completed": ["authentication implementation"],
    "pending": ["integration tests"],
    "artifacts": ["src/auth/", "tests/auth/"],
    "risks": ["token expiration configuration"],
    "instructions": ["Validate authentication flow"],
    "expected": ["test_report"]
  }
}
```