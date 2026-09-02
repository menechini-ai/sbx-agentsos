---
title: Tech Spec Template
description: Technical Specification template for Agent OS
---

# Tech Spec Template

## Purpose

The Technical Specification defines the technical approach for implementing a feature.

## Template

```markdown
# Tech Spec: [Feature Name]

## Overview
- **Feature**: [Name]
- **Status**: Draft/In Review/Approved
- **Owner**: [Architect Name]
- **Created**: YYYY-MM-DD

## Architecture

### High-Level Design
[Architecture diagram or description]

### Components
| Component | Responsibility |
|----------|----------------|
| [Component 1] | [Responsibility] |
| [Component 2] | [Responsibility] |

## Data Model

### Entities
```typescript
// Entity 1
interface Entity1 {
  id: string;
  name: string;
  createdAt: Date;
}
```

## API Design

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /api/resource | List resources |
| POST | /api/resource | Create resource |
| GET | /api/resource/:id | Get resource |
| PUT | /api/resource/:id | Update resource |
| DELETE | /api/resource/:id | Delete resource |

### Request/Response Examples
[Examples for each endpoint]

## Infrastructure

### Azure Resources
- Resource Group: [rg-name]
- AKS Cluster: [cluster-name]
- Azure SQL / Cosmos DB
- Key Vault
- Application Insights

### Configuration
```yaml
# Environment variables or config
DATABASE_URL: postgresql://...
AZURE_KEY_VAULT: https://...
```

## Security

- Authentication: OAuth 2.0 / Managed Identity
- Authorization: RBAC
- Secrets: Azure Key Vault
- Network: Private endpoints

## Non-Functional Requirements

| Requirement | Target |
|-------------|--------|
| Latency | < 200ms p99 |
| Throughput | 1000 req/s |
| Availability | 99.9% |
| Recovery | RTO 1h, RPO 15m |

## Testing Strategy

- Unit tests: > 80% coverage
- Integration tests: Critical paths
- E2E tests: Happy paths

## ADRs
- [ADR-001: Database choice](/architecture/adr-001)
```

## Related

- [ADR Template](/templates/adr)
- [Stories Template](/templates/stories)
- [Architecture Overview](/architecture/overview)