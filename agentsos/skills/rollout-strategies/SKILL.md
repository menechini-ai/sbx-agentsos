# SKILL.md - rollout-strategies

## Metadados

- **Name**: rollout-strategies
- **Version**: 1.0.0
- **Description**: Estratégias de rollout para workloads no AKS (rolling, canary, blue-green).
- **Owner**: azure-aks
- **Status**: stable

## Inputs

- `deployment_name` — Nome do Deployment/StatefulSet
- `namespace` — Kubernetes namespace
- `strategy` — `rolling` | `canary` | `blue-green` (default: rolling)
- `image` — Nova image tag a deployar
- `canary_weight` — Para canary: peso inicial do canary (0-100, default: 10)
- `canary_steps` — Para canary: array de pesos progressivos (ex: [10, 30, 50, 100])
- `blue_green_service` — Para blue-green: nome do Service que troca selector
- `health_checks` — Lista de checks (readiness, liveness, custom http endpoint)
- `rollback_on_failure` — `true` | `false` (default: true)

## Outputs

- `rollout_status` — Status do rollout (in_progress, completed, failed, rolled_back)
- `current_revision` — Revision atual do deployment
- `rollout_report` — Relatório com estratégia, steps, validações, métricas

## Dependencies

- `kubectl` — Para rollout, patch, rollback
- `cluster-setup` — Cluster deve estar healthy

## Tools

- `kubectl` — `kubectl rollout`, `kubectl set image`, `kubectl patch`, `kubectl rollout undo`
- `az aks` — Para get-credentials
- `terminal` — Executar comandos de validação

## Purpose

Executar rollouts controlados de workloads no AKS com validação de saúde em cada step, produzindo um `rollout_report` que pode ser:
- Validado pelo agente L3 azure-aks e L2 SRE
- Promovido para knowledge no memory/knowledge (padrões de rollout)
- Usado como base para qa-gate e incident-response

## When to Use

- Quando receber task envelope INPUT com objective de deployar nova versão
- Quando necessário reduzir risco de deploy (canary/blue-green)
- Para automatizar rollback em caso de health check failure
- Para integrar com pipeline-yaml (stage de deploy)

## When NOT to Use

- Quando o cluster não está healthy (verificar `cluster_report` primeiro)
- Quando a tarefa envolve schema migration de database (planejar separadamente)
- Quando a imagem não existe no registry (validar antes)

## Procedure

1. **Ler task envelope**: Consultar `contracts/input/task-envelope.md` para entender:
   - Objective preciso (deployment, strategy, image)
   - Constraints (downtime tolerado, health checks obrigatórios)
   - Skills e tools autorizadas (matriz ✅⚠️🔐)
   - Memory: patterns de rollout anteriores

2. **Validar pré-requisitos**:
   - Cluster accessible: `kubectl cluster-info`
   - Deployment existe: `kubectl get deployment $deployment_name -n $namespace`
   - Imagem existe no registry (ACR/GHCR/Docker Hub)

3. **Executar rollout por estratégia**:

   **Rolling (padrão)**:
   - `kubectl set image deployment/$deployment_name $container=$image -n $namespace`
   - `kubectl rollout status deployment/$deployment_name -n $namespace --timeout=10m`

   **Canary**:
   - Criar canary deployment com `replicas: 1` e label `version: canary`
   - Ajustar Service para incluir ambos (stable + canary)
   - Loop sobre `canary_steps`:
     - Escalar canary para peso do step
     - Aguardar `health_checks` passarem (readiness + custom endpoint)
     - Se falhar: rollback para stable (scale canary para 0)
   - Se todos passam: promover canary a stable, remover stable antigo

   **Blue-Green**:
   - Criar green deployment paralelo (mesmo spec, nova image)
   - Validar green com `health_checks`
   - Se passa: patch Service para apontar para green (`selector: version=green`)
   - Se falha: manter service no blue, deletar green
   - Após confirmação: deletar blue antigo

4. **Pós-rollout**:
   - Verificar `kubectl rollout status`
   - Executar `health_checks` finais
   - Capturar métricas: latency, error rate, throughput (se Datadog integrado)

5. **Produzir report**: Gerar `rollout_report` com:
   - `status`: completed/failed/rolled_back
   - `strategy`: estratégia usada
   - `steps_executed`: array de steps com timestamp, status, métricas
   - `current_revision`: revision do deployment
   - `rollback_performed`: boolean
   - `risks`: risks identificados
   - `memory_candidates`: patterns de rollout
   - `improvement_candidates`: skills/rules a propor

## Validation

- Verificar se rollout status é completed (ou rolled_back se failure)
- Confirmar que `health_checks` passam em cada step
- Confirmar que métricas não degradam (se Datadog disponível)
- Cross-check com `memory/knowledge` — promover learning se padrão recorrente
- Confirmar que rollout_report descreve realidade

## Failure Modes

- **Health check failure**: Readiness/liveness falha; rollback automático se `rollback_on_failure=true`
- **Image pull error**: Imagem não existe ou sem permissão; rollback
- **Timeout**: Rollout demora > timeout; rollback
- **Service mismatch**: Blue-green service selector não atualiza; investigar endpoints

## Examples

### Exemplo 1: Rolling update padrão

```
Input: deployment_name="api", namespace="production", strategy="rolling",
  image="myregistry.azurecr.io/api:v1.2.3"
Output: rollout_report contendo:
  - status: completed
  - strategy: rolling
  - steps_executed: [{step: "set_image", status: "ok"}, {step: "rollout_status", status: "ok"}]
  - current_revision: 5
  - rollback_performed: false
  - risks: ["Sem health checks customizados"]
```

### Exemplo 2: Canary com steps progressivos

```
Input: deployment_name="api", namespace="production", strategy="canary",
  image="myregistry.azurecr.io/api:v1.2.3",
  canary_steps=[10, 30, 50, 100],
  health_checks=["readiness", "http:/healthz"]
Output: rollout_report contendo:
  - status: completed
  - strategy: canary
  - steps_executed: [
    {step: "canary_10%", status: "ok", metrics: {latency_p99: "120ms", error_rate: "0.01%"}},
    {step: "canary_30%", status: "ok", metrics: {latency_p99: "130ms", error_rate: "0.02%"}},
    {step: "canary_50%", status: "ok", metrics: {latency_p99: "125ms", error_rate: "0.01%"}},
    {step: "canary_100%", status: "ok"}]
  - rollback_performed: false
```

### Exemplo 3: Blue-green

```
Input: deployment_name="api", namespace="production", strategy="blue-green",
  image="myregistry.azurecr.io/api:v1.2.3",
  blue_green_service="api-service",
  health_checks=["readiness", "http:/healthz", "smoke_test"]
Output: rollout_report contendo:
  - status: completed
  - strategy: blue-green
  - steps_executed: [
    {step: "create_green", status: "ok"},
    {step: "validate_green", status: "ok"},
    {step: "switch_service", status: "ok"}]
  - rollback_performed: false
```

## Known Limitations

- Dependente de `kubectl` e cluster healthy
- Canary requer Service com selector que inclua ambos (ex: `app=api` sem version)
- Blue-green requer 2x recursos durante transição
- Não gerencia database migrations (responsabilidade do Dev)

## Improvement Criteria

- **Nova skill proposta**: Quando pattern de rollout detectado em 4+ tasks
- **Promoção para rule**: Quando estratégia padrão se torna obrigatória (ex: canary para prod)
- **Memory promotion**: Quando aprendizado relevante para arquitetura de deploy

## Changelog

- **1.0.0**: Versão inicial