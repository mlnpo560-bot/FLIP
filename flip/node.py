from __future__ import annotations
from dataclasses import dataclass, field
from .block import Block

@dataclass
class NodeState:
    node_id: str
    height: int = 0
    peers: set[str] = field(default_factory=set)
    blocks: dict[str, Block] = field(default_factory=dict)

class Node:
    def __init__(self, node_id: str):
        self.state = NodeState(node_id)

    def add_peer(self, peer_id: str) -> None:
        if peer_id != self.state.node_id:
            self.state.peers.add(peer_id)

    def accept_block(self, block: Block) -> str:
        h = block.header.hash()
        self.state.blocks[h] = block
        self.state.height = max(self.state.height, block.header.height)
        return h
