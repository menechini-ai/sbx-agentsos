---
title: Azure Skills
description: Azure DevOps, Cloud, AKS, and Datadog specialist skills
---

# Azure Skills

Specialist skills for Azure specialists (L3 agents).

## pipeline-yaml

**Purpose**: Create Azure DevOps pipeline YAML files with triggers, stages, and jobs.

**Triggers**: "Create pipeline for...", "Add CI/CD...", "Pipeline YAML..."

**Output**: `pipeline.yaml` with:
- Triggers (branches, tags)
- Stages (build, test, deploy)
- Jobs per stage
- Variables and parameters
- Conditions and dependsOn

## resource-provisioning

**Purpose**: Provision Azure resources (resource groups, VNets, Key Vault, etc.).

**Triggers**: "Provision Azure RG...", "Create VNet...", "Provision resources..."

**Output**: ARM/Bicep/Terraform with:
- Resource group
- Virtual network
- Subnets
- Key Vault
- Policy assignments

## cluster-setup

**Purpose**: Set up Azure AKS clusters with node pools, RBAC, and networking.

**Triggers**: "Set up AKS...", "Create cluster...", "AKS setup..."

**Output**: Cluster config with:
- AKS cluster
- Node pools
- RBAC enabled
- Network profile
- HTTP application routing

## rollout-strategies

**Purpose**: Deployment strategies (rolling, canary, blue-green) for AKS workloads.

**Triggers**: "Deploy with rollout...", "Canary deployment...", "Blue-green deployment..."

**Output**: Deployment strategy with:
- Rolling update config
- Canary parameters
- Blue-green setup
- Health checks

## monitor-setup

**Purpose**: Configure Datadog monitors, alerts, and dashboards.

**Triggers**: "Set up Datadog monitor...", "Configure alerts...", "Monitoring setup..."

**Output**: Datadog monitor config with:
- Metric collection
- Alert thresholds
- Dashboard definition
- SLO definition

## integration-setup

**Purpose**: Set up Azure+Datadog integration and Azure monitor.

**Triggers**: "Set up Azure+Datadog integration...", "Connect Azure to Datadog...", "Integration config..."

**Output**: Integration config with:
- Azure resource mapping
- Datadog tags
- Log collection
- Tracing setup

## Usage

```
Azure DevOps L3: "Use pipeline-yaml for CI/CD pipeline"
→ Creates pipeline.yaml

Azure Cloud L3: "Use resource-provisioning for new project RG"
→ Creates resource group config

Azure AKS L3: "Use cluster-setup for AKS production"
→ Creates AKS cluster config

Datadog L3: "Use monitor-setup for cluster observability"
→ Creates Datadog monitor config
```

## Related

- [Azure Specialist Agents](/agents/sre/azure-devops)
- [SRE Agents](/agents/sre)
- [Delivery Loop](/architecture/delivery-loop)