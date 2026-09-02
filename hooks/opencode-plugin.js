#!/usr/bin/env bash
# OpenCode session-start hook - injects Agent OS context at session start

# Determine the Agent OS root directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
AGENTS_OS_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Read AGENTS.md content (the main system contract)
if [[ -f "${AGENTS_OS_ROOT}/AGENTS.md" ]]; then
    agents_os_content=$(cat "${AGENTS_OS_ROOT}/AGENTS.md" 2>&1)
else
    agents_os_content="Error: AGENTS.md not found at ${AGENTS_OS_ROOT}/AGENTS.md"
fi

# Output context injection as JSON
# OpenCode expects additionalContext (top-level, SDK standard format)
printf '{\n  "additionalContext": "%s"\n}\n' "$agents_os_content" | cat
exit 0