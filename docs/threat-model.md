# FLIP Threat Model

Oracle manipulation: attackers may submit false observations. Median aggregation reduces sensitivity to a minority of bad reporters but does not prove oracle security.

Sybil attacks: v0.1 does not solve identity resistance.

Monetary arithmetic: production code needs checked integer multiplication, deterministic rounding and dust handling.

Consensus: the monetary engine is independent from consensus in v0.1. A production chain needs formal consensus, validator selection, finality and recovery rules.

Market crash: the external market price is allowed to fall. The protocol reference index and market price are intentionally separate variables.
