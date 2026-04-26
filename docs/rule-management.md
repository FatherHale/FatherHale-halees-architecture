# Managing Enforcement Rules At Scale

> [!IMPORTANT]
> A governed system cannot depend on an engineer for every policy change.

In hospitality, operating rules change often. Labor targets change. Store hours change. Roles change. Brand standards change. Minor restrictions change. Vendor conditions change. Menu availability changes. Emergency procedures change.

If every rule update requires a developer, the system will not scale.

HaleES should separate rule ownership from code ownership.

## Ownership Model

| Layer | Primary owner | Responsibility |
| --- | --- | --- |
| Enforcement engine | Engineering | Runtime, schema, validators, permissions, integrations |
| Constitutional rules | Owner, corporate, compliance | Hard rules that normal users cannot bypass silently |
| Store operating rules | Owner or general manager | Local thresholds, service model, escalation paths |
| Shift level preferences | Manager | Day specific context inside approved boundaries |
| Emergency rules | Authorized leader | Temporary downshift, safe mode, override scope |

## Operator Managed Rules

Operators should be able to manage approved business rules through controlled interfaces.

This can include policy templates, store level overrides, role based permissions, approval thresholds, staffing ratios, automation limits, vendor dependency requirements, and escalation rules.

Not every operator should be able to change every rule.

Rule management itself must be governed.

A general manager may be allowed to adjust local staffing preferences within a permitted range.

An owner may be allowed to define approval thresholds and automation limits.

A compliance or corporate role may control hard policy boundaries.

## Rule Change Audit

Every rule change should create an audit record.

| Field | Purpose |
| --- | --- |
| Rule changed | Identifies the affected control |
| Previous value | Preserves history |
| New value | Shows the new operating state |
| Changed by | Connects the change to a verified identity |
| Reason | Explains why the change was made |
| Effective time | Shows when the rule began applying |
| Affected workflows | Shows what the rule can influence |
| Review requirement | Determines whether another approval is required |

## Public Rule Shape

```json
{
  "rule_id": "luxury_front_desk_ratio",
  "rule_type": "staffing_ratio",
  "scope": "property_type:luxury",
  "minimum_ratio": "1:8",
  "editable_by": ["owner", "compliance_admin"],
  "emergency_override_allowed": true,
  "override_requires_reason": true,
  "override_requires_step_up_auth": true,
  "audit_required": true
}
```

## Design Position

The long term goal is not for engineers to hand code every operating rule.

The goal is a controlled policy layer where business leaders can define how their operation should run while the system enforces those rules consistently.
