# FLIP Protocol Layers

The repository now contains research implementations for the native ledger, canonical transaction hashing, Merkle roots, block headers, node state, and validator-quorum finalization.

These components are deliberately marked as prototypes. In particular, the quorum class is **not** a production Byzantine-fault-tolerant consensus algorithm, and the crypto module does not provide production signing.

Production gates remain:
- audited digital signatures;
- canonical binary serialization;
- persistent database-independent state;
- authenticated P2P transport;
- a specified consensus protocol with formal safety/liveness properties;
- economic Sybil resistance;
- chain recovery and finality rules;
- independent security audits.
