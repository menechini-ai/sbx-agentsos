# Promoção: Memory → Skill

## Quando uma memória pode virar Skill

Uma memória pode ser promovida para Skill quando:

- **mesmo conhecimento** repetido across multiple tasks
- **+ repetição** (mínimo 3 ocorrências detectadas)
- **+ resultado comprovado** — o padrão não é apenas ruído
- **+ procedimento generalizável** — não é um one-off, pode ser reaplicado

## Fluxo de Promoção

```
memory (wiki markdown + SQLite)
    │
    ▼ (trigger: pattern detection, min 3 occurrences)
Candidate (memory/candidates/)
    │
    ▼ (risk analysis + review by superior level)
    │
    ├──► LOW RISK      ► Skill (SKILL.md) — activation automática
    │                   │
    │                   ▼
    │               L3/L4 activation
    │
    ├──► MEDIUM RISK   ► Rule candidate → review → approval → AGENTS.md update
    │
    └──► HIGH RISK     ► Proposal → CEO/Principal review → GIT COMMIT
                       (com escrutínio máximo)
```

## Critérios de Risco

| Risco | Exemplos | Aprovação |
|-------|----------|-----------|
| LOW   | código, testes, documentação exemplos | Automática — L3/L4 activation |
| MEDIUM| dependências, configuração, skills | Revisão do Agent superior (L1 CEO) |
| HIGH  | AGENTS.md, GOVERNANCE.md, guardrails, MCP permissions, memória permanente, criação de agents | Aprovação CEO/humano; GIT COMMIT com escrutínio máximo |

## Exemplo Prático

```
TASK 1: "Como testar API?" → Skill research consultada
TASK 2: "Como testar API?" → Pattern detection: mesma pergunta
TASK 3: "Como testar API?" → Pattern detection: mesma pergunta
TASK 4: "Como testar API?" → Pattern detection: 4/4 tasks

O sistema detecta PATTERN DETECTED (4 ocorrências)

→ Promove para: skills/api-testing/SKILL.md (RISK LOW)
   — Procedure já definida, pode ser ativada por L3/L4
   — Activation: L3 Specialist Agent pode usar a partir de agora
```

## Regra de Promoção

Uma memória EPPHEMERAL (curto prazo) promove para Skill quando a mesma pergunta/necessidade aparece repetidamente, indicando:

1. O conhecimento é valioso o suficiente para ser generalizável
2. Um procedimento exists/reusable
3. O sistema pode se beneficiar de ter essa skill disponível imediatamente

## Integração com GOVERNANCE.md

- Risk levels seguem a matriz ✅⚠️🔐 da Seção 01
- Activation follows authority limits: L3 Specialist can activate LOW Risk skills; MEDIUM/HIGH requer revisão L1
- O pipeline não pula níveis — Memory → Candidate → Risk Analysis → Promotion → Skill