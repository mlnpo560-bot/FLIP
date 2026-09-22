# 🌐 FLIP — A New Architecture for Digital Money

<p align="center">
  <strong>FLIP</strong> is an open-source research project exploring a decentralized monetary system built around a <em>monotonic internal reference index</em>.
</p>

<p align="center">
  <em>Transparent rules. Verifiable mathematics. No promise of a risk-free market price.</em>
</p>

<p align="center">
  <a href="https://github.com/mlnpo560-bot/FLIP">Repository</a> ·
  <a href="spec/FLIP-0001-MONETARY.md">Protocol Specification</a> ·
  <a href="WHITEPAPER.md">Whitepaper</a> ·
  <a href="docs/threat-model.md">Threat Model</a>
</p>

---

## ✨ What is FLIP?

**FLIP** is a research-oriented digital monetary protocol designed to investigate a different question from conventional cryptocurrencies:

> **Can a decentralized monetary system maintain a non-decreasing protocol reference index without depending on a reserve of a particular physical asset?**

The project separates two concepts that are often treated as if they were the same:

1. **Protocol reference value** — an internal mathematical quantity governed by deterministic protocol rules.
2. **External market price** — the price at which independently operated markets may value or exchange FLIP.

FLIP's core design can make the **protocol reference index non-decreasing** under its defined state-transition rules. It cannot, by mathematics alone, guarantee that an external market price will never fall.

That distinction is fundamental to the project.

---

## 🧠 The Core Idea

FLIP begins with a reference index:

$$
I_0 = 1
$$

At every protocol epoch, a benchmark value (B_t) is constructed from validated observations:

$$
I_t = \max(I_{t-1}, B_t)
$$

Therefore:

$$
I_t \ge I_{t-1}
$$

and consequently:

$$
I_t \ge I_0
$$

for every valid epoch.

When the reference index increases, the re-expression factor is:

$$
R_t = \frac{I_t}{I_{t-1}}
$$

and an account balance (Q_i) is re-expressed as:

$$
Q_{i,t}=Q_{i,t-1}R_t
$$

Under exact arithmetic, proportional ownership is preserved:

$$
\frac{Q_{i,t}}{\sum_j Q_{j,t}}
=
\frac{Q_{i,t-1}}{\sum_j Q_{j,t-1}}
$$

The goal is not to create value from nothing. The goal is to define a transparent monetary unit whose **internal accounting reference cannot decrease under the protocol's own rules**, while keeping the distinction between accounting mechanics and market economics explicit.

---

## 🔬 Why FLIP Exists

Many digital-currency designs focus on one or more of the following:

- fixed or algorithmically controlled supply;
- proof-of-work or proof-of-stake security;
- collateral or reserves;
- stablecoins linked to external assets;
- speculative market price discovery;
- centralized monetary policy.

FLIP explores another design space:

**a monetary protocol centered on a mathematical reference index and proportional balance re-expression.**

This makes FLIP a research platform for studying:

- monetary invariants;
- decentralized oracle aggregation;
- index construction;
- proportional accounting;
- monetary policy algorithms;
- market/reference-price divergence;
- economic resilience;
- adversarial oracle behavior;
- decentralized governance;
- regulatory interfaces.

---

## 🏗️ Architecture

FLIP is designed as a layered system:

```text
┌─────────────────────────────────────────────┐
│              Applications                   │
│  Wallets • Payments • Exchanges • APIs      │
├─────────────────────────────────────────────┤
│          Compliance / Gateway Layer         │
│ KYC/KYB • AML/CFT • Sanctions • Tax Export  │
├─────────────────────────────────────────────┤
│              Monetary Layer                 │
│ Index • Oracle Aggregation • Re-expression  │
├─────────────────────────────────────────────┤
│              Consensus Layer                │
│ Ordering • Finality • State Validation      │
├─────────────────────────────────────────────┤
│                 Network                    │
│ Peers • Messages • Cryptographic Transport  │
└─────────────────────────────────────────────┘
```

The **monetary layer** is the conceptual center of the current research prototype.

The **compliance/gateway layer is intentionally separated from consensus**. Jurisdictions can impose different requirements on exchanges, custodians, payment providers and other regulated services; protocol code cannot automatically make an activity legal in every jurisdiction.

---

## 🧮 Oracle Aggregation

The benchmark (B_t) should not depend blindly on one data source.

The prototype therefore explores quorum-based observations and robust aggregation:

- minimum observation quorum;
- positive-value validation;
- median aggregation;
- bounded upward movement;
- rejection of malformed/non-positive observations;
- monotonic reference-index updates.

The median is particularly useful as a simple robust estimator because one extreme observation should not automatically determine the benchmark.

The production protocol would require substantially stronger oracle design, including authenticated data feeds, source diversity, liveness rules, dispute mechanisms, manipulation resistance and formally specified failure handling.

---

## 🛡️ Security Philosophy

FLIP is designed around explicit invariants rather than assumptions.

The repository includes tests for:

- index monotonicity;
- rejection of decreasing reference values;
- oracle quorum requirements;
- invalid observation rejection;
- median aggregation;
- proportional balance re-expression;
- preservation of ownership shares.

The project also documents threats involving:

- oracle manipulation;
- Sybil behavior;
- arithmetic and rounding errors;
- consensus failures;
- market/reference-price divergence;
- governance and upgrade risks.

**Unaudited research code must never be treated as production financial infrastructure.**

---

## 📊 Protocol Value vs. Market Price

This is one of the most important parts of FLIP.

Let:

[
P_F(t)=I_t
]

represent the protocol's internal reference value, while:

[
P_M(t)
]

represents an independently determined external market price.

FLIP does **not** assert:

[
P_M(t+1) \ge P_M(t)
]

Instead, the protocol studies:

[
P_F(t+1) \ge P_F(t)
]

and the deviation:

[
E_t=\log\left(\frac{P_M(t)}{P_F(t)}\right)
]

This allows researchers to measure how far market valuation may diverge from the protocol reference without confusing the two quantities.

A market can fall even if the protocol reference index does not.

---

## 🌍 Global & Regulatory Design

FLIP is intended to be **regulatory-aware**, not to claim automatic worldwide legality.

Different jurisdictions can impose different rules on:

- virtual assets;
- exchanges;
- custodians;
- payment services;
- money transmission;
- securities or financial instruments;
- consumer protection;
- taxation;
- AML/CFT;
- sanctions;
- identity verification.

Therefore FLIP separates the open protocol from regulated service providers.

The repository can evolve toward jurisdiction-specific compliance documentation and gateway policies without embedding one country's legal assumptions into the mathematical consensus layer.

> **Important:** FLIP is not automatically legal tender, a licensed financial institution, a guaranteed investment, or a guarantee that operation is lawful in every jurisdiction.

---

## 🧪 Current Status

**FLIP v0.1 is a research prototype.**

It is:

- ✅ mathematically specified at the prototype monetary layer;
- ✅ accompanied by executable tests;
- ✅ accompanied by a deterministic simulation;
- ✅ documented with a threat model;
- ✅ structured for future protocol research;
- ⚠️ not a live blockchain;
- ⚠️ not a production payment network;
- ⚠️ not audited;
- ⚠️ not a guarantee of financial returns;
- ⚠️ not a guarantee that market price cannot decline;
- ⚠️ not automatically recognized as legal tender worldwide.

The project deliberately makes these limitations explicit.

---

## 🚀 Run the Prototype

Clone the repository and run:

```bash
python -m unittest discover -s tests -v
```

Run the deterministic economic experiment:

```bash
python simulator/run_experiment.py
```

The experiment demonstrates the intended distinction between a non-decreasing protocol reference index and an independently simulated market price.

---

## 📁 Repository Structure

```text
FLIP/
├── flip/
│   ├── __init__.py
│   └── monetary.py
│
├── simulator/
│   └── run_experiment.py
│
├── tests/
│   └── test_monetary.py
│
├── spec/
│   └── FLIP-0001-MONETARY.md
│
├── docs/
│   └── threat-model.md
│
├── supabase/
│   ├── README.md
│   └── migrations/
│
├── WHITEPAPER.md
├── SECURITY.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## 🗺️ Research Roadmap

### Phase 1 — Mathematical Foundation
- [x] Define the monotonic reference-index invariant
- [x] Define proportional balance re-expression
- [x] Implement oracle aggregation prototype
- [x] Write invariant tests
- [x] Build deterministic simulation
- [x] Document initial threat model

### Phase 2 — Formal Protocol
- [ ] Integer/fixed-point monetary arithmetic
- [ ] Deterministic rounding and dust rules
- [ ] Overflow/underflow specifications
- [ ] Replay protection
- [ ] State-transition formalization
- [ ] Cryptographic transaction model
- [ ] Consensus specification

### Phase 3 — Decentralized Network
- [ ] Peer-to-peer networking
- [ ] Transaction propagation
- [ ] Block/state architecture
- [ ] Finality mechanism
- [ ] Validator economics
- [ ] Network attack simulations

### Phase 4 — Oracle Research
- [ ] Multi-source authenticated feeds
- [ ] Byzantine-resistant aggregation
- [ ] Oracle dispute protocol
- [ ] Data-source reputation
- [ ] Liveness and fallback rules
- [ ] Manipulation-cost analysis

### Phase 5 — Economic Research
- [ ] Market/reference-price divergence models
- [ ] Liquidity simulations
- [ ] Game-theoretic analysis
- [ ] Stress testing
- [ ] Bank-run/liquidity-crisis analogues
- [ ] Long-horizon monetary simulations

### Phase 6 — Compliance & Deployment Research
- [ ] Jurisdiction-specific legal research
- [ ] Gateway compliance interfaces
- [ ] AML/CFT integration points
- [ ] Sanctions-screening interfaces
- [ ] Consumer-risk disclosures
- [ ] Tax-reporting exports
- [ ] Independent legal review

---

## 🔭 Long-Term Research Questions

FLIP is ultimately an experimental framework for asking difficult questions:

1. Can a monetary reference system remain mathematically monotonic while remaining economically meaningful?
2. What benchmark construction minimizes manipulation?
3. How should an oracle system behave when trusted data sources disagree?
4. Can decentralized governance change parameters without creating unacceptable capture risk?
5. How does market liquidity interact with a monotonic internal reference?
6. What happens when external market price and protocol reference diverge for long periods?
7. Can the system remain robust under Byzantine participants?
8. Which consensus architecture provides the required security and decentralization?
9. How should monetary arithmetic behave under billions of accounts and extremely long time horizons?
10. What regulatory architecture allows open protocol research while regulated gateways comply with local law?

These are research questions—not claims that the answers have already been proven.

---

## 🤝 Open Source

FLIP is intended to be developed transparently.

Contributions should prioritize:

- reproducibility;
- mathematical correctness;
- deterministic behavior;
- security;
- test coverage;
- explicit assumptions;
- documented limitations;
- independent review.

Before proposing a protocol change, contributors should explain:

1. **What invariant changes?**
2. **Why is the change necessary?**
3. **What new attack surface does it introduce?**
4. **How is it tested?**
5. **How does it affect economic behavior?**
6. **Does it change the legal/compliance boundary?**

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

---

## 📚 Documentation

| Document | Purpose |
|---|---|
| [FLIP-0001 Monetary Specification](spec/FLIP-0001-MONETARY.md) | Normative monetary-layer design |
| [Whitepaper](WHITEPAPER.md) | Conceptual and mathematical overview |
| [Threat Model](docs/threat-model.md) | Security assumptions and attack surfaces |
| [Supabase Notes](supabase/README.md) | Optional off-chain analytics architecture |
| [Contributing Guide](CONTRIBUTING.md) | Development and contribution rules |
| [Security Policy](SECURITY.md) | Security reporting and responsible disclosure |

---

## ⚖️ Disclaimer

FLIP is an experimental open-source research project.

Nothing in this repository constitutes:

- financial advice;
- an offer to sell a financial instrument;
- a promise of profit;
- a guarantee of purchasing power;
- a guarantee of market-price stability;
- a guarantee of legal-tender status;
- legal advice;
- tax advice;
- regulatory approval.

The legality of operating, exchanging, custodying, issuing, marketing or providing services around any digital asset depends on the applicable jurisdiction, facts and regulatory framework.

---

## 🌟 The Vision

FLIP explores a simple but ambitious idea:

> **Build monetary rules that can be stated mathematically, tested computationally, inspected publicly, and separated clearly from the unpredictable behavior of external markets.**

The project does not begin by assuming that a perfect currency already exists.

It begins with an invariant.

It tests the invariant.

It exposes its limitations.

And it leaves the harder questions open for mathematics, computer science, economics, cryptography, security research and law to answer.

---

<p align="center">
  <strong>FLIP — Researching a different architecture for digital money.</strong>
</p>

<p align="center">
  Open source • Mathematical • Experimental • Auditable by design
</p>
