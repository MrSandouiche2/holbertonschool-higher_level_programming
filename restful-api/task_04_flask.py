from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
}

@app.route("/")
def hello_world():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_users():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    if request.is_json:
        data = request.get_json()

        username = data.get("username")
        name = data.get("name")
        age = data.get("age")
        city = data.get("city")

        if not username:
            return jsonify({"error": "Username is required"}), 400

        if username in users:
            return jsonify({"error": "Username already exists"}), 400

        users[username] = {"username": username, "name": name, "age": age, "city": city}

        return jsonify({"message": "User added", "user": users[username]}), 201
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == "__main__":
    app.run(debug=True)
