# SKILL.md - pipeline-yaml

## Metadados

- **Name**: pipeline-yaml
- **Version**: 1.0.0
- **Description**: Criação e refatoração de pipelines YAML Azure DevOps para builds, tests e releases.
- **Owner**: azure-devops
- **Status**: stable

## Inputs

- `pipeline_type` — `build` | `test` | `release` (default: build)
- `target_branch` — Branch where the pipeline triggers (default: main)
- `trigger_config` — Optional trigger spec (branch filter, cron, manual)
- `stages` — List of stages to include (e.g. build, test, deploy)
- `service_connection` — Azure DevOps service connection name (optional)

## Outputs

- `pipeline_yaml` — Validated Azure DevOps pipeline YAML
- `pipeline_report` — Report with stages, triggers, variables, and validation status

## Dependencies

- `az devops` — Azure DevOps CLI (az devops pipeline create/update)
- `github` — For repo/branch validation
- `filesystem` — For reading/writing YAML files

## Tools

- `az devops` — Create, update, list pipelines
- `github.read` — Validate branch, repo, and existing pipeline YAML
- `github.write` — Commit pipeline YAML to repo
- `filesystem.read` — Read existing pipeline YAML
- `filesystem.write` — Write pipeline YAML
- `terminal` — Run `az devops pipeline show`, `az devops pipeline validate`

## Purpose

Criar ou refatorar pipelines YAML Azure DevOps de forma determinística, produzindo um `pipeline_report` que pode ser:
- Validado pelo agente L3 azure-devops
- Promovido para knowledge no memory/knowledge (padrões de pipeline)
- Usado como base para futuras skills de pipeline (ex: `pipeline-orchestration`)

## When to Use

- Quando receber um task envelope INPUT com objective de criar/atualizar pipeline
- Quando necessário adicionar etapas de build, test ou release em pipeline existente
- Para refatorar pipelines YAML que violam convenções do projeto
- Para migrar pipelines clássicas para YAML

## When NOT to Use

- Quando a task requer criação de service connection (usar `repo-management` ou `feed-management` primeiro)
- Quando a tarefa envolve permissões de secrets (verificar `GOVERNANCE.md` §01 matriz ✅⚠️🔐)
- Quando a tarefa requer configuração de MCP servers (needs L1 approval)

## Procedure

1. **Ler task envelope**: Consultar `contracts/input/task-envelope.md` para entender:
   - Objective preciso (pipeline_type, stages, target_branch)
   - Constraints e boundaries
   - Skills e tools autorizadas (matriz ✅⚠️🔐 de GOVERNANCE.md)
   - Memory que pode ser consultada

2. **Validar contexto**: Utilizar `github.read` e `az devops pipeline list` para entender:
   - Repo e branch existentes
   - Pipelines existentes no mesmo project
   - Conventions de YAML usadas no projeto

3. **Escrever pipeline YAML**: Criar YAML com:
   - `trigger:` com branch filter
   - `pool:` com vmImage
   - `stages:` com jobs e steps
   - `variables:` com environment-specific values
   - `steps:` com script/bash/task steps
   - Usar `$(Build.SourceBranch)`, `$(Build.BuildId)` etc.

4. **Validar**: Cross-check com:
   - Conformance a YAML syntax
   - Conventions do projeto (ex: `vmImage: ubuntu-latest`, `displayName`)
   - Existing pipelines não quebrados
   - `az devops pipeline validate` (se disponível)

5. **Produzir report**: Gerar `pipeline_report` com:
   - `status`: created/updated/failed
   - `pipeline_id`: ID do pipeline criado/atualizado
   - `stages`: lista de stages incluídos
   - `triggers`: trigger config
   - `variables`: variáveis definidas
   - `risks`: risks identificados (ex: pipeline em prod sem QA gate)
   - `memory_candidates`: padrões de pipeline para promover
   - `improvement_candidates`: skills/rules a propor

## Validation

- Verificar se YAML é válido (parse YAML)
- Confirmar que triggers respeitam target_branch
- Confirmar que stages seguem convenções do projeto
- Cross-check com `memory/knowledge` — promover learning se padrão de pipeline for recorrente
- Confirmar que o pipeline_report descreve realidade (não suposições)

## Failure Modes

- **YAML syntax error**: Pipeline YAML inválido; recomenda-se usar `yaml.safe_load` e corrigir
- **Invalid trigger**: Trigger não respeita target_branch; recomenda-se corrigir trigger config
- **Missing stages**: Pipeline sem etapas críticas (ex: sem test stage); recomenda-se adicionar stages
- **Authority overreach**: Pipeline tentando modify `GOVERNANCE.md` ou hierarquia; recomenda-se propor mudança via `proposals/`

## Examples

### Exemplo 1: Criar pipeline build para Node.js

```
Input: pipeline_type="build", target_branch="main", stages=["build","test"]
Output: pipeline_report contendo:
  - status: created
  - pipeline_id: BUILD-001
  - stages: [build, test]
  - triggers: { branches: [main] }
  - variables: { NODE_ENV: production }
  - risks: ["Pipeline em prod sem QA gate"]
  - memory_candidates: [type: learning, description: "Projeto usa vmImage: ubuntu-latest"]
```

### Exemplo 2: Refatorar pipeline existente

```
Input: pipeline_type="build", target_branch="main", stages=["build","test","deploy"]
Output: pipeline_report contendo:
  - status: updated
  - pipeline_id: BUILD-002
  - stages: [build, test, deploy]
  - triggers: { branches: [main], paths: exclude [docs/*] }
  - risks: ["Deploy stage em prod requer QA gate"]
```

## Known Limitations

- Dependente de `az devops` CLI e permissões do service connection
- Pode não cobrir edge cases de pipelines complexas (ex: matrix builds, parallel stages)
- Requer acesso a Azure DevOps (L3 tools)

## Improvement Criteria

- **Nova skill proposta**: Quando pattern de pipeline detectado em 4+ tasks (GOVERNANCE.md §02.4)
- **Promoção para rule**: Quando pipeline pattern sistêmico impacta múltiplas tarefas
- **Memory promotion**: Quando aprendizado relevante para arquitetura de pipelines

## Changelog

- **1.0.0**: Versão inicial