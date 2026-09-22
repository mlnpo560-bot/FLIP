# FLIP Production Status

FLIP is the project's intended **production digital-money protocol**.

This repository now treats production currency as the target operating mode, while distinguishing implementation status from legal-tender status.

## Production principles

FLIP production software MUST:
- preserve deterministic state transitions;
- require cryptographic authorization for spending;
- prevent replay and double spending;
- use independently verifiable ledger state;
- keep consensus separate from application databases;
- protect monetary keys;
- provide reproducible builds and protocol-versioning;
- expose auditable transaction and block history;
- fail closed on invalid monetary state.

## Current implementation boundary

The repository contains working research implementations of the ledger, transaction identity, block primitives, validator quorum, node state, oracle model and Supabase indexing.

Some components are still prototypes and are not certified production-safe. In particular, no claim is made that the current cryptography, consensus, wallet, networking or monetary-policy implementation has passed an independent security audit.

## Legal boundary

Calling FLIP a production digital-money project does **not** itself make FLIP legal tender or authorized in every jurisdiction.

Legal recognition, licensing, registration, AML/CFT obligations, taxation, consumer protection and payment-service rules remain jurisdiction-specific.

## Release policy

A release labeled production must publish:
1. exact protocol version;
2. reproducible source/build artifacts;
3. cryptographic and consensus specifications;
4. genesis parameters;
5. supply/issuance rules;
6. wallet/address specification;
7. network specification;
8. security audit status;
9. known limitations;
10. applicable legal/compliance documentation.

Until those artifacts are published and independently verified, the repository should describe the release as an **experimental production-target implementation**, not as audited production financial infrastructure.
