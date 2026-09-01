# Guardrail Global — Change Risk Levels

## Definição

Define o que pode ser alterado automaticamente vs. requer aprovação, baseando-se no nível de risco.

## Níveis de Risco

### LOW Risk — Mudança Automática

Permitida sem revisão prévia (L2+, após validação):

- **Código**: Alterações em arquivos de código fonte dentro do scope autorizado
- **Testes**: Adição/modificação de testes
- **Documentação**: Atualização de docs, READMEs, comentários
- **Exemplos**: Adição de exemplos em skills

**Ação**: L2/L3 pode executar diretamente; commit automático após validação de testes

### MEDIUM Risk — Revisão do Agent Superior

Requer aprovação do L1 CEO ou L2 Department Agent antes da execução:

- **Dependências**: Adição/remoção de dependências (ex: `requirements.txt`, `package.json`)
- **Configuração**: Alterações em arquivos de config (exceto secrets)
- **Skills**: Criação/ativação de novas skills (após pattern detection)
- **Workflows**: Modificação de workflows existentes

**Ação**: 
1. Proposta criada em `proposals/`
2. Review por L1 CEO ou L2 Department Agent
3. Aprovação → execução + commit
4. Rejeição → feedback para proposer

### HIGH Risk — Aprovação CEO/Humano

Requer aprovação explícita do L1 CEO ou humano antes de qualquer execução:

- **GOVERNANCE.md**: Qualquer modificação nas políticas globais
- **AGENTS.md**: Modificações nos contratos de agentes
- **Guardrails**: Modificações nas regras de autoridade ou scope
- **MCP permissions**: Modificações nas permissões de ferramentas
- **Memória permanente**: Promoção de memory candidates para knowledge permanente (sem passar pelo pipeline)
- **Criação de agents**: Criação de novos agents ou modificação da hierarquia

**Ação**:
1. Proposta detalhada em `proposals/architecture/` ou `proposals/agents/`
2. Review completo por L1 CEO + validação humana quando aplicável
3. Aprovação → GIT COMMIT com escrutínio máximo + documentação da decisão em `memory/decisions/`
4. Rejeição → feedback detalhado + learning registrado

## Matriz de Aprovação

| Tipo de Mudança | LOW | MEDIUM | HIGH |
|-----------------|-----|--------|------|
| Código | ✅ L2+ | ❌ | ❌ |
| Testes | ✅ L2+ | ❌ | ❌ |
| Documentação | ✅ L2+ | ❌ | ❌ |
| Exemplos | ✅ L2+ | ❌ | ❌ |
| Dependências | ❌ | ⚠️ L1 review | ❌ |
| Configuração | ❌ | ⚠️ L1 review | ❌ |
| Skills | ❌ | ⚠️ L1 review | ❌ |
| Workflows | ❌ | ⚠️ L1 review | ❌ |
| GOVERNANCE.md | ❌ | ❌ | 🔐 L1 + humano |
| AGENTS.md | ❌ | ❌ | 🔐 L1 + humano |
| Guardrails | ❌ | ❌ | 🔐 L1 + humano |
| MCP permissions | ❌ | ❌ | 🔐 L1 + humano |
| Memória permanente | ❌ | ❌ | 🔐 L1 + humano |
| Criação de agents | ❌ | ❌ | 🔐 L1 + humano |

## Validação

Todo task envelope INPUT deve incluir campo `risk_level` indicando o nível de risco esperado da execução.

Exemplo:
```json
{
  "risk_level": "MEDIUM",
  "requires_approval": "L1 CEO"
}
```

## Integração com GOVERNANCE.md

- Baseado em GOVERNANCE.md §01 (Matriz de Autorização ✅⚠️🔐)
- Baseado em GOVERNANCE.md §02.4 (Pipeline de Promoção Controlada)
- Alinhado com CLAW-HCG: LOW → automático, MEDIUM → revisão superior, HIGH → aprovação CEO/humano