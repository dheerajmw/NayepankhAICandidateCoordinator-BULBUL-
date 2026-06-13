"""Export contribution reports to CSV and text PDF."""

from __future__ import annotations

import csv
import io
from typing import Any

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer


def export_report_csv(report: dict[str, Any]) -> bytes:
    output = io.StringIO()
    metrics = report.get("metrics", {})
    writer = csv.writer(output)

    writer.writerow(["Report type", report.get("report_type")])
    writer.writerow(["Volunteer", report.get("volunteer_name") or "All volunteers"])
    writer.writerow(["Period start", report.get("period_start") or "All time"])
    writer.writerow(["Period end", report.get("period_end") or "All time"])
    writer.writerow([])
    writer.writerow(["Narrative", report.get("narrative", "")])
    writer.writerow([])
    writer.writerow(["Metric", "Value"])

    if report.get("report_type") == "volunteer_summary":
        writer.writerow(["Tasks total", metrics.get("tasks_total")])
        writer.writerow(["Tasks completed", metrics.get("tasks_completed")])
        writer.writerow(["Tasks in progress", metrics.get("tasks_in_progress")])
        writer.writerow(["Completion rate %", metrics.get("completion_rate")])
        writer.writerow(["Skills utilized", ", ".join(metrics.get("skills_utilized", []))])
        writer.writerow([])
        writer.writerow(["Task", "Status", "Deadline", "Skills"])
        for task in metrics.get("task_history", []):
            writer.writerow(
                [
                    task.get("title"),
                    task.get("status"),
                    task.get("deadline"),
                    ", ".join(task.get("skills", [])),
                ]
            )
    else:
        writer.writerow(["Volunteers", metrics.get("volunteer_count")])
        writer.writerow(["Tasks total", metrics.get("tasks_total")])
        writer.writerow(["Tasks completed", metrics.get("tasks_completed")])
        writer.writerow(["Completion rate %", metrics.get("completion_rate")])
        writer.writerow(["Skills utilized", ", ".join(metrics.get("skills_utilized", []))])
        writer.writerow([])
        writer.writerow(["Volunteer", "Completed", "Total", "Completion rate %"])
        for summary in metrics.get("volunteer_summaries", []):
            writer.writerow(
                [
                    summary.get("volunteer_name"),
                    summary.get("tasks_completed"),
                    summary.get("tasks_total"),
                    summary.get("completion_rate"),
                ]
            )

    return output.getvalue().encode("utf-8")


def export_report_pdf(report: dict[str, Any]) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=48, leftMargin=48, topMargin=48, bottomMargin=48)
    styles = getSampleStyleSheet()
    story = []

    title = "Volunteer Contribution Summary" if report.get("report_type") == "volunteer_summary" else "Admin Contribution Report"
    story.append(Paragraph(f"<b>{title}</b>", styles["Title"]))
    story.append(Spacer(1, 12))

    if report.get("volunteer_name"):
        story.append(Paragraph(f"<b>Volunteer:</b> {report['volunteer_name']}", styles["Normal"]))
    period = f"{report.get('period_start') or 'All time'} → {report.get('period_end') or 'Present'}"
    story.append(Paragraph(f"<b>Period:</b> {period}", styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"<b>Summary</b>", styles["Heading2"]))
    story.append(Paragraph(report.get("narrative", ""), styles["Normal"]))
    story.append(Spacer(1, 12))

    highlights = report.get("highlights", [])
    if highlights:
        story.append(Paragraph("<b>Highlights</b>", styles["Heading2"]))
        items = [ListItem(Paragraph(h, styles["Normal"])) for h in highlights]
        story.append(ListFlowable(items, bulletType="bullet"))
        story.append(Spacer(1, 12))

    metrics = report.get("metrics", {})
    story.append(Paragraph("<b>Metrics</b>", styles["Heading2"]))
    if report.get("report_type") == "volunteer_summary":
        lines = [
            f"Tasks completed: {metrics.get('tasks_completed')} / {metrics.get('tasks_total')}",
            f"Completion rate: {metrics.get('completion_rate')}%",
            f"Skills utilized: {', '.join(metrics.get('skills_utilized', [])) or '—'}",
        ]
    else:
        lines = [
            f"Volunteers: {metrics.get('volunteer_count')}",
            f"Tasks completed: {metrics.get('tasks_completed')} / {metrics.get('tasks_total')}",
            f"Completion rate: {metrics.get('completion_rate')}%",
        ]
    for line in lines:
        story.append(Paragraph(line, styles["Normal"]))

    doc.build(story)
    return buffer.getvalue()
