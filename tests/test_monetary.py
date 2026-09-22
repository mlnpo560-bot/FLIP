from decimal import Decimal as D
import unittest
from flip.monetary import MonetaryEngine, OracleAggregator

class MonetaryTests(unittest.TestCase):
    def test_index_never_decreases(self):
        engine = MonetaryEngine()
        engine.set_accounts({"a": D("60"), "b": D("40")})
        for value in [D("1.10"), D("0.90"), D("1.20"), D("1.15")]:
            if value >= engine.index:
                engine.reexpress(value)
            self.assertGreaterEqual(engine.index, D("1"))

    def test_share_preservation(self):
        engine = MonetaryEngine()
        engine.set_accounts({"a": D("60"), "b": D("30"), "c": D("10")})
        before = engine.ownership_shares()
        engine.reexpress(D("1.25"))
        self.assertEqual(before, engine.ownership_shares())

    def test_reexpression_ratio(self):
        engine = MonetaryEngine()
        engine.set_accounts({"a": D("100")})
        ratio = engine.reexpress(D("1.50"))
        self.assertEqual(ratio, D("1.5"))
        self.assertEqual(engine.accounts["a"], D("150"))

    def test_decrease_is_rejected(self):
        engine = MonetaryEngine()
        engine.set_accounts({"a": D("10")})
        with self.assertRaises(ValueError):
            engine.reexpress(D("0.9"))

    def test_oracle_quorum(self):
        oracle = OracleAggregator(minimum_quorum=3)
        with self.assertRaises(ValueError):
            oracle.aggregate(D("1"), [D("1.01"), D("1.02")])

    def test_median_resists_one_extreme_value(self):
        oracle = OracleAggregator(minimum_quorum=5, max_step=D("0.50"))
        value = oracle.aggregate(D("1"), [D("1.05"), D("1.06"), D("1.04"), D("999"), D("1.05")])
        self.assertLess(value, D("1.10"))

    def test_nonpositive_oracle_value_rejected(self):
        oracle = OracleAggregator(minimum_quorum=3)
        with self.assertRaises(ValueError):
            oracle.aggregate(D("1"), [D("1"), D("0"), D("1")])

if __name__ == "__main__":
    unittest.main()
