# SKILL.md - monitor-setup

## Metadados

- **Name**: monitor-setup
- **Version**: 1.0.0
- **Description**: Criação e configuração de monitors, dashboards e alerts no Datadog.
- **Owner**: datadog
- **Status**: stable

## Inputs

- `monitor_type` — `metric` | `log` | `apm` | `composite` | `forecast`
- `query` — Query Datadog (ex: `avg:kubernetes.cpu.usage{cluster:aks-prod} by {pod}`)
- `name` — Nome do monitor
- `message` — Mensagem do alerta (inclui @slack, @pagerduty, runbook URL)
- `tags` — Tags do monitor (ex: `env:prod`, `team:sre`, `service:api`)
- `thresholds` — `{critical: 90, warning: 70, ok: 50}` (para metric monitors)
- `evaluation_delay` — Segundos antes de avaliar (default: 900)
- `notification_policy` — Policy de notificação (no data, renotification interval)

## Outputs

- `monitor_id` — Datadog monitor ID
- `monitor_url` — Link direto para o monitor no Datadog
- `monitor_report` — Relatório com configuração, validação e links

## Dependencies

- `datadog API` — API key + App key
- `integration-setup` — Para integrations Azure/AKS

## Tools

- `datadog.api` — `GET/POST /api/v1/monitor`, `/api/v1/dashboard`
- `datadog.terraform` — Terraform Datadog provider (opcional)
- `filesystem` — Para ler/escrever configs
- `terminal` — Para validação via curl

## Purpose

Criar monitors, dashboards e SLOs no Datadog de forma determinística, produzindo um `monitor_report` que pode ser:
- Validado pelo agente L3 datadog e L2 SRE/QA
- Promovido para knowledge no memory/knowledge (padrões de monitoramento)
- Usado como base para qa-gate e incident-response

## When to Use

- Quando receber task envelope INPUT com objective de criar/atualizar monitor
- Quando necessário monitorar métricas de cluster AKS (CPU, memory, pods)
- Para criar alerts de APM (latency, error rate, throughput)
- Para definir SLOs/SLIs baseados em métricas

## When NOT to Use

- Quando o monitor já existe e só precisa de ajuste de threshold (usar update)
- Quando a tarefa envolve configuração de integração Azure/AKS (usar `integration-setup`)
- Quando não há API key Datadog configurada (verificar `GOVERNANCE.md` §01)

## Procedure

1. **Ler task envelope**: Consultar `contracts/input/task-envelope.md` para entender:
   - Objective preciso (monitor_type, query, thresholds)
   - Constraints (tags obrigatórias, notification policy)
   - Skills e tools autorizadas (matriz ✅⚠️🔐)
   - Memory: patterns de monitoramento anteriores

2. **Validar pré-requisitos**:
   - API key + App key válidas (via env vars ou secret manager)
   - Integration Azure/AKS ativa (para métricas kubernetes.*)
   - Métrica/query existe no Datadog (testar query via API)

3. **Criar/Atualizar monitor**:
   - POST `/api/v1/monitor` com payload:
     ```json
     {
       "type": "metric alert",
       "query": "avg(last_5m):avg:kubernetes.cpu.usage{cluster:aks-prod} by {pod} > 90",
       "name": "AKS Prod - High CPU Usage",
       "message": "CPU usage > 90% on pod {{pod.name}}. @slack-sre-alerts Runbook: https://wiki/runbook/cpu",
       "tags": ["env:prod", "team:sre", "service:aks"],
       "options": {
         "thresholds": {"critical": 90, "warning": 70},
         "evaluation_delay": 900,
         "notify_no_data": false,
         "renotification_interval": 3600
       }
     }
     ```
   - Para SLO: POST `/api/v1/slo` com SLI query e target

4. **Validar**:
   - GET `/api/v1/monitor/{monitor_id}` para confirmar criação
   - Testar query manualmente no Datadog UI
   - Verificar se tags obrigatórias presentes

4. **Produzir report**: Gerar `monitor_report` com:
   - `status`: created/updated/failed
   - `monitor_id`: Datadog monitor ID
   - `monitor_url`: Link direto
   - `query`: Query usada
   - `thresholds`: Thresholds configurados
   - `tags`: Tags aplicadas
   - `risks`: Risks identificados (ex: monitor sem notification)
   - `memory_candidates`: Patterns de monitor
   - `improvement_candidates`: Skills/rules a propor

## Validation

- Verificar se monitor_id retornado e monitor acessível via URL
- Confirmar que query retorna dados esperados no Datadog
- Confirmar que tags obrigatórias (env, team, service) presentes
- Cross-check com `memory/knowledge` — promover learning se padrão recorrente
- Confirmar que monitor_report descreve realidade

## Failure Modes

- **Invalid query**: Query sintaxe inválida ou métrica não existe; recomenda-se testar query primeiro
- **API auth failure**: API key/App key inválidas; recomenda-se rotacionar keys
- **Threshold mismatch**: Thresholds não fazem sentido para métrica; recomenda-se revisar baseline
- **Notification gap**: Monitor sem notification policy; recomenda-se adicionar @slack/@pagerduty

## Examples

### Exemplo 1: Monitor de CPU alta no AKS

```
Input: monitor_type="metric", query="avg(last_5m):avg:kubernetes.cpu.usage{cluster:aks-prod} by {pod}",
  name="AKS Prod - High CPU Usage",
  message="CPU > 90% on {{pod.name}}. @slack-sre-alerts Runbook: https://wiki/runbook/cpu",
  tags=["env:prod", "team:sre", "service:aks"],
  thresholds={critical: 90, warning: 70}
Output: monitor_report contendo:
  - status: created
  - monitor_id: 12345678
  - monitor_url: https://app.datadoghq.com/monitors/12345678
  - thresholds: {critical: 90, warning: 70}
  - risks: ["Threshold pode precisar ajuste após baseline"]
```

### Exemplo 2: SLO de disponibilidade

```
Input: monitor_type="slo", name="API Availability SLO",
  sli_query="sum:trace.http.status{service:api,env:prod,status:2xx} / sum:trace.http.status{service:api,env:prod}",
  target=99.9, timeframe="30d"
Output: monitor_report contendo:
  - status: created
  - monitor_id: 87654321
  - slo_target: 99.9%
  - current_sli: 99.95%
  - risks: ["SLO novo, validar baseline"]
```

### Exemplo 3: Monitor de log error

```
Input: monitor_type="log", query="source:kubernetes service:api status:error",
  name="AKS Prod - API Errors in Logs",
  message="Error logs detected in API. @slack-sre-alerts",
  tags=["env:prod", "team:sre", "service:api"]
Output: monitor_report contendo:
  - status: created
  - monitor_id: 11223344
  - query: "source:kubernetes service:api status:error"
  - risks: ["Pode gerar ruído se error logs esperados"]
```

## Known Limitations

- Dependente de Datadog API key + App key válidas
- Métricas kubernetes.* requerem integration AKS ativa
- Alguns tipos de monitor (forecast, composite) mais complexos
- Rate limit API: 300 requests/minute

## Improvement Criteria

- **Nova skill proposta**: Quando pattern de monitor detectado em 4+ tasks
- **Promoção para rule**: Quando monitor obrigatório se torna padrão (ex: CPU/memory em todo cluster)
- **Memory promotion**: Quando aprendizado relevante para arquitetura de observability

## Changelog

- **1.0.0**: Versão inicial