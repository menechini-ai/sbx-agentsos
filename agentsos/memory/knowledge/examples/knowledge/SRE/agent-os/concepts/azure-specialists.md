---
id: agent-os.concept.azure-specialists
title: Azure Specialists (L3)
type: concept
domain: agent-os
tags:
  - azure
  - sre
  - devops
  - aks
  - datadog
  - l3-agents
aliases:
  - especialistas azure
  - agentes l3
status: active
version: "1.0.0"
created: 2026-09-02
updated: 2026-09-02
confidence: high
source: internal
inputs: []
outputs: []
dependencies:
  - [[agent-os-architecture]]
  - [[agent-os-governance]]
quality_score: 90
---

# Azure Specialists (L3)

## Overview

Quatro agentes especializados L3 para operações Azure: Azure DevOps, Azure Cloud, Azure AKS e Datadog.

## Purpose

Fornecer expertise profunda em cada domínio Azure, com guardrails específicos e skills dedicadas.

## Content

### Especialistas

| Agente | Domínio | Skills |
|--------|---------|--------|
| **azure-devops** | Pipelines, repos, artifacts | `pipeline-yaml` |
| **azure-cloud** | RG, VNet, IaC, Bicep/Terraform | `resource-provisioning` |
| **azure-aks** | Clusters, node pools, rollouts | `cluster-setup`, `rollout-strategies` |
| **datadog** | Monitors, tracing, SLOs | `monitor-setup`, `integration-setup` |

### Hierarquia

```
L2 SRE (infra/platform)
├─ L3 azure-devops (Pipelines YAML)
├─ L3 azure-cloud (RG/VNet/IaC)
├─ L3 azure-aks (Clusters/Rollouts)
└─ L3 datadog (Monitors/SLOs)
    └─ L4 subagentes (on-demand)
        └─ L5 tools (az, kubectl, helm, datadog API)
```

### Guardrails Azure

- Cada especialista tem authority.md próprio
- Risk levels específicos por tipo de recurso
- Ferramentas: az, kubectl, helm, terraform, datadog API

## Usage

```
Pipeline YAML com erro:
→ Delegar para L3 azure-devops
→ Usa skill pipeline-yaml
→ Verifica authority.md para risk level
```

## Relationships
- [[agent-os-architecture]] - Estrutura do sistema
- [[promotion-pipeline]] - Como promover learnings

## Notes

- Cada L3 tem AGENTS.md próprio em agentsos/agents/sre/{specialist}/
- Skills Azure ficam em agentsos/skills/{skill-name}/
- Validação automática via agent_conformance_test.py

## References

- `agentsos/agents/sre/azure-devops/AGENTS.md`
- `agentsos/agents/sre/azure-cloud/AGENTS.md`
- `agentsos/agents/sre/azure-aks/AGENTS.md`
- `agentsos/agents/sre/datadog/AGENTS.md`
