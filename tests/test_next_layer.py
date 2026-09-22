import unittest
from decimal import Decimal
from flip.block import Block,BlockHeader,merkle_root
from flip.crypto import KeyPair
from flip.network import PeerMessage,PeerNetwork,PeerError
from flip.issuance import Issuer,IssuancePolicy,IssuanceError

class NextLayerTests(unittest.TestCase):
 def test_network_authentication(self):
  a,b=KeyPair.generate(),KeyPair.generate(); n=PeerNetwork(a.address,a);n.register_peer(b.address,b.public_key)
  m=PeerMessage.sign(b,"block",b"abc");self.assertTrue(n.receive(m));self.assertFalse(n.receive(m))
 def test_unknown_peer_rejected(self):
  a,b=KeyPair.generate(),KeyPair.generate();n=PeerNetwork(a.address,a)
  with self.assertRaises(PeerError):n.receive(PeerMessage.sign(b,"block",b"x"))
 def test_issuance_limits(self):
  i=Issuer(IssuancePolicy(Decimal("1000"),Decimal("100"),Decimal("50")))
  i.mint(50)
  with self.assertRaises(IssuanceError):i.mint(1)
  i.begin_epoch();i.mint(50)
  with self.assertRaises(IssuanceError):i.mint(1)
if __name__=="__main__":unittest.main()
