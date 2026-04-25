# Simple Contract Validator

This is public pseudocode.

It is not the HaleES production grader.

It is not the Sensei OS runtime.

It only shows how someone could think about validating the shape of a governed contract.

## Purpose

A contract should not be accepted if it is missing the basic parts needed for governed execution.

A simple public validator can check whether the contract includes the required sections before any model, tool, or workflow attempts the task.

## Required Sections

1. Objective.
2. Context.
3. Authority boundary.
4. Required output.
5. Acceptance criteria.
6. Decision rule.

## Pseudocode

```text
function validateContract(contract):
    requiredSections = [
        "objective",
        "context",
        "authority boundary",
        "required output",
        "acceptance criteria",
        "decision rule"
    ]

    missingSections = []

    for section in requiredSections:
        if contract does not contain section:
            add section to missingSections

    if missingSections is empty:
        return {
            valid: true,
            message: "Contract has the required public shape."
        }

    return {
        valid: false,
        message: "Contract is missing required sections.",
        missing: missingSections
    }
```

## Public Grading Shape

A public implementation can also check whether a grading result contains the expected categories.

```text
function validateGrade(grade):
    requiredScores = [
        "accuracy",
        "efficiency",
        "constraint adherence",
        "quality",
        "timeliness"
    ]

    for score in requiredScores:
        if grade does not contain score:
            return false

    if grade does not contain global score:
        return false

    if grade does not contain binary decision:
        return false

    return true
```

## Boundary

This document is intentionally simple.

It explains the public shape of the pattern.

It does not expose private scoring logic, model routing, authority checks, memory boundaries, execution queues, or production runtime internals.
