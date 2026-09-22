from __future__ import annotations
from dataclasses import dataclass, field
from .block import Block
from .crypto import KeyPair

@dataclass
class NodeState:
    node_id:str
    height:int=0
    peers:set[str]=field(default_factory=set)
    blocks:dict[str,Block]=field(default_factory=dict)

class Node:
    def __init__(self,node_id:str,key=None):
        self.state=NodeState(node_id); self.key=key or KeyPair.generate()
        if self.key.address!=node_id: raise ValueError("node id must equal key address")
    def add_peer(self,peer_id:str)->None:
        if peer_id!=self.state.node_id: self.state.peers.add(peer_id)
    def accept_block(self,block:Block)->str:
        if not block.valid_signature(): raise ValueError("invalid block signature")
        h=block.header.hash()
        if block.header.height!=self.state.height+1 and self.state.blocks: raise ValueError("non-contiguous block height")
        if self.state.blocks:
            previous=max(self.state.blocks.values(),key=lambda b:b.header.height)
            if block.header.previous_hash!=previous.header.hash(): raise ValueError("invalid previous hash")
        self.state.blocks[h]=block; self.state.height=max(self.state.height,block.header.height)
        return h
