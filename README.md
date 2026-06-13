# NayePankh Bulbul AI Volunteer Coordinator

AI-powered volunteer coordination for [NayePankh Foundation](https://nayepankh.org).

## Phase 5 features (production scale)

- **Supabase storage** — PostgreSQL backend with pluggable storage layer (`auto` / `json` / `supabase`)
- **Schema + migration** — `supabase/schema.sql` and `scripts/migrate_to_supabase.py`
- **Admin RBAC** — Password-protected admin interface via `ADMIN_PASSWORD`
- **LLM fallback** — Primary provider with automatic OpenAI ↔ Gemini fallback
- **Prompt versioning** — `PROMPT_VERSION` env variable
- **Email retry** — Configurable SMTP retries with backoff
- **Production webhooks** — `scripts/webhook_server.py` for n8n scheduled reminders
- **Deployment** — Streamlit config, `Dockerfile`, and `render.yaml`

## Earlier phases (included)

- Phases 1–4: registration, AI matching, reminders, reports, certificates

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Local development (JSON)

Leave `SUPABASE_URL` empty — data stays in `data/*.json`.

### Production (Supabase)

1. Create a Supabase project.
2. Run `supabase/schema.sql` in the SQL Editor.
3. Configure `.env`:

```bash
STORAGE_BACKEND=supabase
SUPABASE_URL=https://YOUR_PROJECT.supabase.co
SUPABASE_KEY=your-service-role-key
ADMIN_PASSWORD=choose-a-strong-password
APP_ENV=production
```

4. Migrate existing JSON data:

```bash
python scripts/migrate_to_supabase.py
```

### LLM, email, webhooks

See `.env.example` for `OPENAI_API_KEY`, SMTP settings, and:

```bash
WEBHOOK_TOKEN=your-secret-token
python scripts/webhook_server.py   # POST /webhooks/reminders
```

Import `workflows/n8n_flow.json` into n8n for scheduled production runs.

## Run

```bash
streamlit run app.py
```

## Deploy

### Streamlit Cloud

1. Push repo to GitHub.
2. Create app at [share.streamlit.io](https://share.streamlit.io).
3. Add secrets from `.env.example` in the Streamlit Cloud secrets UI.

### Render

```bash
# Uses render.yaml — set env vars in Render dashboard
```

### Docker

```bash
docker build -t naye-pankh-bulbul .
docker run -p 8501:8501 --env-file .env naye-pankh-bulbul
```

## Project structure

```
naye-pankh-bulbul/
├── app.py
├── core/
│   ├── config.py              # Phase 5 env config
│   ├── ai_engine.py
│   └── prompts.py
├── utils/
│   ├── storage/
│   │   ├── json_backend.py
│   │   └── supabase_backend.py
│   └── auth.py
├── supabase/
│   └── schema.sql
├── scripts/
│   ├── migrate_to_supabase.py
│   └── webhook_server.py
├── render.yaml
├── Dockerfile
└── .streamlit/config.toml
```

## Docs

- [Problem statement](docs/problemStatement.md)
- [Phase-wise architecture](docs/phaseWiseArchitecture.md)

## Phase 5 exit criteria

- All data in Supabase when `STORAGE_BACKEND=supabase` (no JSON dependency)
- Secrets via environment variables only
- Deployable to Streamlit Cloud / Render / Docker
- n8n or webhook server handles scheduled reminders in production
