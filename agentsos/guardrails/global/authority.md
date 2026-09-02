# Guardrail Global — Authority

## Definição

Define o que cada nível de agente pode decidir autonomamente, baseando-se na matriz ✅⚠️🔐 de GOVERNANCE.md §01.

## Autorização por Nível

### L0 — Governance
- **Pode**: Definir hierarquia, guardrails, MCP permissions, criar/dissolver agents
- **Não pode**: Modificar próprios limites autonomamente — mudanças requerem revisão global

### L1 — CEO / Principal
- **Pode**: Delegar tarefas, aprovar proposals (skills/agents/rules), aprovar changes MEDIUM/HIGH risk
- **Não pode**: Modificar GOVERNANCE.md sem aprovação externa (🔐)

### L2 — Department Agent (Developer, QA, Security, Research, PM, Architect, SRE)
- **Pode**: Executar tarefas dentro de constraints, propor skills/agents, ativar skills LOW risk
- **Não pode**: Alterar hierarquia, guardrails, GOVERNANCE.md; activate MEDIUM/HIGH risk skills sem aprovação

### L3 — Specialist Agent
- **Pode**: Executar tarefas especializadas, ativar skills LOW risk, proposer skills/agents
- **Não pode**: Activate MEDIUM/HIGH risk skills sem aprovação L1; modificar hierarquia ou guardrails

### L4 — Subagent
- **Pode**: Executar tarefas específicas designadas por L3, retornar resultados
- **Não pode**: Propor mudanças no sistema; activation requires L3 authorization

### L5 — Tool / MCP
- **Pode**: Executar comandos autorizados dentro de scope
- **Não pode**: Qualquer decisão de governança; operam dentro de constraints pré-definidas

## Matriz de Autorização — Novos Agentes L2/L3

### L2 — Department Agents (Específicos)

| Ação | PM | Arquiteto | Dev | QA | SRE | Researcher |
|------|-----|-----------|-----|-----|-----|------------|
| Criar Brief/PRD | ✅ | ⚠️ | ❌ | ❌ | ❌ | ⚠️ |
| Aprovar Tech Spec | ⚠️ | ✅ | ⚠️ | ❌ | ⚠️ | ❌ |
| Escrever código / implementar | ❌ | ❌ | ✅ | ⚠️ | ❌ | ❌ |
| Criar test plan / QA gate | ❌ | ❌ | ⚠️ | ✅ | ⚠️ | ❌ |
| Provisionar infra Azure | ❌ | ⚠️ | ❌ | ❌ | ✅ | ❌ |
| Aprovar pipeline prod | ❌ | ⚠️ | ❌ | ❌ | ⚠️ | ❌ |
| Criar monitor Datadog | ❌ | ❌ | ❌ | ⚠️ | ✅ | ❌ |
| Definir SLO/SLI | ❌ | ⚠️ | ❌ | ✅ | ✅ | ❌ |
| Ativar skill LOW risk | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Propor skill/agent | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ativar skill MEDIUM/HIGH | ⚠️ (L1) | ⚠️ (L1) | ⚠️ (L1) | ⚠️ (L1) | ⚠️ (L1) | ⚠️ (L1) |

### L3 — Azure Specialists

| Ação | Azure DevOps | Azure Cloud | Azure AKS | Datadog |
|------|-------------|-------------|-----------|---------|
| Criar/atualizar pipeline YAML | ✅ | ❌ | ❌ | ❌ |
| Gerir repos/boards | ✅ | ❌ | ❌ | ❌ |
| Provisionar recursos Azure (non-prod) | ❌ | ✅ | ❌ | ❌ |
| Provisionar recursos Azure (prod) | ❌ | ⚠️ (L2/L1) | ❌ | ❌ |
| Criar/atualizar cluster AKS (non-prod) | ❌ | ❌ | ✅ | ❌ |
| Upgrade cluster AKS (prod) | ❌ | ❌ | 🔐 (L1/L2) | ❌ |
| Rollout workloads (rolling/canary) | ❌ | ❌ | ✅ | ❌ |
| Criar monitor/alert Datadog | ❌ | ❌ | ❌ | ✅ |
| Configurar integração Azure/AKS | ❌ | ❌ | ❌ | ✅ |
| Definir SLO/SLI | ❌ | ❌ | ⚠️ | ✅ |
| Ativar skill LOW risk | ✅ | ✅ | ✅ | ✅ |
| Propor skill/agent | ✅ | ✅ | ✅ | ✅ |
| Ativar skill MEDIUM/HIGH | ⚠️ (L2) | ⚠️ (L2) | ⚠️ (L2) | ⚠️ (L2) |

## Matriz de Referência

Consultar sempre `GOVERNANCE.md §01` (Matriz de Autorização ✅⚠️🔐) para definições completas por ação e nível.

## Aplicação Prática

Antes de qualquer ação, o agente deve:

1. Verificar sua nível atual (L1, L2, L3 ou L4)
2. Consultar a ação desejada na matriz
3. Confirmar que ✅ autorização é suficiente ou ⚠️ propõe ao nível superior
4. Se 🔐, aguardar aprovação humana/CEO
5. Se ❌, não executar — buscar alternativa dentro do scope autorizado

## Exemplos de Uso da Matriz

### Exemplo: SRE L2 quer provisionar AKS cluster em produção
1. Nível: L2 (SRE)
2. Ação: "Provisionar recursos Azure (prod)" → Matriz: ⚠️ (requer L1/L2 approval)
3. Como SRE é L2, precisa de aprovação L1 (CEO) → Criar proposal em `proposals/agents/`
4. CEO aprova → SRE delega para L3 azure-cloud + azure-aks

### Exemplo: Azure AKS L3 quer fazer upgrade de cluster em produção
1. Nível: L3 (Azure AKS)
2. Ação: "Upgrade cluster AKS (prod)" → Matriz: 🔐 (requer L1/L2)
3. Precisa de aprovação L2 SRE + L1 CEO → Proposal HIGH risk
4. Após aprovação, executa com supervisão

### Exemplo: Datadog L3 quer criar monitor crítico
1. Nível: L3 (Datadog)
2. Ação: "Criar monitor/alert Datadog" → Matriz: ✅
4. Pode executar diretamente (LOW/MEDIUM risk)
5. Reporta no result-envelope