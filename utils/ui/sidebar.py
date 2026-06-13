"""Stitch-style shared sidebar for all screens."""

from __future__ import annotations

import html
import os
from pathlib import Path

import streamlit as st
from streamlit.errors import StreamlitPageNotFoundError
from streamlit.file_util import get_main_script_directory, normalize_path_join
from streamlit.runtime.scriptrunner_utils.script_run_context import get_script_run_ctx

from core.config import APP_NAME_SHORT, ORG_NAME
from utils.auth import is_admin_authenticated
from utils.ui.logo import logo_svg_markup
from utils.ui.render import render_html

HOME_PAGE = "home"
ONBOARDING_PAGE = "pages/1_Volunteer_Onboarding.py"
ADMIN_PAGE = "pages/2_Admin_Dashboard.py"
TASKS_PAGE = "pages/3_Task_Assignment.py"
SETTINGS_PAGE = "pages/4_Settings.py"
HELP_PAGE = "pages/5_Help_Center.py"
ACCOUNT_PAGE = "pages/6_Account.py"

# Streamlit multipage URL paths (fallback when page_link registry is incomplete).
PAGE_HREFS: dict[str, str] = {
    HOME_PAGE: "/",
    ONBOARDING_PAGE: "/Volunteer_Onboarding",
    ADMIN_PAGE: "/Admin_Dashboard",
    TASKS_PAGE: "/Task_Assignment",
    SETTINGS_PAGE: "/Settings",
    HELP_PAGE: "/Help_Center",
    ACCOUNT_PAGE: "/Account",
}

NAV_ITEMS: list[tuple[str, str, str, str]] = [
    ("overview", HOME_PAGE, "Overview", "dashboard"),
    ("onboarding", ONBOARDING_PAGE, "Volunteer Onboarding", "person_add"),
    ("admin", ADMIN_PAGE, "Volunteers", "group"),
    ("tasks", TASKS_PAGE, "Task Engine", "precision_manufacturing"),
]


def _home_script_path() -> str:
    ctx = get_script_run_ctx()
    if ctx and ctx.main_script_path:
        return Path(ctx.main_script_path).name
    return "streamlit_app.py"


def _resolve_page_path(page: str) -> str:
    if page == HOME_PAGE:
        return _home_script_path()
    return page


def _registered_page_path(page: str) -> str | None:
    """Return a script path safe for st.page_link, or None if not registered."""
    ctx = get_script_run_ctx()
    if not ctx:
        return _resolve_page_path(page)

    rel = _resolve_page_path(page)
    main_dir = get_main_script_directory(ctx.main_script_path)
    requested = os.path.realpath(normalize_path_join(main_dir, rel))

    for page_data in ctx.pages_manager.get_pages().values():
        script_path = page_data.get("script_path")
        if not script_path:
            continue
        if os.path.realpath(script_path) != requested:
            continue
        if page_data.get("page_script_hash") and "url_pathname" in page_data:
            return rel.replace("\\", "/")
    return None


def _material_icon(name: str) -> str:
    return f":material/{name}:"


def _fallback_nav_link(label: str, icon: str, href: str, *, active: bool) -> None:
    cls = "np-sidebar-link np-sidebar-link-active" if active else "np-sidebar-link"
    render_html(
        f'<a class="{cls}" href="{html.escape(href)}" target="_self">'
        f'<span class="material-symbols-outlined np-sidebar-icon">{html.escape(icon)}</span>'
        f"<span>{html.escape(label)}</span></a>"
    )


def _brand_html() -> str:
    return f"""
<div class="np-sidebar-brand">
  <div class="np-sidebar-brand-icon">
    {logo_svg_markup(size=40)}
  </div>
  <div>
    <p class="np-sidebar-brand-title">{APP_NAME_SHORT}</p>
    <p class="np-sidebar-brand-sub">by {ORG_NAME}</p>
  </div>
</div>
"""


def _render_nav_link(
    active: str,
    page_id: str,
    page: str,
    label: str,
    icon: str,
    *,
    container_key: str,
) -> None:
    with st.container(key=container_key):
        if active == page_id:
            render_html('<div class="np-nav-active-flag" aria-hidden="true"></div>')
        registered = _registered_page_path(page)
        if registered:
            try:
                st.page_link(
                    registered,
                    label=label,
                    icon=_material_icon(icon),
                    width="stretch",
                )
                return
            except StreamlitPageNotFoundError:
                pass
        _fallback_nav_link(label, icon, PAGE_HREFS.get(page, "/"), active=active == page_id)


def render_app_sidebar(active: str = "", *, show_admin_actions: bool = False) -> None:
    """Render the shared Stitch sidebar on every screen."""
    render_html(_brand_html())

    with st.container(key="np_sidebar_nav"):
        for page_id, page, label, icon in NAV_ITEMS:
            _render_nav_link(
                active,
                page_id,
                page,
                label,
                icon,
                container_key=f"np_nav_{page_id}",
            )
        _render_nav_link(
            active,
            "settings",
            SETTINGS_PAGE,
            "Settings",
            "settings",
            container_key="np_nav_settings",
        )

    with st.container(key="np_sidebar_cta"):
        tasks_registered = _registered_page_path(TASKS_PAGE)
        if tasks_registered:
            try:
                st.page_link(
                    tasks_registered,
                    label="Assign Task",
                    icon=_material_icon("add"),
                    width="stretch",
                )
            except StreamlitPageNotFoundError:
                render_html(
                    '<a class="np-sidebar-cta" href="/Task_Assignment" target="_self">'
                    '<span class="material-symbols-outlined np-sidebar-icon">add</span>'
                    "<span>Assign Task</span></a>"
                )
        else:
            render_html(
                '<a class="np-sidebar-cta" href="/Task_Assignment" target="_self">'
                '<span class="material-symbols-outlined np-sidebar-icon">add</span>'
                "<span>Assign Task</span></a>"
            )

    with st.container(key="np_sidebar_footer"):
        _render_nav_link(
            active,
            "help",
            HELP_PAGE,
            "Help Center",
            "help",
            container_key="np_nav_help",
        )
        _render_nav_link(
            active,
            "account",
            ACCOUNT_PAGE,
            "Account",
            "manage_accounts",
            container_key="np_nav_account",
        )

    if show_admin_actions and is_admin_authenticated():
        if st.button("Sign out admin", key="sidebar_signout", use_container_width=True):
            st.session_state.pop("admin_authenticated", None)
            st.rerun()
