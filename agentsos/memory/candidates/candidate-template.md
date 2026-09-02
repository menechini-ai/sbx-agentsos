---
type: template
title: Learning Candidate Template
domain: agent-os
tags:
  - template
  - candidate
  - learning
---

# Learning Candidate

## Metadata
- **ID**: [agent-os.learning.candidate.{slug}]
- **Date**: YYYY-MM-DD
- **Source Session**: [session-date-agent]
- **Agent**: [agent-name]
- **Risk Level**: [LOW|MEDIUM|HIGH]
- **Status**: [pending|reviewed|promoted|rejected]

## Learning
### Observation
[What was observed or learned]

### Context
[Why this matters, when it applies]

### Evidence
[Code example, log, metric that demonstrates the learning]

## Candidate Promotion Path

### Suggested Destination
- [ ] **concept note** → `memory/knowledge/.../concepts/`
- [ ] **pattern note** → `memory/knowledge/.../patterns/`
- [ ] **runbook** → `memory/knowledge/.../runbooks/`
- [ ] **guardrails update** → `agentsos/guardrails/`
- [ ] **agent update** → `agentsos/agents/`

### Promotion Reasoning
[Why this destination makes sense]

## Review
- **Reviewed by**: [agent or human name]
- **Review Date**: [date]
- **Decision**: [promote|reject|modify]
- **Notes**: [reviewer comments]

## Promotion Record (when promoted)
- **Promoted to**: [path of promoted note]
- **Promoted on**: [date]
- **Promoted by**: [who promoted]
