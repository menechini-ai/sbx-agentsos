# Memory Enrichment & Auto-Improvement Loop Design

**Author**: Agent OS Team
**Created**: 2026-09-01
**Status**: Design approved — ready for implementation planning

---

## 1. Overview

This design adds five incremental capabilities to the Agent OS memory system, aligning it with the ai-memory project's production-grade standards while respecting the existing Git-wiki + SQLite architecture. The features are:

1. **Atomic wiki entries** — one idea per markdown file
2. **Structured triplet fields** — explicit `actor → decision → rationale` in YAML frontmatter
3. **Link evolution metadata** — reference counting and last-referenced tracking
4. **Post-turn auto-learning hook** — automatically propose candidates from result envelopes
5. **Governance authorization wrapper** — L0-L5 access control over ai-memory operations

These features are designed to be **incrementally adoptable** — each can be implemented independently without breaking existing workflows.

---

## 2. Detailed Design

### 2.1 Atomic Wiki Entries (A-MEM influence)

**Current problem**: Learning/decisions entries in `agentsos/memory/learnings/` may contain multiple ideas, making granular linking, querying, and promotion difficult.

**Solution**: Each learning entry becomes one atomic markdown file, following A-MEM's "one note per idea" pattern. Existing entries are not deleted — they are marked as `deprecated` and redirect to the new atomic file.

**New file format** (`agentsos/memory/learnings/learning-entry-LEARN-ID.md`):

```markdown
# LEARN-2026-0001: Refresh token pattern

## Summary
Projeto utiliza refresh token de 7 dias.

## Context
Task: Implementar autenticação
Repository: project
Branch: feature/auth

## Metadata (YAML frontmatter)
---
actor: developer
decision: use-refresh-tokens
rationale: "Refresh tokens reduce login friction for returning users"
times_referenced: 3
last_referenced_by: qa-agent
related_learnings:
  - LEARN-2026-0010
  - LEARN-2026-0015
---

## Deprecated Redirect
This file was refactored from the old multi-entry format at `memory/learnings/learning-entry.md`.
See the new atomic format in sibling files.

## Related Entries
- [LEARN-2026-0010](memory/learnings/learning-entry-LEARN-2026-0010.md) — Pattern detection
- [LEARN-2026-0015](memory/learnings/learning-entry-LEARN-2026-0015.md) — Token rotation procedure
```

**Backward compatibility**: Old `learning-entry.md` files remain readable but display a banner:
> ⚠️ This is a legacy multi-entry format. Consider refactoring to atomic entries for better linking.

**Migration script**: `scripts/migrate-to-atomic.py` — converts existing entries by splitting multi-concept entries into separate atomic files, preserving YAML frontmatter where possible.

---

### 2.2 Structured Triplet Fields (cognee influence)

**Current problem**: No explicit structured knowledge beyond free-text content. Querying is limited to FTS5 keyword search.

**Solution**: Add three mandatory fields to the YAML frontmatter of every learning/decisions entry:

| Field | Type | Description |
|---|---|---|
| `actor` | string | The agent/actor who made the decision/learning |
| `decision` | string | The decision or pattern recorded |
| `rationale` | string | The reason/rationale for the decision |

**Example**:

```yaml
---
actor: developer
decision: use-refresh-tokens
rationale: "Refresh tokens reduce login friction for returning users"
times_referenced: 3
last_referenced_by: qa-agent
related_learnings:
  - LEARN-2026-0010
---
```

**Queryability**: These fields enable new query patterns:
- `SELECT * FROM learnings WHERE actor = 'developer'`
- `SELECT * FROM learnings WHERE decision = 'use-refresh-tokens'`
- `SELECT * FROM learnings WHERE rationale LIKE '%friction%'`

The SQLite index in `ai-memory` can be extended to index these fields via a derived column or FTS5 virtual table inclusion.

**Optional for now**: New entries include the fields; existing entries can opt-in gradually. The fields are not enforced at read time but are expected convention.

---

### 2.3 Link Evolution Metadata (A-MEM influence)

**Current problem**: No way to track how learnings are referenced over time, across tasks and agents.

**Solution**: Two lightweight metadata fields added to the YAML frontmatter:

| Field | Type | Description |
|---|---|---|
| `times_referenced` | integer (default 0) | How many times this learning has been referenced/cited |
| `last_referenced_by` | string (default "none") | The agent/role that last referenced this learning |
| `related_learnings` | string[] (default []) | Learning IDs this entry is related to (explicit links) |

**Behavior**:
- `times_referenced` is auto-incremented when the learning is cited in a new task's context, result envelope, or candidate description.
- `last_referenced_by` is set to the agent ID or role that most recently referenced it.
- `related_learnings` is manually populated or auto-populated by the migration script based on co-occurrence in tasks.

**Example**:

```yaml
---
actor: developer
decision: use-refresh-tokens
rationale: "Refresh tokens reduce login friction for returning users"
times_referenced: 5
last_referenced_by: qa-agent
related_learnings:
  - LEARN-2026-0010
  - LEARN-2026-0015
---
```

This enables emergent knowledge network visualization without requiring a graph database.

---

### 2.4 Post-Turn Auto-Learning Hook (Hermes Agent influence)

**Current problem**: Improvement candidates are manually placed in result envelopes. There's no automatic pipeline that extracts learnings from completed task summaries.

**Solution**: A new script `scripts/auto_learning_hook.py` that runs after each task result envelope is generated. It:

1. Reads the `result-envelope.json` summary field
2. Extracts key concepts, patterns, and decisions
3. Proposes a `learning-entry.md` candidate if novel patterns are detected
4. Pre-fills `promotion_candidate` if pattern repetition threshold is met (≥3 tasks)
5. Comments the result envelope with `improvement_candidates` suggestion

**Input**: `result-envelope.json` (path provided as argument or via env var `AI_MEMORY_LAST_RESULT`)

**Output**: 
- Creates/updates `agentsos/memory/learnings/learning-entry-LEARN-ID.md`
- Appends a summary block to the result envelope: `auto_learning_proposal: true`
- Logs the action to `agentsos/memory/logs/auto_hook.log`

**Example flow**:

```
Task execution → result-envelope.json generated
  ↓
auto_learning_hook.py runs
  ↓
Extracts summary: "Autenticação implementada com JWT. Refresh token de 7 dias usado."
  ↓
Detects pattern: "refresh token" mentioned for 3rd time across tasks
  ↓
Creates learning entry LEARN-2026-0002: "Projeto utiliza refresh token de 7 dias"
  ↓
Sets promotion_candidate: type=skill, description="Padrão de refresh token repetido em 3 tarefas", occurrences=3
  ↓
Appends to result envelope: "auto_learning_proposal: true (LEARN-2026-0002 created)"
  ↓
Task completes → human reviews and decides promotion
```

**Opt-in**: The hook is opt-in per task, controlled by a field in the task envelope:
```json
"auto_learning_hook": {
  "enabled": true,
  "threshold_occurrences": 3
}
```
Default: `enabled: false` (to avoid noise in existing workflows). Users can opt-in by adding the field to their task envelope.

---

### 2.5 Governance Authorization Wrapper (Agent OS L0-L5 influence)

**Current problem**: The L0-L5 hierarchy is defined in GOVERNANCE.md but has no concrete implementation over ai-memory operations. Any agent with ai-memory credentials can read/write any entry.

**Solution**: A new governance file `agentsos/guardrails/memory-authorization.md` that defines an authorization matrix over ai-memory operations, checked before any read/write.

**Authorization Matrix** (checked at runtime by a wrapper/module):

| Operation | L0 | L1 | L2 | L3 | L4 | L5 |
|---|---|---|---|---|---|---|
| `read:any` | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| `write:learning` | ✅ | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| `write:candidate` | ✅ | ✅ | ⚠️ | ❌ | ❌ | ❌ |
| `delete:learning` | ✅ | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| `delete:candidate` | ✅ | ⚠️ | ❌ | ❌ | ❌ | ❌ |

**Key rules**:
- **L0** (GOVERNANCE): Can do anything — audit, configure, emergency access
- **L1** (CEO/Principal): Can read/write learnings, promote MEDIUM risk candidates
- **L2** (Department Agent): Can read learnings, create candidates, cannot promote without L1 approval
- **L3** (Specialist): Can read, cannot write/delete
- **L4** (Subagent): Read-only, cannot create or modify
- **L5** (Tool/MCP): Read-only via MCP gateway, no direct access

**Implementation**:
- A Python module `agentsos/guardrails/authorization.py` reads the matrix + agent level + operation type
- Returns `allow/deny` with reason
- Used by scripts (`capture-session.py`, `promote-memory.py`, `auto_learning_hook.py`) before performing operations
- Can be bypassed only by L0 with explicit audit log entry

**Example usage** in `promote-memory.py`:
```python
from agentsos.guardrails.authorization import check_authorization

if not check_authorization(
    operation="write:candidate",
    agent_level="developer",
    actor="developer":
):
    raise PermissionError("L3 developers cannot auto-promote candidates — require L1 review")
# ... proceed with promotion
```

---

## 3. Data Model Changes Summary

### 3.1 Learning Entry YAML Frontmatter (new — optional, opt-in)

```yaml
---
actor: developer           # who recorded this
decision: use-refresh-tokens  # what was decided
rationale: "Refresh tokens reduce login friction for returning users"  # why
times_referenced: 3        # auto-incremented
last_referenced_by: qa-agent  # who last referenced
related_learnings:        # explicit links
  - LEARN-2026-0010
  - LEARN-2026-0015
---
```

### 3.2 Candidate Entry YAML Frontmatter (new field)

```yaml
---
candidate_id: CAND-2026-0001
task_id: TASK-2026-0001
agent: developer
date: 2026-09-01
type: skill
status: awaiting_review
auto_generated_from: "auto_learning_hook"  # NEW: tracks auto-generation
---
```

### 3.3 Result Envelope (new optional field)

```json
{
  "auto_learning_proposal": {
    "learning_id": "LEARN-2026-0002",
    "created_by": "auto_learning_hook.py",
    "summary_excerpt": "Refresh token pattern detected across 3 tasks"
  }
}
```

---

## 4. New/Modified Files

| Path | Change Type | Description |
|---|---|---|
| `agentsos/memory/learnings/learning-entry.md` | Modified | Add deprecation banner + atomic format example |
| `agentsos/memory/candidates/candidate-entry.md` | Modified | Add `auto_generated_from` field |
| `agentsos/guardrails/memory-authorization.md` | New | Authorization matrix + runtime check module |
| `agentsos/guardrails/authorization.py` | New | Python module for L0-L5 permission checks |
| `agentsos/scripts/auto_learning_hook.py` | New | Post-turn auto-learning proposal hook |
| `agentsos/scripts/migrate-to-atomic.py` | New | Migration script for existing multi-entry learnings |
| `agentsos/memory/learnings/learning-entry-LEARN-ID.md` | New (generated) | Atomic entry format (one per idea) |
| `agentsos/memory/logs/auto_hook.log` | New | Auto-hook execution log |

---

## 5. Migration Path (Incremental, No Breaking Changes)

| Phase | Action | Risk |
|---|---|---|
| **Phase 1** (week 1) | Add YAML frontmatter fields to new entries only; existing entries remain as-is. Low risk — backward compatible. | Low |
| **Phase 2** (week 2) | Run `migrate-to-atomic.py` on existing `learnings/` to split multi-concept entries. Medium risk — depends on entry density. | Medium |
| **Phase 3** (week 3) | Enable `auto_learning_hook` opt-in via task envelope flag. Low risk — opt-in. | Low |
| **Phase 4** (week 4) | Enable authorization wrapper in scripts. Medium risk — permission denials may break existing automated workflows. | Medium |
| **Phase 5** (ongoing) | Iterate on triplet field population and link evolution tracking. Low risk. | Low |

**Migration script notes**: `migrate-to-atomic.py` is conservative — it only splits entries that have clear `## Section` headers or distinct YAML-frontmatter-separated blocks. Entries that are pure free-text are left as-is with the deprecation banner.

---

## 6. Success Metrics

After implementation, measure:

| Metric | Target | Measurement |
|---|---|---|
| % of new learning entries with triplet fields | 100% (new entries) | Script audit |
| % of existing entries migrated to atomic format | ≥ 50% (first quarter) | Migration script report |
| Auto-hook proposals per 10 tasks | 1–2 (if opt-in enabled) | Log analysis |
| Authorization check false-positive rate | < 5% | Governance audit |
| Link evolution metadata completeness | ≥ 80% after migration | Data scan |

---

## 7. Open Questions / Decisions Needed

1. **Triplet fields: mandatory or optional?**
   - Recommendation: optional for now, convention for new entries. Can become mandatory in a future version after adoption.

2. **Auto-hook: opt-in per-task or system-wide default?**
   - Recommendation: opt-in via task envelope `auto_learning_hook.enabled`. Avoids noise in existing workflows. Users explicitly opt-in.

3. **Authorization: enforce at script level or at ai-memory server level?**
   - Recommendation: enforce at Agent OS script level (Python module), as the ai-memory server may not have Agent OS context. The wrapper checks the matrix before calling ai-memory operations.

4. **Do we want the `related_learnings` auto-population?**
   - The migration script can auto-populate based on co-occurrence (same task ID, same actor), but it's heuristic. Manual population is safer initially.

5. **Should the atomic entry format also apply to decisions?**
   - Currently designed for learnings. Decisions can follow the same pattern in a future iteration. For now, decisions remain in their existing format but can adopt the triplet YAML fields.

---

## 8. Approval & Next Steps

✅ **Design approved** — proceeding to implementation planning.

**Next step**: Invoke the `writing-plans` skill to create a detailed implementation plan with:
- Individual task breakdowns
- Dependencies between the 5 capabilities
- Testing strategy
- Rollout schedule

---

*This design follows the Agent OS governance framework (L0-L5) and integrates with the ai-memory architecture as described in the project's README and ARCHITECTURE.md. All changes are incremental and backward-compatible.*