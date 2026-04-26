# Observability And Enforcement Telemetry

> [!IMPORTANT]
> Enforcement is only useful if the system can observe it.

HaleES should not only block unsafe or unauthorized actions. It should record why the action was blocked, what rule was involved, what context was available, what the agent attempted to do, and what should happen next.

Every enforcement event should create telemetry.

| Event type | What HaleES should capture |
| --- | --- |
| Approved action | Contract, authority, grading result, approval identity, final action |
| Blocked action | Violated rule, risk level, attempted action, suggested correction |
| Failed grading | Failed rubric category, score, binary gate result, feedback |
| Missing ground truth | Missing source, stale source, dependency state, required confirmation |
| Policy conflict | User authority, policy boundary, constitutional rule, override status |
| Identity failure | Active session, step up requirement, verification status |
| Emergency override | Trigger, reason, approver, scope, expiration, outcome |
| Outcome failure | Original action, post execution signal, consequence, future contract update |

## Why It Matters

The purpose of enforcement telemetry is not only compliance. It is system improvement.

If an agent is repeatedly blocked for the same reason, that signal should be reviewed.

The issue may be a weak prompt, a missing contract field, a poorly trained workflow, an unclear policy, a bad tool description, or a real operational pattern the system needs to understand better.

HaleES should treat blocked actions as learning events.

A blocked action should not disappear into a log file. It should become part of the system's operational intelligence.

## Questions The System Should Answer

| Question | Reason |
| --- | --- |
| Which actions are blocked most often | Identifies policy friction and unsafe workflows |
| Which agents fail the same constraints | Shows where reasoning or tooling needs correction |
| Which stores override recommendations too often | Detects approval drift and operating risk |
| Which policies create the most conflicts | Reveals unclear rules or real business pressure |
| Which workflows produce stale outputs | Finds bad data dependencies |
| Which external systems cause failed decisions | Exposes vendor or integration reliability problems |
| Which approvals happen too quickly | Detects rubber stamping and approval fatigue |

## Public Event Shape

```json
{
  "event_type": "blocked_action",
  "contract_id": "contract_labor_cut_001",
  "actor_role": "general_manager",
  "attempted_action": "reduce_front_desk_coverage",
  "blocked_by": "staffing_ratio_policy",
  "required_ratio": "1:8",
  "proposed_ratio": "1:15",
  "binary_decision": 0,
  "severity": "high",
  "next_step": "revise_plan_or_request_emergency_override"
}
```

## Design Position

A serious AI operating layer needs more than rules.

It needs telemetry around those rules.

HaleES should be able to show not only that an action was blocked, but why it was blocked, what it means, and how that signal improves future operation.
