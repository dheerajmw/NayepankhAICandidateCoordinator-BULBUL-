"""Global settings — organization, AI mode, notifications, data export."""

from __future__ import annotations

import streamlit as st

from core.config import APP_NAME, ORG_NAME, storage_label
from core.llm_engine import llm_configured
from utils.auth import require_admin
from utils.email_service import email_configured
from utils.ui.layout import setup_page
from utils.ui.support_pages import (
    export_database_csv_summary,
    export_database_json,
    locked_section_overlay,
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
    with st.container(key="org_config_locked"):
        section_card_header("Organization Configuration", "corporate_fare")
        with st.form("org_settings"):
            st.text_input(
                "NGO Name",
                value=st.session_state.get("np_ngo_name", ORG_NAME),
                disabled=True,
            )
            st.text_input(
                "Admin Email",
                value=st.session_state.get("np_admin_email", "admin@nayepankh.org"),
                disabled=True,
            )
            st.text_input(
                "SMTP Host",
                value="smtp.provider.com",
                placeholder="smtp.provider.com",
                disabled=True,
                help="Email delivery is configured via environment variables on the server.",
            )
            st.text_input(
                "Admin Password",
                value="••••••••••••",
                type="password",
                disabled=True,
                help="Managed securely on the server — not editable in the app.",
            )
            st.form_submit_button("Save Changes", type="primary", disabled=True)
        locked_section_overlay(
            title="Organization Configuration",
            message="NGO profile and SMTP credentials are managed via .env for now. Full in-app editing arrives in a future release.",
            badge="Coming soon",
        )

    st.markdown('<div class="np-ai-mode-card">', unsafe_allow_html=True)
    section_card_header("AI Intelligence Mode", "psychology", tone="secondary")
    mode = st.radio(
        "AI Intelligence Mode",
        options=["rule", "neural"],
        index=1 if llm_configured() else 0,
        format_func=lambda x: "Neural LLM (Bulbul-2)" if x == "neural" else "Rule-based Logic",
        help="Neural mode uses an LLM when API keys are configured on the server.",
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
    f"Storage: {storage_label()} · Email: {'Configured' if email_configured() else 'Dry-run demo mode'}"
)
