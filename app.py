from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
import json

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)

# Route to serve static frontend pages
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/dashboard.html")
def serve_dashboard():
    return send_from_directory(app.static_folder, "dashboard.html")

@app.route("/leaderboard.html")
def serve_leaderboard():
    return send_from_directory(app.static_folder, "leaderboard.html")

# API to return intern data from data.json
@app.route("/api/intern")
def intern_data():
    json_path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(json_path, "r") as file:
        data = json.load(file)
    return jsonify(data)

# API for dummy leaderboard (can be made dynamic later)
@app.route("/api/leaderboard")
def leaderboard():
    return jsonify([
        {"name": "Snehasish", "donations": 1200},
        {"name": "Riya", "donations": 950},
        {"name": "Amit", "donations": 870}
    ])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)