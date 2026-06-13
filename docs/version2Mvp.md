# Bulbul by NayePankh Foundation — Version 2 MVP

This document describes **V2** of the AI Volunteer Coordinator: a dual-sided system with public candidate applications, admin approval, a unified volunteer pool, and AI task matching.

For V1 history and phased rollout, see `docs/phaseWiseArchitecture.md` and `docs/problemStatement.md`.

---

## What changed in V2

| Area | V1 | V2 |
|------|----|----|
| Onboarding | Direct volunteer registration | **Candidate application → AI screening → admin approval** |
| Admin add | Same registration path | **Direct add to pool** (bypasses screening) |
| Volunteer source | Single `volunteers` list | **Unified pool** from approved candidates + admin adds |
| UI | Single `app.py` monolith | **Multipage Streamlit** (`app.py` + `pages/`) |
| Data layer | `data/` + optional Supabase | **`database/` JSON** (MVP); services layer |
| Agents | Profile, matcher, decision, summary | **Screening, task matching, admin assist** |
| Memory | Workload + match history | **Per-volunteer assignment/completion memory** |

---

## Core flows

### 1. Candidate application (public)

**Page:** `pages/1_Candidate_Apply.py`

1. User submits: name, email, skills, interests, availability, motivation.
2. Record saved to `database/candidates.json` with `status: pending`.
3. **Screening Agent** (`agents/screening_agent.py`) returns:
   - `score` (0–100)
   - `decision` (`approve` | `reject` | `review`)
   - `suggested_role`
   - `reasoning`
4. Result stored on the candidate as `ai_screening`.
5. Admin must approve before the person enters the volunteer pool.

### 2. Admin approval / rejection

**Page:** `pages/2_Admin_Dashboard.py` → **Review candidates**

- View pending applications and AI screening results.
- Optional **Admin Action Agent** assist (`agents/admin_action_agent.py`).
- **Approve** → candidate copied to `database/volunteers.json`, status `approved`.
- **Reject** → status `rejected` with optional reason.

### 3. Admin direct add

**Page:** `pages/2_Admin_Dashboard.py` → **Add volunteer**

- Admin enters profile fields manually.
- Saved directly to `volunteers.json` with `source: admin`.
- No AI screening step.

### 4. Unified volunteer pool

**File:** `database/volunteers.json`

Single source of truth for:

- Task assignment
- Workload tracking
- Memory (past assignments and completions)

Volunteer `source` values:

- `approved_candidate` — came through application flow
- `admin` — added manually

### 5. AI task matching

**Page:** `pages/3_Task_Assignment.py`

**Agent:** `agents/task_matching_agent.py`

Matches open tasks to volunteers using:

- Skill overlap
- Interest alignment
- Availability text
- Current workload (active assignments)
- Volunteer memory (JSON history)

Output per match:

- `volunteer_id`, `volunteer_name`
- `fit_score`, `reasoning`, `priority`
- `assigned_task` (task title)

Uses LLM when API keys are set; otherwise rule-based fallback.

### 6. Memory system

Stored on each volunteer under `memory`:

```json
{
  "assignments": [
    {
      "task_id": "uuid",
      "task_title": "Weekend tutoring",
      "reason": "Strong teaching skills match",
      "assigned_at": "2026-06-13T12:00:00+00:00"
    }
  ],
  "completed_tasks": [
    {
      "task_id": "uuid",
      "task_title": "Weekend tutoring",
      "completed_at": "2026-06-20T12:00:00+00:00"
    }
  ]
}
```

Updated by `services/volunteer_service.py` on assign/complete.

---

## Project structure (V2)

```
nayePankhBulbul/
├── app.py                          # Home dashboard + navigation
├── streamlit_app.py                # Streamlit Cloud entry point
├── pages/
│   ├── 1_Candidate_Apply.py        # Public application
│   ├── 2_Admin_Dashboard.py        # Candidates, pool, task creation
│   └── 3_Task_Assignment.py        # AI matching + status
├── agents/
│   ├── screening_agent.py          # Candidate AI screening
│   ├── task_matching_agent.py      # Volunteer ↔ task matching
│   └── admin_action_agent.py       # Admin approve/reject assist
├── core/
│   ├── llm_engine.py               # Structured JSON LLM calls
│   ├── prompts.py                  # Screening, matching, admin prompts
│   ├── config.py                   # Environment configuration
│   └── ai_engine.py                # Shared LLM + rule-based helpers (V1)
├── database/
│   ├── candidates.json
│   ├── volunteers.json
│   └── tasks.json
├── services/
│   ├── candidate_service.py
│   ├── volunteer_service.py
│   └── task_service.py
├── utils/
│   ├── json_storage.py             # Read/write database/*.json
│   ├── helpers.py                  # parse_comma_list, etc.
│   ├── auth.py                     # Admin password gate
│   └── ui/                         # Stitch theme components
└── workflows/
    └── n8n_reminder_flow.json      # Optional automation (not wired to V2 yet)
```

---

## Data schemas (MVP)

### Candidate (`candidates.json`)

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | UUID |
| `name`, `email` | string | Required |
| `skills`, `interests` | string[] | Comma-separated in UI |
| `availability`, `motivation` | string | Required |
| `status` | string | `pending` \| `approved` \| `rejected` |
| `source` | string | `application` |
| `ai_screening` | object \| null | Score, decision, role, reasoning |
| `created_at`, `reviewed_at` | ISO datetime | |

### Volunteer (`volunteers.json`)

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | UUID |
| `name`, `email` | string | |
| `skills`, `interests`, `availability` | | |
| `source` | string | `admin` \| `approved_candidate` |
| `candidate_id` | string \| null | Link to original application |
| `ai_screening` | object \| null | Copied from candidate if applicable |
| `memory` | object | Assignments + completions |
| `created_at` | ISO datetime | |

### Task (`tasks.json`)

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | UUID |
| `title`, `description` | string | |
| `required_skills` | string[] | |
| `deadline` | string | Date |
| `assigned_volunteer_id` | string \| null | |
| `status` | string | `open` \| `assigned` \| `in_progress` \| `completed` |
| `assignment_reason` | string | AI or manual |
| `priority` | string | `High` \| `Medium` \| `Low` |
| `ai_assigned` | boolean | |

---

## Prompt templates

Defined in `core/prompts.py`:

| Prompt | Used by |
|--------|---------|
| `SCREENING_*` | Screening agent |
| `TASK_MATCHING_V2_*` | Task matching agent |
| `ADMIN_DECISION_*` | Admin action agent |

All agents expect **JSON-only** LLM responses via `core/llm_engine.py`.

---

## Configuration

Copy `.env.example` → `.env`.

| Variable | Required | Purpose |
|----------|----------|---------|
| `ADMIN_PASSWORD` | Recommended | Protects admin pages |
| `OPENAI_API_KEY` or `GEMINI_API_KEY` | Optional | Real LLM; rule-based fallback without |
| `LLM_PROVIDER` | Optional | `openai` or `gemini` |
| `APP_ENV` | Optional | `development` / `production` |

Legacy V1 vars (`SUPABASE_*`, `SMTP_*`, `WEBHOOK_*`) remain in `.env.example` but are **not wired to V2 services** yet.

---

## Run locally

```bash
cd nayePankhBulbul
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env — set ADMIN_PASSWORD and optional LLM keys
streamlit run app.py
```

Navigate via sidebar:

1. **Home** — KPIs and flow overview  
2. **Apply as Volunteer** — public form  
3. **Admin Dashboard** — sign in, review, add, create tasks  
4. **Task Assignment** — AI matches and status updates  

---

## Deploy (Streamlit Cloud)

- **Main file:** `streamlit_app.py`
- **Secrets:** Set `ADMIN_PASSWORD`, LLM keys in the Cloud dashboard
- **Persistence warning:** JSON files in `database/` reset on redeploy unless you mount external storage or migrate to Supabase

---

## MVP scope — included

- [x] Candidate application form
- [x] AI screening with structured output
- [x] Admin approve / reject
- [x] Admin manual volunteer add
- [x] Unified volunteer pool
- [x] Task creation (admin)
- [x] AI task matching with reasoning
- [x] Assignment + status tracking
- [x] Volunteer memory (JSON)
- [x] Rule-based fallback without API keys
- [x] Admin password gate

---

## Known gaps (post-MVP)

| Item | Status |
|------|--------|
| Supabase persistence for V2 | Not connected — V2 uses `database/` only |
| Email on approve/reject | Not wired — `utils/email_service.py` exists from V1 |
| Reminder automation | n8n flow present; not integrated with V2 tasks |
| Candidate self-service portal | V1 volunteer portal removed in V2 multipage app |
| Reports / certificates | V1 feature; not in V2 pages yet |
| Role-based admin (multi-user) | Single shared password only |

---

## Suggested test plan

1. **Apply** — Submit candidate application; confirm AI screening appears.
2. **Approve** — Admin approves; verify volunteer appears in pool.
3. **Direct add** — Admin adds second volunteer without application.
4. **Create task** — Admin creates open task (or use demo seed on empty tasks).
5. **Match** — Task Assignment → Generate AI matches → Assign volunteer.
6. **Complete** — Update task status to `completed`; check volunteer memory.

---

## Related docs

- `README.md` — Quick start and structure summary  
- `docs/problemStatement.md` — Original product vision (V1)  
- `docs/phaseWiseArchitecture.md` — V1 phased architecture (Phases 1–5)
