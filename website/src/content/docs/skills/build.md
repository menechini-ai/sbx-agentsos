---
title: Build Skills
description: Skills for the Build phase - coding, dev-story, agentos-build
---

# Build Skills

Skills used during the **Build** phase by the Developer agent.

## coding

**Purpose**: General implementation workflow with testing and code review.

**Triggers**: "Implement...", "Write code for...", "Build..."

**Workflow**:
1. Review tech spec
2. Implement in source files
3. Write tests
4. Self-review
5. Report to QA

## dev-story

**Purpose**: Implement a single user story end-to-end.

**Triggers**: "Implement story...", "Build story...", "Work on story..."

**Output**: Working code + tests for one story, following the story's acceptance criteria.

## agentos-build

**Purpose**: Build orchestration - coordinate subagents, manage build pipeline.

**Triggers**: "Build the system...", "Orchestrate build...", "Coordinate build..."

**Workflow**:
1. Delegate to L4 subagents
2. Monitor progress
3. Collect results
4. Report to L2 Developer

## Usage

```
Developer: "Use dev-story for story 5"
→ Implements story 5 with tests

Developer: "Use coding for the auth module"
→ Implements auth module
```

## Related

- [Developer Agent](/agents/developer)
- [Delivery Loop](/architecture/delivery-loop)
- [Verify Skills](/skills/verify)