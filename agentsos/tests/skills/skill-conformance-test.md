# Test: SKILL.md Conformance

## Teste: conformidade de SKILL.md

### Verificações Gerais

1. **Metadados Obrigatórios**: `name`, `version`, `description`, `owner`, `status` presentes
2. **Input/Output**: `inputs` e `outputs` listadas com descriptions
3. **Dependencies**: `dependencies` listados com names
4. **Tools**: `tools` listados com descriptions

### Verificações por Section

5. **Purpose**: section presente e não-vazia
6. **When to Use**: section presente com exemplos
7. **When NOT to Use**: section presente com exemplos
8. **Procedure**: section com steps listadas
9. **Validation**: section com rules listadas
10. **Failure Modes**: section com examples
11. **Known Limitations**: section presente
12. **Improvement Criteria**: section com criteria listadas
13. **Changelog**: section presente

### Teste Específico por Skill

#### research/SKILL.md

- Purpose focused on research/analysis
- When-to-use scenarios de pesquisa
- When-NOT-to-use evita duplicar research já no ai-memory

#### coding/SKILL.md

- Purpose focused on development tasks
- When-to-use scenarios de implementação
- Procedure steps orientadas a código

#### documentation/SKILL.md

- Purpose focused on writing/editing docs
- Procedure steps orientadas a markdown

#### session-handoff/SKILL.md

- Purpose focused on handoff entre sessões/agents
- Inputs estruturados de handoff

## Validação Automatizada

Script que verifica todos os 13 requisitos acima em todos os SKILL.md files.