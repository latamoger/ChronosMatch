from collections import defaultdict, deque


class MatchingEngine:
    def __init__(self):
        self.buy_orders = defaultdict(deque)
        self.sell_orders = defaultdict(deque)
        self.trades = []
        self.next_order_id = 1

    def submit_order(self, side, price, quantity):
        side = side.upper()

        if side not in ("BUY", "SELL"):
            raise ValueError("Invalid order side")

        if price <= 0 or quantity <= 0:
            raise ValueError("Price and quantity must be positive")

        order_id = self.next_order_id
        self.next_order_id += 1

        order = {
            "id": order_id,
            "side": side,
            "price": price,
            "quantity": quantity
        }

        opposite = (
            self.sell_orders
            if side == "BUY"
            else self.buy_orders
        )

        while order["quantity"] > 0 and opposite:
            best_price = (
                min(opposite)
                if side == "BUY"
                else max(opposite)
            )

            if side == "BUY" and price < best_price:
                break

            if side == "SELL" and price > best_price:
                break

            resting = opposite[best_price][0]

            traded = min(
                order["quantity"],
                resting["quantity"]
            )

            self.trades.append({
                "price": best_price,
                "quantity": traded,
                "buy_order_id": (
                    order_id if side == "BUY"
                    else resting["id"]
                ),
                "sell_order_id": (
                    order_id if side == "SELL"
                    else resting["id"]
                )
            })

            order["quantity"] -= traded
            resting["quantity"] -= traded

            if resting["quantity"] == 0:
                opposite[best_price].popleft()

            if not opposite[best_price]:
                del opposite[best_price]

        if order["quantity"] > 0:
            book = (
                self.buy_orders
                if side == "BUY"
                else self.sell_orders
            )
            book[price].append(order)

        return order_id

    def get_trades(self):
        return self.trades

    def get_order_book(self):
        return {
            "BUY": [
                {"price": p, "quantity": sum(o["quantity"] for o in q)}
                for p, q in sorted(
                    self.buy_orders.items(), reverse=True
                )
            ],
            "SELL": [
                {"price": p, "quantity": sum(o["quantity"] for o in q)}
                for p, q in sorted(self.sell_orders.items())
            ]
        }