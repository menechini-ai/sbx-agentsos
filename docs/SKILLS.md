# Skills do Agent OS

## Conceito

Skills representam capacidades operacionais reutilizáveis que podem ser invocadas por qualquer agente. Cada skill é autocontida e segue o formato padrão definido em `skills/skill-name/SKILL.md`.

## Estrutura de uma Skill

```
skill-name/
├── SKILL.md          # Definição da skill (metadados, propósito, procedure, validação)
├── examples/         # Exemplos de uso
└── tests/            # Testes de conformidade
```

## Formato SKILL.md

Cada skill deve conter:

### Frontmatter YAML (Metadados)

```yaml
---
name: skill-name
version: 1.0.0
description: Breve descrição da skill
owner: agent-name
status: stable | proposal | deprecated

inputs:
  - input1
  - input2

outputs:
  - output1
  - output2

dependencies:
  - dependency1

tools:
  - tool1
  - tool2
---
```

### Corpo Markdown

1. **Purpose**: Propósito da skill
2. **When to Use**: Quando usar
3. **When NOT to Use**: Quando não usar
4. **Procedure**: Passos numerados
5. **Validation**: Como validar o resultado
6. **Failure Modes**: Modos de falha conhecidos
7. **Examples**: Exemplos de uso
8. **Known Limitations**: Limitações conhecidas
9. **Improvement Criteria**: Critérios para melhorias
10. **Changelog**: Histórico de versões

## Skills Globais

Disponíveis para todos os agentes em `skills/`:

| Skill | Descrição | Owner |
|-------|-----------|-------|
| research | Pesquisa e análise de informações | researcher |
| coding | Implementação de código, reviews, debugging, testes | developer |
| documentation | Escrita e manutenção de documentação | documentation |
| session-handoff | Handoff entre sessões/agentes | ceo |

## Skills Específicas

Disponíveis somente para determinado agente em `agents/*/skills/`:

```
agents/
└── developer/
    └── skills/
        ├── code-review/
        ├── debugging/
        └── architecture/
```

## Regra de Reuso

Uma skill deve existir no nível mais baixo possível que ainda permita sua reutilização:

1. Se usada por um único agente → `agents/<agent>/skills/`
2. Se usada por vários agentes → `skills/`

## Descoberta de Skills

Antes de propor uma nova skill, verificar:

```
Nova necessidade
       ↓
Existe Skill?
       │
   ┌───┴───┐
   │       │
  SIM     NÃO
   │       │
   ▼       ▼
usar   procurar
        ┌───────┐
        │memory │
        │github │
        │skills │
        │agents │
        └───────┘
            │
            ▼
      reutilizar?
       │       │
      SIM     NÃO
       │       │
       ▼       ▼
      usar    propor
```

## Promoção de Skill

Uma skill é proposta através de `proposals/skills/` após o pipeline de promoção Memory→Skill, quando:

- Pattern detectado em 3+ ocorrências
- Resultado comprovado
- Procedimento generalizável
- Risk level LOW (auto) ou MEDIUM (com aprovação)