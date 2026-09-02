# Portable Context — Export/Import

> **Purpose**: Formato portável para transferir contexto entre Web (Gemini/ChatGPT) e IDE (Claude/Codex/OpenCode), preservando decisões de produto e técnica.

## Memory System

O sistema de memória do Agent OS é composto por:

```
agentsos/memory/
├── knowledge/                    # Skill-kwonledge (Obsidian-style KB)
│   └── examples/knowledge/       # Notas organizadas por categoria
│       ├── IaC/                  # Infrastructure as Code
│       ├── DevOps/               # Kubernetes, ArgoCD
│       ├── AI/                   # LangChain, DeepAgents
│       ├── SRE/                  # Agent OS, SRE patterns
│       │   └── agent-os/         # Arquitetura, governança
│       └── patterns/             # Cross-category patterns
├── sessions/                     # Logs de sessão (flat, por data)
│   └── YYYY-MM-DD-agent.md
├── candidates/                   # Learning candidates
│   └── {slug}.md
└── portable-context.md           # Este arquivo
```

## Format Overview

Portable Context é um Markdown estruturado que encapsula:
1. **Brief** — Product decisions
2. **PRD** — Feature requirements
3. **Tech Spec** — Technical decisions
4. **ADRs** — Architecture decisions
5. **Current Sprint** — What's in progress
6. **Key Learnings** — Important past decisions

## Export Format

```markdown
# Portable Context — [Project Name]

> Generated: YYYY-MM-DD | Sprint: [Number] | Source: Agent OS

## 1. Project Overview

**Name**: [Project Name]
**Status**: [Active | Paused | Completed]
**Tech Stack**: [Node.js + PostgreSQL + AKS + Datadog]
**Last Updated**: YYYY-MM-DD

## 2. Brief Summary

**Objective**: [1-2 sentences]
**Key Stakeholders**: [Names/Roles]
**Constraints**: [Timeline, Budget, Tech]
**Success Criteria**: [3-5 metrics]

## 3. PRD Summary

**Features (MoSCoW)**:
- MUST: [Feature 1], [Feature 2]
- SHOULD: [Feature 3]
- COULD: [Feature 4]

**User Stories Count**: [N]
**Total Points**: [N]

## 4. Tech Spec Summary

**Architecture**: [High-level diagram]
**Key Technologies**: [List]
**Data Model**: [Core entities]
**API Endpoints**: [Main endpoints]
**Infrastructure**: [Azure resources]

## 5. Architecture Decisions

| ADR | Decision | Status | Date |
|-----|----------|--------|------|
| ADR-001 | [Decision] | Accepted | YYYY-MM-DD |
| ADR-002 | [Decision] | Accepted | YYYY-MM-DD |

## 6. Current Sprint

**Sprint Goal**: [1 sentence]
**Committed Stories**:
- [Story 1] — [Points] — [Owner]
- [Story 2] — [Points] — [Owner]

**Velocity**: [N] points/sprint

## 7. Key Learnings

- [Learning 1]: [Context → Decision → Outcome]
- [Learning 2]: [Context → Decision → Outcome]

## 8. Open Questions

| Question | Owner | Due Date |
|----------|-------|----------|
| | | |

## 9. Handoff Notes

**Last Agent**: [Agent Name]
**Next Steps**: [What to do next]
**Blocked By**: [Dependencies]
```

## Import Instructions

### From Web to IDE

1. **Export**: Use `agentos export --format portable` (futuro CLI) ou copie o conteúdo acima
2. **Import**: Cole no início da conversa do IDE como contexto
3. **Validar**: IDE deve reconhecer a estrutura e fazer referência

### From IDE to Web

1. **Export**: `agentos export --format portable` (futuro CLI) ou manual
2. **Import**: Cole no Gemini/ChatGPT como sistema de contexto
3. **Usar**: Referencie seções específicas na conversa

## CLI Commands (Future)

```bash
# Export portable context
agentos export --format portable --output context.md

# Import portable context
agentos import --file context.md

# Validate portable context
agentos validate --file context.md
```

## Integration with Web Bundles

Portable Context pode ser empacotado como:
- **Gemini System Prompt**: Context + Instructions
- **ChatGPT Custom GPT**: Knowledge Base + Instructions
- **Claude Project Knowledge**: Context + Documents

## Validation Rules

- [ ] Brief tem objective mensurável
- [ ] PRD tem features com acceptance criteria
- [ ] Tech Spec tem architecture diagram
- [ ] ADRs têm status (Accepted/Rejected/Superseded)
- [ ] Sprint tem goal e committed stories
- [ ] Learnings têm contexto + decisão + resultado
