"""Volunteer pool service — unified approved volunteers."""

from __future__ import annotations

from typing import Any

from utils.json_storage import find_by_email, find_by_id, load_list, new_id, now_iso, save_list


def list_volunteers() -> list[dict[str, Any]]:
    return load_list("volunteers")


def get_volunteer(volunteer_id: str) -> dict[str, Any] | None:
    return find_by_id("volunteers", volunteer_id)


def volunteer_name(volunteer_id: str | None) -> str:
    if not volunteer_id:
        return "—"
    volunteer = get_volunteer(volunteer_id)
    return volunteer["name"] if volunteer else "Unknown"


def add_volunteer_manual(
    name: str,
    email: str,
    skills: list[str],
    interests: list[str],
    availability: str,
) -> dict[str, Any]:
    if find_by_email("volunteers", email):
        raise ValueError("A volunteer with this email already exists.")

    volunteer = _build_volunteer(
        name=name,
        email=email,
        skills=skills,
        interests=interests,
        availability=availability,
        source="admin",
        candidate_id=None,
    )
    records = load_list("volunteers")
    records.append(volunteer)
    save_list("volunteers", records)
    return volunteer


def add_volunteer_from_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    if find_by_email("volunteers", candidate["email"]):
        raise ValueError("Volunteer already exists for this email.")

    volunteer = _build_volunteer(
        name=candidate["name"],
        email=candidate["email"],
        skills=candidate.get("skills", []),
        interests=candidate.get("interests", []),
        availability=candidate.get("availability", ""),
        source="approved_candidate",
        candidate_id=candidate["id"],
        ai_screening=candidate.get("ai_screening"),
    )
    records = load_list("volunteers")
    records.append(volunteer)
    save_list("volunteers", records)
    return volunteer


def record_assignment(volunteer_id: str, task_id: str, task_title: str, reason: str) -> None:
    records = load_list("volunteers")
    for volunteer in records:
        if volunteer["id"] != volunteer_id:
            continue
        memory = volunteer.setdefault("memory", {"assignments": [], "completed_tasks": []})
        memory["assignments"].append(
            {
                "task_id": task_id,
                "task_title": task_title,
                "reason": reason,
                "assigned_at": now_iso(),
            }
        )
        save_list("volunteers", records)
        return
    raise ValueError("Volunteer not found")


def record_completion(volunteer_id: str, task_id: str, task_title: str) -> None:
    records = load_list("volunteers")
    for volunteer in records:
        if volunteer["id"] != volunteer_id:
            continue
        memory = volunteer.setdefault("memory", {"assignments": [], "completed_tasks": []})
        memory["completed_tasks"].append(
            {
                "task_id": task_id,
                "task_title": task_title,
                "completed_at": now_iso(),
            }
        )
        save_list("volunteers", records)
        return
    raise ValueError("Volunteer not found")


def workload_counts() -> dict[str, int]:
    from services.task_service import list_tasks

    counts: dict[str, int] = {}
    for task in list_tasks():
        vid = task.get("assigned_volunteer_id")
        if vid and task.get("status") in ("assigned", "in_progress"):
            counts[vid] = counts.get(vid, 0) + 1
    return counts


def _build_volunteer(
    name: str,
    email: str,
    skills: list[str],
    interests: list[str],
    availability: str,
    source: str,
    candidate_id: str | None,
    ai_screening: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "id": new_id(),
        "name": name.strip(),
        "email": email.strip(),
        "skills": skills,
        "interests": interests,
        "availability": availability.strip(),
        "source": source,
        "candidate_id": candidate_id,
        "ai_screening": ai_screening,
        "memory": {"assignments": [], "completed_tasks": []},
        "reminder_preferences": {"enabled": True, "email": True},
        "created_at": now_iso(),
    }
