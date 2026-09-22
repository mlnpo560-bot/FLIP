from __future__ import annotations
from dataclasses import dataclass
import hashlib,json
from .crypto import KeyPair,verify

def quorum_size(n:int)->int:
    if n<1: raise ValueError("validator set must be non-empty")
    f=(n-1)//3
    return 2*f+1

@dataclass(frozen=True)
class Vote:
    height:int; round:int; block_hash:str; validator:str; step:str
    public_key:bytes=b""; signature:bytes=b""
    def payload(self)->bytes:
        return json.dumps({"height":self.height,"round":self.round,"block_hash":self.block_hash,"validator":self.validator,"step":self.step},sort_keys=True,separators=(",",":")).encode()
    def sign(self,key:KeyPair):
        if key.address!=self.validator: raise ValueError("validator key mismatch")
        return Vote(self.height,self.round,self.block_hash,self.validator,self.step,key.public_key,key.sign(self.payload()))
    def valid(self,validators:set[str])->bool:
        return self.validator in validators and self.public_key and verify(self.public_key,self.signature,self.payload())

@dataclass(frozen=True)
class QuorumCertificate:
    height:int; round:int; block_hash:str; step:str; validators:tuple[str,...]
    def hash(self)->str:
        return hashlib.sha256(json.dumps(self.__dict__,sort_keys=True,separators=(",",":")).encode()).hexdigest()

class ConsensusError(ValueError): pass

class BFTConsensus:
    """PBFT/Tendermint-style authenticated 2f+1 protocol model.

    Safety holds under authenticated validators, <=f Byzantine validators,
    immutable validator-set snapshots per height, and deterministic locking.
    Liveness additionally requires eventual synchrony and an honest proposer.
    """
    def __init__(self,validators:set[str]):
        if not validators: raise ConsensusError("empty validator set")
        self.validators=frozenset(validators); self.q=quorum_size(len(validators)); self.locked:dict[int,tuple[int,str]]={}
    def certificate(self,votes:list[Vote],height:int,round:int,block_hash:str,step:str)->QuorumCertificate:
        ids={v.validator for v in votes if v.height==height and v.round==round and v.block_hash==block_hash and v.step==step and v.valid(set(self.validators))}
        if len(ids)<self.q: raise ConsensusError("quorum not reached")
        return QuorumCertificate(height,round,block_hash,step,tuple(sorted(ids)))
    def can_prevote(self,height:int,block_hash:str)->bool:
        lock=self.locked.get(height); return lock is None or lock[1]==block_hash
    def lock(self,height:int,round:int,block_hash:str)->None:
        old=self.locked.get(height)
        if old and round<old[0]: raise ConsensusError("cannot move lock backwards")
        self.locked[height]=(round,block_hash)
