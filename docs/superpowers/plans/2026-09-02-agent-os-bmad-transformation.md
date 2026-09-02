# Agent OS → BMAD Transformation Implementation Plan

## Phase 1: Delivery Loop + Planning Paths (Phase 1)

### Task 1.1: Define delivery loop in ARCHITECTURE.md and GOVERNANCE.md
**Files:**
- Modify: `docs/ARCHITECTURE.md` (add loop diagram + right-sized matrix)
- Modify: `docs/GOVERNANCE.md` (add §02 Delivery Loop section)

**Interfaces:**
- Consumes: existing ARCHITECTURE.md structure
- Produces: loop diagram + matrix with Quick/Standard/Full paths

**Steps:**
- [ ] **Step 1:** Add delivery loop diagram to `docs/ARCHITECTURE.md` between sections 55-57 (after Pipeline Controlled):
```
Clarify → Plan → Build → Verify → Learn
```↓ (right-sized: small change → Build direto; vague notion → Clarify → Plan)
```
- [ ] **Step 2:** Add §02 "Delivery Loop" to `docs/GOVERNANCE.md` with the matrix and principle "Nível inferior não sobrescreve regras de nível superior" + "Processo right-sized"
- [ ] **Step 3:** Verify both files are syntactically valid markdown

**Expected:** Loop diagram in ARCHITECTURE.md; §02 Delivery Loop in GOVERNANCE.md with right-sized rules

---

### Task 1.2: Create choose-a-planning-path.md
**Files:**
- Create: `docs/plan/choose-a-planning-path.md`
- Modify: `docs/ARCHITECTURE.md` (reference the new file)

**Interfaces:**
- Consumes: loop diagram from Task 1.1
- Produces: 3 planning paths documented

**Steps:**
- [ ] **Step 1:** Write `docs/plan/choose-a-planning-path.md` with 3 paths:
  - **Quick:** → Build direto (tarefa clara, <2h)
  - **Standard:** Brief → PRD → Arch → Stories (tarefa média, ~2-8h)
  - **Full:** Research → Brief → PRD → Arch → Full Stories (tarefa complexa, >8h)
- [ ] **Step 2:** For each path, list: when to use, skills needed, artifacts produced, exit conditions
- [ ] **Step 3:** Reference `docs/plan/choose-a-planning-path.md` from `docs/ARCHITECTURE.md` §02

**Expected:** `docs/plan/choose-a-planning-path.md` with 3 paths; ARCHITECTURE.md references it

---

### Task 1.3: Create artifact templates (brief, PRD, arch, stories, sprint, retrospective)
**Files:**
- Create: `agentsos/templates/brief/product-brief-template.md`
- Create: `agentsos/templates/prd/prd-template.md`
- Create: `agentsos/templates/architecture/architecture-template.md`
- Create: `agentsos/templates/stories/epic-story-template.md`
- Create: `agentsos/templates/sprint/sprint-plan-template.md`
- Create: `agentsos/templates/retrospective/retrospective-template.md`

**Interfaces:**
- Consumes: planning path choice from Task 1.2
- Produces: standardized artifacts per path

**Steps:**
- [ ] **Step 1:** Write `agentsos/templates/brief/product-brief-template.md` with: objective, stakeholders, scope, constraints, success criteria
- [ ] **Step 2:** Write `agentsos/templates/prd/prd-template.md` with: vision, features, user stories, non-functional requirements, assumptions
- [ ] **Step 3:** Write `agentsos/templates/architecture/architecture-template.md` with: stack diagram, tech decisions, ADRs, dependencies, deployment
- [ ] **Step 4:** Write `agentsos/templates/stories/epic-story-template.md` with: epic description, user stories, acceptance criteria, dependencies, definition of done
- [ ] **Step 5:** Write `agentsos/templates/sprint/sprint-plan-template.md` with: sprint goal, selected stories, capacity, committed items, sprint backlog
- [ ] **Step 6:** Write `agentsos/templates/retrospective/retrospective-template.md` with: what went well, what didn't, action items, learnings, next sprint improvements
- [ ] **Step 7:** Verify each template follows the lean style (~1-2 pages max)

**Expected:** 6 templates exist; each is 1-2 pages; follow lean style

---

### Task 1.4: Create existing-codebase workflow
**Files:**
- Create: `agentsos/workflows/existing-codebase/` directory
- Create: `agentsos/workflows/existing-codebase/scan-repo.md` (guia de scan)
- Create: `agentsos/workflows/existing-codebase/establish-context.md` (gera docs/architecture-existing.md)
- Create: `agentsos/workflows/existing-codebase/entry-point.md` (como entrar no loop)

**Interfaces:**
- Consumes: existing repository
- Produces: `docs/architecture-existing.md` + entry into delivery loop

**Steps:**
- [ ] **Step 1:** Write `agentsos/workflows/existing-codebase/scan-repo.md` with steps: scan repo structure, identify tech stack, map existing patterns
- [ ] **Step 2:** Write `agentsos/workflows/existing-codebase/establish-context.md` with: how to generate `docs/architecture-existing.md` from scan
- [ ] **Step 3:** Write `agentsos/workflows/existing-codebase/entry-point.md` with: how to enter the loop after context is established (chooses planning path based on complexity)
- [ ] **Step 4:** Test with a real subdirectory of the project if available, or verify syntax

**Expected:** Workflow docs exist; scan-repo establishes context; entry-point defines loop entry

---