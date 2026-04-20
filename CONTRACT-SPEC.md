# HaleES Public Contract Specification

This document defines a public, implementation-agnostic Markdown contract format for governed AI execution in HaleES-style systems.

A contract is the authoritative work definition for a task. It establishes scope, boundaries, acceptance requirements, grading targets, and iteration behavior.

---

## 1) Contract Format Overview

Use this template for each task contract.

```md
# Contract: <contract_title>

## Metadata (Required)
- contract_id: <string>
- version: <string>
- created_at_utc: <ISO-8601 timestamp>
- orchestrator: <role or system id>
- requester_role: <string>
- domain: <string>
- risk_level: <low|medium|high>

## Objective (Required)
<Clear statement of the intended deliverable and operational context.>

## Inputs (Required)
- <input_1>
- <input_2>
- ...

## Constraints (Required)
- <constraint_1>
- <constraint_2>
- ...

## Acceptance Criteria (Required)
- [ ] <criterion_1>
- [ ] <criterion_2>
- ...

## Expected Output Format (Required)
- format: <markdown|json|table|mixed>
- required_sections:
  - <section_1>
  - <section_2>
- max_length: <optional length guidance>

## Grading Target (Required)
- rubric: halees-dual-layer-v1
- threshold_global_score: 85
- binary_pass_rule: global_score >= 85 -> 1 else 0
- confidence_tracking: required (0..1)

## Iteration Rules (Required)
- max_iterations: 5
- failure_behavior: append_feedback_and_retry
- stop_condition_pass: binary_decision = 1
- stop_condition_fail: iteration_count > max_iterations

## Optional Fields
- dependencies:
  - <dependency>
- preferred_method:
  - <method hint>
- escalation_path:
  - <role/process>
- notes:
  - <additional context>
```

---

## 2) Required Fields

A valid public contract must include:

- Metadata block
- Objective
- Inputs
- Constraints
- Acceptance Criteria
- Expected Output Format
- Grading Target
- Iteration Rules

If any required field is missing, the contract should be rejected as incomplete.

---

## 3) Optional Fields

Optional fields allow context enrichment without changing governance semantics:

- dependencies
- preferred_method
- escalation_path
- notes

Optional fields may guide implementation choices but cannot override required constraints or grading logic.

---

## 4) Acceptance Criteria Guidance

Acceptance criteria should be:

- specific and verifiable,
- operationally relevant,
- free from contradictory requirements,
- scoped to the contract objective.

Avoid vague criteria such as “looks good.” Prefer testable criteria such as “includes two contingency options with trigger conditions.”

---

## 5) Constraints Guidance

Constraints define hard boundaries and must be explicit (policy, scope, allowed assumptions, output limits).

Examples:

- “Use only provided staffing and availability inputs.”
- “Do not include private guest data.”
- “Provide actions executable within one shift window.”

If constraints conflict with acceptance criteria, orchestrator clarification is required before execution.

---

## 6) Expected Output Format Guidance

Specify:

- output format type,
- required sections,
- structure and naming,
- length expectations (if needed).

This prevents grading ambiguity and supports consistent machine/human evaluation.

---

## 7) Grading Target

All contracts using this public spec target:

- five-category scoring (0–100 per category),
- computed global_score,
- threshold at 85,
- binary_decision derived from threshold,
- confidence tracked separately (0–1).

---

## 8) Iteration Rules

Default iteration loop:

1. Execute against contract.
2. Grade result.
3. If pass (`binary_decision = 1`), finalize.
4. If fail (`binary_decision = 0`), append feedback and retry.
5. Stop at max 5 iterations by default.

---

## 9) Example Contract (Public-Safe Hospitality)

# Contract: Manager Call-Off Coverage Plan

## Metadata (Required)
- contract_id: HC-2026-04-20-001
- version: 1.0
- created_at_utc: 2026-04-20T10:30:00Z
- orchestrator: sensei-control-plane
- requester_role: Operations Manager
- domain: hospitality_operations
- risk_level: medium

## Objective (Required)
Create a same-day manager call-off coverage plan for evening service that preserves service quality and policy compliance.

## Inputs (Required)
- Evening shift is 4:00 PM–11:00 PM.
- One floor manager called off at 9:20 AM.
- Available backup supervisors: Alex (4:00–8:00), Jordan (6:00–11:00).
- Predicted guest volume is high between 6:30 PM and 9:00 PM.
- Existing pre-shift briefing is at 3:30 PM.

## Constraints (Required)
- Do not assume additional staffing outside provided names.
- Keep plan executable within today’s shift only.
- Include a handoff strategy for 8:00 PM transition.
- Do not include private employee personal details.

## Acceptance Criteria (Required)
- [ ] Includes primary coverage plan with time blocks.
- [ ] Includes at least one contingency branch.
- [ ] Defines escalation trigger conditions.
- [ ] Includes guest-service risk mitigation actions.
- [ ] Uses concise manager-ready language.

## Expected Output Format (Required)
- format: markdown
- required_sections:
  - Situation Summary
  - Coverage Plan
  - Contingency Plan
  - Escalation Triggers
  - Guest Recovery Safeguards
  - Final Checklist
- max_length: 500 words

## Grading Target (Required)
- rubric: halees-dual-layer-v1
- threshold_global_score: 85
- binary_pass_rule: global_score >= 85 -> 1 else 0
- confidence_tracking: required (0..1)

## Iteration Rules (Required)
- max_iterations: 5
- failure_behavior: append_feedback_and_retry
- stop_condition_pass: binary_decision = 1
- stop_condition_fail: iteration_count > max_iterations

## Optional Fields
- preferred_method:
  - prioritize continuity during 6:30–9:00 PM peak
- notes:
  - optimize for service stability over process novelty

---

## 10) Example Filled Agent Output

### Situation Summary
A floor manager call-off creates a coverage gap for evening service. Peak demand is expected from 6:30 PM to 9:00 PM, with existing backup supervisor windows split across the shift.

### Coverage Plan
- 3:30 PM briefing: confirm role split and escalation contacts.
- 4:00 PM–6:00 PM: Alex leads floor coordination and pre-peak setup.
- 6:00 PM–8:00 PM: Alex and Jordan overlap; Jordan shadows active priorities and assumes escalation ownership.
- 8:00 PM–11:00 PM: Jordan leads full coverage after structured handoff.

### Contingency Plan
If service queue exceeds target thresholds by 7:00 PM, reassign one senior host to floor support for guest flow updates and manager communication relay.

### Escalation Triggers
Escalate to duty executive if two or more of the following occur simultaneously for 20+ minutes: extended wait spikes, unresolved guest complaints, or critical station backlog.

### Guest Recovery Safeguards
Use proactive guest communication at wait-time checkpoints and authorize service recovery options per policy when delay thresholds are exceeded.

### Final Checklist
- Coverage roles confirmed at briefing.
- 8:00 PM handoff checklist completed.
- Escalation conditions posted for team leads.

---

## 11) Example Feedback After Failure (binary_decision = 0)

Iteration 1 feedback:

- Add explicit time-bound contingency trigger (current trigger too vague).
- Add one additional risk mitigation action for guest complaints during 6:30–9:00 PM peak.
- Clarify escalation threshold with measurable duration.

Required revision goal: improve accuracy and constraint_adherence to reach threshold.

---

## 12) Example Pass Result (binary_decision = 1)

- iteration: 2
- global_score: 89
- confidence: 0.88
- binary_decision: 1
- result: PASS

Finalized output accepted for operational use.
