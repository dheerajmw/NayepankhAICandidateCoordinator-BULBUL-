# Bulbul by NayePankh Foundation

## Overview

NGOs such as **NayePankh Foundation** rely on volunteers to deliver their mission, but coordinating them remains largely manual. Onboarding, task assignment, progress tracking, and follow-ups are fragmented across spreadsheets, messages, and ad hoc coordination. As volunteer numbers grow, these workflows do not scale and consume disproportionate staff time.

**Bulbul by NayePankh Foundation** automates the operational backbone of volunteer management—matching people to the right work, tracking outcomes, and keeping everyone accountable without constant human intervention.

---

## Problem Statement

Volunteer management in NGOs today suffers from four recurring gaps:

| Gap | Description |
|-----|-------------|
| **Manual overhead** | Coordinators spend hours on repetitive onboarding, assignment, and follow-up work |
| **Poor task matching** | Assignments rarely account for skills, interests, and availability in a structured way |
| **No contribution tracking** | Volunteer impact is hard to measure, summarize, or report |
| **Reactive coordination** | Reminders and escalations depend on someone remembering to act |

These gaps limit engagement, waste volunteer potential, and prevent NGOs from scaling their programs efficiently.

---

## Objective

Build an AI agent system that automates the full volunteer coordination lifecycle:

1. **Onboarding & profiling** — Capture skills, interests, and availability at registration
2. **Intelligent task assignment** — Match volunteers to tasks using AI reasoning, not manual guesswork
3. **Progress monitoring** — Track task status and completion over time
4. **Automated follow-ups** — Send reminders and nudges before deadlines slip
5. **Reporting & summarization** — Generate contribution summaries and exportable reports

---

## Expected Impact

| Area | Outcome |
|------|---------|
| **Operational efficiency** | Less manual coordination; staff focus shifts to high-value work |
| **Match quality** | Tasks aligned with volunteer skills and availability |
| **Engagement** | Structured tracking and timely reminders keep volunteers active |
| **Scalability** | AI agents handle growing volunteer pools without linear staff growth |

---

## System Architecture

The system is organized into five layers that work together from user input to automated output.

```
Volunteer Input → AI Agent Core → Task Matching → Memory Store → Dashboard → Automation → Summary
```

### 1. User Layer

- **Volunteer Portal** — Registration, profile management, and assigned task view
- **NGO Admin Interface** — Task creation, volunteer overview, and status monitoring

### 2. AI Agent Layer (Core Intelligence)

- **Profile Analyzer Agent** — Parses and structures volunteer profiles
- **Task Matching Agent** — Scores and ranks volunteer–task fit
- **Decision Engine** — Combines rules with LLM reasoning for final assignments
- **Summary Generator Agent** — Produces contribution reports and summaries

### 3. Memory Layer

Persistent storage for:

- Volunteer profiles and preferences
- Task definitions and history
- Assignment and completion status

> **MVP:** JSON files · **Production upgrade:** Supabase

### 4. Automation Layer

- Email reminders via SMTP or Gmail API
- Optional n8n workflow integrations
- Scheduled notification triggers

### 5. Output Layer

- Assigned tasks with rationale
- Progress dashboard for admins
- Contribution reports
- Certificates (PDF generation)

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Streamlit (fast MVP UI) |
| **Backend** | Python |
| **AI** | OpenAI API / Gemini API |
| **Memory (MVP)** | JSON |
| **Memory (upgrade)** | Supabase |
| **Automation** | Gmail API, optional n8n |
| **Deployment** | Streamlit Cloud, Render, or Vercel (if extended) |

---

## Project Structure

```
naye-pankh-bulbul/
│
├── app.py                      # Streamlit main app
├── requirements.txt
├── README.md
│
├── agents/
│   ├── profile_analyzer.py     # Analyzes volunteer profiles
│   ├── task_matcher.py         # Matches tasks to volunteers
│   └── summary_agent.py        # Generates reports
│
├── core/
│   ├── ai_engine.py            # LLM wrapper (OpenAI / Gemini)
│   └── prompts.py              # Prompt templates
│
├── data/
│   ├── volunteers.json         # Volunteer memory store
│   └── tasks.json              # Task database
│
├── utils/
│   ├── email_service.py        # Reminder and notification service
│   └── helpers.py              # Shared utilities
│
└── workflows/
    └── n8n_flow.json           # Optional automation flow
```

---

## AI Agent Logic (Core Prompt)

The central agent acts as the **Bulbul by NayePankh Foundation** with the following responsibilities:

**Goals**

- Understand each volunteer's skills, interests, and availability
- Match volunteers to suitable NGO tasks
- Ensure fairness and optimal utilization across the volunteer pool
- Recommend only **1–2 best-fit tasks** per volunteer
- Explain **why** each task was assigned

**Output format**

```
Assigned Task:   [Task title and description]
Reason:          [Why this volunteer is a good fit]
Priority:        High | Medium | Low
```

---

## MVP Feature Scope

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Volunteer Registration** | Collect skills, interests, and availability |
| 2 | **AI Task Assignment** | Match volunteers to tasks using LLM reasoning |
| 3 | **Memory System** | Persist volunteer history and assignment records |
| 4 | **Admin Dashboard** | View volunteers, tasks, and completion status |
| 5 | **Automated Reminders** | Notify volunteers about upcoming deadlines |
| 6 | **Summary Generator** | Produce contribution reports for admins and volunteers |

---

## Success Criteria

The MVP is successful when an NGO admin can:

1. Register a volunteer and capture a structured profile
2. Create a task and receive AI-recommended volunteer matches with explanations
3. Track assignment status without manual spreadsheets
4. Trigger automated reminders for pending work
5. Export a basic contribution summary for a volunteer or time period
