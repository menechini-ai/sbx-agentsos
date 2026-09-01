# MCP Server Configuration

## Estrutura

```
mcp/
├── servers/
│   ├── github/
│   │   ├── config.json
│   │   └── README.md
│   ├── filesystem/
│   │   ├── config.json
│   │   └── README.md
│   ├── database/
│   │   ├── config.json
│   │   └── README.md
│   └── http-client/
│       ├── config.json
│       └── README.md
└── policies/
    └── mcp-policy.md
```

## Configuração de Servidor

Cada servidor MCP deve ter um `config.json`:

```json
{
  "name": "github",
  "version": "1.0.0",
  "description": "GitHub integration para leitura/escrita de repositórios",
  "tools": [
    {
      "name": "github.read",
      "description": "Ler issues, PRs, código, commits",
      "allowed_levels": ["L0", "L1", "L2", "L3"],
      "denied_operations": ["production.deploy", "secrets.export"]
    },
    {
      "name": "github.write",
      "description": "Criar/modificar issues, PRs, branches, commits",
      "allowed_levels": ["L0", "L1", "L2", "L3"],
      "denied_operations": ["production.deploy", "secrets.export", "force_push"]
    }
  ]
}
```

## Política de Uso

- MCP servers devem ser configurados em `mcp/servers/<server-name>/config.json`
- Tools devem respeitar a matriz de autorização de GOVERNANCE.md §01
- Tools devem respeitar o scope definido em `guardrails/global/scope.md`
- Modificações em MCP permissions requerem aprovação L1/L0 (HIGH risk)

## Integração com GOVERNANCE.md

- Baseado em GOVERNANCE.md §01 (Matriz de Autorização)
- Baseado em guardrails/global/tools.md (Tool Usage)
- Baseado em guardrails/global/change-risk-levels.md (MCP permissions = HIGH risk)