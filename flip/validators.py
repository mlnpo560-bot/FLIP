from __future__ import annotations
from dataclasses import dataclass
from .crypto import KeyPair

class ValidatorError(ValueError): pass
@dataclass(frozen=True)
class Validator:
    address:str; public_key:bytes; power:int=1; active:bool=True
class ValidatorSet:
    def __init__(self,validators:list[Validator]):
        if not validators or any(v.power<=0 for v in validators): raise ValidatorError("invalid validator set")
        if len({v.address for v in validators})!=len(validators): raise ValidatorError("duplicate validator")
        self._v={v.address:v for v in validators}
    def snapshot(self): return tuple(self._v[a] for a in sorted(self._v))
    def addresses(self): return set(self._v)
    def add(self,v:Validator):
        if v.address in self._v: raise ValidatorError("validator exists")
        self._v[v.address]=v
    def remove(self,address:str):
        if address not in self._v: raise ValidatorError("unknown validator")
        del self._v[address]
    def total_power(self): return sum(v.power for v in self._v.values() if v.active)
