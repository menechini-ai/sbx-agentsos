#!/usr/bin/env python3
"""
Capture Session Script

Captures the current state of a task session for handoff between agents or
between sessions. Creates a handoff report based on the task envelope and
results produced.

Usage:
    python capture-session.py --task_id TASK-2026-0001 --output results.json

Or integrate as a module:
    from scripts.capture_session import capture_session
    report = capture_session(task_id="TASK-2026-0001")
"""

import json
import sys
import os
from datetime import datetime


def capture_session(task_id, output_file=None):
    """
    Capture the session state for a given task ID.
    
    This script:
    1. Reads the task envelope from contracts/input/
    2. Reads the result envelope from contracts/output/
    3. Records learnings and candidates
    4. Produces a handoff-ready report
    
    Args:
        task_id: The task ID to capture (e.g., "TASK-2026-0001")
        output_file: Optional path to write the report to
    
    Returns:
        dict: The captured session report
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_root = os.path.dirname(base_dir)
    
    report = {
        "session_id": f"SESSION-{task_id}",
        "task_id": task_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "from_agent": None,
        "completed": [],
        "pending": [],
        "artifacts": [],
        "risks": [],
        "instructions": [],
        "learnings": [],
        "improvement_candidates": [],
    }
    
    # Read task envelope
    task_envelope_path = os.path.join(project_root, "agentsos", "contracts", "input", f"task-envelope-{task_id.replace('TASK-', '').replace('-', '')}.json")
    # For now, read the sample envelope
    sample_envelope_path = os.path.join(project_root, "agentsos", "contracts", "input", "task-envelope.json")
    
    if os.path.exists(sample_envelope_path):
        with open(sample_envelope_path, "r") as f:
            envelope = json.load(f)
        report["from_agent"] = envelope["task"]["sender"]["agent"]
    
    # Read result envelope
    result_path = os.path.join(project_root, "agentsos", "contracts", "output", "result-envelope.json")
    if os.path.exists(result_path):
        with open(result_path, "r") as f:
            result = json.load(f)
        
        report["completed"] = result["result"]["summary"]
        report["artifacts"] = result["result"]["changes"]["files"]
        report["risks"] = result["result"]["risks"]
        report["improvement_candidates"] = result["result"].get("improvement_candidates", [])
        
        # Extract learnings
        for mc in result["result"].get("memory_candidates", []):
            report["learnings"].append({
                "type": mc["type"],
                "description": mc["description"]
            })
    
    # Set timestamp
    report["timestamp"] = datetime.utcnow().isoformat() + "Z"
    
    # Write output if requested
    if output_file:
        with open(output_file, "w") as f:
            json.dump(report, f, indent=2)
    
    return report


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Capture session state")
    parser.add_argument("--task_id", required=True, help="Task ID to capture")
    parser.add_argument("--output", help="Output file path")
    
    args = parser.parse_args()
    
    report = capture_session(args.task_id, args.output)
    
    if args.output:
        print(f"Session report written to {args.output}")
    else:
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()