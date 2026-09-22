from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
import base64, hashlib, json
from .crypto import KeyPair, verify

@dataclass(frozen=True)
class Transaction:
    sender: str
    recipient: str
    amount: Decimal
    nonce: int
    public_key: bytes
    signature: bytes = b""

    def payload(self) -> bytes:
        return json.dumps({
            "sender": self.sender, "recipient": self.recipient,
            "amount": str(self.amount), "nonce": self.nonce,
            "public_key": base64.b64encode(self.public_key).decode()
        }, sort_keys=True, separators=(",", ":")).encode()

    def txid(self) -> str:
        return hashlib.sha256(self.payload() + self.signature).hexdigest()

    @classmethod
    def sign(cls, key: KeyPair, recipient: str, amount: Decimal, nonce: int):
        unsigned = cls(key.address, recipient, Decimal(amount), nonce, key.public_key)
        return cls(unsigned.sender, unsigned.recipient, unsigned.amount,
                   unsigned.nonce, unsigned.public_key, key.sign(unsigned.payload()))

    def valid_signature(self) -> bool:
        return verify(self.public_key, self.signature, self.payload())
