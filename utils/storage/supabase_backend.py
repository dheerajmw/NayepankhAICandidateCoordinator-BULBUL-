"""Supabase PostgreSQL storage backend (Phase 5)."""

from __future__ import annotations

import uuid
from datetime import date, datetime, timezone
from typing import Any

from core.config import SUPABASE_KEY, SUPABASE_URL


class SupabaseStorageBackend:
    def __init__(self) -> None:
        from supabase import create_client

        self.client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def _now_iso(self) -> str:
        return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    def _new_id(self) -> str:
        return str(uuid.uuid4())

    @staticmethod
    def _volunteer_row(record: dict[str, Any]) -> dict[str, Any]:
        return {
            "id": record["id"],
            "name": record["name"],
            "email": record["email"],
            "skills": record.get("skills", []),
            "interests": record.get("interests", []),
            "availability": record.get("availability", ""),
            "reminder_preferences": record.get("reminder_preferences") or {"enabled": True, "email": True},
            "created_at": record.get("created_at"),
        }

    @staticmethod
    def _task_row(record: dict[str, Any]) -> dict[str, Any]:
        return {
            "id": record["id"],
            "title": record["title"],
            "description": record["description"],
            "required_skills": record.get("required_skills", []),
            "deadline": record["deadline"],
            "assigned_volunteer_id": record.get("assigned_volunteer_id"),
            "status": record.get("status", "pending"),
            "assignment_reason": record.get("assignment_reason"),
            "priority": record.get("priority"),
            "ai_assigned": record.get("ai_assigned", False),
            "created_at": record.get("created_at"),
            "updated_at": record.get("updated_at"),
        }

    def get_volunteers(self) -> list[dict[str, Any]]:
        response = self.client.table("volunteers").select("*").order("created_at").execute()
        return response.data or []

    def get_volunteer(self, volunteer_id: str) -> dict[str, Any] | None:
        response = (
            self.client.table("volunteers").select("*").eq("id", volunteer_id).limit(1).execute()
        )
        rows = response.data or []
        return rows[0] if rows else None

    def add_volunteer(
        self,
        name: str,
        email: str,
        skills: list[str],
        interests: list[str],
        availability: str,
    ) -> dict[str, Any]:
        volunteer = {
            "id": self._new_id(),
            "name": name.strip(),
            "email": email.strip(),
            "skills": skills,
            "interests": interests,
            "availability": availability.strip(),
            "reminder_preferences": {"enabled": True, "email": True},
            "created_at": self._now_iso(),
        }
        self.client.table("volunteers").insert(self._volunteer_row(volunteer)).execute()
        return volunteer

    def update_volunteer_reminder_preferences(
        self,
        volunteer_id: str,
        enabled: bool,
        email: bool,
    ) -> dict[str, Any]:
        prefs = {"enabled": enabled, "email": email}
        response = (
            self.client.table("volunteers")
            .update({"reminder_preferences": prefs})
            .eq("id", volunteer_id)
            .execute()
        )
        rows = response.data or []
        if not rows:
            raise ValueError("Volunteer not found")
        return rows[0]

    def get_tasks(self) -> list[dict[str, Any]]:
        response = self.client.table("tasks").select("*").order("created_at").execute()
        return response.data or []

    def get_task(self, task_id: str) -> dict[str, Any] | None:
        response = self.client.table("tasks").select("*").eq("id", task_id).limit(1).execute()
        rows = response.data or []
        return rows[0] if rows else None

    def add_task(
        self,
        title: str,
        description: str,
        required_skills: list[str],
        deadline: date,
    ) -> dict[str, Any]:
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
        self.client.table("tasks").insert(self._task_row(task)).execute()
        return task

    def assign_task(
        self,
        task_id: str,
        volunteer_id: str,
        assignment_reason: str | None = None,
        priority: str | None = None,
        ai_assigned: bool = False,
    ) -> dict[str, Any]:
        if self.get_volunteer(volunteer_id) is None:
            raise ValueError("Volunteer not found")

        payload: dict[str, Any] = {
            "assigned_volunteer_id": volunteer_id,
            "status": "pending",
            "updated_at": self._now_iso(),
            "ai_assigned": ai_assigned,
        }
        if assignment_reason is not None:
            payload["assignment_reason"] = assignment_reason
        if priority is not None:
            payload["priority"] = priority

        response = self.client.table("tasks").update(payload).eq("id", task_id).execute()
        rows = response.data or []
        if not rows:
            raise ValueError("Task not found")
        return rows[0]

    def update_task_status(self, task_id: str, status: str) -> dict[str, Any]:
        task = self.get_task(task_id)
        if task is None:
            raise ValueError("Task not found")
        if not task.get("assigned_volunteer_id"):
            raise ValueError("Assign a volunteer before updating status")

        response = (
            self.client.table("tasks")
            .update({"status": status, "updated_at": self._now_iso()})
            .eq("id", task_id)
            .execute()
        )
        rows = response.data or []
        if not rows:
            raise ValueError("Task not found")
        return rows[0]

    def get_match_history(self) -> list[dict[str, Any]]:
        response = self.client.table("match_history").select("*").order("created_at").execute()
        return response.data or []

    def add_match_record(
        self,
        match_type: str,
        task_id: str | None,
        volunteer_id: str | None,
        recommendations: list[dict[str, Any]],
    ) -> dict[str, Any]:
        record = {
            "id": self._new_id(),
            "match_type": match_type,
            "task_id": task_id,
            "volunteer_id": volunteer_id,
            "recommendations": recommendations,
            "created_at": self._now_iso(),
        }
        self.client.table("match_history").insert(record).execute()
        return record

    def get_notifications(self) -> list[dict[str, Any]]:
        response = self.client.table("notifications").select("*").order("sent_at").execute()
        return response.data or []

    def notification_exists(self, task_id: str, notification_type: str) -> bool:
        response = (
            self.client.table("notifications")
            .select("id")
            .eq("task_id", task_id)
            .eq("notification_type", notification_type)
            .eq("status", "sent")
            .limit(1)
            .execute()
        )
        return bool(response.data)

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
        self.client.table("notifications").insert(record).execute()
        return record

    def get_reports(self) -> list[dict[str, Any]]:
        response = self.client.table("reports").select("*").order("created_at").execute()
        return response.data or []

    def save_report(self, report: dict[str, Any]) -> dict[str, Any]:
        record = {
            "id": self._new_id(),
            "created_at": self._now_iso(),
            **report,
        }
        self.client.table("reports").insert(record).execute()
        return record
