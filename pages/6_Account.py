"""Account settings — profile, security, and sessions."""

from __future__ import annotations

import streamlit as st

from core.config import APP_NAME
from utils.auth import is_admin_authenticated, require_admin
from utils.ui.layout import setup_page
from utils.ui.support_pages import (
    account_danger_zone,
    account_profile_header,
    account_sessions_panel,
    section_card_header,
    support_page_header,
)

setup_page(f"Account — {APP_NAME}", active="account", show_admin_actions=True)

support_page_header(
    "Account Settings",
    "Manage your identity, security credentials, and active sessions.",
)

if is_admin_authenticated():
    name = st.session_state.get("np_account_name", "Aditi Sharma")
    email = st.session_state.get("np_admin_email", "admin@nayepankh.org")
    role = "Senior Admin"
else:
    name = st.session_state.get("np_account_name", "Volunteer User")
    email = st.session_state.get("np_account_email", "volunteer@example.com")
    role = "Volunteer"

phone = st.session_state.get("np_account_phone", "+91 98765-43210")
joined = st.session_state.get("np_account_joined", "Oct 2023")

account_profile_header(name, role, email, phone, joined)

with st.form("profile_update"):
    c1, c2 = st.columns(2)
    with c1:
        new_name = st.text_input("Display name", value=name)
    with c2:
        new_phone = st.text_input("Contact number", value=phone)
    if st.form_submit_button("Update Profile", type="primary"):
        st.session_state["np_account_name"] = new_name.strip()
        st.session_state["np_account_phone"] = new_phone.strip()
        st.success("Profile updated for this session.")
        st.rerun()

sec_col, sess_col = st.columns(2, gap="large")

with sec_col:
    st.markdown('<div class="np-glass-card np-account-security">', unsafe_allow_html=True)
    section_card_header("Security Settings", "security", tone="secondary")
    st.markdown("Password changes are managed by your platform administrator.")
    st.toggle(
        "Two-Factor Auth",
        value=st.session_state.get("np_2fa", True),
        key="np_2fa_toggle",
    )
    st.session_state["np_2fa"] = st.session_state.get("np_2fa_toggle", True)
    st.info("Use a mobile authenticator app for the highest level of account security.")
    st.markdown("</div>", unsafe_allow_html=True)

with sess_col:
    account_sessions_panel()

account_danger_zone()

st.markdown("---")
if is_admin_authenticated():
    if st.button("Sign out of all sessions", type="secondary"):
        st.session_state.pop("admin_authenticated", None)
        st.success("Signed out.")
        st.rerun()
else:
    st.caption("Sign in as admin from Volunteers or Task Engine to manage NGO operations.")
    if st.button("Go to admin sign in"):
        require_admin()
