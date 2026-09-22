# FLIP: A Decentralized Monetary Reference Protocol

## Abstract

FLIP v0.1 investigates a monetary construction in which a protocol reference index is non-decreasing by state-transition rule while account ownership proportions are preserved during reference-unit re-expression. The prototype uses no commodity reserve and no issuer-owned collateral.

The research question is whether decentralized incentives can keep an external market price within a useful bound around the protocol reference without turning FLIP into a collateral-backed or centrally supported asset.

## Model

I_0 = 1
I_t = max(I_(t-1), B_t)
R_t = I_t / I_(t-1)
Q_i,t = Q_i,t-1 * R_t

## Limitation

Nothing in v0.1 proves that an external market price P_t cannot decline.

## Research agenda

Study E_t = log(P_t / I_t) under rational-agent behavior, oracle faults, adversarial trading, liquidity shocks and network partitions.

## Status

v0.1 is a research simulator, not a live currency network.
