from __future__ import annotations
import base64, hashlib, json
from dataclasses import dataclass

# Prototype-only signing interface. Real production keys MUST use an audited
# cryptographic implementation; this module deliberately avoids inventing one.

def canonical_json(obj: dict) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()

def address_from_public_key(public_key: bytes) -> str:
    digest = hashlib.sha256(public_key).hexdigest()
    return "flip1" + digest[:40]

@dataclass(frozen=True)
class SignedEnvelope:
    public_key: str
    signature: str
    payload: dict

def encode_bytes(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).decode().rstrip("=")

def decode_bytes(value: str) -> bytes:
    return base64.urlsafe_b64decode(value + "=" * (-len(value) % 4))
