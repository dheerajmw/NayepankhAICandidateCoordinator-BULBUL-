"""Shared page setup — theme, sidebar, and page config."""

from __future__ import annotations

import streamlit as st

from utils.ui.logo import logo_mark_path
from utils.ui.render import render_html
from utils.ui.sidebar import render_app_sidebar
from utils.ui.styles import inject_theme


def _init_sidebar_visibility() -> None:
    if "np_sidebar_visible" not in st.session_state:
        st.session_state.np_sidebar_visible = True


def _render_sidebar_visibility_flags() -> None:
    if st.session_state.get("np_sidebar_visible", True):
        render_html('<div class="np-sidebar-visible-flag" aria-hidden="true"></div>')
    else:
        render_html('<div class="np-sidebar-hidden-flag" aria-hidden="true"></div>')


def _render_sidebar_chevron() -> None:
    """Fixed « / » toggle — always outside the sidebar panel."""
    visible = st.session_state.get("np_sidebar_visible", True)
    label = "«" if visible else "»"
    if st.button(label, key="np_sidebar_chevron", help="Toggle navigation menu"):
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
