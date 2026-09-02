# Governança de Agentes

Documento constitucional do sistema de agentes.  
Define limites, hierarquia, autoridade e regras globais.

Camadas inferiores **NÃO** podem sobrescrever regras de camadas superiores.

---

## 00. Estrutura Final de Pastas

### Mapa do Project

```
project/
│
├── GOVERNANCE.md          # (ESTE ARQUIVO) — políticas globais + hierarquia + matriz de autoridade
├── AGENTS.md              # (FUTURO) — contrato global do sistema
├── README.md
│
├── agents/
│   │
│   ├── ceo/
│   │   ├── AGENTS.md
│   │   ├── skills/
│   │   └── prompts/
│   │
│   ├── departments/
│   │   │
│   │   ├── developer/
│   │   │   ├── AGENTS.md
│   │   │   ├── skills/
│   │   │   └── agents/          # L3 Specialist + L4 Subagent
│   │   │
│   │   ├── researcher/
│   │   ├── qa/
│   │   └── security/
│   │
│   └── subagents/         # L4 Subagent
│
├── skills/
│   ├── skill-name/
│   │   ├── SKILL.md       # Padrão: purpose + when-to-use + procedure + validation + examples + limitations
│   │   ├── examples/
│   │   └── tests/
│   │
│   └── ...
│
├── memory/
│   ├── knowledge/       # Base de conhecimento (Obsidian-style, skill-kwonledge)
│   │   └── examples/knowledge/  # Notas por categoria (IaC, DevOps, AI, SRE)
│   ├── sessions/        # Logs de sessão (flat, por data)
│   ├── candidates/      # Learning candidates aguardando review
│   └── policies/        # Políticas de promoção Memory→Skill→Rule→Agent
│
├── contracts/
│   ├── input/             # task-envelope.md (sender, receiver, objective, constraints, resources, expected_output, deadline)
│   └── output/            # result-envelope.md (status, summary, changes, validation, risks, assumptions, memory_candidates, improvement_candidates, handoff)
│
├── guardrails/
│   ├── global/
│   ├── ceo/
│   ├── agents/
│   └── subagents/
│
├── mcp/
│   ├── servers/
│   └── policies/
│
├── workflows/
│   ├── delegation/
│   ├── handoff/
│   ├── review/
│   └── improvement/
│
├── templates/
│   ├── agent/
│   ├── skill/
│   ├── task/
│   ├── handoff/
│   ├── memory/
│   └── improvement/
│
├── proposals/
│   ├── skills/
│   ├── agents/
│   ├── rules/
│   └── architecture/
│
├── tests/
│   ├── agents/
│   ├── skills/
│   ├── contracts/
│   └── guardrails/
│
└── .git/
```

### Princípio de Separação

```
GOVERNANCE.md
    ↓
"QUEM SOU E QUAIS SÃO MEUS LIMITES"

AGENTS.md
    ↓
"QUEM SOU E COMO DEVO ME COMPORTAR"

SKILL.md
    ↓
"COMO EXECUTO UMA TAREFA"

knowledge/
     ↓
"O QUE EU APRENDI"

work/
     ↓
"O QUE ESTOU PRODUZINDO"

docs/
     ↓
"COMO O SISTEMA FUNCIONA"
```

### Regra da Fonte de Verdade Única

Não duplicar lógica de memória. O knowledge base (skill-kwonledge) já implementa:
- Notas Obsidian-style com YAML frontmatter (fonte de verdade)
- Organização por categorias (IaC, DevOps, AI, SRE)
- Deduplication automática via scripts
- Session logs em `memory/sessions/` (flat, por data)

**Proibido criar sistema paralelo:**
```
memory/
├── lessons/
├── decisions/
├── sessions/
└── handoffs/
```

Essas responsabilidades são do knowledge base e memory/sessions/.

### Referências aos Arquivos Existentes

| Arquivo | Conteúdo | Relevância |
|---------|----------|------------|
| `agentsos/001.md` | Visão geral, filosofia, 25 fases, integração knowledge base | Estrutura de pastos + filosofia |
| `agentsos/002.md` | Knowledge manager, models, store, retrieval | Políticas de memória (seção 02) |
| `agentsos/003.md` | CEO coordination, AGENTS.md templates, skills catalogação | Templates de agents/skills |
| `agentsos/004.md` | Guardrails, contracts, hierarquia, delegation flow | Guardrails + matriz de autorização |
| `docs/AGENT-ARCHITECTURE.md` | Princípios resumidos (26 seções) | Consolidação de ideias gerais |

---

## 01. Hierarquia e Autoridade

### Definição dos Níveis

```
L0 — GOVERNANCE
     ↓
L1 — CEO / Principal
     ↓
L2 — Department Agent (Developer, QA, Security, Research, etc.)
     ↓
L3 — Specialist Agent (ex: database-specialist, auth-specialist, code-reviewer)
     ↓
     └── Sub-cell Spawning: L3 pode spawn L4 Subagent quando complexity threshold exceeded
     └── Stem Cell Differentiation: L2 pode diferenciar sub-agentes dependendo da tarefa
     ↓
L4 — Subagent (executando tarefas específicas dentro de um agent L2/L3)
     ↓
L5 — Tool / MCP (github, filesystem, database, http client, etc.)
```

### Regra Fundamental

> **Nível inferior NÃO pode sobrescrever uma regra de nível superior.**

Exemplo prático:

```
CEO (L1)
 └── Developer (L2)
      └── Code Reviewer (L3 - Specialist)
           └── Test Runner (L4 - Subagent)


O Test Runner (L4) pode retornar:

{
  "status": "failed",
  "reason": "3 tests failed"
}


Mas ele não pode decidir:

"Vou ignorar os testes porque acho que o código está correto."
```

Essa regra deriva do princípio de **Zero-Trust Hierarchical Agent Governance** (CLAW-HCG Framework): a camada GUARDS (L0) é intransponível; camadas superiores definem regras que inferiores executam.

### Matriz de Autorização

Notação:
- ✅ = pode efetivar diretamente
- ⚠️ = pode propor/solicitar, mas requer revisão do nível superior
- 🔐 = mudança excepcional, idealmente com aprovação humana/externo
- ❌ = proibido para esse nível

| Ação | L0 Governance | L1 CEO/Principal | L2 Dept Agent | L3 Specialist | L4 Subagent | L5 Tool |
|------|---------------|------------------|---------------|---------------|-------------|---------|
| Ler memória | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| Criar memória candidata | ✅ | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Alterar código da tarefa | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| Criar Skill proposal | ✅ | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Ativar Skill | ❌ | ❌ | ✅ | ⚠️ | ❌ | ❌ |
| Criar Agent proposal | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Ativar Agent | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Alterar Guardrail | ❌ | ❌ | ❌ | ❌ | ❌ | 🔐 |
| Alterar Governance | ❌ | ❌ | ❌ | ❌ | ❌ | 🔐 |
| Alterar hierarquia | ❌ | ❌ | ❌ | ❌ | ❌ | 🔐 |
| Alterar MCP permissions | ❌ | ⚠️ | ✅ | ❌ | ❌ | 🔐 |

### Níveis de Risco para Mudanças

| Risco | Exemplos | Aprovação Requerida |
|-------|----------|---------------------|
| LOW | código, testes, documentação, exemplos | Automático |
| MEDIUM | dependências, configuração, skills | Revisão do Agent superior |
| HIGH | AGENTS.md, GOVERNANCE.md, guardrails, MCP permissions, memória permanente, criação de agents | Aprovação CEO/humano |

### Integração com Padrões Externos

#### 1. Cellular Council (Cell Roles + Sub-cell Spawning + Stem Cell Differentiation)

Inspiração: **HakanKeskinoglu/cellular-council**  
Repositório: https://github.com/HakanKeskinoglu/cellular-council

Mapeamento:

| Conceito cellular-council | Nível na Governança | Descrição |
|---------------------------|---------------------|-----------|
| CellRole (RISK, TECHNICAL, SECURITY, ETHICS, etc.) | L3 Specialist Agent | Papel especializado do agente |
| Sub-cell spawning | L3 → L4 | Quando complexity threshold exceeded, L3 pode spawn sub-council |
| Stem cell differentiation | L2 → L3 | L2 Department Agent "diferencia" sub-agentes em tempo de execução |
| Consensus Engine | L1 CEO/Principal | Agregação de resultados de agentes especializados em decisão final |
| Structured CellOutput | OUTPUT contracts | Decisão estruturada com rationale, confidence scores |
| Max depth guardrail | Matriz ✅⚠️🔐 | Previne unchecked recursion em sub-cell spawning |

Principais features adotadas:
- **Cell specialization**: cada L3 Specialist tem um papel definido (risk, technical, security, etc.)
- **Sub-cell spawning**: L3 pode delegar para L4 quando complexidade excede threshold
- **Structured output**: CellOutput com decisão + rationale + confidence = base para OUTPUT contracts
- **Consensus strategies**: weighted_average, majority_vote, apex_override — aplicáveis no L1 CEO

#### 2. CLAW-HCG Framework (4-Layer Semantic Model + Zero-Trust Command Hardening)

Inspiração: **sztomyan-dotcom/CLAW-HCG-Framework**  
Repositório: https://github.com/sztomyan-dotcom/CLAW-HCG-Framework

Mapeamento:

| Conceito CLAW-HCG | Nível na Governança | Descrição |
|-------------------|---------------------|-----------|
| GUARDS (Constitutional) | L0 Governance | Red lines absolutas, spend limits, safety |
| SOUL (Ideological) | L1 CEO | Persona, ethics, decision logic |
| AGENTS (Functional) | L2-L3 Dept/Specialist | Domain expertise, workflow management |
| TOOLS (Executional) | L4-L5 Subagent/Tool | Low-level API/CLI capabilities |
| Command hardening (denyCommands) | Matriz ✅⚠️🔐 | Bloqueio físico de comandos de risco HIGH |
| Gated Evolution | Pipeline de promoção | Detection → Verification → Shadow Testing → Production |
| Self-Healing Paradox | EXECUTION-FIRST POLICY | Combate "auto-corrigir" o sistema sem aprovação |

Principais features adotadas:
- **4-layer semantic model**: reframing da hierarquia L0-L5 como GUARDS > SOUL > AGENTS > TOOLS
- **Command hardening**: matriz de autorização funciona como "comando whitelist/blacklist" — comandos de risco HIGH/L1 são bloqueados na prática
- **Gated evolution**: todo Memory→Skill→Rule→Agent passa por pipeline gateado
- **Self-healing paradox**: política de autoaperfeiçoamento controlada impede agentes de "consertar" o sistema sem aprovação

#### 3. PA-Agent / RAPH Framework (3-Tier Hierarchy + Commitment Gates + Agency Problems)

Inspiração: **edmundpokuadu-eng/PA-Agent**  
Repositório: https://github.com/edmundpokuadu-eng/PA-Agent

Mapeamento:

| Conceito PA-Agent/RAPH | Nível na Governança | Descrição |
|------------------------|---------------------|-----------|
| Meta-Principal (Field Institutions) | L0 Governance | Journals, IRBs, professional norms (governance standards) |
| Principal (Researcher) | L1 CEO | Delegação + monitoring |
| Agent (AI Research System) | L2-L5 Agents/Subagents/Tools | Executa tarefas delegated |
| Commitment Gates | EXECUTION-FIRST POLICY | Double-hazard junctures: alta complexidade × baixa reversibilidade |
| Double-Hazard Junctures | Pipeline de tarefas | Stages 4, 5, 8 do PA-Agent: theoretical framework, hypothesis development, statistical analysis |
| Agency Problems (3 tipos) | Política de governança | Information asymmetry, moral hazard, adverse selection |

Principais features adotadas:
- **3-tier hierarchy**: META-PRINCIPAL → PRINCIPAL → AGENT = L0 → L1 → L2+
- **Commitment gates**: em estágios "double-hazard" (high complexity × low reversibility), agente deve produzir documento de oversight antes de avançar
- **Agency problems**: informação sobre por que a governança é necessária
  - Information asymmetry: agente tem mais info que principal → mitigação: contratos INPUT/OUTPUT detalhados + memória auditarável
  - Moral hazard: agente sub-monitora em estágios críticos → mitigação: commitment gates
  - Adverse selection: carga de governance recai sobre quem tem menos recursos → mitigação: matriz de autorização distribuída

---

## 02. Governança Global

### 02.1. SELF-IMPROVEMENT POLICY

Agents are encouraged to identify weaknesses, missing capabilities, repeated patterns and opportunities for improvement.

Agents **MUST** prioritize completing the assigned task before performing optimization work.

Agents **MUST NOT** modify governance, permissions, guardrails, hierarchy or authority autonomously.

Agents **MAY** propose:
- new skills
- skill improvements
- new agents
- agent improvements
- workflow improvements
- documentation improvements
- memory promotion
- rule candidates

Proposals **MUST** be reviewed according to their risk level before becoming active system components.

**Nota:** Esta política combate o **Self-Healing Paradox** (CLAW-HCG): o agente não pode "auto-corrigir" o sistema sem aprovação do nível L0 Governance.

### 02.2. EXECUTION-FIRST POLICY

1. TAREFA receives → agent starts **EXECUTION** immediately
2. During execution, agent may **OBSERVE** patterns, gaps, failures
3. AFTER task completion (or safe interruption), agent enters **LEARN** mode
4. Observations → **candidates** (memory/candidates/), **NOT** direct promotion
5. Candidate → review → test → approve → deploy pipeline
6. **IMPROVEMENT WORK must NOT block delivery** of assigned tasks
7. If existing system can safely complete the task, improvement work is deferred
8. **Commitment gates** at double-hazard junctures (high complexity × low reversibility)

**Nota:** Inspirado em PA-Agent/RAPH stages 4, 5, 8 — double-hazard junctures onde o agente deve produzir documented oversight antes de avançar.

### 02.3. Agency Problems

Três tipos de agency problems que escalam com complexidade cognitiva:

1. **Information Asymmetry**
   - O agente tem mais informação que o principal
   - Escala com complexidade cognitiva
   - Mitigação: contratos INPUT/OUTPUT detalhados, memória auditarível

2. **Moral Hazard**
   - Incentivo do agente a sub-monitorar em estágios críticos
   - Mais provável em gaps de reversibilidade
   - Mitigação: commitment gates em junctures críticos

3. **Adverse Selection**
   - Carga de governance recai sobre instituições com recursos limitados
   - Mitigação: matriz de autorização distribuída (L0-L5), propostas revisadas por nível superior

### 02.4. Pipeline de Promoção Controlada

Fluxo com gates de revisão por nível de risco:

```
Knowledge (skill-kwonledge)
    │
    ▼ (trigger: repeated pattern detected, minimum 3 occurrences)
Candidate (memory/candidates/)
    │
    ▼ (risk analysis + review by superior level)
    │
    ├──► LOW RISK      ► Skill (SKILL.md)
    │                   │
    │                   ▼
    │               activation (L3→L4)
    │
    ├──► MEDIUM RISK   ► Rule candidate → review → approval → AGENTS.md update
    │
    └──► HIGH RISK     ► Proposal → CEO/Principal review → GIT COMMIT (com escrutínio máximo)
```

**Risk Levels (CLAW-HCG inspired):**
- **LOW**: código, testes, documentação, exemplos → automático
- **MEDIUM**: dependências, configuração, skills → revisão do Agent superior
- **HIGH**: AGENTS.md, GOVERNANCE.md, guardrails, MCP permissions, memória permanente, criação de agents → aprovação CEO/humano

### 02.5. Política de Promoção

#### Memória → Skill

Uma memória pode virar Skill quando:
- mesmo conhecimento repetido
- + repetição (min 3 ocorrências)
- + resultado comprovado
- + procedimento generalizável

Fluxo:
```
memory
  ↓
candidate
  ↓
pattern detection
  ↓
proposal
  ↓
review
  ↓
skill
```

#### Skill → Rule

Uma skill pode virar Rule quando:
- impacto sistêmico identificado
- repeated failure pattern
- análise de consequências

Fluxo:
```
skill
  ↓
rule candidate
  ↓
impact analysis
  ↓
approval
  ↓
governance rule
```

#### Regra → Novo Agent

Um novo agent pode ser proposto quando:
- 20+ tarefas no mesmo domínio
- mesmas ferramentas
- mesmo tipo de decisão
- alto volume

Fluxo:
```
20 tarefas
  ↓
proposal
  ↓
review
  ↓
approval
  ↓
novo agent
```

### 02.6. Policy de Criação de Novos Agents

Antes de propor um novo agent:

1. Verificar se Department Agent existente pode cobrir a necessidade
2. Verificar se Specialist Agent existente pode ser estendido
3. Verificar se Skill existente resolve o problema
4. Se nenhum dos acima: propor novo agent com:
   - name
   - responsibilities (lista)
   - required_skills
   - required_tools
   - justification (evidência estatística)

### 02.7. Policy de Criação de Skills

Antes de propor uma nova skill:

1. Verificar se skill similar já existe em `skills/` ou em outro agente
2. Verificar se o conhecimento está em `memory/learnings/` como padrão repetido
3. Verificar se o procedimento é generalizável (não one-off)
4. Se nenhum dos acima: propor nova skill com:
   - name
   - description
   - owner (agente responsável)
   - inputs/outputs esperados
   - procedimento step-by-step
   - exemplos

### 02.8. Capability Lifecycle

Todo capability no sistema segue este ciclo:

```
OBSERVE
   ↓
LEARN
   ↓
REUSE
   ↓
IDENTIFY GAP
   ↓
PROPOSE
   ↓
REVIEW
   ↓
TEST
   ↓
APPROVE
   ↓
DEPLOY
   ↓
MONITOR
   ↓
IMPROVE
```

Isso significa:
- O sistema **NÃO** funciona como: Agent → cria coisas aleatoriamente
- O sistema funciona como: Agent executa → aprende → propõe → revisado → testado → aprovado → deploy → monitorado

### 02.9. Improvement Engine (Observador Não-Executivo)

O Improvement Engine é um processo/mecanismo observador que:

**Observa:**
- tasks (conclusão, falhas, padrões)
- agents (performance, overload, gaps)
- skills (missing, underused, outdated)
- memory (learnings não promovidos, candidates acumulados)
- failures (repeated patterns, unresolved issues)
- handoffs (incompletos, perda de informação)
- latency (tarefas lentas, bottlenecks)
- rework (tarefas refeitas)

**Identifica:**
- SKILL MISSING
- AGENT MISSING
- RULE MISSING
- GUARDRAIL MISSING
- DOCUMENTATION MISSING
- WORKFLOW INEFFICIENT

**Propõe** (via `proposals/`):
- new skills
- new agents
- new rules
- workflow improvements
- documentation improvements

**NÃO:**
- executa tarefas principais
- modifica o sistema diretamente
- auto-promove capabilities

Fluxo:
```
TASK HISTORY
    │
    ▼
Improvement Engine (observador)
    │
    ├──► New Skill proposal
    ├──► New Agent proposal
    └──► New Rule proposal
            │
            ▼
        REVIEW (por nível superior)
            │
            ▼
        TEST
            │
            ▼
        APPROVE
            │
            ▼
        GIT COMMIT
```

### 02.10. Git como Controle de Evolução

Toda mudança significativa no sistema deve ser commitada no Git:

```
main
 ├── feature/auth (implementação)
 ├── proposal/new-skill-api-testing (proposta de skill)
 ├── proposal/new-agent-database (proposta de agent)
 └── proposal/rule-dependency-control (proposta de rule)
```

Padrão de commit semântico:
- `feat(skill): add api testing skill`
- `feat(agent): add database specialist`
- `fix(guardrail): restrict dependency installation`
- `docs(agent): improve developer instructions`
- `refactor(memory): reorganize learning storage`

Branch naming:
- `feature/<descricao>` — novas funcionalidades
- `fix/<descricao>` — correções
- `refactor/<descricao>` — refatorações
- `docs/<descricao>` — documentação
- `proposal/<tipo>/<descricao>` — propostas (skill/agent/rule/architecture)

### 02.11. Portabilidade

A arquitetura **não** deve depender de um único modelo ou runtime.

O mesmo projeto deve poder ser utilizado por:
- Claude Code
- Codex
- OpenCode
- Cursor
- Gemini CLI
- outros agentes compatíveis

A camada específica do runtime deve ficar separada da arquitetura dos agentes.

### 02.12. Referências Cruzadas

| Documento | Finalidade |
|-----------|-----------|
| `agentsos/001.md` | Visão geral, filosofia, 25 fases |
| `agentsos/002.md` | Memory manager, policies |
| `agentsos/003.md` | CEO coordination, agents templates |
| `agentsos/004.md` | Guardrails, contracts, delegation flow |
| `docs/AGENT-ARCHITECTURE.md` | Princípios resumidos |
| [cellular-council](https://github.com/HakanKeskinoglu/cellular-council) | Cell roles, sub-cell spawning, consensus strategies |
| [CLAW-HCG-Framework](https://github.com/sztomyan-dotcom/CLAW-HCG-Framework) | 4-layer guards, command hardening, gated evolution |
| [PA-Agent](https://github.com/edmundpokuadu-eng/PA-Agent) | 3-tier hierarchy, commitment gates, agency problems |

### 02.13. Delivery Loop (BMAD Integration)

O Agent OS adota o **BMAD Delivery Loop** como workflow padrão para execução de tarefas, garantindo processo right-sized (dimensionado à complexidade) e contexto durável.

#### Loop Principal

```
Clarify → Plan → Build → Verify → Learn
   ↑                                        │
   └────────────────────────────────────────┘
   (Learn alimenta próximo Clarify/Plan)
```

#### Planning Paths (Right-Sized)

| Path | Trigger | Fases | Artefatos | Tempo Típico |
|------|---------|-------|-----------|--------------|
| **Quick** | Requisitos claros, <2h, LOW risk | → Build direto | Nenhum (task envelope direto) | < 2h |
| **Standard** | Feature média, 2-8h, MEDIUM risk | Brief → PRD → Arch → Stories | Brief, PRD, Tech Spec, Stories, Sprint Plan | 2-8h |
| **Full** | Complexo, >8h, HIGH risk, alta incerteza | Research → Brief → PRD → Arch → Full Stories | Research, Brief, PRD, Tech Spec, ADRs, Stories, Multi-sprint Plan | > 8h |

#### Fase Details

| Fase | Owner | Skills | Artefatos | Exit Criteria |
|------|-------|--------|-----------|---------------|
| **Clarify** | PM | `brainstorming`, `brief-creation` | Brief | Stakeholders aligned |
| **Plan** | PM + Arquiteto | `prd-writing`, `tech-spec`, `adr-writing`, `sprint-planning` | PRD, Tech Spec, ADRs, Stories, Sprint Plan | CEO approval (se HIGH risk) |
| **Build** | Dev + SRE | `agentos-build`, `dev-story`, `pipeline-yaml`, `cluster-setup` | Code, Tests, Infra | Tests pass, QA gate |
| **Verify** | QA + SRE | `qa-gate`, `test-planning`, `monitor-setup` | Test Report, Monitor Status | All gates green |
| **Learn** | CEO + All | `retrospective` | Retrospective, Action Items | Actions committed |

#### Regras do Loop

1. **Right-Sized**: Escolha o path baseado em clareza, escopo e risco — não use Full para tarefas simples.
2. **Durable Context**: Artefatos (Brief, PRD, Tech Spec, ADRs) são a fonte de verdade — não reexplique decisões.
3. **Specialized Perspectives**: Cada fase usa a expertise apropriada (PM, Architect, Dev, QA, SRE).
4. **One Delivery Path**: Clarify → Plan → Build → Verify → Learn é o único caminho — não pule fases no Standard/Full.
5. **Learn → Plan Feedback**: Retrospective gera action items e memory candidates que alimentam o próximo ciclo.
6. **Existing Codebase**: Para codebases herdados, execute `workflows/existing-codebase/` antes de entrar no loop.

#### Referência

- `docs/plan/choose-a-planning-path.md` — Guia completo de escolha de path
- `agentsos/templates/` — Templates de todos os artefatos
- `agentsos/workflows/` — Workflows por fase

---

## Apêndice A. Glossário

| Termo | Definição |
|-------|-----------|
| Agent | Entidade autônoma com identidade, responsabilidades e skills |
| Department Agent | Agente L2 responsável por uma área funcional (Developer, QA, Security, etc.) |
| Specialist Agent | Agente L3 com expertise específica (database-specialist, auth-specialist, etc.) |
| Subagent | Agente L4 executando tarefa específica dentro de um agente L2/L3 |
| CEO/Principal | Agente L1 orquestrador responsável por delegação e coordenação |
| Governance | Nível L0 com autoridade máxima sobre regras, hierarquia e políticas |
| Skill | Capacidade operacional reutilizável documentada em SKILL.md |
| Memory | Conhecimento persistente armazenado em knowledge base (skill-kwonledge, Obsidian-style) |
| Candidate | Item em `memory/candidates/` aguardando promoção (skill/rule/agent) |
| Contract INPUT | Envelope estruturado enviando tarefa de um agente para outro |
| Contract OUTPUT | Envelope estruturado retornando resultado de uma tarefa |
| Handoff | Processo de transferência de conhecimento/artefatos entre agentes/sessões |
| Commitment Gate | Ponto double-hazard (alta complexidade × baixa reversibilidade) onde oversight documentado é obrigatório |
| Agency Problems | Information asymmetry, moral hazard, adverse selection — problemas estruturais em delegação agente-principal |
| Self-Healing Paradox | Risco de agentes "auto-corrigirem" ambiente de forma perigosa sem aprovação |
| Gated Evolution | Pipeline controlado: Detection → Verification → Shadow Testing → Production |
| Capability Lifecycle | Ciclo: OBSERVE → LEARN → REUSE → IDENTIFY GAP → PROPOSE → REVIEW → TEST → APPROVE → DEPLOY → MONITOR → IMPROVE |

---

## Apêndice B. Histórico de Decisões

| Data | Decisão | Contexto | Consequências |
|------|---------|----------|---------------|
| 2026-09-01 | Criação de GOVERNANCE.md | Necessidade de camada formal de governança acima de AGENTS.md/SKILL.md/knowledge base | Define L0-L5, matriz de autorização, políticas de promoção controlada |
