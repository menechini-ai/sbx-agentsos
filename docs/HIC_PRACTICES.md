# Boas Práticas para High-Impact Individual Contributor (HIC) no Agent OS

## Visão Geral

Este documento complementa `BEST_PRACTICES.md` e `GOVERNANCE.md`, focando na perspectiva do **High-Impact Individual Contributor (HIC)** — o profissional que gera impacto organizacional desproporcional sem liderar equipes, usando sistemas, automação e julgamento para amplificar sua produtividade.

No contexto do Agent OS, o HIC é:
- Um agente que opera com alta autonomia dentro dos limites da governança
- Um compressor de discovery, execution, review e iteration
- Um arquiteto de sistemas reutilizáveis (skills, templates, workflows)
- Um orquestrador de capacidade computacional (ferramentas, MCPs, subagentes)

---

## 1. O HIC Não é um "10x Engineer" com AI Branding

### A Distinção
- **10x engineer**: produz mais trabalho individual
- **HIC**: produz mais **organizational throughput** — sistema, não heroísmo

### No Agent OS
- O HIC não executa tudo sozinho
- O HIC orquestra agents, skills, memória e ferramentas para criar leverage
- O HIC constrói primitivos reutilizáveis que outros agents podem usar
- O HIC mede sucesso por **impacto sistêmico**, não por horas trabalhadas

---

## 2. Os 4 Pilares do HIC no Agent OS

### 2.1. Automation Stacking

**Conceito**: Empilhar automações para executar múltiplos workstreams em paralelo.

**No Agent OS**:
- Use skills para automatizar workflows repetitivos
- Use MCPs para integrar ferramentas externas (GitHub, filesystem, database)
- Use subagentes L4 para paralelizar tarefas dentro de um agente L2/L3
- Use o Improvement Engine para detectar e propor novas automações

**Exemplo**:
```
HIC (CEO ou Developer)
  ├── Skill: research → coleta informações
  ├── Skill: coding → implementa
  ├── Skill: testing → valida
  └── Subagent: review → revisa código
```

### 2.2. Coordination Collapse

**Conceito**: Eliminar camadas de alinhamento desnecessárias.

**No Agent OS**:
- Use contratos INPUT/OUTPUT estruturados para eliminar ambiguidades
- Use handoffs estruturados para eliminar reuniões de status
- Use memória compartilhada (memory/knowledge) para eliminar "deixe eu checar com X"
- Use a matriz de autorização ✅⚠️🔐 para eliminar gatekeeping desnecessário

**Exemplo**:
```
Sem governança:
  CEO → "faça autenticação" → Developer → pergunta ao CEO 5 vezes → implementa

Com governança:
  CEO → task envelope completo → Developer → executa → handoff → QA
```

### 2.3. Systemic Architectural Impact

**Conceito**: Cada problema resolvido se torna um primitivo para o próximo.

**No Agent OS**:
- Promova skills quando um pattern é detectado em 3+ tasks
- Promova rules quando um problema sistêmico é identificado
- Documente decisões em `memory/decisions/` para referência futura
- Use o Improvement Engine para identificar gaps sistêmicos

**Exemplo**:
```
Task 1: "Como testar API?" → Skill research
Task 2: "Como testar API?" → Pattern detectado
Task 3: "Como testar API?" → Pattern confirmado
Task 4: "Como testar API?" → Skill auth-testing promovida
```

### 2.4. Taste Under Uncertainty

**Conceito**: Saber quais problemas merecem automação, quais decisões precisam de revisão humana, onde a qualidade importa e onde "good enough" é suficiente.

**No Agent OS**:
- Use risk levels LOW/MEDIUM/HIGH para decidir o nível de supervisão
- Use commitment gates para problemas double-hazard (alta complexidade × baixa reversibilidade)
- Use o Capability Lifecycle para decidir quando propor melhorias
- Use agência problems (information asymmetry, moral hazard, adverse selection) para entender onde a governança é necessária

---

## 3. O HIC como Arquétipo de Agente

### 3.1. Perfil do HIC Agent

```
HIC Agent
├── Autonomia Alta
│   └── Opera dentro de limites claros, sem supervisão constante
├── Contexto Rico
│   └── Consulta memory/knowledge, decisions, learnings antes de agir
├── Sistemas Reutilizáveis
│   └── Constrói skills, templates, workflows que outros agents usam
├── Orquestração
│   └── Delega para subagentes, skills, MCPs quando apropriado
└── Julgamento
    └── Sabe quando executar, quando propor, quando escalar
```

### 3.2. O HIC Não é um "One-Person Army"

**Ele é um "Control Plane"**:
- Não executa tudo sozinho
- Delega para agents L2/L3/L4 quando apropriado
- Usa skills para padronizar procedimentos
- Usa memória para evitar repetição
- Usa contratos INPUT/OUTPUT para comunicação clara

### 3.3. Métricas do HIC Agent

| Métrica | Descrição | Como Medir |
|---------|-----------|------------|
| **Throughput** | Tarefas completadas por unidade de tempo | Tasks/dia |
| **Leverage** | Output / Input (quanto ganho por unidade de esforço) | (tasks delegadas + tasks automatizadas) / tasks executadas |
| **Reusability** | Quantas vezes seus outputs são reutilizados | Skills criadas × usos |
| **Systemic Impact** | Quantas tasks são afetadas por suas melhorias | Tasks beneficiadas por suas proposals |
| **Quality** | Taxa de aprovação sem retrabalho | % tasks sem rework |
| **Learning Rate** | Quantos aprendizados são promovidos por período | Candidates / semana |

---

## 4. Carreira em Y para Agents

### 4.1. O Modelo Tradicional (Obsoleto)

```
Individual Contributor
  ↓
Manager (lidera pessoas)
  ↓
Director (lidera gerentes)
  ↓
VP (lidera diretores)
```

**Problema**: Forçar bons técnicos a se tornarem gestores medíocres.

### 4.2. O Modelo HIC (Carreira em Y)

```
Y
├── Management Track
│   ├── Team Lead
│   ├── Engineering Manager
│   ├── Director
│   └── VP
│
└── HIC Track
    ├── Senior Agent (execução impecável)
    ├── Staff Agent (problemas multi-time)
    ├── Principal Agent (estratégia departamental)
    └── Distinguished/Fellow Agent (influência organizacional)
```

**No Agent OS**:
- **L2 Department Agent** → Senior HIC
- **L3 Specialist Agent** → Staff HIC
- **L1 CEO/Principal** → Principal/Distinguished HIC
- **L0 Governance** → Fellow (influência arquitetural)

### 4.3. Critérios de Promoção no HIC Track

| Nível | Critérios |
|-------|-----------|
| **L2 → L3** | Domínio de domínio específico, 3+ skills promovidas, mentoring de L4s |
| **L3 → L2 (dept)** | Liderança técnica de departamento, 10+ tasks complexas, systemic impact demonstrado |
| **L2 → L1** | Orquestração multi-departamento, 20+ tasks, improvement proposals aprovadas, influência cross-functional |

---

## 5. Governança para HICs

### 5.1. O Problema do "Key-Person Risk"

**Definição**: Se um único HIC orquestra processos vitais, a organização depende excessivamente dessa pessoa.

**Mitigações no Agent OS**:
- **Memória compartilhada**: Todo conhecimento deve estar em `memory/knowledge`, não na cabeça do HIC
- **Skills reutilizáveis**: Procedimentos devem ser documentados em `SKILL.md`, não em prompts privados
- **Handoffs estruturados**: O HIC deve ser capaz de transferir trabalho sem perda de informação
- **Improvement Engine**: O sistema deve detectar gaps mesmo quando o HIC não está presente

### 5.2. Shadow AI e Vazamento de Dados

**Problema**: Se o HIC não tem ferramentas seguras, ele buscará soluções próprias, vazando dados confidenciais.

**Mitigações no Agent OS**:
- **Command Hardening**: Bloqueio de comandos perigosos (pip install, rm -rf, curl | bash)
- **MCP Policies**: Ferramentas autorizadas por nível, com audit trail
- **Scope Limits**: Paths permitidos/negados por nível de agente
- **Memory Isolation**: Memória permanente protegida por governança

### 5.3. Accountability e Compliance

**Princípio**: Agents geram resultados rapidamente, mas responsabilidade fiduciária, compliance regulatório e validação final permanecem 100% humanos.

**No Agent OS**:
- **Traceabilidade**: Todo task tem `task_id`, `agent`, `date` para auditoria
- **Proveniência**: Todo learning tem `agent` e `task_id` de origem
- **Validação**: Todo output passa por validation antes de ser considerado completo
- **Handoff**: Todo handoff é documentado com `from_agent`, `to_agent`, `risks`, `instructions`

---

## 6. Novas Métricas para Organizações HIC

### 6.1. Substituindo "Headcount" por "Value Density"

| Métrica Tradicional | Métrica HIC | Descrição |
|---------------------|-------------|-----------|
| Número de pessoas | Value density | Valor gerado por unidade de esforço |
| Headcount | Computational leverage | Capacidade de orquestrar agents/ferramentas |
| Reuniões/hora | Alignment cost | Energia gasta em alinhamento vs. execução |
| Sprint velocity | Task throughput + quality | Tarefas completadas × taxa de aprovação |
| Story points | Impact score | Impacto sistêmico da tarefa |

### 6.2. Métricas do Agent OS

| Métrica | Como Medir |
|---------|-----------|
| **Agent Throughput** | Tasks completadas por agente por semana |
| **Skill Reuse Rate** | Número de usos de cada skill / número de skills disponíveis |
| **Memory Hit Rate** | % de tasks que consultam memory/knowledge antes de executar |
| **Handoff Success Rate** | % de handoffs sem perda de informação ou retrabalho |
| **Improvement Proposal Rate** | Propostas aprovadas / propostas submetidas |
| **Governance Compliance** | % de tasks sem violations de guardrails |
| **Autonomy Score** | % de tasks executadas sem escalação |

---

## 7. Stack Tecnológico do HIC Agent

### 7.1. Ferramentas Essenciais

| Categoria | Ferramenta | Propósito |
|-----------|------------|-----------|
| **Memória** | memory/knowledge | Conhecimento persistente, retrieval, handoff |
| **Skills** | SKILL.md | Procedimentos reutilizáveis |
| **Contratos** | JSON envelopes | Comunicação estruturada entre agents |
| **MCP** | GitHub, Filesystem, Database | Integração com ferramentas externas |
| **Git** | Versionamento | Rastreabilidade, auditoria, colaboração |
| **Workflows** | delegation, handoff, review | Orquestração de tarefas |

### 7.2. Automação Stack

```
Nível 1: Skills (procedimentos reutilizáveis)
  ↓
Nível 2: Workflows (sequências de skills)
  ↓
Nível 3: Agents (orquestração de workflows)
  ↓
Nível 4: MCPs (integração com ferramentas externas)
  ↓
Nível 5: Improvement Engine (auto-detecção de gaps)
```

---

## 8. O Futuro do Agent OS: HIC-Centric

### 8.1. Princípio Norte

> **"Do we have the right architecture and HICs to deliver this result ten times faster and with a fraction of the infrastructure?"**

Ao invés de:
> "How many people do we need to hire to run this?"

### 8.2. Design Decisions para HIC

1. **Simplicidade First**: Start simple, keep primitives clean, add complexity only when it earns its place
2. **Portabilidade**: Mesmo projeto deve funcionar em Claude Code, Codex, OpenCode, Cursor
3. **Reusabilidade**: Skills devem ser portáveis e reutilizáveis
4. **Observabilidade**: Todo agente deve ser auditável (task_id, agent, date)
5. **Leverage**: O sistema deve amplificar, não substituir, o julgamento humano

### 8.3. O que NÃO Fazer

- ❌ Não crie 50 skills que já existem em outra forma
- ❌ Não modifique governança autonomamente (self-healing paradox)
- ❌ Não force HICs a se tornarem gestores
- ❌ Não meça sucesso por headcount ou horas trabalhadas
- ❌ Não confunda automação com autonomia

---

## 9. Checklist: Você é um HIC no Agent OS?

- [ ] Você executa tarefas dentro dos limites da matriz de autorização sem perguntar repetidamente?
- [ ] Você documenta aprendizados em `memory/learnings/` ou candidates?
- [ ] Você propõe skills/rules/agents APENAS após completar tarefas?
- [ ] Você constrói sistemas reutilizáveis (skills, templates, workflows)?
- [ ] Você delega para subagentes quando apropriado, não quando sobrecarregado?
- [ ] Você mede sucesso por impacto sistêmico, não por horas trabalhadas?
- [ ] Você respeita a governança (GOVERNANCE.md) e os contratos (INPUT/OUTPUT)?
- [ ] Você usa o Improvement Engine para detectar gaps, não para criar trabalho?
- [ ] Você tem "taste under uncertainty" — sabe quando automatizar, quando revisar, quando escalar?
- [ ] Você opera como um "control plane", não como um "one-person army"?

---

## 10. Referências

| Fonte | Link | Relevância |
|-------|------|------------|
| agents-scaffolding | https://github.com/griiettner/agents-scaffolding | Scaffolding leve, `.agents/` structure, skills portáveis |
| agents | https://github.com/wyattowalsh/agents | 37 skills portáveis, cross-harness, MCP config |
| DEV Community - HIC | https://dev.to/pvgomes/the-high-individual-contributor-is-becoming-a-new-organizational-unit-3ef8 | HIC como compressor de throughput, 4 pilares |
| Gupy - HIC | https://www.gupy.io/blog/hic-high-impact-individual-contributor | Carreira em Y, métricas, IA como "exército de uma pessoa só" |
| TI Inside - HIC | https://tiinside.com.br/en/17/08/2026/The-headcount-fetish-is-dead%3B-your-company-is-ready-for-HIC-%28high-performance-individual-contributor%29./ | Headcount fetish dead, HIC como arquiteto de sistemas |

---

## Conclusão

O **High-Impact Individual Contributor (HIC)** no Agent OS não é alguém que executa mais tarefas. É alguém que:

1. **Orquestra** agents, skills, memória e ferramentas para criar leverage
2. **Constrói** sistemas reutilizáveis que outros agents usam
3. **Documenta** decisões e aprendizados para referência futura
4. **Propõe** melhorias APENAS após executar e aprender
5. **Respeita** a governança como limite, não como obstáculo
6. **Mede** sucesso por impacto sistêmico, não por atividade

O Agent OS foi projetado para amplificar HICs, não para substituí-los. A governança (GOVERNANCE.md) garante que o leverage seja seguro e auditável. A memória (memory/knowledge) garante que o conhecimento não se perca. Os contratos (INPUT/OUTPUT) garantem que a comunicação seja clara. As skills garantem que procedimentos sejam reutilizáveis.

**O objetivo final**: Dar ao HIC a arquitetura, as ferramentas e a governança para que ele possa produzir resultados que anteriormente requeriam uma equipe inteira — sem perder o controle, a qualidade ou a rastreabilidade.

---

*Documento vivente — atualize conforme novas descobertas sobre HIC practices forem surgindo no projeto Agent OS.*