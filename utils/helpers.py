"""Storage facade — delegates to JSON or Supabase backend."""

from __future__ import annotations

from datetime import date
from typing import Any

from utils.storage.factory import get_storage

ASSIGNMENT_STATUSES = ("pending", "in_progress", "completed")
PRIORITIES = ("High", "Medium", "Low")


def parse_comma_list(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def format_comma_list(items: list[str]) -> str:
    return ", ".join(items)


def _store():
    return get_storage()


def get_volunteers() -> list[dict[str, Any]]:
    return _store().get_volunteers()


def get_volunteer(volunteer_id: str) -> dict[str, Any] | None:
    return _store().get_volunteer(volunteer_id)


def add_volunteer(
    name: str,
    email: str,
    skills: list[str],
    interests: list[str],
    availability: str,
) -> dict[str, Any]:
    return _store().add_volunteer(name, email, skills, interests, availability)


def update_volunteer_reminder_preferences(
    volunteer_id: str,
    enabled: bool,
    email: bool,
) -> dict[str, Any]:
    return _store().update_volunteer_reminder_preferences(volunteer_id, enabled, email)


def get_tasks() -> list[dict[str, Any]]:
    return _store().get_tasks()


def get_task(task_id: str) -> dict[str, Any] | None:
    return _store().get_task(task_id)


def add_task(
    title: str,
    description: str,
    required_skills: list[str],
    deadline: date,
) -> dict[str, Any]:
    return _store().add_task(title, description, required_skills, deadline)


def assign_task(task_id: str, volunteer_id: str) -> dict[str, Any]:
    return _store().assign_task(task_id, volunteer_id)


def assign_task_with_ai(
    task_id: str,
    volunteer_id: str,
    reason: str,
    priority: str,
) -> dict[str, Any]:
    if priority not in PRIORITIES:
        raise ValueError(f"Invalid priority: {priority}")
    return _store().assign_task(
        task_id,
        volunteer_id,
        assignment_reason=reason.strip(),
        priority=priority,
        ai_assigned=True,
    )


def volunteer_workload() -> dict[str, int]:
    workload: dict[str, int] = {}
    for task in get_tasks():
        volunteer_id = task.get("assigned_volunteer_id")
        if volunteer_id and task.get("status") != "completed":
            workload[volunteer_id] = workload.get(volunteer_id, 0) + 1
    return workload


def update_task_status(task_id: str, status: str) -> dict[str, Any]:
    if status not in ASSIGNMENT_STATUSES:
        raise ValueError(f"Invalid status: {status}")
    return _store().update_task_status(task_id, status)


def volunteer_name(volunteer_id: str | None) -> str:
    if not volunteer_id:
        return "Unassigned"
    volunteer = get_volunteer(volunteer_id)
    return volunteer["name"] if volunteer else "Unknown"


def get_match_history() -> list[dict[str, Any]]:
    return _store().get_match_history()


def add_match_record(
    match_type: str,
    task_id: str | None,
    volunteer_id: str | None,
    recommendations: list[dict[str, Any]],
) -> dict[str, Any]:
    return _store().add_match_record(match_type, task_id, volunteer_id, recommendations)


def get_notifications() -> list[dict[str, Any]]:
    return _store().get_notifications()


def notification_exists(task_id: str, notification_type: str) -> bool:
    return _store().notification_exists(task_id, notification_type)


def add_notification(
    task_id: str,
    volunteer_id: str | None,
    notification_type: str,
    recipient: str,
    channel: str,
    status: str,
    subject: str,
    error: str | None = None,
) -> dict[str, Any]:
    return _store().add_notification(
        task_id,
        volunteer_id,
        notification_type,
        recipient,
        channel,
        status,
        subject,
        error,
    )


def get_reports() -> list[dict[str, Any]]:
    return _store().get_reports()


def save_report(report: dict[str, Any]) -> dict[str, Any]:
    return _store().save_report(report)
