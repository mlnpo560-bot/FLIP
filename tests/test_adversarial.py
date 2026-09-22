import unittest
from decimal import Decimal
from dataclasses import replace
from flip.crypto import KeyPair
from flip.consensus import BFTConsensus,Vote,quorum_size,ConsensusError
from flip.validators import Validator,ValidatorSet
from flip.genesis import make_genesis

class AdversarialTests(unittest.TestCase):
 def test_quorum_is_two_f_plus_one(self):
  self.assertEqual(quorum_size(4),3); self.assertEqual(quorum_size(7),5)
 def test_conflicting_certificate_cannot_share_same_votes(self):
  ks=[KeyPair.generate() for _ in range(4)]
  ids={k.address for k in ks}; c=BFTConsensus(ids)
  vs=[Vote(1,0,"aa"*32,k.address,"PREVOTE").sign(k) for k in ks[:3]]
  cert=c.certificate(vs,1,0,"aa"*32,"PREVOTE")
  self.assertEqual(len(cert.validators),3)
  with self.assertRaises(ConsensusError):
   c.certificate(vs,1,0,"bb"*32,"PREVOTE")
 def test_lock_cannot_move_back(self):
  ks=[KeyPair.generate() for _ in range(4)]; c=BFTConsensus({k.address for k in ks})
  c.lock(2,3,"aa"*32)
  with self.assertRaises(ConsensusError): c.lock(2,2,"bb"*32)
 def test_validator_duplicates_rejected(self):
  k=KeyPair.generate()
  with self.assertRaises(Exception): ValidatorSet([Validator(k.address,k.public_key),Validator(k.address,k.public_key)])
 def test_genesis_deterministic(self):
  g=make_genesis("FLIP-main",1,1000,["b","a"])
  self.assertTrue(g.verify()); self.assertEqual(g.validators,("a","b"))
if __name__=="__main__":unittest.main()
