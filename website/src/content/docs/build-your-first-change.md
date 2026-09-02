---
title: Build Your First Change
description: Step-by-step tutorial to make your first change with Agent OS
---

# Build Your First Change

This tutorial walks you through making your first change using Agent OS, from idea to deployed code.

## Prerequisites

- Node.js 20.12+
- Python 3.10+
- Git
- Azure subscription (for SRE examples)

## Step 1: Install Agent OS

```bash
npx agent-os install
```

The installer will prompt you to select modules:
- **Core** (always selected) — Governance, agents, skills
- **SRE** — Infrastructure platform
- **Azure DevOps** — Pipelines specialist
- **Azure Cloud** — Resources specialist
- **Azure AKS** — Kubernetes specialist
- **Datadog** — Monitoring specialist

## Step 2: Initialize Project

```bash
# In your project directory
agent-os init
```

This creates:
- `AGENTS.md` — System contract
- `GOVERNANCE.md` — Constitutional governance
- `agentsos/` — Architecture directory
- `docs/` — Documentation

## Step 3: Choose Your Planning Path

Ask yourself: **How clear is my requirement?**

| Path | When | Start Here |
|------|------|------------|
| **Quick** | "Fix this bug", "Update this config" | Step 6 |
| **Standard** | "Add payment feature" | Step 4 |
| **Full** | "Build new microservice platform" | Step 3 |

## Step 4: Standard Path — Clarify

Run the brainstorming skill:

```bash
# In your AI coding tool
Use the `brainstorming` skill with:
- topic: "Add user authentication"
- participants: [PM, Architect, Dev, QA, SRE]
```

Output: `brainstorm_report` with ideas, risks, questions.

## Step 5: Standard Path — Plan

Create the artifacts in order:

### 5.1 Brief
```bash
Use the `brief-creation` skill with:
- topic: "User authentication with JWT"
- stakeholders: ["PM", "Tech Lead", "SRE"]
```

Output: `agentsos/templates/brief/product-brief-template.md`

### 5.2 PRD
```bash
Use the `prd-writing` skill with:
- brief: [from step 5.1]
```

Output: `agentsos/templates/prd/prd-template.md`

### 5.3 Tech Spec
```bash
Use the `tech-spec` skill with:
- prd: [from step 5.2]
```

Output: `agentsos/templates/architecture/tech-spec-template.md`

### 5.4 ADRs (for non-trivial decisions)
```bash
Use the `adr-writing` skill with:
- decision: "Use PostgreSQL over MongoDB for auth"
```

Output: `agentsos/templates/architecture/adr-template.md`

### 5.5 Stories & Sprint Plan
```bash
Use the `sprint-planning` skill with:
- prd_stories: [from PRD]
- team_capacity: {dev: 2, qa: 1, sre: 1}
```

Output: `agentsos/templates/sprint/sprint-plan-template.md`

## Step 6: Build

### 6.1 Break Down Story (if complex)
```bash
Use the `dev-story` skill with:
- story: "US-001: As a user, I want to login..."
```

### 6.2 Implement
```bash
Use the `agentos-build` skill with:
- story: "US-001"
- tech_spec: [from step 5.3]
```

This:
1. Creates feature branch
2. Implements code
3. Writes tests
4. Runs quality gate
5. Creates PR

### 6.3 Review
```bash
Use the `review` skill on the PR
```

## Step 7: Verify

```bash
Use the `qa-gate` skill with:
- story: "US-001"
- implementation: [from step 6.2]
```

Checks:
- Acceptance criteria met
- Tests passing
- Security review passed
- Performance acceptable

## Step 8: Learn

```bash
Use the `retrospective` skill with:
- sprint_metrics: {velocity: 18, bugs: 2}
- sprint_outcome: {done: 5, carried: 1}
```

Outputs action items and learnings for `memory/knowledge`.

## Complete Example: Add Authentication

Let's walk through a complete example.

### 1. Clarify
```
Topic: "Add JWT authentication to API"
Participants: PM, Architect, Dev, QA, SRE
Output: brainstorm_report
  - Solutions: JWT, OAuth2, API Keys
  - Risks: Token expiration, refresh flow
  - Questions: Refresh token rotation?
```

### 2. Brief
```
Objective: Implement JWT authentication for API with <100ms latency
Scope: Login, register, token refresh, logout
Success Criteria: p99 latency < 100ms, 99.9% uptime
```

### 3. PRD
```
Features:
- MUST: Login, Register, Refresh Token
- SHOULD: Password reset, Email verification
- COULD: MFA, Social login

NFRs:
- Latency p99 < 100ms
- Availability 99.9%
- PCI compliance for passwords
```

### 4. Tech Spec
```
Architecture: API Gateway → Auth Service → PostgreSQL + Redis
Stack: Node.js + Express + PostgreSQL + Redis
API:
  POST /auth/login
  POST /auth/register
  POST /auth/refresh
  POST /auth/logout
Infra: Azure AKS + PostgreSQL Flexible Server + Redis
```

### 5. Stories
```
US-001: Login endpoint (3 pts)
US-002: Register endpoint (3 pts)
US-003: Token refresh (2 pts)
US-004: Password hashing (2 pts)
```

### 6. Build
```bash
# Dev implements US-001
agentos-build US-001

# Creates: feature/US-001-login
# Implements: POST /auth/login
# Tests: unit + integration
# PR: #42
```

### 7. Verify
```bash
qa-gate US-001
# All criteria pass → merge
```

### 8. Learn
```
Retrospective:
- What went well: TDD caught 3 bugs early
- What didn't: Token refresh logic complex
- Action: Create auth-testing skill
```

## Next Steps

- [Choose a Planning Path](/choose-a-planning-path)
- [Explore Agents](/agents/ceo)
- [Explore Skills](/skills/overview)
- [View Templates](/templates/brief)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Tests failing | Run `agentos-build` again with `--verbose` |
| QA gate stuck | Check `qa-gate` skill for missing criteria |
| Planning path unclear | Use `agentos-help` for guidance |