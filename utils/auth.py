"""Simple admin authentication for Streamlit (Phase 5 RBAC)."""

from __future__ import annotations

import streamlit as st

from core.config import ADMIN_PASSWORD, admin_auth_required


def is_admin_authenticated() -> bool:
    return bool(st.session_state.get("admin_authenticated"))


def login_admin() -> bool:
    if not admin_auth_required():
        st.session_state["admin_authenticated"] = True
        return True

    if is_admin_authenticated():
        return True

    st.subheader("Admin sign in")
    st.caption("Admin Interface requires authentication in production.")
    password = st.text_input("Admin password", type="password", key="admin_password_input")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sign in", type="primary"):
            if password == ADMIN_PASSWORD:
                st.session_state["admin_authenticated"] = True
                st.rerun()
            st.error("Invalid admin password.")
    with col2:
        if st.button("Continue as volunteer"):
            st.session_state["sidebar_view"] = "Volunteer Portal"
            st.rerun()
    return False


def logout_admin() -> None:
    st.session_state.pop("admin_authenticated", None)


def require_admin() -> bool:
    if not admin_auth_required():
        return True
    return login_admin()
