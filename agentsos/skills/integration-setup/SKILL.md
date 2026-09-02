# SKILL.md - integration-setup

## Metadados

- **Name**: integration-setup
- **Version**: 1.0.0
- **Description**: Configuração de integrações Datadog com Azure, AKS e serviços externos.
- **Owner**: datadog
- **Status**: stable

## Inputs

- `integration_type` — `azure` | `kubernetes` | `aks` | `docker` | `prometheus` | `custom`
- `config` — Configuração específica da integração (JSON)
- `api_key` — Datadog API key (ou reference a secret)
- `app_key` — Datadog App key (ou reference a secret)
- `resource_ids` — Para Azure: lista de resource IDs a monitorar

## Outputs

- `integration_id` — Datadog integration ID
- `integration_status` — Status da integração (connected, error, pending)
- `integration_report` — Relatório com configuração, validação e métricas disponíveis

## Dependencies

- `datadog API` — API key + App key
- `monitor-setup` — Para criar monitors baseados nas métricas da integração

## Tools

- `datadog.api` — `GET/POST /api/v1/integration`, `/api/v1/integration/azure`, `/api/v1/integration/kubernetes`
- `az cli` — Para validar recursos Azure
- `kubectl` — Para validar cluster AKS
- `filesystem` — Para ler/escrever configs

## Purpose

Configurar integrações Datadog para coletar métricas, logs e traces de Azure, AKS e outros serviços, produzindo um `integration_report` que pode ser:
- Validado pelo agente L3 datadog e L2 SRE
- Promovido para knowledge no memory/knowledge (padrões de integração)
- Usado como base para monitor-setup e slo-management

## When to Use

- Quando receber task envelope INPUT com objective de configurar integração
- Para conectar subscription Azure ao Datadog (métricas de recursos)
- Para instalar Datadog Agent no AKS (DaemonSet + Cluster Agent)
- Para integrar Prometheus/OpenTelemetry custom metrics

## When NOT to Use

- Quando a integração já existe e está healthy (validar status primeiro)
- Quando não há permissões para instalar Agent no cluster (verificar matriz)
- Quando a tarefa envolve configuração de secrets sem Key Vault

## Procedure

1. **Ler task envelope**: Consultar `contracts/input/task-envelope.md` para entender:
   - Objective preciso (integration_type, config)
   - Constraints (permissions, network, tags)
   - Skills e tools autorizadas (matriz ✅⚠️🔐)
   - Memory: patterns de integração anteriores

2. **Validar pré-requisitos por tipo**:

   **Azure**:
   - Subscription ID, Tenant ID, Client ID, Client Secret
   - Permissões: Reader + Monitoring Reader no subscription
   - Resource IDs a monitorar (ou all)

   **Kubernetes/AKS**:
   - Cluster AKS acessível (`kubectl cluster-info`)
   - Permissões para criar DaemonSet, ClusterRole, ClusterRoleBinding
   - Helm 3 disponível (para Datadog Helm chart)

   **Prometheus**:
   - Prometheus endpoint acessível
   - Métricas expostas em formato Prometheus

3. **Configurar integração**:

   **Azure**:
   - POST `/api/v1/integration/azure` com:
     ```json
     {
       "tenant_name": "my-tenant",
       "client_id": "xxx",
       "client_secret": "xxx",
       "resource_ids": ["/subscriptions/.../resourceGroups/rg-aks-prod"]
     }
     ```

   **AKS (via Helm)**:
   - `helm repo add datadog https://helm.datadoghq.com`
   - `helm install datadog datadog/datadog --set datadog.apiKey=$API_KEY --set datadog.appKey=$APP_KEY --set datadog.site=datadoghq.com --set clusterAgent.enabled=true --set clusterAgent.conf.clusterName=aks-prod`
   - Validar: `kubectl get pods -n datadog`

   **Kubernetes (genérico)**:
   - Similar ao AKS mas sem clusterAgent specifics

4. **Validar integração**:
   - GET `/api/v1/integration/{integration_type}` para status
   - Verificar métricas chegando: `kubernetes.cpu.usage`, `azure.vm.percentage_cpu`, `prometheus.*`
   - Verificar logs chegando: `source:kubernetes`, `source:azure`

4. **Produzir report**: Gerar `integration_report` com:
   - `status`: connected/error/pending
   - `integration_id`: Datadog integration ID
   - `integration_type`: tipo configurado
   - `metrics_available`: lista de métricas detectadas
   - `logs_available`: lista de sources de logs
   - `traces_available`: boolean (se APM enabled)
   - `risks`: risks identificados (ex: integration sem tags)
   - `memory_candidates`: patterns de integração
   - `improvement_candidates`: skills/rules a propor

## Validation

- Verificar se integration_status = connected
- Confirmar que métricas esperadas aparecem no Datadog (query test)
- Confirmar que logs/traces chegam se configurados
- Cross-check com `memory/knowledge` — promover learning se padrão recorrente
- Confirmar que integration_report descreve realidade

## Failure Modes

- **Auth failure**: Credenciais Azure/Datadog inválidas; recomenda-se rotacionar
- **Permission denied**: Sem permissão para criar resources no cluster/subscription; recomenda-se request access
- **Network blocked**: Cluster/recursos sem acesso ao Datadog intake; recomenda-se verificar firewall/VNet
- **Agent crash**: Datadog Agent pods crashlooping; recomenda-se verificar logs e resources limits

## Examples

### Exemplo 1: Integração Azure

```
Input: integration_type="azure",
  config={tenant_id: "xxx", client_id: "xxx", client_secret: "xxx",
    resource_ids: ["/subscriptions/.../resourceGroups/rg-aks-prod"]}
Output: integration_report contendo:
  - status: connected
  - integration_id: azure_12345
  - integration_type: azure
  - metrics_available: ["azure.vm.percentage_cpu", "azure.storage.used_capacity", "aks.*"]
  - risks: ["Client secret expira em 90 dias"]
```

### Exemplo 2: Integração AKS via Helm

```
Input: integration_type="aks",
  config={cluster_name: "aks-prod", api_key: "xxx", app_key: "xxx",
    cluster_agent: true, logs_enabled: true, apm_enabled: true}
Output: integration_report contendo:
  - status: connected
  - integration_id: kubernetes_67890
  - integration_type: aks
  - metrics_available: ["kubernetes.cpu.usage", "kubernetes.memory.usage", "kubernetes.pods.running"]
  - logs_available: ["source:kubernetes"]
  - traces_available: true
  - risks: ["Agent DaemonSet usa 100m CPU / 256Mi memory por node"]
```

## Known Limitations

- Dependente de Datadog API key + App key válidas
- Azure integration requer permissões Reader + Monitoring Reader
- AKS integration via Helm requer cluster admin permissions
- Algumas métricas Azure têm delay de 5-15 minutos

## Improvement Criteria

- **Nova skill proposta**: Quando pattern de integração detectado em 4+ tasks
- **Promoção para rule**: Quando integração obrigatória se torna padrão (ex: Azure em toda subscription)
- **Memory promotion**: Quando aprendizado relevante para arquitetura de observability

## Changelog

- **1.0.0**: Versão inicial