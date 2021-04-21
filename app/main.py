from flask import Flask, request

import db
from models import User


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/users/<int:_id>")
def get_user(_id: int, methods=["GET"]):
    data = db.get(User, _id)
    return data

@app.route("/users", methods=["POST"])
def post_user():
    data = request.json
    user = User(**data)
    db.post(user)
    return user.to_json()
