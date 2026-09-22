from __future__ import annotations
from dataclasses import dataclass
import hashlib,json
@dataclass(frozen=True)
class GenesisConfig:
    chain_id:str
    genesis_time:int
    genesis_hash:str
    initial_supply:str
    validators:tuple[str,...]
    def canonical(self)->bytes:return json.dumps(self.__dict__,sort_keys=True,separators=(",",":")).encode()
    def verify(self)->bool:return hashlib.sha256(self.canonical()).hexdigest()==self.genesis_hash
def make_genesis(chain_id,time,initial_supply,validators):
    g=GenesisConfig(chain_id,time,"",str(initial_supply),tuple(sorted(validators)))
    return GenesisConfig(g.chain_id,g.genesis_time,hashlib.sha256(g.canonical()).hexdigest(),g.initial_supply,g.validators)
