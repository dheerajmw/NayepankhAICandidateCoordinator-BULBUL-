"""Admin Action Agent — assists approve/reject decisions."""

from __future__ import annotations

import json
from typing import Any

from core.llm_engine import complete_json_safe
from core.prompts import ADMIN_DECISION_SYSTEM, ADMIN_DECISION_USER


def assist_admin_decision(
    candidate: dict[str, Any],
    screening: dict[str, Any] | None,
) -> dict[str, Any]:
    screening = screening or {}
    fallback = _rule_based_decision(candidate, screening)
    prompt = ADMIN_DECISION_USER.format(
        candidate_json=json.dumps(candidate, indent=2),
        screening_json=json.dumps(screening, indent=2),
    )
    result = complete_json_safe(ADMIN_DECISION_SYSTEM, prompt, fallback)

    recommendation = str(result.get("recommendation", fallback["recommendation"])).lower()
    if recommendation not in ("approve", "reject"):
        recommendation = fallback["recommendation"]

    return {
        "recommendation": recommendation,
        "confidence": int(result.get("confidence", fallback["confidence"])),
        "summary": str(result.get("summary", fallback["summary"])),
        "key_strengths": result.get("key_strengths", fallback["key_strengths"]),
        "concerns": result.get("concerns", fallback["concerns"]),
    }


def _rule_based_decision(
    candidate: dict[str, Any],
    screening: dict[str, Any],
) -> dict[str, Any]:
    score = int(screening.get("score", 50))
    decision = screening.get("decision", "review")
    skills = candidate.get("skills") or []

    if decision == "approve" or score >= 70:
        rec = "approve"
        confidence = score
    elif decision == "reject" or score < 45:
        rec = "reject"
        confidence = 100 - score
    else:
        rec = "approve" if score >= 55 else "reject"
        confidence = abs(score - 50) + 40

    strengths = [f"{len(skills)} skills listed"]
    if candidate.get("motivation"):
        strengths.append("Motivation statement provided")
    concerns = []
    if score < 60:
        concerns.append("Moderate screening score — review carefully")
    if not candidate.get("availability"):
        concerns.append("Availability not specified")

    return {
        "recommendation": rec,
        "confidence": min(confidence, 95),
        "summary": f"AI screening score {score}/100 with decision '{decision}'.",
        "key_strengths": strengths,
        "concerns": concerns or ["None flagged"],
    }
