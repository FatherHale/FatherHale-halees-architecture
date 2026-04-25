# Quickstart

This quickstart shows the public reference material.

It does not run the HaleES production runtime.

It does not run the private grader.

It only runs public examples, shape validators, and the mock loop.

## Run The Mock Loop

From the repository root, run this command.

```bash
python reference/end_to_end_mock_loop.py
```

The script shows a simple public flow.

Contract.

Mock execution.

Dummy grading.

Binary decision.

Feedback.

Iteration.

Pass or fail.

## Validate A Markdown Contract Shape

From the repository root, run this command.

```bash
python validators/contract_validator.py examples/staffing_recovery_contract.md
```

This checks whether the markdown contract includes the public required sections.

It does not score the work.

It does not reproduce the HaleES runtime.

## Validate A Grading Result Shape

From the repository root, run this command.

```bash
python validators/grading_validator.py examples/sample_grading_result.json
```

This checks whether the grading result includes the required public fields and whether the binary decision matches the threshold rule.

It does not reproduce the private HaleES grader.

## Review The JSON Schemas

The schemas folder contains public JSON Schemas for the visible contract shape and grading result shape.

1. schemas/contract.schema.json
2. schemas/grading_result.schema.json

These schemas are public reference material.

They are not the private production schema system.

## Boundary

This quickstart exists so people can touch the public pattern quickly.

The production HaleES runtime, private grading implementation, private routing, private memory boundaries, and private execution engine remain closed.
