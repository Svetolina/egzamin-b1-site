-- Таблица для словаря, замечаний и отметок «ок» режима проверки.
-- Выполнить один раз: Supabase → SQL Editor → New query → вставить весь файл → Run.
-- Повторный запуск ничего не ломает.

create table if not exists public.user_items (
  user_id    uuid        not null default auth.uid() references auth.users(id) on delete cascade,
  coll       text        not null check (coll in ('words', 'comments', 'marks')),
  id         text        not null,
  data       jsonb       not null default '{}'::jsonb,
  deleted    boolean     not null default false,
  updated_at timestamptz not null default now(),
  primary key (user_id, coll, id)
);

-- Каждый видит и меняет только свои записи. Без входа — ничего.
alter table public.user_items enable row level security;

drop policy if exists "own rows: read"   on public.user_items;
drop policy if exists "own rows: insert" on public.user_items;
drop policy if exists "own rows: update" on public.user_items;
drop policy if exists "own rows: delete" on public.user_items;

create policy "own rows: read"   on public.user_items for select to authenticated using (user_id = (select auth.uid()));
create policy "own rows: insert" on public.user_items for insert to authenticated with check (user_id = (select auth.uid()));
create policy "own rows: update" on public.user_items for update to authenticated using (user_id = (select auth.uid())) with check (user_id = (select auth.uid()));
create policy "own rows: delete" on public.user_items for delete to authenticated using (user_id = (select auth.uid()));

revoke all on public.user_items from anon;
grant select, insert, update, delete on public.user_items to authenticated;
