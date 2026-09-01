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

### L2 — Department Agent (Developer, QA, Security, Research)
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

## Matriz de Referência

Consultar sempre `GOVERNANCE.md §01` (Matriz de Autorização ✅⚠️🔐) para definições completas por ação e nível.

## Aplicação Prática

Antes de qualquer ação, o agente deve:

1. Verificar sua nível atual (L1, L2, L3 ou L4)
2. Consultar a ação desejada na matriz
3. Confirmar que ✅ autorização é suficiente ou ⚠️ propõe ao nível superior
4. Se 🔐, aguardar aprovação humana/CEO
5. Se ❌, não executar — buscar alternativa dentro do scope autorizado