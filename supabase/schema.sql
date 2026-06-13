-- NayePankh Bulbul — Supabase schema (Phase 5)
-- Run in Supabase SQL Editor or via migration tooling.

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE IF NOT EXISTS volunteers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    skills JSONB NOT NULL DEFAULT '[]'::jsonb,
    interests JSONB NOT NULL DEFAULT '[]'::jsonb,
    availability TEXT NOT NULL DEFAULT '',
    reminder_preferences JSONB NOT NULL DEFAULT '{"enabled": true, "email": true}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    required_skills JSONB NOT NULL DEFAULT '[]'::jsonb,
    deadline DATE NOT NULL,
    assigned_volunteer_id UUID REFERENCES volunteers(id) ON DELETE SET NULL,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'in_progress', 'completed')),
    assignment_reason TEXT,
    priority TEXT CHECK (priority IN ('High', 'Medium', 'Low')),
    ai_assigned BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS match_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    match_type TEXT NOT NULL,
    task_id UUID REFERENCES tasks(id) ON DELETE SET NULL,
    volunteer_id UUID REFERENCES volunteers(id) ON DELETE SET NULL,
    recommendations JSONB NOT NULL DEFAULT '[]'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    task_id UUID REFERENCES tasks(id) ON DELETE SET NULL,
    volunteer_id UUID REFERENCES volunteers(id) ON DELETE SET NULL,
    notification_type TEXT NOT NULL,
    recipient TEXT NOT NULL DEFAULT '',
    channel TEXT NOT NULL,
    status TEXT NOT NULL,
    subject TEXT NOT NULL DEFAULT '',
    error TEXT,
    sent_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS reports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    report_type TEXT NOT NULL,
    volunteer_id UUID REFERENCES volunteers(id) ON DELETE SET NULL,
    volunteer_name TEXT,
    period_start DATE,
    period_end DATE,
    metrics JSONB NOT NULL DEFAULT '{}'::jsonb,
    narrative TEXT NOT NULL DEFAULT '',
    highlights JSONB NOT NULL DEFAULT '[]'::jsonb,
    pdf_url TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_tasks_assigned_volunteer ON tasks(assigned_volunteer_id);
CREATE INDEX IF NOT EXISTS idx_tasks_deadline ON tasks(deadline);
CREATE INDEX IF NOT EXISTS idx_notifications_task ON notifications(task_id);
CREATE INDEX IF NOT EXISTS idx_reports_volunteer ON reports(volunteer_id);

ALTER TABLE volunteers ENABLE ROW LEVEL SECURITY;
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;
ALTER TABLE match_history ENABLE ROW LEVEL SECURITY;
ALTER TABLE notifications ENABLE ROW LEVEL SECURITY;
ALTER TABLE reports ENABLE ROW LEVEL SECURITY;

-- Server-side app uses service role key (bypasses RLS).
-- Anon/authenticated policies restrict direct client access.

CREATE POLICY volunteers_service_all ON volunteers
    FOR ALL USING (auth.role() = 'service_role') WITH CHECK (auth.role() = 'service_role');

CREATE POLICY tasks_service_all ON tasks
    FOR ALL USING (auth.role() = 'service_role') WITH CHECK (auth.role() = 'service_role');

CREATE POLICY match_history_service_all ON match_history
    FOR ALL USING (auth.role() = 'service_role') WITH CHECK (auth.role() = 'service_role');

CREATE POLICY notifications_service_all ON notifications
    FOR ALL USING (auth.role() = 'service_role') WITH CHECK (auth.role() = 'service_role');

CREATE POLICY reports_service_all ON reports
    FOR ALL USING (auth.role() = 'service_role') WITH CHECK (auth.role() = 'service_role');

-- Read-only anon policies for future volunteer portal direct access (optional).
CREATE POLICY volunteers_anon_read ON volunteers
    FOR SELECT USING (auth.role() = 'anon');

CREATE POLICY tasks_anon_read ON tasks
    FOR SELECT USING (auth.role() = 'anon');
