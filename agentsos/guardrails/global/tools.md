# Guardrail Global — Tool Usage

## Definição

Define quais ferramentas (MCP, filesystem, github, terminal, etc.) cada nível de agente pode usar.

## Ferramentas Autorizadas por Nível

### L0 — Governance
- **Allowed**: 
  - `filesystem.read` — leitura de todo o filesystem
  - `github.read` — leitura de todo o repository
  - `github.write` — escrita em branches proposal/, docs/
  - `terminal` — qualquer comando necessário
- **Denied**: 
  - `production.deploy`
  - `secrets.export`

### L1 — CEO / Principal
- **Allowed**: 
  - `filesystem.read` — leitura de todo o filesystem
  - `filesystem.write` — escrita exceto paths de segurança
  - `github.read` — leitura de issues, PRs, código
  - `github.write` — criação de issues, PRs, branches feature/
  - `terminal` — comandos de coordenação
- **Denied**: 
  - `production.deploy`
  - `secrets.export`
  - `mcp.permissions.modify` (solicita a L0)

### L2 — Department Agent
- **Allowed**: 
  - `filesystem.read` — leitura do escopo do departamento
  - `filesystem.write` — escrita do escopo do departamento
  - `github.read` — leitura de issues, PRs, código
  - `github.write` — criação de branches feature/, commits, PRs
  - `terminal` — comandos de build, test, lint
- **Denied**: 
  - `production.deploy`
  - `secrets.export`
  - `mcp.permissions.modify`
  - `mcp.servers.modify`
  - Operações fora do escopo do departamento

### L2 — Department Agents (Tools Específicas)

#### PM
- **Allowed**: L2 base + `github.read` (issues, PRs), `github.write` (issues, PRs), `terminal` (npx, npm para scripts de planning)

#### Arquiteto
- **Allowed**: L2 base + `terminal` (diagram tools, architecture docs generators)

#### Developer
- **Allowed**: L2 base + `terminal` (npm, pip, cargo, go, docker build, kubectl para dev)

#### QA
- **Allowed**: L2 base + `terminal` (test runners, k6, playwright, kubectl para test)

#### SRE / Platform
- **Allowed**: L2 base + `terminal` (az cli, kubectl, helm, terraform, bicep, datadog cli)
- **Denied**: L2 base + `production.deploy` (requer 🔐)

#### Researcher
- **Allowed**: L2 base + `terminal` (curl, wget, python para data analysis)

### L3 — Specialist Agent
- **Allowed**: 
  - `filesystem.read` — leitura do scope especializado
  - `filesystem.write` — escrita do scope especializado
  - `github.read` — leitura de issues, PRs, código
  - `github.write` — commits, PRs (dentro do scope)
  - `terminal` — comandos especializados (ex: database queries, test runs)
- **Denied**: 
  - `production.deploy`
  - `secrets.export`
  - `mcp.*` (qualquer operação MCP)
  - Operações fora do scope especializado

### L3 — Specialist Agents Azure (Tools Específicas)

#### Azure DevOps (L3)
- **Allowed**: L3 base + `az devops` (pipelines, repos, boards), `az pipelines` (build, release)
- **Denied**: L3 base + `production.deploy` (requer 🔐 via L1/L2)

#### Azure Cloud (L3)
- **Allowed**: L3 base + `az cli` (resource group, vnet, subnet, nsg, keyvault, policy), `bicep` (build, what-if), `terraform` (init, plan, apply)
- **Denied**: L3 base + `terraform apply` em prod (requer 🔐), `az deployment` em prod (requer 🔐)

#### Azure AKS (L3)
- **Allowed**: L3 base + `az aks` (create, update, upgrade, get-credentials), `kubectl` (apply, rollout, get, describe), `helm` (install, upgrade, template)
- **Denied**: L3 base + `az aks upgrade` em prod (requer 🔐), `kubectl delete` em prod (requer 🔐)

#### Datadog (L3)
- **Allowed**: L3 base + `datadog.api` (monitors, dashboards, slo, integrations), `datadog.terraform` (provider), `datadog.cli`
- **Denied**: L3 base + `datadog.api` delete em prod (requer 🔐)

### L4 — Subagent
- **Allowed**: 
  - `filesystem.read` — leitura dos paths explicitamente autorizados no task envelope
  - `filesystem.write` — escrita dos paths explicitamente autorizados no task envelope
  - `terminal` — comandos estritamente necessários para a tarefa designada
- **Denied**: 
  - `github.*` (qualquer operação GitHub)
  - `mcp.*` (qualquer operação MCP)
  - Qualquer operação fora do scope designado

### L5 — Tool / MCP
- **Allowed**: 
  - Somente as operações explicitamente autorizadas em `mcp/policies/`
- **Denied**: 
  - Qualquer operação não listada na configuração do MCP

## MCP Policies

Ferramentas MCP devem ser configuradas em `mcp/servers/` com policies em `mcp/policies/`.

Exemplo de policy:
```json
{
  "tool": "github",
  "allowed_levels": ["L0", "L1", "L2", "L3"],
  "denied_operations": ["production.deploy", "secrets.export"],
  "scope_rules": {
    "L2": "department-scoped",
    "L3": "specialist-scoped",
    "L4": "none"
  }
}
```

Exemplo para Azure:
```json
{
  "tool": "az",
  "allowed_levels": ["L0", "L1", "L2", "L3"],
  "denied_operations": ["production.deploy", "secrets.export", "az deployment create --resource-group production"],
  "scope_rules": {
    "L2": "sre-scoped",
    "L3": "azure-specialist-scoped"
  }
}
```

Exemplo para Datadog:
```json
{
  "tool": "datadog",
  "allowed_levels": ["L0", "L1", "L2", "L3"],
  "denied_operations": ["production.deploy", "secrets.export", "monitor.delete"],
  "scope_rules": {
    "L2": "sre-scoped",
    "L3": "datadog-specialist-scoped"
  }
}
```

## Command Hardening (CLAW-HCG Inspired)

Alguns comandos são bloqueados por padrão por razões de segurança (Self-Healing Paradox):

**Bloqueados para L2+**:
- `pip install`, `npm install` — adicionar dependências sem aprovação
- `rm -rf`, `rm -r` — remoção recursiva
- `chmod 777`, `chown` — mudança de permissões
- `curl | bash`, `wget | sh` — execução de scripts remotos

**Bloqueados para L1+**:
- Qualquer comando que modifique `GOVERNANCE.md`, `guardrails/`, `memory/knowledge/`
- Qualquer comando de deploy direto (`git push production`, `npm publish`, etc.)

**Bloqueados para L3 Azure**:
- `az deployment create --resource-group production` — deploy direto em prod
- `terraform apply -auto-approve` em prod
- `az aks upgrade --resource-group production` — upgrade cluster prod
- `kubectl delete deployment -n production` — delete em prod

## Validação

Todo task envelope INPUT deve incluir campo `tools` com:
- `allowed`: lista de tools permitidas
- `denied`: lista de tools bloqueadas

Exemplo:
```json
{
  "tools": {
    "allowed": ["github.read", "github.write", "filesystem.read", "filesystem.write"],
    "denied": ["production.deploy", "secrets.export", "mcp.servers.modify"]
  }
}
```

Exemplo para SRE L2:
```json
{
  "tools": {
    "allowed": ["filesystem.read", "filesystem.write", "github.read", "github.write", "terminal", "az", "kubectl", "helm", "terraform", "bicep", "datadog"],
    "denied": ["production.deploy", "secrets.export", "mcp.permissions.modify", "mcp.servers.modify"]
  }
}
```

Exemplo para Azure AKS L3:
```json
{
  "tools": {
    "allowed": ["filesystem.read", "filesystem.write", "github.read", "github.write", "terminal", "az", "kubectl", "helm"],
    "denied": ["production.deploy", "secrets.export", "mcp.*", "az deployment create --resource-group production", "terraform apply -auto-approve"]
  }
}
```