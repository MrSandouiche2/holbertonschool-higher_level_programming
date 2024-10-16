from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
}

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(users)

@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.get_json()
    username = new_user['username']
    users[username] = new_user
    return jsonify(users), 201

if __name__ == '__main__':
    app.run(debug=True)
