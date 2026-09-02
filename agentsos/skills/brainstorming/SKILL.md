# SKILL.md - brainstorming

## Metadados

- **Name**: brainstorming
- **Version**: 1.0.0
- **Description**: Facilita sessões de brainstorming estruturado para explorar ideias, riscos e oportunidades antes do planejamento.
- **Owner**: pm
- **Status**: stable

## Inputs

- `topic` — Tema ou problema a explorar
- `participants` — Lista de roles convidadas (PM, Arquiteto, Dev, QA, SRE)
- `context` — Contexto adicional (brief existente, constraints conhecidos)
- `timebox` — Tempo limite em minutos (default: 30)

## Outputs

- `brainstorm_report` — Relatório com ideias categorizadas, riscos identificados, next steps

## Dependencies

- `research` — Para validar ideias com dados externos

## Tools

- `filesystem.read` — Ler contexto prévio
- `filesystem.write` — Escrever relatório
- `terminal` — Timer para timebox

## Purpose

Gerar divergent thinking estruturado antes de convergir para Brief/PRD, capturando:
- Ideias de solução
- Riscos e unknowns
- Perguntas para research
- Decisões de arquitetura preliminares

## When to Use

- Início de qualquer tarefa Standard/Full (fase Clarify)
- Quando requirements são vagos ou ambíguos
- Antes de PRD writing para validar scope
- Quando equipe discorda sobre abordagem

## When NOT to Use

- Tarefas Quick (→ Build direto)
- Quando solution já está clara e validada
- Para decisões técnicas profundas (usar `tech-spec`)

## Procedure

1. **Setup (5 min)**: Definir topic, participants, timebox. Ler `context` se fornecido.
2. **Divergent (15 min)**: Cada participante escreve ideias independentemente (silent brainstorming). Categorizar: Solutions, Risks, Questions, Decisions.
3. **Convergent (10 min)**: Agrupar ideias similares. Votar nas top 3 por categoria (dot voting).
4. **Synthesize (5 min)**: Produzir `brainstorm_report` com:
   - Top solutions com pros/cons
   - Top risks com mitigações propostas
   - Open questions para `research` skill
   - Preliminary decisions para `adr-writing`
   - Next steps recomendados

## Validation

- Verificar se todas as categorias têm pelo menos 1 item
- Confirmar que top items têm owner definido para follow-up
- Cross-check com `memory/knowledge` — evitar re-discutir decisões já tomadas

## Failure Modes

- **Groupthink**: Maioria domina; mitigação: silent writing primeiro
- **Scope creep**: Discussão sai do topic; mitigação: timebox rigoroso + facilitador
- **No actionable output**: Ideias não viram next steps; mitigação: template de report exige next steps

## Examples

### Exemplo 1: Nova feature de pagamentos

```
Input: topic="Payment integration", participants=[PM, Arch, Dev, QA, SRE], timebox=30
Output: brainstorm_report contendo:
  - solutions: [Stripe, Adyen, custom], top: Stripe (pros: docs, cons: cost)
  - risks: [PCI compliance, vendor lockup], mitigation: use payment gateway
  - questions: [webhook retry logic?, refund flow?] → research skill
  - decisions: [use idempotency keys] → adr-writing
  - next steps: PM cria Brief, Arch faz tech-spec
```

## Known Limitations

- Requer facilitador neutro (PM ideal)
- Não substitui research técnico profundo
- Timebox pode ser insuficiente para tópicos complexos

## Improvement Criteria

- **Nova skill**: Quando pattern de brainstorming ineficaz detectado em 3+ sessões
- **Promoção para rule**: Quando formato de brainstorming se torna obrigatório

## Changelog

- **1.0.0**: Versão inicial