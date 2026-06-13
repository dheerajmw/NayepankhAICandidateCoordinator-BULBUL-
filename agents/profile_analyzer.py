"""Profile Analyzer Agent — structures raw volunteer registration data."""

from __future__ import annotations

import json
from typing import Any

from core import ai_engine
from core.prompts import PROFILE_ANALYZER_SYSTEM, PROFILE_ANALYZER_USER


def analyze_profile(volunteer: dict[str, Any]) -> dict[str, Any]:
    if ai_engine.llm_configured():
        prompt = PROFILE_ANALYZER_USER.format(volunteer_json=json.dumps(volunteer, indent=2))
        result = ai_engine.complete_json(PROFILE_ANALYZER_SYSTEM, prompt)
        result["volunteer_id"] = volunteer["id"]
        return result

    return ai_engine.rule_based_profile(volunteer)


def analyze_profiles(volunteers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [analyze_profile(volunteer) for volunteer in volunteers]
