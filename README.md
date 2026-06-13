# NayePankh Bulbul AI Volunteer Coordinator (V2)

Production-grade MVP for AI-powered NGO volunteer management with a **dual-sided system**:

> **Full V2 spec:** see [docs/version2Mvp.md](docs/version2Mvp.md)

- **Public:** Candidate application + AI screening
- **Admin:** Approve/reject, manual volunteer add, task creation
- **Unified volunteer pool:** Single source of truth for assignments
- **AI task matching:** Skills, interests, availability + memory

## Tech stack

- Streamlit (UI)
- Python (services + agents)
- OpenAI or Gemini (LLM)
- JSON files in `database/` (MVP storage)

## Project structure

```
├── app.py                      # Home / overview
├── streamlit_app.py            # Streamlit Cloud entry
├── pages/
│   ├── 1_Candidate_Apply.py    # Public application form
│   ├── 2_Admin_Dashboard.py    # Candidates, pool, tasks
│   └── 3_Task_Assignment.py    # AI matching + status
├── agents/
│   ├── screening_agent.py
│   ├── task_matching_agent.py
│   └── admin_action_agent.py
├── core/
│   ├── llm_engine.py
│   ├── prompts.py
│   └── config.py
├── database/
│   ├── candidates.json
│   ├── volunteers.json
│   └── tasks.json
├── services/
│   ├── candidate_service.py
│   ├── volunteer_service.py
│   └── task_service.py
└── utils/
    ├── helpers.py
    ├── json_storage.py
    └── email_service.py
```

## Flows

### 1. Candidate application
1. User submits form on **Apply as Volunteer**
2. Record saved to `database/candidates.json` (status: `pending`)
3. AI Screening Agent scores application
4. Admin approves → moves to `database/volunteers.json`

### 2. Admin direct add
Admin adds volunteer manually → saved directly to volunteer pool (no screening).

### 3. Task matching
Open tasks matched to volunteer pool using LLM or rule-based fallback. Assignments stored in task + volunteer memory.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Set OPENAI_API_KEY or GEMINI_API_KEY (optional — rule-based fallback works without)
# Set ADMIN_PASSWORD for admin pages
streamlit run app.py
```

## Environment variables

See `.env.example` for LLM keys, `ADMIN_PASSWORD`, and optional email/webhook settings.

## Deploy

Streamlit Cloud main file: `streamlit_app.py`

## V2 memory system

Each volunteer stores assignment and completion history under `memory`:

```json
{
  "assignments": [{"task_id": "...", "assigned_at": "..."}],
  "completed_tasks": [{"task_id": "...", "completed_at": "..."}]
}
```

Used by the task matching agent for context-aware recommendations.
