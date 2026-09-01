# Promoção: Skill → Rule

## Quando uma Skill pode virar Rule

Uma Skill pode ser promovida para Rule quando:

- **impacto sistêmico** identificado — o problema afeta múltiplos domínios ou tasks
- **padrão de falha repetido** — não é um incidente isolado
- **análise de consequências** — entender o que acontece se o problema não for resolvido
- **necessidade de autoridade** — a regra precisa ter mais "peso" do que uma skill individual

## Fluxo de Promoção

```
Skill (skills/skill-name/SKILL.md)
    │
    ▼ (trigger: impact analysis)
Rule Candidate
    │
    ▼ (impact analysis + approval)
Governance Rule
    │
    ▼ (AGENTS.md update)
```

## Critérios de Promoção

1. **Impacto Identificado**: O problema afeta 4+ tasks no mesmo domínio ou 2+ domínios diferentes
2. **Falha Repetitiva**: Padrão de erro observado mais de uma vez, não é incidente isolado
3. **Consequências Compreendidas**: O que acontece se o problema persistir é entendido e documentado
4. **Autoridade Necessária**: A regra precisa ter peso para sobrescrever decisões individuais

## Exemplo Prático

```
Skill: api-testing (ja promovida, usada em 4 tarefas)

Observação: "Agentes modificaram dependências sem declarar"

RULE CANDIDATE:
"Agents MUST NOT add dependencies
without declaring the dependency change."

Fluxo:
1. Impact analysis: 3 tasks affected; dependency changes not declared
2. Approval: L1 CEO review → approved com escrutínio
3. Result: Governance rule added a AGENTS.md
   → "Agents MUST NOT add dependencies
       without declaring the dependency change."
   → Commit: feat(rule): add dependency declaration rule
```

## Integração com GOVERNANCE.md

- Rules vivem em `AGENTS.md` (global ou de departamento) após aprovação
- O pipeline é: Skill → Rule Candidate → Impact Analysis → Approval → AGENTS.md update
- Risk level MEDIUM/HIGH — requires L1 CEO approval before AGENTS.md modification
- A regra deve ser versionada no Git com commits semânticos: `fix(rule): add dependency declaration rule`