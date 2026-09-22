from __future__ import annotations
from dataclasses import dataclass
import hashlib,json
from typing import Iterable
from .crypto import KeyPair,verify

def merkle_root(txids:Iterable[str])->str:
    layer=[bytes.fromhex(x) for x in txids]
    if not layer:return hashlib.sha256(b"").hexdigest()
    while len(layer)>1:
        if len(layer)%2:layer.append(layer[-1])
        layer=[hashlib.sha256(layer[i]+layer[i+1]).digest() for i in range(0,len(layer),2)]
    return layer[0].hex()

@dataclass(frozen=True)
class BlockHeader:
    height:int; previous_hash:str; state_root:str; tx_root:str; timestamp:int; proposer:str
    def canonical(self)->bytes:return json.dumps(self.__dict__,sort_keys=True,separators=(",",":")).encode()
    def hash(self)->str:return hashlib.sha256(self.canonical()).hexdigest()

@dataclass(frozen=True)
class Block:
    header:BlockHeader
    transactions:tuple[str,...]
    proposer_public_key:bytes=b""
    proposer_signature:bytes=b""
    def signing_payload(self)->bytes:return self.header.canonical()
    def sign(self,key:KeyPair)->"Block":
        if key.address!=self.header.proposer:raise ValueError("proposer key mismatch")
        return Block(self.header,self.transactions,key.public_key,key.sign(self.signing_payload()))
    def valid_signature(self)->bool:
        return bool(self.proposer_public_key and self.proposer_signature) and verify(self.proposer_public_key,self.proposer_signature,self.signing_payload())
