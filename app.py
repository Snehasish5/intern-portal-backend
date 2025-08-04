import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json

# Compute absolute frontend path
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend"))
app = Flask(__name__, static_folder=frontend_path, static_url_path="")
CORS(app)

# Serve index.html at root
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/dashboard.html")
def serve_dashboard():
    return send_from_directory(app.static_folder, "dashboard.html")

@app.route("/leaderboard.html")
def serve_leaderboard():
    return send_from_directory(app.static_folder, "leaderboard.html")

# Serve static files like JS/CSS
@app.route("/<path:path>")
def serve_static_file(path):
    return send_from_directory(app.static_folder, path)

# API: Intern data
@app.route("/api/intern")
def intern_data():
    json_path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(json_path, "r") as file:
        data = json.load(file)
    return jsonify(data)

# API: Leaderboard data
@app.route("/api/leaderboard")
def leaderboard():
    return jsonify([
        {"name": "Snehasish", "donations": 1200},
        {"name": "Riya", "donations": 950},
        {"name": "Amit", "donations": 870}
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)