"""LLM wrapper with OpenAI / Gemini support and rule-based fallback."""

from __future__ import annotations

import json
import os
import re
from typing import Any

from dotenv import load_dotenv

from core.config import LLM_FALLBACK_ENABLED, PROMPT_VERSION

load_dotenv()

PRIORITIES = ("High", "Medium", "Low")


def llm_configured() -> bool:
    return bool(_available_providers())


def prompt_version() -> str:
    return PROMPT_VERSION


def _available_providers() -> list[str]:
    providers: list[str] = []
    primary = _provider()
    if primary == "openai" and os.getenv("OPENAI_API_KEY"):
        providers.append("openai")
    elif primary == "gemini" and os.getenv("GEMINI_API_KEY"):
        providers.append("gemini")

    if LLM_FALLBACK_ENABLED:
        if "openai" not in providers and os.getenv("OPENAI_API_KEY"):
            providers.append("openai")
        if "gemini" not in providers and os.getenv("GEMINI_API_KEY"):
            providers.append("gemini")
    return providers


def _provider() -> str:
    return os.getenv("LLM_PROVIDER", "openai").strip().lower()


def complete_json(system_prompt: str, user_prompt: str) -> dict[str, Any]:
    providers = _available_providers()
    if not providers:
        raise RuntimeError(
            "No LLM API key configured. Set OPENAI_API_KEY or GEMINI_API_KEY in .env "
            "(rule-based matching is used automatically when keys are missing)."
        )

    last_error: Exception | None = None
    for provider in providers:
        try:
            raw = _call_provider(provider, system_prompt, user_prompt)
            return _parse_json(raw)
        except Exception as exc:  # noqa: BLE001
            last_error = exc

    raise RuntimeError(f"All LLM providers failed: {last_error}")


def _call_provider(provider: str, system_prompt: str, user_prompt: str) -> str:
    if provider == "gemini":
        return _call_gemini(system_prompt, user_prompt)
    return _call_openai(system_prompt, user_prompt)


def _call_llm(system_prompt: str, user_prompt: str) -> str:
    return _call_provider(_provider(), system_prompt, user_prompt)


def _call_openai(system_prompt: str, user_prompt: str) -> str:
    from openai import OpenAI

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
        response_format={"type": "json_object"},
    )
    return response.choices[0].message.content or "{}"


def _call_gemini(system_prompt: str, user_prompt: str) -> str:
    import google.generativeai as genai

    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
    model = genai.GenerativeModel(
        model_name,
        system_instruction=system_prompt,
        generation_config={"response_mime_type": "application/json"},
    )
    response = model.generate_content(user_prompt)
    return response.text or "{}"


def _parse_json(raw: str) -> dict[str, Any]:
    text = raw.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def normalize_tags(values: list[str]) -> list[str]:
    return sorted({v.strip().lower() for v in values if v.strip()})


def skill_overlap(required: list[str], candidate: list[str]) -> list[str]:
    req = normalize_tags(required)
    cand = normalize_tags(candidate)
    return [skill for skill in req if skill in cand or any(skill in c or c in skill for c in cand)]


def rule_based_profile(volunteer: dict[str, Any]) -> dict[str, Any]:
    skills = normalize_tags(volunteer.get("skills", []))
    interests = normalize_tags(volunteer.get("interests", []))
    availability = volunteer.get("availability", "")
    level = "beginner"
    if len(skills) >= 4:
        level = "advanced"
    elif len(skills) >= 2:
        level = "intermediate"
    return {
        "volunteer_id": volunteer["id"],
        "skill_tags": skills,
        "interest_tags": interests,
        "availability_summary": availability,
        "experience_level": level,
        "summary": f"{volunteer.get('name', 'Volunteer')} offers {', '.join(skills) or 'general support'}.",
    }


def rule_based_volunteer_rankings(
    task: dict[str, Any],
    volunteers: list[dict[str, Any]],
    profiles: list[dict[str, Any]],
    workload: dict[str, int],
) -> list[dict[str, Any]]:
    profile_by_id = {p["volunteer_id"]: p for p in profiles}
    candidates: list[dict[str, Any]] = []

    task_text = f"{task.get('title', '')} {task.get('description', '')}".lower()
    required = task.get("required_skills", [])

    for volunteer in volunteers:
        profile = profile_by_id.get(volunteer["id"], rule_based_profile(volunteer))
        matches = skill_overlap(required, profile.get("skill_tags", []))
        interest_hits = sum(1 for tag in profile.get("interest_tags", []) if tag in task_text)
        skill_score = min(len(matches) * 25, 75)
        interest_score = min(interest_hits * 15, 30)
        load = workload.get(volunteer["id"], 0)
        load_penalty = min(load * 10, 30)
        fit_score = max(0, min(100, skill_score + interest_score + 10 - load_penalty))

        notes_parts = []
        if matches:
            notes_parts.append(f"Matching skills: {', '.join(matches)}")
        if interest_hits:
            notes_parts.append("Interests align with the task")
        if load:
            notes_parts.append(f"Currently assigned {load} task(s)")
        if not notes_parts:
            notes_parts.append("Available to support based on general profile")

        candidates.append(
            {
                "volunteer_id": volunteer["id"],
                "fit_score": fit_score,
                "matching_skills": matches,
                "notes": "; ".join(notes_parts),
            }
        )

    candidates.sort(key=lambda c: c["fit_score"], reverse=True)
    return candidates


def rule_based_task_recommendations(
    volunteer: dict[str, Any],
    profile: dict[str, Any],
    open_tasks: list[dict[str, Any]],
    workload: int,
) -> list[dict[str, Any]]:
    recommendations: list[dict[str, Any]] = []

    for task in open_tasks:
        matches = skill_overlap(task.get("required_skills", []), profile.get("skill_tags", []))
        task_text = f"{task.get('title', '')} {task.get('description', '')}".lower()
        interest_hits = sum(1 for tag in profile.get("interest_tags", []) if tag in task_text)
        fit_score = max(
            0,
            min(100, len(matches) * 25 + interest_hits * 15 + 10 - workload * 5),
        )

        reason_parts = []
        if matches:
            reason_parts.append(f"Your skills ({', '.join(matches)}) match this task")
        if interest_hits:
            reason_parts.append("the task aligns with your interests")
        if not reason_parts:
            reason_parts.append("your availability fits this opportunity")

        priority = "Low"
        if fit_score >= 70:
            priority = "High"
        elif fit_score >= 45:
            priority = "Medium"

        recommendations.append(
            {
                "task_id": task["id"],
                "fit_score": fit_score,
                "reason": " and ".join(reason_parts).capitalize() + ".",
                "priority": priority,
            }
        )

    recommendations.sort(key=lambda r: r["fit_score"], reverse=True)
    return recommendations[:2]


def rule_based_decision(
    task: dict[str, Any],
    candidates: list[dict[str, Any]],
    volunteers: list[dict[str, Any]],
    max_results: int = 3,
) -> list[dict[str, Any]]:
    volunteer_names = {v["id"]: v["name"] for v in volunteers}
    recommendations: list[dict[str, Any]] = []

    for candidate in candidates[:max_results]:
        score = candidate["fit_score"]
        priority = "Low"
        if score >= 70:
            priority = "High"
        elif score >= 45:
            priority = "Medium"

        name = volunteer_names.get(candidate["volunteer_id"], "Volunteer")
        reason = (
            f"{name} is a strong fit for '{task['title']}' — {candidate.get('notes', 'good overall match')}."
        )
        recommendations.append(
            {
                "volunteer_id": candidate["volunteer_id"],
                "reason": reason,
                "priority": priority,
                "fit_score": score,
            }
        )

    return recommendations
