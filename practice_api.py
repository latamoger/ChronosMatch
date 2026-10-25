from flask import Flask, request, jsonify
from matching_engine import MatchingEngine

app = Flask(__name__)
engine = MatchingEngine()


@app.route("/")
def home():
    return jsonify({"message": "ChronosMatch API is running"})


@app.route("/orders", methods=["POST"])
def submit_order():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON body"}), 400

    try:
        order_id = engine.submit_order(
            data["side"],
            data["price"],
            data["quantity"]
        )
        return jsonify({
            "message": "Order submitted successfully",
            "order_id": order_id
        }), 201

    except (ValueError, KeyError, TypeError, AttributeError) as error:
        return jsonify({"error": str(error)}), 400


@app.route("/trades", methods=["GET"])
def get_trades():
    return jsonify(engine.get_trades())


@app.route("/orderbook", methods=["GET"])
def get_orderbook():
    return jsonify(engine.get_order_book())


if __name__ == "__main__":
    app.run(debug=True)