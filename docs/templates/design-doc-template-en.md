# Design: <topic>

**Date**: YYYY-MM-DD
**Owner**:
**Status**: Draft / Reviewing / Locked
**Source project / branch**:
**Related research / code walkthrough / review**:

## Revision History

| Version | Date | Author | Summary |
|---|---|---|---|
| v0.1 | YYYY-MM-DD |  | Initial draft. |

## 1. Summary

- What problem this design solves:
- Chosen direction:
- Expected outcome:
- What an AI Agent should be able to implement from this document:

## 2. Context and Goals

- Current state:
- Pain points / motivation:
- Goals:
- Non-goals:
- Constraints:
- Success criteria:

## 3. Current System Alignment

| Area / module | Current behavior | Design impact |
|---|---|---|
|  |  |  |

## 4. Candidate Options

| Option | Core idea | Strengths | Weaknesses / Risks | Judgment |
|---|---|---|---|---|
| A |  |  |  |  |
| B |  |  |  |  |
| C |  |  |  |  |

## 5. Decision

**Chosen option**:

**Why this option**:

**Why the other options were rejected**:

- A:
- B:
- C:

**Consequences / trade-offs**:

- What becomes simpler:
- What becomes harder:
- Follow-up decisions this may create:

## 6. Detailed Design

### 6.1 Architecture / Flow

```text
[component / caller]
  -> [new or changed module]
  -> [state / storage / external system]
```

### 6.2 Data / State Model

- New or changed fields:
- Ownership / lifecycle:
- Migration / backfill:
- Compatibility:

### 6.3 API / CLI / Interface Changes

- Public interface:
- Internal interface:
- Input validation:
- Output / error shape:

### 6.4 Key Flows

| Flow | Entry point | Steps | Result |
|---|---|---|---|
|  |  |  |  |

### 6.5 Error Handling and Edge Cases

- Expected errors:
- Retry / timeout behavior:
- Partial failure behavior:
- Concurrency / ordering:
- Idempotency:

### 6.6 Observability and Operations

- Logs:
- Metrics:
- Alerts:
- Debug commands / queries:
- Rollback / disable switch:

## 7. Implementation and Verification Plan

> Implementation and tests belong together. Keep each phase concrete enough that an AI Agent can implement, verify, and stop at the phase boundary without inventing scope.

### Phase 1: <phase name>

**Goal**:

**Implementation scope**:

- [ ] File / module:
- [ ] File / module:

**Data / migration changes**:

- [ ] 

**Agent instructions**:

- Must follow:
- Must not do:
- Ask before deciding:

**Verification for this phase**:

- Automated tests:
- Manual / workflow verification:
- Regression checks:
- Failure / edge-case checks:

**Exit criteria**:

- [ ] 

### Phase 2: <phase name>

**Goal**:

**Implementation scope**:

- [ ] File / module:
- [ ] File / module:

**Data / migration changes**:

- [ ] 

**Agent instructions**:

- Must follow:
- Must not do:
- Ask before deciding:

**Verification for this phase**:

- Automated tests:
- Manual / workflow verification:
- Regression checks:
- Failure / edge-case checks:

**Exit criteria**:

- [ ] 

### Phase 3: <phase name>

**Goal**:

**Implementation scope**:

- [ ] File / module:
- [ ] File / module:

**Data / migration changes**:

- [ ] 

**Agent instructions**:

- Must follow:
- Must not do:
- Ask before deciding:

**Verification for this phase**:

- Automated tests:
- Manual / workflow verification:
- Regression checks:
- Failure / edge-case checks:

**Exit criteria**:

- [ ] 

### Overall Acceptance

| Acceptance area | What to verify | Command / method | Required before merge |
|---|---|---|---|
| Unit / component |  |  | Yes / No |
| Integration / workflow |  |  | Yes / No |
| End-to-end / operational |  |  | Yes / No |
| Regression |  |  | Yes / No |
| Rollback / compatibility |  |  | Yes / No |

**Required test data / fixtures**:

**Performance / scale checks**:

**Backward compatibility checks**:

**Failure injection / negative tests**:

## 8. Rollout and Rollback

- Rollout sequence:
- Feature flag / config gate:
- Deployment order:
- Monitoring during rollout:
- Rollback steps:
- Data cleanup if rollback happens:

## 9. Risks and Mitigations

| Risk | Impact | Mitigation | Test / signal |
|---|---|---|---|
|  |  |  |  |

## 10. AI Agent Handoff Checklist

- [ ] The changed files/modules are named explicitly.
- [ ] Each phase combines implementation scope, verification, and exit criteria.
- [ ] Overall acceptance names required commands or manual checks.
- [ ] Risky decisions are marked as "ask before deciding".
- [ ] Non-goals are explicit enough to prevent scope creep.

## 11. Open Questions

- [ ] 
