# SKILL.md - documentation

## Metadados

- **Name**: documentation
- **Version**: 1.0.0
- **Description**: Skill de escrita e manutenção de documentação — docs, READMEs, arquitetura, guias.
- **Owner**: documentation
- **Status**: stable

## Inputs

- `task_id` — ID da tarefa referenciando o contrato INPUT em `contracts/input/`
- `objective` — Descrição do que documentar
- `context` — Contexto adicional (qual documento, qual parte do sistema)

## Outputs

- `documentation_report` — Relatório estruturado com o novo/atualizado documento

## Dependencies

- `filesystem` — Leitura/escrita de arquivos markdown
- `github` — Para docs que fazem parte do repository

## Tools

- `filesystem.read` — Ler docs existentes, markdown files
- `filesystem.write` — Escrever/atualizar docs, READMEs
- `github.read` — Ler docs no repository remoto
- `github.write` — Commitar docs no repository
- `terminal` — Build commands quando necessário (ex: mkdocs, doc generation)

## Purpose

Escrever, atualizar ou manter documentação do projeto de forma estruturada, produzindo um `documentation_report` que possa ser:
- Consumido por outros agents
- Versionado no repository
- Promovido para conhecimento no memory/knowledge
- Servir de base para future skills ou onboarding

## When to Use

- Quando receber um task envelope INPUT com objective de documentação
- Para criar/atualizar README, arquitetural docs, guides
- Para documentar decisions arquiteturais
- Para onboarding de novos desenvolvedores

## When NOT to Use

- Quando a task requer pesquisa extensa antes da escrita (usar `research` skill primeiro)
- Quando a documentação requer conhecimento de código complexo (consultar `developer` ou fazer code review)
- Quando a documentação requer decisão de arquitetura (consultar `CEO` ou `GOVERNANCE.md`)
- Quando mudanças na docs requerem approval de governança (verificar matriz ✅⚠️🔐)

## Procedure

1. **Ler task envelope**: Consultar `contracts/input/task-envelope.md` para entender:
   - Objective preciso
   - Constraints e boundaries
   - Skills e tools autorizadas
   - Memory que pode ser consultada
2. **Explorar docs existentes**: Utilizar `filesystem.read` e `github.read` para entender:
   - Estrutura de docs do projeto
   - Docs existentes relacionados
   - Formatting conventions
3. **Escrever documentação**: Criar/atualizar docs conforme constraints, following project conventions
4. **Validar**: Cross-check com:
   - Conformance a GOVERNANCE.md authority limits
   - Existing docs consistency
   - Formatting conventions
5. **Produzir report**: Gerar `documentation_report` com:
   - `status`: completed/partial
   - `changes`: files modificados/criados + descrição succinta
   - `validation`: conformance check results
   - `risks`: risks identificados
   - `memory_candidates`: aprendizados para promover
   - `improvement_candidates`: docs a melhorar, skills a criar

## Validation

- Verificar se todas as constraints do task envelope foram respeitadas
- Confirmar que a documentação segue conventions do projeto
- Cross-check com `memory/knowledge` — promover learning se aplicável
- Confirmar que o document_report responde à necessidade original

## Failure Modes

- **Constraint violation**: Documentation written outside boundaries autorizadas; recomenda-se revisar constraints e refatorar
- **Formatting errors**: Docs não seguindo conventions; recomenda-se ajustar formatting
- **Authority overreach**: Documentation tentando modificar GOVERNANCE.md ou hierarquia; recomenda-se propoer mudança via `proposals/`

## Examples

### Exemplo 1: Criar README

```
Input: task_id="TASK-2026-XXX", objective="Criar README inicial do projeto"
Output: documentation_report contendo:
  - status: completed
  - changes: [README.md - criado com estrutura project/, agents/, skills/, memory/, contracts/, workflows/, templates/, proposals/, tests/]
  - validation: conformance check passed
  - risks: baixo
  - memory_candidates: [type: learning, description: "Estrutura de docs definida; promover para policies se necessário"]
  - improvement_candidates: none
```

### Exemplo 2: Atualizar arquitetural doc

```
Input: task_id="TASK-2026-XXX", objective="Atualizar ARCHITECTURE.md com nova hierarquia L0-L5"
Output: documentation_report contendo:
  - status: completed
  - changes: [docs/ARCHITECTURE.md - atualizada com hierarquia L0-L5, governance policies]
  - validation: conformance check passed, cross-checked with GOVERNANCE.md
  - risks: baixo
  - memory_candidates: [type: learning, description: "Nova hierarquia documentada; promover awareness via CEO announcement"]
  - improvement_candidates: none
```

## Known Limitations

- Dependente de conventions estabelecidas do projeto
- Pode não cobrir todos os tipos de documentação (ex: API docs, user guides podem requerer skills específicas)
- Requires acesso a filesystem e github (L2 tools)

## Improvement Criteria

- **Nova skill proposta**: Quando pattern de docs missing detectado em 4+ tasks (GOVERNANCE.md §02.4)
- **Promoção para rule**: Quando gaps de documentation sistêmicos identificados impactando múltiplos domains
- **Memory promotion**: Quando aprendizado relevante para conhecimento do projeto

## Changelog

- **1.0.0**: Versão inicial