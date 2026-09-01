# Boas Práticas para Individual Contributor no Agent OS

## Visão Geral

Como contribuidor individual trabalhando com o Agent OS, suas responsabilidades são focadas em:
- Executar tarefas dentro dos limites definidos
- Aprender com o sistema através do pipeline controlado
- Propor melhorias através dos canais adequados
- Manter a integridade da governança

Este documento complementa o `GOVERNANCE.md` e o `AGENTS.md`, focando no dia a dia de um contribuidor individual.

---

## 1. Regra de Ouro: Execução Primeiro

### A Regra
> **Agents MUST prioritize completing the assigned task before performing optimization work.**

### Na Prática
- Comece executando a tarefa imediatamente (`EXECUTION-FIRST POLICY`)
- Durante a execução, observe patterns e gaps
- Apenas após a conclusão (ou interrupção segura), entre no modo de aprendizado
- **Nunca** comece propondo skills/rules/agents antes de completar a tarefa

### Verificação
- [ ] Tarefa foi completada?
- [ ] Aprendizados foram registrados em `memory/learnings/`?
- [ ] Improvement proposals foram criados APENAS após a conclusão?

---

## 2. Conheça os Seus Limites (Matriz de Autorização)

### Verifique Antes de Agir
Antes de qualquer ação, consulte a matriz ✅⚠️🔐 no `GOVERNANCE.md §01`:

| Se seu nível é: | ✅ Pode fazer diretamente | ⚠️ Pode propor (requer revisão) | 🔐 Requer aprovação CEO/humano | ❌ Proibido |
|-----------------|---------------------------|--------------------------------|-------------------------------|-------------|
| **L1 - CEO/Principal** | Definir estratégia, aprovar proposals | Modificar guardrails/ hierarquia | Governança pura | - |
| **L2 - Dept Agent** (Developer/QA/Research) | Executar tarefas, code, tests | Propor skills, activation LOW | MEDIUM/HIGH risk needs L1 | Modificar governance |
| **L3 - Specialist** | Tarefas especializadas, ativar skills LOW | Propor skills (com review) | MEDIUM/HIGH needs L1 | - |
| **L4 - Subagent** | Executar tarefas designadas | - | - | - |
| **L5 - Tool/MCP** | Operações definidas | - | - | - |

### Ação Prática
```
Antes de executar:
1. Identifique seu nível atual
2. Verifique a ação na matriz
3. Se ❌, não execute — busque alternativa
4. Se ⚠️, prepare proposal e submeta
5. Se ✅, execute com confiança
6. Se 🔐, solicite aprovação ao CEO
```

---

## 3. Siga o Pipeline de Promoção Controlado

### O Pipeline
```
Wiki (ai-memory)
    │
    ▼ (pattern: min 3 ocorrências)
Candidate (memory/candidates/)
    │
    ▼ (risk analysis)
    ├──► LOW RISK      ► Skill activation (L3/L4)
    │                   │
    ├──► MEDIUM RISK   ► Rule candidate → Review → AGENTS.md update
    │
    └──► HIGH RISK     ► Proposal → CEO review → GIT COMMIT
```

### O Que Fazer

#### Como Skill Candidate (LOW risk)
1. Identifique o pattern em 3+ tasks
2. Crie entry em `memory/candidates/skills/`
3. Wait ou propõe automaticamente (risk LOW = pode auto-promover)
4. A skill fica disponível em `skills/skill-name/SKILL.md`

### Como Rule Candidate (MEDIUM risk)
1. Identifique impacto sistêmico ou falhas repetidas
2. Crie entry em `memory/candidates/rules/`
3. Submeta review ao L1 CEO
4. Aprovação → Rule added a AGENTS.md

### Como Agent Candidate (HIGH risk)
1. Necessita 20+ tasks no mesmo domínio
2. Justificativa: volume + mesma ferramenta + mesmo tipo de decisão
3. Proposta em `proposals/agents/` → CEO aprova → GIT COMMIT → Novo agent criado

### O Que NÃO Fazer
- ❌ **Não** promova memory diretamente para skill/rule/agent sem passar pelo pipeline
- ❌ **Não** crie skills/agents sem evidence estatística
- ❌ **Não** ignore os risk levels (LOW/MEDIUM/HIGH)

---

## 3. Use os Contratos INPUT/OUTPUT

### Por Que Usar Contratos
- Garante que todos sabem: quem pediu, para quem, missão, contexto, limites, skills autorizadas, expected output
- Evita comunicação por texto livre que leva a ambiguidades
- Cria cadeia verificável: INPUT → PROCESSAMENTO → VALIDAÇÃO → OUTPUT → HANDOFF

### Formato do Task Envelope (INPUT)

```json
{
  "task": {
    "id": "TASK-2026-0001",
    "sender": {"agent": "ceo", "level": 1},
    "receiver": {"agent": "developer", "level": 2},
    "objective": {"primary": "Implementar autenticação"},
    "constraints": ["Não alterar arquitetura global"],
    "resources": {
      "skills": ["authentication", "testing"],
      "tools": ["github", "filesystem"]
    },
    "memory": {"read": ["decisions/authentication.md"]},
    "expected_output": {"type": "implementation_report", "required": ["status", "changes", "tests", "risks"]}
  }
}
```

### Formato do Result Envelope (OUTPUT)

```json
{
  "result": {
    "task_id": "TASK-2026-0001",
    "status": "completed",
    "summary": ["Autenticação implementada"],
    "changes": {"files": ["src/auth/login.ts"]},
    "validation": {"tests": {"status": "passed", "total": 42}},
    "risks": ["JWT expiration config padrão"],
    "assumptions": ["API compatível"],
    "memory_candidates": [{"type": "learning", "description": "Refresh token 7 dias"}],
    "improvement_candidates": [{"type": "skill", "name": "auth-testing", "reason": "Padrão em 4 tarefas"}],
    "handoff": {"next_agent": "qa", "required": true}
  }
}
```

### Ação Prática
- [ ] Sempre use o envelope JSON em vez de mensagens de texto livre
- [ ] Verifique todos os campos obrigatórios antes de enviar
- [ ] Valide o output contra o expected_output especificado
- [ ] Popule memory_candidates e improvement_candidates se aplicável

---

## 4. Documente Seus Aprendizados

### O Onde
- `memory/learnings/` — para aprendizados episódicos (não promovidos automaticamente)
- `memory/candidates/` — para candidates awaiting review
- `proposals/` — para propostas aprovadas ou em review

### O Formato

#### Learning Entry
```markdown
# Learning Entry

```
learning_id: LEARN-2026-0001
task_id: TASK-2026-0001
agent: developer
date: 2026-09-01
type: ephemeral
status: ephemeral

content:
  - "Projeto utiliza refresh token de 7 dias"

context:
  task: "Implementar autenticação"
  repository: "project"

promotion_candidate:
  type: skill
  description: "Padrão de refresh token repetido em 4 tarefas"
  occurrences: 4
  confidence: 0.87
```
```

#### Candidate Entry
```markdown
# Candidate Entry

```
candidate_id: CAND-2026-0001
task_id: TASK-2026-0001
agent: developer
date: 2026-09-01
type: skill
status: awaiting_review

description:
  - "Projeto utiliza refresh token de 7 dias"

pattern_detection:
  occurrences: 4
  tasks:
    - TASK-2026-0001
    - TASK-2026-0002
    - TASK-2026-0003
    - TASK-2026-0004

confidence: 0.87

risk_level: LOW

review:
  required: true
  reviewer: ceo
  status: pending
```
```

### O Que Documentar
- [ ] Padrões repetidos observados durante as tasks
- [ ] Skills que poderiam resolver gaps recorrentes
- [ ] Rules necessárias para prevenir falhas
- [ ] Melhorias de workflow identificadas
- [ ] Conhecimento que deveria ser promovido para o ai-memory

---

## 4. Handoff Between Sessions

### Quando Fazer Handoff
- Ao encerrar uma sessão antes de completar todas as tarefas
- Ao transferir responsabilidade entre agents (developer → qa, qa → security)
- Ao finalizar o trabalho periodicamente
- Ao mudar de contexto para outra task

### O Que Incluir no Handoff Report

```json
{
  "from_agent": "developer",
  "from_level": 2,
  "task_id": "TASK-2026-0001",
  "completed": ["authentication implementation"],
  "pending": ["integration tests"],
  "artifacts": ["src/auth/", "tests/auth/"],
  "risks": ["token expiration configuration"],
  "instructions": ["Validate authentication flow"],
  "expected": ["test_report"],
  "handoff_id": "HANDOFF-2026-0001",
  "date": "2026-09-01"
}
```

### Ação Prática
- [ ] Sempre crie handoff report ao encerrar sessão
- [ ] Persista no ai-memory para recuperação futura
- [ ] Verifique se completed/pending estão accurados
- [ ] Liste todos os artifacts com paths corretos
- [ ] Documente riscos reais (não inventados)
- [ ] Dê instruções específicas ao próximo agente

---

## 5. Melhores Práticas de Git

### Commits Semânticos

Siga o padrão de commits semânticos definidos em `GOVERNANCE.md §02.10`:

```
feat(skill): add api testing skill
feat(agent): add database specialist
fix(guardrail): restrict dependency installation
docs(agent): improve developer instructions
refactor(memory): reorganize learning storage
```

### Branch Naming

```
feature/<descricao>     — novas funcionalidades
fix/<descricao>         — correções
refactor/<descricao>    — refatorações
docs/<descricao>        — documentação
proposal/<tipo>/<descricao>  — propostas (skill/agent/rule/architecture)
```

### Ação Prática
- [ ] Use commits semânticos em todas as alterações
- [ ] Nomeie branches seguindo o padrão
- [ ] Agrup commits relacionados em commits significativos
- [ ] Nunca faça force-push em branches compartilhados
- [ ] Crie proposals em `proposals/` para mudanças significativas

---

## 6. Evite o Self-Healing Paradox

### O Risco
O "Self-Healing Paradox" (CLAW-HCG) é o impulso do agente de "auto-corrigir" o ambiente de forma perigosa (ex: `pip install` sem aprovação, modificar configurações de produção).

### Como Evitar

| Em vez de fazer | Faça isto |
|-----------------|-----------|
| `pip install pacote` | Crie proposal `proposals/skills/` ou `proposals/agents/` |
| `rm -rf pasta` | Solicite aprovação L1/L0 via proposal |
| `chmod 777 arquivo` | Revise permissions via matriz ✅⚠️🔐 |
| `curl | bash` | Use tools autorizadas e Command Hardening |
| Modificar GOVERNANCE.md sozinho | Slope proposal → review → CEO approval |

### Verificação Rápida
- [ ] Esta mudança modifies governance, permissions, guardrails, hierarchy ou authority?
- [ ] Se sim, → proposal → review → approve → deploy
- [ ] Se não → pode executar dentro do scope L5/L4/L3

---

## 7. Padrão de Discovery de Novas Skills

### Antes de Propor uma Nova Skill

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

### Checklist de Verificação

1. [ ] Busque em `skills/` — já existe uma skill global?
2. [ ] Busque em `agents/*/skills/` — já existe skill específica?
3. [ ] Busque em `memory/learnings/` — o conhecimento está lá como learning?
4. [ ] Busque em `proposals/` — já existe proposal em andamento?
5. [ ] Se NENHUM acima: propoe nova skill

### Se Decidir Propor

1. Verifique risk level (LOW/MEDIUM/HIGH)
2. Crie proposal em `proposals/skills/`
3. Preencha: name, version, description, owner, status, inputs, outputs, dependencies, tools
4. Documente: when-to-use, when-NOT-to-use, procedure, validation, failure-modes, examples, limitations
5. Submeta para review conforme risk level

---

## 8. Ferramentas e Recursos

### Comandos Úteis

```bash
# Capturar sessão
python3 agentsos/scripts/capture-session.py --task_id TASK-2026-0001

# Promover candidate
python3 agentsos/scripts/promote-memory.py --candidate_id CAND-2026-0001 --promote-to skill

# Verificar fluxo de delegação
python3 agentsos/scripts/delegation-workflow.py --delegate --task TASK-2026-0001 --from_agent ceo --to_agent developer

# Status do git
git status
git log --oneline -5
```

### Recursos Rápidos

- `GOVERNANCE.md` — políticas completas (seções 01-02)
- `AGENTS.md` — contrato do seu agente
- `skills/*/SKILL.md` — skills disponíveis
- `memory/policies/` — pipelines de promoção
- `proposals/` — propostas em andamento
- `CONTRACTS.md` — formatos de envelope

---

## Checklist Diário

### Início de Dia
- [ ] Revise seu nível atual e matriz de autorização
- [ ] Verifique se há handoffs pendentes
- [ ] Consulte `ai-memory` para aprendizados relevantes

### Durante o Trabalho
- [ ] Use task envelopes (INPUT/OUTPUT JSON)
- [ ] Documente aprendizados em `memory/learnings/` ou candidates
- [ ] Siga EXECUTION-FIRST POLICY
- [ ] Observe patterns que possam indicar gaps

### Fim de Dia
- [ ] Criehando handoff report se houver tarefas pendentes
- [ ] Commitando com padrão semântico
- [ ] Verifique se não há violations de guardrails
- [ ] Considere se algum pattern merece proposal

### Semanal
- [ ] Revise proposals em andamento
- [ ] Atualize seu AGENTS.md se responsibilities mudaram
- [ ] Revise matriz de autorização para changes planejados

---

## Resumo Rápido (Cheat Sheet)

| Ação | Quando | Como |
|------|--------|------|
| Executar tarefa | Sempre | EXECUTION-FIRST POLICY |
| Consultar limites | Sempre | Matriz ✅⚠️🔐 de GOVERNANCE.md §01 |
| Promover skill | Pattern em 3+ tasks | Pipeline Memory→Skill→Rule→Agent |
| Propor skill | Discovery falhou | `proposals/skills/` com justificativa |
| Handoff session | Encerrar sessão | handoff report JSON + ai-memory |
| Commitar código | Sempre | Commits semânticos + branches feature/fix/refactor/docs/proposal |
| Evitar self-healing | Toda modificação de governance | proposal → review → approve → deploy |
| Discovery skill | Nova necessidade | Buscar em skills/ → memory/ → proposals/ |

---

## Conclusão

Como individual contributor no Agent OS, suas principais responsabilidades são:

1. **Executar tarefas** dentro dos limites da matriz de autorização
2. **Aprender** observando patterns e registrando em `memory/learnings/` ou candidates
3. **Propor** melhorias APENAS após completar tarefas, pelos canais adequados
4. **Respeitar** a governança (GOVERNANCE.md) e os contratos (INPUT/OUTPUT envelopes)
5. **Contribuir** para o crescimento do sistema skills/rules/agents através de proposals bem fundamentadas

Lembre-se: **O sistema foi criado para que agentes possam executar tarefas com segurança e continuar trabalhos anteriores sem depender do contexto da conversa original.** Seu papel é seguir os procedimentos, documentar aprendizados e propor melhorias — nunca pular etapas ou modificar governança autonomamente.

---

*Documento vivente — atualize conforme novas descobertas e patterns forem surgindo no projeto Agent OS.*