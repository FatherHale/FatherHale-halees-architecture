<div align="center">

# HaleES Public Limitations

**What this repository proves, what it does not prove yet, and what remains closed.**

</div>

> [!IMPORTANT]
> This repository is a public architecture specification with reference examples. It should not be read as a finished SaaS runtime, customer deployment report, or independent benchmark claim.

## Current Public Scope

| Area | Public status | Plain meaning |
| --- | --- | --- |
| Architecture | Published | The system design can be inspected |
| HaleES-56 taxonomy | Published | The 56 agent profiles and clusters are public |
| Reference code | Published | Small deterministic examples can be run locally |
| Validators | Published | Public shape checks exist for contracts and grading results |
| Failure cases | Published | Example blocked/reviewed actions are documented |
| Production runtime | Closed | The real HaleES/Sensei OS engine is not published here |

## Known Limitations

| Limitation | Meaning | Why it matters |
| --- | --- | --- |
| No production runtime in this repo | The real execution engine is closed | Prevents confusing the public spec with the product |
| No independent benchmark results yet | There are no third-party performance numbers here | Avoids unsupported superiority claims |
| No customer case studies yet | Use cases are scenario models, not customer proof | Keeps the repo honest |
| No live integrations | POS, PMS, KDS, payroll, SMS, email, and vendor adapters are not included | Prevents leaking private implementation paths |
| No private grader implementation | Public validators show only shape and concept | Protects the core evaluation logic |
| No internal prompts | Agent files describe capabilities, not hidden runtime instructions | Avoids publishing private operating behavior |
| No operational dataset | No customer, employee, guest, transaction, or store data is included | Protects privacy and commercial data |
| No compliance certification | Governance concepts are included, but legal certification is not claimed | Prevents overstating safety or compliance |

## What The Reference Code Proves

The public reference code proves that the architecture can be represented as deterministic, inspectable structures:

| Public code path | What it demonstrates |
| --- | --- |
| `agent_registry.py` | The 56-agent taxonomy is structured and count-checkable |
| `router.py` | Signals can be routed to specialist profiles |
| `policy_gate.py` | Authority, evidence, and risk can produce pass/review/block decisions |
| `workflow_examples.py` | Public hospitality scenarios can be represented safely |
| `demo.py` | The reference behavior can run locally without secrets or LLM calls |

It does not prove production performance, model quality, integration reliability, or real-world business impact.

## Evidence Needed Later

| Evidence type | What would strengthen the repo |
| --- | --- |
| Automated tests | Repeatable proof that public examples behave as expected |
| Scenario benchmarks | Routing accuracy, false block rate, review rate, and audit completeness |
| Operator feedback | Hospitality managers reviewing whether the workflows are understandable |
| Field notes | Real operational observations without private customer data |
| Public demo adapters | Fake POS/KDS/payroll data showing integration shape without live systems |
| Independent review | External readers reproducing the public reference behavior |

## Boundary Statement

The public repo should be judged as an architecture specification with reference examples.

The closed HaleES runtime is the product engine. This repository is the public architecture layer.

[Back to README](README.md)
