"""Mobile UI fragments aligned with Stitch Nayepankh Bulbul AI OS designs."""

from __future__ import annotations

import html

from utils.ui.render import render_html


def onboarding_mobile_chat() -> None:
    render_html(
        """
<div class="np-mob-onboarding-chat">
  <div class="np-mob-onboarding-chat-row">
    <div class="np-mob-onboarding-bot">
      <span class="material-symbols-outlined">smart_toy</span>
      <span class="np-mob-onboarding-bot-dot"></span>
    </div>
    <div class="np-mob-onboarding-bubble">
      <p>Hi there! I'm <strong>Bulbul AI</strong>. I'll help you set up your profile for high-impact volunteering. Ready to find your mission?</p>
    </div>
  </div>
</div>
"""
    )


def onboarding_step_header(step: int, title: str) -> None:
    render_html(
        f"""
<div class="np-mob-step-head">
  <span class="np-mob-step-num">{step}</span>
  <h3 class="np-mob-step-title">{html.escape(title)}</h3>
</div>
"""
    )


def onboarding_mobile_progress_bar(progress: int = 68) -> None:
    render_html(
        f"""
<div class="np-mob-onboarding-dock" aria-hidden="true">
  <div class="np-mob-onboarding-dock-inner">
    <div class="np-mob-dock-status">
      <div class="np-mob-dock-pulse-wrap">
        <span class="np-mob-dock-pulse"></span>
        <span class="np-mob-dock-dot"></span>
      </div>
      <span class="np-mob-dock-label">AI Profiling in Progress</span>
      <span class="np-mob-dock-pct">{progress}% Complete</span>
    </div>
    <div class="np-mob-dock-track">
      <div class="np-mob-dock-fill" style="width:{min(max(progress, 0), 100)}%;"></div>
    </div>
    <p class="np-mob-dock-social">Volunteers online now</p>
  </div>
</div>
"""
    )


def admin_mobile_header(*, greeting: str = "Good morning, Director") -> None:
    render_html(
        f"""
<div class="np-mob-admin-head">
  <div class="np-mob-admin-head-copy">
    <p class="np-mob-admin-greeting">{html.escape(greeting)}</p>
    <h2 class="np-mob-admin-title">Command Center</h2>
  </div>
  <span class="np-mob-live-badge">
    <span class="np-mob-live-dot"></span>
    Live AI Insights
  </span>
</div>
"""
    )


def admin_candidate_card(
    name: str,
    subtitle: str,
    *,
    score: int | None = None,
    tags: list[str] | None = None,
    highlighted: bool = False,
) -> None:
    tags = tags or []
    score_block = ""
    if score is not None:
        score_block = f"""
<div class="np-mob-candidate-score">
  <span class="np-mob-candidate-score-label">Match Score</span>
  <span class="np-mob-candidate-score-value">{score}%</span>
</div>"""
    tag_html = "".join(
        f'<span class="np-mob-candidate-tag">{html.escape(tag)}</span>' for tag in tags[:3]
    )
    glow = " np-mob-candidate-card--glow" if highlighted else ""
    render_html(
        f"""
<div class="np-mob-candidate-card{glow}">
  <div class="np-mob-candidate-top">
    <div class="np-mob-candidate-avatar">
      <span class="material-symbols-outlined">person</span>
    </div>
    <div class="np-mob-candidate-meta">
      <div class="np-mob-candidate-name-row">
        <div>
          <h4 class="np-mob-candidate-name">{html.escape(name)}</h4>
          <p class="np-mob-candidate-sub">{html.escape(subtitle)}</p>
        </div>
        {score_block}
      </div>
      <div class="np-mob-candidate-tags">{tag_html}</div>
    </div>
  </div>
</div>
"""
    )


def admin_mobile_bento(*, open_tasks: int = 0, assignable: int = 0) -> None:
    render_html(
        f"""
<div class="np-mob-admin-bento">
  <div class="np-mob-bento-card np-mob-bento-card--light">
    <span class="material-symbols-outlined">priority_high</span>
    <div>
      <h5>Priority Tasks</h5>
      <p>{open_tasks} tasks require immediate attention</p>
    </div>
  </div>
  <div class="np-mob-bento-card np-mob-bento-card--primary">
    <span class="material-symbols-outlined">insights</span>
    <div>
      <h5>Deployment</h5>
      <p>Ready to assign {assignable} volunteers to active missions.</p>
    </div>
  </div>
</div>
"""
    )


def task_mobile_status_header(*, accuracy: int = 92, matches: int = 0) -> None:
    render_html(
        f"""
<div class="np-mob-task-status">
  <div class="np-mob-task-status-scan"></div>
  <div class="np-mob-task-status-row">
    <div>
      <h2 class="np-mob-task-status-title">AI Task Assignment Complete</h2>
      <p class="np-mob-task-status-sub">Intelligent volunteer-to-task mapping finished.</p>
    </div>
    <div class="np-mob-task-accuracy">
      <span class="np-mob-task-accuracy-label">MATCH ACCURACY</span>
      <span class="np-mob-task-accuracy-value">{accuracy}%</span>
    </div>
  </div>
  <div class="np-mob-task-badges">
    <span class="np-mob-task-badge"><span class="material-symbols-outlined">bolt</span> Optimized Engine</span>
    <span class="np-mob-task-badge np-mob-task-badge--tertiary">
      <span class="material-symbols-outlined">auto_awesome</span> {matches} Matches Ready
    </span>
  </div>
</div>
"""
    )


def task_mobile_match_card(
    volunteer_name: str,
    role: str,
    task_title: str,
    reasoning: str,
    *,
    score: float | int,
    primary: bool = False,
) -> None:
    cls = "np-mob-match-card np-mob-match-card--primary" if primary else "np-mob-match-card"
    render_html(
        f"""
<article class="{cls}">
  <div class="np-mob-match-head">
    <div class="np-mob-match-person">
      <div class="np-mob-match-avatar">
        <span class="material-symbols-outlined">person</span>
      </div>
      <div>
        <h3>{html.escape(volunteer_name)}</h3>
        <span>{html.escape(role)}</span>
      </div>
    </div>
    <div class="np-mob-match-score">
      <span>MATCH SCORE</span>
      <strong>{score}%</strong>
    </div>
  </div>
  <div class="np-mob-match-task">
    <span class="material-symbols-outlined">assignment</span>
    <span>{html.escape(task_title)}</span>
  </div>
  <div class="np-mob-match-reason">
    <span class="material-symbols-outlined">psychology</span>
    <div>
      <h4>AI REASONING</h4>
      <p>{html.escape(reasoning)}</p>
    </div>
  </div>
</article>
"""
    )


def help_mobile_hero() -> None:
    render_html(
        """
<div class="np-mob-help-hero">
  <h1>How can we help?</h1>
  <p>Search our documentation or contact support.</p>
</div>
"""
    )


def help_mobile_support_cta() -> None:
    render_html(
        """
<div class="np-mob-help-cta">
  <h3>Still need help?</h3>
  <p>Our empathy-driven support team is available 24/7 to assist with your mission.</p>
  <div class="np-mob-help-cta-actions">
    <span class="np-mob-help-cta-primary"><span class="material-symbols-outlined">chat</span> Start Live Chat</span>
    <span class="np-mob-help-cta-secondary"><span class="material-symbols-outlined">mail</span> Email Support</span>
  </div>
</div>
"""
    )


def account_mobile_profile(name: str, role: str) -> None:
    render_html(
        f"""
<div class="np-mob-account-profile">
  <div class="np-mob-account-avatar-ring">
    <div class="np-mob-account-avatar">
      <span class="material-symbols-outlined">person</span>
    </div>
    <span class="np-mob-account-online"></span>
  </div>
  <h1>{html.escape(name)}</h1>
  <span class="np-mob-account-role">{html.escape(role)}</span>
</div>
"""
    )


def settings_mobile_section_title(icon: str, title: str) -> None:
    render_html(
        f"""
<div class="np-mob-settings-section-head">
  <span class="material-symbols-outlined">{html.escape(icon)}</span>
  <h3>{html.escape(title)}</h3>
</div>
"""
    )
