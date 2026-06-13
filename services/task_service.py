"""Task management and assignment service."""

from __future__ import annotations

from datetime import date
from typing import Any

from utils.json_storage import find_by_id, load_list, new_id, now_iso, save_list

STATUSES = ("open", "assigned", "in_progress", "completed")
PRIORITIES = ("High", "Medium", "Low")


def list_tasks(status: str | None = None) -> list[dict[str, Any]]:
    records = load_list("tasks")
    if status:
        return [t for t in records if t.get("status") == status]
    return records


def get_task(task_id: str) -> dict[str, Any] | None:
    return find_by_id("tasks", task_id)


def open_tasks() -> list[dict[str, Any]]:
    return [t for t in list_tasks() if not t.get("assigned_volunteer_id") and t.get("status") == "open"]


def create_task(
    title: str,
    description: str,
    required_skills: list[str],
    deadline: str,
    priority: str = "Medium",
) -> dict[str, Any]:
    if priority not in PRIORITIES:
        priority = "Medium"

    task = {
        "id": new_id(),
        "title": title.strip(),
        "description": description.strip(),
        "required_skills": required_skills,
        "deadline": deadline,
        "assigned_volunteer_id": None,
        "status": "open",
        "assignment_reason": "",
        "priority": priority,
        "ai_assigned": False,
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }
    records = load_list("tasks")
    records.append(task)
    save_list("tasks", records)
    return task


def assign_task(
    task_id: str,
    volunteer_id: str,
    reason: str,
    priority: str | None = None,
    ai_assigned: bool = False,
) -> dict[str, Any]:
    from services.volunteer_service import record_assignment

    records = load_list("tasks")
    task_title = ""
    for task in records:
        if task["id"] != task_id:
            continue
        task["assigned_volunteer_id"] = volunteer_id
        task["status"] = "assigned"
        task["assignment_reason"] = reason.strip()
        task["ai_assigned"] = ai_assigned
        task["updated_at"] = now_iso()
        if priority and priority in PRIORITIES:
            task["priority"] = priority
        task_title = task["title"]
        save_list("tasks", records)
        record_assignment(volunteer_id, task_id, task_title, reason)
        return task
    raise ValueError("Task not found")


def update_task_status(task_id: str, status: str) -> dict[str, Any]:
    if status not in STATUSES:
        raise ValueError(f"Invalid status: {status}")

    records = load_list("tasks")
    for task in records:
        if task["id"] != task_id:
            continue
        task["status"] = status
        task["updated_at"] = now_iso()
        if status == "completed" and task.get("assigned_volunteer_id"):
            from services.volunteer_service import record_completion

            record_completion(task["assigned_volunteer_id"], task_id, task["title"])
        save_list("tasks", records)
        return task
    raise ValueError("Task not found")


def seed_demo_tasks() -> None:
    """Add sample tasks when pool is empty (dev convenience)."""
    if list_tasks():
        return
    create_task(
        "Social media campaign",
        "Create posts for an education awareness drive.",
        ["social media", "design"],
        str(date.today().replace(day=min(date.today().day + 14, 28))),
        "High",
    )
    create_task(
        "Weekend tutoring",
        "Support students with homework help on Saturdays.",
        ["teaching", "communication"],
        str(date.today().replace(day=min(date.today().day + 21, 28))),
        "Medium",
    )
