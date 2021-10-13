# FastAPI's jsonable_encoder handles converting various non-JSON types,
# such as datetime between JSON types and native Python types.
from fastapi.encoders import jsonable_encoder
# Pydantic, and Python's built-in typing are used to define a schema
# that defines the structure and types of the different objects stored
# in the recipes collection, and managed by this API.
from typing import List

class User():
    def __init__(self, form):
        self.email = form["email"]
        self.password = form["password"]
        self.name = form["username"]
    
    def complete(self):
        if self.name == "":
            return False
        elif self.email == "":
            return False
        elif self.password == "":
            return False
        else:
            return True

def register_user(form):
    user = {
        "email": form["email"],
        "password": form["password"],
        "name": form["username"]
    }
    validate_user(user, email=True)
    return user

def login_user(form):
    user = {
        "email": form["email"],
        "password": form["password"],
        "name": form["username"]
    }
    validate_user(user, email=False)
    return user

def validate_user(user, email=False):
    if user["name"] == "":
        return False
    if user["password"] == "":
        return False
    if user["email"] == "" and email == True:
        return False
