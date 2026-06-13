"""Stitch-style shared sidebar for all screens."""

from __future__ import annotations

import html

import streamlit as st

from core.config import APP_NAME_SHORT, ORG_NAME
from utils.auth import is_admin_authenticated
from utils.ui.logo import logo_svg_markup
from utils.ui.render import render_html

HOME_PATH = "/"
ONBOARDING_PATH = "/Volunteer_Onboarding"
ADMIN_PATH = "/Admin_Dashboard"
TASKS_PATH = "/Task_Assignment"
SETTINGS_PATH = "/Settings"
HELP_PATH = "/Help_Center"
ACCOUNT_PATH = "/Account"

NAV_ITEMS: list[tuple[str, str, str, str]] = [
    ("overview", HOME_PATH, "Overview", "dashboard"),
    ("onboarding", ONBOARDING_PATH, "Volunteer Onboarding", "person_add"),
    ("admin", ADMIN_PATH, "Volunteers", "group"),
    ("tasks", TASKS_PATH, "Task Engine", "precision_manufacturing"),
]


def _nav_link(active: str, page_id: str, href: str, label: str, icon: str) -> str:
    cls = "np-sidebar-link np-sidebar-link-active" if active == page_id else "np-sidebar-link"
    return (
        f'<a class="{cls}" href="{html.escape(href)}" target="_self">'
        f'<span class="material-symbols-outlined np-sidebar-icon">{html.escape(icon)}</span>'
        f"<span>{html.escape(label)}</span></a>"
    )


def _footer_link(active: str, page_id: str, href: str, label: str, icon: str) -> str:
    cls = "np-sidebar-footer-link np-sidebar-link-active" if active == page_id else "np-sidebar-footer-link"
    return (
        f'<a class="{cls}" href="{html.escape(href)}" target="_self">'
        f'<span class="material-symbols-outlined np-sidebar-icon">{html.escape(icon)}</span>'
        f"<span>{html.escape(label)}</span></a>"
    )


def sidebar_html(active: str) -> str:
    nav = "".join(_nav_link(active, pid, href, label, icon) for pid, href, label, icon in NAV_ITEMS)
    return f"""
<div class="np-sidebar-shell">
  <div class="np-sidebar-brand">
    <div class="np-sidebar-brand-icon">
      {logo_svg_markup(size=40)}
    </div>
    <div>
      <p class="np-sidebar-brand-title">{APP_NAME_SHORT}</p>
      <p class="np-sidebar-brand-sub">by {ORG_NAME}</p>
    </div>
  </div>
  <nav class="np-sidebar-nav" aria-label="Main navigation">
    {nav}
    {_nav_link(active, "settings", SETTINGS_PATH, "Settings", "settings")}
  </nav>
  <a class="np-sidebar-cta" href="{html.escape(TASKS_PATH)}" target="_self">
    <span class="material-symbols-outlined np-sidebar-icon">add</span>
    <span>Assign Task</span>
  </a>
  <div class="np-sidebar-footer">
    {_footer_link(active, "help", HELP_PATH, "Help Center", "help")}
    {_footer_link(active, "account", ACCOUNT_PATH, "Account", "manage_accounts")}
  </div>
</div>
"""


def render_app_sidebar(active: str = "", *, show_admin_actions: bool = False) -> None:
    """Render the shared Stitch sidebar on every screen."""
    render_html(sidebar_html(active))

    if show_admin_actions and is_admin_authenticated():
        if st.button("Sign out admin", key="sidebar_signout", use_container_width=True):
            st.session_state.pop("admin_authenticated", None)
            st.rerun()
