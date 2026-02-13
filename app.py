from flask import Flask, jsonify, request
from app.db import DB
from app.services import create_new_exchange

app = Flask(__name__)
database = DB()


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the API"})

@app.route("/exchanges", methods=["POST"])
def build_new_exchange():
    exchange = create_new_exchange(database)
    if not exchange:
        return jsonify({"message": "Unable to create"})
    return jsonify({"exchange_id" : exchange.id})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)