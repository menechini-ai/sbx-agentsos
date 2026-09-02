---
title: Introduction
description: Agent OS — Modular AI-agent architecture with formal governance
---

# Agent OS

**Agent OS** is a modular AI-agent architecture with formal governance, persistent memory, and reusable skills. It combines a constitutional L0-L5 governance model with the Agent OS (Agent OS Delivery Method) delivery loop.

## Key Features

- **Governance First**: Constitutional L0-L5 hierarchy (GOVERNANCE.md) with zero-trust authority matrix
- **Right-Sized Process**: Three planning paths (Quick/Standard/Full) based on complexity
- **Durable Context**: Decisions carried forward through memory/knowledge (wiki markdown + SQLite)
- **Specialized Perspectives**: PM, Architect, Dev, QA, SRE + Azure specialists
- **Structured Contracts**: INPUT/OUTPUT envelopes for all agent communication

## Quick Start

```bash
# Install Agent OS
npx agent-os install

# Or use the CLI directly
agent-os --help
```

## Architecture Overview

```
L0 GOVERNANCE
 └─ L1 CEO (orchestration)
     ├─ L2 PM (Clarify/Plan)
     ├─ L2 Architect (Tech Spec/ADRs)
     ├─ L2 Developer (Build)
     ├─ L2 QA (Verify)
     └─ L2 SRE (Infra/Platform)
         ├─ L3 Azure DevOps
         ├─ L3 Azure Cloud
         ├─ L3 Azure AKS
         └─ L3 Datadog
```

## Delivery Loop

```
Clarify → Plan → Build → Verify → Learn
```

## Planning Paths

| Path | Trigger | Output | Time |
|------|---------|--------|------|
| **Quick** | Clear, <2h | Direct build | <2h |
| **Standard** | Feature, 2-8h | Brief→PRD→TechSpec→Stories | 2-8h |
| **Full** | Complex, >8h | Research→Brief→PRD→TechSpec→Full Stories | >8h |

## Next Steps

- [Choose a Planning Path](/choose-a-planning-path)
- [Build Your First Change](/build-your-first-change)
- [Explore Agents](/agents/ceo)