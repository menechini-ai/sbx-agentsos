# MCP Policies

## Princípio

MCP (Model Context Protocol) é a camada de ferramentas externas. Ela deve respeitar:

1. **Hierarquia de autoridade**: Tools só operam dentro do scope do nível do agente
2. **Command hardening**: Certos comandos são bloqueados (pip install, rm -rf, etc.)
3. **Gated access**: Ferramentas de risco maior requerem aprovação de nível superior

## Política de Permissões

### Permissões por Nível

| Nível | github.read | github.write | filesystem.read | filesystem.write | terminal | database |
|-------|-------------|--------------|-----------------|------------------|----------|----------|
| L0    | ✅          | ✅           | ✅              | ✅               | ✅       | ✅       |
| L1    | ✅          | ✅           | ✅              | ✅               | ✅       | ✅       |
| L2    | ✅          | ⚠️           | ✅              | ⚠️               | ⚠️       | ⚠️       |
| L3    | ✅          | ⚠️           | ✅              | ⚠️               | ⚠️       | ❌       |
| L4    | ❌          | ❌           | ⚠️              | ⚠️               | ⚠️       | ❌       |

**Notação**:
- ✅ = permitido
- ⚠️ = requer aprovação do nível superior
- ❌ = bloqueado

## Política de Modificação de MCP

- **Modificar configuração de servidores**: HIGH risk → aprovação L1/L0
- **Adicionar novo servidor**: HIGH risk → aprovação L1/L0 + GIT COMMIT
- **Modificar permissões de tools**: HIGH risk → aprovação L1/L0 + GIT COMMIT
- **Remover servidor**: HIGH risk → aprovação L1/L0 + justificativa

## Command Hardening

Comandos bloqueados por razões de segurança:

**Bloqueados para L2+**:
- `pip install`, `npm install`, `yarn add` — adicionar dependências
- `rm -rf`, `rm -r` — remoção recursiva
- `chmod 777`, `chown` — mudança de permissões
- `curl | bash`, `wget | sh` — execução de scripts remotos

**Bloqueados para L1+**:
- Qualquer comando que modifique `GOVERNANCE.md`, `guardrails/`
- Qualquer comando de deploy direto
- Qualquer comando que acesse `secrets/`

## Integração com GOVERNANCE.md

- Baseado em GOVERNANCE.md §01 (Matriz de Autorização)
- Baseado em guardrails/global/change-risk-levels.md (MCP permissions = HIGH risk)
- Baseado em CLAW-HCG (Command hardening, Self-healing paradox)