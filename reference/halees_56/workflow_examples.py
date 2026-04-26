"""Public HaleES-56 workflow examples.

These examples show deterministic governance flow only.
They do not represent live HaleES production workflows.
"""

from __future__ import annotations

from policy_gate import WorkRequest


EXAMPLES: tuple[WorkRequest, ...] = (
    WorkRequest(
        description="Server called off two hours before dinner rush. Find coverage and draft outreach.",
        requested_agent="Call-Off Coverage Agent",
        actor_role="manager",
        risk_level="high",
        has_ground_truth=True,
        asks_to_execute=False,
        requires_manager_approval=True,
        metadata={"workflow": "call_off_coverage"},
    ),
    WorkRequest(
        description="Guest complaint requests a refund after a service failure.",
        requested_agent="Guest Recovery Agent",
        actor_role="shift_lead",
        risk_level="high",
        has_ground_truth=True,
        asks_to_execute=True,
        contains_private_data=True,
        requires_manager_approval=True,
        metadata={"workflow": "guest_recovery"},
    ),
    WorkRequest(
        description="Prep list needs adjustment but inventory count is stale.",
        requested_agent="Prep Production Agent",
        actor_role="manager",
        risk_level="medium",
        has_ground_truth=False,
        asks_to_execute=False,
        metadata={"workflow": "prep_and_waste"},
    ),
    WorkRequest(
        description="Low-risk task assignment for closing checklist follow-up.",
        requested_agent="Task Management Agent",
        actor_role="manager",
        risk_level="low",
        has_ground_truth=True,
        asks_to_execute=False,
        metadata={"workflow": "task_management"},
    ),
)
