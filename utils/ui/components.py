"""Reusable Stitch-styled UI components for Streamlit."""

from __future__ import annotations

import html

import streamlit as st

from utils.ui.logo import logo_svg_markup

STATUS_CLASS = {
    "pending": "np-status-pending",
    "in_progress": "np-status-in_progress",
    "completed": "np-status-completed",
}


def brand_block() -> None:
    st.markdown(
        f"""
        <div class="np-brand-block">
            <div class="np-brand-row">
                {logo_svg_markup(size=52)}
                <div class="np-brand-copy">
                    <p class="np-brand-title">NayePankh Bulbul</p>
                    <p class="np-brand-sub">AI-Powered NGO Ops</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str = "") -> None:
    sub = f'<p class="np-page-sub">{html.escape(subtitle)}</p>' if subtitle else ""
    st.markdown(
        f'<h1 class="np-page-title">{html.escape(title)}</h1>{sub}',
        unsafe_allow_html=True,
    )


def status_pills(items: list[tuple[str, bool]]) -> None:
    pills = []
    for label, ok in items:
        dot = '<span class="np-pill-dot"></span>' if ok else '<span class="np-pill-dot" style="background:#f59e0b"></span>'
        pills.append(f'<span class="np-pill">{dot}{html.escape(label)}</span>')
    st.markdown(f'<div class="np-status-bar">{"".join(pills)}</div>', unsafe_allow_html=True)


def kpi_row(cards: list[dict]) -> None:
    parts = ['<div class="np-kpi-grid">']
    for card in cards:
        badge = ""
        if card.get("badge"):
            badge = f'<span class="np-kpi-badge">{html.escape(card["badge"])}</span>'
        parts.append(
            f"""
            <div class="np-kpi-card">
                {badge}
                <div class="np-kpi-icon"><span class="material-symbols-outlined">{html.escape(card.get("icon", "analytics"))}</span></div>
                <p class="np-kpi-label">{html.escape(card["label"])}</p>
                <p class="np-kpi-value">{html.escape(str(card["value"]))}</p>
            </div>
            """
        )
    parts.append("</div>")
    st.markdown("".join(parts), unsafe_allow_html=True)


def status_chip(status: str, label: str | None = None) -> str:
    cls = STATUS_CLASS.get(status, "np-status-pending")
    text = label or status.replace("_", " ")
    return f'<span class="np-status {cls}">{html.escape(text)}</span>'


def ai_match_card(title: str, reason: str, meta: str, tertiary: bool = False) -> None:
    cls = "np-ai-card np-ai-card-tertiary" if tertiary else "np-ai-card"
    st.markdown(
        f"""
        <div class="{cls}">
            <div style="display:flex;justify-content:space-between;margin-bottom:0.5rem;">
                <strong>{html.escape(title)}</strong>
                <span style="color:#2563eb;font-size:0.875rem;font-weight:600;">{html.escape(meta)}</span>
            </div>
            <p style="margin:0;color:#434655;font-size:0.875rem;line-height:1.5;">{html.escape(reason)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def system_health_card(llm: bool, smtp: bool, storage: str) -> None:
    st.markdown(
        f"""
        <div class="np-system-card">
            <strong style="font-size:0.875rem;">System Health</strong>
            <p style="font-size:0.75rem;opacity:0.85;margin:0.5rem 0;">
                <span class="np-pill-dot"></span> Storage: {html.escape(storage)}
            </p>
            <p style="font-size:0.75rem;opacity:0.85;margin:0.25rem 0;">
                AI Engine: {"Operational" if llm else "Rule-based mode"}
            </p>
            <p style="font-size:0.75rem;opacity:0.85;margin:0.25rem 0;">
                Email: {"SMTP active" if smtp else "Dry-run / log mode"}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def form_panel_header(title: str, subtitle: str = "") -> None:
    sub = f'<p class="np-form-sub">{html.escape(subtitle)}</p>' if subtitle else ""
    st.markdown(
        f'<div class="np-form-header"><h3 class="np-form-title">{html.escape(title)}</h3>{sub}</div>',
        unsafe_allow_html=True,
    )


def volunteer_hero_panel() -> None:
    st.markdown(
        f"""
        <div class="np-hero-panel">
            <div class="np-hero-body">
                <div class="np-hero-logo-wrap">{logo_svg_markup(size=56)}</div>
                <h2>Welcome to the Next Era of Social Impact</h2>
                <p>Our AI analyzes open NGO tasks to find your perfect mission match.
                Complete your profile to activate the NayePankh Bulbul matching engine.</p>
            </div>
            <div class="np-hero-status">
                <p class="np-hero-status-label">CURRENT STATUS</p>
                <p class="np-hero-status-value">Ready to match you with meaningful work</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_card(title: str) -> None:
    st.markdown(
        f"""
        <div class="np-card">
            <div class="np-card-header">
                <h3 class="np-card-title">{html.escape(title)}</h3>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
