import unittest
from practice_api import app, MatchingEngine
import practice_api


class TestChronosMatchAPI(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
        practice_api.engine = MatchingEngine()

    # Test 1: Home API
    def test_home(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["message"],
            "ChronosMatch API is running"
        )

    # Test 2: Submit Buy Order
    def test_buy_order(self):
        response = self.client.post("/orders", json={
            "side": "BUY",
            "price": 100,
            "quantity": 10
        })

        self.assertEqual(response.status_code, 201)
        self.assertIn("order_id", response.get_json())

    # Test 3: Submit Sell Order
    def test_sell_order(self):
        response = self.client.post("/orders", json={
            "side": "SELL",
            "price": 100,
            "quantity": 5
        })

        self.assertEqual(response.status_code, 201)

    # Test 4: Invalid Quantity
    def test_invalid_quantity(self):
        response = self.client.post("/orders", json={
            "side": "BUY",
            "price": 100,
            "quantity": 0
        })

        self.assertEqual(response.status_code, 400)

    # Test 5: Negative Price
    def test_negative_price(self):
        response = self.client.post("/orders", json={
            "side": "BUY",
            "price": -100,
            "quantity": 5
        })

        self.assertEqual(response.status_code, 400)

    # Test 6: Trade History
    def test_trade_history(self):
        self.client.post("/orders", json={
            "side": "BUY",
            "price": 100,
            "quantity": 10
        })

        self.client.post("/orders", json={
            "side": "SELL",
            "price": 100,
            "quantity": 5
        })

        response = self.client.get("/trades")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    # Test 7: Order Book
    def test_orderbook(self):
        response = self.client.get("/orderbook")

        self.assertEqual(response.status_code, 200)
        self.assertIn("BUY", response.get_json())
        self.assertIn("SELL", response.get_json())


if __name__ == "__main__":
    unittest.main(verbosity=2)