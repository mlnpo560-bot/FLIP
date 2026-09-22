from __future__ import annotations
from dataclasses import dataclass
import hashlib, json
from typing import Iterable

def merkle_root(txids: Iterable[str]) -> str:
    layer = [bytes.fromhex(x) for x in txids]
    if not layer:
        return hashlib.sha256(b"").hexdigest()
    while len(layer) > 1:
        if len(layer) % 2:
            layer.append(layer[-1])
        layer = [hashlib.sha256(layer[i] + layer[i+1]).digest()
                 for i in range(0, len(layer), 2)]
    return layer[0].hex()

@dataclass(frozen=True)
class BlockHeader:
    height: int
    previous_hash: str
    state_root: str
    tx_root: str
    timestamp: int
    proposer: str

    def hash(self) -> str:
        payload = json.dumps(self.__dict__, sort_keys=True, separators=(",", ":")).encode()
        return hashlib.sha256(payload).hexdigest()

@dataclass(frozen=True)
class Block:
    header: BlockHeader
    transactions: tuple[str, ...]
