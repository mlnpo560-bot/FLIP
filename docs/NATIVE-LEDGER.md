# FLIP Native Ledger

FLIP is moving from monetary-model code toward an actual native-money ledger.

## State transition

A valid transaction must be:
- authorized by the sender's cryptographic signature;
- addressed to a recipient;
- positive;
- assigned the sender's next nonce;
- backed by sufficient balance;
- not previously committed.

The deterministic transition is:

balance[sender] -= amount
balance[recipient] += amount
nonce[sender] += 1

A transaction identifier is derived from its canonical transaction payload.

## Security boundary

The current Python prototype accepts a pluggable verify_signature function so the state machine can be tested independently. Tests use a test verifier. This is NOT production cryptography.

Before real money can be used, FLIP needs audited public-key cryptography, a canonical address/serialization specification, network protocol, consensus/finality, persistent state, fee rules, and adversarial testing.

## Double-spend protection

The prototype uses sender nonce ordering and replay tracking. In a distributed production ledger, consensus—not merely a local set—must determine which transaction becomes final.

## Supabase boundary

Supabase is an analytics/indexing and application-data layer. It must not be the authoritative consensus ledger or hold monetary signing keys. The authoritative FLIP ledger must be independently reproducible by network nodes.
