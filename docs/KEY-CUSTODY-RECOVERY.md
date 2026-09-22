# Key custody and recovery

Private keys are never stored in Supabase or committed to GitHub.

Production wallet requirements:
1. Generate keys using a CSPRNG.
2. Encrypt private keys at rest using a user-controlled passphrase or platform secure enclave/HSM.
3. Never transmit private keys to validators or indexing services.
4. Support encrypted backup/export with explicit user confirmation.
5. Support key rotation by authenticated account recovery transactions.
6. Treat recovery as a protocol operation; no operator may silently rewrite balances.
7. Hardware-wallet/HSM support should be implemented before production custody.

Loss of a private key must not imply that an administrator can arbitrarily seize or recreate funds.