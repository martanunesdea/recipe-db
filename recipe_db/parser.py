from .db import db_get_all, db_lookup_name

def parse(ingredient):
    result = db_lookup_name(ingredient)
    return result


def load_recipes():
    result = db_get_all()
    return result

def save_recipe(text):
    return("OK")