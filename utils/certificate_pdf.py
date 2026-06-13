"""PDF certificate generation for volunteer milestones."""

from __future__ import annotations

import io
from datetime import date
from typing import Any

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from core.config import APP_NAME, ORG_NAME


def generate_certificate_pdf(volunteer: dict[str, Any], metrics: dict[str, Any]) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4),
        rightMargin=48,
        leftMargin=48,
        topMargin=48,
        bottomMargin=48,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "CertTitle",
        parent=styles["Title"],
        fontSize=28,
        textColor=colors.HexColor("#1a5276"),
        spaceAfter=12,
    )
    subtitle_style = ParagraphStyle(
        "CertSubtitle",
        parent=styles["Normal"],
        fontSize=14,
        textColor=colors.HexColor("#566573"),
        alignment=1,
        spaceAfter=24,
    )
    name_style = ParagraphStyle(
        "CertName",
        parent=styles["Title"],
        fontSize=32,
        textColor=colors.HexColor("#117a65"),
        alignment=1,
        spaceAfter=16,
    )
    body_style = ParagraphStyle(
        "CertBody",
        parent=styles["Normal"],
        fontSize=13,
        alignment=1,
        leading=18,
        spaceAfter=12,
    )
    footer_style = ParagraphStyle(
        "CertFooter",
        parent=styles["Normal"],
        fontSize=11,
        textColor=colors.HexColor("#7f8c8d"),
        alignment=1,
    )

    completed = metrics.get("tasks_completed", 0)
    skills = metrics.get("skills_utilized", [])
    skill_text = ", ".join(skills) if skills else "community service"

    story = [
        Paragraph("Certificate of Appreciation", title_style),
        Paragraph(f"{APP_NAME} · {ORG_NAME}", subtitle_style),
        Spacer(1, 0.2 * inch),
        Paragraph("This is to certify that", body_style),
        Paragraph(volunteer["name"], name_style),
        Paragraph(
            f"has successfully contributed to {ORG_NAME} by completing "
            f"<b>{completed}</b> volunteer task(s), applying skills in "
            f"<b>{skill_text}</b>.",
            body_style,
        ),
        Paragraph(
            "We recognize their dedication, impact, and commitment to our mission.",
            body_style,
        ),
        Spacer(1, 0.4 * inch),
        Paragraph(f"Issued on {date.today().isoformat()}", footer_style),
        Paragraph(f"{ORG_NAME} — Volunteer Program", footer_style),
    ]

    doc.build(story)
    return buffer.getvalue()
