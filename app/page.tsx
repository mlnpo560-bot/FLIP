"use client";

import { useEffect, useState } from "react";

type Epoch = {
  epoch: number;
  reference_index: string;
  total_supply: string;
  market_price: string | null;
};

export default function Home() {
  const [epoch, setEpoch] = useState<Epoch | null>(null);
  const [status, setStatus] = useState("Connecting…");

  useEffect(() => {
    fetch("/api/epochs")
      .then(r => r.json())
      .then(data => {
        if (data.latest) setEpoch(data.latest);
        setStatus(data.configured ? "Live data layer connected" : "Demo mode");
      })
      .catch(() => setStatus("Offline demo"));
  }, []);

  const index = epoch ? Number(epoch.reference_index) : 1;
  const supply = epoch ? Number(epoch.total_supply) : 1000;

  return (
    <main>
      <nav className="nav">
        <div className="brand"><span className="mark">F</span> FLIP</div>
        <div className="navlinks"><a href="#dashboard">Dashboard</a><a href="#protocol">Protocol</a><a href="#security">Security</a><a href="https://github.com/mlnpo560-bot/FLIP">GitHub</a></div>
      </nav>

      <section className="hero">
        <div className="eyebrow">DECENTRALIZED MONETARY RESEARCH NETWORK</div>
        <h1>Money with a<br/><span>monotonic reference.</span></h1>
        <p className="lead">FLIP separates protocol accounting from unpredictable market prices. Its prototype monetary layer maintains a non-decreasing internal reference index under defined state-transition rules.</p>
        <div className="actions"><a className="button primary" href="#dashboard">Open dashboard</a><a className="button" href="https://github.com/mlnpo560-bot/FLIP">Inspect the protocol</a></div>
        <div className="notice"><b>Research status</b><span>{status}</span><span>•</span><span>External market price is not guaranteed to rise.</span></div>
      </section>

      <section id="dashboard" className="section">
        <div className="sectionhead"><div><div className="eyebrow">LIVE PROTOCOL STATE</div><h2>FLIP dashboard</h2></div><span className="live">● {status}</span></div>
        <div className="cards">
          <article><span>REFERENCE INDEX</span><strong>{index.toFixed(6)}</strong><small>Never decreases under protocol rules</small></article>
          <article><span>TOTAL SUPPLY</span><strong>{supply.toFixed(2)}</strong><small>Current indexed account units</small></article>
          <article><span>LATEST EPOCH</span><strong>{epoch?.epoch ?? "—"}</strong><small>Supabase-backed when configured</small></article>
        </div>
      </section>

      <section id="protocol" className="section split">
        <div><div className="eyebrow">CORE INVARIANT</div><h2>Simple rule.<br/>Hard questions.</h2></div>
        <div className="formula"><div>I₀ = 1</div><div>Iₜ = max(Iₜ₋₁, Bₜ)</div><div>Qᵢ,ₜ = Qᵢ,ₜ₋₁ × Iₜ / Iₜ₋₁</div></div>
      </section>

      <section id="security" className="section grid3">
        <article><b>01 · Transparent</b><p>Open specifications, deterministic rules, executable tests and public research artifacts.</p></article>
        <article><b>02 · Non-custodial</b><p>The protocol design does not require a central reserve or administrator to define its monetary invariant.</p></article>
        <article><b>03 · Honest</b><p>A protocol reference index is not the same thing as purchasing power or an external market price.</p></article>
      </section>

      <footer>FLIP v0.2 · Experimental open-source protocol · Not financial advice · Not legal tender by default</footer>
    </main>
  );
}
