#!/usr/bin/env python3
"""
Delegation Workflow Script

Implements the delegation workflow from CEO → Agents → Subagents,
ensuring proper authority checks, envelope handling, and handoff.

Usage:
    python delegation-workflow.py --task TASK-2026-0001 --from ceo --to developer
    python delegation-workflow.py --handoff --from developer --to qa
"""

import json
import sys
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)


def check_authorization(sender_level, receiver_level, action="delegate"):
    """Check if delegation is authorized per GOVERNANCE.md matrix."""
    # simplified matrix check
    matrix = {
        ("L1", "L2"): "✅",  # CEO → Developer
        ("L2", "L3"): "✅",  # Developer → Specialist
        ("L2", "L4"): "⚠️",  # Developer → Subagent (requires L3 design)
        ("L3", "L5"): "✅",  # Specialist → Tool (via MCP)
    }
    
    result = matrix.get((sender_level, receiver_level), "❓")
    
    if result == "❌":
        print(f"❌ DENIED: {sender_level} → {receiver_level} {action} not allowed")
        return False
    elif result == "⚠️":
        print(f"⚠️ WARNING: {sender_level} → {receiver_level} {action} requires design review")
        return True  # Allow but warn
    else:
        print(f"✅ AUTHORIZED: {sender_level} → {receiver_level} {action} allowed")
        return True


def delegate_task(task_id, from_agent, to_agent, from_level, to_level):
    """Execute a delegation step."""
    print(f"Delegating task {task_id}: {from_agent}(L{from_level}) → {to_agent}(L{to_level})")
    
    # Check authorization
    if not check_authorization(from_level, to_level, "delegate"):
        return False
    
    # Read task envelope
    envelope_path = os.path.join(PROJECT_ROOT, "agentsos", "contracts", "input", "task-envelope.json")
    if os.path.exists(envelope_path):
        with open(envelope_path, "r") as f:
            envelope = json.load(f)
        print(f"  Task envelope read: {envelope['task']['id']}")
        print(f"  Objective: {envelope['task']['objective']['primary']}")
        print(f"  Constraints: {envelope['task']['constraints']}")
        print(f"  Authorized skills: {envelope['task']['resources']['skills']}")
        print(f"  Authorized tools: {envelope['task']['resources']['tools']}")
    
    # In a real system, this would:
    # 1. Update task status
    # 2. Notify the receiving agent
    # 3. Create audit log entry
    
    print(f"✅ Task delegated successfully")
    return True


def handoff_task(task_id, from_agent, to_agent, completed=None, pending=None, artifacts=None, risks=None, instructions=None):
    """Execute a handoff step."""
    print(f"Handoff task {task_id}: {from_agent}(L{get_level(from_agent)}) → {to_agent}(L{get_level(to_agent)})")
    
    # Read current result envelope
    result_path = os.path.join(PROJECT_ROOT, "agentsos", "contracts", "output", "result-envelope.json")
    if os.path.exists(result_path):
        with open(result_path, "r") as f:
            result = json.load(f)
        
        # Update with handoff data
        if completed:
            result["result"]["summary"] = completed
        if pending:
            result["result"]["pending_issues"] = pending
        if artifacts:
            result["result"]["changes"]["files"] = artifacts
        if risks:
            result["result"]["risks"] = risks
        if instructions:
            result["result"]["handoff_instructions"] = instructions
        
        # Write back
        with open(result_path, "w") as f:
            json.dump(result, f, indent=2)
    
    # In a real system, this would:
    # 1. Create handoff report
    # 2. Notify receiving agent
    # 3. Persist state in ai-memory
    # 4. Create audit log
    
    print(f"✅ Handoff completed")
    return True


def get_level(agent_name):
    """Get the level for an agent."""
    levels = {
        "ceo": "L1",
        "developer": "L2", 
        "researcher": "L2",
        "qa": "L3",
        "security": "L3"
    }
    return levels.get(agent_name.lower(), "L0")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Delegation workflow")
    subparsers = parser.add_subparsers(dest="command")
    
    # Delegate command
    delegate_parser = subparsers.add_parser("delegate")
    delegate_parser.add_argument("--task", required=True, help="Task ID")
    delegate_parser.add_argument("--from_agent", required=True, help="From agent")
    delegate_parser.add_argument("--to_agent", required=True, help="To agent")
    
    # Handoff command
    handoff_parser = subparsers.add_parser("handoff")
    handoff_parser.add_argument("--task", required=True, help="Task ID")
    handoff_parser.add_argument("--from_agent", required=True, help="From agent")
    handoff_parser.add_argument("--to_agent", required=True, help="To agent")
    handoff_parser.add_argument("--completed", nargs="+", help="Completed items")
    handoff_parser.add_argument("--pending", nargs="+", help="Pending items")
    handoff_parser.add_argument("--artifacts", nargs="+", help="Artifacts")
    handoff_parser.add_argument("--risks", nargs="+", help="Risks")
    handoff_parser.add_argument("--instructions", nargs="+", help="Instructions")
    
    args = parser.parse_args()
    
    if args.command == "delegate":
        from_agent_name = args.from_agent
        to_agent_name = args.to_agent
        from_level = from_agent_name.replace("L", "") if from_agent_name.startswith("L") else "1"
        to_level = to_agent_name.replace("L", "") if to_agent_name.startswith("L") else "2"
        delegate_task(args.task, from_agent_name, to_agent_name, from_level, to_level)
    
    elif args.command == "handoff":
        from_level = get_level(args.from_agent)
        to_level = get_level(args.to_agent)
        completed = args.completed or []
        pending = args.pending or []
        artifacts = args.artifacts or []
        risks = args.risks or []
        instructions = args.instructions or []
        handoff_task(args.task, args.from_agent, args.to_agent, completed, pending, artifacts, risks, instructions)


if __name__ == "__main__":
    main()