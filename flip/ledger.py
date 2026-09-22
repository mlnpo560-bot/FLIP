from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
import hashlib, json

@dataclass(frozen=True)
class Transaction:
    sender: str
    recipient: str
    amount: Decimal
    nonce: int
    signature: str = ""

    def payload(self) -> bytes:
        return json.dumps({
            "sender": self.sender, "recipient": self.recipient,
            "amount": str(self.amount), "nonce": self.nonce
        }, sort_keys=True, separators=(",", ":")).encode()

    def txid(self) -> str:
        return hashlib.sha256(self.payload()).hexdigest()

@dataclass
class LedgerAccount:
    balance: Decimal = Decimal("0")
    nonce: int = 0

class LedgerError(ValueError):
    pass

class NativeLedger:
    """Deterministic single-state-machine prototype for native FLIP money."""
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

    def apply(self, tx: Transaction, verify_signature) -> str:
        if tx.amount <= 0:
            raise LedgerError("amount must be positive")
        if tx.sender == tx.recipient:
            raise LedgerError("self-transfer")
        if tx.nonce < 0:
            raise LedgerError("invalid nonce")
        txid = tx.txid()
        if txid in self.seen:
            raise LedgerError("replay")
        if not verify_signature(tx):
            raise LedgerError("invalid signature")

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
        return {a: {"balance": str(v.balance), "nonce": v.nonce)
                for a, v in sorted(self.accounts.items())}
