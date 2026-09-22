-- Optional off-chain analytics/indexing schema.
-- Supabase is NOT part of FLIP consensus.

create table if not exists public.flip_epochs (
  epoch bigint primary key,
  reference_index numeric(78,30) not null check (reference_index > 0),
  total_supply numeric(78,30) not null check (total_supply >= 0),
  market_price numeric(78,30),
  created_at timestamptz not null default now()
);

create table if not exists public.flip_oracle_observations (
  id bigint generated always as identity primary key,
  epoch bigint not null references public.flip_epochs(epoch) on delete cascade,
  reporter text not null,
  observation numeric(78,30) not null check (observation > 0),
  created_at timestamptz not null default now()
);

alter table public.flip_epochs enable row level security;
alter table public.flip_oracle_observations enable row level security;

create policy "public can read flip epochs"
on public.flip_epochs for select
to anon, authenticated
using (true);

create policy "public can read oracle observations"
on public.flip_oracle_observations for select
to anon, authenticated
using (true);

-- No public write policy is created.
