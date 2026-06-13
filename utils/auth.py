"""Simple admin authentication for Streamlit (Phase 5 RBAC)."""

from __future__ import annotations

import streamlit as st

from core.config import ADMIN_PASSWORD, admin_auth_required

APPLY_PAGE = "pages/1_Volunteer_Onboarding.py"


def is_admin_authenticated() -> bool:
    return bool(st.session_state.get("admin_authenticated"))


def login_admin() -> bool:
    if not admin_auth_required():
        st.session_state["admin_authenticated"] = True
        return True

    if is_admin_authenticated():
        return True

    st.subheader("Admin sign in")
    st.caption("Enter the admin password to manage volunteers and tasks.")
    with st.form("admin_sign_in", clear_on_submit=False):
        password = st.text_input("Admin password", type="password")
        col1, col2 = st.columns(2)
        with col1:
            submitted = st.form_submit_button("Sign in", type="primary", use_container_width=True)
        with col2:
            volunteer = st.form_submit_button("Continue as volunteer", use_container_width=True)

    if volunteer:
        st.switch_page(APPLY_PAGE)

    if submitted:
        if password == ADMIN_PASSWORD:
            st.session_state["admin_authenticated"] = True
            st.rerun()
        st.error("Invalid admin password.")

    return False


def logout_admin() -> None:
    st.session_state.pop("admin_authenticated", None)


def require_admin() -> bool:
    if not admin_auth_required():
        return True
    return login_admin()
