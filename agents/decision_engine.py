"""Decision Engine — final AI recommendations with rationale and priority."""

from __future__ import annotations

import json
from typing import Any

from agents.profile_analyzer import analyze_profile, analyze_profiles
from agents.task_matcher import rank_tasks_for_volunteer, rank_volunteers_for_task
from core import ai_engine
from core.prompts import DECISION_ENGINE_SYSTEM, DECISION_ENGINE_USER
from utils.helpers import (
    add_match_record,
    assign_task_with_ai,
    get_task,
    get_tasks,
    get_volunteer,
    get_volunteers,
    volunteer_workload,
)


def _open_tasks() -> list[dict[str, Any]]:
    return [t for t in get_tasks() if not t.get("assigned_volunteer_id")]


def recommend_volunteers_for_task(task_id: str, max_results: int = 3) -> list[dict[str, Any]]:
    task = get_task(task_id)
    if task is None:
        raise ValueError("Task not found")

    volunteers = get_volunteers()
    if not volunteers:
        return []

    profiles = analyze_profiles(volunteers)
    workload = volunteer_workload()
    candidates = rank_volunteers_for_task(task, volunteers, profiles, workload)

    if ai_engine.llm_configured() and candidates:
        prompt = DECISION_ENGINE_USER.format(
            task_json=json.dumps(task, indent=2),
            candidates_json=json.dumps(candidates[:10], indent=2),
        )
        result = ai_engine.complete_json(DECISION_ENGINE_SYSTEM, prompt)
        recommendations = result.get("recommendations", [])[:max_results]
    else:
        recommendations = ai_engine.rule_based_decision(task, candidates, volunteers, max_results)

    volunteer_names = {v["id"]: v["name"] for v in volunteers}
    enriched: list[dict[str, Any]] = []
    for rec in recommendations:
        enriched.append(
            {
                "volunteer_id": rec["volunteer_id"],
                "volunteer_name": volunteer_names.get(rec["volunteer_id"], "Unknown"),
                "reason": rec.get("reason", ""),
                "priority": rec.get("priority", "Medium"),
                "fit_score": rec.get("fit_score", 0),
            }
        )

    add_match_record(
        match_type="task_to_volunteers",
        task_id=task_id,
        volunteer_id=None,
        recommendations=enriched,
    )
    return enriched


def recommend_tasks_for_volunteer(volunteer_id: str) -> list[dict[str, Any]]:
    volunteer = get_volunteer(volunteer_id)
    if volunteer is None:
        raise ValueError("Volunteer not found")

    open_tasks = _open_tasks()
    if not open_tasks:
        return []

    profile = analyze_profile(volunteer)
    workload = volunteer_workload().get(volunteer_id, 0)
    recommendations = rank_tasks_for_volunteer(volunteer, profile, open_tasks, workload)

    task_titles = {t["id"]: t["title"] for t in open_tasks}
    enriched: list[dict[str, Any]] = []
    for rec in recommendations:
        enriched.append(
            {
                "task_id": rec["task_id"],
                "task_title": task_titles.get(rec["task_id"], "Unknown"),
                "reason": rec.get("reason", ""),
                "priority": rec.get("priority", "Medium"),
                "fit_score": rec.get("fit_score", 0),
            }
        )

    add_match_record(
        match_type="volunteer_to_tasks",
        task_id=None,
        volunteer_id=volunteer_id,
        recommendations=enriched,
    )
    return enriched


def apply_ai_assignment(
    task_id: str,
    volunteer_id: str,
    reason: str,
    priority: str,
) -> dict[str, Any]:
    if priority not in ai_engine.PRIORITIES:
        raise ValueError(f"Invalid priority: {priority}")

    task = assign_task_with_ai(task_id, volunteer_id, reason, priority)
    add_match_record(
        match_type="assignment",
        task_id=task_id,
        volunteer_id=volunteer_id,
        recommendations=[
            {
                "volunteer_id": volunteer_id,
                "reason": reason,
                "priority": priority,
            }
        ],
    )
    return task
