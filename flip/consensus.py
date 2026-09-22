from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Vote:
    height: int
    block_hash: str
    validator: str

class ConsensusError(ValueError):
    pass

class QuorumCertificate:
    """Minimal deterministic quorum model for testnet research.

    This is not a production Byzantine consensus protocol.
    """
    def __init__(self, validators: set[str], quorum: int):
        if quorum <= 0 or quorum > len(validators):
            raise ConsensusError("invalid quorum")
        self.validators = frozenset(validators)
        self.quorum = quorum

    def finalize(self, votes: list[Vote], height: int, block_hash: str) -> bool:
        unique = {v.validator for v in votes
                  if v.height == height and v.block_hash == block_hash
                  and v.validator in self.validators}
        return len(unique) >= self.quorum
