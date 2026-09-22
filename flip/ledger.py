from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from .transaction import Transaction

@dataclass
class LedgerAccount:
    balance: Decimal = Decimal("0")
    nonce: int = 0

class LedgerError(ValueError):
    pass

class NativeLedger:
    """Deterministic native-FLIP state machine."""
    def __init__(self):
        self.accounts: dict[str, LedgerAccount] = {}
        self.seen: set[str] = set()

    def account(self, address: str) -> LedgerAccount:
        if not address:
            raise LedgerError("empty address")
        return self.accounts.setdefault(address, LedgerAccount())

    def credit_genesis(self, address: str, amount: Decimal) -> None:
        amount = Decimal(amount)
        if amount < 0:
            raise LedgerError("negative genesis amount")
        self.account(address).balance += amount

    def apply(self, tx: Transaction) -> str:
        if tx.amount <= 0:
            raise LedgerError("amount must be positive")
        if tx.sender == tx.recipient:
            raise LedgerError("self-transfer")
        if tx.nonce < 0:
            raise LedgerError("invalid nonce")
        if not tx.valid_signature():
            raise LedgerError("invalid signature")
        txid = tx.txid()
        if txid in self.seen:
            raise LedgerError("replay")

        sender = self.account(tx.sender)
        recipient = self.account(tx.recipient)
        if tx.nonce != sender.nonce:
            raise LedgerError("invalid nonce")
        if sender.balance < tx.amount:
            raise LedgerError("insufficient balance")

        sender.balance -= tx.amount
        sender.nonce += 1
        recipient.balance += tx.amount
        self.seen.add(txid)
        return txid

    def snapshot(self) -> dict:
        return {
            address: {"balance": str(account.balance), "nonce": account.nonce}
            for address, account in sorted(self.accounts.items())
        }
