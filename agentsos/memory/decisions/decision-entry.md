# Decision Entry

## Formato Padrão

```
decision_id: DEC-2026-0001
date: 2026-09-01
agent: ceo
status: accepted

context:
  - "Necessidade de adicionar autenticação ao sistema"
  - "JWT escolhido por simplicidade e suporte a refresh tokens"

decision:
  - "Adotar JWT como mecanismo de autenticação"
  - "Refresh token com expiração de 7 dias"
  - "Implementar rotacao de refresh token a cada renovacao"

consequences:
  - "Users precisam re-autenticar a cada 15 minutos"
  - "Refresh token armazenado em banco de dados"

rejected_alternatives:
  - "OAuth 2.0: muito complexo para o escopo atual"
  - "Session-based: requer armazenamento em memória"
```

## Uso

- Decisões são registradas em `memory/decisions/` quando:
  - Uma decisão arquitetural importante é tomada
  - A decisão tem consequências de longo prazo
  - A decisão deve ser consultada por outros agents futuramente

## Validação

- Cada decision deve ter um `decision_id` único
- Deve ter `date` e `agent` para accountability
- Deve ter `status` (accepted, rejected, superseded)
- Deve ter `context`, `decision`, `consequences`, `rejected_alternatives`