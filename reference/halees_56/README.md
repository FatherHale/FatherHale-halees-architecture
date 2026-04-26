# HaleES-56 Public Reference Implementation

This folder contains a small deterministic reference implementation for the public HaleES-56 architecture.

It is meant to make the architecture inspectable and testable without publishing the closed HaleES production runtime.

## What This Code Shows

| File | Purpose |
| --- | --- |
| `agent_registry.py` | Public-safe metadata for the seven clusters and 56 agent profiles |
| `policy_gate.py` | Deterministic policy checks for authority, risk, approval, and missing evidence |
| `router.py` | Simple keyword router that maps hospitality signals to likely agent profiles |
| `workflow_examples.py` | Example governed workflows for call-offs, guest recovery, prep/waste, and refund review |
| `demo.py` | Runs the public examples and prints pass/review/block decisions |

## What This Code Is Not

| Not included | Reason |
| --- | --- |
| Production Sensei OS runtime | Closed commercial product engine |
| Proprietary grader | Private implementation |
| Internal prompts | Private operating instructions |
| Live integrations | Customer and adapter logic stays closed |
| LLM calls | This reference is deterministic and offline-safe |
| Secrets or environment variables | No credentials are required |

## Run

From the repository root:

```bash
python reference/halees_56/demo.py
```

Expected behavior: the demo routes public example events, checks policy conditions, and returns whether each scenario can proceed, requires human review, or is blocked.

## Design Rule

```text
Agent profile != permission to act
Recommendation != execution
Execution requires governance
```

[Back to main README](../../README.md) · [HaleES-56 Architecture](../../HALEES_56_HOSPITALITY_AGENT_ARCHITECTURE.md)
