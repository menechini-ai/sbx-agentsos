# Guardrail Global — Scope

## Definição

Define onde cada nível de agente pode trabalhar.

## Paths Autorizados por Nível

### L0 — Governance
- **Allowed**: `GOVERNANCE.md`, `docs/`, `proposals/`, `memory/candidates/`, `memory/policies/`
- **Denied**: Nenhum — L0 tem acesso universal (pois é governança)

### L1 — CEO / Principal
- **Allowed**: Todo o project exceto paths de segurança crítica
- **Denied**: Nenhum explícito — CEO tem broad scope para coordenação

### L2 — Department Agent
- **Allowed**: 
  - `agents/` (próprio departamento)
  - `skills/` (uso)
  - `work/` (produção do departamento)
  - `memory/candidates/` (consulta)
  - `memory/sessions/` (consulta)
  - `memory/knowledge/` (somente leitura via retrieval)
  - `contracts/` (leitura de envelopes)
- **Denied**: 
  - `agents/` de outros departamentos
  - `memory/knowledge/` (somente leitura via retrieval)
  - `GOVERNANCE.md`
  - `guardrails/`
  - `mcp/`
  - `proposals/`

### L2 — Department Agents (Específicos)

#### PM (Product Manager)
- **Allowed**: `agents/pm/`, `skills/`, `work/pm/`, `agentsos/templates/brief/`, `agentsos/templates/prd/`, `agentsos/templates/stories/`

#### Arquiteto (Architect)
- **Allowed**: `agents/architect/`, `skills/`, `work/architect/`, `agentsos/templates/architecture/`, `docs/architecture-existing.md`

#### Developer
- **Allowed**: `agents/developer/`, `skills/`, `work/developer/`, `src/`, `tests/`

#### QA (Quality Assurance)
- **Allowed**: `agents/qa/`, `skills/`, `work/qa/`, `tests/`, `agentsos/templates/retrospective/`

#### SRE / Platform
- **Allowed**: `agents/sre/`, `agents/sre/azure-devops/`, `agents/sre/azure-cloud/`, `agents/sre/azure-aks/`, `agents/sre/datadog/`, `skills/`, `work/sre/`, `agentsos/templates/iac/`

#### Researcher
- **Allowed**: `agents/researcher/`, `skills/`, `work/researcher/`, `memory/learnings/`, `memory/candidates/`

- **Denied (todos L2)**: 
  - `agents/` de outros departamentos
  - `memory/knowledge/` (somente leitura via retrieval)
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
  - `memory/knowledge/` (somente leitura via retrieval)
  - `GOVERNANCE.md`, `guardrails/`, `mcp/`
  - `proposals/`
  - Paths de segurança crítica (`secrets/`, `production/`, `config/env/`)

### L3 — Specialist Agents (Azure)

#### Azure DevOps (L3)
- **Allowed**: `agents/sre/azure-devops/`, `skills/`, `work/sre/azure-devops/`, `agentsos/templates/pipeline/`

#### Azure Cloud (L3)
- **Allowed**: `agents/sre/azure-cloud/`, `skills/`, `work/sre/azure-cloud/`, `agentsos/templates/iac/`

#### Azure AKS (L3)
- **Allowed**: `agents/sre/azure-aks/`, `skills/`, `work/sre/azure-aks/`, `agentsos/templates/k8s/`

#### Datadog (L3)
- **Allowed**: `agents/sre/datadog/`, `skills/`, `work/sre/datadog/`, `agentsos/templates/monitor/`

- **Denied (todos L3 Azure)**:
  - `agents/` de outros departamentos/especialidades
  - `memory/knowledge/` (somente leitura via retrieval)
  - `GOVERNANCE.md`, `guardrails/`, `mcp/`
  - `proposals/`
  - Paths de segurança crítica (`secrets/`, `production/`, `config/env/`)

### L4 — Subagent
- **Allowed**: 
  - Escopo estritamente limitado à tarefa designada pelo L3
  - Diretórios e arquivos explicitamente autorizados no task envelope
- **Denied**: 
  - Qualquer diretório não explicitamente autorizado
  - `agents/`, `memory/knowledge/`, `memory/sessions/`, `GOVERNANCE.md`, `guardrails/`, `mcp/`
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
memory/knowledge/  # Somente leitura via retrieval tool
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
    "denied_paths": ["secrets/", "production/", "memory/knowledge/"]
  }
}
```

Exemplo para SRE L2:
```json
{
  "scope": {
    "allowed_paths": ["agents/sre/", "agents/sre/azure-devops/", "agents/sre/azure-cloud/", "agents/sre/azure-aks/", "agents/sre/datadog/", "skills/", "work/sre/", "agentsos/templates/iac/"],
    "denied_paths": ["secrets/", "production/", "memory/knowledge/", "GOVERNANCE.md", "guardrails/", "mcp/", "proposals/"]
  }
}
```

Exemplo para Azure AKS L3:
```json
{
  "scope": {
    "allowed_paths": ["agents/sre/azure-aks/", "skills/", "work/sre/azure-aks/", "agentsos/templates/k8s/"],
    "denied_paths": ["secrets/", "production/", "memory/knowledge/", "GOVERNANCE.md", "guardrails/", "mcp/", "proposals/", "agents/sre/azure-devops/", "agents/sre/azure-cloud/", "agents/sre/datadog/"]
  }
}
```