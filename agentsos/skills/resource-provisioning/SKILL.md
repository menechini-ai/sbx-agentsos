# SKILL.md - resource-provisioning

## Metadados

- **Name**: resource-provisioning
- **Version**: 1.0.0
- **Description**: Provisionamento de recursos Azure via IaC (Bicep/Terraform) com validação what-if/plan.
- **Owner**: azure-cloud
- **Status**: stable

## Inputs

- `resource_type` — Tipo de recurso Azure (ex: Microsoft.Network/virtualNetworks, Microsoft.ContainerService/managedClusters)
- `location` — Região Azure (ex: eastus, westeurope)
- `resource_group` — Nome do Resource Group existente ou a criar
- `parameters` — JSON com parâmetros específicos do recurso
- `iac_tool` — `bicep` | `terraform` (default: bicep)
- `tags` — Tags obrigatórias (ex: environment, owner, cost-center)

## Outputs

- `resource_id` — Azure Resource ID do recurso provisionado
- `deployment_output` — Outputs do deployment (ex: subnet IDs, FQDNs)
- `provisioning_report` — Relatório com status, outputs, validação e custos estimados

## Dependencies

- `az cli` — Azure CLI para validação e deployment
- `bicep` / `terraform` — IaC tool
- `filesystem` — Leitura/escrita de templates

## Tools

- `az cli` — `az deployment group create/validate`, `az group create`
- `bicep` — `bicep build`, `bicep what-if` (via `az deployment group what-if`)
- `terraform` — `terraform init/plan/apply`
- `filesystem.read` — Ler templates Bicep/Terraform existentes
- `filesystem.write` — Escrever templates Bicep/Terraform
- `terminal` — Executar comandos de validação

## Purpose

Provisionar recursos Azure de forma determinística e auditável via IaC, produzindo um `provisioning_report` que pode ser:
- Validado pelo agente L3 azure-cloud e L2 SRE
- Promovido para knowledge no memory/knowledge (padrões de provisionamento)
- Usado como base para skills de cluster-setup e rollout

## When to Use

- Quando receber task envelope INPUT com objective de provisionar recurso Azure
- Quando necessário criar/atualizar VNet, Subnet, NSG, Key Vault, Storage Account
- Para provisionar infra base para AKS (RG, VNet, Subnet, Private DNS, Key Vault)
- Para aplicar policies e compliance via Azure Policy

## When NOT to Use

- Quando o recurso já existe e não precisa de alteração (consultar state primeiro)
- Quando a tarefa envolve segredos sensíveis sem Key Vault (verificar `GOVERNANCE.md` §01)
- Quando o deployment é em produção sem aprovação L1/L2 (matriz 🔐)

## Procedure

1. **Ler task envelope**: Consultar `contracts/input/task-envelope.md` para entender:
   - Objective preciso (resource_type, location, resource_group)
   - Constraints (tags obrigatórias, naming convention)
   - Skills e tools autorizadas (matriz ✅⚠️🔐)
   - Memory: patterns de provisionamento anteriores

2. **Verificar estado existente**: Utilizar `az cli` para verificar:
   - Se Resource Group existe
   - Se recurso já existe e seu estado
   - Se há conflicts de naming/tags

3. **Gerar/selecionar template IaC**:
   - Bicep: criar `.bicep` com parâmetros, outputs, modularização
   - Terraform: criar `.tf` com variables, outputs, remote state
   - Usar módulos existentes em `agentsos/templates/iac/` se disponíveis

4. **Validar (what-if/plan)**:
   - Bicep: `az deployment group what-if --template-file main.bicep --parameters ...`
   - Terraform: `terraform plan -out=tfplan`
   - Verificar changes, costs, e se respeita guardrails (scope.md paths)

5. **Aplicar (se aprovado)**:
   - Bicep: `az deployment group create --template-file main.bicep --parameters ...`
   - Terraform: `terraform apply tfplan`
   - Capturar outputs (ex: vnetId, subnetIds, keyVaultUri)

6. **Produzir report**: Gerar `provisioning_report` com:
   - `status`: created/updated/failed/validated
   - `resource_id`: Azure Resource ID
   - `deployment_output`: outputs do deployment
   - `cost_estimate`: estimativa de custo mensal
   - `risks`: risks identificados (ex: recurso em prod sem tag)
   - `memory_candidates`: patterns de provisionamento
   - `improvement_candidates`: skills/rules a propor

## Validation

- Verificar se `az deployment group what-if` ou `terraform plan` passa sem erros
- Confirmar que recursos criados têm tags obrigatórias
- Confirmar que outputs do deployment são capturados
- Cross-check com `memory/knowledge` — promover learning se padrão recorrente
- Confirmar que provisioning_report descreve realidade

## Failure Modes

- **What-if/plan failure**: Template inválido ou conflict de recursos; recomenda-se corrigir template
- **Deployment timeout**: Recurso demora para provisionar; recomenda-se async polling
- **Missing tags**: Recurso sem tags obrigatórias; recomenda-se adicionar tags no template
- **Authority overreach**: Deploy em produção sem approval; recomenda-se propor via `proposals/`

## Examples

### Exemplo 1: Provisionar VNet para AKS

```
Input: resource_type="Microsoft.Network/virtualNetworks", location="eastus",
  resource_group="rg-aks-prod", iac_tool="bicep",
  parameters={vnetName: "vnet-aks", addressSpace: "10.0.0.0/16",
    subnets: [aks-subnet, private-endpoint-subnet]}
Output: provisioning_report contendo:
  - status: created
  - resource_id: /subscriptions/.../resourceGroups/rg-aks-prod/providers/Microsoft.Network/virtualNetworks/vnet-aks
  - deployment_output: { vnetId: "...", subnetIds: ["...", "..."] }
  - cost_estimate: $50/mês
  - memory_candidates: [type: learning, description: "VNet para AKS usa /16 com 2 subnets"]
```

### Exemplo 2: Criar Resource Group com tags

```
Input: resource_type="Microsoft.Resources/resourceGroups", location="eastus",
  resource_group="", iac_tool="bicep",
  tags={environment: "prod", owner: "sre-team", cost-center: "cc-123"}
Output: provisioning_report contendo:
  - status: created
  - resource_id: /subscriptions/.../resourceGroups/rg-new
  - deployment_output: { name: "rg-new", location: "eastus" }
  - risks: baixo
```

## Known Limitations

- Dependente de `az cli` e permissões de Contributor/Owner no subscription
- Bicep what-if nem sempre 100% preciso (alguns recursos não suportam)
- Terraform state management requer backend remoto configurado
- Não cobre todos os 3000+ tipos de recurso Azure (focar em core infra)

## Improvement Criteria

- **Nova skill proposta**: Quando pattern de provisionamento detectado em 4+ tasks
- **Promoção para rule**: Quando pattern sistêmico impacta múltiplas tarefas (ex: naming convention)
- **Memory promotion**: Quando aprendizado relevante para arquitetura de infra

## Changelog

- **1.0.0**: Versão inicial