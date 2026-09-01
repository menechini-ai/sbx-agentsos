# Template: Decision Entry

## Formato Padrão

```
decision_id: DEC-2026-XXXX
date: {{date}}
agent: {{agent_name}}
status: {{status}}  # accepted, rejected, superseded

context:
  - "{{context_point_1}}"
  - "{{context_point_2}}"

decision:
  - "{{decision_point_1}}"
  - "{{decision_point_2}}"

consequences:
  - "{{consequence_1}}"
  - "{{consequence_2}}"

rejected_alternatives:
  - "{{rejected_1}}"
  - "{{rejected_2}}"
```