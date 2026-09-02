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
- **Pipeline YAML (non-prod)**: Criação/atualização de pipelines em branches feature
- **Monitor Datadog (non-prod)**: Criação/atualização de monitors em ambiente de staging
- **IaC templates (non-prod)**: Criação/atualização de Bicep/Terraform para ambientes non-prod

**Ação**: L2/L3 pode executar diretamente; commit automático após validação de testes

### MEDIUM Risk — Revisão do Agent Superior

Requer aprovação do L1 CEO ou L2 Department Agent antes da execução:

- **Dependências**: Adição/remoção de dependências (ex: `requirements.txt`, `package.json`)
- **Configuração**: Alterações em arquivos de config (exceto secrets)
- **Skills**: Criação/ativação de novas skills (após pattern detection)
- **Workflows**: Modificação de workflows existentes
- **Pipeline YAML (prod)**: Criação/atualização de pipelines que deployam para produção
- **Monitor Datadog (prod)**: Criação/atualização de monitors críticos em produção
- **IaC templates (prod)**: Criação/atualização de Bicep/Terraform para produção (com plan aprovado)
- **Cluster AKS (non-prod)**: Criação/atualização de clusters non-prod
- **Node pool changes**: Adição/remoção/modificação de node pools non-prod
- **Rollout strategy changes**: Mudança de estratégia de rollout (rolling→canary)

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
- **Cluster AKS (prod)**: Criação/upgrade/delete de clusters de produção
- **Resource Group/Subscription (prod)**: Provisionamento/modificação de recursos em produção
- **Network changes (prod)**: Mudanças em VNet, Subnet, NSG, Firewall em produção
- **Datadog integration (prod)**: Configuração/modificação de integrações em produção
- **SLO/SLI changes (prod)**: Alteração de targets de SLO em produção
- **Secrets/Keys**: Qualquer operação envolvendo secrets, keys, certificates

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
| Pipeline YAML (non-prod) | ✅ L3 | ❌ | ❌ |
| Pipeline YAML (prod) | ❌ | ⚠️ L1 review | ❌ |
| Monitor Datadog (non-prod) | ✅ L3 | ❌ | ❌ |
| Monitor Datadog (prod, crítico) | ❌ | ⚠️ L1 review | ❌ |
| IaC templates (non-prod) | ✅ L3 | ❌ | ❌ |
| IaC templates (prod, com plan) | ❌ | ⚠️ L1 review | ❌ |
| Cluster AKS (non-prod) | ✅ L3 | ❌ | ❌ |
| Cluster AKS (prod) | ❌ | ❌ | 🔐 L1 + humano |
| Node pool changes (non-prod) | ✅ L3 | ❌ | ❌ |
| Node pool changes (prod) | ❌ | ⚠️ L1 review | ❌ |
| Rollout strategy | ✅ L3 | ⚠️ L1 review | ❌ |
| Upgrade AKS version (prod) | ❌ | ❌ | 🔐 L1 + humano |
| Network (VNet/Subnet/NSG) prod | ❌ | ❌ | 🔐 L1 + humano |
| Datadog integration prod | ❌ | ⚠️ L1 review | ❌ |
| SLO/SLI target changes prod | ❌ | ⚠️ L1 review | ❌ |
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

Exemplo para pipeline YAML prod:
```json
{
  "risk_level": "MEDIUM",
  "requires_approval": "L1 CEO"
}
```

Exemplo para cluster AKS prod:
```json
{
  "risk_level": "HIGH",
  "requires_approval": "L1 CEO + humano"
}
```

## Integração com GOVERNANCE.md

- Baseado em GOVERNANCE.md §01 (Matriz de Autorização ✅⚠️🔐)
- Baseado em GOVERNANCE.md §02.4 (Pipeline de Promoção Controlada)
- Alinhado com CLAW-HCG: LOW → automático, MEDIUM → revisão superior, HIGH → aprovação CEO/humano