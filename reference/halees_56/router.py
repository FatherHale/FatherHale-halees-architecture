"""Simple public router for HaleES-56 reference examples.

This module maps text signals to public agent profiles using deterministic keywords.
It is intentionally small and transparent.
"""

from __future__ import annotations

from agent_registry import AGENTS, AgentProfile


KEYWORDS: dict[str, tuple[str, ...]] = {
    "Call-Off Coverage Agent": ("call-off", "called off", "no show", "missed shift", "coverage"),
    "Scheduling Agent": ("schedule", "shift", "availability", "coverage"),
    "Labor Cost Agent": ("labor", "overtime", "sales per labor", "cut hours"),
    "Guest Recovery Agent": ("complaint", "refund", "angry guest", "bad review", "service failure"),
    "Guest Concierge Agent": ("guest request", "concierge", "reservation request", "amenity"),
    "Prep Production Agent": ("prep", "par", "production", "shortage"),
    "Waste / Variance Agent": ("waste", "variance", "shrink", "overproduction"),
    "Inventory Agent": ("inventory", "stock", "count", "out of stock"),
    "Payments / Billing Agent": ("payment", "billing", "refund", "chargeback", "void"),
    "POS / PMS / KDS Integration Agent": ("pos", "pms", "kds", "ticket time", "integration"),
    "Device Lock / Kiosk Agent": ("kiosk", "device", "lock", "terminal"),
    "Bar / Alcohol Compliance Agent": ("bar", "alcohol", "beer", "liquor", "id check"),
}


def route_signal(signal: str) -> list[AgentProfile]:
    """Return likely agent profiles for a hospitality signal."""

    normalized = signal.lower()
    matches: list[AgentProfile] = []

    for agent_name, words in KEYWORDS.items():
        if any(word in normalized for word in words):
            agent = next((candidate for candidate in AGENTS if candidate.name == agent_name), None)
            if agent and agent not in matches:
                matches.append(agent)

    if not matches:
        fallback = next(agent for agent in AGENTS if agent.name == "Analysis Agent")
        matches.append(fallback)

    return matches
