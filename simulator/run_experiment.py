from decimal import Decimal as D
from pathlib import Path
from random import Random
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from flip.monetary import MonetaryEngine, OracleAggregator

def main():
    rng = Random(20260922)
    oracle = OracleAggregator(minimum_quorum=5, max_step=D("0.10"))
    engine = MonetaryEngine()
    engine.set_accounts({"alice": D("600"), "bob": D("300"), "carol": D("100")})
    market_price = D("1")
    print("epoch,index,total_supply,market_price")
    for epoch in range(1, 21):
        benchmark = D("1") + D(str(epoch)) / D("100")
        observations = []
        for _ in range(7):
            noise = D(str(rng.uniform(-0.015, 0.015)))
            observations.append(max(D("0.01"), benchmark * (D("1") + noise)))
        if epoch == 10:
            market_price *= D("0.55")
        else:
            market_price *= D(str(1 + rng.uniform(-0.04, 0.05)))
        engine.reexpress(oracle.aggregate(engine.index, observations))
        print(f"{epoch},{engine.index:.8f},{engine.total_supply():.8f},{market_price:.8f}")

if __name__ == "__main__":
    main()
