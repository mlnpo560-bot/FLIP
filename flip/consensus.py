from __future__ import annotations
from dataclasses import dataclass
import hashlib, json
from .crypto import KeyPair, verify

@dataclass(frozen=True)
class Vote:
    height:int
    block_hash:str
    validator:str
    public_key:bytes=b""
    signature:bytes=b""
    def payload(self)->bytes:
        return json.dumps({"height":self.height,"block_hash":self.block_hash,"validator":self.validator},sort_keys=True,separators=(",",":")).encode()
    def sign(self,key:KeyPair)->"Vote":
        if key.address!=self.validator: raise ValueError("validator key mismatch")
        return Vote(self.height,self.block_hash,self.validator,key.public_key,key.sign(self.payload()))
    def valid_signature(self)->bool:
        return bool(self.public_key and self.signature) and verify(self.public_key,self.signature,self.payload())

class ConsensusError(ValueError): pass
class QuorumCertificate:
    def __init__(self,validators:set[str],quorum:int):
        if quorum<=0 or quorum>len(validators): raise ConsensusError("invalid quorum")
        self.validators=frozenset(validators); self.quorum=quorum
    def finalize(self,votes:list[Vote],height:int,block_hash:str)->bool:
        unique={v.validator for v in votes if v.height==height and v.block_hash==block_hash and v.validator in self.validators and v.valid_signature()}
        return len(unique)>=self.quorum

@dataclass(frozen=True)
class FinalityProof:
    height:int
    block_hash:str
    validators:tuple[str,...]
    def hash(self)->str:
        return hashlib.sha256(json.dumps(self.__dict__,sort_keys=True,separators=(",",":")).encode()).hexdigest()
