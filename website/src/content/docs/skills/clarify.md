---
title: Clarify Skills
description: Skills for the Clarify phase - brainstorming, brief-creation, prd-writing
---

# Clarify Skills

Skills used during the **Clarify** phase by the PM agent.

## brainstorming

**Purpose**: Explore user intent, requirements, and design before implementation.

**Triggers**: "Let's build...", "I want to add...", "How should we...", "Design..."

**Workflow**:
1. Classify request (Spike/Bounded/Architectural)
2. Ask clarifying questions (one at a time)
3. Propose 2-3 approaches with trade-offs
4. Present design sections, get approval
5. Write spec doc (architectural) or implement (bounded)

## brief-creation

**Purpose**: Create structured briefs with Objective, Constraints, and Success Criteria.

**Triggers**: "Create brief for...", "What's the objective?", "Define requirements..."

**Output**: `brief.md` with:
- Objective (1-2 sentences)
- Constraints (timeline, budget, tech)
- Success Criteria (3-5 measurable metrics)
- Stakeholders

## prd-writing

**Purpose**: Write Product Requirements Documents with MoSCoW features and acceptance criteria.

**Triggers**: "Write PRD for...", "Document requirements...", "Feature spec..."

**Output**: `prd.md` with:
- Features (MUST/SHOULD/COULD/WON'T)
- User stories with acceptance criteria
- Non-functional requirements
- Dependencies

## Usage

```
PM: "Use brief-creation for the new dashboard feature"
→ Creates brief.md

PM: "Use prd-writing for the dashboard PRD"
→ Creates prd.md
```

## Related

- [PM Agent](/agents/pm)
- [Delivery Loop](/architecture/delivery-loop)
- [Plan Skills](/skills/plan)