"""Candidate application and approval service."""

from __future__ import annotations

from typing import Any

from utils.json_storage import find_by_email, find_by_id, load_list, new_id, now_iso, save_list


def list_candidates(status: str | None = None) -> list[dict[str, Any]]:
    records = load_list("candidates")
    if status:
        return [c for c in records if c.get("status") == status]
    return records


def get_candidate(candidate_id: str) -> dict[str, Any] | None:
    return find_by_id("candidates", candidate_id)


def submit_application(
    name: str,
    email: str,
    skills: list[str],
    interests: list[str],
    availability: str,
    motivation: str,
) -> dict[str, Any]:
    if find_by_email("candidates", email):
        raise ValueError("An application with this email already exists.")
    if find_by_email("volunteers", email):
        raise ValueError("This email is already registered as a volunteer.")

    candidate = {
        "id": new_id(),
        "name": name.strip(),
        "email": email.strip(),
        "skills": skills,
        "interests": interests,
        "availability": availability.strip(),
        "motivation": motivation.strip(),
        "status": "pending",
        "source": "application",
        "ai_screening": None,
        "created_at": now_iso(),
        "reviewed_at": None,
    }
    records = load_list("candidates")
    records.append(candidate)
    save_list("candidates", records)
    return candidate


def save_screening_result(candidate_id: str, screening: dict[str, Any]) -> dict[str, Any]:
    records = load_list("candidates")
    for candidate in records:
        if candidate["id"] == candidate_id:
            candidate["ai_screening"] = {
                **screening,
                "screened_at": now_iso(),
            }
            save_list("candidates", records)
            return candidate
    raise ValueError("Candidate not found")


def approve_candidate(candidate_id: str) -> dict[str, Any]:
    from services.volunteer_service import add_volunteer_from_candidate

    candidate = get_candidate(candidate_id)
    if not candidate:
        raise ValueError("Candidate not found")
    if candidate.get("status") == "approved":
        raise ValueError("Candidate is already approved")

    volunteer = add_volunteer_from_candidate(candidate)

    records = load_list("candidates")
    for item in records:
        if item["id"] == candidate_id:
            item["status"] = "approved"
            item["reviewed_at"] = now_iso()
            item["volunteer_id"] = volunteer["id"]
    save_list("candidates", records)
    return volunteer


def reject_candidate(candidate_id: str, reason: str = "") -> dict[str, Any]:
    records = load_list("candidates")
    for candidate in records:
        if candidate["id"] == candidate_id:
            candidate["status"] = "rejected"
            candidate["reviewed_at"] = now_iso()
            candidate["rejection_reason"] = reason.strip()
            save_list("candidates", records)
            return candidate
    raise ValueError("Candidate not found")
