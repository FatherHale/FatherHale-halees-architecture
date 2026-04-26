<div align="center">

# HaleES-56 Public Example Inputs

**Public-safe JSON scenarios for the HaleES-56 reference implementation.**

</div>

> [!IMPORTANT]
> These examples are scenario inputs, not customer data, not production logs, and not benchmark results.

## Example Files

| Scenario | File | Expected result |
| --- | --- | --- |
| Same-day call-off coverage | [call_off_coverage.json](call_off_coverage.json) | Review |
| Guest refund review | [guest_refund_review.json](guest_refund_review.json) | Review |
| Stale inventory prep change | [stale_inventory_prep_block.json](stale_inventory_prep_block.json) | Block |

## Scenario Shape

Each JSON file uses the same public shape:

| Field | Meaning |
| --- | --- |
| `signal` | The operational event being evaluated |
| `expected_agents` | Specialist profiles likely involved |
| `actor_role` | Public-safe role label |
| `risk_level` | Low, medium, or high |
| `has_ground_truth` | Whether the necessary source evidence is present |
| `asks_to_execute` | Whether the request is trying to perform an action |
| `contains_private_data` | Whether private context is involved |
| `requires_manager_approval` | Whether human review is expected |
| `expected_gate_decision` | Expected public result: pass, review, or block |
| `evidence_needed` | Inputs needed before an action should be trusted |

## Why These Exist

The examples make the architecture concrete. They show how a hospitality signal becomes an evidence-aware, governed decision instead of a vague agent response.

[Back to README](../../README.md) · [HaleES-56 Reference Implementation](../../reference/halees_56/README.md)
