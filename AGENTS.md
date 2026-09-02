# AGENTS.md - Projeto Agent OS

## Identidade do Sistema

- **Nome**: Agent OS
- **Versão**: 1.0.0
- **Propósito**: Arquitetura modular de agentes de IA com governança formal, memória persistente e habilidades reutilizáveis.
- **Status**: Sistema ativo - Governança ativa (GOVERNANCE.md define limites e hierarquia)

## Regras Fundamentais

1. **Hierarquia de Autoridade**: Todos os agentes devem respeitar a hierarquia L0-L5 definida em GOVERNANCE.md
2. **Governança Primeiro**: Antes de propor qualquer mudança no sistema, o agente deve completar sua tarefa atual (EXECUTION-FIRST POLICY)
3. **Memória como Fonte de Verdade**: Informações persistentes devem ser armazenadas no knowledge base (skill-kwonledge, Obsidian-style), não em contexto de conversa
4. **Contratos Estruturados**: Todas as tarefas devem seguir o envelope INPUT/OUTPUT definido em contracts/
5. **Guardrails**: Cada agente deve operar dentro de seus limites definidos pela matriz de autorização GOVERNANCE.md §01

## Memória

- **Fonte de Verdade**: knowledge base (skill-kwonledge, wiki markdown + Obsidian-style frontmatter)
- **Consulta**: `→ consultar memory/knowledge/` (para decisões arquiteturais)
- **Aprendizados**: Promovidos através do pipeline Memory→Skill→Rule com gates de risco (LOW/MEDIUM/HIGH)
- **Handoff**: Utilizar skills de session-handoff para continuidade entre sessões

## Skills

- **Skills Globais**: Disponíveis em `skills/` para todos os agentes (research, coding, documentation, session-handoff)
- **Skills Específicas**: Disponíveis por agente em `agents/*/skills/`
- **Padrão SKILL.md**: Todos os skills devem seguir o formato em `skills/skill-name/SKILL.md`

## Handoff

- **Procedimento**: Utilizar skills de session-handoff para transferência entre sessões/agentes
- **Formato**: `handoff` contract com de, pending, artifacts, risks, instructions, expected
- **Recuperação**: `→ utilizar a skill de session-handoff` (para continuidade)

## Governança

- **Propostas de Mudança**: `→ proposals/` directory com review segundo risk level
- **Improvement Engine**: Observa patterns e propõe novas skills/agents/rules via `proposals/`
- **Git**: Todas as mudanças significativas devem ser commitadas com commits semânticos

## Consulta ao GOVERNANCE.md

Para dúvidas sobre hierarquia, limites ou políticas globais, consultar sempre `GOVERNANCE.md`.