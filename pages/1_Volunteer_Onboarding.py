"""Volunteer onboarding — public application and AI screening."""

from __future__ import annotations

import streamlit as st

from agents.screening_agent import screen_candidate
from services.candidate_service import save_screening_result, submit_application
from utils.ui.components import (
    onboarding_hero_panel,
    onboarding_profile_header,
    render_onboarding_background,
    render_onboarding_skills_interests,
)
from core.config import APP_NAME
from utils.ui.layout import setup_onboarding_page
from utils.ui.mobile_stitch import (
    onboarding_mobile_chat,
    onboarding_mobile_progress_bar,
    onboarding_step_header,
)
from utils.ui.render import render_html

setup_onboarding_page(f"Volunteer Onboarding — {APP_NAME}")

SKILLS_KEY = "onboarding_skills"
INTERESTS_KEY = "onboarding_interests"
SCREENING_PHASE_KEY = "np_screening_phase"
SCREENING_PAYLOAD_KEY = "np_screening_payload"
SCREENING_RESULT_KEY = "np_screening_result"
SCREENING_WORK_KEY = "np_screening_work_started"

SKILL_OPTIONS = [
    "Teaching",
    "Design",
    "Social Media",
    "Fundraising",
    "Research",
    "Data Analysis",
]

INTEREST_OPTIONS = [
    "Climate Action",
    "Education",
    "Community Health",
    "Poverty Alleviation",
]

AVAILABILITY_OPTIONS = {
    "Weekdays": "Weekdays (2-4 hrs/day)",
    "Weekends": "Weekends (flex hours)",
    "Flexible": "Flexible / on-call",
}


def _format_availability(selected: list[str]) -> str:
    parts = [AVAILABILITY_OPTIONS[label] for label in selected if label in AVAILABILITY_OPTIONS]
    return "; ".join(parts)


def _reset_profile() -> None:
    st.session_state[SKILLS_KEY] = []
    st.session_state[INTERESTS_KEY] = []
    for key in ("onboarding_name", "onboarding_email", "onboarding_phone"):
        st.session_state.pop(key, None)


def _clear_screening_state() -> None:
    for key in (
        SCREENING_PHASE_KEY,
        SCREENING_PAYLOAD_KEY,
        SCREENING_RESULT_KEY,
        SCREENING_WORK_KEY,
    ):
        st.session_state.pop(key, None)


def _run_screening(payload: dict) -> None:
    candidate = submit_application(
        name=payload["name"],
        email=payload["email"],
        skills=payload["skills"],
        interests=payload["interests"],
        availability=payload["availability"],
        motivation=payload["motivation"],
    )
    screening = screen_candidate(candidate)
    save_screening_result(candidate["id"], screening)
    st.session_state[SCREENING_RESULT_KEY] = {
        "candidate": candidate,
        "screening": screening,
    }
    st.session_state[SCREENING_PHASE_KEY] = "done"
    _reset_profile()
    for key in (SCREENING_PAYLOAD_KEY, SCREENING_WORK_KEY):
        st.session_state.pop(key, None)


screening_phase = st.session_state.get(SCREENING_PHASE_KEY)
screening_result = st.session_state.get(SCREENING_RESULT_KEY)

if screening_phase == "running" and st.session_state.get(SCREENING_WORK_KEY):
    payload = st.session_state.get(SCREENING_PAYLOAD_KEY)
    if payload:
        try:
            _run_screening(payload)
        except ValueError as exc:
            st.session_state["np_screening_error"] = str(exc)
            _clear_screening_state()
        st.rerun()

def _mobile_onboarding_layout() -> bool:
    try:
        if st.query_params.get("np_m") == "1":
            return True
        if st.query_params.get("np_m") == "0":
            return False
    except Exception:
        pass
    return bool(st.session_state.get("np_is_mobile", False))


is_mobile = _mobile_onboarding_layout()
show_idle_mobile_chat = screening_phase not in ("running", "done")

with st.container(key="onboarding_page"):
    if not is_mobile:
        render_onboarding_background()

    if screening_phase == "running":
        hero_state = "loading"
        hero_progress = 45
    elif screening_phase == "done" and screening_result:
        hero_state = "complete"
        hero_progress = min(int(screening_result["screening"].get("score", 0)), 95)
    else:
        hero_state = "idle"
        hero_progress = 45

    if not is_mobile:
        with st.container(key="volunteer_hero_shell"):
            onboarding_hero_panel(progress=hero_progress, v2=True, state=hero_state)

    if show_idle_mobile_chat:
        with st.container(key="onboarding_mobile_chat"):
            onboarding_mobile_chat()

    with st.container(key="volunteer_form_shell"):
        screening_error = st.session_state.pop("np_screening_error", None)
        if screening_error:
            st.error(screening_error)

        if screening_phase == "done" and screening_result:
            screening = screening_result["screening"]
            score = int(screening.get("score", 0))
            render_html(
                f"""
<div class="np-screening-card np-onboarding-v2-success">
  <h4 class="np-onboarding-v2-form-title">Profile submitted</h4>
  <p class="np-onboarding-v2-form-sub">AI screening completed — an NGO admin will review your application.</p>
  <div class="np-onboarding-v2-progress-wrap" style="margin-top:0.75rem;">
    <div class="np-onboarding-v2-progress-head">
      <span class="np-onboarding-v2-progress-label">Fit score</span>
      <span class="np-onboarding-v2-progress-pct">{score}/100</span>
    </div>
    <div class="np-onboarding-v2-progress-track">
      <div class="np-onboarding-v2-progress-fill" style="width:{score}%;"></div>
    </div>
  </div>
  <p class="np-v2-success-meta">
    <strong>Suggested role:</strong> {screening.get("suggested_role", "—")} ·
    <strong>Recommendation:</strong> {str(screening.get("decision", "—")).upper()}
  </p>
</div>
"""
            )
            if st.button("Submit another application", type="secondary"):
                _clear_screening_state()
                st.rerun()
        elif screening_phase == "running":
            onboarding_profile_header(v2=True)
            render_html(
                """
<div class="np-screening-card np-onboarding-v2-success">
  <h4 class="np-onboarding-v2-form-title">Screening in progress</h4>
  <p class="np-onboarding-v2-form-sub">Bulbul AI is reviewing your profile. This usually takes a few seconds.</p>
</div>
"""
            )
        else:
            with st.container(key="volunteer_form_card"):
                onboarding_profile_header(v2=True)
                render_onboarding_skills_interests(
                    SKILLS_KEY,
                    INTERESTS_KEY,
                    SKILL_OPTIONS,
                    INTEREST_OPTIONS,
                )

                with st.form("volunteer_onboarding", clear_on_submit=True):
                    onboarding_step_header(1, "Basics")
                    name_col, email_col = st.columns(2, gap="medium")
                    with name_col:
                        name = st.text_input("Full Name", placeholder="e.g. Alex Rivera", key="onboarding_name")
                    with email_col:
                        email = st.text_input("Email Address", placeholder="alex@impact.org", key="onboarding_email")

                    phone = st.text_input(
                        "Phone Number",
                        placeholder="+1 (555) 000-0000",
                        key="onboarding_phone",
                    )

                    onboarding_step_header(3, "Availability")
                    st.markdown(
                        '<p class="np-v2-field-label np-v2-field-label--sr">Availability</p>',
                        unsafe_allow_html=True,
                    )
                    with st.container(key="availability_cards", horizontal=True, gap=None):
                        weekdays = st.checkbox("Weekdays", key="avail_weekdays")
                        weekends = st.checkbox("Weekends", key="avail_weekends")
                        flexible = st.checkbox("Flexible", key="avail_flexible")

                    onboarding_step_header(4, "Motivation")
                    motivation = st.text_area(
                        "Motivation",
                        placeholder="What drives you to make a change?",
                        height=56,
                    )

                    render_html(
                        """
<div class="np-v2-form-footer">
  <div class="np-v2-form-footer-copy">
    <span class="np-v2-form-footer-sub">Ready for the intelligence match?</span>
    <span class="np-v2-form-footer-highlight">Matched with real NGO opportunities.</span>
  </div>
</div>
"""
                    )
                    submitted = st.form_submit_button(
                        "Start AI Screening →",
                        type="primary",
                        use_container_width=True,
                    )

            onboarding_mobile_progress_bar(68)

            if submitted:
                skills = list(st.session_state.get(SKILLS_KEY, []))
                interests = list(st.session_state.get(INTERESTS_KEY, []))

                selected_slots = [
                    label
                    for label, checked in {
                        "Weekdays": weekdays,
                        "Weekends": weekends,
                        "Flexible": flexible,
                    }.items()
                    if checked
                ]
                availability = _format_availability(selected_slots)
                if phone.strip():
                    availability = f"{availability}; Phone: {phone.strip()}"

                if not all([name.strip(), email.strip(), motivation.strip(), selected_slots]):
                    st.error("Please complete name, email, at least one availability option, and motivation.")
                elif not skills and not interests:
                    st.error("Please select or add at least one skill or interest.")
                else:
                    st.session_state[SCREENING_PAYLOAD_KEY] = {
                        "name": name.strip(),
                        "email": email.strip(),
                        "skills": skills or ["General"],
                        "interests": interests or ["Community Impact"],
                        "availability": availability,
                        "motivation": motivation.strip(),
                    }
                    st.session_state[SCREENING_PHASE_KEY] = "running"
                    st.session_state.pop(SCREENING_RESULT_KEY, None)
                    st.session_state.pop(SCREENING_WORK_KEY, None)
                    st.rerun()

if screening_phase == "running" and st.session_state.get(SCREENING_PAYLOAD_KEY):
    if not st.session_state.get(SCREENING_WORK_KEY):
        st.session_state[SCREENING_WORK_KEY] = True
        st.rerun()
