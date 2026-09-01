# Contratos INPUT/OUTPUT

## Visão

Todo agente se comunica através de contratos estruturados. Não se utiliza texto livre para comunicação entre agentes. Os contratos garantem que cada agente saiba: quem pediu, para quem, qual é a missão, qual o contexto, quais são os limites, quais skills pode usar, quais memórias pode consultar, qual output deve produzir.

## Estrutura de Contratos

```
contracts/
├── input/
│   ├── task-envelope.json
│   ├── delegation-envelope.json
│   └── escalation-envelope.json
│   └── schemas/
│       └── task.schema.json
│
└── output/
    ├── result-envelope.json
    ├── failure-envelope.json
    ├── handoff-envelope.json
    └── schemas/
        └── result.schema.json
```

## Contrato INPUT: Task Envelope

```json
{
  "task": {
    "id": "TASK-2026-0001",
    "parent_id": "TASK-2026-0000",
    "sender": {
      "agent": "ceo",
      "level": 1
    },
    "receiver": {
      "agent": "developer",
      "level": 2
    },
    "objective": {
      "primary": "Implementar autenticação"
    },
    "context": {
      "repository": "project",
      "branch": "feature/auth"
    },
    "constraints": [
      "Não alterar arquitetura global",
      "Não adicionar dependências sem aprovação",
      "Manter compatibilidade com API atual"
    ],
    "resources": {
      "skills": ["authentication", "testing"],
      "tools": ["github", "filesystem"]
    },
    "memory": {
      "read": ["decisions/authentication.md"]
    },
    "expected_output": {
      "type": "implementation_report",
      "required": ["status", "changes", "tests", "risks"]
    },
    "deadline": {
      "priority": "high"
    }
  }
}
```

### Campos do Task Envelope

| Campo | Descrição | Obrigatório |
|-------|-----------|-------------|
| `task.id` | Identificador único da tarefa | ✅ |
| `task.parent_id` | ID da tarefa pai | ✅ |
| `task.sender` | Quem enviou (agent + level) | ✅ |
| `task.receiver` | Para quem é destinado (agent + level) | ✅ |
| `task.objective.primary` | Missão principal | ✅ |
| `task.context.repository` | Repositório a ser trabalhado | ✅ |
| `task.context.branch` | Branch de trabalho | ✅ |
| `task.constraints` | Lista de restrições | ✅ |
| `task.resources.skills` | Skills autorizadas | ✅ |
| `task.resources.tools` | Tools autorizadas | ✅ |
| `task.memory.read` | Memórias que podem ser consultadas | ✅ |
| `task.expected_output.type` | Tipo de output esperado | ✅ |
| `task.expected_output.required` | Campos obrigatórios do output | ✅ |
| `task.deadline.priority` | Prioridade da tarefa | ✅ |

## Contrato OUTPUT: Result Envelope

```json
{
  "result": {
    "task_id": "TASK-2026-0001",
    "status": "completed",
    "summary": [
      "Autenticação implementada",
      "Testes adicionados"
    ],
    "changes": {
      "files": ["src/auth/login.ts", "tests/auth/login.test.ts"]
    },
    "validation": {
      "tests": {
        "status": "passed",
        "total": 42
      }
    },
    "risks": [
      "JWT expiration ainda usa configuração padrão"
    ],
    "assumptions": [
      "API existente deve permanecer compatível"
    ],
    "memory_candidates": [
      {
        "type": "learning",
        "description": "Projeto utiliza refresh token de 7 dias"
      }
    ],
    "improvement_candidates": [
      {
        "type": "skill",
        "name": "auth-testing",
        "reason": "Padrão repetido em 4 tarefas"
      }
    ],
    "handoff": {
      "next_agent": "qa",
      "required": true
    }
  }
}
```

### Campos do Result Envelope

| Campo | Descrição | Obrigatório |
|-------|-----------|-------------|
| `result.task_id` | ID da tarefa original | ✅ |
| `result.status` | Status: completed/partial/blocked/failed | ✅ |
| `result.summary` | Resumo das ações realizadas | ✅ |
| `result.changes.files` | Arquivos modificados | ✅ |
| `result.validation.tests.status` | Status dos testes | ✅ |
| `result.validation.tests.total` | Total de testes executados | ✅ |
| `result.risks` | Riscos identificados | ✅ |
| `result.assumptions` | Suposições feitas | ✅ |
| `result.memory_candidates` | Aprendizados para promoção | ✅ |
| `result.improvement_candidates` | Propostas de melhoria | ✅ |
| `result.handoff.next_agent` | Próximo agente para handoff | ✅ |
| `result.handoff.required` | Handoff é obrigatório? | ✅ |

## Cadeia Verificável

```
INPUT
  ↓
PROCESSAMENTO
  ↓
VALIDAÇÃO
  ↓
OUTPUT
  ↓
HANDOFF
```

Cada etapa deve ser verificável contra os contratos definidos.

## Uso

1. O CEO cria um task envelope e envia ao agente destino
2. O agente executa a tarefa seguindo os constraints e recursos autorizados
3. O agente produz um result envelope com status, changes, validation e handoff
4. Se necessário, o handoff transfere o trabalho para o próximo agente