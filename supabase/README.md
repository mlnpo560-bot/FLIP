# Supabase integration

Supabase is an optional off-chain analytics/indexing layer.

It must NOT be used for consensus, authoritative monetary state, private signing keys, mint/burn authority or validator control.

The migration creates read-only public analytics tables with RLS enabled.

The connected Supabase account currently has no projects, so no hosted database was provisioned. Connect or create a Supabase project before applying this migration.
