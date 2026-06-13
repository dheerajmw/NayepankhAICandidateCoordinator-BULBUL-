"""NayePankh Bulbul V2 — AI Volunteer Coordinator (home)."""

from __future__ import annotations

import streamlit as st

from core.config import admin_auth_required, app_env, storage_label
from core.llm_engine import llm_configured
from services.candidate_service import list_candidates
from services.task_service import list_tasks
from services.volunteer_service import list_volunteers
from utils.ui.components import brand_block, kpi_row, page_header, status_pills
from utils.ui.logo import logo_mark_path
from utils.ui.styles import inject_theme


def main() -> None:
    st.set_page_config(
        page_title="NayePankh Bulbul",
        page_icon=logo_mark_path(),
        layout="wide",
        initial_sidebar_state="expanded",
    )

    inject_theme()

    with st.sidebar:
        brand_block()
        st.caption("Use the page menu above to open Apply, Admin, or Task Assignment.")

    status_pills(
        [
            (storage_label(), True),
            ("LLM enabled" if llm_configured() else "Rule-based AI", llm_configured()),
            (f"Env: {app_env()}", True),
            ("V2 Dual-Sided", True),
        ]
    )

    page_header(
        "NayePankh Bulbul AI Volunteer Coordinator",
        "V2 — Candidate applications, admin approval, unified volunteer pool, and AI task matching.",
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
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            **1. Candidate Apply**  
            Public users submit applications with skills, interests, and motivation.  
            AI screens each application automatically.
            """
        )
    with col2:
        st.markdown(
            """
            **2. Admin Dashboard**  
            NGO admins approve or reject candidates, or add volunteers directly.  
            Approved candidates join the unified volunteer pool.
            """
        )
    with col3:
        st.markdown(
            """
            **3. Task Assignment**  
            AI matches volunteers to open tasks using skills, interests, availability,  
            and assignment memory.
            """
        )

    if admin_auth_required():
        st.info("Admin pages require the password set in `ADMIN_PASSWORD`.")

    st.caption("Open **Candidate Apply**, **Admin Dashboard**, or **Task Assignment** from the sidebar page list.")


if __name__ == "__main__":
    main()
