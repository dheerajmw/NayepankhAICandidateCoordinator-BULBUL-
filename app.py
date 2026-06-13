"""Bulbul by NayePankh Foundation — AI Volunteer Coordinator (home)."""

from __future__ import annotations

import streamlit as st

from core.config import APP_NAME, admin_auth_required, storage_label
from core.llm_engine import llm_configured
from services.candidate_service import list_candidates
from services.task_service import list_tasks
from services.volunteer_service import list_volunteers
from utils.ui.components import flow_steps, hero_panel, kpi_row, status_pills
from utils.ui.layout import setup_page


def main() -> None:
    setup_page(APP_NAME, active="overview")

    status_pills(
        [
            (storage_label(), True),
            ("LLM enabled" if llm_configured() else "Rule-based AI", llm_configured()),
            ("V2 Dual-Sided", True),
        ]
    )

    hero_panel(
        APP_NAME,
        "Candidate applications, admin approval, unified volunteer pool, and AI task matching — one intelligence layer for NGO ops.",
        badge="Luminous Intelligence",
    )

    pending = len(list_candidates("pending"))
    volunteers = len(list_volunteers())
    tasks = len(list_tasks())

    kpi_row(
        [
            {"label": "Pending Applications", "value": str(pending), "icon": "pending_actions", "badge": "Review"},
            {"label": "Volunteer Pool", "value": str(volunteers), "icon": "group", "badge": "Active"},
            {"label": "Tasks", "value": str(tasks), "icon": "task_alt", "badge": "Ops"},
        ]
    )

    st.markdown("### How it works")
    flow_steps(
        [
            (
                1,
                "Volunteer Onboarding",
                "Public users submit applications with skills, interests, and motivation. AI screens each application automatically.",
            ),
            (
                2,
                "Admin Dashboard",
                "NGO admins approve or reject candidates, or add volunteers directly. Approved candidates join the unified volunteer pool.",
            ),
            (
                3,
                "Task Assignment",
                "AI matches volunteers to open tasks using skills, interests, availability, and assignment memory.",
            ),
        ]
    )

    if admin_auth_required():
        st.info("Admin pages require a password configured on the server.")


if __name__ == "__main__":
    main()
