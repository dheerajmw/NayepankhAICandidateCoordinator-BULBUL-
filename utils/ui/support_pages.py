"""Shared UI blocks for Settings, Help Center, and Account pages."""

from __future__ import annotations

import html
import json
from pathlib import Path

from core.config import APP_NAME

from utils.ui.render import render_html

ROOT = Path(__file__).resolve().parents[2]
DATABASE_DIR = ROOT / "database"


def support_page_header(title: str, subtitle: str = "") -> None:
    sub = (
        f'<p class="np-support-sub">{html.escape(subtitle)}</p>'
        if subtitle
        else ""
    )
    render_html(
        f"""
<div class="np-support-header">
  <h1 class="np-support-title">{html.escape(title)}</h1>
  {sub}
</div>
"""
    )


def section_card_header(title: str, icon: str, *, tone: str = "primary") -> None:
    render_html(
        f"""
<div class="np-section-card-head">
  <div class="np-section-icon np-section-icon-{html.escape(tone)}">
    <span class="material-symbols-outlined">{html.escape(icon)}</span>
  </div>
  <h3 class="np-section-card-title">{html.escape(title)}</h3>
</div>
"""
    )


def system_health_footer(*, latency_ms: int = 42, region: str = "Mumbai-South-1") -> None:
    render_html(
        f"""
<div class="np-system-health-bar">
  <div class="np-system-health-left">
    <span class="material-symbols-outlined np-system-health-icon">analytics</span>
    <div>
      <h4 class="np-system-health-title">System Latency: {latency_ms}ms</h4>
      <p class="np-system-health-sub">All AI nodes operating at peak efficiency. Regional server: {html.escape(region)}</p>
    </div>
  </div>
  <span class="np-system-health-link">View Live Logs</span>
</div>
"""
    )


def help_hero() -> None:
    render_html(
        """
<div class="np-help-hero">
  <div class="np-help-hero-glow"></div>
  <div class="np-help-hero-inner">
    <h1 class="np-help-hero-title">How can Bulbul help you today?</h1>
    <p class="np-help-hero-sub">Search our documentation for AI task matching, volunteer coordination, or platform settings.</p>
  </div>
</div>
"""
    )


def help_category_grid() -> None:
    render_html(
        f"""
<div class="np-help-bento">
  <div class="np-glass-card np-help-card">
    <div class="np-help-card-icon np-help-card-icon-primary"><span class="material-symbols-outlined">rocket_launch</span></div>
    <h3>Getting Started</h3>
    <p>Learn the basics of {APP_NAME} and set up your organization in minutes.</p>
    <ul>
      <li>Platform Tour</li>
      <li>Setting Up Workflows</li>
      <li>Role Management</li>
    </ul>
  </div>
  <div class="np-glass-card np-help-card">
    <div class="np-help-card-icon np-help-card-icon-secondary"><span class="material-symbols-outlined">neurology</span></div>
    <h3>AI Task Matching</h3>
    <p>Optimize impact with automated task distribution and skill verification.</p>
    <ul>
      <li>Understanding the Algorithm</li>
      <li>Skill Mapping Guide</li>
      <li>Impact Reporting</li>
    </ul>
  </div>
  <div class="np-glass-card np-help-card">
    <div class="np-help-card-icon np-help-card-icon-tertiary"><span class="material-symbols-outlined">diversity_3</span></div>
    <h3>Volunteer Mgmt</h3>
    <p>Keep your community engaged with dashboards and communication tools.</p>
    <ul>
      <li>Onboarding Flows</li>
      <li>Engagement Analytics</li>
      <li>Reward Systems</li>
    </ul>
  </div>
</div>
"""
    )


def help_support_panel() -> None:
    render_html(
        """
<div class="np-glass-card np-help-support">
  <h3 class="np-section-card-title">Need more help?</h3>
  <p class="np-support-sub">Our dedicated support team is available 24/7 for NGO leaders.</p>
  <p class="np-help-online"><span class="np-help-dot"></span> Team is online</p>
  <p class="np-help-contact">support@nayepankh.org · docs in <code>README.md</code></p>
</div>
<div class="np-glass-card np-help-links">
  <h3 class="np-section-card-title">Quick Links</h3>
  <ul class="np-help-link-list">
    <li><span class="material-symbols-outlined">description</span> API Documentation</li>
    <li><span class="material-symbols-outlined">terminal</span> Developer SDKs</li>
    <li><span class="material-symbols-outlined">play_circle</span> Video Tutorials</li>
    <li><span class="material-symbols-outlined">history_edu</span> Change Log</li>
  </ul>
</div>
"""
    )


def account_profile_header(name: str, role: str, email: str, phone: str, joined: str) -> None:
    render_html(
        f"""
<div class="np-glass-card np-account-profile">
  <div class="np-account-profile-row">
    <div class="np-account-avatar">
      <span class="material-symbols-outlined">person</span>
    </div>
    <div class="np-account-profile-copy">
      <h2>{html.escape(name)}</h2>
      <div class="np-account-badges">
        <span class="np-account-badge np-account-badge-primary">
          <span class="material-symbols-outlined">verified_user</span>{html.escape(role)}
        </span>
        <span class="np-account-badge">Joined {html.escape(joined)}</span>
      </div>
      <div class="np-account-meta-grid">
        <div class="np-account-meta"><p class="np-meta-label">Email Address</p><p>{html.escape(email)}</p></div>
        <div class="np-account-meta"><p class="np-meta-label">Contact Number</p><p>{html.escape(phone)}</p></div>
      </div>
    </div>
  </div>
</div>
"""
    )


def account_sessions_panel() -> None:
    render_html(
        """
<div class="np-glass-card np-account-sessions">
  <div class="np-section-card-head">
    <div class="np-section-icon np-section-icon-primary"><span class="material-symbols-outlined">devices</span></div>
    <h3 class="np-section-card-title">Active Sessions</h3>
  </div>
  <div class="np-session np-session-current">
    <div class="np-session-row">
      <span class="material-symbols-outlined">laptop_mac</span>
      <div>
        <p class="np-session-title">MacBook Pro <span class="np-session-tag">Current</span></p>
        <p class="np-session-sub">Mumbai, India · Chrome Browser</p>
      </div>
    </div>
  </div>
  <div class="np-session">
    <div class="np-session-row">
      <span class="material-symbols-outlined">smartphone</span>
      <div>
        <p class="np-session-title">iPhone · Bulbul App</p>
        <p class="np-session-sub">New Delhi, India</p>
      </div>
    </div>
  </div>
</div>
"""
    )


def account_danger_zone() -> None:
    render_html(
        """
<div class="np-account-danger">
  <div>
    <h4><span class="material-symbols-outlined">warning</span> Danger Zone</h4>
    <p>Account deletion is disabled in this MVP. Contact your NGO admin for access changes.</p>
  </div>
</div>
"""
    )


def export_database_json() -> str:
    payload = {}
    for path in sorted(DATABASE_DIR.glob("*.json")):
        payload[path.stem] = json.loads(path.read_text(encoding="utf-8"))
    return json.dumps(payload, indent=2)


def export_database_csv_summary() -> str:
    lines = ["entity,count"]
    for path in sorted(DATABASE_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        count = len(data) if isinstance(data, list) else 1
        lines.append(f"{path.stem},{count}")
    return "\n".join(lines)
