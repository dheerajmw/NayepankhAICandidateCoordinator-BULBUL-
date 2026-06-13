"""Shared page setup — theme, sidebar, and page config."""

from __future__ import annotations

import streamlit as st
from streamlit.runtime.scriptrunner_utils.script_run_context import get_script_run_ctx

from utils.ui.logo import logo_mark_path
from utils.ui.render import render_html
from utils.ui.sidebar import render_app_sidebar
from utils.ui.styles import inject_theme


def _ua_is_mobile() -> bool:
    try:
        headers = getattr(st.context, "headers", None)
        if headers:
            ua = headers.get("User-Agent", "")
            return any(token in ua for token in ("Mobile", "Android", "iPhone", "iPod", "IEMobile"))
    except Exception:
        pass
    return False


def _sync_mobile_flag() -> None:
    """Keep a mobile-session flag aligned with viewport (via ?np_m=) or user agent."""
    try:
        flag = st.query_params.get("np_m")
        if flag == "1":
            st.session_state.np_is_mobile = True
            return
        if flag == "0":
            st.session_state.np_is_mobile = False
            return
    except Exception:
        pass

    if "np_is_mobile" not in st.session_state:
        st.session_state.np_is_mobile = _ua_is_mobile()


def _current_page_key() -> str:
    ctx = get_script_run_ctx()
    if not ctx:
        return ""
    pm = ctx.pages_manager
    current_hash = pm.current_page_script_hash
    if current_hash:
        for page in pm.get_pages().values():
            if page.get("page_script_hash") == current_hash:
                url_path = page.get("url_pathname")
                if url_path:
                    return str(url_path)
        return current_hash
    return ctx.main_script_path or ""


def _init_sidebar_visibility() -> None:
    _sync_mobile_flag()

    page_key = _current_page_key()
    previous_key = st.session_state.get("_np_page_key")

    if previous_key and page_key and previous_key != page_key:
        # Always collapse the overlay sidebar when switching pages.
        st.session_state.np_sidebar_visible = False

    if page_key:
        st.session_state._np_page_key = page_key

    if "np_sidebar_visible" not in st.session_state:
        # Collapsed by default — mobile uses the chevron as a menu toggle.
        st.session_state.np_sidebar_visible = False


def _render_sidebar_visibility_flags() -> None:
    if st.session_state.get("np_sidebar_visible", True):
        render_html('<div class="np-sidebar-visible-flag" aria-hidden="true"></div>')
    else:
        render_html('<div class="np-sidebar-hidden-flag" aria-hidden="true"></div>')


def _render_sidebar_chevron() -> None:
    """Fixed « / » toggle — always outside the sidebar panel."""
    visible = st.session_state.get("np_sidebar_visible", True)
    label = "«" if visible else "»"
    if st.button(label, key="np_sidebar_chevron", help="Open or close navigation menu"):
        st.session_state.np_sidebar_visible = not visible
        st.rerun()


def setup_page(
    page_title: str,
    *,
    active: str,
    show_admin_actions: bool = False,
    initial_sidebar_state: str = "expanded",
) -> None:
    _init_sidebar_visibility()

    try:
        st.set_page_config(
            page_title=page_title,
            page_icon=logo_mark_path(),
            layout="wide",
            initial_sidebar_state=initial_sidebar_state,
        )
    except st.errors.StreamlitAPIException:
        pass

    inject_theme()
    with st.sidebar:
        render_app_sidebar(active, show_admin_actions=show_admin_actions)

    _render_sidebar_visibility_flags()
    _render_sidebar_chevron()


def setup_onboarding_page(page_title: str) -> None:
    """Volunteer onboarding — same sidebar « / » toggle as other screens."""
    setup_page(page_title, active="onboarding")
