# FLIP v0.1

FLIP is a research prototype for a decentralized digital monetary protocol.

Core invariant:
I_0 = 1
I_t = max(I_(t-1), B_t)

When the reference index rises:
R_t = I_t / I_(t-1)
Q_(i,t) = Q_(i,t-1) * R_t

This preserves ownership shares under exact arithmetic.

FLIP does NOT claim that a freely traded market price can never fall, nor that every jurisdiction must recognize FLIP as legal tender. v0.1 is research software, not a live currency or investment product.

Repository:
- flip/ — monetary engine and oracle aggregation
- simulator/ — deterministic economic simulation
- tests/ — protocol invariants
- spec/ — normative specification
- docs/ — design and threat model
- supabase/ — optional off-chain analytics; never consensus

Run:
python -m unittest discover -s tests -v
python simulator/run_experiment.py

Status: research prototype, pre-network, pre-mainnet, unaudited.
