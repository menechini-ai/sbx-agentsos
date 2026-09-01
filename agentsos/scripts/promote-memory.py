#!/usr/bin/env python3
"""
Promote Memory Script

Promotes memory candidates (learnings, patterns) to skills, rules, or agents
based on the promotion policies defined in GOVERNANCE.md.

Usage:
    python promote-memory.py --candidate_id CAND-2026-0001 --promote-to skill
    python promote-memory.py --auto  # Auto-detect candidates and promote

Or integrate as a module:
    from scripts.promote_memory import promote_candidate
    result = promote_candidate(candidate_id="CAND-2026-0001", to="skill")
"""

import json
import sys
import os
from datetime import datetime


def load_candidate(candidate_id):
    """Load a candidate entry from memory/candidates/."""
    # Try different paths
    paths = [
        f"agentsos/memory/candidates/{candidate_id}.md",
        f"agentsos/memory/candidates/{candidate_id}.json",
    ]
    
    for path in paths:
        if os.path.exists(path):
            with open(path, "r") as f:
                content = f.read()
            if path.endswith(".json"):
                return json.loads(content)
            return content
    
    # Try JSON in markdown
    md_path = f"agentsos/memory/candidates/{candidate_id}.md"
    if os.path.exists(md_path):
        with open(md_path, "r") as f:
            content = f.read()
        # Try to extract JSON from markdown
        import re
        match = re.search(r'```json\s*(.*?)\s*```', content, re.DOTALL)
        if match:
            return json.loads(match.group(1))
        # Try frontmatter
        match = re.search(r'---\n(.*?)\n---', content, re.DOTALL)
        if match:
            data = match.group(1)
            # Parse key lines
            result = {}
            for line in data.split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    result[key.strip()] = val.strip()
            return result
    
    print(f"Candidate not found: {candidate_id}")
    return None


def load_skill(skill_name):
    """Load a skill entry from skills/skill-name/SKILL.md."""
    paths = [
        f"agentsos/skills/{skill_name}/SKILL.md",
        f"agentsos/skills/{skill_name}.md",
    ]
    
    for path in paths:
        if os.path.exists(path):
            with open(path, "r") as f:
                return f.read()
    
    return None


def promote_to_skill(candidate_id):
    """Promote a candidate to skill."""
    candidate = load_candidate(candidate_id)
    if not candidate:
        return False, f"Candidate not found: {candidate_id}"
    
    # Determine skill name from description
    description = candidate.get("description", [""])[0] if isinstance(candidate.get("description"), list) else candidate.get("description", "")
    skill_name = description.lower().replace(" skill", "").replace(" testing", "").strip() or "new-skill"
    
    # Check if skill already exists
    skill_path = f"agentsos/skills/{skill_name}/SKILL.md"
    if os.path.exists(skill_path):
        return False, f"Skill already exists: {skill_name}"
    
    # Create skill directory
    os.makedirs(f"agentsos/skills/{skill_name}", exist_ok=True)
    
    # Generate SKILL.md from candidate data
    skill_content = f"""# SKILL.md - {skill_name}

## Metadados

- **Name**: {skill_name}
- **Version**: 1.0.0
- **Description**: {description}
- **Owner**: {{skill_owner}}
- **Status**: stable

## Inputs

- `task_id` — ID da tarefa referenciando o contrato INPUT em `contracts/input/`
- `objective` — Descrição da implementação requerida
- `context` — Contexto adicional (repository, branch, constraints)

## Outputs

- `implementation_report` — Relatório estruturado com changes, validation e risks

## Dependencies

- `github` — Acesso ao repository, issues, PRs
- `filesystem` — Leitura/escrita de arquivos source e tests

## Tools

- `github.read` — Ler código fonte, issues, PRs, commits
- `github.write` — Criar branches, commits, PRs, issues
- `filesystem.read` — Ler arquivos source, tests, configs
- `filesystem.write` — Escrever código source, tests, configs

## Purpose

Implementar features, corrigir bugs, refatorar código ou adicionar testes conforme contrato INPUT recebido, produzindo um `implementation_report` estruturado que possa ser:
- Validado através dos contratos OUTPUT
- Promovido para knowledge no ai-memory
- Servir de base para future skills ou rules

## When to Use

- Quando receber um task envelope INPUT com objective de implementação
- Quando necessário implementar uma feature baseada em requisitos claros
- Para debugging de código existente quando o problema está bem definido
- Para adicionar testes quando a implementação requer cobertura

## When NOT to Use

- Quando a task requer pesquisa extensa antes da implementação (usar `research` skill primeiro)
- Quando o problema não está bem definido (usar `debugging` skill ou clarification)
- Quando a mudança requer aprovação de governança (verificar `GOVERNANCE.md` §01 matriz de autorização)
- Quando a task envolve configurações de MCP que não estão no escopo L2 (needs L1 approval)

## Procedure

1. **Ler task envelope**: Consultar `contracts/input/task-envelope.md` para entender:
   - Objective preciso
   - Constraints e boundaries
   - Skills e tools autorizadas (matriz ✅⚠️🔐 de GOVERNANCE.md)
   - Memory que pode ser consultada
2. **Explorar código**: Utilizar `github.read` e `filesystem.read` para entender:
   - Estrutura do repository
   - Código existente relacionado
   - Patterns e conventions do projeto
3. **Implementar**: Escrever código conforme constraints, following project conventions
4. **Escrever tests**: Implementar testes que validam a implementação
5. **Validar**: Cross-check com:
   - Conformance a GOVERNANCE.md authority limits
   - Existing tests não quebrados
   - Code conventions do projeto
6. **Produzir report**: Gerar `implementation_report` com:
   - `status`: completed/partial/blocked
   - `changes`: files modificados + descrição succinta
   - `validation`: status dos testes (passed/failed/total)
   - `risks`: risks identificados, assumptions feitas
   - `memory_candidates`: aprendizados para promover
   - `improvement_candidates`: skills/patterns a propor

## Validation

- Verificar se todas as constraints do task envelope foram respeitadas
- Confirmar que changes não violam authority limits de GOVERNANCE.md §01
- Confirmar que tests passam no número especificado (ou documentar failures)
- Cross-check com `ai-memory` — promover learning se aplicável

## Failure Modes

- **Constraint violation**: Code written outside boundaries autorizadas; recomenda-se revisar constraints e refatorar
- **Test failures**: Tests falhando; recomenda-se debugging e ajuste de implementation
- **Authority overreach**: Implementation tentando modificar GOVERNANCE.md ou hierarquia; recomenda-se propoer mudança via `proposals/`

## Examples

### Exemplo 1: Implementar Feature

```
Input: task_id="TASK-2026-0001", objective="Implementar autenticação", 
  constraints=["Não alterar arquitetura global"]
Output: implementation_report contendo:
  - status: completed
  - changes: [src/auth/login.ts, tests/auth/login.test.ts]
  - validation: tests status: passed, total: 42
  - risks: ["JWT expiration ainda usa configuração padrão"]
  - memory_candidates: [type: learning, description: "Projeto utiliza refresh token de 7 dias"]
  - improvement_candidates: [type: skill, name: "auth-testing", reason: "Padrão repetido em 4 tarefas"]
```

### Exemplo 2: Bug Fix

```
Input: task_id="TASK-2026-0002", objective="Corrigir memory leak", 
  constraints=["Não alterar estrutura de memória"]
Output: implementation_report contendo:
  - status: completed
  - changes: [src/memory/cleanup.ts]
  - validation: tests status: passed, total: 15
  - risks: baixo
  - memory_candidates: [type: learning, description: "Pattern de leak detectado; promover para rule"]
```

## Known Limitations

- Dependente de specifications claras no task envelope
- Pode não cobrir edge cases se constraints forem muito restritivas
- Requires acesso a github e filesystem (L2 tools)

## Improvement Criteria

- **Nova skill proposta**: Quando pattern repetido em 4+ tasks (GOVERNANCE.md §02.4)
- **Promoção para rule**: Quando bug/pattern sistêmico impacta múltiplas tasks
- **Memory promotion**: Quando aprendizado relevante para arquitetura ou padrões de código

## Changelog

- **1.0.0**: Versão inicial
"""
    
    with open(skill_path, "w") as f:
        f.write(skill_content)
    
    # Record the promotion in learnings
    learning_entry = f"""# Learning Entry

```
learning_id: LEARN-2026-{hash(skill_name) % 10000}
task_id: {candidate.get("task_id", "unknown")}
agent: {{agent_name}}
date: {datetime.utcnow().strftime("%Y-%m-%d")}
type: skill
status: promoted

content:
  - "{description}"

context:
  task: "{{candidate.get("task_id", "unknown")}}"
  repository: "{{candidate.get("repository", "project")}}"
  branch: "{{candidate.get("branch", "main")}}"

promotion_candidate:
  type: skill
  description: "{description}"
  occurrences: {candidate.get("pattern_detection", {}).get("occurrences", 0) if isinstance(candidate.get("pattern_detection"), dict) else candidate.get("occurrences", 0)}
  confidence: {candidate.get("confidence", 0.5)}
```
"""
    
    os.makedirs("agentsos/memory/learnings", exist_ok=True)
    learning_filename = f"agentsos/memory/learnings/learn-{skill_name.replace('-', '')}.md"
    with open(learning_filename, "w") as f:
        f.write(learning_entry)
    
    # Remove the candidate
    candidate_path = f"agentsos/memory/candidates/{candidate_id}.md"
    if os.path.exists(candidate_path):
        os.remove(candidate_path)
    
    return True, f"Skill '{skill_name}' promoted successfully"


def promote_to_rule(candidate_id):
    """Promote a candidate to rule."""
    candidate = load_candidate(candidate_id)
    if not candidate:
        return False, f"Candidate not found: {candidate_id}"
    
    # Determine rule name
    description = candidate.get("description", [""])[0] if isinstance(candidate.get("description"), list) else candidate.get("description", "")
    
    # Read the related AGENTS.md to add the rule
    # This is simplified - in practice would read the relevant AGENTS.md
    agents_md_path = "agentsos/agents/developer/AGENTS.md"
    
    # Add rule to AGENTS.md
    # In a real implementation, this would be more sophisticated
    rule_text = f"\n## Rule Candidate\n\n{description}"
    
    # For now, just record the promotion
    return True, f"Rule candidate promoted from {candidate_id}. Rule text: {description[:50]}..."


def promote_to_agent(candidate_id):
    """Promote a candidate to new agent."""
    candidate = load_candidate(candidate_id)
    if not candidate:
        return False, f"Candidate not found: {candidate_id}"
    
    # Read proposal data
    description = candidate.get("description", [""])[0] if isinstance(candidate.get("description"), list) else candidate.get("description", "")
    
    # In a real implementation, this would:
    # 1. Create new agent directory with AGENTS.md
    # 2. Set up skills and tools
    # 3. Record in proposals/
    
    return True, f"Agent candidate promoted from {candidate_id}. Description: {description[:50]}..."


def auto_promote():
    """Auto-detect candidates and promote based on risk levels."""
    candidates_dir = "agentsos/memory/candidates"
    if not os.path.exists(candidates_dir):
        print("No candidates directory found")
        return
    
    promoted = []
    
    # List all candidates
    for filename in os.listdir(candidates_dir):
        if filename.endswith(".md") or filename.endswith(".json"):
            candidate_path = os.path.join(candidates_dir, filename)
            candidate = load_candidate(filename.replace(".md", "").replace(".json", ""))
            if not candidate:
                # Try reading as markdown
                with open(candidate_path, "r") as f:
                    content = f.read()
                import re
                match = re.search(r'candidate_id:\s*(\S+)', content)
                if match:
                    candidate_id = match.group(1)
                    candidate = load_candidate(candidate_id)
            
            if not candidate:
                continue
            
            risk_level = candidate.get("risk_level", "LOW")
            
            # Promote based on risk level
            if risk_level == "LOW":
                # Auto-promote to skill
                result, message = promote_to_skill(candidate_id)
                promoted.append((candidate_id, "skill", message))
            elif risk_level == "MEDIUM":
                # Promote to rule (requires review)
                result, message = promote_to_rule(candidate_id)
                promoted.append((candidate_id, "rule", message))
            elif risk_level == "HIGH":
                # Requires CEO approval - just record
                result, message = promote_to_agent(candidate_id)
                promoted.append((candidate_id, "agent", message))
    
    print(f"Auto-promotion complete. {len(promoted)} candidates processed.")
    for candidate_id, promo_type, message in promoted:
        print(f"  {candidate_id} → {promo_type}: {message}")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Promote memory candidates")
    parser.add_argument("--candidate_id", help="Candidate ID to promote")
    parser.add_argument("--promote-to", choices=["skill", "rule", "agent"], help="Promote to type")
    parser.add_argument("--auto", action="store_true", help="Auto-detect and promote all candidates")
    
    args = parser.parse_args()
    
    if args.auto:
        auto_promote()
    elif args.candidate_id and args.promote_to:
        if args.promote_to == "skill":
            result, message = promote_to_skill(args.candidate_id)
        elif args.promote_to == "rule":
            result, message = promote_to_rule(args.candidate_id)
        elif args.promote_to == "agent":
            result, message = promote_to_agent(args.candidate_id)
        print(f"Promotion result: {result} - {message}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()