# FLIP — Worldwide Implementation Roadmap

FLIP is an experimental open-source monetary protocol. This document defines what “implement worldwide” means technically and what cannot be guaranteed by software.

## 1. Worldwide protocol vs worldwide legal tender

FLIP can be implemented as an open protocol available internationally. Software cannot by itself make FLIP legal tender in every jurisdiction. Operation, custody, exchange, payment services, taxation, consumer protection, sanctions compliance and other regulated activities remain subject to applicable law.

The protocol therefore targets **worldwide technical availability with jurisdiction-aware compliance**, not a claim of universal legal status.

## 2. Protocol layers

### Layer A — deterministic ledger

Every state transition MUST be deterministic and independently verifiable.

State includes:
- accounts and balances
- nonce/replay protection
- epoch
- monetary reference index
- transaction history
- protocol version

### Layer B — cryptographic ownership

Transactions MUST be authorized by digital signatures. A balance is controlled by the holder of the corresponding private key, not by a central administrator.

### Layer C — monetary rule

The prototype invariant is:

[
I_0=1,qquad I_t=max(I_{t-1},B_t)
]

where (B_t) is the accepted benchmark aggregate.

If the index changes from (I_{t-1}) to (I_t), accounting units are re-expressed by:

[
Q_{i,t}=Q_{i,t-1}rac{I_t}{I_{t-1}}.
]

This creates a non-decreasing **protocol reference index**. It does not guarantee that FLIP's external market price or purchasing power cannot decline.

### Layer D — oracle security

A production network MUST NOT trust one price reporter. The implementation should support:
- multiple independent reporters
- authenticated observations
- quorum
- robust aggregation
- bounded updates
- stale-data rejection
- anomaly detection
- epoch timestamps
- auditability
- emergency halt/fallback rules defined by protocol governance

The current Python median/quorum prototype is research code, not a production oracle.

### Layer E — consensus

The network requires a permissionless or explicitly governed consensus mechanism. The consensus design must specify:
- validator/node admission
- block/epoch construction
- finality
- fork choice
- Sybil resistance
- validator incentives
- denial-of-service resistance
- network recovery
- software upgrade rules

No single founder/admin key should be required for ordinary monetary operation in a decentralized release.

### Layer F — wallets and payments

The worldwide implementation requires:
- deterministic address format
- key generation/recovery
- signed transfers
- transaction fees
- QR/deep-link payment requests
- merchant APIs
- balance/history display
- hardware-wallet compatibility
- offline-safe transaction handling
- replay protection

### Layer G — interoperability

Adapters may connect FLIP to external systems, but bridges and custodians MUST be treated as separate trust domains. A bridge cannot be assumed to preserve FLIP's monetary invariant unless its own security model is formally specified.

## 3. Supply and issuance

FLIP MUST explicitly specify whether units are:
1. fixed-supply,
2. protocol-issued,
3. burned,
4. re-expressed through the index,
5. or some combination.

The current prototype's proportional re-expression is an accounting transformation and must not be confused with unrestricted money creation.

## 4. Privacy

Worldwide deployment requires privacy-preserving transaction design while preserving compliance obligations where legally applicable. The base protocol should avoid putting unnecessary personal information on the public ledger.

## 5. Governance

A worldwide open protocol needs transparent rules for:
- protocol upgrades
- vulnerability response
- oracle membership/requirements
- parameter changes
- emergency procedures
- dispute handling
- client compatibility

Governance powers should be minimized, explicit, auditable and bounded.

## 6. Compliance boundary

The core protocol should remain jurisdiction-neutral. Regulated interfaces should be modular so a wallet, exchange, custodian or payment provider can implement the compliance requirements applicable to its jurisdiction.

The repository MUST NOT claim that FLIP is “legal worldwide” merely because the code is open-source.

## 7. Production gate

FLIP should not be presented as production money until it has at minimum:
- deterministic consensus implementation
- audited cryptography
- formal transaction/state-transition specification
- adversarial testnet
- economic/security analysis
- oracle attack testing
- independent code audits
- reproducible builds
- key-management procedures
- documented upgrade and incident-response processes
- jurisdiction-specific legal review for regulated deployments

Until those gates are met, FLIP remains a research/test network.
