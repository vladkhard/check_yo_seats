import json
import uuid


class User:
    table_name: str = "user"

    _id: uuid.UUID
    name: str
    email: str
    password: str = None
    friends: list[uuid.UUID] = []
    added_places: list[uuid.UUID] = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self._id = uuid.uuid4().hex

    def to_json(self):
        return json.dumps({
            "name": self.name,
            "email": self.email,
            "friends": self.friends,
            "added_places": self.added_places,
        })
    
    def to_dict(self):
        return {
            "_id": self._id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "friends": self.friends,
            "added_places": self.added_places,
        }
