import hashlib
import uuid


def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha512((password + salt).encode()).hexdigest()
