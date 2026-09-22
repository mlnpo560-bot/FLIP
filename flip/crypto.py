from __future__ import annotations
import base64, hashlib, json
from dataclasses import dataclass
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives import serialization

def canonical_json(obj: dict) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()

def address_from_public_key(public_key: bytes) -> str:
    return "flip1" + hashlib.sha256(public_key).hexdigest()[:40]

@dataclass(frozen=True)
class KeyPair:
    private_key: Ed25519PrivateKey
    public_key: bytes
    address: str

    @classmethod
    def generate(cls):
        private = Ed25519PrivateKey.generate()
        public = private.public_key().public_bytes(
            serialization.Encoding.Raw, serialization.PublicFormat.Raw)
        return cls(private, public, address_from_public_key(public))

    def sign(self, payload: bytes) -> bytes:
        return self.private_key.sign(payload)

def verify(public_key: bytes, signature: bytes, payload: bytes) -> bool:
    try:
        Ed25519PublicKey.from_public_bytes(public_key).verify(signature, payload)
        return True
    except Exception:
        return False

def encode_bytes(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).decode().rstrip("=")

def decode_bytes(value: str) -> bytes:
    return base64.urlsafe_b64decode(value + "=" * (-len(value) % 4))
