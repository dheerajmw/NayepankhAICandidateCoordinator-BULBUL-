"""Reusable HTML fragments for the Luminous Intelligence UI."""

from __future__ import annotations

import html
import re
from typing import Literal

import streamlit as st

from core.config import APP_NAME
from utils.ui.logo import logo_svg_markup
from utils.ui.render import render_html

STATUS_CLASS = {
    "pending": "np-status-pending",
    "in_progress": "np-status-in_progress",
    "completed": "np-status-completed",
    "open": "np-status-pending",
    "assigned": "np-status-in_progress",
}


def brand_block() -> None:
    render_html(
        f"""
<div class="np-brand-block">
  <div class="np-brand-row">
    {logo_svg_markup(size=44)}
    <div class="np-brand-copy">
      <p class="np-brand-title">{APP_NAME}</p>
      <p class="np-brand-sub">Volunteer coordination OS</p>
    </div>
  </div>
</div>
"""
    )


def page_header(title: str, subtitle: str = "", *, compact: bool = False) -> None:
    sub_class = "np-page-sub np-page-sub-compact" if compact else "np-page-sub"
    sub = f'<p class="{sub_class}">{html.escape(subtitle)}</p>' if subtitle else ""
    render_html(
        f"""
<div class="np-page-header">
  <h1 class="np-page-title">{html.escape(title)}</h1>
  {sub}
</div>
"""
    )


def hero_panel(title: str, subtitle: str, badge: str = "AI OS") -> None:
    render_html(
        f"""
<div class="np-hero">
  <div class="np-hero-grid">
    <div>
      <div class="np-hero-badge">{html.escape(badge)}</div>
      <h2 class="np-hero-title">{html.escape(title)}</h2>
      <p class="np-hero-sub">{html.escape(subtitle)}</p>
    </div>
    <div class="np-hero-ai-panel">
      <div class="np-hero-ai-label">AI Engine</div>
      <div class="np-hero-ai-title">Screen · Match · Remind</div>
      <div class="np-hero-ai-sub">Structured decisions with rule-based fallbacks when no API key is set.</div>
    </div>
  </div>
</div>
"""
    )


def status_pills(items: list[tuple[str, bool]]) -> None:
    pills = []
    for label, ok in items:
        dot_color = "#22c55e" if ok else "#f59e0b"
        dot = f'<span class="np-pill-dot" style="background:{dot_color}"></span>'
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


def _score_from_meta(meta: str) -> str | None:
    match = re.search(r"(\d+)", meta)
    return match.group(1) if match else None


def ai_match_card(title: str, reason: str, meta: str, tertiary: bool = False) -> None:
    cls = "np-ai-card np-ai-card-tertiary" if tertiary else "np-ai-card"
    score = _score_from_meta(meta)
    score_html = (
        f'<div class="np-ai-score">{html.escape(score)}%</div>'
        if score is not None
        else ""
    )
    render_html(
        f"""
<div class="{cls}">
  <div class="np-ai-card-head">
    <div class="np-ai-card-title">{html.escape(title)}</div>
    <span class="np-ai-badge">Match</span>
  </div>
  {score_html}
  <p class="np-ai-reason">{html.escape(reason)}</p>
  <div class="np-ai-meta">{html.escape(meta)}</div>
</div>
"""
    )


def flow_steps(steps: list[tuple[int, str, str]]) -> None:
    parts = ['<div class="np-flow-grid">']
    for number, title, body in steps:
        parts.append(
            f"""
<div class="np-flow-step">
  <strong>Step {number}</strong>
  {html.escape(title)}<br>
  <span class="np-flow-body">{html.escape(body)}</span>
</div>
"""
        )
    parts.append("</div>")
    render_html("".join(parts))


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


def render_onboarding_background() -> None:
    """Decorative background blobs for the onboarding screen."""
    render_html(
        """
<div class="np-onboarding-bg-blob np-onboarding-bg-blob-left"></div>
<div class="np-onboarding-bg-blob np-onboarding-bg-blob-right"></div>
"""
    )


def onboarding_hero_panel(
    progress: int = 45,
    *,
    compact: bool = False,
    v2: bool = False,
    state: Literal["idle", "loading", "complete"] = "idle",
) -> None:
    if v2:
        loading = state == "loading"
        complete = state == "complete"
        hero_class = "np-onboarding-v2-hero"
        if loading:
            hero_class += " np-onboarding-v2-hero--loading"
        elif complete:
            hero_class += " np-onboarding-v2-hero--complete"

        typing_row = ""
        progress_block = ""
        if loading:
            typing_row = """
    <div class="np-onboarding-v2-typing-row">
      <div class="np-onboarding-v2-dots">
        <span></span><span></span><span></span>
      </div>
      <span class="np-onboarding-v2-typing">AI is analyzing your profile...</span>
    </div>"""
            progress_block = f"""
  <div class="np-onboarding-v2-progress-wrap">
    <div class="np-onboarding-v2-progress-head">
      <span class="np-onboarding-v2-progress-label">AI Profiling in Progress</span>
      <span class="np-onboarding-v2-progress-pct" id="np-v2-progress-text">{progress}%</span>
    </div>
    <div class="np-onboarding-v2-progress-track">
      <div class="np-onboarding-v2-progress-fill np-onboarding-v2-progress-fill--active" id="np-v2-progress-bar" style="width:{progress}%;">
        <div class="np-onboarding-v2-shimmer"></div>
      </div>
    </div>
  </div>
  <script>
    (function () {{
      var bar = document.getElementById("np-v2-progress-bar");
      var label = document.getElementById("np-v2-progress-text");
      if (!bar || !label || bar.dataset.npStarted === "1") return;
      bar.dataset.npStarted = "1";
      var value = {progress};
      window.setInterval(function () {{
        if (value >= 95) return;
        value += Math.random() * 2;
        if (value > 95) value = 95;
        bar.style.width = value + "%";
        label.textContent = Math.floor(value) + "%";
      }}, 1500);
    }})();
  </script>"""
        elif complete:
            progress_block = f"""
  <div class="np-onboarding-v2-progress-wrap">
    <div class="np-onboarding-v2-progress-head">
      <span class="np-onboarding-v2-progress-label">Profile match complete</span>
      <span class="np-onboarding-v2-progress-pct">{progress}/100</span>
    </div>
    <div class="np-onboarding-v2-progress-track">
      <div class="np-onboarding-v2-progress-fill" style="width:{progress}%;"></div>
    </div>
  </div>"""

        render_html(
            f"""
<div class="{hero_class}">
  <div class="np-onboarding-v2-hero-head">
    <div class="np-onboarding-v2-avatar-wrap">
      <div class="np-onboarding-v2-avatar">
        {logo_svg_markup(size=52)}
        <span class="np-onboarding-v2-status-dot"></span>
      </div>
    </div>
    <div>
      <h2 class="np-onboarding-v2-name">Bulbul AI</h2>
      <p class="np-onboarding-v2-role">Intelligent Assistant</p>
    </div>
  </div>
  <div class="np-onboarding-v2-chat">
    <div class="np-onboarding-v2-bubble">
      <p>Hi 👋 Welcome to {APP_NAME}! I'll help you join meaningful NGO work in under 2 minutes.</p>
    </div>{typing_row}
  </div>{progress_block}
</div>
"""
        )
        return

    if compact:
        render_html(
            f"""
<div class="np-onboarding-hero np-onboarding-hero-compact">
  <div class="np-onboarding-glow"></div>
  <div class="np-onboarding-body np-onboarding-body-compact">
    <div class="np-onboarding-compact-head">
      <div class="np-onboarding-icon np-onboarding-icon-compact">
        {logo_svg_markup(size=40)}
      </div>
      <div class="np-onboarding-compact-copy">
        <h2 class="np-onboarding-title">Welcome to {APP_NAME}!</h2>
        <p class="np-onboarding-typing">I'll help match you with the right NGO opportunities.</p>
      </div>
    </div>
    <div class="np-onboarding-progress">
      <div class="np-onboarding-progress-head">
        <span class="np-onboarding-progress-label">
          <span class="material-symbols-outlined np-spin">sync</span>
          AI Profiling
        </span>
        <span class="np-onboarding-progress-pct">{progress}%</span>
      </div>
      <div class="np-onboarding-progress-track">
        <div class="np-onboarding-progress-fill" style="width:{progress}%;"></div>
      </div>
    </div>
  </div>
</div>
"""
        )
        return

    render_html(
        f"""
<div class="np-onboarding-hero">
  <div class="np-onboarding-glow"></div>
  <div class="np-onboarding-body">
    <div class="np-onboarding-icon">
      {logo_svg_markup(size=48)}
    </div>
    <h2 class="np-onboarding-title">Welcome to {APP_NAME}!</h2>
    <p class="np-onboarding-typing">I'll help match you with the right NGO opportunities.</p>
    <div class="np-onboarding-glass">
      I'm currently analyzing our active humanitarian projects to find the perfect synergy for your profile.
    </div>
    <div class="np-onboarding-progress">
      <div class="np-onboarding-progress-head">
        <span class="np-onboarding-progress-label">
          <span class="material-symbols-outlined np-spin">sync</span>
          AI Profiling in Progress
        </span>
        <span class="np-onboarding-progress-pct">{progress}%</span>
      </div>
      <div class="np-onboarding-progress-track">
        <div class="np-onboarding-progress-fill" style="width:{progress}%;"></div>
      </div>
      <p class="np-onboarding-progress-note">Deep scanning skill clusters &amp; historical NGO impacts...</p>
    </div>
  </div>
  <div class="np-onboarding-secure">
    <span class="material-symbols-outlined">verified_user</span>
    <span>Secured by NayePankh Intelligence Engine</span>
  </div>
</div>
"""
    )


def onboarding_profile_header(*, compact: bool = False, v2: bool = False) -> None:
    if v2:
        render_html(
            """
<div class="np-onboarding-v2-form-header">
  <h1 class="np-onboarding-v2-form-title">Smart Volunteer Profile</h1>
  <p class="np-onboarding-v2-form-sub">Our intelligence engine matches your unique skills with social impact initiatives.</p>
</div>
"""
        )
        return

    if compact:
        render_html(
            """
<div class="np-onboarding-form-header np-onboarding-form-header-compact">
  <h3 class="np-onboarding-form-title">Create Your Smart Profile</h3>
</div>
"""
        )
        return
    render_html(
        """
<div class="np-onboarding-form-header">
  <h3 class="np-onboarding-form-title">Create Your Smart Profile</h3>
  <p class="np-onboarding-form-sub">Tell us more about yourself to refine your matches.</p>
</div>
"""
    )


def _normalize_tag(value: str) -> str:
    return " ".join(value.strip().split())


def _tag_exists(tags: list[str], value: str) -> bool:
    needle = value.casefold()
    return any(tag.casefold() == needle for tag in tags)


def render_preset_pills(
    state_key: str,
    label: str,
    options: list[str],
    *,
    help_text: str = "",
) -> list[str]:
    """Multi-select pill row for predefined skills/interests."""
    current = st.session_state.setdefault(state_key, [])
    valid = [item for item in current if item in options]
    if valid != current:
        st.session_state[state_key] = valid
        current = valid

    render_html(f'<p class="np-v2-field-label">{html.escape(label)}</p>')
    selected = st.pills(
        label,
        options=options,
        selection_mode="multi",
        default=current,
        key=f"preset_pills_{state_key}",
        label_visibility="collapsed",
        help=help_text or None,
    )
    if selected is not None:
        chosen = list(selected)
        if chosen != current:
            st.session_state[state_key] = chosen
            st.rerun()
    return list(st.session_state.get(state_key, []))


def render_preset_pills_with_manual(
    state_key: str,
    label: str,
    options: list[str],
    *,
    placeholder: str = "Add your own…",
    show_label: bool = True,
    help_text: str = "",
) -> list[str]:
    """Preset multi-select pills plus a manual add field (must sit outside st.form)."""
    tags: list[str] = st.session_state.setdefault(state_key, [])
    preset_selected = [item for item in tags if item in options]
    custom_tags = [item for item in tags if item not in options]

    if show_label:
        render_html(f'<p class="np-v2-field-sublabel">{html.escape(label)}</p>')

    selected = st.pills(
        label,
        options=options,
        selection_mode="multi",
        default=preset_selected,
        key=f"preset_pills_{state_key}",
        label_visibility="collapsed",
        help=help_text or None,
    )
    if selected is not None:
        preset_selected = list(selected)

    if custom_tags:
        selected_custom = st.pills(
            f"Custom {label}",
            options=custom_tags,
            selection_mode="multi",
            default=custom_tags,
            key=f"custom_pills_{state_key}",
            label_visibility="collapsed",
            help=f"Click to remove a custom {label.lower()}.",
        )
        if selected_custom is not None:
            custom_tags = list(selected_custom)

    add_label = f"Add {label.lower()}"
    with st.container(key=f"manual_row_{state_key}"):
        input_col, button_col = st.columns([5, 1], gap="small")
        with input_col:
            new_value = st.text_input(
                add_label,
                placeholder=placeholder,
                key=f"manual_{state_key}",
                label_visibility="visible",
                help=f"Type a custom {label.lower()} and click Add.",
            )
        with button_col:
            add_clicked = st.button(
                "Add",
                key=f"manual_add_{state_key}",
                type="secondary",
                use_container_width=True,
            )

    if add_clicked:
        cleaned = _normalize_tag(new_value)
        if not cleaned:
            st.caption(f"Enter a {label.lower()} before adding.")
        elif _tag_exists(preset_selected + custom_tags, cleaned):
            st.caption(f'"{cleaned}" is already selected.')
        elif cleaned in options:
            preset_selected.append(cleaned)
        else:
            custom_tags.append(cleaned)
        st.session_state.pop(f"manual_{state_key}", None)

    merged = list(dict.fromkeys(preset_selected + custom_tags))
    if merged != tags:
        st.session_state[state_key] = merged
        st.rerun()
    return merged


def render_onboarding_skills_interests(
    skills_key: str,
    interests_key: str,
    skill_options: list[str],
    interest_options: list[str],
) -> tuple[list[str], list[str]]:
    """Skills & interests picker with presets and manual entry."""
    render_html('<p class="np-v2-field-label">Skills & Interests</p>')
    render_html(
        '<p class="np-v2-field-hint">Select presets or type your own skills and interests.</p>'
    )
    skills = render_preset_pills_with_manual(
        skills_key,
        "Skills",
        skill_options,
        placeholder="Type a skill, e.g. Photography or Coding",
    )
    interests = render_preset_pills_with_manual(
        interests_key,
        "Interests",
        interest_options,
        placeholder="Type an interest, e.g. Youth empowerment",
    )
    return skills, interests


def render_tag_editor(
    state_key: str,
    label: str,
    placeholder: str,
    *,
    tone: str = "primary",
    add_label: str = "Add",
    compact: bool = False,
) -> list[str]:
    """Multi-value chip editor backed by session state (must sit outside st.form)."""
    tags: list[str] = st.session_state.setdefault(state_key, [])
    label_class = "np-field-label np-field-label-compact" if compact else "np-field-label"

    render_html(f'<p class="{label_class}">{html.escape(label)}</p>')

    if compact:
        if tags:
            with st.container(key=f"tag_pills_{state_key}"):
                selected = st.pills(
                    label,
                    options=tags,
                    selection_mode="multi",
                    default=tags,
                    key=f"pills_{state_key}",
                    label_visibility="collapsed",
                    help=f"Click a tag to remove it from your {label.lower()}.",
                )
                current = list(selected) if selected is not None else tags
                if set(current) != set(tags):
                    st.session_state[state_key] = current
                    st.rerun()

        input_col, button_col = st.columns([11, 1], gap="small")
        with input_col:
            new_value = st.text_input(
                f"New {label.lower()}",
                placeholder=placeholder,
                key=f"input_{state_key}",
                label_visibility="collapsed",
            )
        with button_col:
            add_clicked = st.button("+", key=f"add_{state_key}", use_container_width=True)
    else:
        if tags:
            chips = "".join(
                f'<span class="np-chip np-chip-{html.escape(tone)}">{html.escape(tag)}</span>'
                for tag in tags
            )
            render_html(f'<div class="np-chip-row">{chips}</div>')
            remove_cols = st.columns(min(len(tags), 6))
            for index, tag in enumerate(tags):
                with remove_cols[index % len(remove_cols)]:
                    if st.button("×", key=f"remove_{state_key}_{index}", help=f"Remove {tag}"):
                        tags.pop(index)
                        st.session_state[state_key] = tags
                        st.rerun()

        input_col, button_col = st.columns([5, 1], gap="small")
        with input_col:
            new_value = st.text_input(
                f"New {label.lower()}",
                placeholder=placeholder,
                key=f"input_{state_key}",
                label_visibility="collapsed",
            )
        with button_col:
            add_clicked = st.button(add_label, key=f"add_{state_key}", use_container_width=True)

    if add_clicked:
        cleaned = _normalize_tag(new_value)
        if not cleaned:
            if compact:
                st.caption(f"Enter a {label.lower()} before adding.")
            else:
                st.warning(f"Enter a {label.lower()} before adding.")
        elif _tag_exists(tags, cleaned):
            if compact:
                st.caption(f'"{cleaned}" is already in your {label.lower()}.')
            else:
                st.warning(f'"{cleaned}" is already in your {label.lower()}.')
        else:
            tags.append(cleaned)
            st.session_state[state_key] = tags
            st.session_state.pop(f"input_{state_key}", None)
            st.rerun()

    return tags


def volunteer_hero_panel() -> None:
    """Backward-compatible alias."""
    onboarding_hero_panel()


def form_panel_header(title: str, subtitle: str = "", *, shell: bool = False) -> None:
    sub = f'<p class="np-form-sub">{html.escape(subtitle)}</p>' if subtitle else ""
    shell_class = " np-form-header-shell" if shell else ""
    render_html(
        f'<div class="np-form-header{shell_class}">'
        f'<h3 class="np-form-title">{html.escape(title)}</h3>{sub}</div>'
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
