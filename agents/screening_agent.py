"""AI Screening Agent — evaluates candidate applications."""

from __future__ import annotations

import json
from typing import Any

from core import ai_engine
from core.llm_engine import complete_json_safe
from core.prompts import SCREENING_SYSTEM, SCREENING_USER


def screen_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    fallback = _rule_based_screening(candidate)
    prompt = SCREENING_USER.format(candidate_json=json.dumps(candidate, indent=2))
    result = complete_json_safe(SCREENING_SYSTEM, prompt, fallback)

    score = int(result.get("score", fallback["score"]))
    score = max(0, min(100, score))
    decision = str(result.get("decision", fallback["decision"])).lower()
    if decision not in ("approve", "reject", "review"):
        decision = fallback["decision"]

    return {
        "score": score,
        "decision": decision,
        "suggested_role": str(result.get("suggested_role", fallback["suggested_role"])),
        "reasoning": str(result.get("reasoning", fallback["reasoning"])),
    }


def _rule_based_screening(candidate: dict[str, Any]) -> dict[str, Any]:
    skills = candidate.get("skills") or []
    motivation = (candidate.get("motivation") or "").strip()
    availability = (candidate.get("availability") or "").strip()

    score = 45
    score += min(len(skills) * 8, 24)
    if len(motivation) > 40:
        score += 15
    if availability:
        score += 10
    score = min(score, 92)

    decision = "approve" if score >= 70 else "review" if score >= 50 else "reject"
    role = "General Volunteer"
    if any("social" in s.lower() or "media" in s.lower() for s in skills):
        role = "Social Media Volunteer"
    elif any("teach" in s.lower() or "education" in s.lower() for s in skills):
        role = "Education Volunteer"

    return {
        "score": score,
        "decision": decision,
        "suggested_role": role,
        "reasoning": (
            f"Rule-based screening: {len(skills)} skill(s) listed, "
            f"{'strong' if len(motivation) > 40 else 'brief'} motivation, "
            f"{'availability provided' if availability else 'no availability detail'}."
        ),
    }
