import unittest
from decimal import Decimal
from flip.ledger import NativeLedger, Transaction, LedgerError

def valid(_):
    return True

class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.l = NativeLedger()
        self.l.credit_genesis("alice", Decimal("100"))
        self.l.account("bob")

    def test_transfer(self):
        tx = Transaction("alice", "bob", Decimal("25"), 0, "sig")
        self.l.apply(tx, valid)
        self.assertEqual(self.l.account("alice").balance, Decimal("75"))
        self.assertEqual(self.l.account("bob").balance, Decimal("25"))
        self.assertEqual(self.l.account("alice").nonce, 1)

    def test_double_spend_nonce_rejected(self):
        self.l.apply(Transaction("alice", "bob", Decimal("25"), 0, "sig"), valid)
        with self.assertRaises(LedgerError):
            self.l.apply(Transaction("alice", "bob", Decimal("25"), 0, "sig2"), valid)

    def test_replay_rejected(self):
        tx = Transaction("alice", "bob", Decimal("25"), 0, "sig")
        self.l.apply(tx, valid)
        with self.assertRaises(LedgerError):
            self.l.apply(tx, valid)

    def test_insufficient_balance(self):
        with self.assertRaises(LedgerError):
            self.l.apply(Transaction("alice", "bob", Decimal("101"), 0, "sig"), valid)

if __name__ == "__main__":
    unittest.main()
