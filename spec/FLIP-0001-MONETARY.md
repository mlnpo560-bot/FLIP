# FLIP-0001: Monetary Reference and Re-expression

Scope: v0.1 reference mechanism only. Consensus, networking, identity, legal status, custody and exchange listing are outside this specification.

State:
- I_t > 0: reference index
- Q_i,t >= 0: balance
- B_t > 0: aggregated benchmark

Initial condition: I_0 = 1

Monotonic rule:
I_t = max(I_(t-1), B_t)
Therefore I_t >= I_(t-1).

Re-expression:
R_t = I_t / I_(t-1)
Q_i,t = Q_i,t-1 * R_t

Therefore proportional ownership is preserved under exact arithmetic.

Non-goals:
The protocol does not claim that market exchange price is monotonic, that purchasing power is guaranteed, or that any jurisdiction must recognize FLIP as legal tender.

A production implementation must define deterministic integer rounding, dust handling, overflow checks and replay behavior.
