# Failure Case: Authority Blocked By Core Policy

> [!IMPORTANT]
> Authority gives a user the right to request action. Policy decides whether that action is allowed.

## Scenario

A general manager asks HaleES to approve a schedule change that would place a minor outside the permitted work window.

The general manager has high authority inside the store.

The request still fails because the action violates a hard policy boundary.

## Contract

| Field | Value |
| --- | --- |
| Objective | Approve emergency schedule coverage |
| Actor role | General manager |
| Employee type | Minor |
| Action type | Schedule change |
| Risk level | High |
| Constitutional rule | Minor work restriction |
| Emergency override | Not allowed for legal boundary |

## Proposed Action

```json
{
  "action": "approve_schedule_change",
  "employee_type": "minor",
  "shift_window": "10:30 PM to 1:30 AM",
  "reason": "Emergency call off coverage"
}
```

## Enforcement Result

| Check | Result |
| --- | --- |
| Authority check | Pass |
| Constitutional policy check | Fail |
| Emergency override available | No |
| Grading score | 0 |
| Binary decision | 0 |
| Final action | Blocked |

## Audit Trace

```json
{
  "event_type": "policy_conflict",
  "actor_role": "general_manager",
  "attempted_action": "approve_minor_schedule_change",
  "blocked_by": "minor_work_restriction",
  "override_allowed": false,
  "binary_decision": 0,
  "next_step": "find_eligible_non_minor_employee"
}
```

## Corrected Recommendation

Do not schedule the minor.

Search for eligible non minor employees with the required role and availability.

If no eligible employee is available, escalate to the owner or authorized leader for a non violating operational recovery plan.

## Why This Matters

A high authority user can still make a request the system must reject.

HaleES separates role authority from permission to execute.
