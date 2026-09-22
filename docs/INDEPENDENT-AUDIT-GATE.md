# Independent security audit gate

The repository cannot truthfully claim an independent security audit unless an external qualified auditor has completed one.

Required audit scope:
- Ed25519 key/address handling
- canonical serialization
- transaction/state-machine correctness
- block validation
- BFT safety and liveness assumptions
- validator-set transitions
- genesis and issuance controls
- P2P authentication and DoS boundaries
- persistence/recovery
- adversarial/fuzz testing
- supply and monetary invariants

Audit artifacts must identify auditor, version/commit, scope, findings, severity, remediation and residual risks.