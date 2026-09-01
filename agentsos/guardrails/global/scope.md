# Guardrail Global — Scope

## Definição

Define onde cada nível de agente pode trabalhar.

## Paths Autorizados por Nível

### L0 — Governance
- **Allowed**: `GOVERNANCE.md`, `docs/`, `proposals/`, `memory/decisions/`, `memory/policies/`
- **Denied**: Nenhum — L0 tem acesso universal (pois é governança)

### L1 — CEO / Principal
- **Allowed**: Todo o project exceto paths de segurança crítica
- **Denied**: Nenhum explícito — CEO tem broad scope para coordenação

### L2 — Department Agent
- **Allowed**: 
  - `agents/` (próprio departamento)
  - `skills/` (uso)
  - `work/` (produção do departamento)
  - `memory/learnings/` (consulta)
  - `contracts/` (leitura de envelopes)
- **Denied**: 
  - `agents/` de outros departamentos
  - `memory/ai-memory/wiki/` (somente leitura via retrieval)
  - `GOVERNANCE.md`
  - `guardrails/`
  - `mcp/`
  - `proposals/`

### L3 — Specialist Agent
- **Allowed**: 
  - Escopo do L3 especializado (ex: `src/auth/` para auth-specialist)
  - `skills/` (uso dentro do scope L3)
  - `work/` (tarefas designadas)
- **Denied**: 
  - `agents/` de outros departamentos
  - `memory/ai-memory/wiki/` (somente leitura via retrieval)
  - `GOVERNANCE.md`, `guardrails/`, `mcp/`
  - `proposals/`
  - Paths de segurança crítica (`secrets/`, `production/`, `config/env/`)

### L4 — Subagent
- **Allowed**: 
  - Escopo estritamente limitado à tarefa designada pelo L3
  - Diretórios e arquivos explicitamente autorizados no task envelope
- **Denied**: 
  - Qualquer diretório não explicitamente autorizado
  - `agents/`, `memory/ai-memory/`, `GOVERNANCE.md`, `guardrails/`, `mcp/`
  - `proposals/`, `tests/` (somente leitura quando designada)

### L5 — Tool / MCP
- **Allowed**: 
  - Operações autorizadas via MCP policies em `mcp/policies/`
  - Paths explicitamente permitidos pelas ferramentas
- **Denied**: 
  - Qualquer operação fora do scope da ferramenta
  - Arquivos ou diretórios não autorizados pela tool configuration

## Paths Específicos Negados (Todos os Níveis Abaixo de L0)

```
secrets/          # Credenciais, tokens, chaves API
production/       # Deploy direto
config/env/       # Variáveis de ambiente sensíveis
memory/ai-memory/wiki/  # Somente leitura via retrieval tool
GOVERNANCE.md     # Somente L0 pode modificar
guardrails/       # Somente L0 pode modificar
mcp/              # Somente L0/L1 pode modificar
```

## Validação de Scope

Todo task envelope INPUT deve incluir campo `scope` com:
- `allowed_paths`: lista de paths onde o agente pode operar
- `denied_paths`: lista de paths onde o agente está explicitamente proibido

Exemplo:
```json
{
  "scope": {
    "allowed_paths": ["src/auth/", "tests/auth/"],
    "denied_paths": ["secrets/", "production/", "memory/ai-memory/wiki/"]
  }
}
```