"""
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
"""

import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def db_lookup(table, param, input_param):
    query = f"SELECT * FROM {table} WHERE {param} = ?;"
    record = get_db().execute(query, (input_param,)).fetchone()
    return record

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
    db = get_db()
    recipes = db.execute(
        'SELECT id, title, ingredients, instructions FROM recipes'
    ).fetchall()

    return  recipes

def db_text_search(input_param):
    results = list()
    for doc in get_db()["recipes"].find({"$text": {"$search": input_param}}) :
        results.append(doc)
    return results


def db_insert_recipe(item):
    db = get_db()
    query = "INSERT INTO recipes (title, ingredients, instructions) VALUES (?, ?, ?);"
    db.cursor().execute(query, (item["title"], item["ingredients"], item["instructions"]))
    db.commit()
       

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


    
