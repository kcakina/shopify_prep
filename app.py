from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the API"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)