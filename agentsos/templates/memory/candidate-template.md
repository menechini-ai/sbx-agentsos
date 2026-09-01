# Template: Candidate Entry

## Formato Padrão

```
candidate_id: CAND-2026-XXXX
task_id: TASK-2026-XXXX
agent: {{agent_name}}
date: {{date}}
type: {{candidate_type}}  # skill_candidate, rule_candidate, agent_candidate
status: {{status}}  # awaiting_review, approved, rejected

description:
  - "{{description_1}}"
  - "{{description_2}}"

pattern_detection:
  occurrences: {{occurrences}}
  tasks:
    - {{task_id_1}}
    - {{task_id_2}}

confidence: {{confidence_score}}

risk_level: {{risk_level}}  # LOW, MEDIUM, HIGH

review:
  required: {{review_required}}
  reviewer: {{reviewer_name}}
  status: {{review_status}}
```