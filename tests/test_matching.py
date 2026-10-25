import unittest
from matching_engine import MatchingEngine


class TestMatchingEngine(unittest.TestCase):

    def setUp(self):
        self.engine = MatchingEngine()

    # Test 1: Buy and Sell Matching
    def test_buy_sell_matching(self):
        self.engine.submit_order("BUY", 100, 10)
        self.engine.submit_order("SELL", 100, 5)

        trades = self.engine.get_trades()

        self.assertEqual(len(trades), 1)
        self.assertEqual(trades[0]["quantity"], 5)
        print("Buy and Sell Matching: PASSED")

    # Test 2: Partial Order Fill
    def test_partial_fill(self):
        self.engine.submit_order("BUY", 100, 10)
        self.engine.submit_order("SELL", 100, 4)

        book = self.engine.get_order_book()

        self.assertEqual(book["BUY"][0]["quantity"], 6)
        print("Partial Order Fill: PASSED")

    # Test 3: Price Priority
    def test_price_priority(self):
        self.engine.submit_order("SELL", 102, 5)
        self.engine.submit_order("SELL", 101, 5)
        self.engine.submit_order("BUY", 105, 5)

        trades = self.engine.get_trades()

        self.assertEqual(trades[0]["price"], 101)
        print("Price Priority: PASSED")

    # Test 4: Time Priority
    def test_time_priority(self):
        first_id = self.engine.submit_order("SELL", 100, 5)
        self.engine.submit_order("SELL", 100, 5)
        self.engine.submit_order("BUY", 100, 5)

        trades = self.engine.get_trades()

        self.assertEqual(
            trades[0]["sell_order_id"],
            first_id
        )
        print("Time Priority: PASSED")

    # Test 5: Invalid Quantity
    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.engine.submit_order("BUY", 100, 0)

        print("Invalid Quantity: PASSED")

    # Test 6: Negative Price
    def test_negative_price(self):
        with self.assertRaises(ValueError):
            self.engine.submit_order("BUY", -100, 5)

        print("Negative Price: PASSED")

    # Test 7: Unmatched Orders
    def test_unmatched_orders(self):
        self.engine.submit_order("BUY", 90, 10)
        self.engine.submit_order("SELL", 100, 5)

        trades = self.engine.get_trades()

        self.assertEqual(len(trades), 0)
        print("Unmatched Orders: PASSED")


if __name__ == "__main__":
    unittest.main(verbosity=2)