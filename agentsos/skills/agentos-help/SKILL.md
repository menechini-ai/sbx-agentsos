# SKILL.md - agentos-help

## Metadados

- **Name**: agentos-help
- **Version**: 1.0.0
- **Description**: Guia o usuário sobre próximo passo e opções disponíveis no Agent OS.
- **Owner**: ceo
- **Status**: stable

## Inputs

- `current_state` — Estado atual do projeto/sprint/tarefa
- `user_question` — Pergunta do usuário sobre workflow

## Outputs

- `help_response` — Resposta com próximos passos e opções

## Dependencies

- None (transversal)

## Tools

- `filesystem.read` — Ler estado do projeto
- `terminal` — Comandos de status

## Purpose

Responder "What's next?" e "What's optional?" — guiar usuário no Agent OS sem overwhelm.

## When to Use

- Usuário pergunta "o que fazer agora?"
- Usuário pede `agentos-help`
- Após completar uma fase do loop

## When NOT to Use

- Usuário já sabe o que fazer
- Durante implementation (interrupts são custosos)

## Procedure

1. **Detect State**: Identificar fase atual do delivery loop (Clarify/Plan/Build/Verify/Learn).
2. **Detect Context**: Se é Sprint, tarefa, ou setup inicial.
3. **Suggest Next Step**: Baseado no state, sugerir próxima ação.
4. **Suggest Optional**: Items opcionais que podem melhorar resultado.
5. **Provide Commands**: Listar comandos úteis (`agentos-build`, `agentos-help`, etc.)

## Response Format

```markdown
## Current State: [Fase]

### Next Step (Recommended)
- [Ação concreta com comando/skill]

### Optional (Improve Quality)
- [Ação opcional]

### Quick Reference
- `agentos-build` — Implementar story
- `agentos-help` — Este help
- `agentos-retrospective` — Fim de sprint
```

## Validation

- Verificar se suggested next step é válido para o state
- Confirmar que commands existem

## Failure Modes

- **Wrong suggestion**: Sugere ação irrelevante; mitigação: state detection robust
- **Overwhelming**: Muitas opções; mitigação: máximo 3 suggestions

## Examples

### Exemplo 1: Help após sprint planning

```
Input: current_state="sprint 5 started, 3 stories committed"
Output: help_response={next: "Start US-001: Create branch feature/US-001-payment", optional: "Run dev-story to break into tasks"}
```

### Exemplo 2: Help após code implementation

```
Input: current_state="US-001 code complete, tests passing"
Output: help_response={next: "Create PR and run review skill", optional: "Run qa-gate for pre-merge validation"}
```

## Known Limitations

- State detection pode estar incorreto
- Help é genérico — context específico pode ser necessário

## Improvement Criteria

- **Nova skill**: When help consistently gives wrong suggestions
- **Promoção para rule**: When agentos-help obrigatório para novos usuários

## Changelog

- **1.0.0**: Versão inicial