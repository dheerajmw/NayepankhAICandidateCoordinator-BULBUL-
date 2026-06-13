"""Automated reminder and escalation engine (Phase 3)."""

from __future__ import annotations

from datetime import date
from typing import Any

from utils import email_service
from utils.helpers import (
    add_notification,
    get_notifications,
    get_task,
    get_tasks,
    get_volunteer,
    notification_exists,
    volunteer_name,
)

NOTIFICATION_TYPES = (
    "deadline_3d",
    "deadline_1d",
    "overdue",
    "completion",
)


def _days_until_deadline(task: dict[str, Any]) -> int:
    deadline = date.fromisoformat(task["deadline"])
    return (deadline - date.today()).days


def _volunteer_wants_email(volunteer_id: str) -> bool:
    volunteer = get_volunteer(volunteer_id)
    if volunteer is None:
        return False
    prefs = volunteer.get("reminder_preferences") or {}
    return prefs.get("enabled", True) and prefs.get("email", True)


def _record_and_send(
    *,
    task_id: str,
    volunteer_id: str | None,
    notification_type: str,
    recipient: str,
    subject: str,
    body: str,
) -> dict[str, Any]:
    if not recipient:
        return add_notification(
            task_id=task_id,
            volunteer_id=volunteer_id,
            notification_type=notification_type,
            recipient="",
            channel="log",
            status="skipped",
            subject=subject,
            error="No recipient email",
        )

    success, channel, error = email_service.send_email(recipient, subject, body)
    status = "sent" if success else "failed"
    return add_notification(
        task_id=task_id,
        volunteer_id=volunteer_id,
        notification_type=notification_type,
        recipient=recipient,
        channel=channel,
        status=status,
        subject=subject,
        error=error,
    )


def send_completion_notification(task_id: str) -> dict[str, Any] | None:
    task = get_task(task_id)
    if task is None or task.get("status") != "completed":
        return None
    if notification_exists(task_id, "completion"):
        return None

    volunteer_id = task.get("assigned_volunteer_id")
    if not volunteer_id:
        return None

    volunteer = get_volunteer(volunteer_id)
    if volunteer is None:
        return None

    if not _volunteer_wants_email(volunteer_id):
        return add_notification(
            task_id=task_id,
            volunteer_id=volunteer_id,
            notification_type="completion",
            recipient=volunteer.get("email", ""),
            channel="log",
            status="skipped",
            subject="Task completion",
            error="Volunteer opted out of email reminders",
        )

    subject, body = email_service.render_completion_confirmation(
        volunteer["name"],
        task["title"],
    )
    return _record_and_send(
        task_id=task_id,
        volunteer_id=volunteer_id,
        notification_type="completion",
        recipient=volunteer["email"],
        subject=subject,
        body=body,
    )


def run_reminder_check() -> list[dict[str, Any]]:
    """Evaluate all assigned tasks and send due reminders/escalations."""
    sent: list[dict[str, Any]] = []

    for task in get_tasks():
        volunteer_id = task.get("assigned_volunteer_id")
        if not volunteer_id or task.get("status") == "completed":
            continue

        days_left = _days_until_deadline(task)
        volunteer = get_volunteer(volunteer_id)
        if volunteer is None:
            continue

        if days_left == 3 and not notification_exists(task["id"], "deadline_3d"):
            record = _send_volunteer_reminder(task, volunteer, "deadline_3d", days_left, urgent=False)
            if record:
                sent.append(record)

        if days_left == 1 and not notification_exists(task["id"], "deadline_1d"):
            record = _send_volunteer_reminder(task, volunteer, "deadline_1d", days_left, urgent=True)
            if record:
                sent.append(record)

        if days_left < 0 and not notification_exists(task["id"], "overdue"):
            record = _send_overdue_escalation(task, volunteer, abs(days_left))
            if record:
                sent.append(record)

    return sent


def _send_volunteer_reminder(
    task: dict[str, Any],
    volunteer: dict[str, Any],
    notification_type: str,
    days_left: int,
    urgent: bool,
) -> dict[str, Any] | None:
    if not _volunteer_wants_email(volunteer["id"]):
        return add_notification(
            task_id=task["id"],
            volunteer_id=volunteer["id"],
            notification_type=notification_type,
            recipient=volunteer.get("email", ""),
            channel="log",
            status="skipped",
            subject="Deadline reminder",
            error="Volunteer opted out of email reminders",
        )

    subject, body = email_service.render_deadline_reminder(
        volunteer["name"],
        task["title"],
        task["deadline"],
        days_left,
        urgent=urgent,
    )
    return _record_and_send(
        task_id=task["id"],
        volunteer_id=volunteer["id"],
        notification_type=notification_type,
        recipient=volunteer["email"],
        subject=subject,
        body=body,
    )


def _send_overdue_escalation(
    task: dict[str, Any],
    volunteer: dict[str, Any],
    days_overdue: int,
) -> dict[str, Any]:
    subject, body = email_service.render_overdue_escalation(
        task["title"],
        volunteer["name"],
        task["deadline"],
        days_overdue,
    )
    return _record_and_send(
        task_id=task["id"],
        volunteer_id=volunteer["id"],
        notification_type="overdue",
        recipient=email_service.admin_email(),
        subject=subject,
        body=body,
    )


def get_task_notification_summary(task_id: str) -> dict[str, Any]:
    records = [n for n in get_notifications() if n.get("task_id") == task_id]
    if not records:
        return {"count": 0, "last_notified": None, "last_type": None}

    latest = max(records, key=lambda n: n.get("sent_at", ""))
    return {
        "count": len(records),
        "last_notified": latest.get("sent_at"),
        "last_type": latest.get("notification_type"),
    }
