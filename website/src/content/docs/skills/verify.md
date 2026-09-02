---
title: Verify Skills
description: Skills for the Verify phase - qa-gate, review, testing
---

# Verify Skills

Skills used during the **Verify** phase by the QA agent and SRE.

## qa-gate

**Purpose**: Execute the quality verification gate before deployment.

**Triggers**: "Run QA gate...", "Verify deployment...", "Quality check..."

**Checklist**:
- [ ] All unit tests pass
- [ ] Integration tests pass
- [ ] Linter clean
- [ ] No security vulnerabilities
- [ ] Acceptance criteria met
- [ ] Documentation updated
- [ ] Tech spec compliance

**Output**: QA gate result (PASS/FAIL) with detailed findings.

## review

**Purpose**: Code/technical review against spec and quality standards.

**Triggers**: "Review this code...", "Code review...", "Technical review..."

**Workflow**:
1. Compare implementation vs tech spec
2. Check code quality
3. Verify tests cover acceptance criteria
4. Report findings (pass with comments, or fail with blockers)

## Usage

```
QA: "Use qa-gate for story 5"
→ Returns PASS/FAIL with details

QA: "Use review for the auth module"
→ Returns review comments
```

## Related

- [QA Agent](/agents/qa)
- [Developer Agent](/agents/developer)
- [Delivery Loop](/architecture/delivery-loop)
- [Build Skills](/skills/build)