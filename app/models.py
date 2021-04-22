import uuid

from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    _table_name = "user"
    
    @property
    def table_name(self):
        return self._table_name

    _id: uuid.UUID = uuid.uuid4()
    name: str
    email: EmailStr
    friends: list[uuid.UUID] = Field(default_factory=lambda: [])
    added_places: list[uuid.UUID] = Field(default_factory=lambda: [])
    password: str
