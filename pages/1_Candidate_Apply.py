"""Public candidate application page."""

from __future__ import annotations

import streamlit as st

from agents.screening_agent import screen_candidate
from services.candidate_service import save_screening_result, submit_application
from utils.helpers import parse_comma_list
from utils.ui.components import form_panel_header, page_header, volunteer_hero_panel
from utils.ui.logo import logo_mark_path
from utils.ui.styles import inject_theme

st.set_page_config(
    page_title="Apply — NayePankh Bulbul",
    page_icon=logo_mark_path(),
    layout="wide",
)

inject_theme()

page_header(
    "Apply to Volunteer",
    "Join NayePankh Foundation. Your application will be reviewed by our team with AI-assisted screening.",
    compact=True,
)

hero_col, form_col = st.columns([1, 1], gap="large")
with hero_col:
    with st.container(key="volunteer_hero_shell"):
        volunteer_hero_panel()

with form_col:
    with st.container(border=True, key="volunteer_form_shell", gap="small"):
        form_panel_header(
            "Candidate application",
            "Complete all fields. AI screening runs automatically after you submit.",
            shell=True,
        )
        with st.form("candidate_apply", clear_on_submit=True):
            name_col, email_col = st.columns(2, gap="medium")
            with name_col:
                name = st.text_input("Full name *", placeholder="Your full name")
            with email_col:
                email = st.text_input("Email *", placeholder="you@example.com")

            skills_col, interests_col = st.columns(2, gap="medium")
            with skills_col:
                skills = st.text_input("Skills", placeholder="Teaching, Design, Social media")
            with interests_col:
                interests = st.text_input("Interests", placeholder="Education, Environment")

            availability = st.text_area(
                "Availability *",
                placeholder="e.g. Weekends, 2–4 hours per week",
                height=80,
            )
            motivation = st.text_area(
                "Why do you want to volunteer? *",
                placeholder="Share your motivation and relevant experience.",
                height=100,
            )
            submitted = st.form_submit_button("Submit application", type="primary", use_container_width=True)

    if submitted:
        if not all([name.strip(), email.strip(), availability.strip(), motivation.strip()]):
            st.error("Please fill in all required fields (marked with *).")
        else:
            try:
                candidate = submit_application(
                    name=name,
                    email=email,
                    skills=parse_comma_list(skills),
                    interests=parse_comma_list(interests),
                    availability=availability,
                    motivation=motivation,
                )
                screening = screen_candidate(candidate)
                save_screening_result(candidate["id"], screening)
                st.success("Application submitted successfully!")
                st.markdown("#### AI screening result")
                st.metric("Fit score", f"{screening['score']}/100")
                st.write(f"**Suggested role:** {screening['suggested_role']}")
                st.write(f"**AI recommendation:** {screening['decision'].upper()}")
                st.info(screening["reasoning"])
                st.caption(
                    "An NGO admin will review your application. "
                    "If approved, you will be added to the volunteer pool."
                )
            except ValueError as exc:
                st.error(str(exc))
