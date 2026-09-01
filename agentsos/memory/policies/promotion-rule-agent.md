# Promoção: Rule → Agent

## Quando uma Rule pode gerar um Novo Agent

Um novo Agent pode ser proposto quando:

- **20+ tarefas** no mesmo domínio
- **mesmas ferramentas** usadas consistentemente
- **mesmo tipo de decisão** tomado repetidamente
- **alto volume** de tasks no domínio

## Fluxo de Promoção

```
Rule (em AGENTS.md)
    │
    ▼ (trigger: evidence thresholds)
Candidate Agent
    │
    ▼ (review + justification)
Proposal → CEO/Principal → GIT COMMIT
```

## Critérios de Proposta

1. **Volume de Tarefas**: 20+ tasks no mesmo domínio indicam necessidade de especialização
2. **Mesmas Ferramentas**: As mesmas skills e tools são usadas em maioria das tasks
3. **Mesmo Tipo de Decisão**: As decisões tomadas seguem padrão consistente
4. **Sobrecarga do Agent Existente**: O agent atual (ex: Developer) está overloaded e não consegue cobrir o domínio

## Exemplo Prático

```
Observação: "17 tasks related to database optimization; existing developer agent overloaded"

PROPOSAL:
type: new_agent
name: database-specialist
reason:
  - "17 tasks related to database optimization"
  - "Existing developer agent overloaded"
responsibilities:
  - query optimization
  - schema review
  - migration analysis
required_skills:
  - sql
  - database-performance
required_tools:
  - database

Fluxo:
1. Proposal criada em proposals/agents/
2. Review por L1 CEO/Principal
3. Justificativa: 17/20 tasks são DB-related; Developer overloaded
4. Approval: CEO approves → GIT COMMIT
   → feat(agent): add database specialist
5. New agent criado com AGENTS.md próprio
```

## Integração com GOVERNANCE.md

- Agent proposals seguem matriz ✅⚠️🔐: L1 CEO aprova; L0 Governance não modificada diretamente
- O proposal deve incluir: name, responsibilities, required_skills, required_tools, justification (evidência estatística)
- Após aprovação, novo agent criado em `agents/` com seu own `AGENTS.md`
- O novo agent inicia em L3 (Specialist) e pode promover para L2 (Department) se assumir responsabilidades de departamento inteiro
- Versionamento no Git: `feat(agent): add database specialist`