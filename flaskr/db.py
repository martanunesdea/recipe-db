from flask import g, current_app
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

def get_db():
    pymongo = PyMongo(current_app)
    g.db = pymongo.db
    return pymongo.db

def init_app(app):
    db = PyMongo(app, uri=app.config["URI"])
    return db

###############
#### USERS ####
###############
def get_user_by_name(name):
    db = get_db()
    users = db["users"]
    user = users.find_one({ "name": name})
    return user

def get_user_by_id(id):
    db = get_db()
    users = db["users"]
    user = users.find_one({"_id": ObjectId(id)})
    return user

def add_user(user):
    db = get_db()
    users = db["users"]
    result = users.insert_one({"name": user["name"], "password": user["password"], "email": user["password"]})
    print(result)

def is_email_available(email):
    pass


###############
### RECIPES ###
###############
def db_get_recipes():
    return  get_db()["recipes"].find()

def db_lookup_id(id):
    return get_db()["recipes"].find( { "id": id } )

def db_lookup_name(in_name):
    recipes = get_db()["recipes"].find( { "title": in_name } )
    return recipes
    
def insert_recipe(item):
    dbname = get_db()
    collection_name = dbname["recipes"]
    result = collection_name.insert(item)
    print(result)

def db_update(id, title, ingredients, instructions):
    result = get_db()["recipes"].update_one({"id": id}, {"$set": {"id": id, "title": title, "ingredients": ingredients, "instructions": instructions}})
    print(result)
    return result

def db_delete(id):
    result = get_db()["recipes"].delete_one({"id": id})
    if result.deleted_count == 1: 
        return True
    else:
        return False


    
