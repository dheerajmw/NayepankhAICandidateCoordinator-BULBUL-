"""AI Task Matching Agent — matches volunteers to NGO tasks."""

from __future__ import annotations

import json
from typing import Any

from core import ai_engine
from core.llm_engine import complete_json_safe
from core.prompts import COORDINATOR_SYSTEM, TASK_MATCHING_V2_USER


def match_volunteers_to_task(
    task: dict[str, Any],
    volunteers: list[dict[str, Any]],
    workload: dict[str, int],
) -> list[dict[str, Any]]:
    if not volunteers:
        return []

    memory = {v["id"]: v.get("memory", {}) for v in volunteers}
    fallback = _rule_based_matches(task, volunteers, workload)

    prompt = TASK_MATCHING_V2_USER.format(
        task_json=json.dumps(task, indent=2),
        volunteers_json=json.dumps(volunteers, indent=2),
        memory_json=json.dumps(memory, indent=2),
        workload_json=json.dumps(workload, indent=2),
    )
    result = complete_json_safe(
        COORDINATOR_SYSTEM,
        prompt,
        {"matches": fallback},
    )
    matches = result.get("matches", fallback)
    matches.sort(key=lambda m: m.get("fit_score", 0), reverse=True)
    return matches[:5]


def match_all_open_tasks(
    tasks: list[dict[str, Any]],
    volunteers: list[dict[str, Any]],
    workload: dict[str, int],
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for task in tasks:
        matches = match_volunteers_to_task(task, volunteers, workload)
        if matches:
            results.append({"task": task, "matches": matches})
    return results


def _rule_based_matches(
    task: dict[str, Any],
    volunteers: list[dict[str, Any]],
    workload: dict[str, int],
) -> list[dict[str, Any]]:
    required = task.get("required_skills") or []
    matches: list[dict[str, Any]] = []

    for volunteer in volunteers:
        overlap = ai_engine.skill_overlap(required, volunteer.get("skills") or [])
        interest_overlap = ai_engine.skill_overlap(
            required,
            volunteer.get("interests") or [],
        )
        score = len(overlap) * 22 + len(interest_overlap) * 10
        if volunteer.get("availability"):
            score += 8
        active = workload.get(volunteer["id"], 0)
        score -= active * 12
        score = max(10, min(95, score))

        priority = "High" if score >= 75 else "Medium" if score >= 55 else "Low"
        matches.append(
            {
                "volunteer_id": volunteer["id"],
                "volunteer_name": volunteer["name"],
                "fit_score": score,
                "assigned_task": task.get("title", ""),
                "reasoning": (
                    f"Skill overlap: {', '.join(overlap) or 'none'}. "
                    f"Active tasks: {active}."
                ),
                "priority": priority,
            }
        )

    matches.sort(key=lambda m: m["fit_score"], reverse=True)
    return matches[:3]
