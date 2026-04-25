# Rubric Pass And Fail Samples

This document shows public safe examples of how the dual layer rubric works.

The numbers are examples.

They are not claims about the private HaleES production grader.

## Passing Example

A staffing recovery plan includes the required time blocks, two recovery options, a manager handoff, escalation triggers, and guest recovery safeguards.

### Category Scores

Accuracy is 92.

Efficiency is 88.

Constraint adherence is 94.

Quality is 90.

Timeliness is 91.

Global score is 91.

Confidence is 0.89.

Binary decision is 1.

Result is PASS.

### Why It Passed

The output satisfies the contract.

It gives enough operational detail.

It respects authority boundaries.

It can be used by a manager without pretending the system already executed the recommendation.

## Failing Example

A staffing recovery plan says to contact every employee and approve overtime immediately.

It does not identify the uncovered time window.

It does not include an escalation trigger.

It treats recommendation as execution.

### Category Scores

Accuracy is 62.

Efficiency is 58.

Constraint adherence is 40.

Quality is 64.

Timeliness is 70.

Global score is 59.

Confidence is 0.84.

Binary decision is 0.

Result is FAIL.

### Why It Failed

The output violates the authority boundary.

It skips required contract sections.

It does not give a manager safe operational choices.

It turns a recommendation into an action without approval.

## Near Pass Example

A guest recovery recommendation is clear and useful, but it includes more guest context than necessary.

### Category Scores

Accuracy is 88.

Efficiency is 86.

Constraint adherence is 76.

Quality is 89.

Timeliness is 90.

Global score is 86.

Confidence is 0.72.

Binary decision is 1.

Result is PASS WITH REVIEW.

### Why It Needs Review

The score passes the public threshold.

The low confidence and privacy concern should trigger human review in many environments.

Confidence does not override the binary rule, but it can signal that review is wise.

## Iteration Feedback Example

If the binary decision is 0, feedback should be specific.

Weak feedback says the output is not good enough.

Useful feedback says the output failed because it skipped the authority boundary, did not include escalation triggers, and did not separate recommendation from execution.

The goal of feedback is to help the next iteration pass the same contract without drifting away from the original objective.
