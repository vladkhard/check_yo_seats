import uuid

from fastapi import FastAPI

import db
from models import User
from tools import hash_password


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/users")
async def post_user(user: User):
    user.password = hash_password(user.password)
    db.post(user)
    return user.dict(exclude={"password"}) | {"_id": user._id.hex}

@app.get("/users/{user_id}")
async def get_user(user_id: uuid.UUID):
    user = db.get(User, user_id.hex)
    return user.json(exclude={"password"})
