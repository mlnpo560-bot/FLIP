import unittest
from dataclasses import replace
from decimal import Decimal
from flip.wallet import Wallet
from flip.ledger import NativeLedger, LedgerError

class WalletLedgerTests(unittest.TestCase):
    def test_signed_transfer(self):
        a, b = Wallet(), Wallet()
        ledger = NativeLedger()
        ledger.credit_genesis(a.address, Decimal("100"))
        tx = a.sign_transfer(b.address, Decimal("25"), 0)
        ledger.apply(tx)
        self.assertEqual(ledger.account(a.address).balance, Decimal("75"))
        self.assertEqual(ledger.account(b.address).balance, Decimal("25"))

    def test_tampering_rejected(self):
        a, b = Wallet(), Wallet()
        ledger = NativeLedger()
        ledger.credit_genesis(a.address, Decimal("100"))
        tx = a.sign_transfer(b.address, Decimal("25"), 0)
        with self.assertRaises(LedgerError):
            ledger.apply(replace(tx, amount=Decimal("26")))

    def test_replay_rejected(self):
        a, b = Wallet(), Wallet()
        ledger = NativeLedger()
        ledger.credit_genesis(a.address, Decimal("100"))
        tx = a.sign_transfer(b.address, Decimal("25"), 0)
        ledger.apply(tx)
        with self.assertRaises(LedgerError):
            ledger.apply(tx)

    def test_nonce_and_balance_rules(self):
        a, b = Wallet(), Wallet()
        ledger = NativeLedger()
        ledger.credit_genesis(a.address, Decimal("10"))
        with self.assertRaises(LedgerError):
            ledger.apply(a.sign_transfer(b.address, Decimal("11"), 0))
        ledger.apply(a.sign_transfer(b.address, Decimal("5"), 0))
        with self.assertRaises(LedgerError):
            ledger.apply(a.sign_transfer(b.address, Decimal("1"), 0))

if __name__ == "__main__":
    unittest.main()
