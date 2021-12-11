from flask import g, current_app
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

def get_db():
    if 'db' not in g:
        pymongo = PyMongo(current_app)
        g.db = pymongo.db
    return g.db

def init_app(app):
    db = PyMongo(app, uri=app.config["URI"])
    return db

###############
#### USERS ####
###############
def db_get_user(n, param):
    db = get_db()
    users = db["users"]
    if n == "_id":
        user = users.find_one({ n: ObjectId(param)})
    else:
        user = users.find_one({ n: param})
    # note that user is None if no results were found
    return user

def db_add_user(user):
    db = get_db()
    users = db["users"]
    result = users.insert_one({"name": user["name"], "password": user["password"], "email": user["email"]})
    return True

def db_is_email_available(email):
    db = get_db()
    users = db["users"]
    if users.find_one({"email": email}) is not None:
        return False
    else:
        return True

###############
### RECIPES ###
###############
def db_get_recipes():
    return  get_db()["recipes"].find()

def db_lookup(param, input_param):
    return get_db()["recipes"].find( {param: input_param})
    
def db_insert_recipe(item):
    dbname = get_db()
    collection_name = dbname["recipes"]
    last_id = collection_name.find_one(sort=[("id", -1)])["id"]
    item["id"] = last_id + 1
    collection_name.insert(item)
    

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


    
