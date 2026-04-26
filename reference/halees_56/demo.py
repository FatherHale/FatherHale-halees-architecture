"""Run the public HaleES-56 reference demo.

Usage:
    python reference/halees_56/demo.py
"""

from __future__ import annotations

from agent_registry import validate_registry
from policy_gate import evaluate_request
from router import route_signal
from workflow_examples import EXAMPLES


def main() -> None:
    validate_registry()
    print("HaleES-56 public reference demo")
    print("=" * 38)

    for index, request in enumerate(EXAMPLES, start=1):
        routed_agents = route_signal(request.description)
        decision = evaluate_request(request)

        print(f"\nExample {index}: {request.metadata.get('workflow', 'unknown')}")
        print(f"Signal: {request.description}")
        print("Routed agents:")
        for agent in routed_agents:
            print(f"  - {agent.name} [{agent.cluster}] risk={agent.risk_level}")
        print(f"Gate decision: {decision.decision.upper()} binary={decision.binary}")
        print(f"Reason: {decision.reason}")
        print(f"Next step: {decision.required_next_step}")


if __name__ == "__main__":
    main()
