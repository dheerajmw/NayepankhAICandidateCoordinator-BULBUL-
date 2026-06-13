"""AI task assignment and status tracking."""

from __future__ import annotations

import streamlit as st

from agents.task_matching_agent import match_all_open_tasks, match_volunteers_to_task
from services.task_service import assign_task, list_tasks, open_tasks, seed_demo_tasks, update_task_status
from services.volunteer_service import list_volunteers, volunteer_name, workload_counts
from core.config import APP_NAME
from utils.auth import require_admin
from utils.ui.components import ai_match_card, kpi_row, page_header, status_chip
from utils.ui.layout import setup_page
from utils.ui.render import render_html

setup_page(f"Tasks — {APP_NAME}", active="tasks", show_admin_actions=True)

if not require_admin():
    st.stop()

seed_demo_tasks()

volunteers = list_volunteers()
tasks = list_tasks()
open_list = open_tasks()
workload = workload_counts()

page_header("Task Assignment", "AI-generated volunteer matches with reasoning and status tracking.")

kpi_row(
    [
        {"label": "Open Tasks", "value": str(len(open_list)), "icon": "task_alt", "badge": "Match"},
        {"label": "Volunteers", "value": str(len(volunteers)), "icon": "group", "badge": "Pool"},
        {"label": "Assigned", "value": str(len([t for t in tasks if t.get("assigned_volunteer_id")])), "icon": "assignment_ind", "badge": "Active"},
        {"label": "Completed", "value": str(len([t for t in tasks if t.get("status") == "completed"])), "icon": "check_circle", "badge": "Done"},
    ]
)

if not volunteers:
    st.warning("Volunteer pool is empty. Approve candidates or add volunteers from the Admin Dashboard.")
    st.stop()

if not open_list:
    st.info("No open tasks. Create tasks from the Admin Dashboard.")
    st.stop()

tab_ai, tab_status = st.tabs(["AI matching", "Task status"])

with tab_ai:
    if st.button("Generate AI matches for all open tasks", type="primary"):
        with st.spinner("Matching volunteers to tasks..."):
            st.session_state["ai_matches"] = match_all_open_tasks(open_list, volunteers, workload)

    matches = st.session_state.get("ai_matches")
    if not matches:
        st.caption("Click the button above to run AI task matching.")
    else:
        for item in matches:
            task = item["task"]
            st.markdown(f"### {task['title']}")
            st.caption(task.get("description", ""))
            for idx, match in enumerate(item["matches"]):
                ai_match_card(
                    match.get("volunteer_name", "Volunteer"),
                    match.get("reasoning", ""),
                    f"Score {match.get('fit_score', 0)} · {match.get('priority', 'Medium')}",
                    tertiary=idx > 0,
                )
                if st.button(
                    f"Assign {match.get('volunteer_name')}",
                    key=f"assign_{task['id']}_{match['volunteer_id']}",
                    type="primary" if idx == 0 else "secondary",
                ):
                    assign_task(
                        task["id"],
                        match["volunteer_id"],
                        match.get("reasoning", "AI match"),
                        match.get("priority"),
                        ai_assigned=True,
                    )
                    st.success(f"Assigned {match.get('volunteer_name')} to {task['title']}")
                    st.rerun()

    st.divider()
    st.subheader("Match a single task")
    task_labels = {t["title"]: t["id"] for t in open_list}
    selected = st.selectbox("Select task", options=list(task_labels.keys()))
    if st.button("Get matches for selected task"):
        task = next(t for t in open_list if t["id"] == task_labels[selected])
        results = match_volunteers_to_task(task, volunteers, workload)
        for idx, match in enumerate(results):
            ai_match_card(
                match.get("volunteer_name", ""),
                match.get("reasoning", ""),
                f"Score {match.get('fit_score', 0)}",
                tertiary=idx > 0,
            )

with tab_status:
    for task in tasks:
        status = task.get("status", "open")
        assignee = volunteer_name(task.get("assigned_volunteer_id"))
        chip = status_chip(status, status.replace("_", " ").title())
        render_html(
            f"""
<div class="np-card">
  <div style="display:flex;justify-content:space-between;align-items:start;gap:1rem;">
    <div>
      <h4 style="margin:0 0 0.35rem 0;">{task["title"]}</h4>
      <p style="margin:0;color:var(--np-on-surface-variant);font-size:0.9rem;">{task.get("description", "")}</p>
      <p style="margin:0.5rem 0 0 0;font-size:0.8rem;color:var(--np-outline);">
        Assignee: {assignee} · Deadline: {task.get("deadline", "—")}
      </p>
    </div>
    {chip}
  </div>
</div>
"""
        )
        if task.get("assigned_volunteer_id"):
            new_status = st.selectbox(
                "Update status",
                ["assigned", "in_progress", "completed"],
                index=["assigned", "in_progress", "completed"].index(status)
                if status in ("assigned", "in_progress", "completed")
                else 0,
                key=f"status_{task['id']}",
            )
            if st.button("Save status", key=f"save_{task['id']}"):
                update_task_status(task["id"], new_status)
                st.rerun()
