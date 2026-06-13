"""JSON file storage backend (Phase 1–4 default)."""

from __future__ import annotations

import json
import uuid
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
VOLUNTEERS_FILE = DATA_DIR / "volunteers.json"
TASKS_FILE = DATA_DIR / "tasks.json"
MATCH_HISTORY_FILE = DATA_DIR / "match_history.json"
NOTIFICATIONS_FILE = DATA_DIR / "notifications.json"
REPORTS_FILE = DATA_DIR / "reports.json"

REMINDER_PREFERENCES_ALWAYS_ON = {"enabled": True, "email": True}


class JsonStorageBackend:
    def _now_iso(self) -> str:
        return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    def _new_id(self) -> str:
        return str(uuid.uuid4())

    def _load_list(self, path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, list):
            raise ValueError(f"Expected a JSON array in {path}")
        return data

    def _save_list(self, path: Path, records: list[dict[str, Any]]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(records, handle, indent=2, ensure_ascii=False)
            handle.write("\n")

    @staticmethod
    def _normalize_volunteer(volunteer: dict[str, Any]) -> dict[str, Any]:
        volunteer["reminder_preferences"] = dict(REMINDER_PREFERENCES_ALWAYS_ON)
        return volunteer

    def get_volunteers(self) -> list[dict[str, Any]]:
        return [self._normalize_volunteer(v) for v in self._load_list(VOLUNTEERS_FILE)]

    def get_volunteer(self, volunteer_id: str) -> dict[str, Any] | None:
        volunteer = next((v for v in self._load_list(VOLUNTEERS_FILE) if v["id"] == volunteer_id), None)
        return self._normalize_volunteer(volunteer) if volunteer else None

    def add_volunteer(
        self,
        name: str,
        email: str,
        skills: list[str],
        interests: list[str],
        availability: str,
    ) -> dict[str, Any]:
        volunteers = self.get_volunteers()
        volunteer = {
            "id": self._new_id(),
            "name": name.strip(),
            "email": email.strip(),
            "skills": skills,
            "interests": interests,
            "availability": availability.strip(),
            "reminder_preferences": dict(REMINDER_PREFERENCES_ALWAYS_ON),
            "created_at": self._now_iso(),
        }
        volunteers.append(volunteer)
        self._save_list(VOLUNTEERS_FILE, volunteers)
        return volunteer

    def update_volunteer_reminder_preferences(
        self,
        volunteer_id: str,
        enabled: bool,
        email: bool,
    ) -> dict[str, Any]:
        del enabled, email  # Reminders are permanently on for all volunteers.
        volunteers = self._load_list(VOLUNTEERS_FILE)
        for volunteer in volunteers:
            if volunteer["id"] == volunteer_id:
                volunteer["reminder_preferences"] = dict(REMINDER_PREFERENCES_ALWAYS_ON)
                self._save_list(VOLUNTEERS_FILE, volunteers)
                return self._normalize_volunteer(volunteer)
        raise ValueError("Volunteer not found")

    def get_tasks(self) -> list[dict[str, Any]]:
        return self._load_list(TASKS_FILE)

    def get_task(self, task_id: str) -> dict[str, Any] | None:
        return next((t for t in self.get_tasks() if t["id"] == task_id), None)

    def add_task(
        self,
        title: str,
        description: str,
        required_skills: list[str],
        deadline: date,
    ) -> dict[str, Any]:
        tasks = self.get_tasks()
        task = {
            "id": self._new_id(),
            "title": title.strip(),
            "description": description.strip(),
            "required_skills": required_skills,
            "deadline": deadline.isoformat(),
            "assigned_volunteer_id": None,
            "status": "pending",
            "created_at": self._now_iso(),
            "updated_at": self._now_iso(),
        }
        tasks.append(task)
        self._save_list(TASKS_FILE, tasks)
        return task

    def assign_task(
        self,
        task_id: str,
        volunteer_id: str,
        assignment_reason: str | None = None,
        priority: str | None = None,
        ai_assigned: bool = False,
    ) -> dict[str, Any]:
        tasks = self.get_tasks()
        if self.get_volunteer(volunteer_id) is None:
            raise ValueError("Volunteer not found")

        for task in tasks:
            if task["id"] == task_id:
                task["assigned_volunteer_id"] = volunteer_id
                task["status"] = "pending"
                task["updated_at"] = self._now_iso()
                if assignment_reason is not None:
                    task["assignment_reason"] = assignment_reason
                if priority is not None:
                    task["priority"] = priority
                task["ai_assigned"] = ai_assigned
                self._save_list(TASKS_FILE, tasks)
                return task
        raise ValueError("Task not found")

    def update_task_status(self, task_id: str, status: str) -> dict[str, Any]:
        tasks = self.get_tasks()
        for task in tasks:
            if task["id"] == task_id:
                if not task.get("assigned_volunteer_id"):
                    raise ValueError("Assign a volunteer before updating status")
                task["status"] = status
                task["updated_at"] = self._now_iso()
                self._save_list(TASKS_FILE, tasks)
                return task
        raise ValueError("Task not found")

    def get_match_history(self) -> list[dict[str, Any]]:
        return self._load_list(MATCH_HISTORY_FILE)

    def add_match_record(
        self,
        match_type: str,
        task_id: str | None,
        volunteer_id: str | None,
        recommendations: list[dict[str, Any]],
    ) -> dict[str, Any]:
        history = self.get_match_history()
        record = {
            "id": self._new_id(),
            "match_type": match_type,
            "task_id": task_id,
            "volunteer_id": volunteer_id,
            "recommendations": recommendations,
            "created_at": self._now_iso(),
        }
        history.append(record)
        self._save_list(MATCH_HISTORY_FILE, history)
        return record

    def get_notifications(self) -> list[dict[str, Any]]:
        return self._load_list(NOTIFICATIONS_FILE)

    def notification_exists(self, task_id: str, notification_type: str) -> bool:
        return any(
            n.get("task_id") == task_id
            and n.get("notification_type") == notification_type
            and n.get("status") == "sent"
            for n in self.get_notifications()
        )

    def add_notification(
        self,
        task_id: str,
        volunteer_id: str | None,
        notification_type: str,
        recipient: str,
        channel: str,
        status: str,
        subject: str,
        error: str | None = None,
    ) -> dict[str, Any]:
        notifications = self.get_notifications()
        record = {
            "id": self._new_id(),
            "task_id": task_id,
            "volunteer_id": volunteer_id,
            "notification_type": notification_type,
            "recipient": recipient,
            "channel": channel,
            "status": status,
            "subject": subject,
            "error": error,
            "sent_at": self._now_iso(),
        }
        notifications.append(record)
        self._save_list(NOTIFICATIONS_FILE, notifications)
        return record

    def get_reports(self) -> list[dict[str, Any]]:
        return self._load_list(REPORTS_FILE)

    def save_report(self, report: dict[str, Any]) -> dict[str, Any]:
        reports = self.get_reports()
        record = {
            "id": self._new_id(),
            "created_at": self._now_iso(),
            **report,
        }
        reports.append(record)
        self._save_list(REPORTS_FILE, reports)
        return record
