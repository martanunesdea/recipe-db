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

#TODO: def db_insert (table, list_params, input_params)

###############
#### USERS ####
###############
def db_get_user(n, param):
    user = db_lookup ("users", n, param)
    return user

def db_add_user(user):
    db = get_db()
    query = "INSERT INTO users (username, password, email) VALUES (?, ?, ?);"
    db.cursor().execute(query, (user["name"], user["password"], user["email"]))
    db.commit()

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
    results = search_string_in_table ("recipes", input_param)
    return results

def search_string_in_table(table_name, search_string):
    query = f"SELECT * FROM {table_name} WHERE title LIKE ? OR ingredients LIKE ? OR instructions LIKE ? OR tags LIKE ?;"
    records = get_db().execute(query, ('%' + search_string + '%','%' + search_string + '%','%' + search_string + '%','%' + search_string + '%')).fetchall()
    return records


def db_insert_recipe(item):
    db = get_db()
    query = "INSERT INTO recipes (title, ingredients, instructions, tags) VALUES (?, ?, ?, ?);"
    db.cursor().execute(query, (item["title"], item["ingredients"], item["instructions"], item["tags"]))
    db.commit()
       

def db_update(id, title, ingredients, instructions):
    db = get_db()
    query = f"UPDATE recipes SET ingredients = ?, instructions = ? WHERE title = ?;"
    val = (ingredients, instructions, title)
    db.cursor().execute(query, val)
    db.commit()

def db_delete(id):
    db = get_db()
    query = f"DELETE FROM recipes WHERE id = ?;"
    db.cursor().execute(query, (id,))
    db.commit()
    return True
    
