"""Global settings — organization, AI mode, notifications, data export."""

from __future__ import annotations

import os

import streamlit as st

from core.config import ADMIN_PASSWORD, APP_NAME, ORG_NAME, app_env, storage_label
from core.llm_engine import llm_configured
from utils.auth import require_admin
from utils.email_service import email_configured
from utils.ui.layout import setup_page
from utils.ui.support_pages import (
    export_database_csv_summary,
    export_database_json,
    section_card_header,
    support_page_header,
    system_health_footer,
)

setup_page(f"Settings — {APP_NAME}", active="settings", show_admin_actions=True)

if not require_admin():
    st.stop()

support_page_header(
    "Global Settings",
    "Configure your organization's digital ecosystem and AI intelligence parameters.",
)

main_col, side_col = st.columns([2, 1], gap="large")

with main_col:
    with st.container():
        section_card_header("Organization Configuration", "corporate_fare")
        with st.form("org_settings"):
            ngo_name = st.text_input("NGO Name", value=st.session_state.get("np_ngo_name", ORG_NAME))
            admin_email = st.text_input(
                "Admin Email",
                value=st.session_state.get("np_admin_email", "admin@nayepankh.org"),
            )
            smtp_host = st.text_input(
                "SMTP Host",
                value=os.getenv("SMTP_HOST", ""),
                placeholder="smtp.provider.com",
                disabled=bool(os.getenv("SMTP_HOST")),
                help="Set SMTP_HOST in .env to configure email delivery.",
            )
            st.text_input(
                "Admin Password",
                value="••••••••••••" if ADMIN_PASSWORD else "",
                type="password",
                disabled=True,
                help="Configured via ADMIN_PASSWORD in .env (production only).",
            )
            if st.form_submit_button("Save Changes", type="primary"):
                st.session_state["np_ngo_name"] = ngo_name.strip()
                st.session_state["np_admin_email"] = admin_email.strip()
                st.success("Organization settings saved for this session.")

    st.markdown('<div class="np-ai-mode-card">', unsafe_allow_html=True)
    section_card_header("AI Intelligence Mode", "psychology", tone="secondary")
    mode = st.radio(
        "AI Intelligence Mode",
        options=["rule", "neural"],
        index=1 if llm_configured() else 0,
        format_func=lambda x: "Neural LLM (Bulbul-2)" if x == "neural" else "Rule-based Logic",
        help="Neural mode requires OPENAI_API_KEY or GEMINI_API_KEY in .env.",
        label_visibility="collapsed",
    )
    if mode == "neural" and not llm_configured():
        st.warning("Neural mode selected but no LLM API key is configured — agents use rule-based fallbacks.")
    elif mode == "rule":
        st.caption("Deterministic outcomes, lower latency, ideal for basic task routing.")
    else:
        st.caption("Generative insights, complex matching, and predictive volunteer analysis.")
    st.markdown("</div>", unsafe_allow_html=True)

with side_col:
    section_card_header("Theme Visuals", "palette", tone="primary")
    theme = st.radio(
        "Theme",
        ["Light Mode", "Dark Mode", "System Default"],
        index=["Light Mode", "Dark Mode", "System Default"].index(
            st.session_state.get("np_theme", "Light Mode")
        ),
        label_visibility="collapsed",
    )
    st.session_state["np_theme"] = theme
    st.caption("Theme preference is stored for this session (full dark mode coming soon).")

    st.markdown("---")
    section_card_header("Alerts & Notifications", "notifications", tone="primary")
    st.toggle("Volunteer Onboarding", value=True, help="Notify when a new volunteer joins")
    st.toggle("Task Completion", value=True, help="Daily digest of finished milestones")
    st.toggle("AI Model Updates", value=False, help="Alert on model performance shifts")

    st.markdown("---")
    section_card_header("Data Management", "database", tone="primary")
    st.caption("Export organizational data for auditing or backups.")
    st.download_button(
        "Export as Bulk CSV",
        data=export_database_csv_summary(),
        file_name="nayepankh_export_summary.csv",
        mime="text/csv",
        use_container_width=True,
    )
    st.download_button(
        "Export as JSON Schema",
        data=export_database_json(),
        file_name="nayepankh_export.json",
        mime="application/json",
        use_container_width=True,
    )

system_health_footer()
st.caption(
    f"Storage: {storage_label()} · Email: {'SMTP active' if email_configured() else 'Dry-run'} · Env: {app_env()}"
)
