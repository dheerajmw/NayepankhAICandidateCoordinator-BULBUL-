"""NayePankh Bulbul AI Volunteer Coordinator — Streamlit app."""

from __future__ import annotations

import html
from datetime import date

import streamlit as st

from agents.decision_engine import (
    apply_ai_assignment,
    recommend_tasks_for_volunteer,
    recommend_volunteers_for_task,
)
from agents.summary_agent import (
    eligible_for_certificate,
    generate_admin_report,
    generate_volunteer_summary,
)
from automation.reminder_engine import (
    get_task_notification_summary,
    run_reminder_check,
    send_completion_notification,
)
from core import ai_engine
from core.config import admin_auth_required, app_env, storage_label, use_supabase
from core import prompts
from utils import email_service
from utils.auth import is_admin_authenticated, logout_admin, require_admin
from utils.certificate_pdf import generate_certificate_pdf
from utils.helpers import (
    ASSIGNMENT_STATUSES,
    PRIORITIES,
    add_task,
    add_volunteer,
    assign_task,
    format_comma_list,
    get_match_history,
    get_notifications,
    get_reports,
    get_tasks,
    get_volunteers,
    parse_comma_list,
    update_task_status,
    update_volunteer_reminder_preferences,
    volunteer_name,
)
from utils.report_export import export_report_csv, export_report_pdf
from utils.report_metrics import compute_volunteer_metrics
from utils.ui.components import (
    ai_match_card,
    brand_block,
    form_panel_header,
    kpi_row,
    page_header,
    status_pills,
    system_health_card,
    volunteer_hero_panel,
)
from utils.ui.logo import logo_mark_path
from utils.ui.render import render_html
from utils.ui.styles import inject_theme

st.set_page_config(
    page_title="NayePankh Bulbul",
    page_icon=logo_mark_path(),
    layout="wide",
    initial_sidebar_state="expanded",
)

STATUS_LABELS = {
    "pending": "Pending",
    "in_progress": "In Progress",
    "completed": "Completed",
}

NOTIFICATION_LABELS = {
    "deadline_3d": "3-day reminder",
    "deadline_1d": "1-day urgent reminder",
    "overdue": "Overdue escalation",
    "completion": "Completion confirmation",
}

ADMIN_SECTIONS = [
    "Dashboard",
    "Volunteers",
    "Task Matching",
    "Reports",
    "Notifications",
    "AI Insights",
    "Settings",
]


def render_header() -> None:
    status_pills(
        [
            (storage_label(), True),
            ("LLM enabled" if ai_engine.llm_configured() else "Rule-based AI", ai_engine.llm_configured()),
            ("SMTP enabled" if email_service.email_configured() else "Email dry-run", email_service.email_configured()),
            (f"Prompt {prompts.PROMPT_VERSION_LABEL}", True),
            (app_env(), True),
        ]
    )


def render_task_card(task: dict, show_ai_fields: bool = True) -> None:
    status = STATUS_LABELS.get(task["status"], task["status"])
    status_class = {
        "Pending": "np-status-pending",
        "In Progress": "np-status-in_progress",
        "Completed": "np-status-completed",
    }.get(status, "np-status-pending")

    meta_parts = [f"Deadline: {task['deadline']}"]
    if show_ai_fields and task.get("priority"):
        meta_parts.append(f"Priority: {task['priority']}")
    notify = get_task_notification_summary(task["id"])
    if notify["last_notified"]:
        label = NOTIFICATION_LABELS.get(notify["last_type"], notify["last_type"])
        meta_parts.append(f"Last notified: {notify['last_notified']} ({label})")

    reason_block = ""
    if show_ai_fields and task.get("assignment_reason"):
        reason_block = (
            f'<p style="margin:0.75rem 0 0 0;padding:0.75rem;background:#f2f3ff;border-radius:8px;'
            f'font-size:0.875rem;color:#131b2e;"><strong>Why assigned:</strong> '
            f'{html.escape(task["assignment_reason"])}</p>'
        )

    render_html(
        f"""
<div class="np-card">
  <div style="display:flex;justify-content:space-between;align-items:start;gap:1rem;">
    <div>
      <h4 style="margin:0 0 0.5rem 0;font-size:1.1rem;">{html.escape(task["title"])}</h4>
      <p style="margin:0;color:#434655;font-size:0.925rem;">{html.escape(task["description"])}</p>
    </div>
    <span class="np-status {status_class}">{status}</span>
  </div>
  <p style="margin:0.75rem 0 0 0;font-size:0.8rem;color:#737686;">{" · ".join(html.escape(p) for p in meta_parts)}</p>
  {reason_block}
</div>
"""
    )


def render_volunteer_portal() -> None:
    page_header(
        "Volunteer Registration",
        "Join NayePankh Foundation and get AI-matched to meaningful tasks.",
        compact=True,
    )

    hero_col, form_col = st.columns([1, 1], gap="large")
    with hero_col:
        with st.container(key="volunteer_hero_shell"):
            volunteer_hero_panel()

    with form_col:
        with st.container(border=True, key="volunteer_form_shell", gap="small"):
            form_panel_header(
                "Create your volunteer profile",
                "Tell us about your skills and availability so AI can find the right tasks.",
                shell=True,
            )
            with st.form("volunteer_registration", clear_on_submit=True):
                name_col, email_col = st.columns(2, gap="medium")
                with name_col:
                    name = st.text_input("Full name *", placeholder="Your full name")
                with email_col:
                    email = st.text_input("Email *", placeholder="you@example.com")

                skills_col, interests_col = st.columns(2, gap="medium")
                with skills_col:
                    skills = st.text_input(
                        "Skills (comma-separated)",
                        placeholder="Teaching, Design, Social media",
                    )
                with interests_col:
                    interests = st.text_input(
                        "Interests (comma-separated)",
                        placeholder="Education, Environment",
                    )

                availability = st.text_area(
                    "Availability *",
                    placeholder="e.g. Weekends, 2–4 hours per week",
                    height=88,
                )
                submitted = st.form_submit_button(
                    "Register & activate AI matching",
                    type="primary",
                    use_container_width=True,
                )

        if submitted:
            if not name.strip() or not email.strip() or not availability.strip():
                st.error("Name, email, and availability are required.")
            else:
                volunteer = add_volunteer(
                    name=name,
                    email=email,
                    skills=parse_comma_list(skills),
                    interests=parse_comma_list(interests),
                    availability=availability,
                )
                st.success(f"Registration complete. Welcome, {volunteer['name']}!")
                st.info("Scroll down to view AI recommendations and your contribution summary.")

    st.divider()
    page_header("My Tasks & AI Recommendations", "Enter your email to view assignments and AI-suggested open tasks.")
    email_lookup = st.text_input(
        "Volunteer email",
        placeholder="you@example.com",
        key="volunteer_email_lookup",
    )
    if not email_lookup.strip():
        return

    volunteers = get_volunteers()
    match = next(
        (v for v in volunteers if v["email"].lower() == email_lookup.strip().lower()),
        None,
    )
    if not match:
        st.warning("No volunteer found with that email.")
        return

    my_tasks = [t for t in get_tasks() if t.get("assigned_volunteer_id") == match["id"]]

    col_assigned, col_ai = st.columns(2)

    with col_assigned:
        st.markdown("**Assigned tasks**")
        if not my_tasks:
            st.info("No tasks assigned yet.")
        else:
            for task in my_tasks:
                render_task_card(task)

    with col_ai:
        st.markdown("**AI task recommendations**")
        if st.button("Get AI recommendations", key="volunteer_ai_recs", type="primary"):
            with st.spinner("Analyzing your profile and open tasks..."):
                try:
                    recs = recommend_tasks_for_volunteer(match["id"])
                    st.session_state[f"vol_recs_{match['id']}"] = recs
                except ValueError as exc:
                    st.error(str(exc))

        recs = st.session_state.get(f"vol_recs_{match['id']}", [])
        if not recs:
            st.caption("Up to 2 best-fit open tasks will appear here.")
        else:
            for rec in recs:
                ai_match_card(
                    rec["task_title"],
                    rec["reason"],
                    f"{rec['priority']} · Fit {rec['fit_score']}",
                    tertiary=rec.get("priority") == "High",
                )

    st.divider()
    st.subheader("Reminder preferences")
    prefs = match.get("reminder_preferences") or {"enabled": True, "email": True}
    enabled = st.checkbox("Receive task reminders", value=prefs.get("enabled", True), key=f"rem_en_{match['id']}")
    email_on = st.checkbox(
        "Email notifications",
        value=prefs.get("email", True),
        disabled=not enabled,
        key=f"rem_em_{match['id']}",
    )
    if st.button("Save reminder preferences", key=f"save_prefs_{match['id']}"):
        update_volunteer_reminder_preferences(match["id"], enabled, email_on)
        st.success("Reminder preferences saved.")

    st.divider()
    render_volunteer_contribution(match)


def render_volunteer_contribution(volunteer: dict) -> None:
    st.subheader("My contribution summary")
    use_dates = st.checkbox("Filter by date range", key=f"vol_dates_{volunteer['id']}")
    start = end = None
    if use_dates:
        c1, c2 = st.columns(2)
        start = c1.date_input("From", value=date.today().replace(day=1), key=f"vol_start_{volunteer['id']}")
        end = c2.date_input("To", value=date.today(), key=f"vol_end_{volunteer['id']}")

    if st.button("Generate my summary", key=f"vol_summary_{volunteer['id']}", type="primary"):
        with st.spinner("Generating contribution summary..."):
            report = generate_volunteer_summary(volunteer["id"], start if use_dates else None, end if use_dates else None)
            st.session_state[f"vol_report_{volunteer['id']}"] = report

    report = st.session_state.get(f"vol_report_{volunteer['id']}")
    if not report:
        st.caption("Generate a personal impact summary with task history and skills utilized.")
        return

    st.markdown(f"**{report['narrative']}**")
    for highlight in report.get("highlights", []):
        st.markdown(f"- {highlight}")

    metrics = report["metrics"]
    c1, c2, c3 = st.columns(3)
    c1.metric("Completed", metrics["tasks_completed"])
    c2.metric("In progress", metrics["tasks_in_progress"])
    c3.metric("Completion rate", f"{metrics['completion_rate']}%")

    if metrics.get("task_history"):
        st.markdown("**Task history**")
        st.dataframe(metrics["task_history"], use_container_width=True, hide_index=True)

    if eligible_for_certificate(volunteer["id"]):
        cert_pdf = generate_certificate_pdf(volunteer, metrics)
        st.download_button(
            "Download certificate (PDF)",
            data=cert_pdf,
            file_name=f"certificate_{volunteer['name'].replace(' ', '_')}.pdf",
            mime="application/pdf",
            key=f"cert_{volunteer['id']}",
        )
    else:
        st.info("Complete at least one task to unlock your certificate.")


def render_reports_admin() -> None:
    page_header("Reports & Certificates", "Generate contribution summaries and export PDF/CSV outputs.")
    volunteers = get_volunteers()

    tab_volunteer, tab_org, tab_saved = st.tabs(
        ["Volunteer report", "Organization report", "Saved reports"]
    )

    with tab_volunteer:
        if not volunteers:
            st.info("No volunteers registered yet.")
        else:
            vol_labels = {v["name"]: v["id"] for v in volunteers}
            selected = st.selectbox("Volunteer", options=list(vol_labels.keys()))
            use_dates = st.checkbox("Filter by date range", key="admin_vol_dates")
            start = end = None
            if use_dates:
                c1, c2 = st.columns(2)
                start = c1.date_input("From", value=date.today().replace(day=1), key="admin_vol_start")
                end = c2.date_input("To", value=date.today(), key="admin_vol_end")

            if st.button("Generate volunteer report", type="primary", key="gen_vol_report"):
                with st.spinner("Generating report..."):
                    report = generate_volunteer_summary(
                        vol_labels[selected],
                        start if use_dates else None,
                        end if use_dates else None,
                    )
                    st.session_state["admin_vol_report"] = report

            report = st.session_state.get("admin_vol_report")
            if report:
                _render_report_preview(report)
                volunteer = next(v for v in volunteers if v["id"] == report["volunteer_id"])
                _render_report_downloads(report, volunteer)

    with tab_org:
        scope = st.radio("Scope", ["All volunteers", "Single volunteer"], horizontal=True)
        volunteer_id = None
        if scope == "Single volunteer" and volunteers:
            vol_labels = {v["name"]: v["id"] for v in volunteers}
            volunteer_id = vol_labels[st.selectbox("Volunteer", options=list(vol_labels.keys()), key="org_vol")]

        use_dates = st.checkbox("Filter by date range", key="admin_org_dates")
        start = end = None
        if use_dates:
            c1, c2 = st.columns(2)
            start = c1.date_input("From", value=date.today().replace(day=1), key="admin_org_start")
            end = c2.date_input("To", value=date.today(), key="admin_org_end")

        if st.button("Generate organization report", type="primary", key="gen_org_report"):
            with st.spinner("Generating report..."):
                report = generate_admin_report(
                    volunteer_id,
                    start if use_dates else None,
                    end if use_dates else None,
                )
                st.session_state["admin_org_report"] = report

        report = st.session_state.get("admin_org_report")
        if report:
            _render_report_preview(report, org=True)
            _render_report_downloads(report)

    with tab_saved:
        reports = get_reports()
        if not reports:
            st.info("No saved reports yet.")
        else:
            for saved in reversed(reports[-20:]):
                label = saved.get("report_type", "report").replace("_", " ").title()
                name = saved.get("volunteer_name") or "Organization"
                with st.expander(f"{label} · {name} · {saved.get('created_at', '')}", expanded=False):
                    st.write(saved.get("narrative", ""))
                    st.caption(f"ID: {saved.get('id')}")


def _render_report_preview(report: dict, org: bool = False) -> None:
    st.markdown(f"**{report['narrative']}**")
    for highlight in report.get("highlights", []):
        st.markdown(f"- {highlight}")

    metrics = report["metrics"]
    if org:
        c1, c2, c3 = st.columns(3)
        c1.metric("Volunteers", metrics["volunteer_count"])
        c2.metric("Tasks completed", metrics["tasks_completed"])
        c3.metric("Completion rate", f"{metrics['completion_rate']}%")
    else:
        c1, c2, c3 = st.columns(3)
        c1.metric("Completed", metrics["tasks_completed"])
        c2.metric("Total tasks", metrics["tasks_total"])
        c3.metric("Completion rate", f"{metrics['completion_rate']}%")


def _render_report_downloads(report: dict, volunteer: dict | None = None) -> None:
    c1, c2, c3 = st.columns(3)
    base = (report.get("volunteer_name") or "organization").replace(" ", "_")
    c1.download_button(
        "Export CSV",
        data=export_report_csv(report),
        file_name=f"report_{base}.csv",
        mime="text/csv",
        key=f"csv_{report.get('id', base)}",
    )
    c2.download_button(
        "Export PDF",
        data=export_report_pdf(report),
        file_name=f"report_{base}.pdf",
        mime="application/pdf",
        key=f"pdf_{report.get('id', base)}",
    )
    if volunteer and eligible_for_certificate(volunteer["id"]):
        metrics = report.get("metrics") or compute_volunteer_metrics(volunteer["id"])
        c3.download_button(
            "Certificate PDF",
            data=generate_certificate_pdf(volunteer, metrics),
            file_name=f"certificate_{base}.pdf",
            mime="application/pdf",
            key=f"cert_admin_{report.get('id', base)}",
        )


def render_dashboard() -> None:
    page_header("Operations Dashboard", "Overview of volunteers, tasks, and coordination health.")
    volunteers = get_volunteers()
    tasks = get_tasks()
    assigned = sum(1 for t in tasks if t.get("assigned_volunteer_id"))
    completed = sum(1 for t in tasks if t["status"] == "completed")
    notifications_sent = sum(1 for n in get_notifications() if n.get("status") == "sent")

    kpi_row(
        [
            {"label": "Total Volunteers", "value": str(len(volunteers)), "icon": "group", "badge": "Live"},
            {"label": "Active Tasks", "value": str(len(tasks)), "icon": "task_alt", "badge": f"{assigned} assigned"},
            {"label": "Completed", "value": str(completed), "icon": "check_circle", "badge": "Impact"},
            {
                "label": "Notifications Sent",
                "value": str(notifications_sent),
                "icon": "notifications",
                "badge": "Automation",
            },
        ]
    )

    if not tasks:
        st.info("No tasks yet. Create one under Task Matching.")
        return

    st.markdown("#### Task overview")
    rows = []
    for task in tasks:
        notify = get_task_notification_summary(task["id"])
        last = notify["last_notified"] or "—"
        if notify["last_type"]:
            last = f"{last} ({NOTIFICATION_LABELS.get(notify['last_type'], notify['last_type'])})"
        rows.append(
            {
                "Task": task["title"],
                "Volunteer": volunteer_name(task.get("assigned_volunteer_id")),
                "Deadline": task["deadline"],
                "Status": STATUS_LABELS.get(task["status"], task["status"]),
                "Priority": task.get("priority") or "—",
                "Last notified": last,
                "AI assigned": "Yes" if task.get("ai_assigned") else "No",
                "Skills needed": format_comma_list(task.get("required_skills", [])),
            }
        )
    st.dataframe(rows, use_container_width=True, hide_index=True)


def render_notifications_admin() -> None:
    page_header("Notifications & Automation", "Automated deadline reminders, escalations, and delivery history.")

    col_run, col_info = st.columns([1, 2])
    with col_run:
        if st.button("Run reminder check now", type="primary"):
            with st.spinner("Checking deadlines and sending notifications..."):
                sent = run_reminder_check()
            if sent:
                st.success(f"Processed {len(sent)} notification(s).")
            else:
                st.info("No new reminders due right now.")
            st.rerun()

    with col_info:
        st.caption(
            "Schedule externally with `python scripts/run_reminders.py` (cron/n8n) "
            "or `python scripts/scheduled_reminders.py` (APScheduler)."
        )

    st.divider()
    st.subheader("Notification history")
    notifications = get_notifications()
    if not notifications:
        st.info("No notifications logged yet. Run a reminder check or complete a task.")
        return

    rows = []
    for record in reversed(notifications[-50:]):
        task = next((t for t in get_tasks() if t["id"] == record.get("task_id")), None)
        rows.append(
            {
                "Sent at": record.get("sent_at"),
                "Type": NOTIFICATION_LABELS.get(
                    record.get("notification_type"), record.get("notification_type")
                ),
                "Task": task["title"] if task else "—",
                "Volunteer": volunteer_name(record.get("volunteer_id")),
                "Recipient": record.get("recipient"),
                "Channel": record.get("channel"),
                "Status": record.get("status"),
                "Subject": record.get("subject"),
            }
        )
    st.dataframe(rows, use_container_width=True, hide_index=True)


def render_match_history() -> None:
    page_header("AI Insights", "Audit trail of AI matching runs and assignment decisions.")
    history = get_match_history()

    if not history:
        st.info("No AI match records yet.")
        return

    for record in reversed(history[-20:]):
        label = record.get("match_type", "unknown").replace("_", " ").title()
        with st.expander(f"{label} · {record.get('created_at', '')}", expanded=False):
            st.json(record)


def render_volunteers_admin() -> None:
    page_header("Volunteer Directory", "Browse registered volunteers, skills, and availability.")
    volunteers = get_volunteers()

    if not volunteers:
        st.info("No volunteers registered yet.")
        return

    for volunteer in volunteers:
        with st.expander(volunteer["name"], expanded=False):
            st.write(f"**Email:** {volunteer['email']}")
            st.write(f"**Skills:** {format_comma_list(volunteer.get('skills', [])) or '—'}")
            st.write(f"**Interests:** {format_comma_list(volunteer.get('interests', [])) or '—'}")
            st.write(f"**Availability:** {volunteer.get('availability', '—')}")
            st.caption(f"Registered: {volunteer.get('created_at', '—')}")


def render_ai_recommendations() -> None:
    st.subheader("AI volunteer recommendations")
    tasks = get_tasks()
    volunteers = get_volunteers()
    unassigned = [t for t in tasks if not t.get("assigned_volunteer_id")]

    if not unassigned:
        st.info("No unassigned tasks. Create a task or wait for one to become available.")
        return
    if not volunteers:
        st.info("No volunteers registered yet.")
        return

    task_labels = {f"{t['title']} (due {t['deadline']})": t["id"] for t in unassigned}
    selected_label = st.selectbox("Task for AI matching", options=list(task_labels.keys()))
    task_id = task_labels[selected_label]

    if st.button("Get AI recommendations", type="primary", key="admin_ai_recs"):
        with st.spinner("Running Profile Analyzer → Task Matcher → Decision Engine..."):
            try:
                recs = recommend_volunteers_for_task(task_id)
                st.session_state[f"admin_recs_{task_id}"] = recs
            except ValueError as exc:
                st.error(str(exc))

    recs = st.session_state.get(f"admin_recs_{task_id}", [])
    if not recs:
        st.caption("Recommended volunteers with rationale will appear here.")
        return

    for idx, rec in enumerate(recs):
        ai_match_card(
            rec["volunteer_name"],
            rec["reason"],
            f"{rec['priority']} · Fit {rec['fit_score']}",
            tertiary=rec.get("priority") == "High",
        )
        if st.button("Assign this volunteer", key=f"ai_assign_{task_id}_{idx}", type="primary"):
            apply_ai_assignment(
                task_id=task_id,
                volunteer_id=rec["volunteer_id"],
                reason=rec["reason"],
                priority=rec["priority"],
            )
            st.success(f"Assigned {rec['volunteer_name']} via AI recommendation.")
            st.session_state.pop(f"admin_recs_{task_id}", None)
            st.rerun()


def render_task_management() -> None:
    page_header("Task Matching", "Create tasks, run AI matching, assign volunteers, and update progress.")

    tab_create, tab_ai, tab_assign, tab_status = st.tabs(
        ["Create task", "AI matching", "Manual assign", "Update status"]
    )

    with tab_create:
        with st.form("create_task", clear_on_submit=True):
            title = st.text_input("Title *")
            description = st.text_area("Description *", height=100)
            required_skills = st.text_input("Required skills (comma-separated)")
            deadline = st.date_input("Deadline *", value=date.today())
            submitted = st.form_submit_button("Create task", type="primary")

        if submitted:
            if not title.strip() or not description.strip():
                st.error("Title and description are required.")
            else:
                task = add_task(
                    title=title,
                    description=description,
                    required_skills=parse_comma_list(required_skills),
                    deadline=deadline,
                )
                st.success(f"Task created: {task['title']}")
                st.info("Switch to the **AI matching** tab to get volunteer recommendations.")

    with tab_ai:
        render_ai_recommendations()

    with tab_assign:
        tasks = get_tasks()
        volunteers = get_volunteers()
        unassigned = [t for t in tasks if not t.get("assigned_volunteer_id")]

        if not tasks:
            st.info("Create a task first.")
        elif not volunteers:
            st.info("No volunteers available to assign.")
        elif not unassigned:
            st.info("All tasks are already assigned.")
        else:
            task_labels = {f"{t['title']} (due {t['deadline']})": t["id"] for t in unassigned}
            volunteer_labels = {f"{v['name']} ({v['email']})": v["id"] for v in volunteers}

            selected_task = st.selectbox("Task", options=list(task_labels.keys()))
            selected_volunteer = st.selectbox("Volunteer", options=list(volunteer_labels.keys()))
            priority = st.selectbox("Priority", options=list(PRIORITIES))
            reason = st.text_input("Assignment reason (optional)")

            if st.button("Assign manually", type="primary"):
                task_id = task_labels[selected_task]
                volunteer_id = volunteer_labels[selected_volunteer]
                if reason.strip():
                    apply_ai_assignment(task_id, volunteer_id, reason.strip(), priority)
                else:
                    assign_task(task_id, volunteer_id)
                st.success("Volunteer assigned.")
                st.rerun()

    with tab_status:
        tasks = get_tasks()
        assigned = [t for t in tasks if t.get("assigned_volunteer_id")]

        if not assigned:
            st.info("No assigned tasks to update.")
        else:
            task_labels = {
                f"{t['title']} — {volunteer_name(t['assigned_volunteer_id'])} "
                f"({STATUS_LABELS.get(t['status'], t['status'])})": t["id"]
                for t in assigned
            }
            selected = st.selectbox("Assigned task", options=list(task_labels.keys()))
            new_status = st.selectbox(
                "New status",
                options=list(ASSIGNMENT_STATUSES),
                format_func=lambda s: STATUS_LABELS[s],
            )

            if st.button("Update status", type="primary"):
                task_id = task_labels[selected]
                update_task_status(task_id, new_status)
                if new_status == "completed":
                    send_completion_notification(task_id)
                st.success("Status updated.")
                st.rerun()


def render_settings_admin() -> None:
    page_header("Production Settings", "Supabase, security, webhooks, and deployment checklist.")
    st.markdown(
        """
        **Deployment checklist**

        1. Run `supabase/schema.sql` in Supabase SQL Editor
        2. Set `SUPABASE_URL`, `SUPABASE_KEY`, `STORAGE_BACKEND=supabase`
        3. Migrate data: `python scripts/migrate_to_supabase.py`
        4. Set `ADMIN_PASSWORD` for admin RBAC
        5. Set `WEBHOOK_TOKEN` and run `python scripts/webhook_server.py`
        6. Deploy via Streamlit Cloud, Render, or Docker
        """
    )

    kpi_row(
        [
            {"label": "Storage", "value": storage_label(), "icon": "database"},
            {"label": "Supabase", "value": "Active" if use_supabase() else "Off", "icon": "cloud"},
            {"label": "Admin Auth", "value": "On" if admin_auth_required() else "Off", "icon": "lock"},
        ]
    )

    st.subheader("Automation endpoints")
    st.code(
        "POST /webhooks/reminders\nHeader: X-Webhook-Token: <WEBHOOK_TOKEN>",
        language="text",
    )
    st.caption("Start webhook server: `python scripts/webhook_server.py`")


def render_admin(section: str) -> None:
    if not require_admin():
        return

    if section == "Dashboard":
        render_dashboard()
    elif section == "Volunteers":
        render_volunteers_admin()
    elif section == "Task Matching":
        render_task_management()
    elif section == "Reports":
        render_reports_admin()
    elif section == "Notifications":
        render_notifications_admin()
    elif section == "AI Insights":
        render_match_history()
    elif section == "Settings":
        render_settings_admin()


def main() -> None:
    inject_theme()

    with st.sidebar:
        brand_block()

        nav_options = ["Volunteer Portal", "Admin Interface"]
        nav_index = (
            nav_options.index(st.session_state["sidebar_view"])
            if st.session_state.get("sidebar_view") in nav_options
            else 0
        )
        view = st.radio("Navigate", options=nav_options, index=nav_index, label_visibility="collapsed")
        st.session_state["sidebar_view"] = view

        if view == "Admin Interface" and is_admin_authenticated():
            st.markdown("---")
            st.caption("ADMIN MENU")
            section = st.radio(
                "Admin section",
                options=ADMIN_SECTIONS,
                key="admin_section",
                label_visibility="collapsed",
            )
            if st.button("Sign out admin", use_container_width=True):
                logout_admin()
                st.rerun()
        else:
            section = "Dashboard"

        st.markdown("---")
        if st.button("Run reminder check", use_container_width=True):
            sent = run_reminder_check()
            st.success(f"{len(sent)} notification(s) processed.")

        system_health_card(
            ai_engine.llm_configured(),
            email_service.email_configured(),
            storage_label(),
        )

    render_header()

    if view == "Volunteer Portal":
        render_volunteer_portal()
    else:
        render_admin(section)


if __name__ == "__main__":
    main()
