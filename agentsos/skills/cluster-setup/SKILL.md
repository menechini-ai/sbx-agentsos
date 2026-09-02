# SKILL.md - cluster-setup

## Metadados

- **Name**: cluster-setup
- **Version**: 1.0.0
- **Description**: Criação e configuração de clusters AKS otimizados para produção.
- **Owner**: azure-aks
- **Status**: stable

## Inputs

- `cluster_name` — Nome do cluster AKS (ex: aks-prod, aks-staging)
- `resource_group` — Resource Group existente (provisionado via resource-provisioning)
- `location` — Região Azure (ex: eastus)
- `kubernetes_version` — Versão Kubernetes (ex: 1.29, 1.28) — default: latest stable
- `node_pools` — Lista de node pools com configurações (system, user, spot)
- `network_config` — Network plugin (azure/cilium), vnet_subnet_id, service_cidr, dns_service_ip
- `rbac` — `enabled` | `disabled` (default: enabled)
- `managed_identity` — `system_assigned` | `user_assigned` | `none` (default: system_assigned)
- `addons` — Lista de addons (monitoring, http_application_routing, azure_policy)

## Outputs

- `cluster_resource_id` — Azure Resource ID do cluster
- `kubeconfig` — Kubeconfig para acesso (base64 ou file path)
- `cluster_report` — Relatório com configuração, node pools, addons, validação

## Dependencies

- `az aks` — Azure CLI AKS extension
- `kubectl` — Para validação pós-criação
- `resource-provisioning` — Para VNet, Subnet, Key Vault pré-requisitos

## Tools

- `az aks` — `az aks create/update/show/get-credentials/get-versions`
- `kubectl` — `kubectl get nodes`, `kubectl version`, `kubectl cluster-info`
- `az cli` — Para network, identity, addons
- `terminal` — Executar comandos de validação

## Purpose

Criar clusters AKS com configurações de produção (RBAC, network policies, managed identity, auto-scaling) de forma determinística, produzindo um `cluster_report` que pode ser:
- Validado pelo agente L3 azure-aks e L2 SRE
- Promovido para knowledge no memory/knowledge (padrões de cluster)
- Usado como base para rollout-strategies e security-hardening

## When to Use

- Quando receber task envelope INPUT com objective de criar/atualizar cluster AKS
- Quando necessário provisionar cluster com node pools específicos (system, user, spot)
- Para configurar addons essenciais (monitoring, policy)
- Para integrar com Datadog via addon monitoring

## When NOT to Use

- Quando o cluster já existe e só precisa de update de node pool (usar `node-pool-management`)
- Quando a tarefa envolve upgrade de versão Kubernetes (planejar com L2 SRE + L1 CEO)
- Quando a tarefa requer configuração de secrets sem Key Vault (verificar matriz 🔐)

## Procedure

1. **Ler task envelope**: Consultar `contracts/input/task-envelope.md` para entender:
   - Objective preciso (cluster_name, node_pools, network_config)
   - Constraints (versão Kubernetes, região, budget)
   - Skills e tools autorizadas (matriz ✅⚠️🔐)
   - Memory: patterns de cluster anteriores

2. **Validar pré-requisitos**: Verificar se:
   - Resource Group existe
   - VNet e Subnet existem (via resource-provisioning outputs)
   - Key Vault existe para secrets
   - Subscription tem quota para VM sizes solicitados

3. **Criar/Atualizar cluster**:
   - `az aks create` com parâmetros:
     - `--node-vm-size`, `--node-count`, `--enable-cluster-autoscaler`
     - `--network-plugin azure|cilium`, `--vnet-subnet-id`, `--service-cidr`, `--dns-service-ip`
     - `--enable-rbac`, `--enable-managed-identity`
     - `--enable-addons monitoring,azure-policy,http_application_routing`
   - Configurar node pools: system (critical), user (workloads), spot (batch)
   - Configurar `az aks nodepool add` para pools adicionais

4. **Validar pós-criação**:
   - `az aks get-credentials --name $cluster_name --resource-group $rg`
   - `kubectl get nodes -o wide`
   - `kubectl version --short`
   - Verificar se node pools estão Ready e com auto-scaler ativo
   - Verificar addons: `kubectl get pods -n kube-system`

5. **Produzir report**: Gerar `cluster_report` com:
   - `status`: created/updated/failed
   - `cluster_resource_id`: Azure Resource ID
   - `kubernetes_version`: versão provisionada
   - `node_pools`: lista com name, vm_size, count, min/max, mode
   - `network`: plugin, vnet, subnet, service_cidr
   - `addons`: lista de addons habilitados
   - `risks`: risks identificados (ex: cluster sem private cluster)
   - `memory_candidates`: patterns de configuração
   - `improvement_candidates`: skills/rules a propor

## Validation

- Verificar se `az aks show` retorna provisioningState=Succeeded
- Confirmar que todos os node pools estão Ready
- Confirmar que addons essenciais estão running
- Cross-check com `memory/knowledge` — promover learning se padrão recorrente
- Confirmar que cluster_report descreve realidade

## Failure Modes

- **Quota exceeded**: Subscription sem quota para VM size; recomenda-se request quota increase
- **VNet conflict**: Subnet já em uso ou overlap CIDR; recomenda-se validar network_config
- **Version unsupported**: Kubernetes version deprecated; recomenda-se usar latest stable
- **Addon failure**: Monitoring addon falha; recomenda-se verificar Log Analytics workspace

## Examples

### Exemplo 1: Criar cluster AKS produção

```
Input: cluster_name="aks-prod", resource_group="rg-aks-prod", location="eastus",
  node_pools=[{name: "system", vm_size: "Standard_D4s_v3", min: 3, max: 10, mode: "System"},
    {name: "user", vm_size: "Standard_D4s_v3", min: 2, max: 20, mode: "User"},
    {name: "spot", vm_size: "Standard_D4s_v3", min: 0, max: 50, mode: "User", priority: "Spot"}],
  network_config={plugin: "azure", vnet_subnet_id: "/subscriptions/.../subnets/aks-subnet",
    service_cidr: "10.240.0.0/16", dns_service_ip: "10.240.0.10"},
  addons: ["monitoring", "azure-policy"]
Output: cluster_report contendo:
  - status: created
  - cluster_resource_id: /subscriptions/.../resourceGroups/rg-aks-prod/providers/Microsoft.ContainerService/managedClusters/aks-prod
  - kubernetes_version: 1.29.2
  - node_pools: [system(3-10), user(2-20), spot(0-50)]
  - network: {plugin: azure, vnet: vnet-aks, service_cidr: 10.240.0.0/16}
  - addons: [monitoring, azure-policy]
  - risks: ["Cluster público sem private cluster"]
```

### Exemplo 2: Atualizar node pool existente

```
Input: cluster_name="aks-prod", resource_group="rg-aks-prod",
  node_pools=[{name: "user", min: 3, max: 30}]
Output: cluster_report contendo:
  - status: updated
  - node_pools: [user(3-30)]
  - risks: ["Scale-up pode demorar 5-10 min"]
```

## Known Limitations

- Dependente de `az aks` CLI e permissões de Contributor no RG
- Criação de cluster pode demorar 10-20 minutos
- Alguns addons (ex: monitoring) requerem Log Analytics workspace pré-existente
- Upgrade de versão Kubernetes requer planejamento e aprovação separada

## Improvement Criteria

- **Nova skill proposta**: Quando pattern de cluster setup detectado em 4+ tasks
- **Promoção para rule**: Quando configuração de cluster sistêmica (ex: default node sizes)
- **Memory promotion**: Quando aprendizado relevante para arquitetura de clusters

## Changelog

- **1.0.0**: Versão inicial