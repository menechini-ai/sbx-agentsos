---
name: slo-management
description: Define, track e gerenciar Service Level Objectives (SLOs) e Service Level Indicators (SLIs) para ambientes cloud e Kubernetes, incluindo alertas, error budgets e relatórios de confiabilidade.
version: 1.0.0
tags: [slo, sli, reliability, observability, datadog, cloud, kubernetes]
---
# SLO Management

## Purpose

Define, track e gerenciar Service Level Objectives (SLOs) e Service Level Indicators (SLIs) para ambientes cloud e Kubernetes, incluindo alertas, error budgets e relatórios de confiabilidade.

## When to Use

- Task envelope INPUT contém objective de configuração ou review de SLOs/SLIs
- Configuração de alertas e dashboards no Datadog/Prometheus/Grafana
- Review de error budgets antes de deploy em produção
- Criação de relatórios de confiabilidade para stakeholders

## When NOT to Use

- Tarefa envolve apenas deploy de aplicação (usar `agentos-build`)
- Configuração de apenas métricas application-level (usar `monitor-setup`)
- Otimização de infraestrutura (usar `resource-provisioning`)

## Procedure

### 1. Define SLIs (Service Level Indicators)

```bash
# Exemplo: Latência de API
SLI = (
  metric = "http_request_duration_seconds_bucket"
  metric_kind = "cumulative"
  aggregation = "histogram"
  task = "request_duration_seconds"
  success_criteria = (
    threshold = 0.5
    success_ratio = 0.99
    description = "99% of requests must complete within 500ms"
  )
)

# Exemplo: Disponibilidade
SLI = (
  metric = "kubernetes_deployment_available_replicas"
  metric_kind = "gauge"
  aggregation = "last_value"
  task = "available_replicas"
  success_criteria = (
    threshold = 3
    success_ratio = 1.0
    description = "All 3 replicas must be available"
  )
)
```

### 2. Define SLOs (Service Level Objectives)

```yaml
# Exemplo: Disponibilidade 99.9% mensal
slo:
  name: availability
  indicator: kubernetes_deployment_available_replicas
  window: 30d
  target: "0.999"
  error_budget: 0.1%  # 0.1% of time can have unavailable replicas
  calendar: monthly

# Exemplo: Latência 95th percentile < 500ms
slo:
  name: latency
  indicator: http_request_duration_seconds_95th_percentile
  window: 1h
  target: "0.5"
  error_budget: 0.5  # 500ms threshold exceeded 0.5% of the time
  calendar: hourly
```

### 3. Alertas e Dashboards

```bash
# Datadog alert creation
datadot alert create \
  --name "SLO breach: latency" \
  --query "slo.latency.breach" \
  --message "95th percentile latency exceeded 500ms threshold" \
  --tags environment:prod,service:api

# Prometheus alert rule
apiVersion: monitoring.coreos.com/v1
kind: Alertmanagerspec
spec:
  groups:
  - name: sla
    rules:
    - alert: SLOBreach
      expr | slo.latency.breach > 0
      for: 10m
      labels:
        severity: critical
      annotations:
        summary: "SLO latency breach detected"
        description: "95th percentile latency has exceeded the threshold for 10 minutes"
```

### 4. Error Budget Management

```yaml
# Error budget consumption
error_budget:
  budget: 0.1  # 0.1 = 10% of time can have SLO breach
  spent: 0.03  # 0.03 = 3% já consumido
  burn_rate: 0.01  # 0.01 por hora/dia
  replenishment:  # replenishment policy
    mode: linear
    rate: 0.001  # 0.1% por dia

# Decision boundaries
if burned > 0.5:
  # HIGH risk: bloquear deploy em produção
  require: CEO + L2 approval
elif burned > 0.2:
  # MEDIUM risk: review required
  require: L2 SRE approval
else:
  # LOW risk: deploy liberado
  auto_approve: true
```

## Validation

- Verificar que SLIs são medidos corretamente via Prometheus/Datadog
- Confirmar que SLOs têm janelas de tempo definidas (SLI window)
- Validar que error budgets são calculados corretamente
- Cross-check com `memory/knowledge` — promover patterns de reliability se recorrentes
- Executar `slo` queries no Prometheus/Datadog para validação

## Failure Modes

- **SLI misconfiguration**: Métrica errada ou agregação incorreta; recomenda-se documentar a definição exata
- **SLO irrealista**: Target muito ambiciosa; recomenda-se começar com error budget maior e diminuir ao longo do tempo
- **Error budget muito restritivo**: Bloqueia deploy necessário; recomenda-se revisar targets com stakeholders
- **Alerta falsos positivos**: Configuração incorreta de thresholds; revisar alertas e ajustar thresholds

## Known Limitations

- Datadog SLOs requer Datadog Plan ≥ Service Leve
- Prometheus SLOs requer Prometheus com módulo de SLOs habilitado
- Error budget policies variam por organização e indústria
- Janelas de tempo curtas (< 1h) podem ter ruído estatístico

## Examples

### Exemplo 1: SLO de disponibilidade mensal

```
Input: service_name="api-platform", window="30d", target="0.999"
Output: SLO configurado, dashboard criado, error budget inicial
```

### Exemplo 2: Alertas de latência para equipe SRE

```
Input: service_name="api-gateway", threshold="500ms", window="1h"
Output: alerta configurado no Datadog, notification channel acionado
```

## Improvement Criteria

- **Nova skill proposta**: Quando pattern de SLO/SLI detectado em 4+ tasks
- **Promoção para rule**: Quando configuração de SLO/SLI sistêmica (ex: default SLO profile)
- **Memory promotion**: Quando aprendizado relevante para confiabilidade do sistema

## Changelog

- **1.0.0**: Versão inicial