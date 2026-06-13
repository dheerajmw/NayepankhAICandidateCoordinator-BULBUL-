"""Summary Generator Agent — contribution narratives and structured reports."""

from __future__ import annotations

import json
from datetime import date
from typing import Any

from core import ai_engine
from core.prompts import SUMMARY_ADMIN_USER, SUMMARY_GENERATOR_SYSTEM, SUMMARY_VOLUNTEER_USER
from utils.helpers import save_report
from utils.report_metrics import compute_org_metrics, compute_volunteer_metrics

CERTIFICATE_MILESTONE_TASKS = 1


def _rule_based_volunteer_narrative(metrics: dict[str, Any]) -> dict[str, Any]:
    name = metrics["volunteer_name"]
    completed = metrics["tasks_completed"]
    skills = metrics["skills_utilized"]
    rate = metrics["completion_rate"]

    if completed == 0:
        narrative = (
            f"{name} is registered with NayePankh Foundation and ready to contribute. "
            f"No completed tasks yet in this period."
        )
        highlights = ["Registered volunteer", "Awaiting or working on assigned tasks"]
    else:
        skill_text = ", ".join(skills) if skills else "various areas"
        narrative = (
            f"{name} completed {completed} task(s) with a {rate}% completion rate. "
            f"Skills utilized include {skill_text}, supporting NayePankh Foundation's mission."
        )
        highlights = [
            f"{completed} task(s) completed",
            f"Skills applied: {skill_text}" if skills else "Contributions across assigned tasks",
        ]

    return {"narrative": narrative, "highlights": highlights}


def _rule_based_admin_narrative(metrics: dict[str, Any]) -> dict[str, Any]:
    completed = metrics["tasks_completed"]
    volunteers = metrics["volunteer_count"]
    rate = metrics["completion_rate"]
    skills = metrics["skills_utilized"]

    narrative = (
        f"During this period, {volunteers} volunteer(s) were tracked with "
        f"{completed} completed task(s) and a {rate}% overall completion rate."
    )
    if skills:
        narrative += f" Skills utilized across the program: {', '.join(skills)}."

    return {
        "narrative": narrative,
        "highlights": [
            f"{volunteers} volunteer(s) in report",
            f"{completed} task(s) completed ({rate}%)",
        ],
    }


def _generate_narrative(system: str, user_template: str, metrics: dict[str, Any]) -> dict[str, Any]:
    if ai_engine.llm_configured():
        prompt = user_template.format(metrics_json=json.dumps(metrics, indent=2))
        return ai_engine.complete_json(system, prompt)
    if "volunteer_name" in metrics:
        return _rule_based_volunteer_narrative(metrics)
    return _rule_based_admin_narrative(metrics)


def generate_volunteer_summary(
    volunteer_id: str,
    start: date | None = None,
    end: date | None = None,
    *,
    persist: bool = True,
) -> dict[str, Any]:
    metrics = compute_volunteer_metrics(volunteer_id, start, end)
    narrative_data = _generate_narrative(
        SUMMARY_GENERATOR_SYSTEM,
        SUMMARY_VOLUNTEER_USER,
        metrics,
    )

    report = {
        "report_type": "volunteer_summary",
        "volunteer_id": volunteer_id,
        "volunteer_name": metrics["volunteer_name"],
        "period_start": metrics["period_start"],
        "period_end": metrics["period_end"],
        "metrics": metrics,
        "narrative": narrative_data.get("narrative", ""),
        "highlights": narrative_data.get("highlights", []),
    }

    if persist:
        saved = save_report(report)
        report["id"] = saved["id"]
        report["created_at"] = saved["created_at"]
    return report


def generate_admin_report(
    volunteer_id: str | None = None,
    start: date | None = None,
    end: date | None = None,
    *,
    persist: bool = True,
) -> dict[str, Any]:
    metrics = compute_org_metrics(start, end, volunteer_id)
    narrative_data = _generate_narrative(
        SUMMARY_GENERATOR_SYSTEM,
        SUMMARY_ADMIN_USER,
        metrics,
    )

    report = {
        "report_type": "admin_contribution",
        "volunteer_id": volunteer_id,
        "period_start": metrics["period_start"],
        "period_end": metrics["period_end"],
        "metrics": metrics,
        "narrative": narrative_data.get("narrative", ""),
        "highlights": narrative_data.get("highlights", []),
    }

    if persist:
        saved = save_report(report)
        report["id"] = saved["id"]
        report["created_at"] = saved["created_at"]
    return report


def eligible_for_certificate(volunteer_id: str) -> bool:
    metrics = compute_volunteer_metrics(volunteer_id)
    return metrics["tasks_completed"] >= CERTIFICATE_MILESTONE_TASKS
