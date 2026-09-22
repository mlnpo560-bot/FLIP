from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal

class IssuanceError(ValueError):pass
@dataclass(frozen=True)
class IssuancePolicy:
    max_supply:Decimal
    initial_supply:Decimal=Decimal("0")
    epoch_mint_limit:Decimal=Decimal("0")
    def __post_init__(self):
        if self.max_supply<0 or self.initial_supply<0 or self.epoch_mint_limit<0 or self.initial_supply>self.max_supply:raise IssuanceError("invalid issuance policy")

@dataclass
class IssuanceState:
    total_supply:Decimal
    epoch_minted:Decimal=Decimal("0")

class Issuer:
    def __init__(self,policy:IssuancePolicy):
        self.policy=policy;self.state=IssuanceState(policy.initial_supply)
    def mint(self,amount:Decimal)->Decimal:
        amount=Decimal(amount)
        if amount<=0:raise IssuanceError("mint amount must be positive")
        if self.state.epoch_minted+amount>self.policy.epoch_mint_limit:raise IssuanceError("epoch mint limit exceeded")
        if self.state.total_supply+amount>self.policy.max_supply:raise IssuanceError("max supply exceeded")
        self.state.total_supply+=amount;self.state.epoch_minted+=amount
        return self.state.total_supply
    def begin_epoch(self):self.state.epoch_minted=Decimal("0")
