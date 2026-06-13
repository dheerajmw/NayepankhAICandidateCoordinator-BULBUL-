"""Admin dashboard — candidates, approvals, volunteer pool."""

from __future__ import annotations

import streamlit as st

from agents.admin_action_agent import assist_admin_decision
from agents.screening_agent import screen_candidate
from services.candidate_service import (
    approve_candidate,
    list_candidates,
    reject_candidate,
    save_screening_result,
)
from services.task_service import create_task, seed_demo_tasks
from services.volunteer_service import add_volunteer_manual, list_volunteers
from core.config import APP_NAME
from utils.auth import require_admin
from utils.helpers import format_comma_list, parse_comma_list
from utils.ui.components import kpi_row, page_header
from utils.ui.layout import setup_page

setup_page(f"Admin — {APP_NAME}", active="admin", show_admin_actions=True)

if not require_admin():
    st.stop()

seed_demo_tasks()

page_header("Admin Dashboard", "Review candidates, manage the volunteer pool, and create tasks.")

pending = list_candidates("pending")
approved_c = list_candidates("approved")
rejected_c = list_candidates("rejected")
volunteers = list_volunteers()

kpi_row(
    [
        {"label": "Pending", "value": str(len(pending)), "icon": "pending_actions", "badge": "Review"},
        {"label": "Approved Volunteers", "value": str(len(approved_c)), "icon": "check_circle", "badge": "Done"},
        {"label": "Volunteer Pool", "value": str(len(volunteers)), "icon": "group", "badge": "Pool"},
        {"label": "Rejected", "value": str(len(rejected_c)), "icon": "cancel", "badge": "Closed"},
    ]
)

tab_candidates, tab_add, tab_pool, tab_tasks = st.tabs(
    ["Review candidates", "Add volunteer", "Volunteer pool", "Create task"]
)

with tab_candidates:
    if not pending:
        st.info("No pending applications.")
    for candidate in pending:
        screening = candidate.get("ai_screening")
        with st.expander(f"{candidate['name']} — {candidate['email']}", expanded=True):
            st.write(f"**Skills:** {format_comma_list(candidate.get('skills', [])) or '—'}")
            st.write(f"**Interests:** {format_comma_list(candidate.get('interests', [])) or '—'}")
            st.write(f"**Availability:** {candidate.get('availability', '—')}")
            st.write(f"**Motivation:** {candidate.get('motivation', '—')}")

            c1, c2 = st.columns(2)
            with c1:
                if st.button("Run AI screening", key=f"screen_{candidate['id']}"):
                    result = screen_candidate(candidate)
                    save_screening_result(candidate["id"], result)
                    st.rerun()
            with c2:
                if screening and st.button("Admin AI assist", key=f"assist_{candidate['id']}"):
                    advice = assist_admin_decision(candidate, screening)
                    st.session_state[f"advice_{candidate['id']}"] = advice

            if screening:
                st.markdown("##### AI screening")
                st.write(f"Score: **{screening.get('score')}/100** · Decision: **{screening.get('decision')}**")
                st.write(f"Suggested role: {screening.get('suggested_role')}")
                st.caption(screening.get("reasoning", ""))

            advice = st.session_state.get(f"advice_{candidate['id']}")
            if advice:
                st.markdown("##### Admin assist")
                st.write(advice["summary"])
                st.write(f"Recommendation: **{advice['recommendation'].upper()}** ({advice['confidence']}% confidence)")

            b1, b2 = st.columns(2)
            with b1:
                if st.button("Approve", key=f"approve_{candidate['id']}", type="primary"):
                    approve_candidate(candidate["id"])
                    st.success(f"{candidate['name']} added to volunteer pool.")
                    st.rerun()
            with b2:
                if st.button("Reject", key=f"reject_{candidate['id']}"):
                    reject_candidate(candidate["id"])
                    st.warning("Application rejected.")
                    st.rerun()

with tab_add:
    st.subheader("Add volunteer directly")
    st.caption("Bypasses AI screening and approval — goes straight to the volunteer pool.")
    with st.form("admin_add_volunteer"):
        name = st.text_input("Full name *")
        email = st.text_input("Email *")
        skills = st.text_input("Skills (comma-separated)")
        interests = st.text_input("Interests (comma-separated)")
        availability = st.text_area("Availability *", height=80)
        submitted = st.form_submit_button("Add to volunteer pool", type="primary")
    if submitted:
        if not name.strip() or not email.strip() or not availability.strip():
            st.error("Name, email, and availability are required.")
        else:
            try:
                v = add_volunteer_manual(
                    name, email, parse_comma_list(skills), parse_comma_list(interests), availability
                )
                st.success(f"Added {v['name']} to the volunteer pool.")
            except ValueError as exc:
                st.error(str(exc))

with tab_pool:
    if not volunteers:
        st.info("Volunteer pool is empty.")
    for v in volunteers:
        with st.expander(f"{v['name']} ({v['source']})"):
            st.write(f"**Email:** {v['email']}")
            st.write(f"**Skills:** {format_comma_list(v.get('skills', []))}")
            st.write(f"**Interests:** {format_comma_list(v.get('interests', []))}")
            st.write(f"**Availability:** {v.get('availability', '—')}")
            memory = v.get("memory", {})
            st.write(f"**Assignments:** {len(memory.get('assignments', []))}")
            st.write(f"**Completed:** {len(memory.get('completed_tasks', []))}")

with tab_tasks:
    seed_demo_tasks()
    st.subheader("Create a new task")
    with st.form("admin_create_task"):
        title = st.text_input("Title *")
        description = st.text_area("Description *")
        skills = st.text_input("Required skills (comma-separated)")
        deadline = st.date_input("Deadline *")
        priority = st.selectbox("Priority", ["High", "Medium", "Low"])
        submitted = st.form_submit_button("Create task", type="primary")
    if submitted:
        if not title.strip() or not description.strip():
            st.error("Title and description are required.")
        else:
            task = create_task(
                title=title,
                description=description,
                required_skills=parse_comma_list(skills),
                deadline=str(deadline),
                priority=priority,
            )
            st.success(f"Created task: {task['title']}")
