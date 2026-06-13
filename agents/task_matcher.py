"""Task Matching Agent — ranks volunteer–task fit."""

from __future__ import annotations

import json
from typing import Any

from core import ai_engine
from core.prompts import TASK_MATCHER_USER, TASK_MATCHER_SYSTEM


def rank_volunteers_for_task(
    task: dict[str, Any],
    volunteers: list[dict[str, Any]],
    profiles: list[dict[str, Any]],
    workload: dict[str, int],
) -> list[dict[str, Any]]:
    if not volunteers:
        return []

    if ai_engine.llm_configured():
        prompt = TASK_MATCHER_USER.format(
            task_json=json.dumps(task, indent=2),
            volunteers_json=json.dumps(profiles, indent=2),
            workload_json=json.dumps(workload, indent=2),
        )
        result = ai_engine.complete_json(TASK_MATCHER_SYSTEM, prompt)
        candidates = result.get("candidates", [])
        candidates.sort(key=lambda c: c.get("fit_score", 0), reverse=True)
        return candidates

    return ai_engine.rule_based_volunteer_rankings(task, volunteers, profiles, workload)


def rank_tasks_for_volunteer(
    volunteer: dict[str, Any],
    profile: dict[str, Any],
    open_tasks: list[dict[str, Any]],
    workload: int,
) -> list[dict[str, Any]]:
    if not open_tasks:
        return []

    if ai_engine.llm_configured():
        from core.prompts import VOLUNTEER_TASK_MATCHER_USER

        prompt = VOLUNTEER_TASK_MATCHER_USER.format(
            profile_json=json.dumps(profile, indent=2),
            tasks_json=json.dumps(open_tasks, indent=2),
            workload=workload,
        )
        result = ai_engine.complete_json(TASK_MATCHER_SYSTEM, prompt)
        recommendations = result.get("recommendations", [])
        recommendations.sort(key=lambda r: r.get("fit_score", 0), reverse=True)
        return recommendations[:2]

    return ai_engine.rule_based_task_recommendations(volunteer, profile, open_tasks, workload)
