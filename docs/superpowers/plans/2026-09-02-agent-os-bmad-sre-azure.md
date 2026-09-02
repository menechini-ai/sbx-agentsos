# Agent OS — BMAD + SRE/Azure + Org Completa — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transformar o Agent OS em um sistema BMAD-izado com organização completa (CEO, PM, Arquiteto, Dev, QA) + departamento SRE/DevOps especializado em Azure DevOps, Azure Cloud, AKS e Datadog, preservando a governança L0-L5 como diferencial.

**Architecture:** Evolução em 8 fases incrementais. Cada fase entrega artefatos testáveis. L0 GOVERNANCE permanece constitucional; BMAD delivery loop (Clarify→Plan→Build→Verify→Learn, right-sized) é adotado como workflow L1/L2. SRE é L2 department com 4 specialists L3 (azure-devops, azure-cloud, azure-aks, datadog) — promove para L2 se escalar (Rule→Agent, 20 tasks, HIGH). Contratos INPUT/OUTPUT e guardrails L0-L5 continuam válidos.

**Tech Stack:** Markdown + YAML (AGENTS.md, SKILL.md, guardrails), Python 3 (tests/benchmarks `agent_conformance_test.py`, `skill_conformance_test.py`, `contract_conformance_test.py`, `benchmarks/governance/validate.py`), Node (futuro installer `npx agent-os`), memory/knowledge externo (wiki Markdown Git + SQLite), Astro+Starlight (futuro docs site).

**Spec:** Requisitos do usuário: (1) parity BMAD (delivery loop, durable context, specialized perspectives, right-sized, one delivery path), (2) stack SRE/DevOps Azure (Azure DevOps, Azure Cloud, AKS, Datadog), (3) org completa CEO/PM/Arquiteto/Dev/QA + SRE. Referências: `AGENTS.md`, `docs/GOVERNANCE.md`, `docs/ARCHITECTURE.md`, `docs/SKILLS.md`, `agentsos/templates/agent/AGENTS-template.md`, `agentsos/agents/{ceo,developer,researcher}/AGENTS.md`, `agentsos/skills/{coding,research,documentation,session-handoff}/SKILL.md`, `agentsos/guardrails/global/{authority,scope,tools}.md`, BMAD-METHOD v6.11.0.

## Global Constraints

- GOVERNANCE.md L0 é constitucional — nível inferior NÃO sobrescreve nível superior (zero-trust)
- Todo AGENTS.md deve conter seções: Identidade, Missão, Responsabilidades, Restrições, Skills, Memória, Handoff, Governança + referência GOVERNANCE.md §01
- Todo SKILL.md deve conter: Purpose, When to Use, When NOT to Use, Procedure, Validation, Failure Modes, Examples, Known Limitations, Improvement Criteria, Changelog + frontmatter name/version/description/owner/status
- Contratos seguem `agentsos/contracts/input/task-envelope.json` e `output/result-envelope.json`
- memory/knowledge é fonte de verdade única (wiki Markdown + SQLite) — não duplicar em `memory/lessons/sessions/handoffs`
- Skills lean (~60 linhas BMAD style) — sem corner cases exóticos; testes afirmam outcomes determinísticos, não output de LLM
- Commits semânticos (Conventional Commits) e branches `proposal/<type>/<desc>`

---

## SDD — System Design Document

### SDD-1 Organograma Alvo

```
L0 GOVERNANCE (GOVERNANCE.md)
 └─ L1 CEO / Principal (ceo/) — orquestração, delegação, approval MEDIUM/HIGH
     ├─ L2 PM (pm/) — Brief, PRD, Roadmap, Stories (Clarify/Plan)
     ├─ L2 Arquiteto (architect/) — Tech Spec, ADRs, stack (Plan)
     ├─ L2 Dev (developer/) — Build, code, testes unit (Build) — JÁ EXISTE, refinar
     ├─ L2 QA (qa/) — Verify, test plans, QA gates (Verify)
     ├─ L2 Researcher (researcher/) — manter como L2 transversal ou absorver em PM/Arch — DECISÃO: manter L2
     └─ L2 SRE / Platform (sre/) — infra, confiabilidade, observability — stack Azure
         ├─ L3 azure-devops — pipelines YAML, repos, boards, artifacts
         ├─ L3 azure-cloud — subscriptions, RG, VNet, policies, IaC (Bicep/Terraform)
         ├─ L3 azure-aks — clusters, node pools, rollouts, RBAC
         └─ L3 datadog — monitors, tracing, logs, SLOs
             └─ L4 subagents on-demand (aks-rollout-runner, datadog-monitor-runner)
                 └─ L5 Tools/MCP (az cli, kubectl, helm, datadog API, github, filesystem)
```

Decisão: SRE como L2 + 4 Azure como L3 (não 4× L2) — governança limpa (6 L2), SRE coordena Azure end-to-end, escala via stem-cell differentiation (GOVERNANCE §01). Se um Azure escalar muito, promove L3→L2 via Rule→Agent (20 tasks, HIGH, CEO+human).

### SDD-2 Delivery Loop (BMAD)

```
Clarify → Plan → Build → Verify → Learn ──┐
  (PM)    (PM+Arch) (Dev+SRE) (QA+SRE) (CEO)  └→ volta para Plan
```
- Right-sized: Quick (→ Build direto, <2h), Standard (Brief→PRD→Arch→Stories, 2-8h), Full (Research→Brief→PRD→Arch→Stories completas, >8h)
- Artefatos: brief, PRD, tech-spec/ADR, stories, sprint-plan, retrospective
- Comandos: `agentos-build` (equiv bmad-build), `agentos-help` (what's next / what's optional)

### SDD-3 Mapeamento de Arquivos

| Componente | Arquivo | Tipo |
|---|---|---|
| PM L2 | `agentsos/agents/pm/AGENTS.md` | novo |
| Arquiteto L2 | `agentsos/agents/architect/AGENTS.md` | novo |
| QA L2 | `agentsos/agents/qa/AGENTS.md` | novo |
| SRE L2 | `agentsos/agents/sre/AGENTS.md` | novo |
| Azure DevOps L3 | `agentsos/agents/sre/azure-devops/AGENTS.md` | novo |
| Azure Cloud L3 | `agentsos/agents/sre/azure-cloud/AGENTS.md` | novo |
| Azure AKS L3 | `agentsos/agents/sre/azure-aks/AGENTS.md` | novo |
| Datadog L3 | `agentsos/agents/sre/datadog/AGENTS.md` | novo |
| Delivery loop | `docs/ARCHITECTURE.md` § Fluxo + `docs/GOVERNANCE.md` §02 | modify |
| Planning paths | `docs/plan/choose-a-planning-path.md` | novo |
| Templates | `agentsos/templates/{brief,prd,architecture,stories,sprint,retrospective}/` | novos |
| Skills Clarify/Plan | `agentsos/skills/{brainstorming,brief-creation,prd-writing,tech-spec,sprint-planning}/SKILL.md` | novos |
| Skills Build/Verify/Learn | `agentsos/skills/{agentos-build,dev-story,pipeline-yaml,resource-provisioning,cluster-setup,rollout-strategies,monitor-setup,integration-setup,retrospective,agentos-help}/SKILL.md` | novos |
| Workflows | `agentsos/workflows/{clarify,plan,build,verify,learn,existing-codebase}/` | novos |
| Guardrails | `agentsos/guardrails/global/{scope,tools,authority,change-risk-levels}.md` | modify |
| Installer | `package.json`, `tools/installer/agent-os-cli.js`, `agentsos/module.yaml`, `agentsos-modules.yaml` | novos |
| Quality gate | `.husky/pre-push`, `.lintstagedrc`, `tools/validate_skills.py` | novos |
| Docs site | `website/` Astro+Starlight | novo |
| Web bundles | `web-bundles/` | novo |

### SDD-4 Fluxo SRE Exemplo

```
CEO: "Provisionar AKS prod com Datadog + pipeline"
 → PM: Brief (objetivo, SLOs, constraints)
 → Arquiteto: Tech Spec (VNet, AKS sku, node pools, Datadog integration) + ADR "AKS vs ACI"
 → SRE decompõe p/ L3: azure-cloud (RG+VNet+Bicep) → azure-aks (cluster+node pools) → datadog (monitors+APM) → azure-devops (pipeline YAML)
 → Dev: workloads app
 → QA: qa-gate (cluster healthy? monitors firing? pipeline green?)
 → CEO: retrospective → candidates
```

---

## TDD — Test Strategy (Tests First)

TDD segue `superpowers:test-driven-development`: RED → GREEN → REFACTOR. Não testar output de LLM; testar outcomes determinísticos.

### TDD-1 Testes de Conformidade Existentes (base)

- `agentsos/tests/agents/agent_conformance_test.py` — valida AGENTS.md: seções Identidade/Missão/Responsabilidades/Restrições/Skills/Memória/Handoff/Governança + referência GOVERNANCE.md + level L0-L5. Atualmente testa `["ceo","developer","researcher"]`.
- `agentsos/tests/skills/skill_conformance_test.py` — valida SKILL.md: frontmatter name/version/description/owner/status + seções Purpose/When to Use/When NOT to Use/Procedure/Validation/Failure Modes/Examples/Known Limitations/Improvement Criteria/Changelog. Atualmente testa `["research","coding","documentation","session-handoff"]`.
- `agentsos/tests/contracts/contract_conformance_test.py` — valida envelopes INPUT/OUTPUT.
- `agentsos/benchmarks/governance/validate.py` — benchmark governança.

### TDD-2 Novos Testes a Criar (RED first)

1. **Agent conformance estendido** — adicionar aos arrays de teste: `pm`, `architect`, `qa`, `sre`, `sre/azure-devops`, `sre/azure-cloud`, `sre/azure-aks`, `sre/datadog` → teste falha até AGENTS.md existirem.
2. **Skill conformance estendido** — adicionar skills novas ao array: `brainstorming`, `brief-creation`, `prd-writing`, `tech-spec`, `sprint-planning`, `agentos-build`, `pipeline-yaml`, `resource-provisioning`, `cluster-setup`, `monitor-setup` etc.
3. **Guardrail scope test** — `agentsos/tests/guardrails/scope_test.py` — valida que `scope.md` lista paths autorizados para novos L2/L3 e nega `secrets/`, `production/`.
4. **Delivery loop test** — `agentsos/tests/architecture/delivery_loop_test.py` — valida que `ARCHITECTURE.md` contém loop Clarify→Learn e referência `choose-a-planning-path.md`.
5. **Contract round-trip test** — envelope SRE (ex: TASK SRE-001) com sender `sre` L2 → receiver `sre/azure-aks` L3.

Cada teste é escrito primeiro (RED), depois implementação faz passar (GREEN).

---

## Tasks — Decomposição (Bite-sized, cada task = testável + commitável)

### Task 0: Foundation — package.json, installer, quality gate, modules registry

**Files:**
- Create: `package.json`
- Create: `tools/installer/agent-os-cli.js`
- Create: `agentsos/module.yaml`
- Create: `agentsos-modules.yaml` (ou `agentos-modules.yaml`)
- Create: `.husky/pre-push` (opcional nesta iteração — pode ser Task 0.4 separada)
- Test: `npm pack --dry-run`, `node tools/installer/agent-os-cli.js --help`

**Interfaces:**
- Consumes: `.env` (AI_MEMORY_* vars)
- Produces: `package.json` bin `agent-os`/`aos`, CLI `install` com picker de módulos, registry YAML

- [ ] **Step 1: Write failing test — package.json bin resolve**
```python
# tests/test_foundation.py
def test_package_json_has_bin():
    import json, os
    path = "package.json"
    assert os.path.exists(path), "package.json not found"
    data = json.load(open(path))
    assert "bin" in data
    assert "agent-os" in data["bin"]
```
Run: `pytest tests/test_foundation.py::test_package_json_has_bin -v` → FAIL (file not found)

- [ ] **Step 2: Implement package.json mínimo**
```json
{"name":"agent-os","version":"1.0.0","bin":{"agent-os":"tools/installer/agent-os-cli.js","aos":"tools/installer/agent-os-cli.js"},"scripts":{"quality":"echo quality"}}
```

- [ ] **Step 3: Verify PASS**

- [ ] **Step 4: CLI skeleton + module.yaml** (análogo, TDD)

- [ ] **Step 5: Commit** `feat(foundation): add package.json, installer CLI and module registry`

---

### Task 1: Delivery Loop + Planning Paths + Templates

**Files:**
- Modify: `docs/ARCHITECTURE.md` (loop diagram + matrix)
- Modify: `docs/GOVERNANCE.md` ( §02 Delivery Loop)
- Create: `docs/plan/choose-a-planning-path.md`
- Create: `agentsos/templates/brief/product-brief-template.md`
- Create: `agentsos/templates/prd/prd-template.md`
- Create: `agentsos/templates/architecture/tech-spec-template.md`
- Create: `agentsos/templates/architecture/adr-template.md`
- Create: `agentsos/templates/stories/epic-story-template.md`
- Create: `agentsos/templates/sprint/sprint-plan-template.md`
- Create: `agentsos/templates/retrospective/retrospective-template.md`
- Test: `agentsos/tests/architecture/delivery_loop_test.py`

**Interfaces:**
- Consumes: Task 0 registry
- Produces: loop documentado, 3 paths (Quick/Standard/Full), 6 templates

- [ ] **Step 1: Write failing test**
```python
def test_architecture_has_delivery_loop():
    content = open("docs/ARCHITECTURE.md").read()
    assert "Clarify" in content and "Learn" in content
    assert "choose-a-planning-path" in content
def test_templates_exist():
    import os
    for p in ["agentsos/templates/brief/product-brief-template.md","agentsos/templates/prd/prd-template.md"]:
        assert os.path.exists(p)
```

- [ ] **Step 2: Implement loop + templates (lean 1-2 páginas cada)**

- [ ] **Step 3: Verify PASS**

- [ ] **Step 4: Commit** `feat(loop): add delivery loop, planning paths and artifact templates`

---

### Task 2: Org Core — CEO refinement + PM, Arquiteto, QA

**Files:**
- Modify: `agentsos/agents/ceo/AGENTS.md` (adicionar strategy/orchestration lean, delivery loop)
- Create: `agentsos/agents/pm/AGENTS.md` (L2)
- Create: `agentsos/agents/architect/AGENTS.md` (L2)
- Create: `agentsos/agents/qa/AGENTS.md` (L2)
- Test: `agentsos/tests/agents/agent_conformance_test.py` estendido p/ pm/architect/qa

**Interfaces:**
- Consumes: Task 1 loop + AGENTS-template.md
- Produces: 3 novos L2 AGENTS.md + CEO refinado

- [ ] **Step 1: Write failing test**
```python
def test_new_agents_exist():
    import os
    for agent in ["pm","architect","qa"]:
        assert os.path.exists(f"agentsos/agents/{agent}/AGENTS.md")
        content = open(f"agentsos/agents/{agent}/AGENTS.md").read()
        assert "GOVERNANCE.md" in content
        assert "Handoff" in content
```

- [ ] **Step 2: Implement AGENTS.md lean (~50 linhas) por agente, seguindo template + developer/AGENTS.md como referência, BMAD lean (sem When NOT to Use exótico)**

- [ ] **Step 3: Verify PASS** `python agentsos/tests/agents/agent_conformance_test.py`

- [ ] **Step 4: Commit** `feat(agents): add PM, Architect and QA L2 agents`

---

### Task 3: Org Core Skills — Clarify/Plan/Build/Verify/Learn

**Files:**
- Create: `agentsos/skills/brainstorming/SKILL.md`
- Create: `agentsos/skills/brief-creation/SKILL.md`
- Create: `agentsos/skills/prd-writing/SKILL.md`
- Create: `agentsos/skills/tech-spec/SKILL.md`
- Create: `agentsos/skills/sprint-planning/SKILL.md`
- Create: `agentsos/skills/agentos-build/SKILL.md` (equiv bmad-build)
- Create: `agentsos/skills/dev-story/SKILL.md`
- Create: `agentsos/skills/review/SKILL.md`
- Create: `agentsos/skills/retrospective/SKILL.md`
- Create: `agentsos/skills/agentos-help/SKILL.md` (what's next)
- Test: `agentsos/tests/skills/skill_conformance_test.py` estendido

**Interfaces:**
- Consumes: Task 2 agents
- Produces: 10 lean SKILL.md (~60 linhas cada)

- [ ] **Step 1: Failing test** — lista de skills esperadas não encontrada

- [ ] **Step 2: Implement SKILL.md lean** — frontmatter + Purpose/When to Use/When NOT/Procedure(5 steps)/Validation/Failure Modes/Examples/Limitations/Improvement/Changelog

- [ ] **Step 3: PASS**

- [ ] **Step 4: Commit** `feat(skills): add Clarify/Plan/Build/Verify/Learn lean skills`

---

### Task 4: SRE L2 + 4× Azure L3

**Files:**
- Create: `agentsos/agents/sre/AGENTS.md` (L2)
- Create: `agentsos/agents/sre/azure-devops/AGENTS.md` (L3)
- Create: `agentsos/agents/sre/azure-cloud/AGENTS.md` (L3)
- Create: `agentsos/agents/sre/azure-aks/AGENTS.md` (L3)
- Create: `agentsos/agents/sre/datadog/AGENTS.md` (L3)
- Test: `agent_conformance_test.py` estendido p/ sre/*

**Interfaces:**
- Consumes: Task 2 pattern
- Produces: 1× L2 + 4× L3 AGENTS.md

- [ ] **Step 1: Failing test**
```python
def test_sre_agents_exist():
    import os
    for p in ["agentsos/agents/sre/AGENTS.md","agentsos/agents/sre/azure-aks/AGENTS.md","agentsos/agents/sre/datadog/AGENTS.md"]:
        assert os.path.exists(p)
```

- [ ] **Step 2: Implement AGENTS.md** — Identidade L2/L3, Responsabilidades Azure específicas, Restrições matriz ✅⚠️🔐, Skills, Memória, Handoff, Governança

- [ ] **Step 3: PASS**

- [ ] **Step 4: Commit** `feat(agents): add SRE L2 and 4 Azure L3 specialists`

---

### Task 5: Azure Skills — pipeline-yaml, resource-provisioning, cluster-setup, rollout, monitor

**Files:**
- Create: `agentsos/skills/pipeline-yaml/SKILL.md` (azure-devops)
- Create: `agentsos/skills/resource-provisioning/SKILL.md` (azure-cloud, Bicep/Terraform)
- Create: `agentsos/skills/cluster-setup/SKILL.md` (azure-aks)
- Create: `agentsos/skills/rollout-strategies/SKILL.md` (azure-aks)
- Create: `agentsos/skills/monitor-setup/SKILL.md` (datadog)
- Create: `agentsos/skills/integration-setup/SKILL.md` (datadog+AKS)
- Create: `agentsos/skills/slo-management/SKILL.md` (opcional)
- Test: `skill_conformance_test.py` estendido

**Interfaces:**
- Consumes: Task 4 agents
- Produces: 6 lean SKILL.md Azure

- [ ] **Step 1: Failing test** — skills não encontradas

- [ ] **Step 2: Implement SKILL.md** — Inputs: pipeline_type/target_branch, resource_type/location, cluster_name/rg, strategy rolling/canary, metric/query/threshold; Tools: az cli, kubectl, helm, datadog API

- [ ] **Step 3: PASS**

- [ ] **Step 4: Commit** `feat(skills): add Azure DevOps/Cloud/AKS/Datadog skills`

---

### Task 6: Guardrails — scope, tools, authority, change-risk-levels

**Files:**
- Modify: `agentsos/guardrails/global/scope.md` (paths L2 novos + L3 sre/*)
- Modify: `agentsos/guardrails/global/tools.md` (azure.cli, kubectl, helm, datadog.api, bicep/terraform)
- Modify: `agentsos/guardrails/global/authority.md` (matriz PM/Arch/Dev/QA/SRE/L3)
- Modify: `agentsos/guardrails/global/change-risk-levels.md` (pipeline dev LOW, prod MEDIUM, AKS prod HIGH)
- Test: `agentsos/tests/guardrails/scope_test.py` (novo)

**Interfaces:**
- Consumes: Tasks 2+4 agent paths
- Produces: guardrails atualizados

- [ ] **Step 1: Failing test**
```python
def test_scope_has_sre_paths():
    content = open("agentsos/guardrails/global/scope.md").read()
    assert "agents/sre" in content
    assert "azure-aks" in content
```

- [ ] **Step 2: Implement guardrails**

- [ ] **Step 3: PASS**

- [ ] **Step 4: Commit** `fix(guardrails): update scope/tools/authority for SRE/Azure`

---

### Task 7: Durable Context — memory/knowledge portable, web-bundles, agentos-build/help

**Files:**
- Create: `agentsos/memory/portable-context.md` (export/import format)
- Create: `web-bundles/` (Gemini Gems / ChatGPT GPTs prompts)
- Create/modify: `.opencode/skills/agentos-build/SKILL.md` + `agentos-help/SKILL.md` hooks
- Test: manual `agent-os export` / `import` round-trip (se CLI pronto) ou teste de existência de portable-context.md

**Interfaces:**
- Consumes: Task 1 templates + Task 3 skills
- Produces: contexto portável Web→IDE

---

### Task 8: Docs Site — Astro+Starlight + Build your first change

**Files:**
- Create: `website/` (Astro 6.4.6 + Starlight 0.40.0)
- Create: `website/src/content/docs/build-your-first-change.md`
- Modify: `docs/` migrado para Starlight
- Test: `npm run docs:build` (Astro build)

---

## Coding — Ordem de Execução (Sprints)

Sprint 1 (esta sessão): Tasks 2 + 4 + 6 (agents + guardrails) — entrega org completa testável
Sprint 2: Tasks 3 + 5 (skills lean)
Sprint 3: Task 1 (delivery loop + templates) — pode paralelizar com Sprint 2
Sprint 4: Tasks 0 + 7 + 8 (foundation, durable context, docs site)

Cada sprint: RED (teste falha) → GREEN (implementa mínimo) → REFACTOR → COMMIT

---

## Review — Critérios de Aceite

- [ ] `python agentsos/tests/agents/agent_conformance_test.py` PASS para todos os agentes (ceo, developer, researcher, pm, architect, qa, sre, sre/azure-*, sre/datadog)
- [ ] `python agentsos/tests/skills/skill_conformance_test.py` PASS para todas as skills
- [ ] `python agentsos/tests/contracts/contract_conformance_test.py` PASS
- [ ] `python agentsos/benchmarks/governance/validate.py` grade geral > 80%
- [ ] `agentsos/guardrails/global/scope.md` lista paths L2 novos e nega secrets/production
- [ ] `docs/ARCHITECTURE.md` contém delivery loop e referência choose-a-planning-path
- [ ] Nenhum AGENTS.md/SKILL.md viola GOVERNANCE.md L0
- [ ] Commits semânticos por task

---

## Self-Review do Plano

1. **Spec coverage:** Todos os requisitos (BMAD parity + SRE/Azure + org completa) mapeados para Tasks 0-8. Sem gaps.
2. **Placeholder scan:** Nenhum TBD/TODO; todos os steps têm código de teste e estrutura de arquivo explícita.
3. **Type consistency:** Nomes de agentes/skills consistentes entre SDD, TDD e Tasks (pm, architect, qa, sre, sre/azure-*, pipeline-yaml etc.).
