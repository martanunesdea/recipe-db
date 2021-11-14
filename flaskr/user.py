# FastAPI's jsonable_encoder handles converting various non-JSON types,
# such as datetime between JSON types and native Python types.
from fastapi.encoders import jsonable_encoder
# Pydantic, and Python's built-in typing are used to define a schema
# that defines the structure and types of the different objects stored
# in the recipes collection, and managed by this API.
from typing import List
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.recipe import recipe_update

from .db import db_is_email_available, db_add_user, db_get_user

def user_validate(form):
    user = {
        "email": form["email"],
        "password": form["password"],
        "name": form["username"]
    }
    if user_details_correct(user) == False:
        return False
    if db_is_email_available(user["email"]) == False:
        return False

    return

def user_register(form):
    user = {
        "email": form["email"],
        "password": form["password"],
        "name": form["username"]
    }
    user["password"] = generate_password_hash(form["password"])
    return db_add_user(user)

def user_authenticate(form):
    input = {
        "password": form["password"],
        "name": form["username"]
    }
    # check for dangerous inputs...
    if input["name"] == "" or input["password"] == "":
        print("Incorrect input details")
        return None
        
    # inputs are OK, let's check if user exists...    
    user = db_get_user("name", input["name"])
    if user is None:
        print("Couldn't get user")
        return None
    elif user_check_password(user, input["password"]) == True:
        return user

    return None

def user_check_password(user, input_password):
    if check_password_hash(user['password'], input_password):
        return True
    else:
        return False
    
def user_login(user):
    session.clear()
    session['user_id'] = str(user['_id'])

def user_details_correct(user):
    if user["name"] == "":
        return False
    if user["password"] == "":
        return False
    if user["email"] == "":
        return False

def user_get_user_by_id(user_id):
    return db_get_user("_id", (user_id))