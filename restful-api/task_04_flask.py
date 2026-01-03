#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
