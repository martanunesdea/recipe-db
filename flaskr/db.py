import pymongo
import click
from flask import g
from flask.cli import with_appcontext

def get_db():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://cooluser:password12345@cluster0.sbchk.mongodb.net/recipe-db?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = pymongo.MongoClient(CONNECTION_STRING)

    return client['recipe-db']

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    pass


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def compile_items(*args):
    items = []
    for item in args:
        items.append(item)
        print(item)
    return items

def insert_items(items):
    dbname = get_db()
    collection_name = dbname["recipes"]
    collection_name.insert_many(items)
    
def db_insert(item):
    dbname = get_db()
    collection_name = dbname["recipes"]
    result = collection_name.insert(item)
    print(result)
    
def db_get_all():
    dbname = get_db()
    
    collection_name = dbname["recipes"]
   
    recipes = collection_name.find()
    text = ""
    for recipe in recipes:
        for k, val in recipe.items():
            if k == "_id":
                pass
            if k == "name":
                line = f'\nTitle: {val}\n'
                text = text + line
            if k == "ingredients":
                pass
            # TODO check if tags is list, if so print as list
            if k == "tags":
                line = f'Categories: {val}\n'
                text = text + line
    return text
   
def db_get_recipes():
    dbname = get_db()
    collection_name = dbname["recipes"]
    recipes = collection_name.find()
    list = []
    for recipe in recipes:
        for k, val in recipe.items():
            if k == "id":
                this_id = val
            if k == "name":
                this_name = val
            if k == "ingredients":
                this_ingredients = val
            # TODO check if tags is list, if so print as list
            if k == "tags":
                this_tags = val
        entry = {"id": this_id, "title": this_name, "ingredients": this_ingredients, "tags": this_tags}
        list.append(entry)
    return list

def db_lookup_id(id):
    dbname = get_db()
    collection_name = dbname["recipes"]
    recipe = collection_name.find( { "id": id } )
    for entry in recipe:
        for k, val in entry.items():
            if k == "id":
                this_id = val
            if k == "name":
                this_name = val
            if k == "ingredients":
                this_ingredients = val
            # TODO check if tags is list, if so print as list
            if k == "tags":
                this_tags = val
        entry = {"id": this_id, "title": this_name, "ingredients": this_ingredients, "tags": this_tags}
    return entry

def db_lookup_name(in_name):
    dbname = get_db()
    
    collection_name = dbname["recipes"]

    # TODO search with regex
    recipes = collection_name.find( { "name": in_name } )
    text = ""
    for entry in recipes:
        for k, val in entry.items():
            if k == "_id":
                pass
            if k == "name":
                line = f'\nTitle: {val}\n'
                text = text + line
            if k == "ingredients":
                line = f'Ingredients:\n'
                text = text + line
                for ing in val:
                    line = f'{ing}\n'
                    text = text + line
            # TODO check if tags is list, if so print as list
            if k == "tags":
                line = f'Categories: {val}\n'
                text = text + line
        
    return text