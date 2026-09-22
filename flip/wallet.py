from decimal import Decimal
from .crypto import KeyPair
from .transaction import Transaction

class Wallet:
    def __init__(self, key=None):
        self.key = key or KeyPair.generate()

    @property
    def address(self) -> str:
        return self.key.address

    def sign_transfer(self, recipient: str, amount: Decimal, nonce: int) -> Transaction:
        return Transaction.sign(self.key, recipient, amount, nonce)
