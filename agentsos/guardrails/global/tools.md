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

## Command Hardening (CLAW-HCG Inspired)

Alguns comandos são bloqueados por padrão por razões de segurança (Self-Healing Paradox):

**Bloqueados para L2+**:
- `pip install`, `npm install` — adicionar dependências sem aprovação
- `rm -rf`, `rm -r` — remoção recursiva
- `chmod 777`, `chown` — mudança de permissões
- `curl | bash`, `wget | sh` — execução de scripts remotos

**Bloqueados para L1+**:
- Qualquer comando que modifique `GOVERNANCE.md`, `guardrails/`, `memory/ai-memory/wiki/`
- Qualquer comando de deploy direto (`git push production`, `npm publish`, etc.)

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