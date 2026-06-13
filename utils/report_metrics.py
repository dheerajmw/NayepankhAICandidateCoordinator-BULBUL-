"""Compute contribution metrics from task and volunteer data."""

from __future__ import annotations

from datetime import date
from typing import Any

from utils.helpers import get_tasks, get_volunteer, get_volunteers


def _parse_date(value: str) -> date:
    return date.fromisoformat(value[:10])


def _in_period(value: str, start: date | None, end: date | None) -> bool:
    if not value:
        return True
    task_date = _parse_date(value)
    if start and task_date < start:
        return False
    if end and task_date > end:
        return False
    return True


def volunteer_tasks(
    volunteer_id: str,
    start: date | None = None,
    end: date | None = None,
) -> list[dict[str, Any]]:
    tasks = []
    for task in get_tasks():
        if task.get("assigned_volunteer_id") != volunteer_id:
            continue
        ref_date = task.get("updated_at") or task.get("created_at", "")
        if _in_period(ref_date, start, end):
            tasks.append(task)
    return tasks


def compute_volunteer_metrics(
    volunteer_id: str,
    start: date | None = None,
    end: date | None = None,
) -> dict[str, Any]:
    volunteer = get_volunteer(volunteer_id)
    if volunteer is None:
        raise ValueError("Volunteer not found")

    tasks = volunteer_tasks(volunteer_id, start, end)
    completed = [t for t in tasks if t.get("status") == "completed"]
    in_progress = [t for t in tasks if t.get("status") == "in_progress"]
    pending = [t for t in tasks if t.get("status") == "pending"]

    skills_utilized: set[str] = set()
    for task in completed:
        for skill in task.get("required_skills", []):
            skills_utilized.add(skill)

    total = len(tasks)
    completion_rate = round(len(completed) / total * 100) if total else 0

    return {
        "volunteer_id": volunteer_id,
        "volunteer_name": volunteer["name"],
        "volunteer_email": volunteer["email"],
        "period_start": start.isoformat() if start else None,
        "period_end": end.isoformat() if end else None,
        "tasks_total": total,
        "tasks_completed": len(completed),
        "tasks_in_progress": len(in_progress),
        "tasks_pending": len(pending),
        "completion_rate": completion_rate,
        "skills_utilized": sorted(skills_utilized),
        "task_history": [
            {
                "title": t["title"],
                "status": t.get("status"),
                "deadline": t.get("deadline"),
                "completed_at": t.get("updated_at") if t.get("status") == "completed" else None,
                "skills": t.get("required_skills", []),
            }
            for t in tasks
        ],
    }


def compute_org_metrics(
    start: date | None = None,
    end: date | None = None,
    volunteer_id: str | None = None,
) -> dict[str, Any]:
    volunteers = get_volunteers()
    if volunteer_id:
        volunteers = [v for v in volunteers if v["id"] == volunteer_id]
        if not volunteers:
            raise ValueError("Volunteer not found")

    summaries = [compute_volunteer_metrics(v["id"], start, end) for v in volunteers]
    total_completed = sum(s["tasks_completed"] for s in summaries)
    total_tasks = sum(s["tasks_total"] for s in summaries)

    all_skills: set[str] = set()
    for summary in summaries:
        all_skills.update(summary["skills_utilized"])

    return {
        "period_start": start.isoformat() if start else None,
        "period_end": end.isoformat() if end else None,
        "volunteer_count": len(summaries),
        "tasks_total": total_tasks,
        "tasks_completed": total_completed,
        "completion_rate": round(total_completed / total_tasks * 100) if total_tasks else 0,
        "skills_utilized": sorted(all_skills),
        "volunteer_summaries": summaries,
    }
