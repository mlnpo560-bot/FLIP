import unittest
from flip.block import merkle_root, BlockHeader
from flip.consensus import QuorumCertificate, Vote

class ProtocolTests(unittest.TestCase):
    def test_merkle_root_is_deterministic(self):
        xs = ["00"*32, "11"*32, "22"*32]
        self.assertEqual(merkle_root(xs), merkle_root(xs))

    def test_quorum(self):
        q = QuorumCertificate({"a","b","c"}, 2)
        votes=[Vote(1,"h","a"), Vote(1,"h","b")]
        self.assertTrue(q.finalize(votes,1,"h"))

    def test_insufficient_quorum(self):
        q = QuorumCertificate({"a","b","c"}, 2)
        self.assertFalse(q.finalize([Vote(1,"h","a")],1,"h"))

if __name__ == "__main__":
    unittest.main()
