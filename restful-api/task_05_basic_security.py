#!/usr/bin/python3
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity 


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your-secret-key"
jwt = JWTManager(app)

auth = HTTPBasicAuth()

users = {
   "user1": {
       "username": "user1",
       "password": generate_password_hash("password"),
       "role": "user"
   },
   "admin1": {
       "username": "admin1",
       "password": generate_password_hash("password"),
       "role": "admin"
}
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        stored_password = users[username]["password"]
        return check_password_hash(stored_password, password)
    return False

@app.route("/")
def home():
  return "Welcome to Flask API!"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity={"username": username, "role": users[username]["role"]})
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
