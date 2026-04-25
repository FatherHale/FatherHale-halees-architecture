"""
Simple public contract validator for the HaleES Architecture Specification.

This is not the HaleES production runtime.
This is not the private grader.
This only checks whether a public contract includes the required visible sections.
"""

from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "objective",
    "context",
    "authority boundary",
    "required output",
    "acceptance criteria",
    "decision rule",
]


def normalize(text: str) -> str:
    return text.lower().replace("_", " ")


def validate_contract(text: str) -> dict:
    normalized = normalize(text)
    missing = [section for section in REQUIRED_SECTIONS if section not in normalized]

    return {
        "valid": len(missing) == 0,
        "missing_sections": missing,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validators/contract_validator.py path_to_contract.md")
        return 2

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"File not found: {path}")
        return 2

    result = validate_contract(path.read_text(encoding="utf-8"))

    if result["valid"]:
        print("Contract shape is valid.")
        return 0

    print("Contract shape is incomplete.")
    print("Missing sections:")
    for section in result["missing_sections"]:
        print(f"{section}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
