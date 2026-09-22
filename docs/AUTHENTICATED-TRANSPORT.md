# Authenticated transport boundary

FLIP peers authenticate every application message with Ed25519 signatures.
A production transport MUST additionally provide:
- encrypted channel transport (TLS 1.3 or an equivalent audited secure transport);
- peer identity binding to the FLIP validator/node identity;
- replay protection and freshness;
- connection rate limits and message-size limits;
- peer discovery controls;
- key rotation and revocation.

The current repository implements authenticated application messages, not a complete Internet transport stack.