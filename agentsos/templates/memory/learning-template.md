# Template: Learning Entry

## Formato Padrão

```
learning_id: LEARN-2026-XXXX
task_id: TASK-2026-XXXX
agent: {{agent_name}}
date: {{date}}
type: {{learning_type}}  # ephemeral, skill_candidate, rule_candidate, agent_candidate
status: {{status}}

content:
  - "{{content_point_1}}"
  - "{{content_point_2}}"

context:
  task: "{{task_description}}"
  repository: "{{repository_name}}"
  branch: "{{branch_name}}"

promotion_candidate:
  type: {{promotion_type}}  # skill, rule, agent
  description: "{{promotion_description}}"
  occurrences: {{occurrences}}  # número de vezes que o pattern foi detectado
  confidence: {{confidence_score}}  # 0.0 a 1.0
```