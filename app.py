from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 1
@app.route("/users", methods=["GET"])
def fn_get_user():
    return jsonify({
        "payload": "success"
    })

# 2
@app.route("/user", methods=["POST"])
def fn_post_user():
    return jsonify({
        "payload": "success"
    })

# 3
@app.route("/user", methods=["DELETE"])
def fn_del_user():
    return jsonify({
        "payload": "success"
    })

# 4
@app.route("/user", methods=["PUT"])
def fn_put_user():
    return jsonify({
        "payload": "success",
        "error": False
    })

# 5
@app.route("/api/v1/user", methods=["GET"])
def api_get_user():
    return jsonify({
        "payload": []
    })

# 6
@app.route("/api/v1/user", methods=["POST"])
def api_post_user():
    email = request.args.get("email")
    name = request.args.get("name")
    return jsonify({
        "payload": {
            "email": email,
            "name": name
        }
    })

# 7
@app.route("/api/v1/user/add", methods=["POST"])
def api_post_add_user():
    email = request.args.get("email")
    name = request.args.get("name")
    id = request.args.get("id")
    return jsonify({
        "payload": {
            "email": email,
            "name": name,
            "id": id
        }
    })

# 8
@app.route("/api/v1/user/create", methods=["POST"])
def api_post_create_user():
    data = request.get_json()
    return jsonify({
        "payload": {
            "email": data["email"],
            "name": data["name"],
            "id": data["id"]
        }
    })

if __name__ == "__main__":
    app.run(debug=True)