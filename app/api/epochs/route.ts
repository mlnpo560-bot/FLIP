import { NextResponse } from "next/server";

export async function GET() {
  const url = process.env.SUPABASE_URL;
  const key = process.env.SUPABASE_PUBLISHABLE_KEY;

  if (!url || !key) {
    return NextResponse.json({ configured: false, latest: null });
  }

  const res = await fetch(
    `${url}/rest/v1/flip_epochs?select=epoch,reference_index,total_supply,market_price&order=epoch.desc&limit=1`,
    { headers: { apikey: key, Authorization: `Bearer ${key}` }, cache: "no-store" }
  );

  if (!res.ok) {
    return NextResponse.json({ configured: true, latest: null, error: "database query failed" }, { status: 502 });
  }

  const rows = await res.json();
  return NextResponse.json({ configured: true, latest: rows[0] ?? null });
}
