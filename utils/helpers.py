"""Shared helper utilities and storage facade."""

from __future__ import annotations

from typing import Any

from utils.storage.factory import get_storage


def get_volunteers() -> list[dict[str, Any]]:
    return get_storage().get_volunteers()


def get_volunteer(volunteer_id: str) -> dict[str, Any] | None:
    return get_storage().get_volunteer(volunteer_id)


def get_tasks() -> list[dict[str, Any]]:
    return get_storage().get_tasks()


def get_task(task_id: str) -> dict[str, Any] | None:
    return get_storage().get_task(task_id)


def get_notifications() -> list[dict[str, Any]]:
    return get_storage().get_notifications()


def notification_exists(task_id: str, notification_type: str) -> bool:
    return get_storage().notification_exists(task_id, notification_type)


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
    return get_storage().add_notification(
        task_id=task_id,
        volunteer_id=volunteer_id,
        notification_type=notification_type,
        recipient=recipient,
        channel=channel,
        status=status,
        subject=subject,
        error=error,
    )


def volunteer_name(volunteer_id: str | None) -> str:
    if not volunteer_id:
        return "—"
    volunteer = get_volunteer(volunteer_id)
    return volunteer["name"] if volunteer else "Unknown"


def volunteer_workload() -> dict[str, int]:
    counts: dict[str, int] = {}
    for task in get_tasks():
        volunteer_id = task.get("assigned_volunteer_id")
        if volunteer_id and task.get("status") != "completed":
            counts[volunteer_id] = counts.get(volunteer_id, 0) + 1
    return counts


def assign_task_with_ai(
    task_id: str,
    volunteer_id: str,
    reason: str,
    priority: str | None = None,
) -> dict[str, Any]:
    return get_storage().assign_task(
        task_id,
        volunteer_id,
        assignment_reason=reason,
        priority=priority,
        ai_assigned=True,
    )


def add_match_record(
    match_type: str,
    task_id: str | None,
    volunteer_id: str | None,
    recommendations: list[dict[str, Any]],
) -> dict[str, Any]:
    return get_storage().add_match_record(
        match_type,
        task_id,
        volunteer_id,
        recommendations,
    )


def save_report(report: dict[str, Any]) -> dict[str, Any]:
    return get_storage().save_report(report)


def parse_comma_list(value: str) -> list[str]:
    if not value or not value.strip():
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def format_comma_list(items: list[str]) -> str:
    return ", ".join(items)
