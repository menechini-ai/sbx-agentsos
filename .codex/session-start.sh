#!/usr/bin/env bash
# SessionStart hook for Agent OS
# Injects Agent OS context at the start of every session

set -euo pipefail

# Determine the Agent OS root directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
AGENTS_OS_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Read AGENTS.md content (the main system contract)
if [[ -f "${AGENTS_OS_ROOT}/AGENTS.md" ]]; then
    agents_os_content=$(cat "${AGENTS_OS_ROOT}/AGENTS.md" 2>&1)
else
    agents_os_content="Error: AGENTS.md not found at ${AGENTS_OS_ROOT}/AGENTS.md"
fi

# Read GOVERNANCE.md summary (constitutional layer)
if [[ -f "${AGENTS_OS_ROOT}/docs/GOVERNANCE.md" ]]; then
    governance_summary=$(head -100 "${AGENTS_OS_ROOT}/docs/GOVERNANCE.md" 2>&1)
else
    governance_summary="Error: GOVERNANCE.md not found"
fi

# Escape string for JSON embedding
escape_for_json() {
    local s="$1"
    s="${s//\\/\\\\}"
    s="${s//\"/\\\"}"
    s="${s//$'\n'/\\n}"
    s="${s//$'\r'/\\r}"
    s="${s//$'\t'/\\t}"
    printf '%s' "$s"
}

agents_os_escaped=$(escape_for_json "$agents_os_content")
governance_escaped=$(escape_for_json "$governance_summary")

# Build the context injection
# Format matches what each platform expects
session_context="<EXTREMELY_IMPORTANT>
You are operating within Agent OS — a modular AI agent architecture with formal governance, persistent memory, and reusable skills.

**Below is the full content of Agent OS AGENTS.md (system contract) and GOVERNANCE.md summary:**

## AGENTS.md — System Contract
${agents_os_escaped}

## GOVERNANCE.md — Constitutional Governance (L0)
${governance_escaped}

## Memory System
- Knowledge base: agentsos/memory/knowledge/ (skill-kwonledge, Obsidian-style)
- Sessions: agentsos/memory/sessions/ (flat logs by date)
- Candidates: agentsos/memory/candidates/ (learning promotion pipeline)

## Key Directives
1. **Hierarchy L0-L5**: Lower levels CANNOT override higher levels
2. **Governance First**: Complete current task before proposing changes
3. **Memory as Truth**: Persistent info in memory/knowledge/, not conversation
4. **Structured Contracts**: All tasks follow INPUT/OUTPUT envelopes
5. **Guardrails**: Operate within authorization matrix (✅⚠️🔐❌)

## Skills
- Core: brainstorming, brief-creation, prd-writing, tech-spec, adr-writing, sprint-planning, agentos-build, dev-story, qa-gate, review, retrospective, agentos-help
- Azure: pipeline-yaml, resource-provisioning, cluster-setup, rollout-strategies, monitor-setup, integration-setup
- Use skill tool before ANY task

</EXTREMELY_IMPORTANT>"

# Output context injection based on platform
if [ -n "${CURSOR_PLUGIN_ROOT:-}" ]; then
    # Cursor expects additional_context (snake_case)
    printf '{\n  "additional_context": "%s"\n}\n' "$session_context"
elif [ -n "${CLAUDE_PLUGIN_ROOT:-}" ] && [ -z "${COPILOT_CLI:-}" ]; then
    # Claude Code expects hookSpecificOutput.additionalContext (nested)
    printf '{\n  "hookSpecificOutput": {\n    "hookEventName": "SessionStart",\n    "additionalContext": "%s"\n  }\n}\n' "$session_context"
elif [ -n "${COPILOT_CLI:-}" ] || [ -n "${OPENCODE:-}" ]; then
    # Copilot CLI or OpenCode - SDK standard format (top-level additionalContext)
    printf '{\n  "additionalContext": "%s"\n}\n' "$session_context"
else
    # Default/Unknown platform - SDK standard format
    printf '{\n  "additionalContext": "%s"\n}\n' "$session_context"
fi

exit 0