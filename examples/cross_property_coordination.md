# Cross Property Coordination Example

This is a public safe example of how HaleES can support pattern level learning without exposing private property data.

## Objective

Create a cross property staffing insight that helps operators prepare for a known demand pattern.

## Context

Multiple properties may experience similar demand pressure during major events, weather shifts, holidays, or local traffic patterns.

The system should identify a useful operational pattern without exposing private data from one property to another.

## Authority Boundary

The system may describe a generalized demand pattern.

The system may recommend preparation steps.

The system may not reveal one property private staffing data to another property.

The system may not expose private sales, guest, employee, or manager information.

The system may not create schedule changes without local authority.

## Required Output

1. Generalized pattern summary.
2. Operational risk.
3. Recommended preparation steps.
4. Local manager decision points.
5. Data boundary statement.

## Acceptance Criteria

1. The output explains the pattern without exposing private property details.
2. The output gives practical preparation steps.
3. The output separates generalized insight from local execution.
4. The output names what must be decided by the local property.
5. The output avoids implying that cross property learning overrides local authority.

## Grading Shape

Accuracy measures whether the pattern is described correctly.

Efficiency measures whether the recommendation helps operators act quickly.

Constraint adherence measures whether privacy and property boundaries are respected.

Quality measures whether the guidance is clear and operationally useful.

Timeliness measures whether the guidance can be used before the demand window.

## Decision Rule

The global score must be 85 or higher.

If the score is below 85, the output should iterate with feedback focused on privacy, clarity, and local authority.
