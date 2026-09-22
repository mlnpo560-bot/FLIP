from __future__ import annotations
from dataclasses import dataclass
import json
from .crypto import KeyPair,verify

@dataclass(frozen=True)
class PeerMessage:
    sender:str
    kind:str
    payload:bytes
    public_key:bytes
    signature:bytes
    def signing_payload(self)->bytes:
        return json.dumps({"sender":self.sender,"kind":self.kind,"payload":self.payload.hex()},sort_keys=True,separators=(",",":")).encode()
    @classmethod
    def sign(cls,key:KeyPair,kind:str,payload:bytes):
        m=cls(key.address,kind,payload,key.public_key,b"")
        return cls(m.sender,m.kind,m.payload,m.public_key,key.sign(m.signing_payload()))
    def valid(self)->bool:
        return bool(self.public_key and self.signature) and verify(self.public_key,self.signature,self.signing_payload())

class PeerError(ValueError):pass
class PeerNetwork:
    def __init__(self,node_id:str,key:KeyPair):
        if key.address!=node_id:raise PeerError("node/key mismatch")
        self.node_id=node_id;self.key=key;self.peers:dict[str,bytes]={};self.seen:set[str]=set()
    def register_peer(self,address:str,public_key:bytes):
        if not address or address==self.node_id:raise PeerError("invalid peer")
        self.peers[address]=public_key
    def receive(self,message:PeerMessage)->bool:
        if message.sender not in self.peers:raise PeerError("unknown peer")
        if self.peers[message.sender]!=message.public_key or not message.valid():raise PeerError("unauthenticated message")
        mid=__import__("hashlib").sha256(message.signing_payload()+message.signature).hexdigest()
        if mid in self.seen:return False
        self.seen.add(mid);return True
