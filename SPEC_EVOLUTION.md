# Spec Evolution

> [!NOTE]
> The public HaleES specification can grow without opening the private HaleES runtime.

## Current Focus

The current public focus is simple.

1. Make the contract format easier to understand.
2. Make the grading rubric easier to test.
3. Add public safe examples from real operational patterns.
4. Add reference validators that check public shape, not private logic.
5. Keep the boundary clear between open specification and closed runtime.

## Public Roadmap

| Area | Direction |
| --- | --- |
| Contracts | Clearer examples, safer authority language, better field definitions |
| Rubric | More pass and fail samples, clearer feedback examples, better review guidance |
| Examples | More scenarios across risk levels, privacy needs, and inference placement choices |
| Validators | Better public shape checks for contracts and grading results |
| Glossary | Clearer terms for authority, contract, grading, inference, privacy boundary, and audit |

## What Will Improve Over Time

The contract specification can improve through clearer examples, better field definitions, safer language around authority, and stronger distinction between recommendation and execution.

The grading rubric can improve through more calibration examples, clearer pass and fail cases, better feedback examples, and more guidance on when human review should happen.

The example library can improve through more operational scenarios that show different risk levels, privacy needs, and inference placement choices.

The reference validators can improve by checking whether a public contract includes the required sections and whether a public grading result includes the required score fields.

## What Will Not Be Opened Here

This public repository will not open the production Sensei OS runtime.

It will not open private model routing.

It will not open private memory implementation.

It will not open customer data, private datasets, deployment systems, commercial product code, or internal execution engines.

The public spec explains the pattern.

The private product remains the machine.

## Contribution Direction

Useful public contributions should improve clarity, examples, validator shape, documentation, or rubric calibration.

They should not include secrets, private data, private runtime details, or speculative claims.

The standard is simple.

Make the public pattern easier to understand without exposing what should stay protected.

[Back to README](README.md)
