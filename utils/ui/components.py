"""Reusable Stitch-styled UI components for Streamlit."""

from __future__ import annotations

import html

from utils.ui.logo import logo_svg_markup
from utils.ui.render import render_html

STATUS_CLASS = {
    "pending": "np-status-pending",
    "in_progress": "np-status-in_progress",
    "completed": "np-status-completed",
}


def brand_block() -> None:
    render_html(
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
"""
    )


def page_header(title: str, subtitle: str = "", *, compact: bool = False) -> None:
    sub_class = "np-page-sub np-page-sub-compact" if compact else "np-page-sub"
    sub = f'<p class="{sub_class}">{html.escape(subtitle)}</p>' if subtitle else ""
    render_html(f'<h1 class="np-page-title">{html.escape(title)}</h1>{sub}')


def status_pills(items: list[tuple[str, bool]]) -> None:
    pills = []
    for label, ok in items:
        dot = '<span class="np-pill-dot"></span>' if ok else '<span class="np-pill-dot" style="background:#f59e0b"></span>'
        pills.append(f'<span class="np-pill">{dot}{html.escape(label)}</span>')
    render_html(f'<div class="np-status-bar">{"".join(pills)}</div>')


def kpi_row(cards: list[dict]) -> None:
    parts = ['<div class="np-kpi-grid">']
    for card in cards:
        badge = ""
        if card.get("badge"):
            badge = f'<span class="np-kpi-badge">{html.escape(card["badge"])}</span>'
        icon = html.escape(card.get("icon", "analytics"))
        parts.append(
            f'<div class="np-kpi-card">{badge}'
            f'<div class="np-kpi-icon"><span class="material-symbols-outlined">{icon}</span></div>'
            f'<p class="np-kpi-label">{html.escape(card["label"])}</p>'
            f'<p class="np-kpi-value">{html.escape(str(card["value"]))}</p>'
            f"</div>"
        )
    parts.append("</div>")
    render_html("".join(parts))


def status_chip(status: str, label: str | None = None) -> str:
    cls = STATUS_CLASS.get(status, "np-status-pending")
    text = label or status.replace("_", " ")
    return f'<span class="np-status {cls}">{html.escape(text)}</span>'


def ai_match_card(title: str, reason: str, meta: str, tertiary: bool = False) -> None:
    cls = "np-ai-card np-ai-card-tertiary" if tertiary else "np-ai-card"
    render_html(
        f"""
<div class="{cls}">
  <div style="display:flex;justify-content:space-between;margin-bottom:0.5rem;">
    <strong>{html.escape(title)}</strong>
    <span style="color:#2563eb;font-size:0.875rem;font-weight:600;">{html.escape(meta)}</span>
  </div>
  <p style="margin:0;color:#434655;font-size:0.875rem;line-height:1.5;">{html.escape(reason)}</p>
</div>
"""
    )


def system_health_card(llm: bool, smtp: bool, storage: str) -> None:
    render_html(
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
"""
    )


def form_panel_header(title: str, subtitle: str = "", *, shell: bool = False) -> None:
    sub = f'<p class="np-form-sub">{html.escape(subtitle)}</p>' if subtitle else ""
    shell_class = " np-form-header-shell" if shell else ""
    render_html(
        f'<div class="np-form-header{shell_class}">'
        f'<h3 class="np-form-title">{html.escape(title)}</h3>{sub}</div>'
    )


def volunteer_hero_panel() -> None:
    render_html(
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
"""
    )


def section_card(title: str) -> None:
    render_html(
        f"""
<div class="np-card">
  <div class="np-card-header">
    <h3 class="np-card-title">{html.escape(title)}</h3>
  </div>
</div>
"""
    )
