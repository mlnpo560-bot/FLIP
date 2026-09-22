import unittest
from flip.block import Block, BlockHeader, merkle_root
from flip.consensus import QuorumCertificate, Vote
from flip.crypto import KeyPair
from flip.node import Node

class ProtocolTests(unittest.TestCase):
    def test_authenticated_block_and_node(self):
        key=KeyPair.generate()
        header=BlockHeader(1,"00"*32,"11"*32,merkle_root(["22"*32]),1,key.address)
        block=Block(header,("22"*32,)).sign(key)
        node=Node(key.address,key)
        self.assertTrue(block.valid_signature())
        node.accept_block(block)
        self.assertEqual(node.state.height,1)

    def test_invalid_block_signature_rejected(self):
        key=KeyPair.generate(); other=KeyPair.generate()
        h=BlockHeader(1,"00"*32,"11"*32,merkle_root([]),1,key.address)
        with self.assertRaises(ValueError):
            Node(key.address,key).accept_block(Block(h,()).sign(other))

    def test_authenticated_quorum(self):
        keys=[KeyPair.generate() for _ in range(3)]
        q=QuorumCertificate({k.address for k in keys},2)
        block_hash="aa"*32
        votes=[Vote(1,block_hash,k.address).sign(k) for k in keys[:2]]
        self.assertTrue(q.finalize(votes,1,block_hash))
        bad=Vote(1,block_hash,keys[2].address,keys[0].public_key,keys[0].sign(Vote(1,block_hash,keys[2].address).payload()))
        self.assertFalse(q.finalize([votes[0],bad],1,block_hash))

if __name__=="__main__": unittest.main()
