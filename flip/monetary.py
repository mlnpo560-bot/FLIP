from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, getcontext
from statistics import median
from typing import Iterable, Mapping

getcontext().prec = 50
D = Decimal

@dataclass(frozen=True)
class Account:
    address: str
    balance: Decimal

class OracleAggregator:
    """Deterministic median oracle with quorum and step checks."""
    def __init__(self, minimum_quorum: int = 3, max_step: Decimal = D("0.25")):
        if minimum_quorum < 1:
            raise ValueError("minimum_quorum must be positive")
        if max_step <= 0:
            raise ValueError("max_step must be positive")
        self.minimum_quorum = minimum_quorum
        self.max_step = D(str(max_step))

    def aggregate(self, previous_index: Decimal, observations: Iterable[Decimal]) -> Decimal:
        previous_index = D(str(previous_index))
        values = [D(str(v)) for v in observations]
        if len(values) < self.minimum_quorum:
            raise ValueError("insufficient oracle quorum")
        if previous_index <= 0 or any(v <= 0 for v in values):
            raise ValueError("index and observations must be positive")
        candidate = D(str(median(values)))
        upper = previous_index * (D("1") + self.max_step)
        return max(previous_index, min(candidate, upper))

class MonetaryEngine:
    """Reference-index and proportional balance re-expression."""
    def __init__(self, initial_index: Decimal = D("1")):
        initial_index = D(str(initial_index))
        if initial_index <= 0:
            raise ValueError("initial_index must be positive")
        self.index = initial_index
        self.accounts: dict[str, Decimal] = {}
        self.epoch = 0

    def set_accounts(self, accounts: Mapping[str, Decimal]) -> None:
        clean = {}
        for address, balance in accounts.items():
            b = D(str(balance))
            if b < 0:
                raise ValueError("balances cannot be negative")
            clean[address] = b
        self.accounts = clean

    def total_supply(self) -> Decimal:
        return sum(self.accounts.values(), D("0"))

    def ownership_shares(self) -> dict[str, Decimal]:
        total = self.total_supply()
        if total == 0:
            return {a: D("0") for a in self.accounts}
        return {a: b / total for a, b in self.accounts.items()}

    def reexpress(self, new_index: Decimal) -> Decimal:
        new_index = D(str(new_index))
        if new_index <= 0 or new_index < self.index:
            raise ValueError("reference index must remain positive and non-decreasing")
        ratio = new_index / self.index
        self.accounts = {a: b * ratio for a, b in self.accounts.items()}
        self.index = new_index
        self.epoch += 1
        return ratio
